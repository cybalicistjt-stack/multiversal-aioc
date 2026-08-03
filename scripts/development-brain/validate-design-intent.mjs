import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const inputPath = process.argv[2] || 'governance/development-brain/design-intent/AIOC_DESIGN_INTENT.generated.json';
const file = path.isAbsolute(inputPath) ? inputPath : path.join(root, inputPath);
if (!fs.existsSync(file)) throw new Error(`Design intent artifact missing: ${inputPath}`);
const data = JSON.parse(fs.readFileSync(file, 'utf8'));
if (data.format !== 'multiversal-aioc-design-intent' || data.version !== '1.0.0') throw new Error('Unexpected design intent format or version.');
if (!Array.isArray(data.intents) || !Array.isArray(data.unresolved)) throw new Error('Intents and unresolved arrays are required.');
const ids = new Set();
for (const intent of data.intents) {
  if (!intent.intentId?.startsWith('INTENT-')) throw new Error('Invalid intent identity.');
  if (ids.has(intent.intentId)) throw new Error(`Duplicate intent identity: ${intent.intentId}`);
  ids.add(intent.intentId);
  if (!intent.subjectIds?.length || !intent.goal || !intent.intendedOutcome || !intent.problemAddressed) throw new Error(`Incomplete intent: ${intent.intentId}`);
  if (!['explicit','high','medium','low'].includes(intent.confidence)) throw new Error(`Invalid confidence: ${intent.intentId}`);
  if (!intent.evidence?.length || intent.advisory !== true) throw new Error(`Missing evidence or advisory safeguard: ${intent.intentId}`);
  for (const field of ['tradeoffs','rejectedAlternatives','invariants','extensionNotes']) if (!Array.isArray(intent[field])) throw new Error(`${field} must be an array: ${intent.intentId}`);
}
for (const unresolved of data.unresolved) if (!unresolved.unresolvedId || !unresolved.subjectId || !unresolved.reason || !unresolved.evidence?.length) throw new Error('Malformed unresolved design-intent record.');
if (data.summary?.totalIntents !== data.intents.length || data.summary?.unresolvedSubjects !== data.unresolved.length) throw new Error('Summary totals do not match artifact contents.');
console.log(`Validated ${data.intents.length} design-intent records and ${data.unresolved.length} unresolved subjects.`);
