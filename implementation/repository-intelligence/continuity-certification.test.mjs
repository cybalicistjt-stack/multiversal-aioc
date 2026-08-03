import assert from 'node:assert/strict';
import { certifyContinuity, assertContinuityCertified, inspectDocumentationDrift } from './continuity-certification.mjs';

const state = {
  active: { repositoryId: 'multiversal-aioc', milestoneId: 'AIOC-I-002', workItemId: 'AIOC-I-002C', branch: 'governance/session-bootstrap-v1' },
  workItems: [{ id: 'AIOC-I-002C', title: 'Documentation Drift and Continuity Certification' }]
};
const documents = {
  'governance/current-state/AIOC_CURRENT_STATE.md': { content: 'AIOC-I-002 AIOC-I-002C governance/session-bootstrap-v1' },
  'governance/current-state/SESSION_HANDOFF.md': { content: 'Next: AIOC-I-002C' },
  'governance/roadmaps/AIOC_CANONICAL_ROADMAP.md': { content: 'AIOC-I-002C Documentation Drift and Continuity Certification' },
  'governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md': { content: 'bootstrap' }
};
const snapshot = { status: 'verified', orientation: { workItemId: 'AIOC-I-002C', branch: 'governance/session-bootstrap-v1' } };
const health = { overall: 'healthy' };
const tests = [];
const test = (name, fn) => tests.push({ name, fn });

test('aligned continuity evidence certifies PASS', () => {
  const result = certifyContinuity({ state, documents, snapshot, health, certifiedAt: '2026-08-03T04:00:00.000Z' });
  assert.equal(result.status, 'pass');
  assert.equal(result.executionAllowed, true);
  assert.deepEqual(result.counts, { blocking: 0, warnings: 0 });
});

test('missing required document blocks certification', () => {
  const copy = { ...documents };
  delete copy['governance/current-state/SESSION_HANDOFF.md'];
  const result = certifyContinuity({ state, documents: copy, snapshot, health });
  assert.equal(result.status, 'fail');
  assert.equal(result.findings.some(x => x.code === 'document.missing'), true);
});

test('current-state work-item drift is blocking', () => {
  const copy = { ...documents, 'governance/current-state/AIOC_CURRENT_STATE.md': { content: 'AIOC-I-002 governance/session-bootstrap-v1' } };
  assert.equal(inspectDocumentationDrift({ state, documents: copy, snapshot, health }).some(x => x.code === 'current-state.work-item-drift'), true);
});

test('handoff work-item drift is blocking', () => {
  const copy = { ...documents, 'governance/current-state/SESSION_HANDOFF.md': { content: 'old work' } };
  assert.equal(certifyContinuity({ state, documents: copy, snapshot, health }).executionAllowed, false);
});

test('unverified snapshot blocks execution', () => {
  const result = certifyContinuity({ state, documents, snapshot: { ...snapshot, status: 'recovery-required' }, health });
  assert.equal(result.findings.some(x => x.code === 'snapshot.unverified'), true);
});

test('snapshot branch drift blocks execution', () => {
  const result = certifyContinuity({ state, documents, snapshot: { ...snapshot, orientation: { ...snapshot.orientation, branch: 'main' } }, health });
  assert.equal(result.findings.some(x => x.code === 'snapshot.branch-drift'), true);
});

test('blocked repository health fails certification', () => {
  const result = certifyContinuity({ state, documents, snapshot, health: { overall: 'blocked' } });
  assert.equal(result.status, 'fail');
});

test('degraded health passes with warning', () => {
  const result = certifyContinuity({ state, documents, snapshot, health: { overall: 'degraded' } });
  assert.equal(result.status, 'pass-with-warnings');
  assert.equal(result.executionAllowed, true);
});

test('missing health evidence blocks certification', () => {
  assert.equal(certifyContinuity({ state, documents, snapshot }).executionAllowed, false);
});

test('assertion accepts certified continuity', () => {
  const certificate = certifyContinuity({ state, documents, snapshot, health });
  assert.equal(assertContinuityCertified(certificate), certificate);
});

test('assertion freezes execution after failure', () => {
  const certificate = certifyContinuity({ state, documents: {}, snapshot, health });
  assert.throws(() => assertContinuityCertified(certificate), error => error.code === 'continuity.not-certified');
});

let failed = 0;
for (const { name, fn } of tests) {
  try { await fn(); console.log(`PASS ${name}`); }
  catch (error) { failed += 1; console.error(`FAIL ${name}`); console.error(error); }
}
console.log(`RESULT ${tests.length - failed}/${tests.length} passed`);
if (failed) process.exit(1);
