import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import {
  buildSessionOrientation,
  detectContinuityConflicts,
  buildRecoveryPlan,
  createDecisionRecord,
  createSessionHandoff
} from './recovery-services.mjs';

const state = JSON.parse(await readFile(new URL('../project-state/canonical-project-state.seed.json', import.meta.url), 'utf8'));
const clone = value => JSON.parse(JSON.stringify(value));
const tests = [];
const test = (name, fn) => tests.push({ name, fn });

test('orientation restores active repository milestone and work item', () => {
  const orientation = buildSessionOrientation(state);
  assert.equal(orientation.active.repository.id, state.active.repositoryId);
  assert.equal(orientation.active.milestone.id, state.active.milestoneId);
  assert.equal(orientation.active.workItem.id, state.active.workItemId);
});

test('orientation uses latest handoff action when available', () => {
  const candidate = clone(state);
  candidate.handoffs = [
    { id: 'H-1', createdAt: '2026-01-01T00:00:00.000Z', workItemId: state.active.workItemId, summary: 'old', nextAction: 'old action', evidence: [] },
    { id: 'H-2', createdAt: '2026-01-02T00:00:00.000Z', workItemId: state.active.workItemId, summary: 'new', nextAction: 'new action', evidence: [] }
  ];
  assert.equal(buildSessionOrientation(candidate).nextAction, 'new action');
});

test('false completion claims are blocking findings', () => {
  const findings = detectContinuityConflicts(state, [{ id: 'C-1', type: 'work-complete', workItemId: state.active.workItemId }]);
  assert.equal(findings.some(item => item.code === 'claim.false-completion' && item.severity === 'error'), true);
});

test('verified completion claims do not produce false-completion findings', () => {
  const completed = state.workItems.find(item => item.status === 'complete');
  const findings = detectContinuityConflicts(state, [{ id: 'C-2', type: 'work-complete', workItemId: completed.id }]);
  assert.equal(findings.some(item => item.code === 'claim.false-completion'), false);
});

test('repository writes require live push capability evidence', () => {
  const findings = detectContinuityConflicts(state, [{ id: 'C-3', type: 'repository-write', repositoryId: 'multiversal-aioc', commitSha: 'abc' }], []);
  assert.equal(findings.some(item => item.code === 'claim.unverified-write'), true);
});

test('verified repository write capability clears capability finding', () => {
  const observations = [{ repositoryId: 'multiversal-aioc', headSha: 'abc', capabilities: { read: true, push: true, admin: true } }];
  const findings = detectContinuityConflicts(state, [{ id: 'C-4', type: 'repository-write', repositoryId: 'multiversal-aioc', commitSha: 'abc' }], observations);
  assert.equal(findings.some(item => item.code === 'claim.unverified-write'), false);
});

test('commit drift is surfaced as a warning', () => {
  const observations = [{ repositoryId: 'multiversal-aioc', headSha: 'def', capabilities: { read: true, push: true } }];
  const findings = detectContinuityConflicts(state, [{ id: 'C-5', type: 'repository-write', repositoryId: 'multiversal-aioc', commitSha: 'abc' }], observations);
  assert.equal(findings.some(item => item.code === 'claim.commit-drift' && item.severity === 'warning'), true);
});

test('recovery plan freezes writes for broken canonical invariants', () => {
  const plan = buildRecoveryPlan(state, [{ severity: 'error', code: 'state.active-count', message: 'broken' }]);
  assert.equal(plan.blocking, true);
  assert.equal(plan.steps[0].action, 'freeze-writes');
});

test('recovery plan reopens unverified completion', () => {
  const plan = buildRecoveryPlan(state, [{ severity: 'error', code: 'claim.false-completion', message: 'not complete' }]);
  assert.equal(plan.steps.some(step => step.action === 'reopen-unverified-work'), true);
});

test('clean recovery plan continues active work', () => {
  const plan = buildRecoveryPlan(state, []);
  assert.equal(plan.blocking, false);
  assert.equal(plan.steps[0].action, 'continue-active-work');
});

test('resolved decisions require rationale', () => {
  assert.throws(() => createDecisionRecord({ id: 'D-1', title: 'Decision', status: 'approved' }), error => error.code === 'decision.rationale');
});

test('approved decision records authority rationale and evidence', () => {
  const record = createDecisionRecord({ id: 'D-2', title: 'Repository first', status: 'approved', rationale: 'Prevents context loss.', evidence: ['test://decision'] });
  assert.equal(record.status, 'approved');
  assert.equal(record.evidence.length, 1);
  assert.ok(record.resolvedAt);
});

test('handoff binds next action to current canonical work item', () => {
  const handoff = createSessionHandoff({ id: 'H-TEST', state, summary: 'Session complete', nextAction: 'Continue implementation', evidence: ['test://handoff'] });
  assert.equal(handoff.workItemId, state.active.workItemId);
  assert.ok(handoff.orientationFingerprint.includes(state.active.workItemId));
});

let failures = 0;
for (const { name, fn } of tests) {
  try {
    await fn();
    console.log(`PASS ${name}`);
  } catch (error) {
    failures += 1;
    console.error(`FAIL ${name}`);
    console.error(error);
  }
}
console.log(`RESULT ${tests.length - failures}/${tests.length} passed`);
if (failures) process.exit(1);
