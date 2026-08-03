import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const reviewPath = process.argv[2] || 'governance/development-brain/multi-agent-review/AIOC_MULTI_AGENT_REVIEW.generated.json';
const outputPath = process.argv[3] || 'governance/development-brain/safe-plans/AIOC_SAFE_PLAN_PROPOSALS.generated.json';
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const hash = value => crypto.createHash('sha256').update(String(value)).digest('hex');
const readJson = value => JSON.parse(fs.readFileSync(resolvePath(value), 'utf8'));

const review = readJson(reviewPath);
const statusMap = {
  'consensus': 'later-executable-after-approval',
  'supported-disagreement': 'proposal-only',
  'unresolved-conflict': 'owner-decision-required',
  'minority-finding': 'proposal-only',
  'blocked-review': 'blocked',
  'owner-decision-required': 'owner-decision-required'
};

const panels = review.reviewPanels || review.reviews || [];
const plans = panels.map((panel, index) => {
  const outcome = panel.outcome || panel.classification || 'blocked-review';
  const contributions = panel.contributions || [];
  const evidence = [...new Set(contributions.flatMap(item => item.evidence || []))];
  const unresolved = [...new Set(contributions.flatMap(item => item.unresolvedQuestions || []))];
  const minority = contributions.filter(item => item.minority === true || item.position === 'minority').map(item => ({ contributionId: item.contributionId, position: item.position, evidence: item.evidence || [] }));
  return {
    planId: `SAFE-PLAN-${String(index + 1).padStart(4, '0')}`,
    sourceReviewId: panel.reviewId || panel.panelId || `REVIEW-${index + 1}`,
    status: statusMap[outcome] || 'blocked',
    scope: panel.scope || panel.routedScope || [],
    sequence: [
      { order: 1, action: 'Confirm source freshness and prerequisite availability.', authority: 'read-only' },
      { order: 2, action: 'Prepare bounded proposal package for governed review.', authority: 'proposal-only' },
      { order: 3, action: 'Obtain all required owner and governance approvals before any execution.', authority: 'approval-required' }
    ],
    prerequisites: panel.prerequisites || [],
    risks: panel.risks || (outcome === 'consensus' ? [] : ['Review outcome is not full consensus.']),
    unresolvedQuestions: unresolved,
    evidence,
    confidence: panel.confidence || 'medium',
    authorityRequirements: ['Repository review', 'CI validation', 'Authority compatibility check'],
    approvalRequirements: outcome === 'consensus' ? ['Owner or delegated governed approval before execution'] : ['Owner decision', 'Governance review'],
    rejectionPath: ['Reject proposal without mutating canonical content.', 'Record rejection rationale and evidence.', 'Return unresolved items to governed review.'],
    rollbackGuidance: ['No automatic rollback is authorized.', 'Any approved implementation must define repository-specific rollback steps before execution.'],
    minorityFindings: minority
  };
});

const artifact = {
  format: 'multiversal-aioc-safe-plan-proposal',
  version: '1.0.0',
  generatedAt: '2026-08-03T00:00:00.000Z',
  sourceFingerprint: hash(JSON.stringify(review)),
  plans,
  diagnostics: {
    missingEvidence: plans.filter(plan => plan.evidence.length === 0).map(plan => plan.planId),
    unresolvedOwnerDecisions: plans.filter(plan => plan.status === 'owner-decision-required').map(plan => plan.planId),
    blockedPlans: plans.filter(plan => plan.status === 'blocked').map(plan => plan.planId),
    unsupportedExecutionClaims: []
  },
  authority: { proposalOnly: true, canonicalMutationAllowed: false, approvalGranted: false, executionAllowed: false }
};

fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(artifact, null, 2)}\n`);
console.log(`Generated ${plans.length} safe plans at ${outputPath}`);
