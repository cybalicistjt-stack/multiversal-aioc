import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const BASELINE_FILE = 'phase-1-8-canonical-objects.json';
const BASELINE_EXPECTED_RECORDS = 487;
const SUPPLEMENTAL_FORMAT = 'multiversal-canonical-content-source';
const SUPPLEMENTAL_STATUS = 'owner-approved-canonical-incorporation';

const sha256 = value => `sha256:${crypto.createHash('sha256').update(value).digest('hex')}`;

function unwrapObjects(payload) {
  if (Array.isArray(payload)) return payload;
  for (const key of ['records', 'objects', 'gameObjects', 'entries', 'content']) {
    if (Array.isArray(payload?.[key])) return payload[key];
  }
  return payload && typeof payload === 'object' ? [payload] : [];
}

function stableIdOf(raw) {
  const object = raw?.gameObject || raw?.object || raw;
  return object?.id || object?.stableId || raw?.stableId || raw?.refId || '';
}

export async function loadCanonicalContentSource(root = process.cwd()) {
  const sourceDir = path.join(root, 'content-source');
  const baselinePath = path.join(sourceDir, BASELINE_FILE);
  const baselineText = await fs.readFile(baselinePath, 'utf8');
  const baselinePayload = JSON.parse(baselineText);
  if (baselinePayload.format !== 'multiversal-content-source-bundle') {
    throw new Error(`Unexpected baseline canonical source format: ${baselinePayload.format}`);
  }
  const baselineRecords = unwrapObjects(baselinePayload);
  if (baselineRecords.length !== BASELINE_EXPECTED_RECORDS) {
    throw new Error(`Expected ${BASELINE_EXPECTED_RECORDS} baseline canonical records; found ${baselineRecords.length}.`);
  }

  const sources = [{
    sourceClass: 'baseline',
    sourcePath: `content-source/${BASELINE_FILE}`,
    sourceDigest: sha256(baselineText),
    bundleId: baselinePayload.bundleId || 'phase-1-8-canonical-objects',
    bundlePart: null,
    recordCount: baselineRecords.length
  }];
  const entries = baselineRecords.map(raw => ({
    raw,
    sourceClass: 'baseline',
    sourcePath: `content-source/${BASELINE_FILE}`,
    sourceDigest: sources[0].sourceDigest,
    sourceBundleId: sources[0].bundleId,
    sourceBundlePart: null
  }));

  const names = (await fs.readdir(sourceDir))
    .filter(name => name.endsWith('.json') && name !== BASELINE_FILE)
    .sort();

  for (const name of names) {
    const filePath = path.join(sourceDir, name);
    const text = await fs.readFile(filePath, 'utf8');
    const payload = JSON.parse(text);
    if (payload.format !== SUPPLEMENTAL_FORMAT) continue;
    if (payload.status !== SUPPLEMENTAL_STATUS) {
      throw new Error(`Supplemental canonical bundle ${name} has unsupported status: ${payload.status}`);
    }
    const records = unwrapObjects(payload);
    if (!records.length) throw new Error(`Supplemental canonical bundle ${name} has no records.`);
    const source = {
      sourceClass: 'supplemental',
      sourcePath: `content-source/${name}`,
      sourceDigest: sha256(text),
      bundleId: payload.bundleId || name.replace(/\.json$/i, ''),
      bundlePart: payload.authority?.bundlePart || payload.bundlePart || null,
      recordCount: records.length
    };
    sources.push(source);
    for (const raw of records) {
      entries.push({
        raw,
        sourceClass: source.sourceClass,
        sourcePath: source.sourcePath,
        sourceDigest: source.sourceDigest,
        sourceBundleId: source.bundleId,
        sourceBundlePart: source.bundlePart
      });
    }
  }

  const stableIds = new Set();
  for (const [index, entry] of entries.entries()) {
    const stableId = stableIdOf(entry.raw);
    if (!stableId) throw new Error(`Canonical record ${index} has no stable ID.`);
    if (stableIds.has(stableId)) throw new Error(`Duplicate canonical stable ID across source set: ${stableId}`);
    stableIds.add(stableId);
  }

  const sourceSetProjection = sources.map(source => [
    source.sourceClass,
    source.sourcePath,
    source.sourceDigest,
    source.bundleId,
    source.bundlePart,
    source.recordCount
  ]);
  const sourceSetDigest = sha256(JSON.stringify(sourceSetProjection));
  const supplementalRecordCount = entries.length - baselineRecords.length;

  return {
    baselineRecordCount: baselineRecords.length,
    supplementalRecordCount,
    recordCount: entries.length,
    sourceSetDigest,
    sources,
    entries
  };
}

export { BASELINE_EXPECTED_RECORDS, BASELINE_FILE, SUPPLEMENTAL_FORMAT, SUPPLEMENTAL_STATUS };
