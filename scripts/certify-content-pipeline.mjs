import fs from 'node:fs/promises';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';

const ROOT = process.cwd();
const PART_DIR = path.join(ROOT, 'catalog-seed-parts');
const SOURCE_DIR = path.join(ROOT, 'content-source');
const DB_DIR = path.join(ROOT, 'content-db');
const EVIDENCE_DIR = path.join(ROOT, 'evidence', 'content-pipeline');
const PARTS = [0, 1, 2, 3, 4].map(i => path.join(PART_DIR, `phase1-7.${String(i).padStart(2, '0')}.txt`));

const fail = message => { throw new Error(message); };
const sha256 = value => crypto.createHash('sha256').update(value).digest('hex');
const readJson = async file => JSON.parse(await fs.readFile(file, 'utf8'));

function decodeBase64Strict(text, label) {
  const compact = String(text).replace(/\s/g, '');
  if (!compact) fail(`${label} is empty.`);
  if (!/^[A-Za-z0-9+/=]+$/.test(compact)) fail(`${label} contains non-Base64 characters.`);
  if (compact.length % 4 === 1) fail(`${label} has an invalid Base64 length.`);
  const bytes = Buffer.from(compact, 'base64');
  if (!bytes.length) fail(`${label} decoded to an empty buffer.`);
  return bytes;
}

async function certifySeedArchive() {
  const fragments = [];
  const fragmentEvidence = [];
  for (const [index, file] of PARTS.entries()) {
    const encoded = await fs.readFile(file, 'utf8');
    const bytes = decodeBase64Strict(encoded, `Seed fragment ${index}`);
    fragments.push(bytes);
    fragmentEvidence.push({
      path: path.relative(ROOT, file).replaceAll(path.sep, '/'),
      encodedBytes: Buffer.byteLength(encoded),
      decodedBytes: bytes.length,
      sha256: sha256(bytes)
    });
  }

  const archive = Buffer.concat(fragments);
  if (archive[0] !== 0x1f || archive[1] !== 0x8b) fail('Recovered Phase 1–7 archive does not have a gzip header.');

  let payload;
  try {
    payload = JSON.parse(zlib.gunzipSync(archive).toString('utf8'));
  } catch (error) {
    fail(`Recovered Phase 1–7 archive is invalid: ${error.message}`);
  }
  if (!Array.isArray(payload.records) || payload.records.length < 1000) {
    fail(`Recovered Phase 1–7 inventory is incomplete: ${payload.records?.length ?? 0} records.`);
  }

  return {
    fragmentEvidence,
    archiveBytes: archive.length,
    archiveSha256: sha256(archive),
    inventoryRecords: payload.records.length,
    inventorySha256: sha256(JSON.stringify(payload))
  };
}

async function certifyCanonicalSource() {
  const file = path.join(SOURCE_DIR, 'phase-1-8-canonical-objects.json');
  const payload = await readJson(file);
  if (payload.format !== 'multiversal-content-source-bundle') fail('Canonical source has an unexpected format.');
  if (!Array.isArray(payload.records) || payload.records.length !== 487) {
    fail(`Canonical source must contain 487 records; found ${payload.records?.length ?? 0}.`);
  }
  return { records: payload.records.length, sha256: sha256(JSON.stringify(payload)) };
}

async function certifyGeneratedDatabase(seed, source) {
  const index = await readJson(path.join(DB_DIR, 'index.json'));
  const manifest = await readJson(path.join(DB_DIR, 'manifest.json'));
  if (index.format !== 'multiversal-content-database') fail('Generated index format is invalid.');
  if (!Array.isArray(index.records)) fail('Generated index has no records array.');
  if (index.recordCount !== index.records.length) fail('Generated index recordCount does not match records length.');
  if (manifest.recordCount !== index.recordCount) fail('Manifest and index record counts do not match.');
  if (index.recordCount < seed.inventoryRecords) fail('Generated database lost recovered inventory records.');
  if ((index.summary?.fullObjectBodies ?? 0) < source.records) fail('Generated database lost canonical full object bodies.');

  const databaseIds = new Set();
  const stableIds = new Set();
  for (const [position, record] of index.records.entries()) {
    if (!record.databaseId) fail(`Record ${position} has no databaseId.`);
    if (databaseIds.has(record.databaseId)) fail(`Duplicate databaseId: ${record.databaseId}`);
    databaseIds.add(record.databaseId);
    if (record.stableId) {
      if (stableIds.has(record.stableId)) fail(`Duplicate stableId: ${record.stableId}`);
      stableIds.add(record.stableId);
    }
  }

  const semantic = index.records.map(record => [
    record.databaseId,
    record.stableId || '',
    record.objectType || '',
    record.name || ''
  ]);
  const semanticFingerprint = `sha256:${sha256(JSON.stringify(semantic))}`;

  return {
    databaseVersion: index.databaseVersion,
    records: index.recordCount,
    fullObjectBodies: index.summary?.fullObjectBodies ?? 0,
    uniqueDatabaseIds: databaseIds.size,
    uniqueStableIds: stableIds.size,
    semanticFingerprint
  };
}

const seed = await certifySeedArchive();
const canonicalSource = await certifyCanonicalSource();
const database = await certifyGeneratedDatabase(seed, canonicalSource);
const certificate = {
  format: 'multiversal-content-pipeline-certificate',
  version: '1.1.0',
  result: 'PASS',
  certifiedAt: new Date().toISOString(),
  recordCount: database.records,
  fullObjectBodies: database.fullObjectBodies,
  semanticFingerprint: database.semanticFingerprint,
  seed,
  canonicalSource,
  database
};

await fs.mkdir(EVIDENCE_DIR, { recursive: true });
await fs.mkdir(DB_DIR, { recursive: true });
const serialized = JSON.stringify(certificate, null, 2) + '\n';
await fs.writeFile(path.join(EVIDENCE_DIR, 'latest-certificate.json'), serialized);
await fs.writeFile(path.join(DB_DIR, 'certification.json'), serialized);
console.log(`Content pipeline certified PASS: ${certificate.recordCount} records, ${certificate.fullObjectBodies} full object bodies, ${certificate.semanticFingerprint}.`);
