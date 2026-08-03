import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const outputPath = process.argv[2] || 'governance/development-brain/inventory/AIOC_UNIFIED_INVENTORY.generated.json';

function readJson(relativePath) {
  return JSON.parse(fs.readFileSync(path.join(root, relativePath), 'utf8'));
}

function stableId(record) {
  return record?.stableId || record?.refId || record?.databaseId || record?.catalogId || record?.id || null;
}

function nameOf(record, id) {
  return record?.name || record?.title || record?.label || id;
}

function typeOf(record) {
  return record?.objectType || record?.contentType || record?.objectKind || record?.type || 'Unknown';
}

function lifecycleOf(record, authorityLayer) {
  if (authorityLayer === 'canonical') return record?.retired ? 'retired' : 'canonical';
  const raw = String(record?.developmentStage || record?.stage || 'draft').toLowerCase().replace(/[_ ]+/g, '-');
  const mapping = {
    'source': 'source-only', 'source-only': 'source-only', 'draft': 'draft', 'in-development': 'development',
    'development': 'development', 'needs-validation': 'validation', 'validation': 'validation',
    'ready-for-review': 'review', 'review': 'review', 'game-ready': 'game-ready', 'canonical': 'canonical',
    'retired': 'retired', 'obsolete': 'retired'
  };
  return mapping[raw] || 'unknown';
}

function valuesReferencingId(container, id) {
  if (!container || typeof container !== 'object') return [];
  return Object.entries(container)
    .filter(([, value]) => JSON.stringify(value).includes(id))
    .map(([key]) => key);
}

function memoryReferences(memory, id) {
  return (memory.memories || [])
    .filter(entry => JSON.stringify(entry).includes(id))
    .map(entry => entry.memoryId)
    .filter(Boolean);
}

const canonical = readJson('content-db/index.json');
const shared = readJson('governance/shared-state/AIOC_SHARED_STATE.json');
const memory = readJson('governance/development-brain/memory/AIOC_PROJECT_MEMORY.json');

if (!Array.isArray(canonical.records)) throw new Error('content-db/index.json has no records array.');

const workingById = new Map((shared.workingObjects || []).map((record, index) => [stableId(record), { record, index }]));
const objects = [];

for (const [index, record] of canonical.records.entries()) {
  const id = stableId(record);
  if (!id) throw new Error(`Canonical record ${index} has no stable identifier.`);
  const working = workingById.get(id);
  const structure = shared.structureDecisions?.[id] || null;
  objects.push({
    inventoryId: `INV-${id}`,
    stableId: id,
    name: nameOf(working?.record || record, id),
    objectType: typeOf(working?.record || record),
    authorityLayer: working ? 'working' : 'canonical',
    lifecycle: lifecycleOf(working?.record || record, working ? 'working' : 'canonical'),
    sourceRecord: working?.record?.sourceRecordId || working?.record?.sourceId || id,
    structure,
    references: {
      packs: valuesReferencingId(shared.packLists, id),
      balanceEvidence: valuesReferencingId(shared.balanceEvidence, id),
      testingEvidence: valuesReferencingId(shared.testingEvidence, id),
      reviewItems: valuesReferencingId(shared.reviewQueue, id),
      memoryIds: memoryReferences(memory, id),
      dependencies: [...new Set([...(record.dependencies || []), ...(working?.record?.dependencies || [])].filter(Boolean))]
    },
    provenance: working?.record?.provenance || record.provenance || record.source || null,
    rawPointers: { canonicalIndex: index, workingIndex: working?.index ?? null }
  });
  workingById.delete(id);
}

for (const [id, { record, index }] of workingById.entries()) {
  if (!id) throw new Error(`Working record ${index} has no stable identifier.`);
  objects.push({
    inventoryId: `INV-${id}`,
    stableId: id,
    name: nameOf(record, id),
    objectType: typeOf(record),
    authorityLayer: 'working',
    lifecycle: lifecycleOf(record, 'working'),
    sourceRecord: record.sourceRecordId || record.sourceId || null,
    structure: shared.structureDecisions?.[id] || null,
    references: {
      packs: valuesReferencingId(shared.packLists, id),
      balanceEvidence: valuesReferencingId(shared.balanceEvidence, id),
      testingEvidence: valuesReferencingId(shared.testingEvidence, id),
      reviewItems: valuesReferencingId(shared.reviewQueue, id),
      memoryIds: memoryReferences(memory, id),
      dependencies: [...new Set(record.dependencies || [])]
    },
    provenance: record.provenance || null,
    rawPointers: { canonicalIndex: null, workingIndex: index }
  });
}

objects.sort((a, b) => a.stableId.localeCompare(b.stableId));
const sumRefs = key => objects.reduce((total, object) => total + object.references[key].length, 0);

const inventory = {
  format: 'multiversal-aioc-unified-inventory',
  version: '1.0.0',
  generatedAt: new Date().toISOString(),
  sources: {
    canonicalContent: { path: 'content-db/index.json', version: canonical.version ?? canonical.formatVersion ?? null },
    sharedState: { path: 'governance/shared-state/AIOC_SHARED_STATE.json', version: shared.version ?? null, revision: shared.revision ?? 0 },
    projectMemory: { path: 'governance/development-brain/memory/AIOC_PROJECT_MEMORY.json', version: memory.version ?? null, revision: memory.revision ?? 0 }
  },
  summary: {
    totalObjects: objects.length,
    canonicalObjects: objects.filter(object => object.authorityLayer === 'canonical').length,
    workingObjects: objects.filter(object => object.authorityLayer === 'working').length,
    structureDecisions: Object.keys(shared.structureDecisions || {}).length,
    reviewItems: (shared.reviewQueue || []).length,
    packReferences: sumRefs('packs'),
    balanceEvidenceReferences: sumRefs('balanceEvidence'),
    testingEvidenceReferences: sumRefs('testingEvidence'),
    memoryReferences: sumRefs('memoryIds')
  },
  objects
};

fs.mkdirSync(path.dirname(path.join(root, outputPath)), { recursive: true });
fs.writeFileSync(path.join(root, outputPath), `${JSON.stringify(inventory, null, 2)}\n`);
console.log(`Generated ${objects.length} unified inventory objects at ${outputPath}.`);
