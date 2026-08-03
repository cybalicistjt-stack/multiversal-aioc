import fs from 'node:fs';

const artifact = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const allowed = new Set(['awaiting-owner-approval', 'approved-validation-ready', 'approved-stale', 'rejected', 'blocked']);
const failures = [];
if (artifact.format !== 'multiversal-aioc-continuous-validation-approval') failures.push('invalid format');
if (!Array.isArray(artifact.gates) || artifact.gates.length === 0) failures.push('gates must contain at least one item');
if (!Array.isArray(artifact.auditTrail) || artifact.auditTrail.length !== artifact.gates?.length) failures.push('audit trail must cover every gate');
for (const gate of artifact.gates || []) {
  if (!gate.gateId || !gate.packageId || !gate.packageFingerprint) failures.push('gate identities and fingerprint are required');
  if (!allowed.has(gate.status)) failures.push(`${gate.gateId}: invalid status`);
  if (!Array.isArray(gate.requiredApprovals) || !gate.requiredApprovals.includes('human-owner')) failures.push(`${gate.gateId}: human owner approval requirement missing`);
  if (gate.status === 'approved-validation-ready') {
    if (gate.decision?.action !== 'approve' || gate.decision?.actorType !== 'human-owner') failures.push(`${gate.gateId}: approved state lacks explicit human owner approval`);
    if (gate.decision?.packageFingerprint !== gate.packageFingerprint) failures.push(`${gate.gateId}: approved state fingerprint mismatch`);
    if (gate.executionEligibility !== 'validation-only') failures.push(`${gate.gateId}: approved state may only allow validation readiness`);
  } else if (gate.executionEligibility !== 'none') failures.push(`${gate.gateId}: non-approved gate has eligibility`);
  if (gate.status === 'approved-stale' && (!Array.isArray(gate.invalidationReasons) || gate.invalidationReasons.length === 0)) failures.push(`${gate.gateId}: stale approval lacks invalidation reason`);
}
if (!artifact.authority?.proposalOnly || artifact.authority?.executionAllowed || artifact.authority?.canonicalMutationAllowed || artifact.authority?.approvalMayBeInferred || artifact.authority?.mergeAllowed) failures.push('unsafe authority declaration');
if (failures.length) { console.error(failures.join('\n')); process.exit(1); }
console.log(`Validated ${artifact.gates.length} human approval gates and audit records.`);
