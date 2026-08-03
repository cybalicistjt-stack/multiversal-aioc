import fs from 'node:fs/promises';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';

const ROOT = process.cwd();
const PART_DIR = path.join(ROOT, 'catalog-seed-parts');
const PARTS = [0, 1, 2, 3, 4].map(i => path.join(PART_DIR, `phase1-7.${String(i).padStart(2, '0')}.txt`));
const clean = value => String(value).replace(/[^A-Za-z0-9+/=]/g, '');
const sha256 = value => crypto.createHash('sha256').update(value).digest('hex');

const fragments = await Promise.all(PARTS.map(async file => clean(await fs.readFile(file, 'utf8'))));
const expectedRegularLength = 17000;
const anomalous = fragments
  .map((value, index) => ({ index, length: value.length }))
  .filter(({ index, length }) => index < fragments.length - 1 && length !== expectedRegularLength);

if (anomalous.length === 0) {
  console.log('Seed fragments already match the canonical layout.');
  process.exit(0);
}
if (anomalous.length !== 1) {
  throw new Error(`Expected exactly one anomalous regular fragment; found ${JSON.stringify(anomalous)}.`);
}

const { index, length } = anomalous[0];
const excess = length - expectedRegularLength;
if (excess <= 0 || excess > 8) {
  throw new Error(`Unsupported fragment anomaly at ${index}: length ${length}, expected ${expectedRegularLength}.`);
}

const passing = [];
for (let trimStart = 0; trimStart <= excess; trimStart++) {
  const trimEnd = excess - trimStart;
  const candidateFragments = [...fragments];
  candidateFragments[index] = fragments[index].slice(trimStart, trimEnd ? -trimEnd : undefined);
  const joined = candidateFragments.join('');
  if (joined.length % 4 !== 0) continue;
  try {
    const archive = Buffer.from(joined, 'base64');
    if (archive[0] !== 0x1f || archive[1] !== 0x8b) continue;
    const payload = JSON.parse(zlib.gunzipSync(archive).toString('utf8'));
    if (!Array.isArray(payload.records) || payload.records.length < 1000) continue;
    passing.push({ trimStart, trimEnd, joined, archive, recordCount: payload.records.length });
  } catch {
    // Candidate rejected; continue searching the bounded boundary space.
  }
}

if (passing.length !== 1) {
  throw new Error(`Seed normalization requires exactly one valid candidate; found ${passing.length}.`);
}

const winner = passing[0];
const normalizedFragment = fragments[index].slice(
  winner.trimStart,
  winner.trimEnd ? -winner.trimEnd : undefined
);
await fs.writeFile(PARTS[index], normalizedFragment);

const evidenceDir = path.join(ROOT, 'evidence', 'content-pipeline');
await fs.mkdir(evidenceDir, { recursive: true });
const evidence = {
  format: 'multiversal-seed-fragment-normalization',
  version: '1.0.0',
  fragment: path.relative(ROOT, PARTS[index]).replaceAll(path.sep, '/'),
  originalLength: length,
  normalizedLength: normalizedFragment.length,
  trimStart: winner.trimStart,
  trimEnd: winner.trimEnd,
  recoveredRecords: winner.recordCount,
  normalizedStreamSha256: sha256(winner.joined),
  archiveSha256: sha256(winner.archive)
};
await fs.writeFile(
  path.join(evidenceDir, 'seed-normalization.json'),
  JSON.stringify(evidence, null, 2) + '\n'
);
console.log(`Normalized seed fragment ${index}: trimStart=${winner.trimStart}, trimEnd=${winner.trimEnd}, records=${winner.recordCount}.`);
