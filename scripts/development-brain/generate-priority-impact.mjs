import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const inventoryPath = process.argv[2] || 'tmp/AIOC_UNIFIED_INVENTORY.json';
const graphPath = process.argv[3] || 'tmp/AIOC_DEPENDENCY_GRAPH.json';
const structurePath = process.argv[4] || 'tmp/AIOC_STRUCTURE_INTELLIGENCE.json';
const readinessPath = process.argv[5] || 'tmp/AIOC_COMPLETION_READINESS.json';
const outputPath = process.argv[6] || 'governance/development-brain/priority-impact/AIOC_PRIORITY_IMPACT.generated.json';

function ensure(file, command, args) {
  if (!fs.existsSync(resolvePath(file))) execFileSync(process.execPath, [command, ...args], { cwd: root, stdio: 'inherit' });
}
ensure(inventoryPath, 'scripts/development-brain/generate-unified-inventory.mjs', [inventoryPath]);
ensure(graphPath, 'scripts/development-brain/generate-dependency-graph.mjs', [inventoryPath, graphPath]);
ensure(structurePath, 'scripts/development-brain/generate-structure-intelligence.mjs', [inventoryPath, graphPath, structurePath]);
ensure(readinessPath, 'scripts/development-brain/generate-completion-readiness.mjs', [inventoryPath, graphPath, structurePath, readinessPath]);

const inventory = JSON.parse(fs.readFileSync(resolvePath(inventoryPath), 'utf8'));
const graph = JSON.parse(fs.readFileSync(resolvePath(graphPath), 'utf8'));
const structure = JSON.parse(fs.readFileSync(resolvePath(structurePath), 'utf8'));
const readiness = JSON.parse(fs.readFileSync(resolvePath(readinessPath), 'utf8'));
const nodeToStable = new Map((graph.nodes || []).map(node => [node.nodeId, node.stableId || node.nodeId.replace(/^NODE-/, '')]));
const incoming = new Map();
const outgoingBlocks = new Map();
for (const edge of graph.edges || []) {
  const target = nodeToStable.get(edge.target) || edge.target.replace(/^NODE-/, '');
  incoming.set(target, (incoming.get(target) || 0) + 1);
  if (edge.relationship === 'blocks') {
    const source = nodeToStable.get(edge.source) || edge.source.replace(/^NODE-/, '');
    outgoingBlocks.set(source, (outgoingBlocks.get(source) || 0) + 1);
  }
}
const highImpact = new Map((structure.highImpactDependencies || []).map(item => [item.stableId || item.objectStableId, item]));
const governedPriorities = new Set((inventory.objects || []).filter(object => (object.references?.memoryIds || []).length > 0).map(object => object.stableId));
const clamp = value => Math.max(0, Math.min(100, Math.round(value)));

const priorities = (readiness.objects || []).map(item => {
  const readinessDeficit = 100 - item.score;
  const dependencyCentrality = clamp((incoming.get(item.stableId) || 0) * 10);
  const blockerPropagation = clamp((outgoingBlocks.get(item.stableId) || 0) * 20 + item.blockers.filter(blocker => blocker.severity === 'critical').length * 10);
  const structuralImpact = clamp(highImpact.has(item.stableId) ? 80 : item.scores?.structure < 75 ? 55 : 10);
  const evidenceGap = clamp(100 - (item.scores?.evidence ?? 0));
  const governedPriority = governedPriorities.has(item.stableId) ? 80 : 20;
  const unlockValue = clamp(dependencyCentrality * 0.55 + blockerPropagation * 0.45);
  const components = { readinessDeficit, dependencyCentrality, blockerPropagation, structuralImpact, evidenceGap, governedPriority, unlockValue };
  const score = clamp(readinessDeficit * 0.24 + dependencyCentrality * 0.16 + blockerPropagation * 0.18 + structuralImpact * 0.14 + evidenceGap * 0.1 + governedPriority * 0.08 + unlockValue * 0.1);
  const tier = score >= 75 ? 'critical' : score >= 55 ? 'high' : score >= 30 ? 'medium' : 'low';
  const reasons = [
    `Readiness deficit contributes ${readinessDeficit} points before weighting.`,
    `${incoming.get(item.stableId) || 0} incoming dependency relationship(s) and ${outgoingBlocks.get(item.stableId) || 0} propagated blocker(s) were evaluated.`,
    `${item.blockers.length} readiness blocker(s) and an evidence gap of ${evidenceGap} were evaluated.`,
    governedPriorities.has(item.stableId) ? 'The object is referenced by governed project memory.' : 'No direct governed-priority memory reference was found.'
  ];
  return {
    priorityId: `PRIORITY-${item.stableId}`,
    stableId: item.stableId,
    name: item.name,
    objectType: item.objectType,
    authorityLayer: item.authorityLayer,
    readinessStatus: item.status,
    score,
    tier,
    components,
    estimatedUnlockValue: unlockValue,
    reasons,
    evidence: [
      { sourcePath: readinessPath, pointer: item.readinessId, claim: 'Readiness deficit and blocker basis.' },
      { sourcePath: graphPath, pointer: `NODE-${item.stableId}`, claim: 'Dependency centrality and blocker propagation basis.' },
      { sourcePath: structurePath, pointer: item.stableId, claim: 'Structural-impact basis.' },
      { sourcePath: inventoryPath, pointer: item.stableId, claim: 'Authority and governed-memory reference basis.' }
    ],
    advisory: true
  };
}).sort((a, b) => b.score - a.score || a.stableId.localeCompare(b.stableId));
priorities.forEach((item, index) => { item.rank = index + 1; });
const count = tier => priorities.filter(item => item.tier === tier).length;
const result = {
  format: 'multiversal-aioc-priority-impact',
  version: '1.0.0',
  generatedAt: new Date().toISOString(),
  sources: { inventory: inventoryPath, dependencyGraph: graphPath, structureIntelligence: structurePath, completionReadiness: readinessPath },
  policy: {
    rankingRule: 'Weighted readiness deficit, dependency centrality, blocker propagation, structural impact, evidence gap, governed priority, and estimated unlock value.',
    authorityRule: 'Rankings are advisory, never modify content, and never override owner or governance authority.',
    tieBreakRule: 'Descending score, then stable ID ascending.'
  },
  summary: { totalPriorities: priorities.length, critical: count('critical'), high: count('high'), medium: count('medium'), low: count('low') },
  priorities
};
fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(result, null, 2)}\n`);
console.log(`Generated ${priorities.length} priority assessments at ${outputPath}.`);
