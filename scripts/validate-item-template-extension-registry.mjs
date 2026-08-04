import fs from 'node:fs';

const path = 'governance/object-system/item-templates/ITEM_TEMPLATE_EXTENSION_REGISTRY.json';
const registry = JSON.parse(fs.readFileSync(path, 'utf8'));
const failures = [];

if (registry.format !== 'multiversal-item-template-extension-registry') failures.push('unsupported registry format');
if (registry.workstream !== '8E-009L4') failures.push('wrong workstream');
if (!Array.isArray(registry.templates) || registry.templates.length !== 9) failures.push('expected exactly nine template extensions');

const expected = new Set([
  'item.weapon.ranged','item.weapon.energy','item.ammunition','item.implant',
  'item.modification.module','item.tool','item.device.general','item.trap','item.software'
]);
const requiredKeys = [
  'templateId','displayName','parentFamily','requiredFields','optionalFields',
  'allowedCapabilityModules','allowedSubtypes','compatibleModifications',
  'sourceSupportedParameters','validationRules','designStudioSections',
  'runtimeBehaviors','knownAmbiguities','exampleObjectRequired'
];
const seen = new Set();
for (const template of registry.templates ?? []) {
  for (const key of requiredKeys) if (!(key in template)) failures.push(`${template.templateId ?? 'unknown'} missing ${key}`);
  if (seen.has(template.templateId)) failures.push(`duplicate templateId ${template.templateId}`);
  seen.add(template.templateId);
  if (!expected.has(template.templateId)) failures.push(`unexpected template ${template.templateId}`);
  if (!template.requiredFields?.includes('identity')) failures.push(`${template.templateId} missing identity`);
  if (!template.requiredFields?.includes('provenance')) failures.push(`${template.templateId} missing provenance`);
  if (!template.allowedCapabilityModules?.includes('universal-envelope')) failures.push(`${template.templateId} missing universal envelope`);
  if (!template.sourceSupportedParameters?.length) failures.push(`${template.templateId} missing source parameters`);
  if (!template.validationRules?.length) failures.push(`${template.templateId} missing validation rules`);
  if (!template.designStudioSections?.length) failures.push(`${template.templateId} missing Design Studio sections`);
  if (!template.runtimeBehaviors?.length) failures.push(`${template.templateId} missing runtime behaviors`);
  if (template.exampleObjectRequired !== true) failures.push(`${template.templateId} must require representative example`);
}
for (const id of expected) if (!seen.has(id)) failures.push(`missing template ${id}`);
if (!registry.promotionBoundary?.includes('do not authorize bulk conversion')) failures.push('promotion boundary missing');

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log(`Item template extension registry validated: ${registry.templates.length} templates.`);
