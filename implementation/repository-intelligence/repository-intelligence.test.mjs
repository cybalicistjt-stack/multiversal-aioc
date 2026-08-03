import assert from 'node:assert/strict';
import { classifyCheck, evaluateRepositoryHealth, projectRepositoryIntelligence, detectDocumentationDrift } from './repository-intelligence.mjs';

const now = '2026-08-03T04:00:00.000Z';
const canonicalState = {
  project: { id: 'multiversal' },
  repositories: [
    { id: 'multiversal-app', fullName: 'cybalicistjt-stack/Multiversal-app' },
    { id: 'multiversal-aioc', fullName: 'cybalicistjt-stack/multiversal-aioc' }
  ],
  active: { repositoryId: 'multiversal-aioc', milestoneId: 'AIOC-I-002', workItemId: 'AIOC-I-002A', branch: 'governance/session-bootstrap-v1' }
};

const healthy = {
  repository: { id: 'multiversal-aioc', fullName: 'cybalicistjt-stack/multiversal-aioc' },
  observedAt: '2026-08-03T03:55:00.000Z',
  capabilities: { read: true, push: true, admin: true },
  head: { sha: 'abc', committedAt: '2026-08-03T03:50:00.000Z' },
  checks: [{ name: 'smoke', status: 'completed', conclusion: 'success', completedAt: '2026-08-03T03:56:00.000Z' }],
  pullRequests: [{ number: 1, state: 'open', mergeable: true, updatedAt: '2026-08-03T03:57:00.000Z' }],
  drift: []
};

const tests = [];
const test = (name, fn) => tests.push({ name, fn });

test('check conclusions normalize deterministically', () => {
  assert.equal(classifyCheck({ status: 'completed', conclusion: 'success' }), 'passing');
  assert.equal(classifyCheck({ status: 'completed', conclusion: 'failure' }), 'failing');
  assert.equal(classifyCheck({ status: 'in_progress' }), 'pending');
});

test('healthy repository has no blockers or warnings', () => {
  const result = evaluateRepositoryHealth(healthy, { now });
  assert.equal(result.status, 'healthy');
  assert.deepEqual(result.blockers, []);
  assert.deepEqual(result.warnings, []);
});

test('failed required check blocks repository', () => {
  const snapshot = structuredClone(healthy);
  snapshot.checks[0].conclusion = 'failure';
  const result = evaluateRepositoryHealth(snapshot, { now });
  assert.equal(result.status, 'blocked');
  assert(result.blockers.includes('required-check-failing'));
});

test('missing push capability degrades but does not invent a blocker', () => {
  const snapshot = structuredClone(healthy);
  snapshot.capabilities.push = false;
  const result = evaluateRepositoryHealth(snapshot, { now });
  assert.equal(result.status, 'degraded');
  assert(result.warnings.includes('repository-write-unavailable'));
});

test('missing read capability blocks repository', () => {
  const snapshot = structuredClone(healthy);
  snapshot.capabilities.read = false;
  assert.equal(evaluateRepositoryHealth(snapshot, { now }).status, 'blocked');
});

test('stale observations are detected', () => {
  const snapshot = structuredClone(healthy);
  snapshot.observedAt = '2026-08-01T00:00:00.000Z';
  const result = evaluateRepositoryHealth(snapshot, { now, staleAfterHours: 24 });
  assert(result.warnings.includes('observation-stale'));
});

test('blocking drift blocks repository', () => {
  const snapshot = structuredClone(healthy);
  snapshot.drift = [{ code: 'branch.mismatch', severity: 'blocking' }];
  assert.equal(evaluateRepositoryHealth(snapshot, { now }).status, 'blocked');
});

test('project projection includes missing repository observations', () => {
  const result = projectRepositoryIntelligence({ canonicalState, observations: [healthy], now });
  assert.equal(result.repositories.length, 2);
  assert.equal(result.overallStatus, 'blocked');
  assert.equal(result.counts.unknown, 1);
});

test('project projection is healthy when every repository is healthy', () => {
  const app = structuredClone(healthy);
  app.repository = { id: 'multiversal-app', fullName: 'cybalicistjt-stack/Multiversal-app' };
  const result = projectRepositoryIntelligence({ canonicalState, observations: [healthy, app], now });
  assert.equal(result.overallStatus, 'healthy');
  assert.equal(result.nextWorkItemId, 'AIOC-I-002A');
});

test('documentation drift detects missing current-state document', () => {
  const findings = detectDocumentationDrift({ canonicalState, documents: [{ name: 'SESSION_HANDOFF.md', workItemId: 'AIOC-I-002A' }] });
  assert(findings.some(item => item.code === 'document.missing'));
});

test('documentation drift detects stale handoff', () => {
  const findings = detectDocumentationDrift({
    canonicalState,
    documents: [
      { name: 'AIOC_CURRENT_STATE.md', workItemId: 'AIOC-I-002A' },
      { name: 'SESSION_HANDOFF.md', workItemId: 'AIOC-I-001C' }
    ]
  });
  assert(findings.some(item => item.document === 'SESSION_HANDOFF.md' && item.code === 'document.stale-work-item'));
});

test('latest activity selects newest observed event', () => {
  const result = evaluateRepositoryHealth(healthy, { now });
  assert.equal(result.latestActivityAt, '2026-08-03T03:57:00.000Z');
});

let failures = 0;
for (const { name, fn } of tests) {
  try { await fn(); console.log(`PASS ${name}`); }
  catch (error) { failures += 1; console.error(`FAIL ${name}`); console.error(error); }
}
console.log(`RESULT ${tests.length - failures}/${tests.length} passed`);
if (failures) process.exit(1);
