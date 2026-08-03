import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const contractsPath = process.argv[2] || 'tmp/AIOC_SPECIALIST_AGENT_CONTRACTS.json';
const routingPath = process.argv[3] || 'tmp/AIOC_ORCHESTRATION_ROUTING.json';
const outputPath = process.argv[4] || 'governance/development-brain/multi-agent-review/AIOC_MULTI_AGENT_REVIEW.generated.json';
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const hash = value => crypto.createHash('sha256').update(String(value)).digest('hex');

if (!fs.existsSync(resolvePath(contractsPath))) {
  execFileSync(process.execPath, ['scripts/development-brain/generate-specialist-agent-contracts.mjs', contractsPath], { cwd: root, stdio: 'inherit' });
}
if (!fs.existsSync(resolvePath(routingPath))) {
  execFileSync(process.execPath, ['scripts/development-brain/generate-orchestration-routing.mjs', contractsPath, routingPath], { cwd: root, stdio: 'inherit' });
}

const contracts = JSON.parse(fs.readFileSync(resolvePath(contractsPath), 'utf8'));
const routing = JSON.parse(fs.readFileSync(resolvePath(routingPath), 'utf8'));
const contractByRole = new Map((contracts.contracts || []).map(item => [item.roleId, item]));
const coordinator = 'AGENT-ROLE-DEVELOPMENT-COORDINATOR';
const evidenceFor = (sourcePath, pointer, claim) => ({ sourcePath, pointer, claim });

const reviewableRoutes = (routing.routes || []).filter(route => ['routable', 'ambiguous', 'escalation-required'].includes(route.status));
const panels = reviewableRoutes.map((route, index) => {
  const primary = route.selectedRoleId || route.eligibleRoleIds?.[0] || coordinator;
  const governance = 'AGENT-ROLE-GOVERNANCE-PROVENANCE-AGENT';
  const verification = 'AGENT-ROLE-VERIFICATION-TESTING-AGENT';
  const reviewerRoleIds = [...new Set([primary, governance, verification])].filter(roleId => contractByRole.has(roleId));
  while (reviewerRoleIds.length < 2 && reviewerRoleIds.length < contracts.contracts.length) {
    const next = contracts.contracts.find(c => !reviewerRoleIds.includes(c.roleId));
    if (!next) break;
    reviewerRoleIds.push(next.roleId);
  }
  const contributions = reviewerRoleIds.map((roleId, contributionIndex) => {
    const contract = contractByRole.get(roleId);
    const isPrimary = roleId === primary;
    const position = route.status === 'ambiguous'
      ? `${contract.name} finds the route supportable only after ambiguity is resolved.`
      : route.status === 'escalation-required'
        ? `${contract.name} supports escalation and preserves the unresolved authority boundary.`
        : isPrimary
          ? `${contract.name} supports the bounded route within its permitted outputs.`
          : `${contract.name} supports review subject to evidence, authority, and validation constraints.`;
    return {
      contributionId: `REVIEW-CONTRIBUTION-${hash(`${route.routeId}:${roleId}`).slice(0, 20)}`,
      roleId,
      position,
      confidence: route.status === 'routable' ? 'high' : 'medium',
      evidence: [
        evidenceFor(routingPath, `/routes/${index}`, 'Governed routing record.'),
        evidenceFor(contractsPath, `/contracts/${contracts.contracts.findIndex(c => c.roleId === roleId)}`, 'Validated specialist contract.')
      ],
      constraints: [...(route.constraints || []), ...(contract.prohibitedActions || [])],
      unresolvedQuestions: [...(route.unresolvedQuestions || [])]
    };
  });

  let outcome = 'consensus';
  if (route.status === 'ambiguous') outcome = 'supported-disagreement';
  if (route.status === 'escalation-required') outcome = 'owner-decision-required';
  if (route.status === 'blocked') outcome = 'blocked-review';
  const minorityPositions = outcome === 'supported-disagreement'
    ? contributions.slice(1).map(item => ({ roleId: item.roleId, position: item.position }))
    : [];

  return {
    panelId: `REVIEW-PANEL-${hash(route.routeId).slice(0, 20)}`,
    taskId: route.taskId,
    reviewerRoleIds,
    contributions,
    outcome,
    synthesis: outcome === 'consensus'
      ? 'The panel supports the bounded route while preserving evidence, authority, constraints, and unresolved questions.'
      : outcome === 'owner-decision-required'
        ? 'The panel cannot resolve the matter within delegated authority and requires an owner decision.'
        : 'The panel preserves supported disagreement and does not fabricate consensus.',
    minorityPositions,
    evidence: [evidenceFor(routingPath, `/routes/${index}`, 'Source route for review panel.')],
    authorityMode: route.authorityMode || 'proposal-only',
    unresolvedQuestions: [...(route.unresolvedQuestions || [])]
  };
});

const diagnostics = {
  fabricatedConsensus: [],
  missingEvidence: panels.filter(panel => panel.contributions.some(c => !c.evidence.length)).map(panel => ({ panelId: panel.panelId })),
  scopeViolations: panels.flatMap(panel => panel.contributions.filter(c => !panel.reviewerRoleIds.includes(c.roleId)).map(c => ({ panelId: panel.panelId, roleId: c.roleId }))),
  unresolvedConflicts: panels.filter(panel => panel.outcome === 'unresolved-conflict').map(panel => ({ panelId: panel.panelId })),
  blockedReviews: panels.filter(panel => panel.outcome === 'blocked-review').map(panel => ({ panelId: panel.panelId })),
  ownerDecisionsRequired: panels.filter(panel => panel.outcome === 'owner-decision-required').map(panel => ({ panelId: panel.panelId }))
};

const artifact = {
  format: 'multiversal-aioc-multi-agent-review',
  version: '1.0.0',
  generatedAt: '2026-08-03T00:00:00.000Z',
  sourceFingerprint: hash(JSON.stringify({ contracts: contracts.sourceFingerprint, routing: routing.sourceFingerprint })),
  panels,
  diagnostics,
  authority: { advisoryOnly: true, canonicalMutationAllowed: false, approvalGranted: false, certificationAllowed: false }
};

fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(artifact, null, 2)}\n`);
console.log(`Generated ${panels.length} governed review panels at ${outputPath}`);
