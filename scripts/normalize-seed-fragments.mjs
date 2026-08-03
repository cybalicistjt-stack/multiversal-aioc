import fs from 'node:fs/promises';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';

const ROOT = process.cwd();
const PART_DIR = path.join(ROOT, 'catalog-seed-parts');
const PARTS = [0, 1, 2, 3, 4].map(i => path.join(PART_DIR, `phase1-7.${String(i).padStart(2, '0')}.txt`));
const clean = value => String(value).replace(/[^A-Za-z0-9+/=]/g, '');
const sha256 = value => crypto.createHash('sha256').update(value).digest('hex');
const BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
const REGULAR_LENGTH = 17000;
const WINDOW = 8;

const fragments = await Promise.all(PARTS.map(async file => clean(await fs.readFile(file, 'utf8'))));
const original = fragments.join('');
const boundaries = [];
let offset = 0;
for (let index = 0; index < fragments.length - 1; index++) {
  offset += fragments[index].length;
  boundaries.push({ index, offset });
}

function validateCandidate(encoded) {
  if (!encoded || encoded.length % 4 !== 0) return null;
  if (!/^[A-Za-z0-9+/]+={0,2}$/.test(encoded)) return null;
  try {
    const archive = Buffer.from(encoded, 'base64');
    if (archive[0] !== 0x1f || archive[1] !== 0x8b) return null;
    const payload = JSON.parse(zlib.gunzipSync(archive).toString('utf8'));
    if (!Array.isArray(payload.records) || payload.records.length < 1000) return null;
    return { archive, recordCount: payload.records.length };
  } catch {
    return null;
  }
}

const baseline = validateCandidate(original);
if (baseline) {
  console.log(`Seed stream already valid: ${baseline.recordCount} records.`);
  process.exit(0);
}

const passing = [];
const seen = new Set();
function consider(encoded, repair) {
  const key = sha256(encoded);
  if (seen.has(key)) return;
  seen.add(key);
  const valid = validateCandidate(encoded);
  if (valid) passing.push({ encoded, repair, ...valid });
}

// The observed stream length is one character short of a Base64 quantum.
// Search one-character insertion around each physical fragment boundary.
if (original.length % 4 === 3) {
  for (const boundary of boundaries) {
    const start = Math.max(0, boundary.offset - WINDOW);
    const end = Math.min(original.length, boundary.offset + WINDOW);
    for (let position = start; position <= end; position++) {
      for (const character of BASE64) {
        consider(
          original.slice(0, position) + character + original.slice(position),
          { operation: 'insert', character, position, boundaryAfterFragment: boundary.index }
        );
      }
    }
  }
}

// Defensive bounded alternatives for a single duplicated or substituted character.
if (original.length % 4 === 1) {
  for (const boundary of boundaries) {
    const start = Math.max(0, boundary.offset - WINDOW);
    const end = Math.min(original.length - 1, boundary.offset + WINDOW);
    for (let position = start; position <= end; position++) {
      consider(
        original.slice(0, position) + original.slice(position + 1),
        { operation: 'delete', removed: original[position], position, boundaryAfterFragment: boundary.index }
      );
    }
  }
}
if (original.length % 4 === 0) {
  for (const boundary of boundaries) {
    const start = Math.max(0, boundary.offset - WINDOW);
    const end = Math.min(original.length - 1, boundary.offset + WINDOW);
    for (let position = start; position <= end; position++) {
      for (const character of BASE64) {
        if (character === original[position]) continue;
        consider(
          original.slice(0, position) + character + original.slice(position + 1),
          { operation: 'substitute', removed: original[position], character, position, boundaryAfterFragment: boundary.index }
        );
      }
    }
  }
}

if (passing.length !== 1) {
  const summary = {
    originalLength: original.length,
    modulo4: original.length % 4,
    boundaries,
    candidatesTested: seen.size,
    passingCandidates: passing.map(item => item.repair)
  };
  const evidenceDir = path.join(ROOT, 'evidence', 'content-pipeline');
  await fs.mkdir(evidenceDir, { recursive: true });
  await fs.writeFile(path.join(evidenceDir, 'seed-normalization-search.json'), JSON.stringify(summary, null, 2) + '\n');
  throw new Error(`Seed normalization requires exactly one valid candidate; found ${passing.length} after ${seen.size} bounded repairs.`);
}

const winner = passing[0];
const canonicalParts = [];
let cursor = 0;
for (let index = 0; index < PARTS.length; index++) {
  const remaining = winner.encoded.length - cursor;
  const length = index < PARTS.length - 1 ? REGULAR_LENGTH : remaining;
  canonicalParts.push(winner.encoded.slice(cursor, cursor + length));
  cursor += length;
}
if (cursor !== winner.encoded.length || canonicalParts.slice(0, -1).some(part => part.length !== REGULAR_LENGTH)) {
  throw new Error('Canonical seed repartition failed.');
}
await Promise.all(canonicalParts.map((value, index) => fs.writeFile(PARTS[index], value)));

const evidenceDir = path.join(ROOT, 'evidence', 'content-pipeline');
await fs.mkdir(evidenceDir, { recursive: true });
const evidence = {
  format: 'multiversal-seed-fragment-normalization',
  version: '2.0.0',
  originalLengths: fragments.map(value => value.length),
  normalizedLengths: canonicalParts.map(value => value.length),
  originalStreamLength: original.length,
  normalizedStreamLength: winner.encoded.length,
  repair: winner.repair,
  candidatesTested: seen.size,
  recoveredRecords: winner.recordCount,
  normalizedStreamSha256: sha256(winner.encoded),
  archiveSha256: sha256(winner.archive)
};
await fs.writeFile(path.join(evidenceDir, 'seed-normalization.json'), JSON.stringify(evidence, null, 2) + '\n');
console.log(`Normalized seed stream with ${winner.repair.operation} at ${winner.repair.position}; recovered ${winner.recordCount} records.`);
