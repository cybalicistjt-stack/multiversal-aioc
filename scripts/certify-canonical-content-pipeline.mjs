import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const ROOT = process.cwd();
const SOURCE_PATH = path.join(ROOT, 'content-source', 'phase-1-8-canonical-objects.json');
const DB_DIR = path.join(ROOT, 'content-db');
const EVIDENCE_DIR = path.join(ROOT, 'evidence', 'content-pipeline');

const sha256 = value => `sha256:${crypto.createHash('sha256').update(value).digest('hex')}`;
const fail = message => { throw new Error(message); };
const readJson = async file => JSON.parse(await fs.readFile(file, 'utf8'));

const sourceText = await fs.readFile(SOURCE_PATH, 'utf8');
const source = JSON.parse(sourceText);
if (source.format !== 'multiversal-content-source-bundle') fail('Canonical source format is invalid.');
if (!Array.isArray(source.records) || source.records.length !== 487) {
  fail(`Canonical source must contain exactly 487 records; found ${source.records?.length ?? 0}.`);
}

const index = await readJson(path.join(DB_DIR, 'index.json'));
const manifest = await readJson(path.join(DB_DIR, 'manifest.json'));
if (index.format !== 'multiversal-content-database') fail('Database format is invalid.');
if (index.databaseVersion !== '3.0.0') fail(`Unexpected database version: ${index.databaseVersion}`);
if (!Array.isArray(index.records) || index.records.length !== 487) {
  fail(`Canonical database must contain exactly 487 records; found ${index.records?.length ?? 0}.`);
}
if (index.recordCount !== index.records.length) fail('Index record count mismatch.');
if (manifest.recordCount !== index.recordCount) fail('Manifest record count mismatch.');
if (manifest.fullObjectBodies !== 487) fail('Manifest full-object count mismatch.');
if (index.summary?.fullObjectBodies !== 487) fail('Index full-object count mismatch.');
if (index.summary?.legacyInventoryStatus !== 'QUARANTINED_CORRUPTED_SOURCE') {
  fail('Legacy inventory quarantine status is missing.');
}

const expectedSourceDigest = sha256(sourceText);
if (index.sourceDigest !== expectedSourceDigest || manifest.sourceDigest !== expectedSourceDigest) {
  fail('Canonical source digest mismatch.');
}

const databaseIds = new Set();
const stableIds = new Set();
for (const [position, record] of index.records.entries()) {
  if (!record.databaseId) fail(`Record ${position} has no databaseId.`);
  if (!record.stableId) fail(`Record ${position} has no stableId.`);
  if (!record.gameObject) fail(`Record ${record.stableId} has no full game object.`);
  if (databaseIds.has(record.databaseId)) fail(`Duplicate databaseId: ${record.databaseId}`);
  if (stableIds.has(record.stableId)) fail(`Duplicate stableId: ${record.stableId}`);
  databaseIds.add(record.databaseId);
  stableIds.add(record.stableId);
  if (record.provenance?.sourceDigest !== expectedSourceDigest) {
    fail(`Record ${record.stableId} has an invalid provenance source digest.`);
  }
}

const semanticProjection = index.records.map(record => [
  record.databaseId,
  record.stableId,
  record.objectType,
  record.name
]);
const semanticFingerprint = sha256(JSON.stringify(semanticProjection));
if (index.semanticFingerprint !== semanticFingerprint) fail('Index semantic fingerprint mismatch.');
if (manifest.semanticFingerprint !== semanticFingerprint) fail('Manifest semantic fingerprint mismatch.');

const certificate = {
  format: 'multiversal-content-pipeline-certificate',
  version: '2.0.0',
  pipelineMode: 'CANONICAL_OBJECTS_ONLY',
  result: 'PASS',
  certifiedAt: new Date().toISOString(),
  recordCount: index.recordCount,
  fullObjectBodies: index.summary.fullObjectBodies,
  semanticFingerprint,
  sourceDigest: expectedSourceDigest,
  uniqueDatabaseIds: databaseIds.size,
  uniqueStableIds: stableIds.size,
  legacyInventory: {
    status: 'QUARANTINED_CORRUPTED_SOURCE',
    expectedAuditRows: 1347,
    includedRecords: 0,
    promotionAllowed: false,
    recoveryRequirement: 'Import the intact approved 8E-008G Foundational Inventory Coverage source.'
  }
};

await fs.mkdir(EVIDENCE_DIR, { recursive: true });
const serialized = JSON.stringify(certificate, null, 2) + '\n';
await fs.writeFile(path.join(EVIDENCE_DIR, 'latest-certificate.json'), serialized);
await fs.writeFile(path.join(DB_DIR, 'certification.json'), serialized);
console.log(`Canonical content pipeline PASS: ${certificate.recordCount} governed objects; ${semanticFingerprint}.`);
