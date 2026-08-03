import assert from 'node:assert/strict';
import { ContinuitySnapshotService } from './continuity-snapshot.mjs';

const state = {
  project: { id: 'multiversal' },
  repositories: [{ id: 'multiversal-aioc', fullName: 'cybalicistjt-stack/multiversal-aioc' }],
  milestones: [{ id: 'AIOC-I-002', title: 'Repository Intelligence and Continuity', evidence: ['ci://health'] }],
  workItems: [{ id: 'AIOC-I-002B', title: 'Continuity Snapshot and Session Restore API', status: 'active', evidence: [] }],
  handoffs: [{ id: 'H-1', createdAt: '2026-08-03T03:00:00.000Z', workItemId: 'AIOC-I-002B', nextAction: 'Run continuity validation.', evidence: ['handoff://1'] }],
  active: { repositoryId: 'multiversal-aioc', milestoneId: 'AIOC-I-002', workItemId: 'AIOC-I-002B', branch: 'governance/session-bootstrap-v1' }
};
const healthy = { overall: 'healthy', generatedAt: '2026-08-03T03:30:00.000Z', repositories: [{ id: 'multiversal-aioc', findings: [] }] };
const clock = () => '2026-08-03T03:30:00.000Z';
const service = new ContinuitySnapshotService({ clock, maxAgeMs: 60000 });
const tests = [];
const test = (name, fn) => tests.push({ name, fn });

test('creates a compact verified orientation snapshot', async () => {
  const snapshot = await service.create({ state, health: healthy, capabilityEvidence: ['capability://github-write'], repositoryEvidence: ['repo://head'] });
  assert.equal(snapshot.executionAllowed, true);
  assert.equal(snapshot.orientation.workItem.id, 'AIOC-I-002B');
  assert.equal(snapshot.orientation.nextAction, 'Run continuity validation.');
  assert.ok(snapshot.fingerprint.length >= 8);
});

test('links capability repository milestone and handoff evidence', async () => {
  const snapshot = await service.create({ state, health: healthy, capabilityEvidence: ['capability://github-write'], repositoryEvidence: ['repo://head'] });
  assert.deepEqual(snapshot.evidence, ['capability://github-write', 'ci://health', 'handoff://1', 'repo://head']);
});

test('valid snapshot restores an executable session', async () => {
  const snapshot = await service.create({ state, health: healthy });
  const restored = await service.restore(snapshot, { now: '2026-08-03T03:30:30.000Z', expectedState: state });
  assert.equal(restored.status, 'ready');
  assert.equal(restored.executionAllowed, true);
});

test('expired snapshot triggers recovery', async () => {
  const snapshot = await service.create({ state, health: healthy });
  const restored = await service.restore(snapshot, { now: '2026-08-03T03:32:00.000Z', expectedState: state });
  assert.equal(restored.status, 'recovery-required');
  assert.equal(restored.findings.some(item => item.code === 'snapshot.stale'), true);
});

test('tampered snapshot triggers recovery', async () => {
  const snapshot = await service.create({ state, health: healthy });
  const altered = { ...snapshot, orientation: { ...snapshot.orientation, workItem: { ...snapshot.orientation.workItem, id: 'FALSE' } } };
  const restored = await service.restore(altered, { now: clock(), expectedState: state });
  assert.equal(restored.status, 'recovery-required');
  assert.equal(restored.findings.some(item => item.code === 'snapshot.fingerprint.invalid'), true);
});

test('canonical work item drift blocks execution', async () => {
  const snapshot = await service.create({ state, health: healthy });
  const changed = structuredClone(state);
  changed.active.workItemId = 'AIOC-I-002C';
  const restored = await service.restore(snapshot, { now: clock(), expectedState: changed });
  assert.equal(restored.findings.some(item => item.code === 'snapshot.work-item-drift'), true);
});

test('canonical branch drift blocks execution', async () => {
  const snapshot = await service.create({ state, health: healthy });
  const changed = structuredClone(state);
  changed.active.branch = 'main';
  const restored = await service.restore(snapshot, { now: clock(), expectedState: changed });
  assert.equal(restored.findings.some(item => item.code === 'snapshot.branch-drift'), true);
});

test('blocking repository findings produce a recovery-only snapshot', async () => {
  const health = { overall: 'blocked', repositories: [{ id: 'multiversal-aioc', findings: [{ severity: 'blocking', code: 'repository.write-missing' }] }] };
  const snapshot = await service.create({ state, health });
  assert.equal(snapshot.executionAllowed, false);
  assert.equal(snapshot.recoveryRequired, true);
});

test('recovery findings are preserved and block execution', async () => {
  const snapshot = await service.create({ state, health: healthy, recovery: { required: true, findings: [{ severity: 'blocking', code: 'claim.false-completion' }] } });
  assert.equal(snapshot.blockers.some(item => item.code === 'claim.false-completion'), true);
  const restored = await service.restore(snapshot, { now: clock(), expectedState: state });
  assert.equal(restored.status, 'recovery-required');
});

test('missing active records are rejected at creation', async () => {
  const bad = structuredClone(state);
  bad.workItems = [];
  await assert.rejects(() => service.create({ state: bad, health: healthy }), error => error.code === 'continuity.work-item');
});

test('snapshot output is deterministic for identical inputs and clock', async () => {
  const first = await service.create({ state, health: healthy });
  const second = await service.create({ state, health: healthy });
  assert.equal(first.fingerprint, second.fingerprint);
});

let failures = 0;
for (const { name, fn } of tests) {
  try { await fn(); console.log(`PASS ${name}`); }
  catch (error) { failures += 1; console.error(`FAIL ${name}`); console.error(error); }
}
console.log(`RESULT ${tests.length - failures}/${tests.length} passed`);
if (failures) process.exit(1);
