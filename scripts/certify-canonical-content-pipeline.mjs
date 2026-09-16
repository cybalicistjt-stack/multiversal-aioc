import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { loadCanonicalContentSource } from './lib/canonical-content-source.mjs';

const ROOT = process.cwd();
const DB_DIR = path.join(ROOT, 'content-db');
const EVIDENCE_DIR = path.join(ROOT, 'evidence', 'content-pipeline');

const sha256 = value => `sha256:${crypto.createHash('sha256').update(value).digest('hex')}`;
const fail = message => { throw new Error(message); };
const readJson = async file => JSON.parse(await fs.readFile(file, 'utf8'));
const stableIdOf = raw => {
  const object = raw?.gameObject || raw?.object || raw;
  return object?.id || object?.stableId || raw?.stableId || raw?.refId || '';
};

const sourceSet = await loadCanonicalContentSource(ROOT);
const expectedByStableId = new Map(sourceSet.entries.map(entry => [stableIdOf(entry.raw), entry]));

const index = await readJson(path.join(DB_DIR, 'index.json'));
const manifest = await readJson(path.join(DB_DIR, 'manifest.json'));
const sourceRegistry = await readJson(path.join(DB_DIR, 'source-registry.json'));
if (index.format !== 'multiversal-content-database') fail('Database format is invalid.');
if (index.databaseVersion !== '3.0.0') fail(`Unexpected database version: ${index.databaseVersion}`);
if (!Array.isArray(index.records) || index.records.length !== sourceSet.recordCount) {
  fail(`Canonical database must contain ${sourceSet.recordCount} records; found ${index.records?.length ?? 0}.`);
}
if (index.recordCount !== index.records.length) fail('Index record count mismatch.');
if (manifest.recordCount !== index.recordCount) fail('Manifest record count mismatch.');
if (manifest.fullObjectBodies !== sourceSet.recordCount) fail('Manifest full-object count mismatch.');
if (index.summary?.fullObjectBodies !== sourceSet.recordCount) fail('Index full-object count mismatch.');
if (index.summary?.baselineSourceRecords !== sourceSet.baselineRecordCount) fail('Index baseline record count mismatch.');
if (index.summary?.supplementalSourceRecords !== sourceSet.supplementalRecordCount) fail('Index supplemental record count mismatch.');
if (index.summary?.legacyInventoryStatus !== 'QUARANTINED_CORRUPTED_SOURCE') {
  fail('Legacy inventory quarantine status is missing.');
}

if (index.sourceDigest !== sourceSet.sourceSetDigest || manifest.sourceDigest !== sourceSet.sourceSetDigest) {
  fail('Canonical composite source-set digest mismatch.');
}
if (sourceRegistry.sourceSetDigest !== sourceSet.sourceSetDigest) fail('Source registry digest mismatch.');
if (sourceRegistry.recordCount !== sourceSet.recordCount) fail('Source registry record count mismatch.');
if (sourceRegistry.baselineRecordCount !== sourceSet.baselineRecordCount) fail('Source registry baseline count mismatch.');
if (sourceRegistry.supplementalRecordCount !== sourceSet.supplementalRecordCount) fail('Source registry supplemental count mismatch.');

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

  const expected = expectedByStableId.get(record.stableId);
  if (!expected) fail(`Record ${record.stableId} is not present in the canonical source set.`);
  if (record.provenance?.sourcePath !== expected.sourcePath) {
    fail(`Record ${record.stableId} has an invalid provenance source path.`);
  }
  if (record.provenance?.sourceDigest !== expected.sourceDigest) {
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
  version: '3.0.0',
  pipelineMode: 'COMPOSITE_CANONICAL_SOURCE_SET',
  result: 'PASS',
  certifiedAt: new Date().toISOString(),
  recordCount: index.recordCount,
  baselineRecordCount: sourceSet.baselineRecordCount,
  supplementalRecordCount: sourceSet.supplementalRecordCount,
  sourceCount: sourceSet.sources.length,
  fullObjectBodies: index.summary.fullObjectBodies,
  semanticFingerprint,
  sourceDigest: sourceSet.sourceSetDigest,
  uniqueDatabaseIds: databaseIds.size,
  uniqueStableIds: stableIds.size,
  sources: sourceSet.sources,
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
console.log(
  `Canonical content pipeline PASS: ${certificate.recordCount} governed objects ` +
  `(${certificate.baselineRecordCount} baseline + ${certificate.supplementalRecordCount} supplemental); ${semanticFingerprint}.`
);
