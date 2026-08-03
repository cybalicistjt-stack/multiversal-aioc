import fs from 'node:fs';
import path from 'node:path';

const file = process.argv[2] || 'governance/development-brain/recommendation-planner/AIOC_RECOMMENDATION_PLANNER.generated.json';
const resolved = path.isAbsolute(file) ? file : path.join(process.cwd(), file);
const data = JSON.parse(fs.readFileSync(resolved, 'utf8'));
const issues = [];
if (data.format !== 'multiversal-aioc-recommendation-planner') issues.push('Invalid format.');
if (data.version !== '1.0.0') issues.push('Unsupported version.');
if (!Array.isArray(data.recommendations)) issues.push('Recommendations must be an array.');
const ids = new Set();
const stableIds = new Set();
let previousRank = 0;
for (const [index, item] of (data.recommendations || []).entries()) {
  const label = `recommendations[${index}]`;
  if (!item.recommendationId || ids.has(item.recommendationId)) issues.push(`${label}: missing or duplicate recommendationId.`);
  ids.add(item.recommendationId);
  if (!item.stableId || stableIds.has(item.stableId)) issues.push(`${label}: missing or duplicate stableId.`);
  stableIds.add(item.stableId);
  if (item.rank !== previousRank + 1) issues.push(`${label}: rank must be contiguous and deterministic.`);
  previousRank = item.rank;
  if (!['executable', 'owner-decision', 'blocked', 'observation-only'].includes(item.classification)) issues.push(`${label}: invalid classification.`);
  if (!Array.isArray(item.rationale) || !item.rationale.length) issues.push(`${label}: rationale is required.`);
  if (!Array.isArray(item.prerequisites)) issues.push(`${label}: prerequisites must be an array.`);
  if (!Array.isArray(item.tasks) || !item.tasks.length) issues.push(`${label}: at least one bounded task is required.`);
  if (!Array.isArray(item.evidence) || !item.evidence.length) issues.push(`${label}: evidence is required.`);
  if (item.advisory !== true) issues.push(`${label}: advisory safeguard must be true.`);
  for (const task of item.tasks || []) {
    if (!task.taskId || !Number.isInteger(task.sequence) || !task.action || !task.boundedOutcome) issues.push(`${label}: invalid task record.`);
    if (item.classification !== 'executable' && task.executionAllowed !== false) issues.push(`${label}: non-executable classification cannot allow execution.`);
  }
}
const summary = data.summary || {};
const count = classification => (data.recommendations || []).filter(item => item.classification === classification).length;
if (summary.totalRecommendations !== (data.recommendations || []).length) issues.push('Summary totalRecommendations mismatch.');
if (summary.executable !== count('executable')) issues.push('Summary executable mismatch.');
if (summary.ownerDecision !== count('owner-decision')) issues.push('Summary ownerDecision mismatch.');
if (summary.blocked !== count('blocked')) issues.push('Summary blocked mismatch.');
if (summary.observationOnly !== count('observation-only')) issues.push('Summary observationOnly mismatch.');
if (!String(data.policy?.authorityRule || '').includes('advisory')) issues.push('Policy must preserve advisory authority boundaries.');
if (issues.length) {
  console.error(`Recommendation planner validation failed with ${issues.length} issue(s):`);
  for (const issue of issues) console.error(`- ${issue}`);
  process.exit(1);
}
console.log(JSON.stringify({ result: 'PASS', recommendations: data.recommendations.length, summary }, null, 2));
