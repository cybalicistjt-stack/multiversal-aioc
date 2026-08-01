import fs from 'node:fs/promises';
import path from 'node:path';
import zlib from 'node:zlib';

const ROOT = process.cwd();
const PART_DIR = path.join(ROOT, 'catalog-seed-parts');
const OUT_DIR = path.join(ROOT, 'content-db');
const PARTS = [0,1,2,3,4].map(i => path.join(PART_DIR, `phase1-7.${String(i).padStart(2,'0')}.txt`));
const SOURCE = 'Multiversal 8E-008G Foundational Inventory Coverage (Phase 1–7 baseline)';
const DB_VERSION = '1.0.0';
const STAGES = {
  CANONICAL_ID_PRESENT: 'Schema review',
  ALIAS_RESOLVES: 'Partial conversion',
  PLAYTEST_INVENTORY_ONLY: 'Source identified'
};

function cleanBase64(text) {
  return String(text).replace(/[^A-Za-z0-9+/=]/g, '');
}

function decodeLayers(input) {
  let value = cleanBase64(input);
  for (let layer = 0; layer < 4; layer++) {
    const bytes = Buffer.from(value, 'base64');
    if (bytes.length >= 2 && bytes[0] === 0x1f && bytes[1] === 0x8b) return bytes;
    const asText = bytes.toString('utf8').trim();
    if (!/^[A-Za-z0-9+/=\s]+$/.test(asText)) {
      throw new Error(`Decoded layer ${layer + 1} is neither gzip nor Base64 text.`);
    }
    value = cleanBase64(asText);
  }
  throw new Error('Could not reach gzip data after four Base64 layers.');
}

function expand(x, index) {
  const coverage = x.v || '';
  const stableId = x.r || '';
  return {
    databaseId: x.c || `phase17-${index + 1}`,
    stableId,
    name: x.n || stableId || `Unnamed inventory record ${index + 1}`,
    objectType: x.t || 'Unclassified',
    developmentStage: STAGES[coverage] || x.g || 'Source identified',
    source: x.s || SOURCE,
    sourceLocator: x.l || '',
    coverageStatus: coverage,
    promotionDecision: x.p || '',
    reviewStatus: x.w || '',
    packIds: [],
    dependencies: [],
    tags: ['phase-1-7', coverage.toLowerCase(), String(x.p || '').toLowerCase()].filter(Boolean),
    provenance: {
      authority: SOURCE,
      phaseRange: '1-7',
      inventoryId: x.c || '',
      importedBy: 'scripts/build-content-database.mjs'
    }
  };
}

await fs.mkdir(OUT_DIR, { recursive: true });
const texts = await Promise.all(PARTS.map(file => fs.readFile(file, 'utf8')));
const gzipBytes = decodeLayers(texts.join(''));
const payload = JSON.parse(zlib.gunzipSync(gzipBytes).toString('utf8'));
if (!Array.isArray(payload.records) || payload.records.length < 1000) {
  throw new Error(`Recovered inventory is invalid: ${payload.records?.length ?? 0} records.`);
}

const records = payload.records.map(expand);
const byType = {};
const byStage = {};
const byCoverage = {};
for (const record of records) {
  (byType[record.objectType] ??= []).push(record.databaseId);
  (byStage[record.developmentStage] ??= []).push(record.databaseId);
  (byCoverage[record.coverageStatus || 'UNCLASSIFIED'] ??= []).push(record.databaseId);
}

const generatedAt = new Date().toISOString();
const index = {
  format: 'multiversal-content-database',
  databaseVersion: DB_VERSION,
  generatedAt,
  source: SOURCE,
  recordCount: records.length,
  summary: {
    canonicalIds: records.filter(r => r.coverageStatus === 'CANONICAL_ID_PRESENT').length,
    aliasResolved: records.filter(r => r.coverageStatus === 'ALIAS_RESOLVES').length,
    playtestOnly: records.filter(r => r.coverageStatus === 'PLAYTEST_INVENTORY_ONLY').length,
    types: Object.fromEntries(Object.entries(byType).map(([k,v]) => [k, v.length]))
  },
  records
};

const manifest = {
  format: 'multiversal-content-database-manifest',
  databaseVersion: DB_VERSION,
  generatedAt,
  source: SOURCE,
  recordCount: records.length,
  indexPath: './index.json',
  indexes: {
    byType: './indexes/by-type.json',
    byStage: './indexes/by-stage.json',
    byCoverage: './indexes/by-coverage.json'
  }
};

await fs.mkdir(path.join(OUT_DIR, 'indexes'), { recursive: true });
await fs.writeFile(path.join(OUT_DIR, 'index.json'), JSON.stringify(index, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'indexes', 'by-type.json'), JSON.stringify(byType, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'indexes', 'by-stage.json'), JSON.stringify(byStage, null, 2) + '\n');
await fs.writeFile(path.join(OUT_DIR, 'indexes', 'by-coverage.json'), JSON.stringify(byCoverage, null, 2) + '\n');
console.log(`Generated Multiversal content database with ${records.length} records.`);
