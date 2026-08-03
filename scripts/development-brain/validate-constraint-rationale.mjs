import fs from 'node:fs';
import path from 'node:path';
const root = process.cwd();
const file = process.argv[2] || 'governance/development-brain/constraint-rationale/AIOC_CONSTRAINT_RATIONALE.generated.json';
const data = JSON.parse(fs.readFileSync(path.isAbsolute(file) ? file : path.join(root, file), 'utf8'));
const errors = [];
if (data.format !== 'multiversal-aioc-constraint-rationale') errors.push('Unexpected format.');
if (data.version !== '1.0.0') errors.push('Unexpected version.');
if (data.authority !== 'advisory-derived') errors.push('Authority must remain advisory-derived.');
if (!Array.isArray(data.records)) errors.push('records must be an array.');
const ids = new Set();
for (const record of data.records || []) {
  if (!record.reasoningId || ids.has(record.reasoningId)) errors.push(`Invalid or duplicate reasoningId: ${record.reasoningId}`);
  ids.add(record.reasoningId);
  if (!record.subject) errors.push(`${record.reasoningId} lacks subject.`);
  if (!Array.isArray(record.constraints) || !record.constraints.length) errors.push(`${record.reasoningId} lacks explicit constraints.`);
  if (!Array.isArray(record.rationaleChain)) errors.push(`${record.reasoningId} lacks rationaleChain.`);
  if (!Array.isArray(record.conclusions)) errors.push(`${record.reasoningId} lacks conclusions.`);
  if (!Array.isArray(record.evidence)) errors.push(`${record.reasoningId} lacks evidence array.`);
  if (record.advisory !== true) errors.push(`${record.reasoningId} must remain advisory.`);
}
if (!data.diagnostics || typeof data.diagnostics !== 'object') errors.push('diagnostics are required.');
if (errors.length) { console.error(errors.join('\n')); process.exit(1); }
console.log(`Validated ${data.records.length} constraint and rationale reasoning records.`);
