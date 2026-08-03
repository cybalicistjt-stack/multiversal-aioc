import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const inputPath = process.argv[2] || 'governance/development-brain/multi-agent-review/AIOC_MULTI_AGENT_REVIEW.generated.json';
const resolved = path.isAbsolute(inputPath) ? inputPath : path.join(root, inputPath);
const artifact = JSON.parse(fs.readFileSync(resolved, 'utf8'));
const allowedOutcomes = new Set(['consensus', 'supported-disagreement', 'unresolved-conflict', 'minority-finding', 'blocked-review', 'owner-decision-required']);
const allowedAuthority = new Set(['read-only', 'advisory', 'proposal-only']);
const errors = [];

if (artifact.format !== 'multiversal-aioc-multi-agent-review') errors.push('Invalid format.');
if (!artifact.sourceFingerprint) errors.push('Missing source fingerprint.');
if (!Array.isArray(artifact.panels)) errors.push('Panels must be an array.');
const panelIds = new Set();
for (const [index, panel] of (artifact.panels || []).entries()) {
  if (!panel.panelId || panelIds.has(panel.panelId)) errors.push(`Invalid or duplicate panelId at ${index}.`);
  panelIds.add(panel.panelId);
  if (!allowedOutcomes.has(panel.outcome)) errors.push(`Invalid outcome for ${panel.panelId}.`);
  if (!allowedAuthority.has(panel.authorityMode)) errors.push(`Invalid authority for ${panel.panelId}.`);
  if (!Array.isArray(panel.reviewerRoleIds) || panel.reviewerRoleIds.length < 2) errors.push(`Panel ${panel.panelId} requires at least two reviewers.`);
  if (!Array.isArray(panel.contributions) || panel.contributions.length < 2) errors.push(`Panel ${panel.panelId} requires at least two contributions.`);
  const contributionIds = new Set();
  for (const contribution of panel.contributions || []) {
    if (!contribution.contributionId || contributionIds.has(contribution.contributionId)) errors.push(`Duplicate contribution in ${panel.panelId}.`);
    contributionIds.add(contribution.contributionId);
    if (!panel.reviewerRoleIds.includes(contribution.roleId)) errors.push(`Contribution role outside panel scope in ${panel.panelId}.`);
    if (!Array.isArray(contribution.evidence) || !contribution.evidence.length) errors.push(`Missing evidence in ${contribution.contributionId}.`);
  }
  if (panel.outcome === 'supported-disagreement' && !(panel.minorityPositions || []).length) errors.push(`Supported disagreement lacks minority position in ${panel.panelId}.`);
  if (!Array.isArray(panel.evidence) || !panel.evidence.length) errors.push(`Missing panel evidence in ${panel.panelId}.`);
}
if (!artifact.authority?.advisoryOnly || artifact.authority?.canonicalMutationAllowed || artifact.authority?.approvalGranted || artifact.authority?.certificationAllowed) {
  errors.push('Authority safeguards are invalid.');
}
if ((artifact.diagnostics?.fabricatedConsensus || []).length) errors.push('Fabricated consensus diagnostic is non-empty.');
if (errors.length) {
  console.error(errors.join('\n'));
  process.exit(1);
}
console.log(`Validated ${artifact.panels.length} multi-agent review panels.`);
