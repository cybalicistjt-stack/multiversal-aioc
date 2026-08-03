import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const outputPath = process.argv[2] || 'governance/development-brain/semantic-retrieval/AIOC_SEMANTIC_RETRIEVAL.generated.json';
const paths = {
  inventory: 'tmp/AIOC_UNIFIED_INVENTORY.json',
  graph: 'tmp/AIOC_DEPENDENCY_GRAPH.json',
  structure: 'tmp/AIOC_STRUCTURE_INTELLIGENCE.json',
  semantic: 'tmp/AIOC_SEMANTIC_ONTOLOGY.json',
  causal: 'tmp/AIOC_CAUSAL_IMPACT.json',
  memory: 'governance/development-brain/memory/AIOC_PROJECT_MEMORY.json',
  readiness: 'tmp/AIOC_COMPLETION_READINESS.json',
  priority: 'tmp/AIOC_PRIORITY_IMPACT.json',
  recommendations: 'tmp/AIOC_RECOMMENDATION_PLANNER.json',
  verification: 'tmp/AIOC_VERIFICATION_GOVERNANCE.json'
};
function ensure(file, script, args = []) {
  if (!fs.existsSync(resolvePath(file))) execFileSync(process.execPath, [script, ...args], { cwd: root, stdio: 'inherit' });
}
ensure(paths.inventory, 'scripts/development-brain/generate-unified-inventory.mjs', [paths.inventory]);
ensure(paths.graph, 'scripts/development-brain/generate-dependency-graph.mjs', [paths.inventory, paths.graph]);
ensure(paths.structure, 'scripts/development-brain/generate-structure-intelligence.mjs', [paths.inventory, paths.graph, paths.structure]);
ensure(paths.semantic, 'scripts/development-brain/generate-semantic-ontology.mjs', [paths.inventory, paths.graph, paths.semantic]);
ensure(paths.causal, 'scripts/development-brain/generate-causal-impact.mjs', [paths.semantic, paths.causal]);
ensure(paths.readiness, 'scripts/development-brain/generate-completion-readiness.mjs', [paths.inventory, paths.graph, paths.structure, paths.readiness]);
ensure(paths.priority, 'scripts/development-brain/generate-priority-impact.mjs', [paths.inventory, paths.graph, paths.structure, paths.readiness, paths.priority]);
ensure(paths.recommendations, 'scripts/development-brain/generate-recommendation-planner.mjs', [paths.inventory, paths.graph, paths.structure, paths.readiness, paths.priority, paths.recommendations]);
ensure(paths.verification, 'scripts/development-brain/generate-verification-governance.mjs', [paths.inventory, paths.readiness, paths.recommendations, paths.verification]);

const read = file => JSON.parse(fs.readFileSync(resolvePath(file), 'utf8'));
const inventory = read(paths.inventory);
const semantic = read(paths.semantic);
const causal = read(paths.causal);
const memory = read(paths.memory);
const readiness = read(paths.readiness);
const priority = read(paths.priority);
const recommendations = read(paths.recommendations);
const verification = read(paths.verification);
const hash = value => crypto.createHash('sha256').update(String(value)).digest('hex').slice(0, 20);
const fingerprint = hash(JSON.stringify({
  inventory: inventory.generatedAt, semantic: semantic.generatedAt, causal: causal.generatedAt,
  memory: memory.revision ?? memory.version, readiness: readiness.generatedAt, priority: priority.generatedAt,
  recommendations: recommendations.generatedAt, verification: verification.generatedAt
}));
const MAX_ITEMS = 24;
const MAX_CHARS = 12000;
const packages = [];
const truncated = [];

