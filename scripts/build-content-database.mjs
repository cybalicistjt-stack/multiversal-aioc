import fs from 'node:fs/promises';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';

const ROOT = process.cwd();
const PART_DIR = path.join(ROOT, 'catalog-seed-parts');
const SOURCE_DIR = path.join(ROOT, 'content-source');
const OUT_DIR = path.join(ROOT, 'content-db');
const PARTS = [0,1,2,3,4].map(i => path.join(PART_DIR, `phase1-7.${String(i).padStart(2,'0')}.txt`));
const SOURCE = 'Multiversal 8E-008G Foundational Inventory Coverage (Phase 1–7 baseline)';
const DB_VERSION = '2.0.0';
const STAGES = {
  CANONICAL_ID_PRESENT: 'Schema review',
  ALIAS_RESOLVES: 'Partial conversion',
  PLAYTEST_INVENTORY_ONLY: 'Source identified'
};

function cleanBase64(text) { return String(text).replace(/[^A-Za-z0-9+/=]/g, ''); }
function looksLikeJson(text) {
  const trimmed = String(text).replace(/^\uFEFF/, '').trim();
  return trimmed.startsWith('{') || trimmed.startsWith('[');
}
function decodeBase64Strict(text, label) {
  const clean = cleanBase64(text);
  if (!clean) throw new Error(`${label} is empty.`);
  if (clean.length % 4 === 1) throw new Error(`${label} has an invalid Base64 length.`);
  const decoded = Buffer.from(clean, 'base64');
  if (!decoded.length) throw new Error(`${label} could not be decoded.`);
  return decoded;
}
function decodeArchivePayload(value) {
  let bytes = Buffer.isBuffer(value) ? value : Buffer.from(value);
  const trace = [];
  for (let layer = 0; layer < 8; layer++) {
    if (bytes.length >= 2 && bytes[0] === 0x1f && bytes[1] === 0x8b) {
      trace.push(`layer ${layer}: gzip`);
      return { text: zlib.gunzipSync(bytes).toString('utf8'), encoding: 'gzip', trace };
    }
    const text = bytes.toString('utf8').replace(/^\uFEFF/, '').trim();
    if (looksLikeJson(text)) {
      trace.push(`layer ${layer}: json`);
      return { text, encoding: 'json', trace };
    }
    const compact = text.replace(/\s/g, '');
    if (!compact || !/^[A-Za-z0-9+/=]+$/.test(compact)) {
      const preview = text.slice(0, 80).replace(/\s+/g, ' ');
      throw new Error(`Decoded layer ${layer + 1} is neither gzip, JSON, nor Base64 text. Preview: ${JSON.stringify(preview)}`);
    }
    trace.push(`layer ${layer}: base64(${compact.length})`);
    bytes = decodeBase64Strict(compact, `Nested Base64 layer ${layer + 1}`);
  }
  throw new Error(`Could not reach gzip or JSON data after eight decoding layers. Trace: ${trace.join(' -> ')}`);
}
function digest(text) { return `sha256:${crypto.createHash('sha256').update(text).digest('hex')}`; }
function slug(value) { return String(value || 'unclassified').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'unclassified'; }

function expandInventory(x, index) {
  const coverage = x.v || '';
  const stableId = x.r || '';
  return {
    databaseId: x.c || `phase17-${index + 1}`,
    stableId,
    name: x.n || stableId || `Unnamed inventory record ${index + 1}`,
    objectType: x.t || 'Unclassified',
    developmentStage: STAGES[coverage] || x.g || 'Source identified',
    source: x.s || SOURCE,
    sourceLocator: x.l || '',
    coverageStatus: coverage,
    promotionDecision: x.p || '',
    reviewStatus: x.w || '',
    schemaVersion: '',
    contentVersion: '',
    packIds: [],
    dependencies: [],
    tags: ['phase-1-7', coverage.toLowerCase(), String(x.p || '').toLowerCase()].filter(Boolean),
    manualEntry: null,
    gameObject: null,
    validation: null,
    balance: null,
    testing: null,
    provenance: {
      authority: SOURCE,
      phaseRange: '1-7',
      inventoryId: x.c || '',
      importedBy: 'scripts/build-content-database.mjs'
    }
  };
}

