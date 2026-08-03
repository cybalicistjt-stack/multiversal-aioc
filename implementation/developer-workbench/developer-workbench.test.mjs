import assert from 'node:assert/strict';
import { projectDeveloperWorkbench, assertWorkbenchReady, createChangePlan } from './developer-workbench.mjs';

const baseState = {
  repositories: [{ id: 'multiversal-aioc', fullName: 'cybalicistjt-stack/multiversal-aioc', defaultBranch: 'main' }],
  workItems: [
    { id: 'AIOC-I-003C', status: 'complete', title: 'Certification' },
    { id: 'AIOC-I-004A', status: 'active', title: 'Developer Workbench Change Planning and Evidence Projection' }
  ],
  active: { repositoryId: 'multiversal-aioc', milestoneId: 'AIOC-I-004', workItemId: 'AIOC-I-004A', branch: 'governance/session-bootstrap-v1' }
};
const health = { repositories: [{ repositoryId: 'multiversal-aioc', status: 'healthy' }] };
const continuity = { result: 'PASS' };
const change = {
  id: 'CH-1', repositoryId: 'multiversal-aioc', title: 'Add workbench',
  files: ['b.mjs', 'a.mjs', 'a.mjs'], capabilities: ['github.write'],
  dependencies: ['AIOC-I-003C'], acceptanceCriteria: ['Tests pass']
};
const clone = value => JSON.parse(JSON.stringify(value));
const tests = [];
const test = (name, fn) => tests.push({ name, fn });

test('healthy governed change is permitted', () => {
  const projection = projectDeveloperWorkbench({ state: baseState, repositoryHealth: health, continuityCertification: continuity, change });
  assert.equal(projection.execution.permitted, true);
  assert.deepEqual(projection.impact.files, ['a.mjs', 'b.mjs']);
});

test('unknown repository blocks execution', () => {
  const projection = projectDeveloperWorkbench({ state: baseState, repositoryHealth: health, continuityCertification: continuity, change: { ...change, repositoryId: 'missing' } });
  assert.equal(projection.execution.permitted, false);
  assert.equal(projection.findings.some(item => item.code === 'repository.unknown'), true);
});

test('failed continuity blocks execution', () => {
  const projection = projectDeveloperWorkbench({ state: baseState, repositoryHealth: health, continuityCertification: { result: 'FAIL' }, change });
  assert.equal(projection.findings.some(item => item.code === 'continuity.blocked'), true);
});

test('missing repository health blocks execution', () => {
  const projection = projectDeveloperWorkbench({ state: baseState, repositoryHealth: { repositories: [] }, continuityCertification: continuity, change });
  assert.equal(projection.findings.some(item => item.code === 'health.missing'), true);
});

test('degraded health warns without blocking', () => {
  const projection = projectDeveloperWorkbench({ state: baseState, repositoryHealth: { repositories: [{ repositoryId: 'multiversal-aioc', status: 'degraded' }] }, continuityCertification: continuity, change });
  assert.equal(projection.execution.permitted, true);
  assert.equal(projection.findings.some(item => item.code === 'health.degraded'), true);
});

test('incomplete dependency blocks execution', () => {
  const state = clone(baseState);
  state.workItems[0].status = 'active';
  const projection = projectDeveloperWorkbench({ state, repositoryHealth: health, continuityCertification: continuity, change });
  assert.equal(projection.findings.some(item => item.code === 'dependency.incomplete'), true);
});

test('high risk change requires prior evidence', () => {
  const projection = projectDeveloperWorkbench({ state: baseState, repositoryHealth: health, continuityCertification: continuity, change: { ...change, risk: 'high', evidence: [] } });
  assert.equal(projection.findings.some(item => item.code === 'risk.evidence'), true);
});

test('missing acceptance criteria produces warning', () => {
  const projection = projectDeveloperWorkbench({ state: baseState, repositoryHealth: health, continuityCertification: continuity, change: { ...change, acceptanceCriteria: [] } });
  assert.equal(projection.execution.permitted, true);
  assert.equal(projection.findings.some(item => item.code === 'acceptance.empty'), true);
});

test('assertion rejects blocked workbench', () => {
  const projection = projectDeveloperWorkbench({ state: baseState, repositoryHealth: health, continuityCertification: { result: 'FAIL' }, change });
  assert.throws(() => assertWorkbenchReady(projection), error => error.code === 'workbench.blocked');
});

test('change plan binds canonical context and evidence', () => {
  const projection = projectDeveloperWorkbench({ state: baseState, repositoryHealth: health, continuityCertification: continuity, change });
  const plan = createChangePlan(projection, { actor: 'developer-agent', steps: [{ action: 'edit', paths: ['b.mjs', 'a.mjs'] }, { action: 'test', paths: [] }] });
  assert.equal(plan.workItemId, 'AIOC-I-004A');
  assert.equal(plan.steps.length, 2);
  assert.equal(plan.acceptanceEvidence.length, 1);
});

test('change plan requires actor', () => {
  const projection = projectDeveloperWorkbench({ state: baseState, repositoryHealth: health, continuityCertification: continuity, change });
  assert.throws(() => createChangePlan(projection, { steps: [{ action: 'test' }] }), error => error.code === 'plan.actor');
});

test('change requires files', () => {
  assert.throws(() => projectDeveloperWorkbench({ state: baseState, repositoryHealth: health, continuityCertification: continuity, change: { ...change, files: [] } }), error => error.code === 'change.files');
});

let failures = 0;
for (const { name, fn } of tests) {
  try { await fn(); console.log(`PASS ${name}`); }
  catch (error) { failures += 1; console.error(`FAIL ${name}`); console.error(error); }
}
console.log(`RESULT ${tests.length - failures}/${tests.length} passed`);
if (failures) process.exit(1);
