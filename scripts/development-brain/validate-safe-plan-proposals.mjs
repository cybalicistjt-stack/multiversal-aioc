import fs from 'node:fs';

const artifactPath = process.argv[2] || 'governance/development-brain/safe-plans/AIOC_SAFE_PLAN_PROPOSALS.generated.json';
const artifact = JSON.parse(fs.readFileSync(artifactPath, 'utf8'));
const allowedStatuses = new Set(['proposal-only', 'owner-decision-required', 'blocked', 'observation-only', 'later-executable-after-approval']);
const failures = [];
if (artifact.format !== 'multiversal-aioc-safe-plan-proposal') failures.push('invalid format');
if (!Array.isArray(artifact.plans)) failures.push('plans must be an array');
if (Array.isArray(artifact.plans) && artifact.plans.length === 0) failures.push('plans must contain at least one meaningful plan');
for (const plan of artifact.plans || []) {
  if (!plan.planId || !plan.sourceReviewId) failures.push('plan must preserve stable plan and source review identities');
  if (!allowedStatuses.has(plan.status)) failures.push(`${plan.planId}: invalid status`);
  if (!Array.isArray(plan.scope) || plan.scope.length === 0) failures.push(`${plan.planId}: missing bounded scope`);
  if (!Array.isArray(plan.evidence) || plan.evidence.length === 0) failures.push(`${plan.planId}: missing supporting evidence`);
  if (!Array.isArray(plan.sequence) || plan.sequence.length === 0) failures.push(`${plan.planId}: missing sequence`);
  if (!Array.isArray(plan.prerequisites)) failures.push(`${plan.planId}: missing prerequisites array`);
  if (!Array.isArray(plan.risks)) failures.push(`${plan.planId}: missing risks array`);
  if (!Array.isArray(plan.unresolvedQuestions)) failures.push(`${plan.planId}: missing unresolved questions array`);
  if (!Array.isArray(plan.approvalRequirements) || plan.approvalRequirements.length === 0) failures.push(`${plan.planId}: missing approval requirements`);
  if (!Array.isArray(plan.rejectionPath) || plan.rejectionPath.length === 0) failures.push(`${plan.planId}: missing rejection path`);
  if (!Array.isArray(plan.rollbackGuidance) || plan.rollbackGuidance.length === 0) failures.push(`${plan.planId}: missing rollback guidance`);
  if (!Array.isArray(plan.minorityFindings)) failures.push(`${plan.planId}: missing minority findings array`);
  if (plan.status === 'blocked' && plan.prerequisites.length === 0 && plan.unresolvedQuestions.length === 0) failures.push(`${plan.planId}: blocked plan must explain its blocker`);
  if (plan.status === 'owner-decision-required' && !plan.approvalRequirements.some(value => String(value).toLowerCase().includes('owner'))) failures.push(`${plan.planId}: owner decision status requires explicit owner approval`);
}
if (!artifact.authority?.proposalOnly || artifact.authority?.canonicalMutationAllowed || artifact.authority?.approvalGranted || artifact.authority?.executionAllowed) failures.push('unsafe authority declaration');
if ((artifact.diagnostics?.unsupportedExecutionClaims || []).length > 0) failures.push('unsupported execution claims present');
if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log(`Validated ${artifact.plans.length} meaningful safe plans.`);
