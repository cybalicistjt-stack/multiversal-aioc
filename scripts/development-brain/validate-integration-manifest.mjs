import fs from 'node:fs';
import path from 'node:path';

const file = process.argv[2] || 'governance/development-brain/integration/AIOC_INTEGRATION_MANIFEST.generated.json';
const resolved = path.isAbsolute(file) ? file : path.join(process.cwd(), file);
const data = JSON.parse(fs.readFileSync(resolved, 'utf8'));
const issues = [];

if (data.format !== 'multiversal-aioc-development-brain-integration') issues.push('Invalid format.');
if (data.version !== '1.0.0') issues.push('Unsupported version.');
if (!Array.isArray(data.artifacts) || data.artifacts.length < 8) issues.push('All Development Brain artifacts are required.');
if (!Array.isArray(data.surfaces) || data.surfaces.length !== 4) issues.push('Exactly four governed surfaces are required.');

const kinds = new Set();
const ids = new Set();
for (const [index, surface] of (data.surfaces || []).entries()) {
  const label = `surfaces[${index}]`;
  if (!surface.surfaceId || ids.has(surface.surfaceId)) issues.push(`${label}: missing or duplicate surfaceId.`);
  ids.add(surface.surfaceId);
  kinds.add(surface.kind);
  if (!['browser', 'mcp', 'rest', 'codex'].includes(surface.kind)) issues.push(`${label}: invalid kind.`);
  if (!['read-only', 'proposal-only'].includes(surface.mode)) issues.push(`${label}: invalid mode.`);
  if (!Array.isArray(surface.capabilities) || surface.capabilities.length === 0) issues.push(`${label}: capabilities required.`);
  if (surface.advisory !== true) issues.push(`${label}: advisory safeguard required.`);
  if (!surface.authority?.writes?.includes('Proposal-only')) issues.push(`${label}: proposal-only write boundary required.`);
  if (!surface.staleDetection?.staleBehavior?.includes('regeneration')) issues.push(`${label}: stale-artifact rejection required.`);
  if (!Array.isArray(surface.audit?.requiredFields) || surface.audit.requiredFields.length < 6) issues.push(`${label}: complete audit fields required.`);
}
for (const kind of ['browser', 'mcp', 'rest', 'codex']) if (!kinds.has(kind)) issues.push(`Missing ${kind} surface.`);
if ((data.surfaces || []).find(item => item.kind === 'browser')?.mode !== 'read-only') issues.push('Browser surface must be read-only in Step 9.');
if ((data.surfaces || []).filter(item => ['mcp', 'rest', 'codex'].includes(item.kind)).some(item => item.mode !== 'proposal-only')) issues.push('MCP, REST, and Codex surfaces must be proposal-only.');
if (!data.policy?.canonicalMutationRule?.includes('No integration surface')) issues.push('Canonical mutation prohibition required.');
if (!data.policy?.approvalRule?.includes('No integration surface')) issues.push('Approval substitution prohibition required.');

const expected = {
  artifactCount: data.artifacts?.length || 0,
  surfaceCount: data.surfaces?.length || 0,
  readOnlySurfaces: (data.surfaces || []).filter(item => item.mode === 'read-only').length,
  proposalOnlySurfaces: (data.surfaces || []).filter(item => item.mode === 'proposal-only').length
};
for (const [key, value] of Object.entries(expected)) if (data.summary?.[key] !== value) issues.push(`Summary mismatch for ${key}.`);

if (issues.length) {
  console.error(issues.join('\n'));
  process.exit(1);
}
console.log(`Validated ${data.surfaces.length} integration surfaces and ${data.artifacts.length} artifacts.`);
