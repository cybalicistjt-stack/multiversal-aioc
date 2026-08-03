import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const inventoryPath = process.argv[2] || 'tmp/AIOC_UNIFIED_INVENTORY.json';
const graphPath = process.argv[3] || 'tmp/AIOC_DEPENDENCY_GRAPH.json';
const outputPath = process.argv[4] || 'governance/development-brain/structure-intelligence/AIOC_STRUCTURE_INTELLIGENCE.generated.json';
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);

if (!fs.existsSync(resolvePath(inventoryPath))) execFileSync(process.execPath, ['scripts/development-brain/generate-unified-inventory.mjs', inventoryPath], { cwd: root, stdio: 'inherit' });
if (!fs.existsSync(resolvePath(graphPath))) execFileSync(process.execPath, ['scripts/development-brain/generate-dependency-graph.mjs', inventoryPath, graphPath], { cwd: root, stdio: 'inherit' });

const inventory = JSON.parse(fs.readFileSync(resolvePath(inventoryPath), 'utf8'));
const graph = JSON.parse(fs.readFileSync(resolvePath(graphPath), 'utf8'));
const edgeTypes = new Set(['contains', 'parent-of', 'variant-of', 'member-of-pack', 'requires', 'blocks']);
const edges = (graph.edges || []).filter(edge => edgeTypes.has(edge.relationship));
const nodeById = new Map((graph.nodes || []).map(node => [node.nodeId, node]));
const stableByNode = nodeId => nodeById.get(nodeId)?.stableId || nodeId.replace(/^NODE-/, '');
const unique = values => [...new Set(values)].sort();
const incoming = nodeId => edges.filter(edge => edge.target === nodeId);
const outgoing = nodeId => edges.filter(edge => edge.source === nodeId);

const objects = (inventory.objects || []).map(object => {
  const nodeId = `NODE-${object.stableId}`;
  const inEdges = incoming(nodeId);
  const outEdges = outgoing(nodeId);
  const parents = unique([
    ...inEdges.filter(edge => edge.relationship === 'contains').map(edge => stableByNode(edge.source)),
    ...inEdges.filter(edge => edge.relationship === 'parent-of').map(edge => stableByNode(edge.source))
  ]);
  const children = unique([
    ...outEdges.filter(edge => edge.relationship === 'contains').map(edge => stableByNode(edge.target)),
    ...outEdges.filter(edge => edge.relationship === 'parent-of').map(edge => stableByNode(edge.target))
  ]);
  const variants = unique([
    ...outEdges.filter(edge => edge.relationship === 'variant-of').map(edge => stableByNode(edge.target)),
    ...inEdges.filter(edge => edge.relationship === 'variant-of').map(edge => stableByNode(edge.source))
  ]);
  const packs = unique([
    ...(object.references?.packs || []),
    ...outEdges.filter(edge => edge.relationship === 'member-of-pack').map(edge => stableByNode(edge.target))
  ]);
  const classification = object.structure?.classification || object.structure?.category || object.objectType || null;
  const issues = [];
  if (!classification || classification === 'Unknown') issues.push({ type: 'unresolved-classification', severity: 'high' });
  const hasStructuralRelationship = parents.length || children.length || variants.length || packs.length;
  if (!hasStructuralRelationship && !['World', 'Setting', 'System', 'Pack'].includes(object.objectType)) issues.push({ type: 'orphan', severity: 'medium' });
  if (object.structure && object.structure.parentId && parents.length === 0) issues.push({ type: 'structural-gap', severity: 'high', field: 'parentId' });
  const declaredParentValues = unique([object.structure?.parentId, object.structure?.parent, object.structure?.parentStableId].filter(Boolean).map(String));
  if (declaredParentValues.length > 1) issues.push({ type: 'conflicting-structure-decision', severity: 'high', values: declaredParentValues });
  const structuralDependencies = unique([
    ...outEdges.filter(edge => ['requires', 'blocks'].includes(edge.relationship)).map(edge => `${edge.relationship}:${stableByNode(edge.target)}`),
    ...inEdges.filter(edge => ['requires', 'blocks'].includes(edge.relationship)).map(edge => `${edge.relationship}-by:${stableByNode(edge.source)}`)
  ]);
  return {
    stableId: object.stableId,
    nodeId,
    name: object.name,
    objectType: object.objectType,
    authorityLayer: object.authorityLayer,
    classification,
    parents,
    children,
    variants,
    packs,
    structuralDependencies,
    issues,
    evidence: [{ sourcePath: inventory.sources?.sharedState?.path || 'governance/shared-state/AIOC_SHARED_STATE.json', pointer: `/objects/${object.stableId}`, derivation: 'unified inventory plus dependency graph' }]
  };
}).sort((a, b) => a.stableId.localeCompare(b.stableId));

const unresolvedClassifications = objects.filter(o => o.issues.some(i => i.type === 'unresolved-classification')).map(o => o.stableId);
const orphans = objects.filter(o => o.issues.some(i => i.type === 'orphan')).map(o => o.stableId);
const structuralGaps = objects.flatMap(o => o.issues.filter(i => i.type === 'structural-gap').map(issue => ({ stableId: o.stableId, ...issue })));
const conflicts = objects.flatMap(o => o.issues.filter(i => i.type === 'conflicting-structure-decision').map(issue => ({ stableId: o.stableId, ...issue })));
const impact = new Map();
for (const edge of edges.filter(edge => ['contains', 'parent-of', 'requires', 'blocks'].includes(edge.relationship))) impact.set(edge.target, (impact.get(edge.target) || 0) + 1);
const highImpactDependencies = [...impact.entries()].filter(([, count]) => count >= 3).map(([nodeId, inboundCount]) => ({ stableId: stableByNode(nodeId), inboundCount })).sort((a, b) => b.inboundCount - a.inboundCount || a.stableId.localeCompare(b.stableId));

const result = {
  format: 'multiversal-aioc-structure-intelligence',
  version: '1.0.0',
  generatedAt: new Date().toISOString(),
  sources: { inventory: inventoryPath, dependencyGraph: graphPath },
  summary: {
    totalObjects: objects.length,
    classifiedObjects: objects.length - unresolvedClassifications.length,
    unresolvedClassifications: unresolvedClassifications.length,
    orphans: orphans.length,
    structuralGaps: structuralGaps.length,
    conflicts: conflicts.length,
    highImpactDependencies: highImpactDependencies.length
  },
  objects,
  diagnostics: { unresolvedClassifications, orphans, structuralGaps, conflicts, highImpactDependencies }
};

fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(result, null, 2)}\n`);
console.log(`Generated structure intelligence for ${objects.length} objects at ${outputPath}.`);
