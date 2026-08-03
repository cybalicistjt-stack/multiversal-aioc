import assert from 'node:assert/strict';
import { projectTestHarness, assertExecutableProjection, fingerprint } from './test-harness-projection.mjs';

const canonical = {repository:'cybalicistjt-stack/multiversal-aioc',branch:'governance/session-bootstrap-v1',milestoneId:'AIOC-I-006',workItemId:'AIOC-I-006A'};
const base = {
  canonical,
  continuity:{certified:true},
  repositoryHealth:{status:'healthy'},
  request:{
    ...canonical,
    runnerCapabilities:['execute-tests'],
    evidenceSinks:['artifact://test-results'],
    availableDependencies:['core-rules'],
    requiredKinds:['unit','integration'],
    approvals:[],
    scenarios:[
      {id:'unit-1',title:'Unit case',kind:'unit',expectedOutcome:'pass',dependencies:['core-rules']},
      {id:'int-1',title:'Integration case',kind:'integration',expectedOutcome:'pass'}
    ]
  }
};

const tests = [];
function test(name, fn){ tests.push([name, fn]); }
function clone(v){ return structuredClone(v); }

test('aligned harness projects PASS',()=>{ const p=projectTestHarness(base); assert.equal(p.status,'PASS'); assert.equal(p.plan.length,2); });
test('projection fingerprint is deterministic',()=>{ const a=projectTestHarness(base); const b=projectTestHarness(base); assert.equal(a.fingerprint,b.fingerprint); assert.equal(a.fingerprint,fingerprint({...a,fingerprint:undefined})); });
test('uncertified continuity blocks',()=>{ const x=clone(base); x.continuity.certified=false; assert.equal(projectTestHarness(x).status,'FAIL'); });
test('blocked repository health blocks',()=>{ const x=clone(base); x.repositoryHealth.status='blocked'; assert.equal(projectTestHarness(x).executionAllowed,false); });
test('canonical repository mismatch blocks',()=>{ const x=clone(base); x.request.repository='wrong/repo'; assert(projectTestHarness(x).findings.some(f=>f.code==='CANONICAL_REPOSITORY_MISMATCH')); });
test('canonical branch mismatch blocks',()=>{ const x=clone(base); x.request.branch='main'; assert(projectTestHarness(x).findings.some(f=>f.code==='CANONICAL_BRANCH_MISMATCH')); });
test('empty scenario collection blocks',()=>{ const x=clone(base); x.request.scenarios=[]; assert(projectTestHarness(x).findings.some(f=>f.code==='NO_SCENARIOS')); });
test('missing required scenario field blocks',()=>{ const x=clone(base); x.request.scenarios[0].title=''; assert.equal(projectTestHarness(x).status,'FAIL'); });
test('duplicate scenario ids block',()=>{ const x=clone(base); x.request.scenarios[1].id='unit-1'; assert(projectTestHarness(x).findings.some(f=>f.code==='DUPLICATE_SCENARIO_ID')); });
test('missing dependency blocks',()=>{ const x=clone(base); x.request.availableDependencies=[]; assert(projectTestHarness(x).findings.some(f=>f.code==='SCENARIO_DEPENDENCY_MISSING')); });
test('missing required scenario kind blocks',()=>{ const x=clone(base); x.request.scenarios=x.request.scenarios.filter(s=>s.kind!=='integration'); assert(projectTestHarness(x).findings.some(f=>f.code==='REQUIRED_SCENARIO_KIND_MISSING')); });
test('high risk scenario requires evidence-backed approval',()=>{ const x=clone(base); x.request.scenarios[0].risk='high'; assert(projectTestHarness(x).findings.some(f=>f.code==='HIGH_RISK_SCENARIO_APPROVAL_MISSING')); });
test('high risk approval permits execution',()=>{ const x=clone(base); x.request.scenarios[0].risk='high'; x.request.approvals=[{scope:'unit-1',approved:true,evidence:'approval://1'}]; assert.equal(projectTestHarness(x).status,'PASS'); });
test('missing evidence sink blocks',()=>{ const x=clone(base); x.request.evidenceSinks=[]; assert(projectTestHarness(x).findings.some(f=>f.code==='EVIDENCE_SINK_MISSING')); });
test('missing runner capability blocks',()=>{ const x=clone(base); x.request.runnerCapabilities=[]; assert(projectTestHarness(x).findings.some(f=>f.code==='RUNNER_CAPABILITY_MISSING')); });
test('assertion accepts executable projection',()=>{ assert.equal(assertExecutableProjection(projectTestHarness(base)).status,'PASS'); });
test('assertion freezes failed projection',()=>{ const x=clone(base); x.continuity.certified=false; assert.throws(()=>assertExecutableProjection(projectTestHarness(x))); });

let passed=0;
for (const [name,fn] of tests){ try{ fn(); passed++; console.log(`PASS ${name}`); } catch(error){ console.error(`FAIL ${name}`); throw error; } }
console.log(`RESULT ${passed}/${tests.length} passed`);
