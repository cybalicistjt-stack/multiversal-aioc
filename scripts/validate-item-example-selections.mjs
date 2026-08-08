import fs from 'node:fs';

const registry = JSON.parse(fs.readFileSync('governance/object-system/item-templates/ITEM_TEMPLATE_REGISTRY.json', 'utf8'));
const selections = JSON.parse(fs.readFileSync('governance/object-system/item-examples/ITEM_REPRESENTATIVE_OBJECT_SELECTIONS.json', 'utf8'));
const failures = [];

if (selections.format !== 'multiversal-item-representative-object-selections') failures.push('unsupported selection format');
if (selections.workstream !== '8E-009L') failures.push('wrong workstream');
const templateIds = new Set(registry.templates.map(entry => entry.templateId));
const selectedIds = new Set(selections.selections.map(entry => entry.templateId));
if (selectedIds.size !== selections.selections.length) failures.push('duplicate template selection');
for (const id of templateIds) if (!selectedIds.has(id)) failures.push(`missing selection for ${id}`);
for (const entry of selections.selections) {
  if (!templateIds.has(entry.templateId)) failures.push(`unknown template ${entry.templateId}`);
  if (!entry.sourceDocument || !Number.isInteger(entry.sourcePage) || entry.sourcePage < 1) failures.push(`${entry.templateId}: invalid source location`);
  if (!entry.sourceObjectName || !entry.reason) failures.push(`${entry.templateId}: incomplete selection evidence`);
  if (!['selected-for-extraction','selected-class-example','visually-verified-partial-extraction'].includes(entry.selectionState)) failures.push(`${entry.templateId}: unsupported selection state`);
}
const firearm = selections.selections.find(entry => entry.templateId === 'item.weapon.firearm');
if (!firearm || firearm.sourceDocument !== 'Guns 11-8-24.PDF' || firearm.selectionState !== 'visually-verified-partial-extraction') failures.push('visually verified firearm selection missing');
if (!selections.knownLimitations?.some(value => value.includes('visual') || value.includes('rendered'))) failures.push('visual firearm review limitation missing');
if (!selections.knownLimitations?.some(value => value.includes('does not mean complete'))) failures.push('completion boundary missing');
if (!selections.nextAction?.includes('field-level provenance')) failures.push('next action must require field-level provenance');

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log(`Representative item selections validated: ${selections.selections.length} templates.`);
