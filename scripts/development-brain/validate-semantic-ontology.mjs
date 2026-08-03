import fs from 'node:fs';
import path from 'node:path';

const file = process.argv[2] || 'governance/development-brain/semantic-ontology/AIOC_SEMANTIC_ONTOLOGY.generated.json';
const resolved = path.isAbsolute(file) ? file : path.join(process.cwd(), file);
const data = JSON.parse(fs.readFileSync(resolved, 'utf8'));
const issues = [];
if (data.format !== 'multiversal-aioc-semantic-ontology') issues.push('Invalid format.');
if (data.version !== '1.0.0') issues.push('Unsupported version.');
if (!Array.isArray(data.concepts) || !Array.isArray(data.entities) || !Array.isArray(data.assertions) || !Array.isArray(data.unresolved)) issues.push('Concepts, entities, assertions, and unresolved must be arrays.');
const conceptIds = new Set();
for (const [index, item] of (data.concepts || []).entries()) {
  const label = `concepts[${index}]`;
  if (!item.conceptId || conceptIds.has(item.conceptId)) issues.push(`${label}: missing or duplicate conceptId.`);
  conceptIds.add(item.conceptId);
  if (item.authority !== 'derived') issues.push(`${label}: concept authority must be derived.`);
  if (!Array.isArray(item.evidence) || item.evidence.length === 0) issues.push(`${label}: evidence is required.`);
}
const entityIds = new Set();
for (const [index, item] of (data.entities || []).entries()) {
  const label = `entities[${index}]`;
  if (!item.entityId || entityIds.has(item.entityId)) issues.push(`${label}: missing or duplicate entityId.`);
  entityIds.add(item.entityId);
  if (!item.stableId || !Array.isArray(item.evidence) || item.evidence.length === 0) issues.push(`${label}: stableId and evidence are required.`);
}
const assertionIds = new Set();
for (const [index, item] of (data.assertions || []).entries()) {
  const label = `assertions[${index}]`;
  if (!item.assertionId || assertionIds.has(item.assertionId)) issues.push(`${label}: missing or duplicate assertionId.`);
  assertionIds.add(item.assertionId);
  if (!entityIds.has(item.subject)) issues.push(`${label}: subject must reference a semantic entity.`);
  const validObject = entityIds.has(item.object) || conceptIds.has(item.object);
  if (!validObject) issues.push(`${label}: object must reference a semantic entity or concept.`);
  if (!['field-mapping', 'graph-projection'].includes(item.inferenceMethod)) issues.push(`${label}: unsupported inference method.`);
  if (!['explicit', 'high', 'medium', 'low'].includes(item.confidence)) issues.push(`${label}: invalid confidence.`);
  if (!Array.isArray(item.evidence) || item.evidence.length === 0) issues.push(`${label}: evidence is required.`);
  if (item.advisory !== true) issues.push(`${label}: advisory safeguard is required.`);
}
const expected = {
  totalConcepts: data.concepts?.length || 0,
  totalEntities: data.entities?.length || 0,
  totalAssertions: data.assertions?.length || 0,
  unresolved: data.unresolved?.length || 0
};
for (const [key, value] of Object.entries(expected)) if (data.summary?.[key] !== value) issues.push(`Summary ${key} mismatch.`);
if (!String(data.policy?.unknownRule || '').toLowerCase().includes('unresolved')) issues.push('Unknown-semantics policy is required.');
if (issues.length) {
  console.error(issues.join('\n'));
  process.exit(1);
}
console.log(`Semantic ontology validation passed for ${expected.totalEntities} entities and ${expected.totalAssertions} assertions.`);
