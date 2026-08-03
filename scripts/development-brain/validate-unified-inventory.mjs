import fs from 'node:fs';

const inventoryPath = process.argv[2] || 'governance/development-brain/inventory/AIOC_UNIFIED_INVENTORY.generated.json';
const inventory = JSON.parse(fs.readFileSync(inventoryPath, 'utf8'));
const errors = [];

if (inventory.format !== 'multiversal-aioc-unified-inventory') errors.push('Unexpected inventory format.');
if (inventory.version !== '1.0.0') errors.push('Unexpected inventory version.');
if (!Array.isArray(inventory.objects)) errors.push('Inventory objects must be an array.');

const ids = new Set();
const inventoryIds = new Set();
for (const [index, object] of (inventory.objects || []).entries()) {
  if (!object.stableId) errors.push(`Object ${index} has no stableId.`);
  if (!object.inventoryId) errors.push(`Object ${index} has no inventoryId.`);
  if (object.stableId && ids.has(object.stableId)) errors.push(`Duplicate stableId: ${object.stableId}`);
  if (object.inventoryId && inventoryIds.has(object.inventoryId)) errors.push(`Duplicate inventoryId: ${object.inventoryId}`);
  ids.add(object.stableId);
  inventoryIds.add(object.inventoryId);
  if (!['canonical', 'working'].includes(object.authorityLayer)) errors.push(`${object.stableId}: invalid authorityLayer.`);
  if (!object.name || !object.objectType) errors.push(`${object.stableId}: missing name or objectType.`);
  if (!object.references || !Array.isArray(object.references.dependencies)) errors.push(`${object.stableId}: invalid references.`);
  if (object.authorityLayer === 'canonical' && object.rawPointers?.canonicalIndex === null) errors.push(`${object.stableId}: canonical object lacks canonical pointer.`);
  if (object.authorityLayer === 'working' && object.rawPointers?.workingIndex === null) errors.push(`${object.stableId}: working object lacks working pointer.`);
}

const canonicalCount = (inventory.objects || []).filter(object => object.authorityLayer === 'canonical').length;
const workingCount = (inventory.objects || []).filter(object => object.authorityLayer === 'working').length;
if (inventory.summary?.totalObjects !== (inventory.objects || []).length) errors.push('summary.totalObjects mismatch.');
if (inventory.summary?.canonicalObjects !== canonicalCount) errors.push('summary.canonicalObjects mismatch.');
if (inventory.summary?.workingObjects !== workingCount) errors.push('summary.workingObjects mismatch.');
if ((inventory.objects || []).length < 487) errors.push('Unified inventory unexpectedly contains fewer than 487 objects.');

if (errors.length) {
  console.error(`Unified inventory validation failed with ${errors.length} error(s):`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(JSON.stringify({
  result: 'PASS',
  totalObjects: inventory.summary.totalObjects,
  canonicalObjects: canonicalCount,
  workingObjects: workingCount,
  structureDecisions: inventory.summary.structureDecisions
}, null, 2));
