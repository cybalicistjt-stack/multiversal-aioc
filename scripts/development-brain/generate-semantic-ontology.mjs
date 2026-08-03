import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const inventoryPath = process.argv[2] || 'tmp/AIOC_UNIFIED_INVENTORY.json';
const graphPath = process.argv[3] || 'tmp/AIOC_DEPENDENCY_GRAPH.json';
const outputPath = process.argv[4] || 'governance/development-brain/semantic-ontology/AIOC_SEMANTIC_ONTOLOGY.generated.json';

function ensure(file, command, args) {
  if (!fs.existsSync(resolvePath(file))) execFileSync(process.execPath, [command, ...args], { cwd: root, stdio: 'inherit' });
}
ensure(inventoryPath, 'scripts/development-brain/generate-unified-inventory.mjs', [inventoryPath]);
ensure(graphPath, 'scripts/development-brain/generate-dependency-graph.mjs', [inventoryPath, graphPath]);

const inventory = JSON.parse(fs.readFileSync(resolvePath(inventoryPath), 'utf8'));
const graph = JSON.parse(fs.readFileSync(resolvePath(graphPath), 'utf8'));
const hash = value => crypto.createHash('sha256').update(value).digest('hex').slice(0, 20);
const slug = value => String(value ?? 'unknown').trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'unknown';
const conceptMap = new Map();
const assertions = [];
const unresolved = [];

function evidence(sourcePath, pointer, claim) { return { sourcePath, pointer, claim }; }
function concept(kind, key, label, sourcePath, pointer) {
  const normalized = slug(key);
  const mapKey = `${kind}:${normalized}`;
  if (!conceptMap.has(mapKey)) conceptMap.set(mapKey, {
    conceptId: `CONCEPT-${kind.toUpperCase()}-${normalized.toUpperCase()}`,
    kind,
    key: normalized,
    label: String(label || key),
    authority: 'derived',
    evidence: [evidence(sourcePath, pointer, `Explicit ${kind} value represented as a semantic concept.`)]
  });
  return conceptMap.get(mapKey).conceptId;
}
function addAssertion(subject, predicate, object, confidence, inferenceMethod, sourceEvidence) {
  const key = `${subject}|${predicate}|${object}`;
  assertions.push({ assertionId: `ASSERT-${hash(key)}`, subject, predicate, object, confidence, inferenceMethod, evidence: sourceEvidence, advisory: true });
}

const entities = (inventory.objects || []).map((object, index) => {
  const entityId = `ENTITY-${object.stableId}`;
  const pointer = `/objects/${index}`;
  const source = inventoryPath;
  const typeValue = String(object.objectType || '').trim();
  const authorityValue = String(object.authorityLayer || '').trim();
  const lifecycleValue = String(object.lifecycle || '').trim();
  if (typeValue && typeValue.toLowerCase() !== 'unknown') addAssertion(entityId, 'has-object-type', concept('object-type', typeValue, typeValue, source, `${pointer}/objectType`), 'explicit', 'field-mapping', [evidence(source, `${pointer}/objectType`, 'Inventory objectType field.')]);
  else unresolved.push({ unresolvedId: `UNRESOLVED-${object.stableId}-OBJECT-TYPE`, stableId: object.stableId, field: 'objectType', reason: 'No supported explicit object type is available.', evidence: [evidence(source, `${pointer}/objectType`, 'Missing or unknown objectType field.')] });
  if (authorityValue) addAssertion(entityId, 'has-authority-layer', concept('authority-layer', authorityValue, authorityValue, source, `${pointer}/authorityLayer`), 'explicit', 'field-mapping', [evidence(source, `${pointer}/authorityLayer`, 'Inventory authorityLayer field.')]);
  if (lifecycleValue) addAssertion(entityId, 'has-lifecycle', concept('lifecycle', lifecycleValue, lifecycleValue, source, `${pointer}/lifecycle`), 'explicit', 'field-mapping', [evidence(source, `${pointer}/lifecycle`, 'Inventory lifecycle field.')]);
  for (const [packIndex, pack] of (object.references?.packs || []).entries()) {
    const packConcept = concept('pack', pack, pack, source, `${pointer}/references/packs/${packIndex}`);
    addAssertion(entityId, 'member-of-pack', packConcept, 'high', 'field-mapping', [evidence(source, `${pointer}/references/packs/${packIndex}`, 'Explicit inventory pack reference.')]);
  }
  return {
    entityId,
    stableId: object.stableId,
    name: object.name || object.stableId,
    authorityLayer: object.authorityLayer || 'unknown',
    lifecycle: object.lifecycle || 'unknown',
    evidence: [evidence(source, pointer, 'Unified inventory object represented as a semantic entity.')]
  };
}).sort((a, b) => a.entityId.localeCompare(b.entityId));

const entityIds = new Set(entities.map(item => item.entityId));
for (const [index, edge] of (graph.edges || []).entries()) {
  const sourceStableId = String(edge.source || '').replace(/^NODE-/, '');
  const targetStableId = String(edge.target || '').replace(/^NODE-/, '');
  const subject = `ENTITY-${sourceStableId}`;
  const object = `ENTITY-${targetStableId}`;
  if (!entityIds.has(subject) || !entityIds.has(object)) {
    unresolved.push({ unresolvedId: `UNRESOLVED-EDGE-${edge.edgeId || index}`, edgeId: edge.edgeId || null, field: 'edge-target', reason: 'Dependency edge cannot be projected because one or both semantic entities are absent.', evidence: edge.evidence || [evidence(graphPath, `/edges/${index}`, 'Unprojectable dependency edge.')] });
    continue;
  }
  concept('relationship', edge.relationship, edge.relationship, graphPath, `/edges/${index}/relationship`);
  addAssertion(subject, edge.relationship, object, edge.confidence || 'medium', 'graph-projection', (edge.evidence || []).map(item => ({ ...item, sourcePath: item.sourcePath || graphPath })));
}

const concepts = [...conceptMap.values()].sort((a, b) => a.conceptId.localeCompare(b.conceptId));
const uniqueAssertions = [...new Map(assertions.sort((a, b) => a.assertionId.localeCompare(b.assertionId)).map(item => [item.assertionId, item])).values()];
const assertionsByPredicate = {};
for (const item of uniqueAssertions) assertionsByPredicate[item.predicate] = (assertionsByPredicate[item.predicate] || 0) + 1;

const result = {
  format: 'multiversal-aioc-semantic-ontology',
  version: '1.0.0',
  generatedAt: new Date().toISOString(),
  sources: { unifiedInventory: inventoryPath, dependencyGraph: graphPath },
  policy: {
    derivationRule: 'Only explicit repository fields and validated dependency-graph edges may create semantic assertions.',
    unknownRule: 'Unsupported meaning remains unresolved; names and lexical similarity do not create semantic claims.',
    authorityRule: 'All concepts and assertions are derived and advisory and cannot mutate, promote, or certify source content.'
  },
  summary: {
    totalConcepts: concepts.length,
    totalEntities: entities.length,
    totalAssertions: uniqueAssertions.length,
    unresolved: unresolved.length,
    assertionsByPredicate
  },
  concepts,
  entities,
  assertions: uniqueAssertions,
  unresolved: unresolved.sort((a, b) => a.unresolvedId.localeCompare(b.unresolvedId))
};
fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(result, null, 2)}\n`);
console.log(`Generated semantic ontology with ${concepts.length} concepts, ${entities.length} entities, and ${uniqueAssertions.length} assertions at ${outputPath}.`);
