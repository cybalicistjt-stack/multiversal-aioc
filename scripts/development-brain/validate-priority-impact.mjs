import fs from 'node:fs';
import path from 'node:path';

const file = process.argv[2] || 'governance/development-brain/priority-impact/AIOC_PRIORITY_IMPACT.generated.json';
const resolved = path.isAbsolute(file) ? file : path.join(process.cwd(), file);
const data = JSON.parse(fs.readFileSync(resolved, 'utf8'));
const issues = [];
if (data.format !== 'multiversal-aioc-priority-impact') issues.push('Invalid format.');
if (data.version !== '1.0.0') issues.push('Unsupported version.');
if (!Array.isArray(data.priorities)) issues.push('Priorities must be an array.');
const ids = new Set();
let previousScore = Infinity;
for (const [index, item] of (data.priorities || []).entries()) {
  const label = `priorities[${index}]`;
  if (!item.priorityId || ids.has(item.priorityId)) issues.push(`${label}: missing or duplicate priorityId.`);
  ids.add(item.priorityId);
  if (item.rank !== index + 1) issues.push(`${label}: rank is not deterministic.`);
  if (!Number.isInteger(item.score) || item.score < 0 || item.score > 100) issues.push(`${label}: score must be an integer from 0 to 100.`);
  if (!['critical', 'high', 'medium', 'low'].includes(item.tier)) issues.push(`${label}: invalid tier.`);
  if (item.score > previousScore) issues.push(`${label}: priorities are not sorted by descending score.`);
  previousScore = item.score;
  if (item.advisory !== true) issues.push(`${label}: advisory safeguard is required.`);
  if (!Array.isArray(item.reasons) || item.reasons.length === 0) issues.push(`${label}: reasons are required.`);
  if (!Array.isArray(item.evidence) || item.evidence.length < 4) issues.push(`${label}: complete evidence basis is required.`);
  const componentKeys = ['readinessDeficit', 'dependencyCentrality', 'blockerPropagation', 'structuralImpact', 'evidenceGap', 'governedPriority', 'unlockValue'];
  for (const key of componentKeys) if (!Number.isFinite(item.components?.[key])) issues.push(`${label}: missing component ${key}.`);
}
const summaryTotal = ['critical', 'high', 'medium', 'low'].reduce((sum, key) => sum + (data.summary?.[key] || 0), 0);
if (summaryTotal !== (data.priorities || []).length || data.summary?.totalPriorities !== summaryTotal) issues.push('Summary counts do not match priorities.');
if (!data.policy?.authorityRule?.includes('advisory')) issues.push('Authority policy must state that rankings are advisory.');
if (issues.length) {
  console.error(`Priority and Impact validation failed with ${issues.length} issue(s):`);
  for (const issue of issues) console.error(`- ${issue}`);
  process.exit(1);
}
console.log(JSON.stringify({ result: 'PASS', priorities: data.priorities.length, summary: data.summary }, null, 2));
