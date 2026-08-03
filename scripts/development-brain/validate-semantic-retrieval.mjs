import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const input = process.argv[2] || 'governance/development-brain/semantic-retrieval/AIOC_SEMANTIC_RETRIEVAL.generated.json';
const file = path.isAbsolute(input) ? input : path.join(root, input);
if (!fs.existsSync(file)) throw new Error(`Semantic retrieval artifact missing: ${input}`);
const data = JSON.parse(fs.readFileSync(file, 'utf8'));
const errors = [];
const requiredCategories = new Set(['source-fact','derived-finding','recommendation','constraint','unresolved-question']);
if (data.format !== 'multiversal-aioc-semantic-retrieval') errors.push('Invalid format.');
if (data.version !== '1.0.0') errors.push('Invalid version.');
if (!Array.isArray(data.packages)) errors.push('packages must be an array.');
const packageIds = new Set();
for (const pkg of data.packages || []) {
  if (!pkg.packageId?.startsWith('CONTEXT-')) errors.push(`Invalid packageId: ${pkg.packageId}`);
  if (packageIds.has(pkg.packageId)) errors.push(`Duplicate packageId: ${pkg.packageId}`);
  packageIds.add(pkg.packageId);
  if (!pkg.subject?.startsWith('ENTITY-')) errors.push(`${pkg.packageId} has invalid subject.`);
  if (pkg.authority !== 'read-only-context' || pkg.advisory !== true) errors.push(`${pkg.packageId} violates authority safeguards.`);
  if (pkg.freshness?.status !== 'current' || !pkg.freshness?.sourceFingerprint) errors.push(`${pkg.packageId} lacks current freshness evidence.`);
  const budget = pkg.budget || {};
  if ((pkg.items || []).length !== budget.usedItems) errors.push(`${pkg.packageId} usedItems mismatch.`);
  if (budget.usedItems > budget.maxItems) errors.push(`${pkg.packageId} exceeds item budget.`);
  if (budget.usedCharacters > budget.maxCharacters) errors.push(`${pkg.packageId} exceeds character budget.`);
  const itemIds = new Set();
  let priorScore = Infinity;
  for (const [index, item] of (pkg.items || []).entries()) {
    if (!item.contextItemId?.startsWith('CTXITEM-')) errors.push(`${pkg.packageId} has invalid context item ID.`);
    if (itemIds.has(item.contextItemId)) errors.push(`${pkg.packageId} contains duplicate item ${item.contextItemId}.`);
    itemIds.add(item.contextItemId);
    if (!requiredCategories.has(item.category)) errors.push(`${item.contextItemId} has invalid category.`);
    if (item.rank !== index + 1) errors.push(`${item.contextItemId} rank is not deterministic.`);
    if (item.score > priorScore) errors.push(`${pkg.packageId} items are not score ordered.`);
    priorScore = item.score;
    if (!item.statement || !Array.isArray(item.sourceEvidence) || item.sourceEvidence.length === 0) errors.push(`${item.contextItemId} lacks statement or evidence.`);
    if (item.freshness !== 'current' || item.advisory !== true) errors.push(`${item.contextItemId} violates freshness or advisory policy.`);
  }
}
if ((data.diagnostics?.duplicateItems || []).length) errors.push('Duplicate context items detected.');
if ((data.diagnostics?.stalePackages || []).length) errors.push('Stale context packages detected.');
if (data.summary?.totalPackages !== (data.packages || []).length) errors.push('summary.totalPackages mismatch.');
if (data.summary?.totalItems !== (data.packages || []).reduce((n,p) => n + (p.items || []).length, 0)) errors.push('summary.totalItems mismatch.');
if (errors.length) {
  console.error(errors.map(error => `- ${error}`).join('\n'));
  process.exit(1);
}
console.log(`Validated ${data.packages.length} semantic reasoning-context packages with ${data.summary.totalItems} items.`);
