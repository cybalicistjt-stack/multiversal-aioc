import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const memoryPath = process.argv[2] || 'governance/development-brain/memory/AIOC_PROJECT_MEMORY.json';
const intentPath = process.argv[3] || 'governance/development-brain/design-intent/AIOC_DESIGN_INTENT.generated.json';
const outputPath = process.argv[4] || 'governance/development-brain/decision-history/AIOC_DECISION_HISTORY.generated.json';

const memory = JSON.parse(fs.readFileSync(resolvePath(memoryPath), 'utf8'));
const intent = fs.existsSync(resolvePath(intentPath)) ? JSON.parse(fs.readFileSync(resolvePath(intentPath), 'utf8')) : { intents: [] };
const hash = value => crypto.createHash('sha256').update(String(value)).digest('hex').slice(0, 20);
const entries = memory.entries || [];
const intentsByMemory = new Map((intent.intents || []).map(item => [item.sourceMemoryId, item]));
const mapStatus = entry => {
  if (entry.status === 'superseded') return 'superseded';
  if (entry.status === 'rejected') return 'rejected';
  if (entry.status === 'deferred') return 'deferred';
  if (entry.kind === 'open-question') return 'unresolved';
  return 'active';
};
const evidenceFor = entry => (entry.sourceRecords || []).length
  ? entry.sourceRecords.map((record, index) => ({ sourcePath: record.path, pointer: `/sourceRecords/${index}`, claim: record.note || 'Governed source record.' }))
  : [{ sourcePath: memoryPath, pointer: `/entries/${entries.indexOf(entry)}`, claim: 'Governed project-memory entry.' }];

const decisions = entries
  .filter(entry => ['decision', 'priority', 'constraint', 'open-question'].includes(entry.kind))
  .map(entry => {
    const linkedIntent = intentsByMemory.get(entry.memoryId);
    return {
      decisionId: `DECISION-${hash(entry.memoryId)}`,
      sourceMemoryId: entry.memoryId,
      title: entry.title,
      status: mapStatus(entry),
      chronology: { createdAt: entry.createdAt || null, updatedAt: entry.updatedAt || null, effectiveAt: entry.createdAt || null },
      decision: entry.summary,
      rationale: entry.rationale || '',
      alternatives: linkedIntent?.rejectedAlternatives || [],
      tradeoffs: linkedIntent?.tradeoffs || [],
      consequences: linkedIntent?.intendedOutcomes || [],
      supersedes: entry.supersedes || null,
      authority: entry.authority || 'unknown',
      confidence: entry.authority === 'owner-approved' || entry.authority === 'governance-record' ? 'explicit' : 'unknown',
      scopes: entry.scope || [],
      relatedIds: entry.relatedIds || [],
      evidence: evidenceFor(entry),
      advisory: true
    };
  })
  .sort((a, b) => (a.chronology.createdAt || '').localeCompare(b.chronology.createdAt || '') || a.decisionId.localeCompare(b.decisionId));

const byId = new Map(decisions.map(item => [item.sourceMemoryId, item]));
const duplicates = [];
const titleMap = new Map();
for (const decision of decisions) {
  const key = decision.title.trim().toLowerCase();
  if (titleMap.has(key)) duplicates.push({ decisionIds: [titleMap.get(key), decision.decisionId], reason: 'identical-normalized-title' });
  else titleMap.set(key, decision.decisionId);
}
const brokenSupersession = decisions.filter(item => item.supersedes && !byId.has(item.supersedes)).map(item => ({ decisionId: item.decisionId, missingSourceMemoryId: item.supersedes }));
const missingRationale = decisions.filter(item => !item.rationale.trim()).map(item => ({ decisionId: item.decisionId, reason: 'explicit-rationale-absent' }));
const stale = decisions.filter(item => item.status === 'active' && item.chronology.updatedAt && Date.parse(item.chronology.updatedAt) < Date.parse('2025-01-01T00:00:00.000Z')).map(item => ({ decisionId: item.decisionId, reason: 'active-decision-has-old-review-date' }));
const conflicts = [];
for (let i = 0; i < decisions.length; i++) for (let j = i + 1; j < decisions.length; j++) {
  const a = decisions[i], b = decisions[j];
  const shared = a.relatedIds.filter(id => b.relatedIds.includes(id));
  if (shared.length && a.status === 'active' && b.status === 'active' && a.decision !== b.decision && a.title === b.title) conflicts.push({ decisionIds: [a.decisionId, b.decisionId], sharedRelatedIds: shared, reason: 'active-decisions-share-subject-and-title-with-different-statements' });
}

const statusCounts = {};
for (const decision of decisions) statusCounts[decision.status] = (statusCounts[decision.status] || 0) + 1;
const result = {
  format: 'multiversal-aioc-decision-history',
  version: '1.0.0',
  generatedAt: new Date().toISOString(),
  sources: { projectMemory: memoryPath, designIntent: intentPath },
  policy: {
    derivationRule: 'Only explicit governed project-memory entries and linked validated design-intent fields create decision-history records.',
    unknownRule: 'Undocumented alternatives, tradeoffs, consequences, chronology, or rationale remain empty or diagnostic rather than inferred.',
    authorityRule: 'Decision history is advisory and cannot create, reverse, approve, supersede, or enforce a decision.'
  },
  summary: { totalDecisions: decisions.length, statusCounts, conflicts: conflicts.length, duplicates: duplicates.length, stale: stale.length, missingRationale: missingRationale.length, brokenSupersession: brokenSupersession.length },
  decisions,
  diagnostics: { conflicts, duplicates, stale, missingRationale, brokenSupersession }
};
fs.mkdirSync(path.dirname(resolvePath(outputPath)), { recursive: true });
fs.writeFileSync(resolvePath(outputPath), `${JSON.stringify(result, null, 2)}\n`);
console.log(`Generated ${decisions.length} decision-history records at ${outputPath}.`);
