import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { ProjectStateEngine, validateProjectState, stableStringify } from './project-state-engine.mjs';

const seed = JSON.parse(await readFile(new URL('./canonical-project-state.seed.json', import.meta.url), 'utf8'));
const clone = value => JSON.parse(JSON.stringify(value));
const tests = [];
const test = (name, fn) => tests.push({ name, fn });

test('seed is structurally valid', () => {
  assert.deepEqual(validateProjectState(seed).filter(x => x.severity === 'error'), []);
});

test('engine initializes with exactly one active item', () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  assert.equal(engine.snapshot().workItems.filter(x => x.status === 'active').length, 1);
  assert.equal(engine.snapshot().active.workItemId, 'AIOC-I-001A');
});

test('completion requires evidence', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  await assert.rejects(() => engine.transitionWorkItem('AIOC-I-001A', 'complete', { reason: 'test' }), error => error.code === 'workItem.completion-evidence');
});

test('valid completion appends ledger evidence', async () => {
  const engine = new ProjectStateEngine({ initialState: seed, actor: 'test-agent' });
  const before = engine.snapshot().ledger.length;
  await engine.transitionWorkItem('AIOC-I-001A', 'complete', { reason: 'Acceptance met', evidence: ['test://AIOC-I-001A'] });
  const state = engine.snapshot();
  assert.equal(state.workItems.find(x => x.id === 'AIOC-I-001A').status, 'complete');
  assert.equal(state.ledger.length, before + 1);
  assert.equal(state.ledger.at(-1).actor, 'test-agent');
});

test('dependencies prevent premature activation', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  await engine.transitionWorkItem('AIOC-I-001B', 'ready', { reason: 'queue' });
  await assert.rejects(() => engine.transitionWorkItem('AIOC-I-001B', 'active', { reason: 'start' }), error => error.code === 'workItem.dependencies');
});

test('next executable work item respects dependency completion', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  assert.equal(engine.getNextExecutableWorkItem(), null);
  await engine.transitionWorkItem('AIOC-I-001A', 'complete', { reason: 'done', evidence: ['test://done'] });
  assert.equal(engine.getNextExecutableWorkItem().id, 'AIOC-I-001B');
});

test('decision records are first-class and ledgered', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  await engine.recordDecision({ id: 'DEC-TEST-001', title: 'Use deterministic state serialization' });
  const state = engine.snapshot();
  assert.equal(state.decisions.some(x => x.id === 'DEC-TEST-001'), true);
  assert.equal(state.ledger.at(-1).entityType, 'decision');
});

test('handoffs require a known work item', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  await assert.rejects(() => engine.createHandoff({ id: 'H-1', workItemId: 'missing', summary: 'x', nextAction: 'y' }), error => error.code === 'handoff.workItem');
});

test('valid handoff is persisted in canonical state', async () => {
  const engine = new ProjectStateEngine({ initialState: seed });
  await engine.createHandoff({ id: 'H-1', workItemId: 'AIOC-I-001A', summary: 'Engine implemented', nextAction: 'Run validation', evidence: ['test://handoff'] });
  assert.equal(engine.snapshot().handoffs.length, 1);
});

test('duplicate identifiers are rejected', () => {
  const bad = clone(seed);
  bad.workItems.push(clone(bad.workItems[0]));
  assert.equal(validateProjectState(bad).some(x => x.code === 'workItem.duplicate'), true);
});

test('completed work without evidence is rejected', () => {
  const bad = clone(seed);
  bad.workItems[0].status = 'complete';
  bad.workItems[0].evidence = [];
  assert.equal(validateProjectState(bad).some(x => x.code === 'workItem.evidence'), true);
});

test('repository purposes remain distinct', () => {
  const purposes = new Set(seed.repositories.map(x => x.purpose));
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