async function walkJson(dir) {
  const out = [];
  try {
    for (const entry of await fs.readdir(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) out.push(...await walkJson(full));
      else if (entry.isFile() && entry.name.toLowerCase().endsWith('.json')) out.push(full);
    }
  } catch (error) {
    if (error.code !== 'ENOENT') throw error;
  }
  return out;
}

function unwrapObjects(payload) {
  if (Array.isArray(payload)) return payload;
  for (const key of ['records','objects','gameObjects','entries','content']) if (Array.isArray(payload?.[key])) return payload[key];
  return payload && typeof payload === 'object' ? [payload] : [];
}

function normalizeFullObject(raw, sourcePath, sourceDigest, index) {
  const object = raw.gameObject || raw.object || raw;
  const stableId = object.id || object.stableId || raw.stableId || raw.refId || '';
  const objectType = object.objectKind || object.type || object.kind || raw.objectType || raw.contentType || 'Unclassified';
  const name = object.name || object.title || raw.name || stableId || `Unnamed imported object ${index + 1}`;
  const provenance = object.provenance || raw.provenance || {};
  return {
    databaseId: raw.databaseId || stableId || `imported-${digest(sourcePath + ':' + index).slice(7,23)}`,
    stableId,
    name,
    objectType,
    developmentStage: raw.developmentStage || raw.stage || (object.lifecycleStatus === 'released' ? 'Released' : object.canonStatus === 'approved' ? 'Approved' : 'Structured draft'),
    source: raw.source || provenance.source || provenance.authority || sourcePath,
    sourceLocator: raw.sourceLocator || provenance.locator || sourcePath,
    coverageStatus: raw.coverageStatus || '',
    promotionDecision: raw.promotionDecision || '',
    reviewStatus: raw.reviewStatus || '',
    schemaVersion: object.schemaVersion || raw.schemaVersion || '',
    contentVersion: object.contentVersion || raw.contentVersion || '',
    packIds: raw.packIds || object.packIds || [],
    dependencies: raw.dependencies || object.dependencies || [],
    tags: [...new Set([...(raw.tags || []), ...(object.tags || []), 'full-object'])],
    manualEntry: raw.manualEntry || null,
    gameObject: object,
    validation: raw.validation || object.validation || null,
    balance: raw.balance || object.balanceReport || object.extensions?.['app.multiversal.aioc']?.balanceReport || null,
    testing: raw.testing || null,
    provenance: {
      ...provenance,
      authority: provenance.authority || provenance.source || raw.source || sourcePath,
      sourcePath,
      sourceDigest,
      importedBy: 'scripts/build-content-database.mjs',
      importedAt: new Date().toISOString()
    }
  };
}

await fs.mkdir(OUT_DIR, { recursive: true });
const texts = await Promise.all(PARTS.map(file => fs.readFile(file, 'utf8')));
const decodedFragments = texts.map((text, index) => {
  try {
    return decodeBase64Strict(text, `Archive fragment ${index}`).toString('utf8');
  } catch (error) {
    throw new Error(`Failed to decode ${path.relative(ROOT, PARTS[index])}: ${error.message}`);
  }
});
const joinedPayload = decodedFragments.join('').replace(/^\uFEFF/, '').trim();
const archive = decodeArchivePayload(Buffer.from(joinedPayload, 'utf8'));
let inventoryPayload;
try {
  inventoryPayload = JSON.parse(archive.text);
} catch (error) {
  throw new Error(`Recovered ${archive.encoding} inventory payload is not valid JSON: ${error.message}. Trace: ${archive.trace.join(' -> ')}`);
}
if (!Array.isArray(inventoryPayload.records) || inventoryPayload.records.length < 1000) throw new Error(`Recovered inventory is invalid: ${inventoryPayload.records?.length ?? 0} records.`);
console.log(`Recovered inventory through ${archive.encoding}; ${inventoryPayload.records.length} records. Trace: ${archive.trace.join(' -> ')}`);

const inventoryRecords = inventoryPayload.records.map(expandInventory);
const byKey = new Map();
for (const record of inventoryRecords) byKey.set(record.stableId || record.databaseId, record);

