import fs from 'node:fs';

const artifactPath = process.argv[2] || 'governance/development-brain/safe-plans/AIOC_SAFE_PLAN_PROPOSALS.generated.json';
const artifact = JSON.parse(fs.readFileSync(artifactPath, 'utf8'));
const allowedStatuses = new Set(['proposal-only', 'owner-decision-required', 'blocked', 'observation-only', 'later-executable-after-approval']);
const failures = [];
if (artifact.format !== 'multiversal-aioc-safe-plan-proposal') failures.push('invalid format');
if (!Array.isArray(artifact.plans)) failures.push('plans must be an array');
for (const plan of artifact.plans || []) {
  if (!allowedStatuses.has(plan.status)) failures.push(`${plan.planId}: invalid status`);
  if (!Array.isArray(plan.evidence)) failures.push(`${plan.planId}: missing evidence array`);
  if (!Array.isArray(plan.sequence) || plan.sequence.length === 0) failures.push(`${plan.planId}: missing sequence`);
  if (!Array.isArray(plan.approvalRequirements) || plan.approvalRequirements.length === 0) failures.push(`${plan.planId}: missing approval requirements`);
  if (!Array.isArray(plan.rejectionPath) || plan.rejectionPath.length === 0) failures.push(`${plan.planId}: missing rejection path`);
  if (!Array.isArray(plan.rollbackGuidance) || plan.rollbackGuidance.length === 0) failures.push(`${plan.planId}: missing rollback guidance`);
}
if (!artifact.authority?.proposalOnly || artifact.authority?.canonicalMutationAllowed || artifact.authority?.approvalGranted || artifact.authority?.executionAllowed) failures.push('unsafe authority declaration');
if ((artifact.diagnostics?.unsupportedExecutionClaims || []).length > 0) failures.push('unsupported execution claims present');
if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log(`Validated ${artifact.plans.length} safe plans.`);
