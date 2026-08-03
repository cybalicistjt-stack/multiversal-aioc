const clone = value => JSON.parse(JSON.stringify(value));

const severityRank = { blocker: 0, error: 1, warning: 2, info: 3 };

function sortFindings(findings = []) {
  return [...findings].sort((a, b) =>
    (severityRank[a.severity] ?? 9) - (severityRank[b.severity] ?? 9) ||
    String(a.code).localeCompare(String(b.code)) ||
    String(a.path ?? '').localeCompare(String(b.path ?? ''))
  );
}

function normalizeChange(change) {
  if (!change?.id) throw Object.assign(new Error('Change id is required'), { code: 'change.id' });
  if (!change?.repositoryId) throw Object.assign(new Error('Repository id is required'), { code: 'change.repository' });
  if (!Array.isArray(change.files) || change.files.length === 0) {
    throw Object.assign(new Error('At least one file is required'), { code: 'change.files' });
  }
  return {
    id: change.id,
    repositoryId: change.repositoryId,
    title: change.title ?? change.id,
    description: change.description ?? '',
    files: [...new Set(change.files)].sort(),
    capabilities: [...new Set(change.capabilities ?? [])].sort(),
    dependencies: [...new Set(change.dependencies ?? [])].sort(),
    acceptanceCriteria: [...new Set(change.acceptanceCriteria ?? [])],
    evidence: [...new Set(change.evidence ?? [])].sort(),
    risk: change.risk ?? 'normal'
  };
}

export function projectDeveloperWorkbench({ state, repositoryHealth, continuityCertification, change }) {
  if (!state?.active?.workItemId) throw Object.assign(new Error('Canonical active work item is required'), { code: 'state.active' });
  const normalized = normalizeChange(change);
  const findings = [];
  const repository = state.repositories?.find(item => item.id === normalized.repositoryId);
  if (!repository) findings.push({ severity: 'blocker', code: 'repository.unknown', message: `Unknown repository ${normalized.repositoryId}` });

  if (!continuityCertification || continuityCertification.result === 'FAIL') {
    findings.push({ severity: 'blocker', code: 'continuity.blocked', message: 'Continuity certification does not permit development work' });
  }

  const health = repositoryHealth?.repositories?.find(item => item.repositoryId === normalized.repositoryId);
  if (!health) findings.push({ severity: 'blocker', code: 'health.missing', message: 'Repository health evidence is missing' });
  else if (health.status === 'blocked' || health.status === 'unknown') {
    findings.push({ severity: 'blocker', code: 'health.blocked', message: `Repository health is ${health.status}` });
  } else if (health.status === 'degraded') {
    findings.push({ severity: 'warning', code: 'health.degraded', message: 'Repository health is degraded' });
  }

  const workItem = state.workItems?.find(item => item.id === state.active.workItemId);
  if (!workItem) findings.push({ severity: 'blocker', code: 'workItem.missing', message: 'Active work item is missing' });

  for (const dependency of normalized.dependencies) {
    const item = state.workItems?.find(candidate => candidate.id === dependency);
    if (!item || item.status !== 'complete') {
      findings.push({ severity: 'blocker', code: 'dependency.incomplete', message: `Dependency ${dependency} is not complete` });
    }
  }

  if (normalized.acceptanceCriteria.length === 0) {
    findings.push({ severity: 'warning', code: 'acceptance.empty', message: 'No acceptance criteria were supplied' });
  }
  if (normalized.capabilities.length === 0) {
    findings.push({ severity: 'warning', code: 'capability.empty', message: 'No required capabilities were declared' });
  }
  if (normalized.risk === 'high' && normalized.evidence.length === 0) {
    findings.push({ severity: 'blocker', code: 'risk.evidence', message: 'High-risk changes require prior evidence' });
  }

  const orderedFindings = sortFindings(findings);
  const blocked = orderedFindings.some(item => item.severity === 'blocker' || item.severity === 'error');
  return {
    schemaVersion: '1.0.0',
    change: normalized,
    context: {
      repository: repository ? { id: repository.id, fullName: repository.fullName, defaultBranch: repository.defaultBranch } : null,
      branch: state.active.branch,
      milestoneId: state.active.milestoneId,
      workItemId: state.active.workItemId,
      workItemTitle: workItem?.title ?? null
    },
    execution: {
      permitted: !blocked,
      mode: blocked ? 'recovery' : 'change-planning',
      requiredCapabilities: normalized.capabilities,
      requiredEvidence: normalized.acceptanceCriteria.map((criterion, index) => ({ id: `${normalized.id}-AC-${index + 1}`, criterion }))
    },
    impact: {
      fileCount: normalized.files.length,
      files: normalized.files,
      dependencyCount: normalized.dependencies.length,
      risk: normalized.risk
    },
    findings: orderedFindings
  };
}

export function assertWorkbenchReady(projection) {
  if (!projection?.execution?.permitted) {
    throw Object.assign(new Error('Developer workbench execution is blocked'), {
      code: 'workbench.blocked',
      findings: clone(projection?.findings ?? [])
    });
  }
  return projection;
}

export function createChangePlan(projection, { actor, steps = [] } = {}) {
  assertWorkbenchReady(projection);
  if (!actor) throw Object.assign(new Error('Actor is required'), { code: 'plan.actor' });
  if (!Array.isArray(steps) || steps.length === 0) throw Object.assign(new Error('Plan steps are required'), { code: 'plan.steps' });
  return {
    schemaVersion: '1.0.0',
    id: `plan-${projection.change.id}`,
    changeId: projection.change.id,
    actor,
    repositoryId: projection.change.repositoryId,
    branch: projection.context.branch,
    workItemId: projection.context.workItemId,
    steps: steps.map((step, index) => ({ sequence: index + 1, action: step.action, paths: [...new Set(step.paths ?? [])].sort() })),
    acceptanceEvidence: projection.execution.requiredEvidence,
    status: 'planned'
  };
}