const sourceFiles = await walkJson(SOURCE_DIR);
let fullObjectCount = 0;
for (const file of sourceFiles) {
  const text = await fs.readFile(file, 'utf8');
  const relative = path.relative(ROOT, file).replaceAll(path.sep, '/');
  const payload = JSON.parse(text);
  for (const [index, raw] of unwrapObjects(payload).entries()) {
    const full = normalizeFullObject(raw, relative, digest(text), index);
    const key = full.stableId || full.databaseId;
    const existing = byKey.get(key);
    byKey.set(key, existing ? {
      ...existing,
      ...full,
      databaseId: existing.databaseId || full.databaseId,
      coverageStatus: existing.coverageStatus || full.coverageStatus,
      promotionDecision: existing.promotionDecision || full.promotionDecision,
      reviewStatus: existing.reviewStatus || full.reviewStatus,
      tags: [...new Set([...(existing.tags || []), ...(full.tags || [])])],
      provenance: { ...existing.provenance, ...full.provenance }
    } : full);
    fullObjectCount++;
  }
}

const records = [...byKey.values()].sort((a,b) => a.objectType.localeCompare(b.objectType) || a.name.localeCompare(b.name));
const byType = {}, byStage = {}, byCoverage = {}, bySource = {};
for (const record of records) {
  (byType[record.objectType] ??= []).push(record.databaseId);
  (byStage[record.developmentStage] ??= []).push(record.databaseId);
  (byCoverage[record.coverageStatus || 'UNCLASSIFIED'] ??= []).push(record.databaseId);
  (bySource[record.source || 'Unknown source'] ??= []).push(record.databaseId);
}

const generatedAt = new Date().toISOString();
const summary = {
  inventoryRecords: inventoryRecords.length,
  fullObjectBodies: records.filter(r => r.gameObject).length,
  importedSourceObjects: fullObjectCount,
  canonicalIds: records.filter(r => r.coverageStatus === 'CANONICAL_ID_PRESENT').length,
  aliasResolved: records.filter(r => r.coverageStatus === 'ALIAS_RESOLVES').length,
  playtestOnly: records.filter(r => r.coverageStatus === 'PLAYTEST_INVENTORY_ONLY').length,
  types: Object.fromEntries(Object.entries(byType).map(([k,v]) => [k, v.length]))
};
const index = { format:'multiversal-content-database', databaseVersion:DB_VERSION, generatedAt, source:SOURCE, recordCount:records.length, summary, records };
const manifest = {
  format:'multiversal-content-database-manifest', databaseVersion:DB_VERSION, generatedAt, source:SOURCE,
  recordCount:records.length, fullObjectBodies:summary.fullObjectBodies,
  recordSchema:'./content-record.schema.json', sourceRegistry:'./source-registry.json', indexPath:'./index.json',
  indexes:{ byType:'./indexes/by-type.json', byStage:'./indexes/by-stage.json', byCoverage:'./indexes/by-coverage.json', bySource:'./indexes/by-source.json' }
};

await fs.mkdir(path.join(OUT_DIR, 'indexes'), { recursive: true });
await fs.mkdir(path.join(OUT_DIR, 'objects'), { recursive: true });
await fs.writeFile(path.join(OUT_DIR, 'index.json'), JSON.stringify(index, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'indexes', 'by-type.json'), JSON.stringify(byType, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'indexes', 'by-stage.json'), JSON.stringify(byStage, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'indexes', 'by-coverage.json'), JSON.stringify(byCoverage, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'indexes', 'by-source.json'), JSON.stringify(bySource, null, 2) + '\n');
for (const record of records.filter(r => r.gameObject)) {
  const folder = path.join(OUT_DIR, 'objects', slug(record.objectType));
  await fs.mkdir(folder, { recursive: true });
  await fs.writeFile(path.join(folder, `${slug(record.stableId || record.databaseId)}.json`), JSON.stringify(record, null, 2) + '\n');
}
console.log(`Generated Multiversal content database: ${records.length} records, ${summary.fullObjectBodies} full object bodies.`);
