import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { loadCanonicalContentSource } from '../../scripts/lib/canonical-content-source.mjs';

const root = await fs.mkdtemp(path.join(os.tmpdir(), 'mv-canonical-replacement-'));
const sourceDir = path.join(root, 'content-source');
await fs.mkdir(sourceDir, { recursive: true });

const baseline = Array.from({ length: 487 }, (_, index) => ({
  id: index === 0 ? 'mv.core.item.weapon.battleaxe' : `mv.test.baseline.${String(index).padStart(3, '0')}`,
  name: index === 0 ? 'Battleaxe' : `Baseline ${index}`,
  objectType: index === 0 ? 'mv.object.item-definition' : 'mv.object.test-definition',
  schemaVersion: '1.0.0',
  contentVersion: index === 0 ? '' : '1.0.0'
}));
await fs.writeFile(path.join(sourceDir, 'phase-1-8-canonical-objects.json'), JSON.stringify({
  format: 'multiversal-content-source-bundle',
  bundleId: 'test-baseline',
  records: baseline
}));

await fs.writeFile(path.join(sourceDir, 'append.json'), JSON.stringify({
  format: 'multiversal-canonical-content-source',
  version: '1.0.0',
  bundleId: 'test-append',
  status: 'owner-approved-canonical-incorporation',
  records: [{
    id: 'mv.test.appended',
    name: 'Appended',
    objectType: 'mv.object.test-definition',
    schemaVersion: '1.0.0',
    contentVersion: '1.0.0'
  }]
}));

await fs.writeFile(path.join(sourceDir, 'replace-item.json'), JSON.stringify({
  format: 'multiversal-canonical-content-source',
  version: '1.0.0',
  bundleId: 'test-item-completion-replacement',
  status: 'owner-approved-canonical-replacement',
  records: [{
    id: 'mv.core.item.weapon.battleaxe',
    name: 'Battleaxe',
    objectType: 'mv.object.item-definition',
    schemaVersion: '1.0.0',
    contentVersion: '1.0.0',
    replacementOf: {
      stableId: 'mv.core.item.weapon.battleaxe',
      expectedContentVersion: null,
      reason: 'Item completion materializes an exact version for an existing baseline identity.'
    }
  }]
}));

const sourceSet = await loadCanonicalContentSource(root);
assert.equal(sourceSet.baselineRecordCount, 487);
assert.equal(sourceSet.appendedRecordCount, 1);
assert.equal(sourceSet.replacementRecordCount, 1);
assert.equal(sourceSet.recordCount, 488, 'replacement must not increase the effective unique-object count');
const battleaxe = sourceSet.entries.find(entry => entry.raw.id === 'mv.core.item.weapon.battleaxe');
assert.ok(battleaxe, 'replacement target must remain present');
assert.equal(battleaxe.raw.contentVersion, '1.0.0');
assert.equal(battleaxe.sourceClass, 'replacement');
assert.equal(battleaxe.replaces?.stableId, 'mv.core.item.weapon.battleaxe');
assert.equal(battleaxe.replaces?.contentVersion, null);

// An ordinary incorporation bundle must never silently overwrite an existing identity.
await fs.writeFile(path.join(sourceDir, 'bad-duplicate.json'), JSON.stringify({
  format: 'multiversal-canonical-content-source',
  version: '1.0.0',
  bundleId: 'test-bad-duplicate',
  status: 'owner-approved-canonical-incorporation',
  records: [{
    id: 'mv.core.item.weapon.battleaxe',
    name: 'Bad Duplicate',
    objectType: 'mv.object.item-definition',
    schemaVersion: '1.0.0',
    contentVersion: '9.9.9'
  }]
}));
await assert.rejects(
  () => loadCanonicalContentSource(root),
  /Duplicate canonical stable ID|already exists|replacement/i,
  'unmarked duplicates must remain a hard failure'
);

await fs.rm(root, { recursive: true, force: true });
console.log('Canonical content governed replacement contract: PASS');
