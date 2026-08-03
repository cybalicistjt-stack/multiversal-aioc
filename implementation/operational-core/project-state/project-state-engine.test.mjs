import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { ProjectStateEngine, validateProjectState, stableStringify } from './project-state-engine.mjs';

const fixture = JSON.parse(await readFile(new URL('./project-state-engine.fixture.json', import.meta.url), 'utf8'));
const liveState = JSON.parse(await readFile(new URL('./canonical-project-state.seed.json', import.meta.url), 'utf8'));
const clone = value => JSON.parse(JSON.stringify(value));
const tests = [];
const test = (name, fn) => tests.push({ name, fn });

test('immutable fixture is structurally valid', () => {
  assert.deepEqual(validateProjectState(fixture).filter(issue => issue.severity === 'error'), []);
});

test('live canonical state is independently valid', () => {
  assert.deepEqual(validateProjectState(liveState).filter(issue => issue.severity === 'error'), []);
});

test('fixture initializes at AIOC-I-001A', () => {
  const engine = new ProjectStateEngine({ initialState: fixture });
  assert.equal(engine.snapshot().active.workItemId, 'AIOC-I-001A');
  assert.equal(engine.snapshot().workItems.filter(item => item.status === 'active').length, 1);
});

test('completion requires evidence', async () => {
  const engine = new ProjectStateEngine({ initialState: fixture });
  await assert.rejects(
    () => engine.completeAndAdvance('AIOC-I-001A', { reason: 'test' }),
    error => error.code === 'workItem.completion-evidence'
  );
});

test('completion and successor activation are atomic', async () => {
  const engine = new ProjectStateEngine({ initialState: fixture, actor: 'test-agent' });
  const before = engine.snapshot().ledger.length;
  const result = await engine.completeAndAdvance('AIOC-I-001A', {
    reason: 'Acceptance met',
    evidence: ['test://AIOC-I-001A']
  });
  const state = engine.snapshot();
  assert.equal(result.completed.id, 'AIOC-I-001A');
  assert.equal(result.activated.id, 'AIOC-I-001B');
  assert.equal(state.active.workItemId, 'AIOC-I-001B');
  assert.equal(state.workItems.find(item => item.id === 'AIOC-I-001A').status, 'complete');
  assert.equal(state.workItems.find(item => item.id === 'AIOC-I-001B').status, 'active');
  assert.equal(state.workItems.filter(item => item.status === 'active').length, 1);
  assert.equal(state.ledger.length, before + 1);
  assert.equal(state.ledger.at(-1).operation, 'complete-and-advance');
});

test('transitionWorkItem delegates completion to atomic advance', async () => {
  const engine = new ProjectStateEngine({ initialState: fixture });
  await engine.transitionWorkItem('AIOC-I-001A', 'complete', {
    reason: 'done', evidence: ['test://delegated']
  });
  assert.equal(engine.snapshot().active.workItemId, 'AIOC-I-001B');
});

test('dependencies prevent premature activation', async () => {
  const engine = new ProjectStateEngine({ initialState: fixture });
  await engine.transitionWorkItem('AIOC-I-001B', 'ready', { reason: 'queue' });
  await assert.rejects(
    () => engine.transitionWorkItem('AIOC-I-001B', 'active', { reason: 'start' }),
    error => error.code === 'workItem.dependencies'
  );
});

test('next executable work item is deterministic after advancement', async () => {
  const engine = new ProjectStateEngine({ initialState: fixture });
  assert.equal(engine.getNextExecutableWorkItem(), null);
  await engine.completeAndAdvance('AIOC-I-001A', { reason: 'done', evidence: ['test://done'] });
  assert.equal(engine.snapshot().active.workItemId, 'AIOC-I-001B');
  assert.equal(engine.getNextExecutableWorkItem().id, 'AIOC-I-001C');
});

test('missing successor rolls back the entire transaction', async () => {
  const terminal = clone(fixture);
  terminal.workItems = terminal.workItems.filter(item => item.id === 'AIOC-I-001A');
  terminal.active.workItemId = 'AIOC-I-001A';
  const engine = new ProjectStateEngine({ initialState: terminal });
  const before = engine.snapshot();
  await assert.rejects(
    () => engine.completeAndAdvance('AIOC-I-001A', { reason: 'terminal', evidence: ['test://terminal'] }),
    error => error.code === 'workItem.no-successor'
  );
  assert.deepEqual(engine.snapshot(), before);
});

test('persistence failure leaves state unchanged and emits no event', async () => {
  const engine = new ProjectStateEngine({
    initialState: fixture,
    persist: async () => { throw Object.assign(new Error('disk unavailable'), { code: 'persist.failed' }); }
  });
  let events = 0;
  engine.subscribe(() => { events += 1; });
  const before = engine.snapshot();
  await assert.rejects(
    () => engine.recordDecision({ id: 'DEC-FAIL', title: 'Must roll back' }),
    error => error.code === 'persist.failed'
  );
  assert.deepEqual(engine.snapshot(), before);
  assert.equal(events, 0);
});

test('decision and handoff records are ledgered', async () => {
  const engine = new ProjectStateEngine({ initialState: fixture });
  await engine.recordDecision({ id: 'DEC-TEST-001', title: 'Deterministic state serialization' });
  await engine.createHandoff({
    id: 'H-1', workItemId: 'AIOC-I-001A', summary: 'Engine implemented',
    nextAction: 'Run validation', evidence: ['test://handoff']
  });
  const state = engine.snapshot();
  assert.equal(state.decisions.some(item => item.id === 'DEC-TEST-001'), true);
  assert.equal(state.handoffs.some(item => item.id === 'H-1'), true);
  assert.equal(state.ledger.at(-1).entityType, 'handoff');
});

test('validation rejects duplicate IDs and evidence-free completion', () => {
  const duplicate = clone(fixture);
  duplicate.workItems.push(clone(duplicate.workItems[0]));
  assert.equal(validateProjectState(duplicate).some(issue => issue.code === 'workItem.duplicate'), true);
  const incompleteEvidence = clone(fixture);
  incompleteEvidence.workItems[0].status = 'complete';
  incompleteEvidence.workItems[0].evidence = [];
  assert.equal(validateProjectState(incompleteEvidence).some(issue => issue.code === 'workItem.evidence'), true);
});

test('serialization and repository purposes remain deterministic', () => {
  assert.equal(stableStringify({ b: 2, a: 1 }), stableStringify({ a: 1, b: 2 }));
  const purposes = new Set(fixture.repositories.map(repository => repository.purpose));
  assert.equal(purposes.size, fixture.repositories.length);
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
