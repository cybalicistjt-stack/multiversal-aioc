import { createHash } from 'node:crypto';

const milestones = ['AIOC-I-001','AIOC-I-002','AIOC-I-003','AIOC-I-004','AIOC-I-005','AIOC-I-006','AIOC-I-007'];
const capabilities = ['project-state','continuity','repository-intelligence','orchestration','developer-workbench','content-studio','testing-simulation','release-hardening','deployment-recovery'];

const stable = value => Array.isArray(value)
  ? value.map(stable)
  : value && typeof value === 'object'
    ? Object.fromEntries(Object.keys(value).sort().map(key => [key, stable(value[key])]))
    : value;

const hash = value => createHash('sha256').update(JSON.stringify(stable(value))).digest('hex');
const hasEvidence = value => Boolean(value?.evidenceId && value?.evidenceUri && value?.observedAt);

export function certifyAiocOperationalRelease(input = {}) {
  const findings = [];
  const error = (code, message) => findings.push({ severity: 'error', code, message });
  const warning = (code, message) => findings.push({ severity: 'warning', code, message });

  if (input.continuity?.result !== 'PASS') error('continuity.not-pass', 'Continuity certification must pass.');
  if (input.repositoryHealth?.status !== 'healthy') error('repository.unhealthy', 'Repository health must be healthy.');
  if (!input.canonical?.repository || !input.canonical?.branch || !input.canonical?.workItemId) error('canonical.missing', 'Canonical bindings are required.');

  const milestoneMap = new Map((input.milestones ?? []).map(item => [item.id, item]));
  for (const id of milestones) {
    const item = milestoneMap.get(id);
    if (!item) error('milestone.missing', `Missing ${id}.`);
    else if (item.result !== 'PASS') error('milestone.not-pass', `${id} must pass.`);
    else if (!hasEvidence(item)) error('milestone.evidence', `${id} lacks durable evidence.`);
  }

  const capabilityMap = new Map((input.capabilities ?? []).map(item => [item.id, item]));
  for (const id of capabilities) {
    const item = capabilityMap.get(id);
    if (!item?.available) error('capability.unavailable', `${id} is unavailable.`);
    else if (!hasEvidence(item)) error('capability.evidence', `${id} lacks durable evidence.`);
  }

  if (input.deploymentCertification?.result !== 'PASS') error('deployment.not-pass', 'Deployment certification must pass.');
  if (!input.deploymentCertification?.fingerprint || !hasEvidence(input.deploymentCertification)) error('deployment.evidence', 'Deployment evidence is incomplete.');
  if (input.ownerApproval?.decision !== 'approved' || !hasEvidence(input.ownerApproval)) error('approval.missing', 'Evidence-backed owner approval is required.');

  const handoff = input.operationalHandoff;
  if (!handoff?.nextAction || !handoff?.supportModel || !handoff?.recoveryEntryPoint || !hasEvidence(handoff)) error('handoff.incomplete', 'Operational handoff is incomplete.');

  for (const risk of input.openRisks ?? []) {
    if (['critical','high'].includes(risk.severity)) error('risk.blocking', `Blocking risk ${risk.id ?? 'unknown'} remains open.`);
    else warning('risk.nonblocking', `Nonblocking risk ${risk.id ?? 'unknown'} remains open.`);
  }

  const result = findings.some(item => item.severity === 'error') ? 'FAIL' : findings.length ? 'PASS WITH WARNINGS' : 'PASS';
  const certificate = {
    schemaVersion: '1.0.0',
    certificateId: input.certificateId ?? 'AIOC-OPERATIONAL-CERTIFICATE',
    result,
    completionAuthorized: result === 'PASS',
    executionFrozen: result !== 'PASS',
    canonical: input.canonical ?? null,
    milestoneIds: [...milestoneMap.keys()].sort(),
    capabilityIds: [...capabilityMap.keys()].sort(),
    deploymentFingerprint: input.deploymentCertification?.fingerprint ?? null,
    findings: findings.sort((a,b) => `${a.severity}:${a.code}:${a.message}`.localeCompare(`${b.severity}:${b.code}:${b.message}`)),
    nextAction: result === 'PASS' ? handoff.nextAction : 'Resolve findings and rerun final operational certification.'
  };
  return { ...certificate, fingerprint: hash(certificate) };
}

export const FINAL_OPERATIONAL_REQUIREMENTS = Object.freeze({ milestones, capabilities });
