import fs from 'node:fs';

const memoryPath = 'governance/development-brain/memory/AIOC_PROJECT_MEMORY.json';
const memory = JSON.parse(fs.readFileSync(memoryPath, 'utf8'));
const allowedKinds = new Set(['decision', 'constraint', 'priority', 'technical-debt', 'open-question', 'investigation', 'assumption', 'lesson']);
const allowedStatuses = new Set(['active', 'resolved', 'superseded', 'retired']);
const allowedAuthorities = new Set(['owner-approved', 'governance-record', 'validated-inference', 'working-hypothesis']);
const issues = [];

if (memory.format !== 'multiversal-aioc-project-memory') issues.push('Invalid memory format.');
if (memory.version !== '1.0.0') issues.push('Unsupported memory version.');
if (!Number.isInteger(memory.revision) || memory.revision < 0) issues.push('Revision must be a non-negative integer.');
if (!Array.isArray(memory.entries)) issues.push('Entries must be an array.');

const ids = new Set();
for (const [index, entry] of (memory.entries || []).entries()) {
  const label = `entry[${index}]`;
  if (!/^AIOC-MEM-\d{4,}$/.test(entry.memoryId || '')) issues.push(`${label}: invalid memoryId.`);
  if (ids.has(entry.memoryId)) issues.push(`${label}: duplicate memoryId ${entry.memoryId}.`);
  ids.add(entry.memoryId);
  if (!allowedKinds.has(entry.kind)) issues.push(`${label}: invalid kind ${entry.kind}.`);
  if (!allowedStatuses.has(entry.status)) issues.push(`${label}: invalid status ${entry.status}.`);
  if (!allowedAuthorities.has(entry.authority)) issues.push(`${label}: invalid authority ${entry.authority}.`);
  if (!entry.title || entry.title.length < 3) issues.push(`${label}: title is required.`);
  if (!entry.summary || entry.summary.length < 10) issues.push(`${label}: summary is required.`);
  if (!entry.createdAt || Number.isNaN(Date.parse(entry.createdAt))) issues.push(`${label}: invalid createdAt.`);
  if (!entry.updatedAt || Number.isNaN(Date.parse(entry.updatedAt))) issues.push(`${label}: invalid updatedAt.`);
  if (!Array.isArray(entry.sourceRecords) || entry.sourceRecords.length === 0) issues.push(`${label}: at least one source record is required.`);
  for (const source of entry.sourceRecords || []) {
    if (!source.path || typeof source.path !== 'string') issues.push(`${label}: source record path is required.`);
  }
  if (entry.status === 'resolved' && !entry.resolution) issues.push(`${label}: resolved entries require a resolution.`);
  if (entry.status === 'superseded' && !entry.supersedes) issues.push(`${label}: superseded entries require a supersedes reference.`);
}

if (issues.length) {
  console.error(`Development Brain memory validation failed with ${issues.length} issue(s):`);
  for (const issue of issues) console.error(`- ${issue}`);
  process.exit(1);
}

const counts = Object.fromEntries([...allowedKinds].map(kind => [kind, memory.entries.filter(entry => entry.kind === kind).length]));
console.log(JSON.stringify({ result: 'PASS', revision: memory.revision, entries: memory.entries.length, counts }, null, 2));
