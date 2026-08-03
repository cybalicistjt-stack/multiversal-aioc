import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root = process.cwd();
const fixture = path.join(root, 'governance/development-brain/acceptance/fixtures/step19-review-corpus.json');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'aioc-step19-'));
const output = path.join(tempDir, 'safe-plans.json');

const run = (args, expectedStatus = 0) => {
  const result = spawnSync(process.execPath, args, { cwd: root, encoding: 'utf8' });
  assert.equal(result.status, expectedStatus, `Command failed: node ${args.join(' ')}\nSTDOUT:\n${result.stdout}\nSTDERR:\n${result.stderr}`);
  return result;
};

run(['scripts/development-brain/generate-safe-plan-proposals.mjs', fixture, output]);
run(['scripts/development-brain/validate-safe-plan-proposals.mjs', output]);

const artifact = JSON.parse(fs.readFileSync(output, 'utf8'));
assert.equal(artifact.plans.length, 5, 'acceptance corpus must produce five plans');

const byReview = new Map(artifact.plans.map(plan => [plan.sourceReviewId, plan]));
assert.equal(byReview.get('REVIEW-ACCEPT-0001')?.status, 'later-executable-after-approval');
assert.equal(byReview.get('REVIEW-ACCEPT-0002')?.status, 'proposal-only');
assert.equal(byReview.get('REVIEW-ACCEPT-0003')?.status, 'owner-decision-required');
assert.equal(byReview.get('REVIEW-ACCEPT-0004')?.status, 'blocked');
assert.equal(byReview.get('REVIEW-ACCEPT-0005')?.status, 'owner-decision-required');
assert.equal(byReview.get('REVIEW-ACCEPT-0002')?.minorityFindings.length, 1, 'minority finding must survive planning');
assert.ok(byReview.get('REVIEW-ACCEPT-0003')?.unresolvedQuestions.length > 0, 'conflict questions must survive planning');
assert.ok(byReview.get('REVIEW-ACCEPT-0004')?.prerequisites.includes('Mac access'), 'blocked prerequisites must survive planning');
assert.deepEqual(artifact.authority, {
  proposalOnly: true,
  canonicalMutationAllowed: false,
  approvalGranted: false,
  executionAllowed: false
});

const emptyArtifact = { ...artifact, plans: [] };
const emptyPath = path.join(tempDir, 'empty.json');
fs.writeFileSync(emptyPath, `${JSON.stringify(emptyArtifact, null, 2)}\n`);
run(['scripts/development-brain/validate-safe-plan-proposals.mjs', emptyPath], 1);

const unsafeArtifact = {
  ...artifact,
  authority: { ...artifact.authority, executionAllowed: true }
};
const unsafePath = path.join(tempDir, 'unsafe.json');
fs.writeFileSync(unsafePath, `${JSON.stringify(unsafeArtifact, null, 2)}\n`);
run(['scripts/development-brain/validate-safe-plan-proposals.mjs', unsafePath], 1);

console.log('Step 19 acceptance corpus passed: populated outcomes, dissent preservation, blocking, owner decision, and authority rejection verified.');
