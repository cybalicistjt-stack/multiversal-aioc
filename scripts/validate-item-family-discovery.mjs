import fs from 'node:fs';

const root = 'governance/object-system/item-discovery';
const inventory = JSON.parse(fs.readFileSync(`${root}/ITEM_SOURCE_INVENTORY.json`, 'utf8'));
const discovery = fs.readFileSync(`${root}/ITEM_FAMILY_DISCOVERY.md`, 'utf8');
const failures = [];

if (inventory.format !== 'multiversal-item-source-inventory') failures.push('unsupported inventory format');
if (inventory.workstream !== '8E-009A') failures.push('wrong workstream');
if (inventory.sourceCount !== inventory.sources.length) failures.push('source count mismatch');
if (inventory.sources.reduce((total, source) => total + source.pages, 0) !== inventory.totalPages) failures.push('page total mismatch');
if (inventory.sourceCount !== 13 || inventory.totalPages !== 218) failures.push('authoritative bundle totals changed');

const sourceFiles = new Set();
for (const source of inventory.sources) {
  if (!source.id || !source.file || !source.pages) failures.push(`incomplete source record: ${source.id ?? 'unknown'}`);
  if (!source.primaryDomains?.length) failures.push(`${source.id}: no primary domains`);
  if (!source.explicitFamilies?.length) failures.push(`${source.id}: no explicit families`);
  if (!source.keyParameters?.length) failures.push(`${source.id}: no key parameters`);
  if (sourceFiles.has(source.file)) failures.push(`duplicate source file: ${source.file}`);
  sourceFiles.add(source.file);
}

for (const required of [
  'Normalized item-family hierarchy',
  'Full parameter matrix by major family',
  'Shared capability-module candidates',
  'Object/non-object boundary decisions',
  'Ambiguity queue',
  'Source coverage'
]) {
  if (!discovery.includes(required)) failures.push(`missing discovery section: ${required}`);
}

for (const boundary of ['Clones and inactive clone bodies are artificial beings, not items', 'Physical item type and magitech discipline are separate classifications']) {
  if (!discovery.includes(boundary)) failures.push(`missing required boundary: ${boundary}`);
}

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}

console.log(`Item family discovery validated: ${inventory.sourceCount} sources, ${inventory.totalPages} pages.`);
