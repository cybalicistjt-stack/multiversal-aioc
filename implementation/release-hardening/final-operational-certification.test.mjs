import assert from 'node:assert/strict';
import { certifyAiocOperationalRelease, FINAL_OPERATIONAL_REQUIREMENTS } from './final-operational-certification.mjs';

const evidence = id => ({ evidenceId: id, evidenceUri: `evidence://${id}`, observedAt: '2026-08-03T00:00:00Z' });
const valid = () => ({
  certificateId: 'AIOC-FINAL-001',
  continuity: { result: 'PASS' },
  repositoryHealth: { status: 'healthy' },
  canonical: { repository: 'cybalicistjt-stack/multiversal-aioc', branch: 'governance/session-bootstrap-v1', workItemId: 'AIOC-I-007C' },
  milestones: FINAL_OPERATIONAL_REQUIREMENTS.milestones.map(id => ({ id, result: 'PASS', ...evidence(`milestone-${id}`) })),
  capabilities: FINAL_OPERATIONAL_REQUIREMENTS.capabilities.map(id => ({ id, available: true, ...evidence(`capability-${id}`) })),
  deploymentCertification: { result: 'PASS', fingerprint: 'deploy-fingerprint', ...evidence('deployment') },
  ownerApproval: { decision: 'approved', ...evidence('owner-approval') },
  operationalHandoff: { nextAction: 'Operate AIOC and begin governed Multiversal application delivery.', supportModel: 'repository-governed', recoveryEntryPoint: 'governance/current-state/SESSION_HANDOFF.md', ...evidence('handoff') },
  openRisks: []
});

const tests = [];
const test = (name, fn) => tests.push([name, fn]);

test('clean evidence produces PASS', () => {
  const result = certifyAiocOperationalRelease(valid());
  assert.equal(result.result, 'PASS');
  assert.equal(result.completionAuthorized, true);
  assert.equal(result.executionFrozen, false);
});

test('fingerprint is deterministic', () => {
  assert.equal(certifyAiocOperationalRelease(valid()).fingerprint, certifyAiocOperationalRelease(valid()).fingerprint);
});

test('continuity failure blocks completion', () => {
  const input = valid(); input.continuity.result = 'FAIL';
  assert.equal(certifyAiocOperationalRelease(input).result, 'FAIL');
});

test('unhealthy repository blocks completion', () => {
  const input = valid(); input.repositoryHealth.status = 'degraded';
  assert.equal(certifyAiocOperationalRelease(input).completionAuthorized, false);
});

test('missing canonical binding blocks completion', () => {
  const input = valid(); delete input.canonical.branch;
  assert.equal(certifyAiocOperationalRelease(input).result, 'FAIL');
});

test('missing milestone blocks completion', () => {
  const input = valid(); input.milestones.pop();
  assert.equal(certifyAiocOperationalRelease(input).result, 'FAIL');
});

test('non-pass milestone blocks completion', () => {
  const input = valid(); input.milestones[0].result = 'FAIL';
  assert.equal(certifyAiocOperationalRelease(input).result, 'FAIL');
});

test('milestone without evidence blocks completion', () => {
  const input = valid(); delete input.milestones[0].evidenceUri;
  assert.equal(certifyAiocOperationalRelease(input).result, 'FAIL');
});

test('missing capability blocks completion', () => {
  const input = valid(); input.capabilities.pop();
  assert.equal(certifyAiocOperationalRelease(input).result, 'FAIL');
});

test('unavailable capability blocks completion', () => {
  const input = valid(); input.capabilities[0].available = false;
  assert.equal(certifyAiocOperationalRelease(input).result, 'FAIL');
});

test('deployment certification must pass', () => {
  const input = valid(); input.deploymentCertification.result = 'FAIL';
  assert.equal(certifyAiocOperationalRelease(input).result, 'FAIL');
});

test('deployment fingerprint is required', () => {
  const input = valid(); delete input.deploymentCertification.fingerprint;
  assert.equal(certifyAiocOperationalRelease(input).result, 'FAIL');
});

test('owner approval is required', () => {
  const input = valid(); input.ownerApproval.decision = 'pending';
  assert.equal(certifyAiocOperationalRelease(input).result, 'FAIL');
});

test('operational handoff is required', () => {
  const input = valid(); delete input.operationalHandoff.recoveryEntryPoint;
  assert.equal(certifyAiocOperationalRelease(input).result, 'FAIL');
});

test('high risk blocks completion', () => {
  const input = valid(); input.openRisks = [{ id: 'R-1', severity: 'high' }];
  assert.equal(certifyAiocOperationalRelease(input).result, 'FAIL');
});

test('low risk produces warning and freezes completion', () => {
  const input = valid(); input.openRisks = [{ id: 'R-2', severity: 'low' }];
  const result = certifyAiocOperationalRelease(input);
  assert.equal(result.result, 'PASS WITH WARNINGS');
  assert.equal(result.executionFrozen, true);
});

test('successful certificate projects next action', () => {
  assert.match(certifyAiocOperationalRelease(valid()).nextAction, /Operate AIOC/);
});

test('failed certificate projects recovery action', () => {
  const input = valid(); input.ownerApproval = null;
  assert.match(certifyAiocOperationalRelease(input).nextAction, /Resolve findings/);
});

let passed = 0;
for (const [name, fn] of tests) {
  try { fn(); console.log(`PASS ${name}`); passed += 1; }
  catch (error) { console.error(`FAIL ${name}`); console.error(error); }
}
console.log(`RESULT ${passed}/${tests.length} passed`);
if (passed !== tests.length) process.exit(1);
