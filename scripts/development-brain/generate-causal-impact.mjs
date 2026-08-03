import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const ontologyPath = process.argv[2] || 'tmp/AIOC_SEMANTIC_ONTOLOGY.json';
const outputPath = process.argv[3] || 'governance/development-brain/causal-impact/AIOC_CAUSAL_IMPACT.generated.json';
const maxDepth = 4;

if (!fs.existsSync(resolvePath(ontologyPath))) {
  execFileSync(process.execPath, ['scripts/development-brain/generate-semantic-ontology.mjs', 'tmp/AIOC_UNIFIED_INVENTORY.json', 'tmp/AIOC_DEPENDENCY_GRAPH.json', ontologyPath], { cwd: root, stdio: 'inherit' });
}
const ontology = JSON.parse(fs.readFileSync(resolvePath(ontologyPath), 'utf8'));
const hash = value => crypto.createHash('sha256').update(value).digest('hex').slice(0, 20);
const entityById = new Map((ontology.entities || []).map(item => [item.entityId, item]));
const domainByEntity = new Map();
for (const assertion of ontology.assertions || []) {
  if (assertion.predicate === 'has-object-type') {
    domainByEntity.set(assertion.subject, String(assertion.object).replace(/^CONCEPT-OBJECT-TYPE-/, '').toLowerCase());
  }
}

const relationshipPolicy = {
  affects: { classification: 'direct-causal-evidence', traversable: true, weight: 1.0 },
  requires: { classification: 'dependency-impact', traversable: true, weight: 0.8 },
  blocks: { classification: 'dependency-impact', traversable: true, weight: 0.8 },
  validates: { classification: 'dependency-impact', traversable: true, weight: 0.7 },
  grants: { classification: 'dependency-impact', traversable: true, weight: 0.7 },
  supersedes: { classification: 'dependency-impact', traversable: true, weight: 0.6 },
  'parent-of': { classification: 'structural-impact', traversable: true, weight: 0.5 },
  contains: { classification: 'structural-impact', traversable: true, weight: 0.5 },
  'variant-of': { classification: 'structural-impact', traversable: true, weight: 0.5 },
  'member-of-pack': { classification: 'structural-impact', traversable: false, weight: 0.4 }
};
const assertions = (ontology.assertions || []).filter(item => entityById.has(item.subject) && entityById.has(item.object) && relationshipPolicy[item.predicate]);
const adjacency = new Map();
for (const assertion of assertions) {
  if (!adjacency.has(assertion.subject)) adjacency.set(assertion.subject, []);
  adjacency.get(assertion.subject).push(assertion);
}
for (const list of adjacency.values()) list.sort((a, b) => a.assertionId.localeCompare(b.assertionId));

const reachableCount = source => {
  const seen = new Set([source]);
  const queue = [{ id: source, depth: 0 }];
  let deepest = 0;
  while (queue.length) {
    const current = queue.shift();
    deepest = Math.max(deepest, current.depth);
    if (current.depth >= maxDepth) continue;
    for (const edge of adjacency.get(current.id) || []) {
      if (!relationshipPolicy[edge.predicate]?.traversable || seen.has(edge.object)) continue;
      seen.add(edge.object);
      queue.push({ id: edge.object, depth: current.depth + 1 });
    }
  }
  const count = Math.max(0, seen.size - 1);
  return { reachableEntities: count, maxDepth: deepest, rating: count >= 20 ? 'critical' : count >= 10 ? 'high' : count >= 4 ? 'medium' : 'low' };
};

const paths = [];
for (const source of [...entityById.keys()].sort()) {
  const blastRadius = reachableCount(source);
  const queue = [{ entity: source, chain: [], evidence: [], confidence: 'explicit' }];
  const bestDepth = new Map([[source, 0]]);
  while (queue.length) {
    const current = queue.shift();
    if (current.chain.length >= maxDepth) continue;
    for (const assertion of adjacency.get(current.entity) || []) {
      if (!relationshipPolicy[assertion.predicate]?.traversable) continue;
      const chain = [...current.chain, assertion.predicate];
      const target = assertion.object;
      if (target === source) continue;
      const depth = chain.length;
      if ((bestDepth.get(target) ?? Infinity) < depth) continue;
      bestDepth.set(target, depth);
      const classification = chain.length === 1 ? relationshipPolicy[assertion.predicate].classification : 'dependency-impact';
      const confidence = chain.length === 1 ? assertion.confidence : (chain.length === 2 ? 'medium' : 'low');
      const evidence = [...current.evidence, ...(assertion.evidence || [])];
      paths.push({
        impactPathId: `IMPACT-${hash(`${source}|${target}|${chain.join('>')}`)}`,
        sourceEntity: source,
        targetEntity: target,
        classification,
        relationshipChain: chain,
        hopCount: depth,
        confidence,
        derivationMethod: chain.length === 1 ? 'direct-semantic-assertion' : 'bounded-graph-propagation',
        blastRadius,
        affectedDomains: [...new Set([domainByEntity.get(source), domainByEntity.get(target)].filter(Boolean))].sort(),
        evidence,
        advisory: true
      });
      queue.push({ entity: target, chain, evidence, confidence });
    }
  }
}

const uniquePaths = [...new Map(paths.sort((a, b) => a.impactPathId.localeCompare(b.impactPathId)).map(item => [item.impactPathId, item])).values()];
const unresolvedHypotheses = (ontology.unresolved || []).map(item => ({
  hypothesisId: `HYPOTHESIS-${hash(item.unresolvedId || JSON.stringify(item))}`,
  status: 'unresolved',
  reason: 'A causal claim cannot be derived because the underlying semantic meaning is unresolved.',
  sourceFinding: item.unresolvedId || null,
  evidence: item.evidence || [],
  advisory: true
})).sort((a, b) => a.hypothesisId.localeCompare(b.hypothesisId));

const result = {
  format: 'multiversal-aioc-causal-impact',
  version: '1.0.0',
  generatedAt: new Date().toISOString(),
  sources: { semanticOntology: ontologyPath },
  policy: {
    causationRule: 'Only explicit affects assertions are classified as direct causal evidence; dependency propagation is never treated as proof of causation.',
    propagationRule: `Impact propagation is deterministic and bounded to ${maxDepth} hops over approved semantic relationships.`,
    hypothesisRule: 'Unsupported causal claims remain unresolved hypotheses and are not promoted to facts.',
    authorityRule: 'All outputs are derived, advisory, and cannot mutate, promote, certify, assign, or schedule source content.'
  },
  summary: {
    totalImpactPaths: uniquePaths.length,
    directCausalEvidence: uniquePaths.filter(item => item.classification === 'direct-causal-evidence').length,
    dependencyImpact: uniquePaths.filter(item => item.classification === 'dependency-impact').length,
    structuralImpact: uniquePaths.filter(item => item.classification === 'structural-impact').length,
    unresolvedHypotheses: unresolvedHypotheses.length
  },
  impactPaths: uniquePaths,
  unresolvedHypotheses
};
fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(result, null, 2)}\n`);
console.log(`Generated ${uniquePaths.length} causal and impact paths at ${outputPath}.`);
