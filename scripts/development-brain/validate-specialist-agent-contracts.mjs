import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const artifactPath = process.argv[2] || 'governance/development-brain/specialist-agents/AIOC_SPECIALIST_AGENT_CONTRACTS.generated.json';
const resolvePath = value => path.isAbsolute(value) ? value : path.join(root, value);
const fail = message => { console.error(`Specialist contract validation failed: ${message}`); process.exit(1); };
if (!fs.existsSync(resolvePath(artifactPath))) fail(`missing artifact ${artifactPath}`);
const data = JSON.parse(fs.readFileSync(resolvePath(artifactPath), 'utf8'));
if (data.format !== 'multiversal-aioc-specialist-agent-contracts') fail('unexpected format');
if (!Array.isArray(data.contracts) || data.contracts.length < 1) fail('contracts are required');
if (!Array.isArray(data.handoffs)) fail('handoffs are required');
const contractIds = new Set();
const roleIds = new Set();
for (const contract of data.contracts) {
  if (!contract.contractId?.startsWith('AGENT-CONTRACT-')) fail('invalid contractId');
  if (!contract.roleId?.startsWith('AGENT-ROLE-')) fail(`invalid roleId for ${contract.contractId}`);
  if (contractIds.has(contract.contractId)) fail(`duplicate contractId ${contract.contractId}`);
  if (roleIds.has(contract.roleId)) fail(`duplicate roleId ${contract.roleId}`);
  contractIds.add(contract.contractId); roleIds.add(contract.roleId);
  for (const field of ['domainScope','responsibilities','requiredInputs','permittedOutputs','evidenceRequirements','escalationTriggers','handoffRequirements','prohibitedActions']) {
    if (!Array.isArray(contract[field]) || contract[field].length === 0) fail(`${contract.contractId} missing ${field}`);
  }
  if (!['read-only','advisory','proposal-only'].includes(contract.authorityMode)) fail(`${contract.contractId} has unsupported authority mode`);
  const prohibited = contract.prohibitedActions.join(' ').toLowerCase();
  for (const term of ['canonical content','approval','authority']) if (!prohibited.includes(term)) fail(`${contract.contractId} lacks ${term} prohibition`);
}
const handoffIds = new Set();
for (const handoff of data.handoffs) {
  if (handoffIds.has(handoff.handoffId)) fail(`duplicate handoff ${handoff.handoffId}`);
  handoffIds.add(handoff.handoffId);
  if (!roleIds.has(handoff.fromRoleId) || !roleIds.has(handoff.toRoleId)) fail(`${handoff.handoffId} references unknown role`);
  if (handoff.fromRoleId === handoff.toRoleId) fail(`${handoff.handoffId} is a self handoff`);
  if (handoff.authorityPreserved !== true) fail(`${handoff.handoffId} does not preserve authority`);
  if (!Array.isArray(handoff.requiredPayload) || handoff.requiredPayload.length === 0) fail(`${handoff.handoffId} lacks payload contract`);
}
for (const key of ['roleOverlaps','missingCapabilities','circularHandoffs','unsupportedSpecializations','authorityConflicts']) if (!Array.isArray(data.diagnostics?.[key])) fail(`missing diagnostic ${key}`);
if (data.diagnostics.missingCapabilities.length) fail('required specialist capabilities are missing');
if (data.diagnostics.circularHandoffs.length) fail('circular handoffs detected');
if (data.diagnostics.unsupportedSpecializations.length) fail('unsupported specializations detected');
if (data.diagnostics.authorityConflicts.length) fail('authority conflicts detected');
if (data.authority?.advisoryOnly !== true || data.authority?.canonicalMutationAllowed !== false || data.authority?.approvalGranted !== false || data.authority?.certificationAllowed !== false) fail('authority safeguard invalid');
console.log(`Validated ${data.contracts.length} specialist contracts and ${data.handoffs.length} handoffs.`);
