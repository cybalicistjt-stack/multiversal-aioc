import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const memoryPath = process.argv[2] || 'governance/development-brain/memory/AIOC_PROJECT_MEMORY.json';
const intentPath = process.argv[3] || 'governance/development-brain/design-intent/AIOC_DESIGN_INTENT.generated.json';
const historyPath = process.argv[4] || 'governance/development-brain/decision-history/AIOC_DECISION_HISTORY.generated.json';
const outputPath = process.argv[5] || 'governance/development-brain/constraint-rationale/AIOC_CONSTRAINT_RATIONALE.generated.json';

const read = file => JSON.parse(fs.readFileSync(resolvePath(file), 'utf8'));
const memory = read(memoryPath);
const intent = read(intentPath);
const history = read(historyPath);
const hash = value => crypto.createHash('sha256').update(String(value)).digest('hex').slice(0, 20);
const entries = memory.entries || memory.memories || [];
const constraints = entries.filter(item => item.status === 'active' && item.kind === 'constraint');
const records = [];
const diagnostics = { conflicts: [], circularChains: [], staleInputs: [], missingEvidence: [], unmetPrerequisites: [], unresolvedGaps: [] };

for (const constraint of constraints) {
  const relatedIntent = (intent.records || intent.intents || []).filter(item => JSON.stringify(item).includes(constraint.memoryId));
  const relatedDecisions = (history.records || history.decisions || []).filter(item => JSON.stringify(item).includes(constraint.memoryId));
  const evidence = constraint.sourceRecords || [];
  const rationaleChain = [];
  if (constraint.rationale) rationaleChain.push({ step: 1, kind: 'explicit-rationale', statement: constraint.rationale, sourceId: constraint.memoryId });
  for (const item of relatedIntent) rationaleChain.push({ step: rationaleChain.length + 1, kind: 'supported-intent', statement: item.rationale || item.summary || item.title || 'Linked design intent.', sourceId: item.intentId || item.designIntentId });
  for (const item of relatedDecisions) rationaleChain.push({ step: rationaleChain.length + 1, kind: 'supported-decision', statement: item.rationale || item.summary || item.title || 'Linked decision history.', sourceId: item.decisionId });
  if (!evidence.length) diagnostics.missingEvidence.push({ sourceId: constraint.memoryId, reason: 'Constraint has no source records.' });
  if (!rationaleChain.length) diagnostics.unresolvedGaps.push({ sourceId: constraint.memoryId, reason: 'Constraint has no explicit or supported rationale chain.' });
  records.push({
    reasoningId: `REASON-${hash(constraint.memoryId)}`,
    subject: constraint.memoryId,
    constraints: [{ statement: constraint.summary, authority: constraint.authority, status: constraint.status }],
    rationaleChain,
    conclusions: rationaleChain.length ? [{ statement: 'The explicit constraint remains applicable unless superseded by a higher-authority governed record.', derivationMethod: 'constraint-plus-supported-rationale', status: 'supported' }] : [],
    conflicts: [],
    unmetPrerequisites: [],
    authorityRequirements: ['Normal repository review, CI validation, and owner/governance approval remain required.'],
    authority: constraint.authority || 'governance-record',
    confidence: constraint.rationale && evidence.length ? 'high' : 'medium',
    freshness: { status: 'current', sourceUpdatedAt: constraint.updatedAt || memory.updatedAt || null },
    evidence,
    advisory: true
  });
}

const byScope = new Map();
for (const constraint of constraints) for (const scope of constraint.scope || []) {
  if (!byScope.has(scope)) byScope.set(scope, []);
  byScope.get(scope).push(constraint);
}
for (const [scope, items] of byScope) {
  const summaries = new Set(items.map(item => item.summary));
  if (items.length > 1 && summaries.size > 1) diagnostics.conflicts.push({ scope, sourceIds: items.map(item => item.memoryId), reason: 'Multiple active constraints apply to the same scope and require governed review.' });
}

records.sort((a,b) => a.reasoningId.localeCompare(b.reasoningId));
const result = {
  format: 'multiversal-aioc-constraint-rationale', version: '1.0.0', generatedAt: new Date().toISOString(),
  sources: { memory: memoryPath, designIntent: intentPath, decisionHistory: historyPath },
  policy: {
    precedence: 'Explicit source constraints outrank derived conclusions.',
    derivation: 'Only explicit constraints and directly linked design-intent or decision-history records may form rationale chains.',
    uncertainty: 'Conflicts, missing evidence, stale inputs, circular chains, and unresolved gaps remain visible.',
    authority: 'Outputs are advisory and grant no execution, mutation, approval, promotion, certification, assignment, or scheduling authority.'
  },
  summary: { totalRecords: records.length, totalConstraints: constraints.length, totalDiagnostics: Object.values(diagnostics).reduce((n, list) => n + list.length, 0) },
  records,
  diagnostics,
  authority: 'advisory-derived'
};
fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(result, null, 2)}\n`);
console.log(`Generated ${records.length} constraint and rationale reasoning records at ${outputPath}.`);
