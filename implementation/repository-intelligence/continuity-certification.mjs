const REQUIRED_DOCS = Object.freeze([
  'governance/current-state/AIOC_CURRENT_STATE.md',
  'governance/current-state/SESSION_HANDOFF.md',
  'governance/roadmaps/AIOC_CANONICAL_ROADMAP.md',
  'governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md'
]);

const clone = value => globalThis.structuredClone ? globalThis.structuredClone(value) : JSON.parse(JSON.stringify(value));

function finding(severity, code, message, evidence = []) {
  return { severity, code, message, evidence: [...evidence] };
}

export function inspectDocumentationDrift({ state, documents = {}, snapshot = null, health = null }) {
  const findings = [];
  const active = state?.active || {};
  const activeItem = (state?.workItems || []).find(item => item.id === active.workItemId);

  for (const path of REQUIRED_DOCS) {
    if (!documents[path]?.content) findings.push(finding('blocking', 'document.missing', `Required continuity document is missing: ${path}`, [path]));
  }

  const currentState = documents['governance/current-state/AIOC_CURRENT_STATE.md']?.content || '';
  const handoff = documents['governance/current-state/SESSION_HANDOFF.md']?.content || '';
  const roadmap = documents['governance/roadmaps/AIOC_CANONICAL_ROADMAP.md']?.content || '';

  if (active.workItemId && !currentState.includes(active.workItemId)) {
    findings.push(finding('blocking', 'current-state.work-item-drift', `Current-state document does not identify active work item ${active.workItemId}.`, ['canonical-state', 'AIOC_CURRENT_STATE.md']));
  }
  if (active.milestoneId && !currentState.includes(active.milestoneId)) {
    findings.push(finding('blocking', 'current-state.milestone-drift', `Current-state document does not identify active milestone ${active.milestoneId}.`, ['canonical-state', 'AIOC_CURRENT_STATE.md']));
  }
  if (active.branch && !currentState.includes(active.branch)) {
    findings.push(finding('warning', 'current-state.branch-drift', `Current-state document does not identify active branch ${active.branch}.`, ['canonical-state', 'AIOC_CURRENT_STATE.md']));
  }
  if (active.workItemId && !handoff.includes(active.workItemId)) {
    findings.push(finding('blocking', 'handoff.work-item-drift', `Session handoff does not identify active work item ${active.workItemId}.`, ['canonical-state', 'SESSION_HANDOFF.md']));
  }
  if (activeItem?.title && !roadmap.includes(activeItem.id)) {
    findings.push(finding('warning', 'roadmap.work-item-missing', `Canonical roadmap does not mention ${activeItem.id}.`, ['canonical-state', 'AIOC_CANONICAL_ROADMAP.md']));
  }

  if (!snapshot) findings.push(finding('blocking', 'snapshot.missing', 'No verified continuity snapshot was supplied.', ['continuity-snapshot']));
  else {
    if (snapshot.status !== 'verified') findings.push(finding('blocking', 'snapshot.unverified', `Continuity snapshot status is ${snapshot.status}.`, ['continuity-snapshot']));
    if (snapshot.orientation?.workItemId !== active.workItemId) findings.push(finding('blocking', 'snapshot.work-item-drift', 'Snapshot work item does not match canonical state.', ['continuity-snapshot', 'canonical-state']));
    if (snapshot.orientation?.branch !== active.branch) findings.push(finding('blocking', 'snapshot.branch-drift', 'Snapshot branch does not match canonical state.', ['continuity-snapshot', 'canonical-state']));
  }

  if (!health) findings.push(finding('blocking', 'health.missing', 'No repository-health projection was supplied.', ['repository-intelligence']));
  else if (['blocked', 'unknown'].includes(health.overall)) findings.push(finding('blocking', 'health.not-certifiable', `Repository health is ${health.overall}.`, ['repository-intelligence']));
  else if (health.overall === 'degraded') findings.push(finding('warning', 'health.degraded', 'Repository health is degraded; certification may proceed only with recorded warnings.', ['repository-intelligence']));

  return findings;
}

export function certifyContinuity(input) {
  const findings = inspectDocumentationDrift(input);
  const blocking = findings.filter(item => item.severity === 'blocking');
  const warnings = findings.filter(item => item.severity === 'warning');
  return {
    schemaVersion: '1.0.0',
    status: blocking.length ? 'fail' : warnings.length ? 'pass-with-warnings' : 'pass',
    certifiedAt: input.certifiedAt || new Date().toISOString(),
    active: clone(input.state.active),
    evidence: [...new Set(findings.flatMap(item => item.evidence))],
    findings,
    counts: { blocking: blocking.length, warnings: warnings.length },
    executionAllowed: blocking.length === 0
  };
}

export function assertContinuityCertified(certificate) {
  if (!certificate?.executionAllowed) {
    const error = new Error('Continuity certification failed; execution is frozen.');
    error.code = 'continuity.not-certified';
    error.certificate = clone(certificate);
    throw error;
  }
  return certificate;
}

export { REQUIRED_DOCS };
