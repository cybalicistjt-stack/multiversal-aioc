import assert from 'node:assert/strict';
import { certifyContentRelease, assertContentReleaseCertified } from './content-release-certification.mjs';

const base = () => ({
  canonical: { repository: 'cybalicistjt-stack/multiversal-aioc', branch: 'governance/session-bootstrap-v1', workItemId: 'AIOC-I-005C' },
  continuity: { status: 'PASS', evidence: ['continuity://pass'] },
  repositoryHealth: { status: 'healthy', evidence: ['repo://healthy'] },
  packCertification: { status: 'PASS', evidence: ['pack://certified'] },
  pack: { id: 'multiversal.core.test', version: '1.0.0', filename: 'multiversal.core.test.pack' },
  release: {
    repository: 'cybalicistjt-stack/multiversal-aioc', branch: 'governance/session-bootstrap-v1', workItemId: 'AIOC-I-005C',
    releaseId: 'release-001', channel: 'stable', createdAt: '2026-08-03T12:00:00Z',
    artifacts: ['multiversal.core.test.pack'], checksum: 'a'.repeat(64), provenance: ['source://manifest'],
    approvals: [
      { role: 'owner', status: 'approved', evidence: ['approval://owner'] },
      { role: 'release', status: 'approved', evidence: ['approval://release'] }
    ]
  },
  installation: {
    cleanEnvironment: true,
    stages: Object.fromEntries(['preflight','install','activate','verify'].map(stage => [stage, { status: 'PASS', evidence: [`install://${stage}`] }])),
    upgradeTest: { status: 'PASS', evidence: ['install://upgrade'] },
    dependencyResolution: { status: 'PASS', evidence: ['install://dependencies'] }
  },
  rollback: {
    uninstall: { status: 'PASS', evidence: ['rollback://uninstall'] },
    restore: { status: 'PASS', evidence: ['rollback://restore'] },
    dataIntegrity: { status: 'PASS', evidence: ['rollback://integrity'] }
  }
});

const tests = [];
const test = (name, fn) => tests.push({ name, fn });
const mutate = fn => { const input = base(); fn(input); return input; };

test('fully governed release certifies PASS', () => {
  const result = certifyContentRelease(base());
  assert.equal(result.status, 'PASS');
  assert.equal(result.completionAllowed, true);
  assert.equal(result.fingerprint.length, 64);
  assert.equal(assertContentReleaseCertified(result), true);
});

test('continuity failure blocks release', () => assert.equal(certifyContentRelease(mutate(x => x.continuity.status = 'FAIL')).status, 'FAIL'));
test('repository drift blocks release', () => assert.ok(certifyContentRelease(mutate(x => x.release.repository = 'wrong/repo')).findings.some(x => x.code === 'REPOSITORY_DRIFT')));
test('branch drift blocks release', () => assert.ok(certifyContentRelease(mutate(x => x.release.branch = 'main')).findings.some(x => x.code === 'BRANCH_DRIFT')));
test('work item drift blocks release', () => assert.ok(certifyContentRelease(mutate(x => x.release.workItemId = 'wrong')).findings.some(x => x.code === 'WORK_ITEM_DRIFT')));
test('uncertified pack blocks release', () => assert.ok(certifyContentRelease(mutate(x => x.packCertification.status = 'FAIL')).findings.some(x => x.code === 'PACK_NOT_CERTIFIED')));
test('invalid pack identity blocks release', () => assert.ok(certifyContentRelease(mutate(x => x.pack.filename = 'bad.zip')).findings.some(x => x.code === 'INVALID_PACK_IDENTITY')));
test('missing checksum blocks release', () => assert.ok(certifyContentRelease(mutate(x => x.release.checksum = '')).findings.some(x => x.code === 'CHECKSUM_MISSING')));
test('missing provenance blocks release', () => assert.ok(certifyContentRelease(mutate(x => x.release.provenance = [])).findings.some(x => x.code === 'RELEASE_PROVENANCE_MISSING')));
test('failed install stage blocks release', () => assert.ok(certifyContentRelease(mutate(x => x.installation.stages.activate.status = 'FAIL')).findings.some(x => x.code === 'INSTALL_ACTIVATE_FAILED')));
test('clean install proof is required', () => assert.ok(certifyContentRelease(mutate(x => x.installation.cleanEnvironment = false)).findings.some(x => x.code === 'CLEAN_INSTALL_NOT_PROVEN')));
test('upgrade path must pass', () => assert.ok(certifyContentRelease(mutate(x => x.installation.upgradeTest.status = 'FAIL')).findings.some(x => x.code === 'UPGRADE_PATH_NOT_CERTIFIED')));
test('dependency install must pass', () => assert.ok(certifyContentRelease(mutate(x => x.installation.dependencyResolution.status = 'FAIL')).findings.some(x => x.code === 'DEPENDENCY_INSTALL_FAILED')));
test('uninstall must pass', () => assert.ok(certifyContentRelease(mutate(x => x.rollback.uninstall.status = 'FAIL')).findings.some(x => x.code === 'UNINSTALL_NOT_CERTIFIED')));
test('restore must pass', () => assert.ok(certifyContentRelease(mutate(x => x.rollback.restore.status = 'FAIL')).findings.some(x => x.code === 'RESTORE_NOT_CERTIFIED')));
test('rollback integrity must pass', () => assert.ok(certifyContentRelease(mutate(x => x.rollback.dataIntegrity.status = 'FAIL')).findings.some(x => x.code === 'ROLLBACK_DATA_INTEGRITY_FAILED')));
test('stable release approval is required', () => assert.ok(certifyContentRelease(mutate(x => x.release.approvals = x.release.approvals.filter(a => a.role !== 'release'))).findings.some(x => x.code === 'STABLE_RELEASE_APPROVAL_MISSING')));
test('warnings produce PASS WITH WARNINGS and prevent completion', () => {
  const result = certifyContentRelease(mutate(x => x.release.warnings = [{ code: 'DOC_NOTE', message: 'Non-blocking note', evidence: ['note://1'] }]));
  assert.equal(result.status, 'PASS WITH WARNINGS');
  assert.equal(result.executionAllowed, true);
  assert.equal(result.completionAllowed, false);
});
test('failed assertion freezes completion', () => assert.throws(() => assertContentReleaseCertified(certifyContentRelease(mutate(x => x.release.checksum = '')))));
test('certification is deterministic', () => assert.equal(certifyContentRelease(base()).fingerprint, certifyContentRelease(base()).fingerprint));

let passed = 0;
for (const { name, fn } of tests) {
  try { fn(); passed += 1; console.log(`PASS ${name}`); }
  catch (error) { console.error(`FAIL ${name}`); console.error(error); process.exitCode = 1; }
}
console.log(`RESULT ${passed}/${tests.length} passed`);
if (passed !== tests.length) process.exitCode = 1;
