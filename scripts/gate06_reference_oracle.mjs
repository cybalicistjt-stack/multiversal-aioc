// Design-only fixture oracle: no real PostgreSQL, signed grant, device, payment or server authorization.
import {readFileSync} from 'node:fs';
const f=JSON.parse(readFileSync(new URL('../governance/application-planning/governed-access-transactions-entitlements/GATE_06_POLICY_FIXTURES.json',import.meta.url),'utf8'));
const evaluate=function(v) {
 if(v.verified===false)return "DENY_ACCOUNT";
 if(v.suspended===true)return "DENY_SUSPENDED";
 if(v.kind==="issue"){
  if(v.gm!==true)return "DENY_NOT_GM";
  if(v.gmSubscriber!==true)return "DENY_GM_SUBSCRIPTION";
  if(v.member!==true)return "DENY_MEMBER";
  if(v.sharingRights!==true)return "DENY_SHARING";
  if(v.validClosure!==true)return "DENY_CLOSURE";
  if(v.slotOccupied===true)return "OCCUPIED";
  if(v.idemOtherSubject===true)return "DENY_IDEMPOTENCY";
  return "ISSUE_SINGLE_SLOT";
 }
 if(v.kind==="use"){
  if(v.member!==true)return "DENY_MEMBER";
  if(v.campaignMatch!==true)return "DENY_CAMPAIGN";
  if(v.rolePermits!==true)return "DENY_ROLE";
  if(v.visible!==true)return "DENY_VISIBILITY";
  if(v.licensed!==true)return "DENY_LICENSE";
  if(v.subscriber===true)return "ALLOW_PERSONAL";
  if(v.sponsored===true)return "ALLOW_SPONSORED";
  if(v.grantActive!==true)return "DENY_GRANT";
  if(v.rootIncluded!==true)return "DENY_UNRELATED_ROOT";
  if(v.grantRevoked===true)return "DENY_REVOKED";
  if(v.beneficiaryMatches!==true)return "DENY_BENEFICIARY";
  if(v.actionPermitted!==true)return "DENY_ACTION";
  return "ALLOW_CAMPAIGN_CLOSURE";
 }
 if(v.kind==="view"){
  if(v.owner!==true)return "DENY_OWNER";
  if(v.hidden===true)return "DENY_PRIVATE";
  if(v.retainedProjection!==true)return "DENY_PROJECTION";
  if(v.purpose!=="read")return "DENY_PROJECTION_RUNTIME";
  return "ALLOW_RETAINED_CHARACTER_VIEW";
 }
 if(v.kind==="transfer"){
  if(v.provenanceKnown!==true)return "DENY_UNKNOWN_ORIGIN";
  if(v.restricted===true||v.restrictedNested===true)return "DENY_RESTRICTED_TRANSFER";
  if(v.owner!==true)return "DENY_OWNER";
  if(v.destinationLicensed!==true)return "DENY_DESTINATION_LICENSE";
  if(v.destinationRole!==true)return "DENY_DESTINATION_ROLE";
  return "ALLOW_INDEPENDENT_TRANSFER";
 }
 if(v.kind==="sponsor"){
  if(v.subjectMatches!==true)return "DENY_SPONSORED_SUBJECT";
  if(v.sourceVerified!==true)return "DENY_SPONSOR_SOURCE";
  if(v.finitePeriod!==true)return "DENY_SPONSOR_FINITE";
  if(v.inPeriod!==true)return "DENY_SPONSOR_EXPIRED";
  if(v.scopeMatches!==true)return "DENY_SPONSOR_SCOPE";
  return "ALLOW_ACCOUNT_SPONSORSHIP";
 }
 if(v.kind==="offline"){
  if(v.signedLease!==true)return "DENY_UNSIGNED";
  if(v.deviceMatches!==true)return "DENY_DEVICE";
  if(v.unchangedAccount!==true)return "DENY_SWITCH";
  if(v.campaignMatches!==true)return "DENY_CAMPAIGN";
  if(v.digestMatches!==true)return "DENY_MANIFEST";
  if(v.finiteExpiry!==true)return "DENY_FINITE";
  if(v.unexpired!==true)return "DENY_EXPIRED";
  if(v.knownDenial===true)return "DENY_KNOWN";
  return "ALLOW_PREVERIFIED_OFFLINE_SCOPE";
 }
 return "DENY_UNSUPPORTED";
};
const closure=function(graph,root){
 const seen=new Set(),onPath=new Set(),nodes=[];
 function visit(id){
  if(onPath.has(id))return "CYCLE";
  if(seen.has(id))return "OK";
  const n=graph[id];if(!n)return "MISSING";
  if(n.trusted!==true)return "UNTRUSTED";
  if(n.licensed!==true)return "UNLICENSED";
  onPath.add(id);
  for(const dep of n.required||[]){const result=visit(dep);if(result!=="OK")return result;}
  onPath.delete(id);seen.add(id);nodes.push(id);return "OK";
 }
 const status=visit(root);
 return {status,resources:status==="OK"?nodes.slice().sort():[]};
};
let failures=0;
for(const c of f.decisions){const got=evaluate(c.input);if(got!==c.expected){console.error(c.id,got,c.expected);failures++;}}
for(const g of f.graphs){const got=closure(g.graph,g.root);if(got.status!==g.expectedStatus||JSON.stringify(got.resources)!==JSON.stringify(g.expectedResources)){console.error(g.id,got);failures++;}}
if(failures)process.exitCode=1;
else console.log(`GATE06 reference PASS ${f.decisions.length} policy + ${f.graphs.length} closure; installed/DB/security proof NOT_RUN.`);
