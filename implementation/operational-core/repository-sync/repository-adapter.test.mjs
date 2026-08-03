import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { normalizeRepositorySnapshot, fingerprintSnapshot, compareRepositoryState, RepositoryStateSynchronizer } from './repository-adapter.mjs';

const seed = JSON.parse(await readFile(new URL('../project-state/canonical-project-state.seed.json', import.meta.url), 'utf8'));
const tests=[]; const test=(name,fn)=>tests.push({name,fn});
const live = fullName => ({fullName,defaultBranch:'main',private:true,permissions:{read:true,push:true,admin:true},head:{sha:'abc123',message:'test',committedAt:'2026-08-03T00:00:00Z'},openPullRequests:[],capabilityEvidence:['github:read','github:write'],observedAt:'2026-08-03T00:00:00Z'});

test('normalization preserves identity and permissions',()=>{const x=normalizeRepositorySnapshot(live('cybalicistjt-stack/multiversal-aioc'));assert.equal(x.fullName,'cybalicistjt-stack/multiversal-aioc');assert.equal(x.permissions.push,true)});
test('fingerprint ignores observation time',async()=>{const a=live('x/y'),b={...live('x/y'),observedAt:'2027-01-01T00:00:00Z'};assert.equal(await fingerprintSnapshot(normalizeRepositorySnapshot(a)),await fingerprintSnapshot(normalizeRepositorySnapshot(b)))});
test('identity drift is blocking',()=>{const drift=compareRepositoryState({fullName:'a/b',defaultBranch:'main',canonical:true},normalizeRepositorySnapshot(live('c/d')));assert.equal(drift.some(x=>x.code==='repository.identity'&&x.severity==='error'),true)});
test('missing push is visible but non-destructive',()=>{const snapshot=normalizeRepositorySnapshot({...live('a/b'),permissions:{read:true,push:false,admin:false}});const drift=compareRepositoryState({fullName:'a/b',defaultBranch:'main',canonical:true},snapshot);assert.equal(drift.some(x=>x.code==='repository.push'),true)});
test('synchronizer observes all canonical repositories',async()=>{const provider={getRepository:async name=>live(name)};const sync=new RepositoryStateSynchronizer({provider});const result=await sync.synchronize(seed);assert.equal(result.observations.length,seed.repositories.length);assert.equal(result.hasBlockingDrift,false)});
test('synchronizer never mutates input state',async()=>{const original=JSON.stringify(seed);const sync=new RepositoryStateSynchronizer({provider:{getRepository:async name=>live(name)}});await sync.synchronize(seed);assert.equal(JSON.stringify(seed),original)});
test('destructive mode is rejected',async()=>{const sync=new RepositoryStateSynchronizer({provider:{getRepository:async name=>live(name)}});await assert.rejects(()=>sync.synchronize(seed,{destructive:true}),e=>e.code==='sync.destructive')});
test('changed fingerprint marks live-state change',async()=>{const prior=JSON.parse(JSON.stringify(seed));prior.repositoryObservations=[{repositoryId:'multiversal-aioc',fingerprint:'old'}];const sync=new RepositoryStateSynchronizer({provider:{getRepository:async name=>live(name)}});const result=await sync.synchronize(prior);assert.equal(result.observations.find(x=>x.repositoryId==='multiversal-aioc').changed,true)});
test('provider failure prevents partial persistence',async()=>{let persisted=false;const sync=new RepositoryStateSynchronizer({provider:{getRepository:async name=>{if(name.includes('Multiversal-app'))throw new Error('offline');return live(name)}},persistObservation:async()=>{persisted=true}});await assert.rejects(()=>sync.synchronize(seed));assert.equal(persisted,false)});

let failures=0;for(const {name,fn} of tests){try{await fn();console.log(`PASS ${name}`)}catch(error){failures++;console.error(`FAIL ${name}`);console.error(error)}}console.log(`RESULT ${tests.length-failures}/${tests.length} passed`);if(failures)process.exit(1);
