import assert from 'node:assert/strict';
import fs from 'node:fs';

const html=fs.readFileSync('content-library.html','utf8');
const collections=fs.readFileSync('content-library-collections.js','utf8');
const worker=fs.readFileSync('recovery-import-worker.js','utf8');
const database=fs.readFileSync('content-database.js','utf8');

assert.match(html,/content-library-collections\.js/,'collection wrapper must load before the library UI');
assert.ok(html.indexOf('content-library-collections.js')<html.indexOf('content-library.js'),'collection wrapper must load before content-library.js');
assert.match(collections,/canonical-487/,'the preserved certified collection must remain addressable');
assert.match(collections,/recovered-staging/,'the recovered staging collection must remain separate');
assert.match(collections,/indexedDB/,'large staging collections must use IndexedDB rather than localStorage');
assert.match(collections,/importRecoveryLedger/,'a governed recovery import operation must exist');
assert.match(collections,/not installed in this browser/,'missing staging data must fail explicitly');
assert.match(worker,/row\.name\|\|!row\.object_type/,'staging import must require source-provided names and explicit types');
assert.match(worker,/semantic_key/,'staging import must preserve deterministic identity grouping');
assert.match(worker,/not-canonical/,'recovered records must remain visibly non-canonical');
assert.match(database,/CERTIFIED_RECORD_COUNT=487/,'the original certified collection remains locked and restorable');
console.log('Content Library staging collection contract: PASS');
