import fs from 'node:fs';

const artifactPath = process.argv[2] || 'governance/development-brain/review-packages/AIOC_AUTOMATED_REVIEW_PACKAGES.generated.json';
const artifact = JSON.parse(fs.readFileSync(artifactPath, 'utf8'));
const allowed = new Set(['supported-risk', 'possible-risk', 'insufficient-evidence', 'no-known-regression']);
const failures = [];
if (artifact.format !== 'multiversal-aioc-automated-review-package') failures.push('invalid format');
if (!Array.isArray(artifact.packages) || artifact.packages.length === 0) failures.push('packages must contain at least one meaningful review package');
for (const item of artifact.packages || []) {
  if (!item.packageId || !item.sourcePlanId) failures.push('package must preserve stable package and source plan identities');
  if (!Array.isArray(item.scope) || item.scope.length === 0) failures.push(`${item.packageId}: missing bounded scope`);
  if (!Array.isArray(item.evidence) || item.evidence.length === 0) failures.push(`${item.packageId}: missing evidence`);
  if (!Array.isArray(item.regressionPredictions) || item.regressionPredictions.length === 0) failures.push(`${item.packageId}: missing regression predictions`);
  for (const risk of item.regressionPredictions || []) {
    if (!allowed.has(risk.classification)) failures.push(`${risk.predictionId}: invalid regression classification`);
    if (risk.confirmedDefect !== false) failures.push(`${risk.predictionId}: prediction must not claim confirmed defect`);
    if (!Array.isArray(risk.assumptions) || risk.assumptions.length === 0) failures.push(`${risk.predictionId}: missing assumptions`);
  }
  if (!Array.isArray(item.validationChecks) || item.validationChecks.length === 0) failures.push(`${item.packageId}: missing validation checks`);
  if (!Array.isArray(item.rollbackReview) || item.rollbackReview.length === 0) failures.push(`${item.packageId}: missing rollback review`);
  if (!Array.isArray(item.approvalGates) || item.approvalGates.length === 0) failures.push(`${item.packageId}: missing approval gates`);
  if (!Array.isArray(item.rejectionConditions) || item.rejectionConditions.length === 0) failures.push(`${item.packageId}: missing rejection conditions`);
  if (!item.freshness?.sourceFingerprint) failures.push(`${item.packageId}: missing freshness fingerprint`);
}
if (!artifact.authority?.advisoryOnly || artifact.authority?.executionAllowed || artifact.authority?.approvalGranted || artifact.authority?.canonicalMutationAllowed || artifact.authority?.mergeAllowed) failures.push('unsafe authority declaration');
if ((artifact.diagnostics?.confirmedDefectClaims || []).length > 0) failures.push('confirmed defect claims present');
if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log(`Validated ${artifact.packages.length} meaningful automated review packages.`);
