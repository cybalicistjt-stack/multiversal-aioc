import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const graphPath = process.argv[2] || 'governance/development-brain/dependency-graph/AIOC_DEPENDENCY_GRAPH.generated.json';
const requiredRelationships = ['requires','grants','contains','parent-of','variant-of','validates','affects','supersedes','blocks','member-of-pack'];
const errors = [];
const graph = JSON.parse(fs.readFileSync(path.join(root, graphPath), 'utf8'));

if (graph.format !== 'multiversal-aioc-dependency-graph') errors.push('Unexpected graph format.');
if (graph.version !== '1.0.0') errors.push('Unexpected graph version.');
if (!Array.isArray(graph.nodes)) errors.push('nodes must be an array.');
if (!Array.isArray(graph.edges)) errors.push('edges must be an array.');
for (const relationship of requiredRelationships) if (!graph.relationshipVocabulary?.includes(relationship)) errors.push(`Missing relationship vocabulary: ${relationship}`);

const nodeIds = new Set();
for (const [index, node] of (graph.nodes || []).entries()) {
  if (!node.nodeId || !node.nodeId.startsWith('NODE-')) errors.push(`Node ${index} has invalid nodeId.`);
  if (nodeIds.has(node.nodeId)) errors.push(`Duplicate nodeId: ${node.nodeId}`);
  nodeIds.add(node.nodeId);
  for (const field of ['inventoryId','stableId','name','objectType','authorityLayer','lifecycle']) if (node[field] == null) errors.push(`Node ${node.nodeId || index} missing ${field}.`);
}
const edgeIds = new Set();
const triples = new Set();
for (const [index, edge] of (graph.edges || []).entries()) {
  if (!edge.edgeId || !edge.edgeId.startsWith('EDGE-')) errors.push(`Edge ${index} has invalid edgeId.`);
  if (edgeIds.has(edge.edgeId)) errors.push(`Duplicate edgeId: ${edge.edgeId}`);
  edgeIds.add(edge.edgeId);
  if (!nodeIds.has(edge.source)) errors.push(`Dangling edge source: ${edge.edgeId} -> ${edge.source}`);
  if (!nodeIds.has(edge.target)) errors.push(`Dangling edge target: ${edge.edgeId} -> ${edge.target}`);
  if (edge.source === edge.target) errors.push(`Self dependency: ${edge.edgeId}`);
  if (!requiredRelationships.includes(edge.relationship)) errors.push(`Unknown relationship on ${edge.edgeId}: ${edge.relationship}`);
  if (!['explicit','high','medium','low'].includes(edge.confidence)) errors.push(`Invalid confidence on ${edge.edgeId}.`);
  if (!Array.isArray(edge.evidence) || edge.evidence.length === 0) errors.push(`Missing evidence on ${edge.edgeId}.`);
  for (const evidence of edge.evidence || []) for (const field of ['sourcePath','pointer','derivation']) if (!evidence[field]) errors.push(`Incomplete evidence on ${edge.edgeId}.`);
  const triple = `${edge.source}|${edge.relationship}|${edge.target}`;
  if (triples.has(triple)) errors.push(`Duplicate edge triple: ${triple}`);
  triples.add(triple);
}

const diagnostics = graph.diagnostics || {};
for (const key of ['danglingTargets','duplicateEdges','selfDependencies','prohibitedCycles']) if (!Array.isArray(diagnostics[key])) errors.push(`Missing diagnostics array: ${key}`);
if ((diagnostics.danglingTargets || []).length) errors.push(`Graph reports ${diagnostics.danglingTargets.length} dangling targets.`);
if ((diagnostics.duplicateEdges || []).length) errors.push(`Graph reports ${diagnostics.duplicateEdges.length} duplicate edges.`);
if ((diagnostics.selfDependencies || []).length) errors.push(`Graph reports ${diagnostics.selfDependencies.length} self dependencies.`);
if ((diagnostics.prohibitedCycles || []).length) errors.push(`Graph reports ${diagnostics.prohibitedCycles.length} prohibited cycles.`);
if (graph.summary?.totalNodes !== (graph.nodes || []).length) errors.push('summary.totalNodes does not match nodes length.');
if (graph.summary?.totalEdges !== (graph.edges || []).length) errors.push('summary.totalEdges does not match edges length.');

if (errors.length) {
  console.error(`Dependency graph validation failed with ${errors.length} error(s):`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}
console.log(`Dependency graph validation passed: ${graph.nodes.length} nodes, ${graph.edges.length} edges.`);
