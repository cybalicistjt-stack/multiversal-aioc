import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { ProjectStateEngine, validateProjectState, stableStringify } from './project-state-engine.mjs';

const seed = JSON.parse(await readFile(new URL('./canonical-project-state.seed.json', import.meta.url), 'utf8'));
const clone = value => JSON.parse(JSON.stringify(value));
const tests = [];
const test = (name, fn) => tests.push({ name, fn });

test('seed is structurally valid', () => {
  assert.deepEqual(validateProjectState(seed).filter(issue => issue.severity === 'error'), []);
});

test('engine initializes with exactly one active item', () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  assert.equal(engine.snapshot().workItems.filter(item => item.status === 'active').length, 1);
  assert.equal(engine.snapshot().active.workItemId, 'AIOC-I-001A');
});

test('completion requires evidence', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  await assert.rejects(
    () => engine.completeAndAdvance('AIOC-I-001A', { reason: 'test' }),
    error => error.code === 'workItem.completion-evidence'
  );
});

test('completion and successor activation are one atomic transaction', async () => {
  const engine = new ProjectStateEngine({ initialState: seed, actor: 'test-agent' });
  const ledgerBefore = engine.snapshot().ledger.length;
  const result = await engine.completeAndAdvance('AIOC-I-001A', {
    reason: 'Acceptance met',
    evidence: ['test://AIOC-I-001A']
  });
  const state = engine.snapshot();
  assert.equal(result.completed.id, 'AIOC-I-001A');
  assert.equal(result.activated.id, 'AIOC-I-001B');
  assert.equal(state.workItems.find(item => item.id === 'AIOC-I-001A').status, 'complete');
  assert.equal(state.workItems.find(item => item.id === 'AIOC-I-001B').status, 'active');
  assert.equal(state.active.workItemId, 'AIOC-I-001B');
  assert.equal(state.workItems.filter(item => item.status === 'active').length, 1);
  assert.equal(state.ledger.length, ledgerBefore + 1);
  assert.equal(state.ledger.at(-1).operation, 'complete-and-advance');
  assert.equal(state.ledger.at(-1).actor, 'test-agent');
});

test('transitionWorkItem delegates completion to atomic advance', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  await engine.transitionWorkItem('AIOC-I-001A', 'complete', {
    reason: 'done',
    evidence: ['test://delegated']
  });
  assert.equal(engine.snapshot().active.workItemId, 'AIOC-I-001B');
});

test('dependencies prevent premature activation', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  await engine.transitionWorkItem('AIOC-I-001B', 'ready', { reason: 'queue' });
  await assert.rejects(
    () => engine.transitionWorkItem('AIOC-I-001B', 'active', { reason: 'start' }),
    error => error.code === 'workItem.dependencies'
  );
});

test('next executable work item is deterministic after advancement', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  assert.equal(engine.getNextExecutableWorkItem(), null);
  await engine.completeAndAdvance('AIOC-I-001A', { reason: 'done', evidence: ['test://done'] });
  assert.equal(engine.snapshot().active.workItemId, 'AIOC-I-001B');
  assert.equal(engine.getNextExecutableWorkItem().id, 'AIOC-I-001C');
});

test('missing successor rolls back the entire completion transaction', async () => {
  const terminal = clone(seed);
  terminal.workItems = terminal.workItems.filter(item => item.id === 'AIOC-I-001A');
  const engine = new ProjectStateEngine({ initialState: terminal });
  const before = engine.snapshot();
  await assert.rejects(
    () => engine.completeAndAdvance('AIOC-I-001A', { reason: 'terminal', evidence: ['test://terminal'] }),
    error => error.code === 'workItem.no-successor'
  );
  assert.deepEqual(engine.snapshot(), before);
});

test('persistence failure leaves in-memory state unchanged', async () => {
  const engine = new ProjectStateEngine({
    initialState: seed,
    persist: async () => { throw Object.assign(new Error('disk unavailable'), { code: 'persist.failed' }); }
  });
  const before = engine.snapshot();
  await assert.rejects(
    () => engine.recordDecision({ id: 'DEC-FAIL', title: 'Must roll back' }),
    error => error.code === 'persist.failed'
  );
  assert.deepEqual(engine.snapshot(), before);
});

test('failed transaction emits no event', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  let events = 0;
  engine.subscribe(() => { events += 1; });
  await assert.rejects(
    () => engine.completeAndAdvance('AIOC-I-001A', { reason: 'missing evidence' }),
    error => error.code === 'workItem.completion-evidence'
  );
  assert.equal(events, 0);
});

test('successful transaction emits one committed event', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  const events = [];
  engine.subscribe(event => events.push(event));
  await engine.recordDecision({ id: 'DEC-TEST-001', title: 'Use deterministic state serialization' });
  assert.equal(events.length, 1);
  assert.equal(events[0].entityType, 'decision');
});

test('decision records are first-class and ledgered', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  await engine.recordDecision({ id: 'DEC-TEST-001', title: 'Use deterministic state serialization' });
  const state = engine.snapshot();
  assert.equal(state.decisions.some(item => item.id === 'DEC-TEST-001'), true);
  assert.equal(state.ledger.at(-1).entityType, 'decision');
});

test('handoffs require a known work item', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  await assert.rejects(
    () => engine.createHandoff({ id: 'H-1', workItemId: 'missing', summary: 'x', nextAction: 'y' }),
    error => error.code === 'handoff.workItem'
  );
});

test('valid handoff is persisted in canonical state', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  await engine.createHandoff({
    id: 'H-1',
    workItemId: 'AIOC-I-001A',
    summary: 'Engine implemented',
    nextAction: 'Run validation',
    evidence: ['test://handoff']
  });
  assert.equal(engine.snapshot().handoffs.length, 1);
});

test('duplicate identifiers are rejected', () => {
  const bad = clone(seed);
  bad.workItems.push(clone(bad.workItems[0]));
  assert.equal(validateProjectState(bad).some(issue => issue.code === 'workItem.duplicate'), true);
});

test('completed work without evidence is rejected', () => {
  const bad = clone(seed);
  bad.workItems[0].status = 'complete';
  bad.workItems[0].evidence = [];
  assert.equal(validateProjectState(bad).some(issue => issue.code === 'workItem.evidence'), true);
});

test('repository purposes remain distinct', () => {
  const purposes = new Set(seed.repositories.map(repository => repository.purpose));
  assert.equal(purposes.size, seed.repositories.length);
});

test('stable serialization is independent of key insertion order', () => {
  assert.equal(stableStringify({ b: 2, a: 1 }), stableStringify({ a: 1, b: 2 }));
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
