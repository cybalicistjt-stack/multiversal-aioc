import fs from 'node:fs';
import path from 'node:path';

const file = process.argv[2] || 'governance/development-brain/verification-governance/AIOC_VERIFICATION_GOVERNANCE.generated.json';
const resolved = path.isAbsolute(file) ? file : path.join(process.cwd(), file);
const data = JSON.parse(fs.readFileSync(resolved, 'utf8'));
const issues = [];
if (data.format !== 'multiversal-aioc-verification-governance') issues.push('Invalid format.');
if (data.version !== '1.0.0') issues.push('Unsupported version.');
if (!Array.isArray(data.verifications)) issues.push('Verifications must be an array.');
const ids = new Set();
for (const [index, item] of (data.verifications || []).entries()) {
  const label = `verifications[${index}]`;
  if (!item.verificationId || ids.has(item.verificationId)) issues.push(`${label}: missing or duplicate verificationId.`);
  ids.add(item.verificationId);
  if (item.rank !== index + 1) issues.push(`${label}: deterministic rank mismatch.`);
  if (!['verified-executable', 'requires-approval', 'blocked', 'observation-only'].includes(item.status)) issues.push(`${label}: invalid status.`);
  if (!Array.isArray(item.checks) || item.checks.length < 6) issues.push(`${label}: complete verification checks are required.`);
  if (!Array.isArray(item.evidence) || item.evidence.length < 3) issues.push(`${label}: complete evidence is required.`);
  if (item.advisory !== true) issues.push(`${label}: advisory safeguard is required.`);
  if (item.status === 'requires-approval' && item.approval?.required !== true) issues.push(`${label}: approval-required status must require approval.`);
  if (item.status === 'verified-executable' && item.approval?.granted === true) issues.push(`${label}: verification must not grant approval.`);
  if (item.status === 'verified-executable' && item.checks.some(check => check.passed !== true)) issues.push(`${label}: verified-executable requires all checks to pass.`);
  if (item.sourceClassification === 'observation-only' && item.status !== 'observation-only') issues.push(`${label}: observation classification mismatch.`);
}
const counts = {
  total: data.verifications?.length || 0,
  verifiedExecutable: (data.verifications || []).filter(item => item.status === 'verified-executable').length,
  requiresApproval: (data.verifications || []).filter(item => item.status === 'requires-approval').length,
  blocked: (data.verifications || []).filter(item => item.status === 'blocked').length,
  observationOnly: (data.verifications || []).filter(item => item.status === 'observation-only').length
};
for (const [key, value] of Object.entries(counts)) if (data.summary?.[key] !== value) issues.push(`Summary mismatch for ${key}.`);
if (!String(data.policy?.authorityRule || '').includes('never execute')) issues.push('Authority rule must prohibit execution and mutation.');
if (issues.length) {
  console.error(`Verification governance validation failed with ${issues.length} issue(s):`);
  for (const issue of issues) console.error(`- ${issue}`);
  process.exit(1);
}
console.log(JSON.stringify({ result: 'PASS', ...counts }, null, 2));
