import assert from 'node:assert/strict';
import { certifyContentPack, assertContentPackCertified } from './content-pack-certification.mjs';

const base = () => ({
  canonical: { repository: 'cybalicistjt-stack/multiversal-aioc', branch: 'governance/session-bootstrap-v1', milestoneId: 'AIOC-I-005', workItemId: 'AIOC-I-005B' },
  continuityCertification: { result: 'PASS', evidence: ['continuity'] },
  repositoryHealth: { status: 'healthy', evidence: ['health'] },
  conversion: { sourceFormat: 'legacy-json', targetFormat: 'multiversal-pack-v1', converterVersion: '1.0.0', result: 'PASS', evidence: ['conversion'] },
  availableDependencies: ['core.rules@1'],
  pack: {
    repository: 'cybalicistjt-stack/multiversal-aioc', branch: 'governance/session-bootstrap-v1', milestoneId: 'AIOC-I-005', workItemId: 'AIOC-I-005B',
    id: 'test.creatures', version: '0.1.0', extension: '.pack',
    entities: [{ id: 'creature.alpha' }, { id: 'creature.beta' }],
    manifest: { entities: ['creature.alpha', 'creature.beta'] }, dependencies: ['core.rules@1'],
    provenance: ['source-a'], installTest: { result: 'PASS', evidence: ['install'] }, uninstallTest: { result: 'PASS', evidence: ['uninstall'] }
  }
});

const tests = [
  ['valid pack passes', value => assert.equal(certifyContentPack(value).result, 'PASS')],
  ['continuity blocks', value => { value.continuityCertification.result = 'FAIL'; assert.equal(certifyContentPack(value).result, 'FAIL'); }],
  ['repository health blocks', value => { value.repositoryHealth.status = 'blocked'; assert.equal(certifyContentPack(value).result, 'FAIL'); }],
  ['canonical branch mismatch blocks', value => { value.pack.branch = 'main'; assert.equal(certifyContentPack(value).result, 'FAIL'); }],
  ['conversion failure blocks', value => { value.conversion.result = 'FAIL'; assert.equal(certifyContentPack(value).result, 'FAIL'); }],
  ['pack extension is governed', value => { value.pack.extension = '.zip'; assert.equal(certifyContentPack(value).result, 'FAIL'); }],
  ['duplicate entity ids block', value => { value.pack.entities[1].id = 'creature.alpha'; assert.equal(certifyContentPack(value).result, 'FAIL'); }],
  ['manifest omissions block', value => { value.pack.manifest.entities.pop(); assert.equal(certifyContentPack(value).result, 'FAIL'); }],
  ['manifest orphans block', value => { value.pack.manifest.entities.push('creature.missing'); assert.equal(certifyContentPack(value).result, 'FAIL'); }],
  ['unresolved dependency blocks', value => { value.pack.dependencies.push('world.unknown@1'); assert.equal(certifyContentPack(value).result, 'FAIL'); }],
  ['missing provenance blocks', value => { value.pack.provenance = []; assert.equal(certifyContentPack(value).result, 'FAIL'); }],
  ['install failure blocks', value => { value.pack.installTest.result = 'FAIL'; assert.equal(certifyContentPack(value).result, 'FAIL'); }],
  ['uninstall failure blocks', value => { value.pack.uninstallTest.result = 'FAIL'; assert.equal(certifyContentPack(value).result, 'FAIL'); }],
  ['warnings produce pass with warnings', value => { value.pack.warnings = ['legacy alias retained']; assert.equal(certifyContentPack(value).result, 'PASS WITH WARNINGS'); }],
  ['assertion accepts certified pack', value => assert.equal(assertContentPackCertified(certifyContentPack(value)).completionAllowed, true)],
  ['assertion freezes failed pack', value => { value.pack.provenance = []; assert.throws(() => assertContentPackCertified(certifyContentPack(value))); }]
];

let passed = 0;
for (const [name, test] of tests) {
  try { test(base()); passed += 1; console.log(`PASS ${name}`); }
  catch (error) { console.error(`FAIL ${name}`); throw error; }
}
console.log(`RESULT ${passed}/${tests.length} passed`);
