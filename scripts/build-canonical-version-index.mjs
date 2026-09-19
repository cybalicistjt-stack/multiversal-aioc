import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const ROOT = process.cwd();
const SOURCE_DIR = path.join(ROOT, 'content-source');
const OUT = path.join(ROOT, 'content-db', 'version-index.json');
const BASELINE = 'phase-1-8-canonical-objects.json';
const SUPPLEMENTAL_FORMAT = 'multiversal-canonical-content-source';
const ALLOWED_STATUSES = new Set([
  'owner-approved-canonical-incorporation',
  'owner-approved-canonical-replacement'
]);

const sha256 = value => `sha256:${crypto.createHash('sha256').update(value).digest('hex')}`;

function unwrap(payload) {
  if (Array.isArray(payload)) return payload;
  for (const key of ['records', 'objects', 'gameObjects', 'entries', 'content']) {
    if (Array.isArray(payload?.[key])) return payload[key];
  }
  return payload && typeof payload === 'object' ? [payload] : [];
}

function objectOf(raw) { return raw?.gameObject || raw?.object || raw; }
function stableIdOf(raw) {
  const object = objectOf(raw);
  return object?.id || object?.stableId || raw?.stableId || raw?.refId || '';
}
function versionOf(raw) {
  const object = objectOf(raw);
  const version = object?.contentVersion ?? raw?.contentVersion ?? null;
  return typeof version === 'string' && version.trim() ? version.trim() : null;
}

const files = (await fs.readdir(SOURCE_DIR)).filter(name => name.endsWith('.json')).sort();
const versions = [];
const keys = new Set();

for (const name of files) {
  const sourcePath = `content-source/${name}`;
  const text = await fs.readFile(path.join(SOURCE_DIR, name), 'utf8');
  const payload = JSON.parse(text);
  let sourceClass = null;
  if (name === BASELINE) {
    if (payload.format !== 'multiversal-content-source-bundle') continue;
    sourceClass = 'baseline';
  } else {
    if (payload.format !== SUPPLEMENTAL_FORMAT || !ALLOWED_STATUSES.has(payload.status)) continue;
    sourceClass = payload.status === 'owner-approved-canonical-replacement' ? 'replacement' : 'supplemental';
  }
  const digest = sha256(text);
  for (const raw of unwrap(payload)) {
    const stableId = stableIdOf(raw);
    const contentVersion = versionOf(raw);
    if (!stableId || !contentVersion) continue;
    const key = `${stableId}@${contentVersion}`;
    if (keys.has(key)) throw new Error(`Duplicate canonical version identity: ${key}`);
    keys.add(key);
    versions.push({
      key,
      stableId,
      contentVersion,
      sourceClass,
      sourcePath,
      sourceDigest: digest,
      gameObject: objectOf(raw)
    });
  }
}

versions.sort((a, b) => a.stableId.localeCompare(b.stableId) || a.contentVersion.localeCompare(b.contentVersion));
let generatedAt = new Date().toISOString();
try {
  const previous = JSON.parse(await fs.readFile(OUT, 'utf8'));
  if (
    previous.versionCount === versions.length &&
    JSON.stringify(previous.versions) === JSON.stringify(versions) &&
    typeof previous.generatedAt === 'string' &&
    previous.generatedAt
  ) {
    generatedAt = previous.generatedAt;
  }
} catch {
  // No prior version index: the first material generation may stamp wall-clock time.
}
const payload = {
  format: 'multiversal-canonical-version-index',
  version: '1.0.0',
  generatedAt,
  purpose: 'Resolve immutable exact-version canonical references independently of the effective-current record projection.',
  gameReadinessAssessed: false,
  versionCount: versions.length,
  versions
};
await fs.writeFile(OUT, JSON.stringify(payload, null, 2) + '\n');
console.log(`Generated canonical version index: ${versions.length} exact versions.`);
