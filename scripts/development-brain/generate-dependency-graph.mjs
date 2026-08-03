import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const inventoryPath = process.argv[2] || '/tmp/AIOC_UNIFIED_INVENTORY.json';
const outputPath = process.argv[3] || 'governance/development-brain/dependency-graph/AIOC_DEPENDENCY_GRAPH.generated.json';
const vocabulary = ['requires','grants','contains','parent-of','variant-of','validates','affects','supersedes','blocks','member-of-pack'];

if (!fs.existsSync(path.join(root, inventoryPath))) {
  execFileSync(process.execPath, ['scripts/development-brain/generate-unified-inventory.mjs', inventoryPath], { cwd: root, stdio: 'inherit' });
}
const inventory = JSON.parse(fs.readFileSync(path.join(root, inventoryPath), 'utf8'));
const objects = Array.isArray(inventory.objects) ? inventory.objects : [];
const nodes = objects.map(object => ({
  nodeId: `NODE-${object.stableId}`,
  inventoryId: object.inventoryId,
  stableId: object.stableId,
  name: object.name,
  objectType: object.objectType,
  authorityLayer: object.authorityLayer,
  lifecycle: object.lifecycle
})).sort((a,b) => a.nodeId.localeCompare(b.nodeId));
const nodeByStableId = new Map(nodes.map(node => [node.stableId, node.nodeId]));
const edges = [];

function hash(value) { return crypto.createHash('sha256').update(value).digest('hex').slice(0, 20); }
function addEdge(sourceStableId, targetStableId, relationship, confidence, sourcePath, pointer, derivation) {
  if (!sourceStableId || !targetStableId || !vocabulary.includes(relationship)) return;
  const source = nodeByStableId.get(String(sourceStableId)) || `NODE-${sourceStableId}`;
  const target = nodeByStableId.get(String(targetStableId)) || `NODE-${targetStableId}`;
  const key = `${source}|${relationship}|${target}`;
  edges.push({ edgeId: `EDGE-${hash(key)}`, source, target, relationship, confidence, evidence: [{ sourcePath, pointer, derivation }] });
}
function valueIds(value) {
  if (value == null) return [];
  if (typeof value === 'string' || typeof value === 'number') return [String(value)];
  if (Array.isArray(value)) return value.flatMap(valueIds);
  if (typeof value === 'object') return ['stableId','id','target','targetId','objectId','refId','parentId','canonicalTarget','variantOf','supersedes','blocks'].flatMap(key => value[key] == null ? [] : valueIds(value[key]));
  return [];
}

for (const object of objects) {
  const id = object.stableId;
  for (const dependency of object.references?.dependencies || []) addEdge(id, dependency, 'requires', 'explicit', inventory.sources?.canonicalContent?.path || 'content-db/index.json', `/objects/${id}/references/dependencies`, 'declared dependency');
  for (const pack of object.references?.packs || []) addEdge(id, pack, 'member-of-pack', 'high', inventory.sources?.sharedState?.path || 'governance/shared-state/AIOC_SHARED_STATE.json', `/objects/${id}/references/packs`, 'inventory pack reference');
  const structure = object.structure || {};
  for (const target of valueIds(structure.parentId ?? structure.parent ?? structure.parentStableId)) addEdge(target, id, 'parent-of', 'high', inventory.sources?.sharedState?.path || 'governance/shared-state/AIOC_SHARED_STATE.json', `/objects/${id}/structure`, 'structure parent');
  for (const target of valueIds(structure.canonicalTarget ?? structure.contains ?? structure.children)) addEdge(id, target, 'contains', 'medium', inventory.sources?.sharedState?.path || 'governance/shared-state/AIOC_SHARED_STATE.json', `/objects/${id}/structure`, 'structure containment');
  for (const target of valueIds(structure.variantOf ?? structure.variantOfId)) addEdge(id, target, 'variant-of', 'high', inventory.sources?.sharedState?.path || 'governance/shared-state/AIOC_SHARED_STATE.json', `/objects/${id}/structure`, 'structure variant');
  for (const relationship of ['grants','validates','affects','supersedes','blocks']) {
    for (const target of valueIds(structure[relationship])) addEdge(id, target, relationship, 'medium', inventory.sources?.sharedState?.path || 'governance/shared-state/AIOC_SHARED_STATE.json', `/objects/${id}/structure/${relationship}`, `structure ${relationship}`);
  }
}

