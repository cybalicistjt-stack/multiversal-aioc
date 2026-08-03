import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const memoryPath = process.argv[2] || 'governance/development-brain/memory/AIOC_PROJECT_MEMORY.json';
const inventoryPath = process.argv[3] || 'tmp/AIOC_UNIFIED_INVENTORY.json';
const outputPath = process.argv[4] || 'governance/development-brain/design-intent/AIOC_DESIGN_INTENT.generated.json';
if (!fs.existsSync(resolvePath(inventoryPath))) execFileSync(process.execPath, ['scripts/development-brain/generate-unified-inventory.mjs', inventoryPath], { cwd: root, stdio: 'inherit' });
const memory = JSON.parse(fs.readFileSync(resolvePath(memoryPath), 'utf8'));
const inventory = JSON.parse(fs.readFileSync(resolvePath(inventoryPath), 'utf8'));
const hash = value => crypto.createHash('sha256').update(String(value)).digest('hex').slice(0, 20);
const evidence = (pointer, claim) => [{ sourcePath: memoryPath, pointer, claim }];
const supportedKinds = new Set(['decision', 'constraint', 'priority', 'technical-debt']);
const intents = [];
for (const [index, entry] of (memory.entries || []).entries()) {
  if (!supportedKinds.has(entry.kind) || entry.status !== 'active' || !entry.rationale || !entry.summary) continue;
  const subjects = [...new Set((entry.relatedIds || []).map(String).filter(Boolean))];
  if (!subjects.length) subjects.push(`MEMORY-${entry.memoryId}`);
  const invariants = entry.kind === 'constraint' ? [entry.summary] : [];
  const tradeoffs = entry.kind === 'technical-debt' ? [entry.summary] : [];
  const extensionNotes = entry.kind === 'priority' ? [entry.summary] : [];
  intents.push({
    intentId: `INTENT-${hash(entry.memoryId)}`,
    sourceMemoryId: entry.memoryId,
    subjectIds: subjects,
    title: entry.title,
    goal: entry.summary,
    intendedOutcome: entry.summary,
    problemAddressed: entry.rationale,
    tradeoffs,
    rejectedAlternatives: [],
    invariants,
    extensionNotes,
    authority: entry.authority || 'governance-record',
    confidence: entry.authority === 'owner-approved' ? 'explicit' : 'high',
    evidence: evidence(`/entries/${index}`, 'Explicit governed project-memory record containing summary and rationale.'),
    advisory: true
  });
}
intents.sort((a, b) => a.intentId.localeCompare(b.intentId));
const covered = new Set(intents.flatMap(item => item.subjectIds));
const unresolved = [];
for (const object of inventory.objects || []) {
  if (!covered.has(String(object.stableId))) unresolved.push({
    unresolvedId: `UNRESOLVED-INTENT-${hash(object.stableId)}`,
    subjectId: object.stableId,
    reason: 'No explicit governed design-intent record is linked to this subject.',
    evidence: [{ sourcePath: inventoryPath, pointer: `/objects/${object.stableId}`, claim: 'Inventory object exists, but rationale must not be inferred from its name or implementation.' }]
  });
}
const result = {
  format: 'multiversal-aioc-design-intent',
  version: '1.0.0',
  generatedAt: new Date().toISOString(),
  sources: { projectMemory: memoryPath, unifiedInventory: inventoryPath },
  policy: {
    derivationRule: 'Design intent may only be created from active governed memory records with explicit summary and rationale.',
    inferenceRule: 'Names, code structure, implementation details, lexical similarity, and model preference cannot create rationale.',
    uncertaintyRule: 'Missing tradeoffs, rejected alternatives, invariants, extension notes, or subject rationale remain empty or unresolved rather than guessed.',
    authorityRule: 'Design intent is advisory context and cannot mutate, promote, certify, approve, assign, or schedule work.'
  },
  summary: { totalIntents: intents.length, ownerApproved: intents.filter(x => x.authority === 'owner-approved').length, unresolvedSubjects: unresolved.length },
  intents,
  unresolved: unresolved.sort((a, b) => a.unresolvedId.localeCompare(b.unresolvedId))
};
fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(result, null, 2)}\n`);
console.log(`Generated ${intents.length} explicit design-intent records and ${unresolved.length} unresolved subjects at ${outputPath}.`);