function refs(value, entityId, stableId) {
  const text = JSON.stringify(value);
  return text.includes(entityId) || text.includes(stableId);
}
function evidence(pathValue, pointer, claim) { return [{ sourcePath: pathValue, pointer, claim }]; }
function item(category, statement, authorityLayer, confidence, score, sourceEvidence, key) {
  return { contextItemId: `CTXITEM-${hash(key)}`, category, score, statement, authorityLayer, confidence, sourceEvidence, freshness: 'current', advisory: true };
}
function collect(entity) {
  const stableId = entity.stableId;
  const entityId = entity.entityId;
  const candidates = [];
  const invIndex = (inventory.objects || []).findIndex(x => x.stableId === stableId);
  const inv = inventory.objects?.[invIndex];
  if (inv) candidates.push(item('source-fact', `${inv.name} is an explicit ${inv.objectType} object in the ${inv.authorityLayer} authority layer with lifecycle ${inv.lifecycle}.`, inv.authorityLayer, 'explicit', 100, evidence(paths.inventory, `/objects/${invIndex}`, 'Unified inventory record.'), `${entityId}|inventory`));
  for (const assertion of semantic.assertions || []) if (assertion.subject === entityId || assertion.object === entityId) candidates.push(item('derived-finding', `${assertion.subject} ${assertion.predicate} ${assertion.object}.`, 'derived', assertion.confidence || 'unknown', 85, assertion.evidence || evidence(paths.semantic, `/assertions/${assertion.assertionId}`, 'Semantic assertion.'), `${entityId}|semantic|${assertion.assertionId}`));
  for (const pathItem of causal.impactPaths || causal.paths || []) if (refs(pathItem, entityId, stableId)) candidates.push(item('derived-finding', `Impact path ${pathItem.pathId || pathItem.impactPathId || 'unidentified'} connects governed entities with classification ${pathItem.classification || pathItem.kind || 'impact'}.`, 'derived', pathItem.confidence || 'unknown', 75, pathItem.evidence || evidence(paths.causal, '/impactPaths', 'Causal-impact path.'), `${entityId}|causal|${pathItem.pathId || JSON.stringify(pathItem)}`));
  for (const record of memory.memories || []) if (refs(record, entityId, stableId)) candidates.push(item(record.type === 'constraint' ? 'constraint' : 'source-fact', record.summary || record.statement || record.title || `Project memory ${record.memoryId}`, record.authority || 'governed-memory', record.confidence || 'explicit', record.type === 'constraint' ? 95 : 80, record.evidence || evidence(paths.memory, `/memories/${record.memoryId}`, 'Governed project-memory record.'), `${entityId}|memory|${record.memoryId}`));
  for (const source of [readiness, priority]) for (const record of [...(source.objects || []), ...(source.results || []), ...(source.priorities || [])]) if (refs(record, entityId, stableId)) candidates.push(item('derived-finding', record.reason || record.summary || `${stableId} has derived intelligence result.`, 'derived', record.confidence || 'medium', source === priority ? 70 : 65, record.evidence || evidence(source === priority ? paths.priority : paths.readiness, '/', 'Derived intelligence record.'), `${entityId}|derived|${hash(JSON.stringify(record))}`));
  for (const record of recommendations.recommendations || []) if (refs(record, entityId, stableId)) candidates.push(item('recommendation', record.rationale || record.title || `Recommendation ${record.recommendationId}`, 'advisory', record.confidence || 'medium', 60, record.evidence || evidence(paths.recommendations, `/recommendations/${record.recommendationId}`, 'Advisory recommendation.'), `${entityId}|recommendation|${record.recommendationId}`));
  for (const record of verification.verifications || verification.records || []) if (refs(record, entityId, stableId)) candidates.push(item('constraint', `Verification status ${record.status || record.outcome || 'unknown'} applies to ${record.recommendationId || stableId}.`, 'governance', record.confidence || 'high', 90, record.evidence || evidence(paths.verification, '/', 'Verification-governance record.'), `${entityId}|verification|${record.verificationId || hash(JSON.stringify(record))}`));
  for (const unresolved of [...(semantic.unresolved || []), ...(causal.unresolved || [])]) if (refs(unresolved, entityId, stableId)) candidates.push(item('unresolved-question', unresolved.reason || 'A related semantic or causal question remains unresolved.', 'derived', 'unknown', 50, unresolved.evidence || evidence(paths.semantic, '/unresolved', 'Explicit unresolved finding.'), `${entityId}|unresolved|${unresolved.unresolvedId || hash(JSON.stringify(unresolved))}`));
  const unique = [...new Map(candidates.map(x => [x.contextItemId, x])).values()].sort((a,b) => b.score - a.score || a.contextItemId.localeCompare(b.contextItemId));
  const selected = [];
  let usedCharacters = 0;
  for (const candidate of unique) {
    const size = JSON.stringify(candidate).length;
    if (selected.length >= MAX_ITEMS || usedCharacters + size > MAX_CHARS) { truncated.push({ subject: entityId, contextItemId: candidate.contextItemId, reason: 'budget-exceeded' }); continue; }
    selected.push(candidate); usedCharacters += size;
  }
  selected.forEach((x, index) => x.rank = index + 1);
  return { packageId: `CONTEXT-${stableId}`, subject: entityId, budget: { maxItems: MAX_ITEMS, maxCharacters: MAX_CHARS, usedItems: selected.length, usedCharacters }, freshness: { status: 'current', sourceFingerprint: fingerprint }, items: selected, authority: 'read-only-context', advisory: true };
}
for (const entity of semantic.entities || []) packages.push(collect(entity));
packages.sort((a,b) => a.packageId.localeCompare(b.packageId));
const duplicateItems = [];
for (const pkg of packages) {
  const seen = new Set();
  for (const entry of pkg.items) { if (seen.has(entry.contextItemId)) duplicateItems.push({ packageId: pkg.packageId, contextItemId: entry.contextItemId }); seen.add(entry.contextItemId); }
}
const result = {
  format: 'multiversal-aioc-semantic-retrieval', version: '1.0.0', generatedAt: new Date().toISOString(),
  sources: paths,
  policy: {
    rankingRule: 'Items are ranked deterministically by category-aware score then stable context-item identity.',
    budgetRule: `Each package is limited to ${MAX_ITEMS} items and ${MAX_CHARS} serialized characters.`,
    separationRule: 'Source facts, derived findings, recommendations, constraints, and unresolved questions remain explicitly separated.',
    authorityRule: 'Context packages are read-only and advisory and grant no execution, mutation, approval, promotion, or certification authority.',
    freshnessRule: 'Every package carries a fingerprint of all upstream generated and governed sources.'
  },
  summary: { totalPackages: packages.length, totalItems: packages.reduce((n,p) => n + p.items.length, 0), truncatedItems: truncated.length, duplicateItems: duplicateItems.length },
  packages,
  diagnostics: { truncated, duplicateItems, stalePackages: [] }
};
fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(result, null, 2)}\n`);
console.log(`Generated ${packages.length} semantic reasoning-context packages at ${outputPath}.`);
