import fs from 'node:fs';

const templates = JSON.parse(fs.readFileSync('governance/object-system/item-templates/ITEM_TEMPLATE_REGISTRY.json', 'utf8'));
const forms = JSON.parse(fs.readFileSync('governance/object-system/item-design-studio/ITEM_DESIGN_STUDIO_FORM_REGISTRY.json', 'utf8'));
const examples = JSON.parse(fs.readFileSync('governance/object-system/item-examples/ITEM_REPRESENTATIVE_OBJECT_PLAN.json', 'utf8'));
const failures = [];

const templateIds = new Set(templates.templates.map(entry => entry.templateId));
const formIds = new Set(forms.forms.map(entry => entry.templateId));
const exampleIds = new Set(examples.plannedExamples.map(entry => entry.templateId));

if (forms.format !== 'multiversal-item-design-studio-form-registry') failures.push('unsupported form registry format');
if (forms.workstream !== '8E-009K') failures.push('wrong form workstream');
if (examples.format !== 'multiversal-item-representative-object-plan') failures.push('unsupported example plan format');
if (examples.workstream !== '8E-009L') failures.push('wrong example workstream');

for (const id of templateIds) {
  if (!formIds.has(id)) failures.push(`missing form for ${id}`);
  if (!exampleIds.has(id)) failures.push(`missing representative object plan for ${id}`);
}
for (const form of forms.forms) {
  if (!templateIds.has(form.templateId)) failures.push(`form references unknown template ${form.templateId}`);
  if (!form.sections?.includes('provenance') || !form.sections?.includes('governance')) failures.push(`${form.templateId}: provenance or governance section missing`);
}
for (const example of examples.plannedExamples) {
  if (!templateIds.has(example.templateId)) failures.push(`example plan references unknown template ${example.templateId}`);
  if (example.selectionState !== 'pending-exact-source-extraction') failures.push(`${example.templateId}: unsupported example completion claim`);
}
if (!forms.globalBehavior?.unresolvedValuesNeverDefaulted) failures.push('unresolved default prohibition missing');
if (!examples.rule?.includes('not invented')) failures.push('source-grounding rule missing');
if (!examples.promotionBoundary?.includes('No planned example is certified')) failures.push('promotion boundary missing');

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log(`Item Design Studio forms and representative-object plans validated: ${formIds.size} templates.`);
