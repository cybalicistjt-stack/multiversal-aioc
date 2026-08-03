const clone = value => globalThis.structuredClone ? globalThis.structuredClone(value) : JSON.parse(JSON.stringify(value));

function assert(condition, message, code = 'repository-intelligence.invalid') {
  if (!condition) {
    const error = new Error(message);
    error.code = code;
    throw error;
  }
}

function newestTimestamp(values) {
  return values.filter(Boolean).sort().at(-1) || null;
}

export function classifyCheck(check) {
  const conclusion = check?.conclusion ?? null;
  const status = check?.status ?? 'unknown';
  if (status !== 'completed') return 'pending';
  if (conclusion === 'success') return 'passing';
  if (['failure', 'timed_out', 'cancelled', 'action_required'].includes(conclusion)) return 'failing';
  return 'neutral';
}

export function evaluateRepositoryHealth(snapshot, { now = new Date().toISOString(), staleAfterHours = 24 } = {}) {
  assert(snapshot?.repository?.fullName, 'Repository fullName is required.', 'repository.required');
  const checks = Array.isArray(snapshot.checks) ? snapshot.checks : [];
  const pullRequests = Array.isArray(snapshot.pullRequests) ? snapshot.pullRequests : [];
  const drift = Array.isArray(snapshot.drift) ? snapshot.drift : [];
  const capabilities = snapshot.capabilities || {};
  const checkStates = checks.map(classifyCheck);
  const observedAt = snapshot.observedAt || null;
  const ageHours = observedAt ? (Date.parse(now) - Date.parse(observedAt)) / 3_600_000 : Infinity;

  const blockers = [];
  const warnings = [];
  if (!capabilities.read) blockers.push('repository-read-unavailable');
  if (!capabilities.push) warnings.push('repository-write-unavailable');
  if (checkStates.includes('failing')) blockers.push('required-check-failing');
  if (drift.some(item => item.severity === 'blocking')) blockers.push('blocking-drift');
  if (ageHours > staleAfterHours) warnings.push('observation-stale');
  if (checkStates.includes('pending')) warnings.push('checks-pending');
  if (pullRequests.some(pr => pr.mergeable === false)) warnings.push('pull-request-not-mergeable');

  let status = 'healthy';
  if (blockers.length) status = 'blocked';
  else if (warnings.length) status = 'degraded';

  return {
    repositoryId: snapshot.repository.id,
    fullName: snapshot.repository.fullName,
    status,
    blockers,
    warnings,
    observedAt,
    ageHours: Number.isFinite(ageHours) ? Number(ageHours.toFixed(2)) : null,
    passingChecks: checkStates.filter(value => value === 'passing').length,
    failingChecks: checkStates.filter(value => value === 'failing').length,
    pendingChecks: checkStates.filter(value => value === 'pending').length,
    openPullRequests: pullRequests.filter(pr => pr.state === 'open').length,
    latestActivityAt: newestTimestamp([
      snapshot.head?.committedAt,
      ...pullRequests.map(pr => pr.updatedAt),
      ...checks.map(check => check.completedAt || check.startedAt)
    ])
  };
}

export function projectRepositoryIntelligence({ canonicalState, observations, now, staleAfterHours = 24 }) {
  assert(canonicalState?.repositories, 'Canonical repositories are required.', 'state.repositories');
  assert(Array.isArray(observations), 'Observations must be an array.', 'observations.type');
  const byId = new Map(observations.map(item => [item.repository?.id, item]));
  const repositories = canonicalState.repositories.map(repository => {
    const observation = byId.get(repository.id);
    if (!observation) {
      return {
        repositoryId: repository.id,
        fullName: repository.fullName,
        status: 'unknown',
        blockers: ['observation-missing'],
        warnings: [],
        observedAt: null,
        ageHours: null,
        passingChecks: 0,
        failingChecks: 0,
        pendingChecks: 0,
        openPullRequests: 0,
        latestActivityAt: null
      };
    }
    return evaluateRepositoryHealth(observation, { now, staleAfterHours });
  });

  const counts = repositories.reduce((result, repository) => {
    result[repository.status] = (result[repository.status] || 0) + 1;
    return result;
  }, { healthy: 0, degraded: 0, blocked: 0, unknown: 0 });

  return {
    schemaVersion: '1.0.0',
    generatedAt: now || new Date().toISOString(),
    projectId: canonicalState.project.id,
    active: clone(canonicalState.active),
    repositories,
    counts,
    overallStatus: counts.blocked || counts.unknown ? 'blocked' : counts.degraded ? 'degraded' : 'healthy',
    nextWorkItemId: canonicalState.active.workItemId
  };
}

export function detectDocumentationDrift({ canonicalState, documents }) {
  const active = canonicalState.active;
  const required = new Map([
    ['AIOC_CURRENT_STATE.md', active.workItemId],
    ['SESSION_HANDOFF.md', active.workItemId]
  ]);
  const findings = [];
  for (const [name, expected] of required) {
    const document = documents.find(item => item.name === name);
    if (!document) {
      findings.push({ code: 'document.missing', severity: 'blocking', document: name, expected });
      continue;
    }
    if (document.workItemId !== expected) {
      findings.push({ code: 'document.stale-work-item', severity: 'blocking', document: name, expected, actual: document.workItemId });
    }
  }
  return findings;
}
