import assert from 'node:assert/strict';
import { certifyDigitalTwin } from './digital-twin-regression-certification.mjs';

const base = () => ({
  canonical: { repository: 'cybalicistjt-stack/multiversal-aioc', branch: 'governance/session-bootstrap-v1', milestoneId: 'AIOC-I-006', workItemId: 'AIOC-I-006C' },
  continuity: { result: 'PASS' },
  repositoryHealth: { status: 'healthy' },
  twin: { id: 'twin-main', baselineFingerprint: 'abc', modelVersion: '1.0.0', domains: ['combat','progression','economy','content'], evidence: ['artifact://twin'] },
  regressions: [{ id: 'REG-1', severity: 'low', status: 'resolved', sourceEvidence: ['artifact://reg-1'] }],
  tests: [
    { id: 'T-COMBAT', result: 'pass', domains: ['combat'], evidence: ['artifact://combat'] },
    { id: 'T-PROGRESSION', result: 'pass', domains: ['progression'], evidence: ['artifact://progression'] },
    { id: 'T-ECONOMY', result: 'pass', domains: ['economy'], evidence: ['artifact://economy'] },
    { id: 'T-CONTENT', result: 'pass', domains: ['content'], evidence: ['artifact://content'] }
  ],
  runner: { capabilities: ['digital-twin','regression-mining'] },
  evidenceSink: { durable: true }
});

const cases = [];
const test = (name, fn) => cases.push([name, fn]);

test('valid certification passes', () => assert.equal(certifyDigitalTwin(base()).result, 'PASS'));
test('fingerprint is deterministic', () => assert.equal(certifyDigitalTwin(base()).fingerprint, certifyDigitalTwin(base()).fingerprint));
test('continuity failure blocks', () => { const x=base(); x.continuity.result='FAIL'; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('repository health blocks', () => { const x=base(); x.repositoryHealth.status='blocked'; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('canonical work item is enforced', () => { const x=base(); x.canonical.workItemId='AIOC-I-006B'; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('baseline fingerprint is required', () => { const x=base(); delete x.twin.baselineFingerprint; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('all four domains are required', () => { const x=base(); x.twin.domains=['combat']; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('twin evidence is required', () => { const x=base(); x.twin.evidence=[]; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('duplicate regression ids fail', () => { const x=base(); x.regressions.push({...x.regressions[0]}); assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('critical open regression fails', () => { const x=base(); x.regressions=[{id:'R',severity:'critical',status:'open',sourceEvidence:['e']}]; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('noncritical open regression warns', () => { const x=base(); x.regressions=[{id:'R',severity:'medium',status:'open',sourceEvidence:['e']}]; const r=certifyDigitalTwin(x); assert.equal(r.result,'PASS WITH WARNINGS'); assert.equal(r.completionAllowed,false); });
test('regression evidence is required', () => { const x=base(); x.regressions[0].sourceEvidence=[]; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('duplicate test ids fail', () => { const x=base(); x.tests.push({...x.tests[0]}); assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('required failed test blocks', () => { const x=base(); x.tests[0].result='fail'; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('optional failed test warns', () => { const x=base(); x.tests.push({id:'OPT',required:false,result:'fail',domains:[],evidence:['e']}); assert.equal(certifyDigitalTwin(x).result,'PASS WITH WARNINGS'); });
test('test evidence is required', () => { const x=base(); x.tests[0].evidence=[]; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('passing domain coverage is required', () => { const x=base(); x.tests=x.tests.filter(t=>!t.domains.includes('economy')); assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('digital twin runner capability is required', () => { const x=base(); x.runner.capabilities=['regression-mining']; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('regression mining capability is required', () => { const x=base(); x.runner.capabilities=['digital-twin']; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });
test('durable evidence sink is required', () => { const x=base(); x.evidenceSink.durable=false; assert.equal(certifyDigitalTwin(x).result,'FAIL'); });

let passed=0;
for (const [name, fn] of cases) {
  try { fn(); passed++; console.log(`PASS ${name}`); }
  catch (error) { console.error(`FAIL ${name}`); console.error(error); process.exitCode=1; }
}
console.log(`RESULT ${passed}/${cases.length} passed`);
if (passed !== cases.length) process.exitCode=1;
