import fs from 'node:fs';

const path = 'governance/object-system/item-examples/objects/LASER_ASSAULT_RIFLE.visual-source-extraction.json';
const object = JSON.parse(fs.readFileSync(path, 'utf8'));
const failures = [];

if (object.identity?.templateId !== 'item.weapon.firearm') failures.push('wrong template');
if (object.identity?.displayName !== 'Laser Assault Rifle') failures.push('wrong object');
if (object.provenance?.inspectionMethod !== 'rendered-page visual review') failures.push('visual inspection evidence missing');
if (object.weaponProfile?.damageDice !== '1d10' || object.weaponProfile?.damageType !== 'Radiant') failures.push('damage mismatch');
if (object.weaponProfile?.normalRange?.value !== 80 || object.weaponProfile?.longRange?.value !== 320) failures.push('range mismatch');
if (object.physicalProperties?.weight?.value !== 8) failures.push('weight mismatch');
if (object.economy?.cost?.value !== 1200) failures.push('cost mismatch');
const capacity = object.firearmOperation?.capacity;
if (capacity?.standard !== 40 || capacity?.extendedClip !== 60 || capacity?.highCapacityMagazine !== 80 || capacity?.unit !== 'charges') failures.push('capacity mismatch');
if (!object.firearmOperation?.fireModes?.some(mode => mode.name === 'Burst Fire')) failures.push('Burst Fire missing');
if (!object.firearmOperation?.specialRules?.some(rule => rule.name === 'Rapid Reload' && rule.state === 'named-in-table-definition-not-located')) failures.push('Rapid Reload ambiguity not preserved');
if (object.validationState?.promotionReady !== false || object.validationState?.ownerApproved !== false) failures.push('unsupported completion claim');
if (!object.unresolvedFields?.length) failures.push('unresolved fields missing');

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log('Visually sourced Laser Assault Rifle example validated.');
