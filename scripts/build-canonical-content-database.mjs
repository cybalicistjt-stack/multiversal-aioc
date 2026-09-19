import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { loadCanonicalContentSource } from './lib/canonical-content-source.mjs';

const ROOT = process.cwd();
const OUT_DIR = path.join(ROOT, 'content-db');
const DB_VERSION = '3.0.0';

const sha256 = value => `sha256:${crypto.createHash('sha256').update(value).digest('hex')}`;
const slug = value => String(value || 'unclassified')
  .toLowerCase()
  .replace(/[^a-z0-9]+/g, '-')
  .replace(/^-|-$/g, '') || 'unclassified';

function normalizeRecord(entry, index) {
  const raw = entry.raw;
  const object = raw.gameObject || raw.object || raw;
  const stableId = object.id || object.stableId || raw.stableId || raw.refId || '';
  if (!stableId) throw new Error(`Canonical record ${index} has no stable ID.`);

  const objectType = object.objectKind || object.type || object.kind || raw.objectType || raw.contentType || 'Unclassified';
  const name = object.name || object.title || raw.name || stableId;
  const provenance = object.provenance || raw.provenance || {};
  const fallbackSource = entry.sourceClass === 'baseline' ? 'phase-1-8-canonical-objects' : entry.sourceBundleId;

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
    source: raw.source || provenance.source || provenance.authority || fallbackSource,
    sourceLocator: raw.sourceLocator || provenance.locator || entry.sourcePath,
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
      sourcePath: entry.sourcePath,
      sourceDigest: entry.sourceDigest,
      ...(entry.sourceClass !== 'baseline' ? {
        sourceBundleId: entry.sourceBundleId,
        sourceBundlePart: entry.sourceBundlePart,
        sourceClass: entry.sourceClass
      } : {}),
      ...(entry.replaces ? { replaces: entry.replaces } : {}),
      importedBy: 'scripts/build-canonical-content-database.mjs'
    }
  };
}

const sourceSet = await loadCanonicalContentSource(ROOT);
const records = sourceSet.entries.map((entry, index) => normalizeRecord(entry, index));
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
  record.name,
  record.contentVersion
]);
const semanticFingerprint = sha256(JSON.stringify(semanticProjection));
let generatedAt = new Date().toISOString();
try {
  const previous = JSON.parse(await fs.readFile(path.join(OUT_DIR, 'index.json'), 'utf8'));
  if (
    previous.sourceDigest === sourceSet.sourceSetDigest &&
    previous.semanticFingerprint === semanticFingerprint &&
    typeof previous.generatedAt === 'string' &&
    previous.generatedAt
  ) {
    generatedAt = previous.generatedAt;
  }
} catch {
  // No prior certified projection: the first material generation may stamp wall-clock time.
}
const sourceComposition = {
  baselineRecords: sourceSet.baselineRecordCount,
  appendedRecords: sourceSet.appendedRecordCount,
  replacementRecords: sourceSet.replacementRecordCount,
  supplementalInputRecords: sourceSet.supplementalRecordCount,
  effectiveRecords: sourceSet.recordCount,
  sources: sourceSet.sources
};
const summary = {
  canonicalSourceRecords: sourceSet.recordCount,
  baselineSourceRecords: sourceSet.baselineRecordCount,
  appendedSourceRecords: sourceSet.appendedRecordCount,
  replacementSourceRecords: sourceSet.replacementRecordCount,
  supplementalSourceRecords: sourceSet.supplementalRecordCount,
  fullObjectBodies: records.length,
  certificationScope: 'canonical-source-integrity-not-game-readiness',
  gameReadinessAuthority: 'OBJECT_GAME_READINESS_PROGRAM / OGR',
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
  source: 'Multiversal composite canonical source set',
  sourceDigest: sourceSet.sourceSetDigest,
  sourceComposition,
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
  sourceDigest: sourceSet.sourceSetDigest,
  sourceComposition,
  semanticFingerprint,
  recordCount: records.length,
  fullObjectBodies: records.length,
  certificationScope: summary.certificationScope,
  gameReadinessAuthority: summary.gameReadinessAuthority,
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
const sourceRegistry = {
  format: 'multiversal-content-source-registry',
  version: '1.1.0',
  sourceSetDigest: sourceSet.sourceSetDigest,
  recordCount: sourceSet.recordCount,
  baselineRecordCount: sourceSet.baselineRecordCount,
  appendedRecordCount: sourceSet.appendedRecordCount,
  replacementRecordCount: sourceSet.replacementRecordCount,
  supplementalRecordCount: sourceSet.supplementalRecordCount,
  certificationScope: summary.certificationScope,
  gameReadinessAuthority: summary.gameReadinessAuthority,
  sources: sourceSet.sources
};

await fs.mkdir(OUT_DIR, { recursive: true });
for (const generatedPath of [
  'index.json',
  'manifest.json',
  'source-registry.json',
  'certification.json',
  'indexes',
  'objects'
]) {
  await fs.rm(path.join(OUT_DIR, generatedPath), { recursive: true, force: true });
}
await fs.mkdir(path.join(OUT_DIR, 'indexes'), { recursive: true });
await fs.mkdir(path.join(OUT_DIR, 'objects'), { recursive: true });
await fs.writeFile(path.join(OUT_DIR, 'index.json'), JSON.stringify(index, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'source-registry.json'), JSON.stringify(sourceRegistry, null, 2) + '\n');
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

console.log(
  `Generated canonical Multiversal content database: ${records.length} governed objects ` +
  `(${sourceSet.baselineRecordCount} baseline + ${sourceSet.appendedRecordCount} appended; ` +
  `${sourceSet.replacementRecordCount} replacements applied); ${semanticFingerprint}.`
);
