import fs from 'node:fs';

const root = 'governance/object-system/item-registry';
const hierarchy = JSON.parse(fs.readFileSync(`${root}/ITEM_TYPE_HIERARCHY.json`, 'utf8'));
const registry = JSON.parse(fs.readFileSync(`${root}/ITEM_CAPABILITY_MODULE_REGISTRY.json`, 'utf8'));
const failures = [];

if (hierarchy.format !== 'multiversal-item-type-hierarchy') failures.push('unsupported hierarchy format');
if (registry.format !== 'multiversal-item-capability-module-registry') failures.push('unsupported module registry format');
if (!hierarchy.workstreams?.includes('8E-009B')) failures.push('hierarchy workstream missing');
if (!registry.workstreams?.includes('8E-009C')) failures.push('module workstream missing');

const familyIds = new Set(hierarchy.families.map(f => f.id));
if (familyIds.size !== hierarchy.families.length) failures.push('duplicate family ids');
for (const family of hierarchy.families) {
  if (!family.id || !family.children?.length) failures.push(`incomplete family ${family.id ?? 'unknown'}`);
}

const moduleIds = new Set(registry.modules.map(m => m.id));
if (moduleIds.size !== registry.modules.length) failures.push('duplicate module ids');
for (const module of registry.modules) {
  if (!module.id || !module.fields?.length) failures.push(`incomplete module ${module.id ?? 'unknown'}`);
  if (new Set(module.fields).size !== module.fields.length) failures.push(`${module.id}: duplicate fields`);
}

for (const required of ['cap.identity-governance','cap.weapon-profile','cap.protection','cap.typed-storage','cap.charges','cap.modular-host','cap.environmental-protection','cap.computer-core','cap.spell-implement','cap.sentience-autonomy','cap.bonding-host','cap.progression-evolution','cap.material-properties','cap.magitech-discipline']) {
  if (!moduleIds.has(required)) failures.push(`missing required module: ${required}`);
}

for (const boundary of ['Clones and inactive clone bodies are artificial beings, not items.','Services, facilities, actions, effects, conditions, checks, and failure tables are not item types.']) {
  if (!hierarchy.boundaryRules.includes(boundary)) failures.push(`missing boundary: ${boundary}`);
}

if (!registry.knownNonInterchangeableConcepts.some(group => group.includes('weightCapacity') && group.includes('soulCapacity'))) failures.push('typed capacity distinction missing');
if (!registry.knownNonInterchangeableConcepts.some(group => group.includes('physicalType') && group.includes('magitechDiscipline'))) failures.push('physical/discipline distinction missing');

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}

console.log(`Item hierarchy and capability modules validated: ${hierarchy.families.length} families, ${registry.modules.length} modules.`);
