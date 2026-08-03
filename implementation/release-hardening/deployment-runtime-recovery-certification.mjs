import crypto from 'node:crypto';

const REQUIRED_RUNTIME_CHECKS = ['startup','health','persistence','permissions','continuity'];
const REQUIRED_RECOVERY_CHECKS = ['rollback','restore','data-integrity','service-recovery'];

function stable(value) {
  if (Array.isArray(value)) return value.map(stable);
  if (value && typeof value === 'object') {
    return Object.fromEntries(Object.keys(value).sort().map((key) => [key, stable(value[key])]));
  }
  return value;
}

function fingerprint(value) {
  return crypto.createHash('sha256').update(JSON.stringify(stable(value))).digest('hex');
}

function finding(code, message, severity = 'error') {
  return { code, message, severity };
}

export function certifyDeploymentExecution(input = {}) {
  const findings = [];
  const readiness = input.releaseReadiness ?? {};
  const deployment = input.deployment ?? {};
  const runtimeChecks = Array.isArray(input.runtimeChecks) ? input.runtimeChecks : [];
  const recoveryChecks = Array.isArray(input.recoveryChecks) ? input.recoveryChecks : [];
  const approvals = Array.isArray(input.approvals) ? input.approvals : [];
  const evidence = Array.isArray(input.evidence) ? input.evidence : [];

  if (readiness.result !== 'PASS') findings.push(finding('readiness.not-pass', 'Release readiness must be a clean PASS.'));
  if (!readiness.fingerprint) findings.push(finding('readiness.fingerprint.missing', 'Release-readiness fingerprint is required.'));

  for (const field of ['repository','branch','workItemId','releaseId','version','environment','commitSha']) {
    if (!deployment[field]) findings.push(finding(`deployment.${field}.missing`, `Deployment ${field} is required.`));
  }

  if (deployment.repository !== input.canonical?.repository) findings.push(finding('canonical.repository.mismatch', 'Deployment repository does not match canonical state.'));
  if (deployment.branch !== input.canonical?.branch) findings.push(finding('canonical.branch.mismatch', 'Deployment branch does not match canonical state.'));
  if (deployment.workItemId !== input.canonical?.workItemId) findings.push(finding('canonical.work-item.mismatch', 'Deployment work item does not match canonical state.'));

  if (!deployment.startedAt || !deployment.completedAt) findings.push(finding('deployment.timestamps.missing', 'Deployment start and completion timestamps are required.'));
  if (deployment.status !== 'succeeded') findings.push(finding('deployment.failed', 'Deployment execution did not succeed.'));
  if (!deployment.artifactChecksum || deployment.artifactChecksum !== readiness.artifactChecksum) findings.push(finding('artifact.checksum.mismatch', 'Deployed artifact checksum does not match release readiness evidence.'));

  const runtimeById = new Map(runtimeChecks.map((check) => [check.id, check]));
  for (const id of REQUIRED_RUNTIME_CHECKS) {
    const check = runtimeById.get(id);
    if (!check) findings.push(finding(`runtime.${id}.missing`, `Required runtime check ${id} is missing.`));
    else if (check.status !== 'pass') findings.push(finding(`runtime.${id}.failed`, `Required runtime check ${id} did not pass.`));
    else if (!check.evidenceId) findings.push(finding(`runtime.${id}.evidence.missing`, `Runtime check ${id} lacks evidence.`));
  }

  const recoveryById = new Map(recoveryChecks.map((check) => [check.id, check]));
  for (const id of REQUIRED_RECOVERY_CHECKS) {
    const check = recoveryById.get(id);
    if (!check) findings.push(finding(`recovery.${id}.missing`, `Required recovery check ${id} is missing.`));
    else if (check.status !== 'pass') findings.push(finding(`recovery.${id}.failed`, `Required recovery check ${id} did not pass.`));
    else if (!check.evidenceId) findings.push(finding(`recovery.${id}.evidence.missing`, `Recovery check ${id} lacks evidence.`));
  }

  const ownerApproval = approvals.find((approval) => approval.role === 'owner' && approval.decision === 'approve' && approval.evidenceId);
  if (!ownerApproval) findings.push(finding('approval.owner.missing', 'Evidence-backed owner approval is required.'));

  const evidenceIds = new Set(evidence.map((item) => item.id));
  for (const id of [...runtimeChecks, ...recoveryChecks].map((check) => check.evidenceId).filter(Boolean)) {
    if (!evidenceIds.has(id)) findings.push(finding('evidence.unresolved', `Referenced evidence ${id} is unavailable.`));
  }
  for (const approval of approvals.filter((item) => item.evidenceId)) {
    if (!evidenceIds.has(approval.evidenceId)) findings.push(finding('approval.evidence.unresolved', `Approval evidence ${approval.evidenceId} is unavailable.`));
  }

  const warnings = findings.filter((item) => item.severity === 'warning');
  const errors = findings.filter((item) => item.severity === 'error');
  const result = errors.length ? 'FAIL' : warnings.length ? 'PASS WITH WARNINGS' : 'PASS';
  const certification = {
    schemaVersion: '1.0.0',
    workItemId: 'AIOC-I-007B',
    result,
    executionFrozen: result !== 'PASS',
    completionAuthorized: result === 'PASS',
    deployment: stable(deployment),
    runtimeChecks: stable(runtimeChecks),
    recoveryChecks: stable(recoveryChecks),
    findings,
    nextAction: result === 'PASS'
      ? 'Advance to final operational release certification.'
      : 'Correct deployment, runtime, recovery, approval, or evidence failures and recertify.'
  };
  certification.fingerprint = fingerprint(certification);
  return certification;
}

export const requiredRuntimeChecks = Object.freeze([...REQUIRED_RUNTIME_CHECKS]);
export const requiredRecoveryChecks = Object.freeze([...REQUIRED_RECOVERY_CHECKS]);
