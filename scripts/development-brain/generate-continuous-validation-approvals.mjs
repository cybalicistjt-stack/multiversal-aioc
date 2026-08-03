import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const packagePath = process.argv[2];
const decisionsPath = process.argv[3];
const outputPath = process.argv[4];
if (!packagePath || !decisionsPath || !outputPath) throw new Error('usage: node generate-continuous-validation-approvals.mjs <packages> <decisions> <output>');
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const hash = value => crypto.createHash('sha256').update(String(value)).digest('hex');
const packagesArtifact = JSON.parse(fs.readFileSync(resolvePath(packagePath), 'utf8'));
const decisionsArtifact = JSON.parse(fs.readFileSync(resolvePath(decisionsPath), 'utf8'));
const decisions = new Map((decisionsArtifact.decisions || []).map(item => [item.packageId, item]));
const timestamp = '2026-08-03T00:00:00.000Z';

const gates = (packagesArtifact.packages || []).map((pkg, index) => {
  const packageFingerprint = hash(JSON.stringify(pkg));
  const decision = decisions.get(pkg.packageId) || null;
  let status = 'awaiting-owner-approval';
  const invalidationReasons = [];
  if (decision?.action === 'reject') status = 'rejected';
  else if (decision?.action === 'block') status = 'blocked';
  else if (decision?.action === 'approve') {
    if (decision.packageFingerprint === packageFingerprint && decision.actorType === 'human-owner') status = 'approved-validation-ready';
    else {
      status = 'approved-stale';
      if (decision.packageFingerprint !== packageFingerprint) invalidationReasons.push('approval fingerprint does not match current package');
      if (decision.actorType !== 'human-owner') invalidationReasons.push('approval actor is not the human owner');
    }
  }
  return {
    gateId: `APPROVAL-GATE-${String(index + 1).padStart(4, '0')}`,
    packageId: pkg.packageId,
    status,
    packageFingerprint,
    requiredApprovals: ['human-owner'],
    validationChecks: pkg.validationChecks || [],
    decision: decision ? { decisionId: decision.decisionId, action: decision.action, actor: decision.actor, actorType: decision.actorType, reason: decision.reason || '', packageFingerprint: decision.packageFingerprint || '' } : null,
    executionEligibility: status === 'approved-validation-ready' ? 'validation-only' : 'none',
    invalidationReasons
  };
});

const auditTrail = gates.map(gate => ({
  auditId: `AUDIT-${gate.gateId}`,
  timestamp,
  packageId: gate.packageId,
  action: gate.decision?.action || 'awaiting-decision',
  actor: gate.decision?.actor || 'system',
  actorType: gate.decision?.actorType || 'system',
  packageFingerprint: gate.packageFingerprint,
  resultingStatus: gate.status,
  reason: gate.decision?.reason || 'No explicit human decision recorded.'
}));

const artifact = {
  format: 'multiversal-aioc-continuous-validation-approval',
  version: '1.0.0',
  generatedAt: timestamp,
  sourceFingerprint: hash(JSON.stringify(packagesArtifact)),
  gates,
  auditTrail,
  diagnostics: {
    pending: gates.filter(item => item.status === 'awaiting-owner-approval').map(item => item.gateId),
    staleApprovals: gates.filter(item => item.status === 'approved-stale').map(item => item.gateId),
    rejected: gates.filter(item => item.status === 'rejected').map(item => item.gateId),
    blocked: gates.filter(item => item.status === 'blocked').map(item => item.gateId)
  },
  authority: { proposalOnly: true, executionAllowed: false, canonicalMutationAllowed: false, approvalMayBeInferred: false, mergeAllowed: false }
};
fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(artifact, null, 2)}\n`);
console.log(`Generated ${gates.length} continuous validation approval gates at ${outputPath}`);
