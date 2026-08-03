import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const ROOT = process.cwd();
const SOURCE_PATH = path.join(ROOT, 'content-source', 'phase-1-8-canonical-objects.json');
const OUT_DIR = path.join(ROOT, 'content-db');
const DB_VERSION = '3.0.0';

const sha256 = value => `sha256:${crypto.createHash('sha256').update(value).digest('hex')}`;
const slug = value => String(value || 'unclassified')
  .toLowerCase()
  .replace(/[^a-z0-9]+/g, '-')
  .replace(/^-|-$/g, '') || 'unclassified';

function unwrapObjects(payload) {
  if (Array.isArray(payload)) return payload;
  for (const key of ['records', 'objects', 'gameObjects', 'entries', 'content']) {
    if (Array.isArray(payload?.[key])) return payload[key];
  }
  return payload && typeof payload === 'object' ? [payload] : [];
}

function normalizeRecord(raw, index, sourceDigest) {
  const object = raw.gameObject || raw.object || raw;
  const stableId = object.id || object.stableId || raw.stableId || raw.refId || '';
  if (!stableId) throw new Error(`Canonical record ${index} has no stable ID.`);

  const objectType = object.objectKind || object.type || object.kind || raw.objectType || raw.contentType || 'Unclassified';
  const name = object.name || object.title || raw.name || stableId;
  const provenance = object.provenance || raw.provenance || {};

  return {
    databaseId: raw.databaseId || stableId,
    stableId,
    name,
    objectType,
    developmentStage: raw.developmentStage || raw.stage || (
      object.lifecycleStatus === 'released' ? 'Released' :
      object.canonStatus === 'approved' ? 'Approved' :
      'Structured draft'
    ),
    source: raw.source || provenance.source || provenance.authority || 'phase-1-8-canonical-objects',
    sourceLocator: raw.sourceLocator || provenance.locator || 'content-source/phase-1-8-canonical-objects.json',
    coverageStatus: 'CANONICAL_OBJECT_PRESENT',
    promotionDecision: raw.promotionDecision || '',
    reviewStatus: raw.reviewStatus || '',
    schemaVersion: object.schemaVersion || raw.schemaVersion || '',
    contentVersion: object.contentVersion || raw.contentVersion || '',
    packIds: raw.packIds || object.packIds || [],
    dependencies: raw.dependencies || object.dependencies || [],
    tags: [...new Set([...(raw.tags || []), ...(object.tags || []), 'canonical-object'])],
    manualEntry: raw.manualEntry || null,
    gameObject: object,
    validation: raw.validation || object.validation || null,
    balance: raw.balance || object.balanceReport || object.extensions?.['app.multiversal.aioc']?.balanceReport || null,
    testing: raw.testing || null,
    provenance: {
      ...provenance,
      authority: provenance.authority || provenance.source || raw.source || 'Multiversal canonical source bundle',
      sourcePath: 'content-source/phase-1-8-canonical-objects.json',
      sourceDigest,
      importedBy: 'scripts/build-canonical-content-database.mjs'
    }
  };
}

const sourceText = await fs.readFile(SOURCE_PATH, 'utf8');
const payload = JSON.parse(sourceText);
if (payload.format !== 'multiversal-content-source-bundle') {
  throw new Error(`Unexpected canonical source format: ${payload.format}`);
}

const rawRecords = unwrapObjects(payload);
if (rawRecords.length !== 487) {
  throw new Error(`Expected exactly 487 canonical records; found ${rawRecords.length}.`);
}

const sourceDigest = sha256(sourceText);
const records = rawRecords.map((record, index) => normalizeRecord(record, index, sourceDigest));
const databaseIds = new Set();
const stableIds = new Set();
for (const record of records) {
  if (databaseIds.has(record.databaseId)) throw new Error(`Duplicate databaseId: ${record.databaseId}`);
  if (stableIds.has(record.stableId)) throw new Error(`Duplicate stableId: ${record.stableId}`);
  databaseIds.add(record.databaseId);
  stableIds.add(record.stableId);
}

records.sort((a, b) => a.objectType.localeCompare(b.objectType) || a.name.localeCompare(b.name));

const byType = {};
const byStage = {};
const byCoverage = {};
const bySource = {};
for (const record of records) {
  (byType[record.objectType] ??= []).push(record.databaseId);
  (byStage[record.developmentStage] ??= []).push(record.databaseId);
  (byCoverage[record.coverageStatus] ??= []).push(record.databaseId);
  (bySource[record.source || 'Unknown source'] ??= []).push(record.databaseId);
}

const semanticProjection = records.map(record => [
  record.databaseId,
  record.stableId,
  record.objectType,
  record.name
]);
const semanticFingerprint = sha256(JSON.stringify(semanticProjection));
const generatedAt = new Date().toISOString();
const summary = {
  canonicalSourceRecords: rawRecords.length,
  fullObjectBodies: records.length,
  legacyInventoryRecords: 0,
  legacyInventoryStatus: 'QUARANTINED_CORRUPTED_SOURCE',
  uniqueDatabaseIds: databaseIds.size,
  uniqueStableIds: stableIds.size,
  types: Object.fromEntries(Object.entries(byType).map(([key, value]) => [key, value.length]))
};

const index = {
  format: 'multiversal-content-database',
  databaseVersion: DB_VERSION,
  generatedAt,
  source: 'Multiversal Phase 1–8 canonical object bundle',
  sourceDigest,
  semanticFingerprint,
  recordCount: records.length,
  summary,
  records
};
const manifest = {
  format: 'multiversal-content-database-manifest',
  databaseVersion: DB_VERSION,
  generatedAt,
  source: index.source,
  sourceDigest,
  semanticFingerprint,
  recordCount: records.length,
  fullObjectBodies: records.length,
  legacyInventoryStatus: summary.legacyInventoryStatus,
  recordSchema: './content-record.schema.json',
  sourceRegistry: './source-registry.json',
  indexPath: './index.json',
  indexes: {
    byType: './indexes/by-type.json',
    byStage: './indexes/by-stage.json',
    byCoverage: './indexes/by-coverage.json',
    bySource: './indexes/by-source.json'
  }
};

await fs.rm(OUT_DIR, { recursive: true, force: true });
await fs.mkdir(path.join(OUT_DIR, 'indexes'), { recursive: true });
await fs.mkdir(path.join(OUT_DIR, 'objects'), { recursive: true });
await fs.writeFile(path.join(OUT_DIR, 'index.json'), JSON.stringify(index, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'indexes', 'by-type.json'), JSON.stringify(byType, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'indexes', 'by-stage.json'), JSON.stringify(byStage, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'indexes', 'by-coverage.json'), JSON.stringify(byCoverage, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'indexes', 'by-source.json'), JSON.stringify(bySource, null, 2) + '\n');

for (const record of records) {
  const folder = path.join(OUT_DIR, 'objects', slug(record.objectType));
  await fs.mkdir(folder, { recursive: true });
  await fs.writeFile(
    path.join(folder, `${slug(record.stableId)}.json`),
    JSON.stringify(record, null, 2) + '\n'
  );
}

console.log(`Generated canonical Multiversal content database: ${records.length} governed objects; ${semanticFingerprint}.`);
