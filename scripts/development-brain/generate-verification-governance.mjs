import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const inventoryPath = process.argv[2] || 'tmp/AIOC_UNIFIED_INVENTORY.json';
const readinessPath = process.argv[3] || 'tmp/AIOC_COMPLETION_READINESS.json';
const plannerPath = process.argv[4] || 'tmp/AIOC_RECOMMENDATION_PLANNER.json';
const outputPath = process.argv[5] || 'governance/development-brain/verification-governance/AIOC_VERIFICATION_GOVERNANCE.generated.json';

function ensure(file, command, args) {
  if (!fs.existsSync(resolvePath(file))) execFileSync(process.execPath, [command, ...args], { cwd: root, stdio: 'inherit' });
}
ensure(inventoryPath, 'scripts/development-brain/generate-unified-inventory.mjs', [inventoryPath]);
ensure(readinessPath, 'scripts/development-brain/generate-completion-readiness.mjs', ['tmp/AIOC_UNIFIED_INVENTORY.json', 'tmp/AIOC_DEPENDENCY_GRAPH.json', 'tmp/AIOC_STRUCTURE_INTELLIGENCE.json', readinessPath]);
ensure(plannerPath, 'scripts/development-brain/generate-recommendation-planner.mjs', ['tmp/AIOC_UNIFIED_INVENTORY.json', 'tmp/AIOC_DEPENDENCY_GRAPH.json', 'tmp/AIOC_STRUCTURE_INTELLIGENCE.json', readinessPath, 'tmp/AIOC_PRIORITY_IMPACT.json', plannerPath]);

const inventory = JSON.parse(fs.readFileSync(resolvePath(inventoryPath), 'utf8'));
const readiness = JSON.parse(fs.readFileSync(resolvePath(readinessPath), 'utf8'));
const planner = JSON.parse(fs.readFileSync(resolvePath(plannerPath), 'utf8'));
const inventoryById = new Map((inventory.objects || []).map(item => [item.stableId, item]));
const readinessById = new Map((readiness.objects || []).map(item => [item.stableId, item]));

const verifications = (planner.recommendations || []).map(rec => {
  const object = inventoryById.get(rec.stableId) || {};
  const ready = readinessById.get(rec.stableId) || {};
  const checks = [
    { code: 'EVIDENCE_SUFFICIENT', passed: Array.isArray(rec.evidence) && rec.evidence.length >= 3, detail: `${rec.evidence?.length || 0} recommendation evidence record(s).` },
    { code: 'PREREQUISITES_SATISFIED', passed: (rec.prerequisites || []).every(item => item.satisfied === true), detail: `${(rec.prerequisites || []).filter(item => !item.satisfied).length} unsatisfied prerequisite(s).` },
    { code: 'LIFECYCLE_COMPATIBLE', passed: rec.classification !== 'executable' || ['development', 'validation', 'review', 'game-ready'].includes(object.lifecycle), detail: `Lifecycle is ${object.lifecycle || 'unknown'}.` },
    { code: 'AUTHORITY_COMPATIBLE', passed: rec.classification !== 'executable' || object.authorityLayer !== 'canonical', detail: `Authority layer is ${object.authorityLayer || 'unknown'}.` },
    { code: 'TASK_ELIGIBILITY', passed: rec.classification === 'executable' ? (rec.tasks || []).every(task => task.executionAllowed === true) : (rec.tasks || []).every(task => task.executionAllowed === false), detail: `${(rec.tasks || []).length} task proposal(s) checked.` },
    { code: 'READINESS_COMPATIBLE', passed: rec.classification !== 'executable' || !['blocked'].includes(ready.status), detail: `Readiness status is ${ready.status || 'unknown'}.` }
  ];
  const needsApproval = rec.classification === 'owner-decision' || object.authorityLayer === 'canonical' || (rec.prerequisites || []).some(item => item.authorityRequired);
  let status = 'verified-executable';
  if (rec.classification === 'observation-only') status = 'observation-only';
  else if (needsApproval) status = 'requires-approval';
  else if (rec.classification === 'blocked' || checks.some(check => !check.passed)) status = 'blocked';
  return {
    verificationId: `VERIFY-${rec.stableId}`,
    recommendationId: rec.recommendationId,
    stableId: rec.stableId,
    rank: rec.rank,
    sourceClassification: rec.classification,
    status,
    checks,
    approval: {
      required: needsApproval,
      authority: needsApproval ? (object.authorityLayer === 'canonical' ? 'owner-or-governance' : 'owner') : 'normal-governed-review',
      granted: false,
      note: needsApproval ? 'Explicit approval is required; this record does not infer or grant it.' : 'Normal repository review and validation remain required.'
    },
    evidence: [
      { sourcePath: plannerPath, pointer: rec.recommendationId, claim: 'Recommendation classification, prerequisites, tasks, and evidence basis.' },
      { sourcePath: readinessPath, pointer: ready.readinessId || rec.stableId, claim: 'Readiness status and blocker basis.' },
      { sourcePath: inventoryPath, pointer: rec.stableId, claim: 'Lifecycle and authority compatibility basis.' }
    ],
    advisory: true
  };
}).sort((a, b) => a.rank - b.rank || a.stableId.localeCompare(b.stableId));

const count = status => verifications.filter(item => item.status === status).length;
const result = {
  format: 'multiversal-aioc-verification-governance',
  version: '1.0.0',
  generatedAt: new Date().toISOString(),
  sources: { inventory: inventoryPath, completionReadiness: readinessPath, recommendationPlanner: plannerPath },
  policy: {
    verificationRule: 'Every recommendation is checked for evidence, prerequisites, lifecycle, authority, task eligibility, readiness, and approval requirements.',
    authorityRule: 'Verification records are advisory and never execute, assign, schedule, mutate, promote, certify, or substitute owner decisions.',
    executionRule: 'Verified-executable means checks passed; normal governed repository approval and validation remain mandatory.'
  },
  summary: {
    total: verifications.length,
    verifiedExecutable: count('verified-executable'),
    requiresApproval: count('requires-approval'),
    blocked: count('blocked'),
    observationOnly: count('observation-only')
  },
  verifications
};
fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(result, null, 2)}\n`);
console.log(`Generated ${verifications.length} verification records at ${outputPath}.`);
