import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import crypto from 'node:crypto';
import { spawnSync } from 'node:child_process';

const root = process.cwd();
const temp = fs.mkdtempSync(path.join(os.tmpdir(), 'aioc-step21-'));
const plans = path.join(temp, 'plans.json');
const packages = path.join(temp, 'packages.json');
const decisions = path.join(temp, 'decisions.json');
const gates = path.join(temp, 'gates.json');
const run = (args, expected = 0) => { const r = spawnSync(process.execPath, args, { cwd: root, encoding: 'utf8' }); assert.equal(r.status, expected, `node ${args.join(' ')}\n${r.stdout}\n${r.stderr}`); };
const hash = value => crypto.createHash('sha256').update(String(value)).digest('hex');
run(['scripts/development-brain/generate-safe-plan-proposals.mjs', 'governance/development-brain/acceptance/fixtures/step19-review-corpus.json', plans]);
run(['scripts/development-brain/generate-automated-review-packages.mjs', plans, packages]);
const packageArtifact = JSON.parse(fs.readFileSync(packages, 'utf8'));
const [a,b,c,d,e] = packageArtifact.packages;
fs.writeFileSync(decisions, JSON.stringify({ decisions: [
  { decisionId: 'DEC-1', packageId: a.packageId, action: 'approve', actor: 'John Brandon Turner', actorType: 'human-owner', packageFingerprint: hash(JSON.stringify(a)), reason: 'Approved for validation.' },
  { decisionId: 'DEC-2', packageId: b.packageId, action: 'reject', actor: 'John Brandon Turner', actorType: 'human-owner', packageFingerprint: hash(JSON.stringify(b)), reason: 'Design conflict unresolved.' },
  { decisionId: 'DEC-3', packageId: c.packageId, action: 'approve', actor: 'John Brandon Turner', actorType: 'human-owner', packageFingerprint: 'stale-fingerprint', reason: 'Old approval.' },
  { decisionId: 'DEC-5', packageId: e.packageId, action: 'block', actor: 'John Brandon Turner', actorType: 'human-owner', packageFingerprint: hash(JSON.stringify(e)), reason: 'Prerequisite not available.' }
] }, null, 2));
run(['scripts/development-brain/generate-continuous-validation-approvals.mjs', packages, decisions, gates]);
run(['scripts/development-brain/validate-continuous-validation-approvals.mjs', gates]);
const artifact = JSON.parse(fs.readFileSync(gates, 'utf8'));
assert.equal(artifact.gates.length, 5);
assert.deepEqual(artifact.gates.map(item => item.status), ['approved-validation-ready','rejected','approved-stale','awaiting-owner-approval','blocked']);
assert.equal(artifact.gates[0].executionEligibility, 'validation-only');
assert.ok(artifact.gates[2].invalidationReasons.length > 0);
assert.equal(artifact.auditTrail.length, 5);
assert.deepEqual(artifact.authority, { proposalOnly: true, executionAllowed: false, canonicalMutationAllowed: false, approvalMayBeInferred: false, mergeAllowed: false });
const unsafe = { ...artifact, authority: { ...artifact.authority, executionAllowed: true } };
const unsafePath = path.join(temp, 'unsafe.json'); fs.writeFileSync(unsafePath, JSON.stringify(unsafe));
run(['scripts/development-brain/validate-continuous-validation-approvals.mjs', unsafePath], 1);
const forged = structuredClone(artifact); forged.gates[0].decision.actorType = 'ai-agent';
const forgedPath = path.join(temp, 'forged.json'); fs.writeFileSync(forgedPath, JSON.stringify(forged));
run(['scripts/development-brain/validate-continuous-validation-approvals.mjs', forgedPath], 1);
console.log('Step 21 acceptance passed: exact approval, rejection, staleness, pending, blocking, audit, and authority denial verified.');
