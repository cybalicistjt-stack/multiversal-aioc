import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const inputPath = process.argv[2] || 'governance/development-brain/structure-intelligence/AIOC_STRUCTURE_INTELLIGENCE.generated.json';
const resolved = path.isAbsolute(inputPath) ? inputPath : path.join(root, inputPath);
const data = JSON.parse(fs.readFileSync(resolved, 'utf8'));
const errors = [];

if (data.format !== 'multiversal-aioc-structure-intelligence') errors.push('Unexpected structure intelligence format.');
if (data.version !== '1.0.0') errors.push('Unexpected structure intelligence version.');
if (!Array.isArray(data.objects)) errors.push('objects must be an array.');
if (!data.diagnostics || typeof data.diagnostics !== 'object') errors.push('diagnostics missing.');

const ids = new Set();
for (const [index, object] of (data.objects || []).entries()) {
  if (!object.stableId) errors.push(`Object ${index} missing stableId.`);
  if (ids.has(object.stableId)) errors.push(`Duplicate stableId: ${object.stableId}`);
  ids.add(object.stableId);
  if (!object.nodeId?.startsWith('NODE-')) errors.push(`${object.stableId}: invalid nodeId.`);
  if (!['canonical', 'working'].includes(object.authorityLayer)) errors.push(`${object.stableId}: invalid authorityLayer.`);
  for (const field of ['parents', 'children', 'variants', 'packs', 'structuralDependencies', 'issues', 'evidence']) if (!Array.isArray(object[field])) errors.push(`${object.stableId}: ${field} must be an array.`);
  if (!object.evidence?.length) errors.push(`${object.stableId}: evidence is required.`);
}

const diagnostics = data.diagnostics || {};
for (const key of ['unresolvedClassifications', 'orphans', 'structuralGaps', 'conflicts', 'highImpactDependencies']) if (!Array.isArray(diagnostics[key])) errors.push(`Missing diagnostics array: ${key}`);
const expected = {
  totalObjects: (data.objects || []).length,
  classifiedObjects: (data.objects || []).filter(o => o.classification && o.classification !== 'Unknown').length,
  unresolvedClassifications: diagnostics.unresolvedClassifications?.length || 0,
  orphans: diagnostics.orphans?.length || 0,
  structuralGaps: diagnostics.structuralGaps?.length || 0,
  conflicts: diagnostics.conflicts?.length || 0,
  highImpactDependencies: diagnostics.highImpactDependencies?.length || 0
};
for (const [key, value] of Object.entries(expected)) if (data.summary?.[key] !== value) errors.push(`summary.${key} mismatch.`);
if ((data.objects || []).length < 487) errors.push('Structure intelligence unexpectedly contains fewer than 487 objects.');

if (errors.length) {
  console.error(`Structure intelligence validation failed with ${errors.length} error(s):`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}
console.log(JSON.stringify({ result: 'PASS', ...data.summary }, null, 2));
