import assert from 'node:assert/strict';
import { projectReleaseReadiness } from './release-readiness-projection.mjs';

const evidence = ['evidence://pass'];
const base = {
  repository:'cybalicistjt-stack/multiversal-aioc',
  branch:'governance/session-bootstrap-v1',
  canonical:{repository:'cybalicistjt-stack/multiversal-aioc',branch:'governance/session-bootstrap-v1',workItem:'AIOC-I-007A'},
  continuityStatus:'PASS', repositoryHealth:'healthy',
  certifications:['operational-core','continuity','orchestration','developer-workbench','content-studio','testing-simulation'].map(domain=>({domain,status:'PASS',evidence})),
  securityChecks:['secret-scan','dependency-audit','permission-review','artifact-integrity'].map(id=>({id,status:'PASS',evidence})),
  release:{id:'aioc-0.1.0',version:'0.1.0',channel:'stable',artifacts:[{path:'dist/aioc.zip',sha256:'abc'}],approvals:[{role:'owner',status:'approved',evidence}]},
  deployment:{preflight:{status:'PASS',evidence},deploy:{status:'PASS',evidence},verify:{status:'PASS',evidence}},
  recovery:{rollback:{status:'PASS',evidence},restore:{status:'PASS',evidence}}
};

const tests = [
  ['clean release passes', x=>assert.equal(x.status,'PASS')],
  ['clean release is executable', x=>assert.equal(x.executionFrozen,false)],
  ['clean release has five steps', x=>assert.equal(x.plan.length,5)],
  ['fingerprint is deterministic', x=>assert.equal(x.fingerprint,projectReleaseReadiness(structuredClone(base)).fingerprint)],
];

let passed=0;
for (const [name, check] of tests) { check(projectReleaseReadiness(structuredClone(base))); console.log(`PASS ${name}`); passed++; }

const cases = [
  ['canonical repository mismatch', d=>d.repository='wrong/repo','canonical.repository'],
  ['canonical branch mismatch', d=>d.branch='wrong','canonical.branch'],
  ['wrong active item', d=>d.canonical.workItem='AIOC-I-006C','canonical.work-item'],
  ['continuity failure', d=>d.continuityStatus='FAIL','continuity.status'],
  ['blocked repository', d=>d.repositoryHealth='blocked','repository.health'],
  ['missing domain certification', d=>d.certifications.pop(),'certification.testing-simulation'],
  ['failed security check', d=>d.securityChecks[0].status='FAIL','security.secret-scan'],
  ['missing release id', d=>delete d.release.id,'release.id'],
  ['missing artifact checksum', d=>delete d.release.artifacts[0].sha256,'release.artifact-integrity'],
  ['failed deployment verify', d=>d.deployment.verify.status='FAIL','deployment.verify'],
  ['failed rollback', d=>d.recovery.rollback.status='FAIL','recovery.rollback'],
  ['missing stable approval', d=>d.release.approvals=[],'approval.owner'],
];
for (const [name, mutate, code] of cases) {
  const data=structuredClone(base); mutate(data); const result=projectReleaseReadiness(data);
  assert.equal(result.status,'FAIL'); assert.equal(result.executionFrozen,true); assert.ok(result.findings.some(f=>f.code===code));
  console.log(`PASS ${name}`); passed++;
}
console.log(`RESULT ${passed}/${tests.length+cases.length} passed`);
