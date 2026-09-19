import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { loadCanonicalContentSource } from './lib/canonical-content-source.mjs';

const ROOT = process.cwd();
const DB_DIR = path.join(ROOT, 'content-db');
const EVIDENCE_DIR = path.join(ROOT, 'evidence', 'content-pipeline');
const CERTIFICATION_SCOPE = 'canonical-source-integrity-not-game-readiness';
const GAME_READINESS_AUTHORITY = 'OBJECT_GAME_READINESS_PROGRAM / OGR';

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
  fail(`Canonical database must contain ${sourceSet.recordCount} effective records; found ${index.records?.length ?? 0}.`);
}
if (index.recordCount !== index.records.length) fail('Index record count mismatch.');
if (manifest.recordCount !== index.recordCount) fail('Manifest record count mismatch.');
if (manifest.fullObjectBodies !== sourceSet.recordCount) fail('Manifest full-object count mismatch.');
if (index.summary?.fullObjectBodies !== sourceSet.recordCount) fail('Index full-object count mismatch.');
if (index.summary?.baselineSourceRecords !== sourceSet.baselineRecordCount) fail('Index baseline record count mismatch.');
if (index.summary?.appendedSourceRecords !== sourceSet.appendedRecordCount) fail('Index appended record count mismatch.');
if (index.summary?.replacementSourceRecords !== sourceSet.replacementRecordCount) fail('Index replacement record count mismatch.');
if (index.summary?.supplementalSourceRecords !== sourceSet.supplementalRecordCount) fail('Index supplemental input count mismatch.');
if (index.summary?.certificationScope !== CERTIFICATION_SCOPE || manifest.certificationScope !== CERTIFICATION_SCOPE) {
  fail('Canonical certification scope must explicitly exclude game-readiness certification.');
}
if (index.summary?.gameReadinessAuthority !== GAME_READINESS_AUTHORITY || manifest.gameReadinessAuthority !== GAME_READINESS_AUTHORITY) {
  fail('Object Game Readiness authority boundary is missing.');
}
if (index.summary?.legacyInventoryStatus !== 'QUARANTINED_CORRUPTED_SOURCE') {
  fail('Legacy inventory quarantine status is missing.');
}

if (index.sourceDigest !== sourceSet.sourceSetDigest || manifest.sourceDigest !== sourceSet.sourceSetDigest) {
  fail('Canonical composite source-set digest mismatch.');
}
if (sourceRegistry.sourceSetDigest !== sourceSet.sourceSetDigest) fail('Source registry digest mismatch.');
if (sourceRegistry.recordCount !== sourceSet.recordCount) fail('Source registry record count mismatch.');
if (sourceRegistry.baselineRecordCount !== sourceSet.baselineRecordCount) fail('Source registry baseline count mismatch.');
if (sourceRegistry.appendedRecordCount !== sourceSet.appendedRecordCount) fail('Source registry appended count mismatch.');
if (sourceRegistry.replacementRecordCount !== sourceSet.replacementRecordCount) fail('Source registry replacement count mismatch.');
if (sourceRegistry.supplementalRecordCount !== sourceSet.supplementalRecordCount) fail('Source registry supplemental input count mismatch.');

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
  if (!expected) fail(`Record ${record.stableId} is not present in the effective canonical source set.`);
  if (record.provenance?.sourcePath !== expected.sourcePath) {
    fail(`Record ${record.stableId} has an invalid provenance source path.`);
  }
  if (record.provenance?.sourceDigest !== expected.sourceDigest) {
    fail(`Record ${record.stableId} has an invalid provenance source digest.`);
  }
  if (expected.replaces) {
    if (record.provenance?.sourceClass !== 'replacement') fail(`Replacement ${record.stableId} lost its source class.`);
    if (record.provenance?.replaces?.stableId !== expected.replaces.stableId) fail(`Replacement lineage mismatch for ${record.stableId}.`);
    if (record.provenance?.replaces?.contentVersion !== expected.replaces.contentVersion) fail(`Replacement predecessor version mismatch for ${record.stableId}.`);
  }
}

const semanticProjection = index.records.map(record => [
  record.databaseId,
  record.stableId,
  record.objectType,
  record.name,
  record.contentVersion
]);
const semanticFingerprint = sha256(JSON.stringify(semanticProjection));
if (index.semanticFingerprint !== semanticFingerprint) fail('Index semantic fingerprint mismatch.');
if (manifest.semanticFingerprint !== semanticFingerprint) fail('Manifest semantic fingerprint mismatch.');

let certifiedAt = new Date().toISOString();
try {
  const previous = JSON.parse(await fs.readFile(path.join(DB_DIR, 'certification.json'), 'utf8'));
  if (
    previous.sourceDigest === sourceSet.sourceSetDigest &&
    previous.semanticFingerprint === semanticFingerprint &&
    typeof previous.certifiedAt === 'string' &&
    previous.certifiedAt
  ) {
    certifiedAt = previous.certifiedAt;
  }
} catch {
  // No prior certificate: the first material certification may stamp wall-clock time.
}

const certificate = {
  format: 'multiversal-content-pipeline-certificate',
  version: '3.1.0',
  pipelineMode: 'COMPOSITE_CANONICAL_SOURCE_SET_WITH_GOVERNED_REPLACEMENTS',
  certificationScope: CERTIFICATION_SCOPE,
  gameReadinessAuthority: GAME_READINESS_AUTHORITY,
  result: 'PASS',
  certifiedAt,
  recordCount: index.recordCount,
  baselineRecordCount: sourceSet.baselineRecordCount,
  appendedRecordCount: sourceSet.appendedRecordCount,
  replacementRecordCount: sourceSet.replacementRecordCount,
  supplementalInputRecordCount: sourceSet.supplementalRecordCount,
  sourceCount: sourceSet.sources.length,
  fullObjectBodies: index.summary.fullObjectBodies,
  semanticFingerprint,
  sourceDigest: sourceSet.sourceSetDigest,
  uniqueDatabaseIds: databaseIds.size,
  uniqueStableIds: stableIds.size,
  sources: sourceSet.sources,
  gameReadiness: {
    assessed: false,
    authority: GAME_READINESS_AUTHORITY,
    explicitNonClaim: 'Canonical source/database certification does not imply GAME_READY, validated mechanics, runtime readiness, or playtest completion.'
  },
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
  `Canonical content pipeline PASS: ${certificate.recordCount} effective governed objects ` +
  `(${certificate.baselineRecordCount} baseline + ${certificate.appendedRecordCount} appended; ` +
  `${certificate.replacementRecordCount} replacements applied); ${semanticFingerprint}.`
);
