import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const BASELINE_FILE = 'phase-1-8-canonical-objects.json';
const BASELINE_EXPECTED_RECORDS = 487;
const SUPPLEMENTAL_FORMAT = 'multiversal-canonical-content-source';
const INCORPORATION_STATUS = 'owner-approved-canonical-incorporation';
const REPLACEMENT_STATUS = 'owner-approved-canonical-replacement';

const sha256 = value => `sha256:${crypto.createHash('sha256').update(value).digest('hex')}`;

function unwrapObjects(payload) {
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
function contentVersionOf(raw) {
  const object = objectOf(raw);
  const value = object?.contentVersion ?? raw?.contentVersion ?? null;
  return typeof value === 'string' && value.trim() ? value.trim() : null;
}
function semver(value, label) {
  const match = String(value || '').match(/^(\d+)\.(\d+)\.(\d+)$/);
  if (!match) throw new Error(`${label} must be an exact semantic version (x.y.z); found ${JSON.stringify(value)}.`);
  return match.slice(1).map(Number);
}
function compareSemver(a, b) {
  for (let i = 0; i < 3; i++) if (a[i] !== b[i]) return a[i] - b[i];
  return 0;
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
  const baselineEntries = baselineRecords.map(raw => ({
    raw,
    sourceClass: 'baseline',
    sourcePath: `content-source/${BASELINE_FILE}`,
    sourceDigest: sources[0].sourceDigest,
    sourceBundleId: sources[0].bundleId,
    sourceBundlePart: null,
    replaces: null
  }));

  const appendedEntries = [];
  const replacementEntries = [];
  async function discoverSupplementalJson(relativeDir = '') {
    const absoluteDir = path.join(sourceDir, relativeDir);
    const dirents = await fs.readdir(absoluteDir, { withFileTypes: true });
    const found = [];
    for (const dirent of dirents) {
      const relativePath = path.join(relativeDir, dirent.name);
      if (dirent.isDirectory()) {
        found.push(...await discoverSupplementalJson(relativePath));
      } else if (dirent.isFile() && dirent.name.endsWith('.json') && relativePath !== BASELINE_FILE) {
        found.push(relativePath);
      }
    }
    return found;
  }

  const names = (await discoverSupplementalJson()).sort();

  for (const name of names) {
    const filePath = path.join(sourceDir, name);
    const text = await fs.readFile(filePath, 'utf8');
    const payload = JSON.parse(text);
    if (payload.format !== SUPPLEMENTAL_FORMAT) continue;
    if (![INCORPORATION_STATUS, REPLACEMENT_STATUS].includes(payload.status)) {
      throw new Error(`Supplemental canonical bundle ${name} has unsupported status: ${payload.status}`);
    }
    const records = unwrapObjects(payload);
    if (!records.length) throw new Error(`Supplemental canonical bundle ${name} has no records.`);
    const sourceClass = payload.status === REPLACEMENT_STATUS ? 'replacement' : 'supplemental';
    const source = {
      sourceClass,
      sourcePath: `content-source/${name}`,
      sourceDigest: sha256(text),
      bundleId: payload.bundleId || name.replace(/\.json$/i, ''),
      bundlePart: payload.authority?.bundlePart || payload.bundlePart || null,
      recordCount: records.length
    };
    sources.push(source);
    for (const raw of records) {
      const entry = {
        raw,
        sourceClass,
        sourcePath: source.sourcePath,
        sourceDigest: source.sourceDigest,
        sourceBundleId: source.bundleId,
        sourceBundlePart: source.bundlePart,
        replaces: null
      };
      if (sourceClass === 'replacement') replacementEntries.push(entry);
      else appendedEntries.push(entry);
    }
  }

  const effectiveByStableId = new Map();
  for (const entry of baselineEntries) {
    const stableId = stableIdOf(entry.raw);
    if (!stableId) throw new Error('Baseline canonical record has no stable ID.');
    if (effectiveByStableId.has(stableId)) throw new Error(`Duplicate canonical stable ID in baseline: ${stableId}`);
    effectiveByStableId.set(stableId, entry);
  }
  for (const entry of appendedEntries) {
    const stableId = stableIdOf(entry.raw);
    if (!stableId) throw new Error('Supplemental canonical record has no stable ID.');
    if (effectiveByStableId.has(stableId)) {
      throw new Error(`Duplicate canonical stable ID ${stableId}; existing identities require an owner-approved canonical replacement bundle.`);
    }
    effectiveByStableId.set(stableId, entry);
  }

  const unresolved = [...replacementEntries];
  while (unresolved.length) {
    const applicable = [];
    for (const entry of unresolved) {
      const stableId = stableIdOf(entry.raw);
      const replacementOf = objectOf(entry.raw)?.replacementOf || entry.raw?.replacementOf;
      if (!stableId || !replacementOf || replacementOf.stableId !== stableId) {
        throw new Error(`Replacement record ${stableId || '<missing>'} must declare replacementOf.stableId equal to its own stable ID.`);
      }
      const current = effectiveByStableId.get(stableId);
      if (!current) continue;
      const currentVersion = contentVersionOf(current.raw);
      const expectedVersion = replacementOf.expectedContentVersion ?? null;
      if (expectedVersion === currentVersion) applicable.push({ entry, current, stableId, currentVersion });
    }
    if (!applicable.length) {
      const details = unresolved.map(entry => {
        const id = stableIdOf(entry.raw);
        const expected = objectOf(entry.raw)?.replacementOf?.expectedContentVersion ?? entry.raw?.replacementOf?.expectedContentVersion ?? null;
        const current = effectiveByStableId.get(id);
        return `${id} expected ${JSON.stringify(expected)} current ${JSON.stringify(current ? contentVersionOf(current.raw) : '<missing>')}`;
      });
      throw new Error(`Canonical replacement predecessor/version mismatch: ${details.join('; ')}`);
    }
    const byTarget = new Map();
    for (const candidate of applicable) {
      const list = byTarget.get(candidate.stableId) || [];
      list.push(candidate);
      byTarget.set(candidate.stableId, list);
    }
    for (const [stableId, candidates] of byTarget.entries()) {
      if (candidates.length > 1) throw new Error(`Forked canonical replacement chain for ${stableId}.`);
      const { entry, current, currentVersion } = candidates[0];
      const nextVersion = contentVersionOf(entry.raw);
      semver(nextVersion, `Replacement ${stableId} contentVersion`);
      if (currentVersion !== null) {
        if (compareSemver(semver(nextVersion, `Replacement ${stableId} contentVersion`), semver(currentVersion, `Existing ${stableId} contentVersion`)) <= 0) {
          throw new Error(`Replacement ${stableId} contentVersion ${nextVersion} must be greater than ${currentVersion}.`);
        }
      }
      entry.replaces = {
        stableId,
        contentVersion: currentVersion,
        sourcePath: current.sourcePath,
        sourceDigest: current.sourceDigest
      };
      effectiveByStableId.set(stableId, entry);
      unresolved.splice(unresolved.indexOf(entry), 1);
    }
  }

  const entries = [...effectiveByStableId.values()];
  const sourceSetProjection = sources.map(source => [
    source.sourceClass,
    source.sourcePath,
    source.sourceDigest,
    source.bundleId,
    source.bundlePart,
    source.recordCount
  ]);
  const sourceSetDigest = sha256(JSON.stringify(sourceSetProjection));

  return {
    baselineRecordCount: baselineEntries.length,
    appendedRecordCount: appendedEntries.length,
    replacementRecordCount: replacementEntries.length,
    supplementalRecordCount: appendedEntries.length + replacementEntries.length,
    recordCount: entries.length,
    sourceSetDigest,
    sources,
    entries
  };
}

export {
  BASELINE_EXPECTED_RECORDS,
  BASELINE_FILE,
  SUPPLEMENTAL_FORMAT,
  INCORPORATION_STATUS,
  REPLACEMENT_STATUS
};
