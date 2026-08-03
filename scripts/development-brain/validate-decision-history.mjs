import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const target = process.argv[2] || 'governance/development-brain/decision-history/AIOC_DECISION_HISTORY.generated.json';
const file = path.isAbsolute(target) ? target : path.join(root, target);
if (!fs.existsSync(file)) throw new Error(`Decision history artifact missing: ${target}`);
const data = JSON.parse(fs.readFileSync(file, 'utf8'));
const errors = [];
if (data.format !== 'multiversal-aioc-decision-history') errors.push('Unexpected format.');
if (data.version !== '1.0.0') errors.push('Unexpected version.');
if (!Array.isArray(data.decisions)) errors.push('decisions must be an array.');
if (!data.diagnostics || typeof data.diagnostics !== 'object') errors.push('diagnostics must be present.');
const ids = new Set();
for (const [index, item] of (data.decisions || []).entries()) {
  if (!/^DECISION-/.test(item.decisionId || '')) errors.push(`Decision ${index} has invalid decisionId.`);
  if (ids.has(item.decisionId)) errors.push(`Duplicate decisionId ${item.decisionId}.`);
  ids.add(item.decisionId);
  if (!['active','superseded','rejected','deferred','unresolved'].includes(item.status)) errors.push(`Decision ${item.decisionId} has invalid status.`);
  if (!item.decision || !item.title || !item.sourceMemoryId) errors.push(`Decision ${item.decisionId} lacks required source fields.`);
  if (!Array.isArray(item.evidence) || item.evidence.length === 0) errors.push(`Decision ${item.decisionId} lacks evidence.`);
  if (item.advisory !== true) errors.push(`Decision ${item.decisionId} must remain advisory.`);
}
if (!String(data.policy?.unknownRule || '').includes('rather than inferred')) errors.push('Unknown-information safeguard missing.');
if (!String(data.policy?.authorityRule || '').includes('cannot')) errors.push('Authority safeguard missing.');
if (errors.length) {
  console.error(errors.join('\n'));
  process.exit(1);
}
console.log(`Validated ${data.decisions.length} decision-history records.`);
