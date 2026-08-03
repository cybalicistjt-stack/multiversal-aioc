import assert from 'node:assert/strict';
import { certifyWorkbenchExecution, assertWorkbenchExecutionCertified } from './workbench-execution-certification.mjs';

const base = () => ({
  continuityCertification: { result: 'PASS' },
  changeCertification: { result: 'PASS' },
  canonical: { repositoryId: 'multiversal-aioc', branch: 'governance/session-bootstrap-v1', workItemId: 'AIOC-I-004C' },
  execution: {
    repositoryId: 'multiversal-aioc', branch: 'governance/session-bootstrap-v1', workItemId: 'AIOC-I-004C',
    commitSha: 'abc123', status: 'success', changedFiles: ['a.mjs'], validationEvidence: ['ci://workbench'], evidence: ['commit://abc123']
  },
  handoff: {
    repositoryId: 'multiversal-aioc', branch: 'governance/session-bootstrap-v1', completedWorkItemId: 'AIOC-I-004C',
    nextAction: 'Begin AIOC-I-005A', evidence: ['ci://workbench']
  },
  requiredEvidence: ['ci://workbench']
});

const tests = [
  ['aligned execution certifies PASS', x => assert.equal(certifyWorkbenchExecution(x).result, 'PASS')],
  ['missing continuity blocks', x => { x.continuityCertification = null; assert.equal(certifyWorkbenchExecution(x).result, 'FAIL'); }],
  ['failed change certification blocks', x => { x.changeCertification.result = 'FAIL'; assert.equal(certifyWorkbenchExecution(x).result, 'FAIL'); }],
  ['missing execution blocks', x => { x.execution = null; assert.equal(certifyWorkbenchExecution(x).result, 'FAIL'); }],
  ['repository drift blocks', x => { x.execution.repositoryId = 'other'; assert.equal(certifyWorkbenchExecution(x).result, 'FAIL'); }],
  ['branch drift blocks', x => { x.execution.branch = 'main'; assert.equal(certifyWorkbenchExecution(x).result, 'FAIL'); }],
  ['work item drift blocks', x => { x.execution.workItemId = 'other'; assert.equal(certifyWorkbenchExecution(x).result, 'FAIL'); }],
  ['missing commit evidence blocks', x => { x.execution.commitSha = ''; assert.equal(certifyWorkbenchExecution(x).result, 'FAIL'); }],
  ['missing validation evidence blocks', x => { x.execution.validationEvidence = []; assert.equal(certifyWorkbenchExecution(x).result, 'FAIL'); }],
  ['partial execution warns and cannot complete', x => { x.execution.status = 'partial'; const r = certifyWorkbenchExecution(x); assert.equal(r.result, 'PASS WITH WARNINGS'); assert.equal(r.completionAllowed, false); }],
  ['missing handoff blocks', x => { x.handoff = null; assert.equal(certifyWorkbenchExecution(x).result, 'FAIL'); }],
  ['missing next action blocks', x => { x.handoff.nextAction = ''; assert.equal(certifyWorkbenchExecution(x).result, 'FAIL'); }],
  ['assertion accepts passing result', x => assert.equal(assertWorkbenchExecutionCertified(certifyWorkbenchExecution(x)).result, 'PASS')],
  ['assertion freezes failed result', x => { x.execution.commitSha = ''; assert.throws(() => assertWorkbenchExecutionCertified(certifyWorkbenchExecution(x)), /completion is frozen/); }]
];

let passed = 0;
for (const [name, fn] of tests) {
  try { fn(base()); passed++; console.log(`PASS ${name}`); }
  catch (error) { console.error(`FAIL ${name}`); throw error; }
}
console.log(`RESULT ${passed}/${tests.length} passed`);
