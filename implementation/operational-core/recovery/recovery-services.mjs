import { validateProjectState, stableStringify } from '../project-state/project-state-engine.mjs';

const clone = value => globalThis.structuredClone ? globalThis.structuredClone(value) : JSON.parse(JSON.stringify(value));
const now = () => new Date().toISOString();

function invariant(condition, message, code = 'recovery.invalid') {
  if (!condition) {
    const error = new Error(message);
    error.code = code;
    throw error;
  }
}

function sorted(items, selector) {
  return [...items].sort((a, b) => selector(a).localeCompare(selector(b)));
}

export function buildSessionOrientation(state, { repositoryObservations = [], capabilityEvidence = [] } = {}) {
  const errors = validateProjectState(state).filter(issue => issue.severity === 'error');
  invariant(errors.length === 0, errors.map(issue => `${issue.code}: ${issue.message}`).join('\n'), 'recovery.state-invalid');

  const activeItem = state.workItems.find(item => item.id === state.active.workItemId);
  const activeMilestone = state.milestones.find(item => item.id === state.active.milestoneId);
  const activeRepository = state.repositories.find(item => item.id === state.active.repositoryId);
  invariant(activeItem && activeMilestone && activeRepository, 'Active pointers cannot be resolved.', 'recovery.active-pointer');

  const blockers = state.workItems
    .filter(item => item.status === 'blocked')
    .map(item => ({ id: item.id, title: item.title, blocker: item.blocker || 'Unspecified blocker' }));

  const openDecisions = state.decisions
    .filter(decision => !['approved', 'rejected', 'superseded'].includes(decision.status))
    .map(decision => ({ id: decision.id, title: decision.title, status: decision.status }));

  const latestHandoff = sorted(state.handoffs || [], item => item.createdAt || '').at(-1) || null;

  return {
    generatedAt: now(),
    project: { id: state.project.id, name: state.project.name, owner: state.project.owner },
    active: {
      repository: { id: activeRepository.id, fullName: activeRepository.fullName },
      milestone: { id: activeMilestone.id, title: activeMilestone.title },
      workItem: { id: activeItem.id, title: activeItem.title, status: activeItem.status },
      branch: state.active.branch
    },
    blockers,
    openDecisions,
    latestHandoff,
    repositoryObservations: clone(repositoryObservations),
    capabilityEvidence: clone(capabilityEvidence),
    nextAction: latestHandoff?.nextAction || `Execute ${activeItem.id} — ${activeItem.title}`
  };
}

export function detectContinuityConflicts(state, claims = [], repositoryObservations = []) {
  const findings = [];
  const workById = new Map(state.workItems.map(item => [item.id, item]));
  const repoById = new Map(state.repositories.map(item => [item.id, item]));

  for (const claim of claims) {
    if (claim.type === 'work-complete') {
      const item = workById.get(claim.workItemId);
      if (!item) findings.push({ severity: 'error', code: 'claim.unknown-work', claimId: claim.id, message: `Unknown work item ${claim.workItemId}.` });
      else if (item.status !== 'complete') findings.push({ severity: 'error', code: 'claim.false-completion', claimId: claim.id, message: `${claim.workItemId} is ${item.status}, not complete.` });
      else if (!(item.evidence || []).length) findings.push({ severity: 'error', code: 'claim.missing-evidence', claimId: claim.id, message: `${claim.workItemId} has no completion evidence.` });
    }
    if (claim.type === 'repository-write') {
      const repository = repoById.get(claim.repositoryId);
      if (!repository) findings.push({ severity: 'error', code: 'claim.unknown-repository', claimId: claim.id, message: `Unknown repository ${claim.repositoryId}.` });
      const observation = repositoryObservations.find(item => item.repositoryId === claim.repositoryId);
      if (!observation?.capabilities?.push) findings.push({ severity: 'error', code: 'claim.unverified-write', claimId: claim.id, message: `Write capability for ${claim.repositoryId} is not verified.` });
      if (claim.commitSha && observation?.headSha && claim.commitSha !== observation.headSha) {
        findings.push({ severity: 'warning', code: 'claim.commit-drift', claimId: claim.id, message: `Claimed commit ${claim.commitSha} differs from observed head ${observation.headSha}.` });
      }
    }
  }

  const activeItems = state.workItems.filter(item => item.status === 'active');
  if (activeItems.length !== 1) findings.push({ severity: 'error', code: 'state.active-count', message: `Expected one active item; found ${activeItems.length}.` });
  if (activeItems[0] && activeItems[0].id !== state.active.workItemId) findings.push({ severity: 'error', code: 'state.active-pointer', message: 'Active pointer disagrees with active work item.' });

  return findings;
}

export function buildRecoveryPlan(state, findings, { owner = state.project.owner } = {}) {
  const blocking = findings.filter(item => item.severity === 'error');
  const steps = [];

  if (blocking.some(item => item.code.startsWith('state.'))) {
    steps.push({ order: steps.length + 1, action: 'freeze-writes', reason: 'Canonical state invariants are broken.' });
    steps.push({ order: steps.length + 1, action: 'restore-last-valid-snapshot', reason: 'Return to a validated canonical state.' });
  }
  if (blocking.some(item => item.code === 'claim.false-completion' || item.code === 'claim.missing-evidence')) {
    steps.push({ order: steps.length + 1, action: 'reopen-unverified-work', reason: 'Completion cannot stand without canonical evidence.' });
  }
  if (blocking.some(item => item.code === 'claim.unverified-write')) {
    steps.push({ order: steps.length + 1, action: 'verify-connector-capabilities', reason: 'Repository write claims require live permission evidence.' });
  }
  if (!steps.length) steps.push({ order: 1, action: 'continue-active-work', reason: 'No blocking continuity conflicts were detected.' });

  return {
    id: `recovery-${Date.now()}`,
    generatedAt: now(),
    owner,
    blocking: blocking.length > 0,
    findings: clone(findings),
    steps,
    checksumInput: stableStringify({ active: state.active, findings, steps })
  };
}

export function createDecisionRecord({ id, title, status = 'open', rationale = '', evidence = [], authority = 'owner' }) {
  invariant(id && title, 'Decision id and title are required.', 'decision.required');
  invariant(['open', 'proposed', 'approved', 'rejected', 'superseded'].includes(status), `Unsupported decision status ${status}.`, 'decision.status');
  if (['approved', 'rejected', 'superseded'].includes(status)) invariant(rationale.trim().length > 0, 'Resolved decisions require rationale.', 'decision.rationale');
  return { id, title, status, authority, rationale, evidence: [...evidence], createdAt: now(), resolvedAt: ['approved', 'rejected', 'superseded'].includes(status) ? now() : null };
}

export function createSessionHandoff({ id, state, summary, completed = [], nextAction, evidence = [], risks = [] }) {
  invariant(id && summary && nextAction, 'Handoff id, summary, and nextAction are required.', 'handoff.required');
  const orientation = buildSessionOrientation(state);
  return {
    id,
    createdAt: now(),
    workItemId: state.active.workItemId,
    summary,
    completed: [...completed],
    nextAction,
    evidence: [...evidence],
    risks: [...risks],
    orientationFingerprint: stableStringify({ active: orientation.active, nextAction: orientation.nextAction })
  };
}
