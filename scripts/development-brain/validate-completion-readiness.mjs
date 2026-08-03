import fs from 'node:fs';
import path from 'node:path';

const file = process.argv[2] || 'governance/development-brain/completion-readiness/AIOC_COMPLETION_READINESS.generated.json';
const target = path.isAbsolute(file) ? file : path.join(process.cwd(), file);
const data = JSON.parse(fs.readFileSync(target, 'utf8'));
const errors = [];
if (data.format !== 'multiversal-aioc-completion-readiness') errors.push('Unexpected readiness format.');
if (data.version !== '1.0.0') errors.push('Unexpected readiness version.');
if (!Array.isArray(data.objects)) errors.push('objects must be an array.');
const ids = new Set();
for (const [index, object] of (data.objects || []).entries()) {
  const label = object.stableId || index;
  if (!object.readinessId?.startsWith('READY-')) errors.push(`${label}: invalid readinessId.`);
  if (ids.has(object.readinessId)) errors.push(`${label}: duplicate readinessId.`);
  ids.add(object.readinessId);
  for (const field of ['stableId','inventoryId','name','objectType','authorityLayer','lifecycle','status']) if (object[field] == null) errors.push(`${label}: missing ${field}.`);
  if (!['canonical','working'].includes(object.authorityLayer)) errors.push(`${label}: invalid authorityLayer.`);
  if (!['ready','review-ready','blocked','incomplete'].includes(object.status)) errors.push(`${label}: invalid status.`);
  if (typeof object.score !== 'number' || object.score < 0 || object.score > 100) errors.push(`${label}: invalid score.`);
  for (const dimension of ['identity','content','evidence','structure','dependencies','governance']) {
    const score = object.scores?.[dimension];
    if (typeof score !== 'number' || score < 0 || score > 100) errors.push(`${label}: invalid ${dimension} score.`);
  }
  if (!Array.isArray(object.blockers)) errors.push(`${label}: blockers must be an array.`);
  for (const blocker of object.blockers || []) for (const field of ['code','severity','message','source']) if (!blocker[field]) errors.push(`${label}: incomplete blocker.`);
  if (!Array.isArray(object.reasons) || object.reasons.length === 0) errors.push(`${label}: reasons required.`);
  if (!Array.isArray(object.evidence) || object.evidence.length === 0) errors.push(`${label}: evidence required.`);
  for (const evidence of object.evidence || []) for (const field of ['sourcePath','pointer','claim']) if (!evidence[field]) errors.push(`${label}: incomplete evidence.`);
  if (object.promotionReady && (object.authorityLayer !== 'working' || object.blockers?.some(blocker => blocker.severity === 'critical'))) errors.push(`${label}: invalid promotionReady claim.`);
}
const counts = status => (data.objects || []).filter(object => object.status === status).length;
if (data.summary?.totalObjects !== (data.objects || []).length) errors.push('summary.totalObjects mismatch.');
if (data.summary?.ready !== counts('ready')) errors.push('summary.ready mismatch.');
if (data.summary?.reviewReady !== counts('review-ready')) errors.push('summary.reviewReady mismatch.');
if (data.summary?.blocked !== counts('blocked')) errors.push('summary.blocked mismatch.');
if (data.summary?.incomplete !== counts('incomplete')) errors.push('summary.incomplete mismatch.');
if ((data.objects || []).length < 487) errors.push('Readiness output unexpectedly contains fewer than 487 objects.');
if (errors.length) {
  console.error(`Completion readiness validation failed with ${errors.length} error(s):`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}
console.log(`Completion readiness validation passed: ${data.objects.length} objects; average ${data.summary.averageScore}.`);
