import assert from 'node:assert/strict';
import { certifyDeploymentExecution, requiredRuntimeChecks, requiredRecoveryChecks } from './deployment-runtime-recovery-certification.mjs';

function validInput() {
  const runtimeChecks = requiredRuntimeChecks.map((id) => ({ id, status: 'pass', evidenceId: `ev-runtime-${id}` }));
  const recoveryChecks = requiredRecoveryChecks.map((id) => ({ id, status: 'pass', evidenceId: `ev-recovery-${id}` }));
  const evidence = [...runtimeChecks, ...recoveryChecks].map((check) => ({ id: check.evidenceId, uri: `evidence://${check.evidenceId}` }));
  evidence.push({ id: 'ev-owner', uri: 'evidence://owner-approval' });
  return {
    canonical: { repository: 'cybalicistjt-stack/multiversal-aioc', branch: 'governance/session-bootstrap-v1', workItemId: 'AIOC-I-007B' },
    releaseReadiness: { result: 'PASS', fingerprint: 'ready-fingerprint', artifactChecksum: 'sha256:abc' },
    deployment: {
      repository: 'cybalicistjt-stack/multiversal-aioc', branch: 'governance/session-bootstrap-v1', workItemId: 'AIOC-I-007B',
      releaseId: 'aioc-0.1.0', version: '0.1.0', environment: 'staging', commitSha: 'abc123',
      startedAt: '2026-08-03T05:00:00Z', completedAt: '2026-08-03T05:10:00Z', status: 'succeeded', artifactChecksum: 'sha256:abc'
    },
    runtimeChecks,
    recoveryChecks,
    approvals: [{ role: 'owner', decision: 'approve', evidenceId: 'ev-owner' }],
    evidence
  };
}

const tests = [
  ['clean deployment certifies PASS', (i) => assert.equal(certifyDeploymentExecution(i).result, 'PASS')],
  ['PASS authorizes completion', (i) => assert.equal(certifyDeploymentExecution(i).completionAuthorized, true)],
  ['PASS does not freeze execution', (i) => assert.equal(certifyDeploymentExecution(i).executionFrozen, false)],
  ['readiness must pass', (i) => { i.releaseReadiness.result = 'FAIL'; assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['readiness fingerprint required', (i) => { delete i.releaseReadiness.fingerprint; assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['canonical repository enforced', (i) => { i.deployment.repository = 'wrong/repo'; assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['canonical branch enforced', (i) => { i.deployment.branch = 'wrong'; assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['canonical work item enforced', (i) => { i.deployment.workItemId = 'wrong'; assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['deployment success required', (i) => { i.deployment.status = 'failed'; assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['artifact checksum enforced', (i) => { i.deployment.artifactChecksum = 'sha256:nope'; assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['timestamps required', (i) => { delete i.deployment.completedAt; assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['all runtime checks required', (i) => { i.runtimeChecks.pop(); assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['runtime failures block', (i) => { i.runtimeChecks[0].status = 'fail'; assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['runtime evidence required', (i) => { delete i.runtimeChecks[0].evidenceId; assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['all recovery checks required', (i) => { i.recoveryChecks.pop(); assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['recovery failures block', (i) => { i.recoveryChecks[0].status = 'fail'; assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['owner approval required', (i) => { i.approvals = []; assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['approval evidence must resolve', (i) => { i.evidence = i.evidence.filter((e) => e.id !== 'ev-owner'); assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['check evidence must resolve', (i) => { i.evidence = i.evidence.filter((e) => e.id !== i.runtimeChecks[0].evidenceId); assert.equal(certifyDeploymentExecution(i).result, 'FAIL'); }],
  ['fingerprint is deterministic', (i) => assert.equal(certifyDeploymentExecution(i).fingerprint, certifyDeploymentExecution(structuredClone(i)).fingerprint)]
];

let passed = 0;
for (const [name, test] of tests) {
  try { test(validInput()); console.log(`PASS ${name}`); passed += 1; }
  catch (error) { console.error(`FAIL ${name}`); console.error(error); }
}
console.log(`RESULT ${passed}/${tests.length} passed`);
if (passed !== tests.length) process.exit(1);