edges.sort((a,b) => a.edgeId.localeCompare(b.edgeId));
const nodeIds = new Set(nodes.map(node => node.nodeId));
const seen = new Map();
const duplicateEdges = [];
for (const edge of edges) {
  const key = `${edge.source}|${edge.relationship}|${edge.target}`;
  if (seen.has(key)) duplicateEdges.push({ edgeId: edge.edgeId, duplicateOf: seen.get(key), key }); else seen.set(key, edge.edgeId);
}
const danglingTargets = edges.filter(edge => !nodeIds.has(edge.source) || !nodeIds.has(edge.target)).map(edge => ({ edgeId: edge.edgeId, sourceMissing: !nodeIds.has(edge.source), targetMissing: !nodeIds.has(edge.target) }));
const selfDependencies = edges.filter(edge => edge.source === edge.target).map(edge => ({ edgeId: edge.edgeId, relationship: edge.relationship, nodeId: edge.source }));
const acyclic = new Set(['requires','parent-of','variant-of','supersedes','blocks']);
const adjacency = new Map();
for (const edge of edges.filter(edge => acyclic.has(edge.relationship) && nodeIds.has(edge.source) && nodeIds.has(edge.target))) {
  const key = `${edge.relationship}:${edge.source}`;
  if (!adjacency.has(key)) adjacency.set(key, []);
  adjacency.get(key).push(edge.target);
}
const prohibitedCycles = [];
for (const relationship of acyclic) {
  const visiting = new Set(), visited = new Set(), stack = [];
  function visit(node) {
    if (visiting.has(node)) { const index = stack.indexOf(node); prohibitedCycles.push({ relationship, nodes: [...stack.slice(index), node] }); return; }
    if (visited.has(node)) return;
    visiting.add(node); stack.push(node);
    for (const target of adjacency.get(`${relationship}:${node}`) || []) visit(target);
    stack.pop(); visiting.delete(node); visited.add(node);
  }
  for (const node of nodes.map(node => node.nodeId)) visit(node);
}
const uniqueEdges = edges.filter(edge => !duplicateEdges.some(duplicate => duplicate.edgeId === edge.edgeId));
const edgesByType = Object.fromEntries(vocabulary.map(type => [type, uniqueEdges.filter(edge => edge.relationship === type).length]));
const diagnostics = { danglingTargets, duplicateEdges, selfDependencies, prohibitedCycles };
const graph = {
  format: 'multiversal-aioc-dependency-graph', version: '1.0.0', generatedAt: new Date().toISOString(),
  sources: { unifiedInventory: inventory.sources || {}, inventoryFormat: inventory.format, inventoryVersion: inventory.version },
  relationshipVocabulary: vocabulary,
  summary: { totalNodes: nodes.length, totalEdges: uniqueEdges.length, edgesByType, danglingTargets: danglingTargets.length, duplicateEdges: duplicateEdges.length, selfDependencies: selfDependencies.length, prohibitedCycles: prohibitedCycles.length },
  nodes, edges: uniqueEdges, diagnostics
};
fs.mkdirSync(path.dirname(path.join(root, outputPath)), { recursive: true });
fs.writeFileSync(path.join(root, outputPath), `${JSON.stringify(graph, null, 2)}\n`);
console.log(`Generated dependency graph with ${nodes.length} nodes and ${uniqueEdges.length} edges at ${outputPath}.`);
