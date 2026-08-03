import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const planPath = process.argv[2] || 'governance/development-brain/safe-plans/AIOC_SAFE_PLAN_PROPOSALS.generated.json';
const outputPath = process.argv[3] || 'governance/development-brain/review-packages/AIOC_AUTOMATED_REVIEW_PACKAGES.generated.json';
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const hash = value => crypto.createHash('sha256').update(String(value)).digest('hex');
const plansArtifact = JSON.parse(fs.readFileSync(resolvePath(planPath), 'utf8'));

const classifyRisks = plan => {
  const predictions = [];
  for (const [index, risk] of (plan.risks || []).entries()) {
    predictions.push({
      predictionId: `${plan.planId}-RISK-${String(index + 1).padStart(2, '0')}`,
      classification: (plan.evidence || []).length > 0 ? 'supported-risk' : 'insufficient-evidence',
      statement: String(risk),
      evidence: plan.evidence || [],
      assumptions: ['Risk statement originates from the governed source plan.'],
      confidence: plan.confidence || 'medium',
      confirmedDefect: false
    });
  }
  if (predictions.length === 0) {
    predictions.push({
      predictionId: `${plan.planId}-RISK-00`,
      classification: 'no-known-regression',
      statement: 'No regression is identified by the current governed evidence.',
      evidence: plan.evidence || [],
      assumptions: ['Absence of a known regression is not proof that no regression exists.'],
      confidence: 'low',
      confirmedDefect: false
    });
  }
  return predictions;
};

const packages = (plansArtifact.plans || []).map((plan, index) => ({
  packageId: `REVIEW-PACKAGE-${String(index + 1).padStart(4, '0')}`,
  sourcePlanId: plan.planId,
  summary: `Governed review package for ${plan.sourceReviewId}.`,
  scope: plan.scope || [],
  evidence: plan.evidence || [],
  affectedDomains: [...new Set(plan.scope || [])],
  regressionPredictions: classifyRisks(plan),
  assumptions: ['All source-plan evidence remains current until freshness is revalidated.'],
  unresolvedQuestions: plan.unresolvedQuestions || [],
  minorityFindings: plan.minorityFindings || [],
  validationChecks: [
    'Revalidate source fingerprint and evidence availability.',
    'Run affected repository tests and validators.',
    'Confirm authority and approval requirements remain satisfied.'
  ],
  rollbackReview: plan.rollbackGuidance || [],
  approvalGates: plan.approvalRequirements || [],
  rejectionConditions: [
    'Reject when required evidence is missing or stale.',
    'Reject when an approval requirement is unsatisfied.',
    'Reject when execution authority is asserted by this package.'
  ],
  confidence: plan.confidence || 'medium',
  freshness: { sourceFingerprint: plansArtifact.sourceFingerprint, status: 'current-at-generation' }
}));

const artifact = {
  format: 'multiversal-aioc-automated-review-package',
  version: '1.0.0',
  generatedAt: '2026-08-03T00:00:00.000Z',
  sourceFingerprint: hash(JSON.stringify(plansArtifact)),
  packages,
  diagnostics: {
    missingEvidence: packages.filter(item => item.evidence.length === 0).map(item => item.packageId),
    missingRollbackReview: packages.filter(item => item.rollbackReview.length === 0).map(item => item.packageId),
    missingApprovalGates: packages.filter(item => item.approvalGates.length === 0).map(item => item.packageId),
    confirmedDefectClaims: packages.flatMap(item => item.regressionPredictions.filter(risk => risk.confirmedDefect).map(risk => risk.predictionId))
  },
  authority: { advisoryOnly: true, executionAllowed: false, approvalGranted: false, canonicalMutationAllowed: false, mergeAllowed: false }
};

fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(artifact, null, 2)}\n`);
console.log(`Generated ${packages.length} automated review packages at ${outputPath}`);
