const SEVERITY_ORDER = Object.freeze({ blocker: 0, critical: 1, warning: 2, info: 3 });

const clone = value => globalThis.structuredClone ? globalThis.structuredClone(value) : JSON.parse(JSON.stringify(value));

function percent(completed, total) {
  return total ? Math.round((completed / total) * 100) : 0;
}

function normalizeCheck(check = {}) {
  const conclusion = check.conclusion || check.status || 'unknown';
  const state = ['success', 'neutral', 'skipped'].includes(conclusion) ? 'pass'
    : ['failure', 'timed_out', 'cancelled', 'action_required'].includes(conclusion) ? 'fail'
    : 'pending';
  return { name: check.name || 'unnamed', state, conclusion, url: check.url || null };
}

function findingSeverity(finding = {}) {
  if (finding.blocking || finding.severity === 'blocker') return 'blocker';
  if (finding.severity === 'critical' || finding.severity === 'error') return 'critical';
  if (finding.severity === 'warning') return 'warning';
  return 'info';
}

function repositoryCard(repository, health = {}, checks = []) {
  const normalizedChecks = checks.map(normalizeCheck);
  const failed = normalizedChecks.filter(check => check.state === 'fail').length;
  const pending = normalizedChecks.filter(check => check.state === 'pending').length;
  const status = health.status || (failed ? 'blocked' : pending ? 'degraded' : 'healthy');
  return {
    id: repository.id,
    fullName: repository.fullName,
    purpose: repository.purpose,
    status,
    branch: health.branch || repository.defaultBranch,
    headSha: health.headSha || null,
    pullRequests: health.pullRequests || 0,
    checks: normalizedChecks,
    findings: clone(health.findings || [])
  };
}

function milestoneCards(state) {
  return [...state.milestones]
    .sort((a, b) => a.sequence - b.sequence)
    .map(milestone => {
      const work = state.workItems.filter(item => item.milestoneId === milestone.id);
      const complete = work.filter(item => item.status === 'complete').length;
      const blocked = work.filter(item => item.status === 'blocked').length;
      return {
        id: milestone.id,
        title: milestone.title,
        status: milestone.status,
        progress: percent(complete, work.length),
        completedItems: complete,
        totalItems: work.length,
        blockedItems: blocked,
        activeItem: work.find(item => item.status === 'active')?.id || null
      };
    });
}

function blockers(state, repositoryHealth, certification) {
  const items = [];
  for (const item of state.workItems.filter(work => work.status === 'blocked')) {
    items.push({ id: `work:${item.id}`, severity: 'blocker', source: 'work-item', title: item.title, detail: item.blocker || 'Blocked' });
  }
  for (const health of Object.values(repositoryHealth || {})) {
    for (const finding of health.findings || []) {
      const severity = findingSeverity(finding);
      if (severity !== 'info') items.push({ id: finding.id || `repo:${items.length}`, severity, source: 'repository', title: finding.title || finding.code || 'Repository finding', detail: finding.message || '' });
    }
  }
  for (const finding of certification?.findings || []) {
    const severity = findingSeverity(finding);
    if (severity !== 'info') items.push({ id: finding.id || `continuity:${items.length}`, severity, source: 'continuity', title: finding.title || finding.code || 'Continuity finding', detail: finding.message || '' });
  }
  return items.sort((a, b) => SEVERITY_ORDER[a.severity] - SEVERITY_ORDER[b.severity] || a.id.localeCompare(b.id));
}

function executiveSummary({ activeMilestone, activeWorkItem, projectHealth, blockerCount, repositoryCards }) {
  const healthy = repositoryCards.filter(card => card.status === 'healthy').length;
  const total = repositoryCards.length;
  const action = activeWorkItem ? `${activeWorkItem.id} — ${activeWorkItem.title}` : 'No active work item';
  return `${projectHealth.toUpperCase()}: ${activeMilestone?.id || 'No milestone'}; ${healthy}/${total} repositories healthy; ${blockerCount} blocking or warning findings; next action ${action}.`;
}

export function buildExecutiveDashboard({ state, repositoryHealth = {}, ciChecks = {}, continuityCertification = null, generatedAt = new Date().toISOString() }) {
  if (!state?.active) throw new Error('Canonical project state with active pointers is required.');
  const activeMilestone = state.milestones.find(item => item.id === state.active.milestoneId) || null;
  const activeWorkItem = state.workItems.find(item => item.id === state.active.workItemId) || null;
  const repositories = state.repositories.map(repository => repositoryCard(repository, repositoryHealth[repository.id], ciChecks[repository.id] || []));
  const findingList = blockers(state, repositoryHealth, continuityCertification);
  const hardBlocked = continuityCertification?.executionAllowed === false || repositories.some(repository => repository.status === 'blocked') || findingList.some(item => item.severity === 'blocker');
  const degraded = repositories.some(repository => ['degraded', 'unknown'].includes(repository.status)) || findingList.some(item => ['critical', 'warning'].includes(item.severity));
  const projectHealth = hardBlocked ? 'blocked' : degraded ? 'degraded' : 'healthy';
  const milestones = milestoneCards(state);
  const completedWork = state.workItems.filter(item => item.status === 'complete').length;
  const dashboard = {
    schemaVersion: '1.0.0',
    generatedAt,
    project: { id: state.project.id, name: state.project.name, owner: state.project.owner, health: projectHealth },
    active: {
      repositoryId: state.active.repositoryId,
      branch: state.active.branch,
      milestone: activeMilestone ? clone(activeMilestone) : null,
      workItem: activeWorkItem ? clone(activeWorkItem) : null,
      nextAction: continuityCertification?.nextAction || activeWorkItem?.title || null,
      executionAllowed: !hardBlocked
    },
    progress: { completedWorkItems: completedWork, totalWorkItems: state.workItems.length, percent: percent(completedWork, state.workItems.length), milestones },
    repositories,
    findings: findingList,
    counters: {
      blockers: findingList.filter(item => item.severity === 'blocker').length,
      critical: findingList.filter(item => item.severity === 'critical').length,
      warnings: findingList.filter(item => item.severity === 'warning').length,
      openDecisions: state.decisions.filter(item => item.status === 'open').length,
      blockedWorkItems: state.workItems.filter(item => item.status === 'blocked').length
    }
  };
  dashboard.summary = executiveSummary({ activeMilestone, activeWorkItem, projectHealth, blockerCount: dashboard.counters.blockers + dashboard.counters.critical + dashboard.counters.warnings, repositoryCards: repositories });
  return dashboard;
}

export function assertDashboardExecutable(dashboard) {
  if (!dashboard?.active?.executionAllowed) {
    const error = new Error('Executive dashboard blocks execution until governed findings are resolved.');
    error.code = 'dashboard.execution-blocked';
    error.findings = clone(dashboard?.findings || []);
    throw error;
  }
  return dashboard;
}
