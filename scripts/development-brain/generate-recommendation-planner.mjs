import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const inventoryPath = process.argv[2] || 'tmp/AIOC_UNIFIED_INVENTORY.json';
const graphPath = process.argv[3] || 'tmp/AIOC_DEPENDENCY_GRAPH.json';
const structurePath = process.argv[4] || 'tmp/AIOC_STRUCTURE_INTELLIGENCE.json';
const readinessPath = process.argv[5] || 'tmp/AIOC_COMPLETION_READINESS.json';
const priorityPath = process.argv[6] || 'tmp/AIOC_PRIORITY_IMPACT.json';
const outputPath = process.argv[7] || 'governance/development-brain/recommendation-planner/AIOC_RECOMMENDATION_PLANNER.generated.json';

function ensure(file, command, args) {
  if (!fs.existsSync(resolvePath(file))) execFileSync(process.execPath, [command, ...args], { cwd: root, stdio: 'inherit' });
}
ensure(inventoryPath, 'scripts/development-brain/generate-unified-inventory.mjs', [inventoryPath]);
ensure(graphPath, 'scripts/development-brain/generate-dependency-graph.mjs', [inventoryPath, graphPath]);
ensure(structurePath, 'scripts/development-brain/generate-structure-intelligence.mjs', [inventoryPath, graphPath, structurePath]);
ensure(readinessPath, 'scripts/development-brain/generate-completion-readiness.mjs', [inventoryPath, graphPath, structurePath, readinessPath]);
ensure(priorityPath, 'scripts/development-brain/generate-priority-impact.mjs', [inventoryPath, graphPath, structurePath, readinessPath, priorityPath]);

const inventory = JSON.parse(fs.readFileSync(resolvePath(inventoryPath), 'utf8'));
const readiness = JSON.parse(fs.readFileSync(resolvePath(readinessPath), 'utf8'));
const priorities = JSON.parse(fs.readFileSync(resolvePath(priorityPath), 'utf8'));
const inventoryById = new Map((inventory.objects || []).map(item => [item.stableId, item]));
const readinessById = new Map((readiness.objects || []).map(item => [item.stableId, item]));

const recommendations = (priorities.priorities || []).map(priority => {
  const object = inventoryById.get(priority.stableId) || {};
  const ready = readinessById.get(priority.stableId) || {};
  const criticalBlockers = (ready.blockers || []).filter(item => item.severity === 'critical');
  const requiresOwner = criticalBlockers.some(item => ['GOVERNANCE_STAGE', 'STRUCTURE_UNRESOLVED'].includes(item.code)) || object.authorityLayer === 'canonical';
  let classification = 'executable';
  if (criticalBlockers.length) classification = requiresOwner ? 'owner-decision' : 'blocked';
  else if (priority.tier === 'low' && ready.status === 'ready') classification = 'observation-only';

  const prerequisites = (ready.blockers || []).map((blocker, index) => ({
    prerequisiteId: `PRE-${priority.stableId}-${String(index + 1).padStart(2, '0')}`,
    code: blocker.code,
    description: blocker.message,
    satisfied: false,
    authorityRequired: blocker.code === 'GOVERNANCE_STAGE' || blocker.code === 'STRUCTURE_UNRESOLVED'
  }));

  const tasks = [];
  if (classification === 'executable') {
    tasks.push(
      { taskId: `TASK-${priority.stableId}-01`, sequence: 1, action: 'Review the cited readiness deficits and source evidence.', boundedOutcome: 'A verified list of required corrections or confirmations.', executionAllowed: true },
      { taskId: `TASK-${priority.stableId}-02`, sequence: 2, action: 'Prepare the smallest source change that addresses the verified deficit without altering unrelated content.', boundedOutcome: 'A reviewable bounded change proposal.', executionAllowed: true },
      { taskId: `TASK-${priority.stableId}-03`, sequence: 3, action: 'Run the applicable validators and preserve resulting evidence.', boundedOutcome: 'Validation evidence attached to the proposed change.', executionAllowed: true }
    );
  } else if (classification === 'owner-decision') {
    tasks.push({ taskId: `TASK-${priority.stableId}-01`, sequence: 1, action: 'Present the decision, supported options, consequences, and cited evidence to the owner.', boundedOutcome: 'An explicit owner decision or deferral.', executionAllowed: false });
  } else if (classification === 'blocked') {
    tasks.push({ taskId: `TASK-${priority.stableId}-01`, sequence: 1, action: 'Resolve or externally satisfy all listed prerequisites before implementation.', boundedOutcome: 'The recommendation can be reclassified after regeneration.', executionAllowed: false });
  } else {
    tasks.push({ taskId: `TASK-${priority.stableId}-01`, sequence: 1, action: 'Retain as an observation and reassess when upstream evidence changes.', boundedOutcome: 'No source mutation.', executionAllowed: false });
  }

  return {
    recommendationId: `REC-${priority.stableId}`,
    stableId: priority.stableId,
    rank: priority.rank,
    priorityScore: priority.score,
    priorityTier: priority.tier,
    classification,
    title: `${classification.replaceAll('-', ' ')} recommendation for ${priority.name || priority.stableId}`,
    rationale: [
      `Priority score ${priority.score} (${priority.tier}) was generated by the validated Priority and Impact Engine.`,
      `Readiness status is ${ready.status || 'unknown'} with ${(ready.blockers || []).length} blocker(s).`,
      `Classification is ${classification}; this classification does not authorize mutation, assignment, scheduling, promotion, or certification.`
    ],
    prerequisites,
    tasks,
    evidence: [
      { sourcePath: priorityPath, pointer: priority.priorityId, claim: 'Priority rank, score, component, and unlock-value basis.' },
      { sourcePath: readinessPath, pointer: ready.readinessId || priority.stableId, claim: 'Readiness status, blockers, and promotion-readiness basis.' },
      { sourcePath: inventoryPath, pointer: priority.stableId, claim: 'Object authority, lifecycle, and provenance basis.' }
    ],
    advisory: true
  };
}).sort((a, b) => a.rank - b.rank || a.stableId.localeCompare(b.stableId));

const count = classification => recommendations.filter(item => item.classification === classification).length;
const result = {
  format: 'multiversal-aioc-recommendation-planner',
  version: '1.0.0',
  generatedAt: new Date().toISOString(),
  sources: { inventory: inventoryPath, dependencyGraph: graphPath, structureIntelligence: structurePath, completionReadiness: readinessPath, priorityImpact: priorityPath },
  policy: {
    classificationRule: 'Recommendations are classified as executable, owner-decision, blocked, or observation-only from validated readiness and priority evidence.',
    authorityRule: 'Recommendations and tasks are advisory; they never assign, schedule, mutate, promote, certify, or override owner or governance authority.',
    executionRule: 'Only tasks with executionAllowed true may be proposed for governed execution, and still require the normal repository approval and validation process.'
  },
  summary: {
    totalRecommendations: recommendations.length,
    executable: count('executable'),
    ownerDecision: count('owner-decision'),
    blocked: count('blocked'),
    observationOnly: count('observation-only')
  },
  recommendations
};
fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(result, null, 2)}\n`);
console.log(`Generated ${recommendations.length} recommendation records at ${outputPath}.`);
