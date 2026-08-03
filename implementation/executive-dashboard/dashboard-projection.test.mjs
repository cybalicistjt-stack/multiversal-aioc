import assert from 'node:assert/strict';
import { buildExecutiveDashboard, assertDashboardExecutable } from './dashboard-projection.mjs';

const baseState = {
  project: { id: 'multiversal', name: 'Multiversal', owner: 'John Brandon Turner' },
  repositories: [
    { id: 'multiversal-app', fullName: 'cybalicistjt-stack/Multiversal-app', purpose: 'Application', defaultBranch: 'main' },
    { id: 'multiversal-aioc', fullName: 'cybalicistjt-stack/multiversal-aioc', purpose: 'Command center', defaultBranch: 'main' }
  ],
  milestones: [
    { id: 'AIOC-I-002', title: 'Repository Intelligence', status: 'complete', sequence: 2 },
    { id: 'AIOC-I-003', title: 'Executive Dashboard and Orchestration', status: 'active', sequence: 3 }
  ],
  workItems: [
    { id: 'AIOC-I-002C', milestoneId: 'AIOC-I-002', title: 'Continuity Certification', status: 'complete', sequence: 220, evidence: ['ci://pass'] },
    { id: 'AIOC-I-003A', milestoneId: 'AIOC-I-003', title: 'Executive Dashboard Operational Projection', status: 'active', sequence: 300, evidence: [] },
    { id: 'AIOC-I-003B', milestoneId: 'AIOC-I-003', title: 'Governed Orchestration Queue', status: 'planned', sequence: 310, evidence: [] }
  ],
  decisions: [{ id: 'D1', status: 'open' }],
  active: { repositoryId: 'multiversal-aioc', milestoneId: 'AIOC-I-003', workItemId: 'AIOC-I-003A', branch: 'governance/session-bootstrap-v1' }
};

const healthy = {
  'multiversal-app': { status: 'healthy', branch: 'main', headSha: 'abc', findings: [] },
  'multiversal-aioc': { status: 'healthy', branch: 'governance/session-bootstrap-v1', headSha: 'def', findings: [] }
};

const tests = [];
const test = (name, fn) => tests.push({ name, fn });

test('healthy evidence produces executable dashboard', () => {
  const dashboard = buildExecutiveDashboard({ state: baseState, repositoryHealth: healthy, continuityCertification: { executionAllowed: true, findings: [], nextAction: 'Implement AIOC-I-003A' } });
  assert.equal(dashboard.project.health, 'healthy');
  assert.equal(dashboard.active.executionAllowed, true);
  assert.equal(assertDashboardExecutable(dashboard), dashboard);
});

test('active milestone and work item are projected', () => {
  const dashboard = buildExecutiveDashboard({ state: baseState, repositoryHealth: healthy });
  assert.equal(dashboard.active.milestone.id, 'AIOC-I-003');
  assert.equal(dashboard.active.workItem.id, 'AIOC-I-003A');
});

test('progress is deterministic', () => {
  const dashboard = buildExecutiveDashboard({ state: baseState, repositoryHealth: healthy });
  assert.equal(dashboard.progress.completedWorkItems, 1);
  assert.equal(dashboard.progress.totalWorkItems, 3);
  assert.equal(dashboard.progress.percent, 33);
});

test('repository cards preserve distinct purposes', () => {
  const dashboard = buildExecutiveDashboard({ state: baseState, repositoryHealth: healthy });
  assert.equal(new Set(dashboard.repositories.map(item => item.purpose)).size, 2);
});

test('failed CI blocks project execution', () => {
  const dashboard = buildExecutiveDashboard({ state: baseState, repositoryHealth: healthy, ciChecks: { 'multiversal-aioc': [{ name: 'smoke', conclusion: 'failure' }] } });
  assert.equal(dashboard.repositories.find(item => item.id === 'multiversal-aioc').checks[0].state, 'fail');
});

test('blocking repository finding blocks dashboard', () => {
  const repositoryHealth = structuredClone(healthy);
  repositoryHealth['multiversal-aioc'] = { status: 'blocked', findings: [{ id: 'F1', blocking: true, title: 'CI failed' }] };
  const dashboard = buildExecutiveDashboard({ state: baseState, repositoryHealth });
  assert.equal(dashboard.project.health, 'blocked');
  assert.equal(dashboard.active.executionAllowed, false);
  assert.throws(() => assertDashboardExecutable(dashboard), error => error.code === 'dashboard.execution-blocked');
});

test('continuity certification failure freezes execution', () => {
  const dashboard = buildExecutiveDashboard({ state: baseState, repositoryHealth: healthy, continuityCertification: { executionAllowed: false, findings: [{ id: 'C1', blocking: true, title: 'Snapshot stale' }] } });
  assert.equal(dashboard.active.executionAllowed, false);
});

test('warnings degrade but do not block', () => {
  const repositoryHealth = structuredClone(healthy);
  repositoryHealth['multiversal-app'].findings = [{ id: 'W1', severity: 'warning', title: 'PR aging' }];
  const dashboard = buildExecutiveDashboard({ state: baseState, repositoryHealth });
  assert.equal(dashboard.project.health, 'degraded');
  assert.equal(dashboard.active.executionAllowed, true);
});

test('blocked work items appear as top blockers', () => {
  const state = structuredClone(baseState);
  state.workItems.push({ id: 'AIOC-X', milestoneId: 'AIOC-I-003', title: 'Blocked task', status: 'blocked', sequence: 320, blocker: 'Dependency missing' });
  const dashboard = buildExecutiveDashboard({ state, repositoryHealth: healthy });
  assert.equal(dashboard.findings[0].source, 'work-item');
  assert.equal(dashboard.counters.blockedWorkItems, 1);
});

test('open decisions are counted', () => {
  const dashboard = buildExecutiveDashboard({ state: baseState, repositoryHealth: healthy });
  assert.equal(dashboard.counters.openDecisions, 1);
});

test('summary contains health and next action', () => {
  const dashboard = buildExecutiveDashboard({ state: baseState, repositoryHealth: healthy });
  assert.match(dashboard.summary, /HEALTHY/);
  assert.match(dashboard.summary, /AIOC-I-003A/);
});

test('input state is not mutated', () => {
  const before = JSON.stringify(baseState);
  buildExecutiveDashboard({ state: baseState, repositoryHealth: healthy });
  assert.equal(JSON.stringify(baseState), before);
});

let failures = 0;
for (const { name, fn } of tests) {
  try { await fn(); console.log(`PASS ${name}`); }
  catch (error) { failures += 1; console.error(`FAIL ${name}`); console.error(error); }
}
console.log(`RESULT ${tests.length - failures}/${tests.length} passed`);
if (failures) process.exit(1);
