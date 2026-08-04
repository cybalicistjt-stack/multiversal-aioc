import fs from 'node:fs';

const path = 'governance/object-system/item-templates/ITEM_TEMPLATE_REGISTRY.json';
const registry = JSON.parse(fs.readFileSync(path, 'utf8'));
const failures = [];

if (registry.format !== 'multiversal-item-template-registry') failures.push('unsupported registry format');
if (registry.workstream !== '8E-009D') failures.push('wrong workstream');
if (!Array.isArray(registry.templates) || registry.templates.length < 10) failures.push('insufficient template coverage');

const ids = new Set();
const requiredKeys = [
  'templateId','displayName','parentFamily','requiredFields','optionalFields',
  'allowedCapabilityModules','allowedSubtypes','compatibleModifications',
  'sourceSupportedParameters','validationRules','designStudioSections',
  'runtimeBehaviors','knownAmbiguities','exampleObjectRequired'
];

for (const template of registry.templates ?? []) {
  for (const key of requiredKeys) {
    if (!(key in template)) failures.push(`${template.templateId ?? 'unknown'} missing ${key}`);
  }
  if (ids.has(template.templateId)) failures.push(`duplicate templateId ${template.templateId}`);
  ids.add(template.templateId);
  if (!template.requiredFields?.includes('identity')) failures.push(`${template.templateId} missing identity requirement`);
  if (!template.requiredFields?.includes('provenance')) failures.push(`${template.templateId} missing provenance requirement`);
  if (!template.allowedCapabilityModules?.includes('universal-envelope')) failures.push(`${template.templateId} missing universal envelope`);
  if (!template.sourceSupportedParameters?.length) failures.push(`${template.templateId} has no source-supported parameters`);
  if (!template.validationRules?.length) failures.push(`${template.templateId} has no validation rules`);
  if (!template.designStudioSections?.length) failures.push(`${template.templateId} has no Design Studio sections`);
  if (!template.runtimeBehaviors?.length) failures.push(`${template.templateId} has no runtime behaviors`);
  if (template.exampleObjectRequired !== true) failures.push(`${template.templateId} does not require an example object`);
}

for (const requiredTemplate of [
  'item.weapon.melee','item.weapon.firearm','item.protection.armor','item.protection.eva-suit',
  'item.storage.typed-container','item.consumable.effect-delivery','item.device.computer',
  'item.magic.implement','item.living.sentient-companion','item.living.symbiote',
  'item.material.crafting-resource'
]) {
  if (!ids.has(requiredTemplate)) failures.push(`missing required template ${requiredTemplate}`);
}

const storage = registry.templates.find(t => t.templateId === 'item.storage.typed-container');
if (!storage?.validationRules?.some(rule => rule.includes('never interchangeable'))) failures.push('typed storage distinction missing');
if (!registry.safetyBoundary?.includes('does not authorize bulk conversion')) failures.push('safety boundary missing');

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}

console.log(`Item template registry validated: ${registry.templates.length} canonical templates.`);
