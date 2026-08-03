import assert from 'node:assert/strict';
import { GovernedOrchestrationService } from './orchestration-service.mjs';

const state = {
  workItems: [
    { id: 'AIOC-I-003B', status: 'active' },
    { id: 'AIOC-I-003C', status: 'planned' }
  ]
};
const certification = { result: 'PASS', executionAllowed: true };
const capabilities = [
  { capability: 'github.read', available: true },
  { capability: 'github.write', available: true }
];
const tests = [];
const test = (name, fn) => tests.push({ name, fn });
const make = options => new GovernedOrchestrationService({ canonicalState: state, certification, capabilityEvidence: capabilities, ...options });

test('certification failure freezes enqueue', () => {
  const service = new GovernedOrchestrationService({ canonicalState: state, certification: { result: 'FAIL', executionAllowed: false } });
  assert.throws(() => service.enqueue({ id: 'q1', workItemId: 'AIOC-I-003B', agentRole: 'developer', operation: 'build' }), e => e.code === 'orchestration.frozen');
});

test('only active governed work can be queued', () => {
  const service = make();
  assert.throws(() => service.enqueue({ id: 'q1', workItemId: 'AIOC-I-003C', agentRole: 'developer', operation: 'build' }), e => e.code === 'queue.not-active');
});

test('missing required capability blocks queue item', () => {
  const service = make();
  assert.throws(() => service.enqueue({ id: 'q1', workItemId: 'AIOC-I-003B', agentRole: 'developer', operation: 'build', requires: ['secrets.write'] }), e => e.code === 'queue.capability');
});

test('queue ordering is deterministic by priority sequence and id', () => {
  const service = make();
  service.enqueue({ id: 'q-c', workItemId: 'AIOC-I-003B', agentRole: 'reviewer', operation: 'review', priority: 50, sequence: 2 });
  service.enqueue({ id: 'q-b', workItemId: 'AIOC-I-003B', agentRole: 'tester', operation: 'test', priority: 80, sequence: 3 });
  service.enqueue({ id: 'q-a', workItemId: 'AIOC-I-003B', agentRole: 'developer', operation: 'build', priority: 80, sequence: 1 });
  assert.equal(service.nextDispatchable().id, 'q-a');
});

test('duplicate queue ids are rejected', () => {
  const service = make();
  service.enqueue({ id: 'q1', workItemId: 'AIOC-I-003B', agentRole: 'developer', operation: 'build' });
  assert.throws(() => service.enqueue({ id: 'q1', workItemId: 'AIOC-I-003B', agentRole: 'tester', operation: 'test' }), e => e.code === 'queue.duplicate');
});

test('dispatch creates a lease and append-only event', async () => {
  const service = make();
  service.enqueue({ id: 'q1', workItemId: 'AIOC-I-003B', agentRole: 'developer', operation: 'build', evidence: ['work-order://003B'] });
  const result = await service.dispatchNext({ workerId: 'agent-1' });
  assert.equal(result.job.status, 'dispatched');
  assert.equal(result.lease.workerId, 'agent-1');
  assert.equal(service.snapshot().dispatchLedger.length, 1);
});

test('persistence failure rolls dispatch back', async () => {
  const service = make({ persist: async () => { throw Object.assign(new Error('disk'), { code: 'persist.failed' }); } });
  service.enqueue({ id: 'q1', workItemId: 'AIOC-I-003B', agentRole: 'developer', operation: 'build' });
  await assert.rejects(() => service.dispatchNext({ workerId: 'agent-1' }), e => e.code === 'persist.failed');
  assert.equal(service.snapshot().queue[0].status, 'queued');
  assert.equal(service.snapshot().dispatchLedger.length, 0);
});

test('only lease owner may acknowledge', async () => {
  const service = make();
  service.enqueue({ id: 'q1', workItemId: 'AIOC-I-003B', agentRole: 'developer', operation: 'build' });
  await service.dispatchNext({ workerId: 'agent-1' });
  await assert.rejects(() => service.acknowledge('q1', { workerId: 'agent-2', outcome: 'failed' }), e => e.code === 'dispatch.lease');
});

test('successful completion requires evidence', async () => {
  const service = make();
  service.enqueue({ id: 'q1', workItemId: 'AIOC-I-003B', agentRole: 'developer', operation: 'build' });
  await service.dispatchNext({ workerId: 'agent-1' });
  await assert.rejects(() => service.acknowledge('q1', { workerId: 'agent-1', outcome: 'complete' }), e => e.code === 'dispatch.evidence');
});

test('acknowledgement records governed outcome evidence', async () => {
  const service = make();
  service.enqueue({ id: 'q1', workItemId: 'AIOC-I-003B', agentRole: 'developer', operation: 'build' });
  await service.dispatchNext({ workerId: 'agent-1' });
  const event = await service.acknowledge('q1', { workerId: 'agent-1', outcome: 'complete', evidence: ['commit://abc'] });
  assert.equal(event.outcome, 'complete');
  assert.deepEqual(service.snapshot().queue[0].resultEvidence, ['commit://abc']);
});

test('expired leases return work to queue', async () => {
  const service = make();
  service.enqueue({ id: 'q1', workItemId: 'AIOC-I-003B', agentRole: 'developer', operation: 'build' });
  await service.dispatchNext({ workerId: 'agent-1', leaseSeconds: -1 });
  assert.deepEqual(service.reclaimExpired(new Date()), ['q1']);
  assert.equal(service.snapshot().queue[0].status, 'queued');
});

test('empty queue dispatch returns null', async () => {
  assert.equal(await make().dispatchNext({ workerId: 'agent-1' }), null);
});

let failures = 0;
for (const { name, fn } of tests) {
  try { await fn(); console.log(`PASS ${name}`); }
  catch (error) { failures += 1; console.error(`FAIL ${name}`); console.error(error); }
}
console.log(`RESULT ${tests.length - failures}/${tests.length} passed`);
if (failures) process.exit(1);