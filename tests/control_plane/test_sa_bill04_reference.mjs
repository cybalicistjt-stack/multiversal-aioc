import test from 'node:test';
import assert from 'node:assert/strict';
import {
 parseInstant,windowActive,readProviderEntitlement,trustedDependencyClosure,
 decideAllowanceUse,decideAllowanceIssuance
} from './sa_bill04_reference.mjs';

const paid=()=>({origin:'verified-billing-ledger',provider:'sandbox-provider',productId:'mock-product',purchaseBindingId:'purchase-GM-1',sourceRevision:'revision-17',payerSubjectId:'gm',boundSubjectId:'gm',status:'verified_active',entitledFrom:'2026-10-01T00:00:00Z',entitledUntil:'2026-12-01T00:00:00Z'});
const graph=()=>({setting:{version:'v1',kind:'custom-setting',active:true,rightsApproved:true,canUseInCampaign:true,ownerAllowedAsGrantRoot:true,dependencies:['species','item']},species:{version:'v1',kind:'registered-species',active:true,rightsApproved:true,canUseInCampaign:true,dependencies:['tree']},item:{version:'v1',kind:'registered-item-set',active:true,rightsApproved:true,canUseInCampaign:true,dependencies:[]},tree:{version:'v1',kind:'registered-ability-tree',active:true,rightsApproved:true,canUseInCampaign:true,dependencies:[]},unrelated:{version:'v1',kind:'registered-species',active:true,rightsApproved:true,canUseInCampaign:true,dependencies:[]}});
function fixture(){const registry=graph(),closure=trustedDependencyClosure(registry,'setting');return{request:{subjectId:'player',campaignId:'campaign-A',resourceId:'tree',action:'campaign-use',now:'2026-11-01T00:00:00Z'},owner:{registry,slot:{playerSubjectId:'player',campaignId:'campaign-A',rootReleaseId:'setting',issuerGmSubjectId:'gm',state:'active',grantEpoch:4,entitlementRulesetVersion:'r2',closureDigest:closure.digest},access:{campaignId:'campaign-A',playerSubjectId:'player',currentGmSubjectId:'gm',gmRoleActive:true,playerMembershipActive:true,sourceRevisionCurrent:true,currentGrantEpoch:4,entitlementRulesetVersion:'r2'},verifiedGmSubscription:paid()}};}
const use=(delta={})=>{const f=fixture();return decideAllowanceUse({request:{...f.request,...(delta.request||{})},owner:{...f.owner,...(delta.owner||{})}})};

test('SA04-01 normalize offsets, reject invalid civil dates/naive/24:00/overlong zones',()=>{
 assert.equal(parseInstant('2026-11-01T00:00:00+02:00'),parseInstant('2026-10-31T22:00:00Z'));
 for(const s of ['2026-02-30T12:00:00Z','2026-13-01T00:00:00Z','2026-11-01T24:00:00Z','2026-11-01T00:00:60Z','2026-11-01T00:00:00','nonsense','2026-11-01T00:00:00+15:00'])assert.equal(parseInstant(s),null,s);
});
test('SA04-02 exact UTC expiry: old lexical bug is denied',()=>{
 assert.equal(windowActive('2026-10-01T00:00:00Z','2026-11-01T00:00:00+02:00','2026-10-31T23:00:00Z'),false);
 assert.equal(windowActive('2026-10-01T00:00:00Z','2026-11-01T00:00:00+02:00','2026-10-31T21:59:59Z'),true);
});
test('SA04-03 invalid expiry never creates an indefinite subscription',()=>{
 assert.equal(readProviderEntitlement({...paid(),entitledUntil:'nonsense'},'2026-11-01T00:00:00Z').kind,'deny');
 assert.equal(readProviderEntitlement({...paid(),entitledUntil:undefined},'2026-11-01T00:00:00Z').kind,'deny');
});
test('SA04-04 verified cancellation preserves already-paid term but stops at expiry',()=>{
 assert.equal(readProviderEntitlement({...paid(),status:'cancel_scheduled'},'2026-11-30T23:59:59Z').kind,'allow');
 assert.equal(readProviderEntitlement({...paid(),status:'cancel_scheduled'},'2026-12-01T00:00:00Z').kind,'deny');
});
test('SA04-05 source origin, binding and revision are required assumptions',()=>{
 for(const delta of [{origin:'client-flag'},{boundSubjectId:'other'},{sourceRevision:''},{purchaseBindingId:''},{productId:''}])assert.equal(readProviderEntitlement({...paid(),...delta},'2026-11-01T00:00:00Z').kind,'deny');
});
test('SA04-06 verified grace can extend beyond paid term without new grant issuance',()=>{
 const grace={...paid(),status:'grace_entitled',providerConfirmsGrace:true,providerGraceUntil:'2026-12-03T00:00:00Z'};
 assert.equal(readProviderEntitlement(grace,'2026-12-02T00:00:00Z').issueAllowance,false);
 assert.equal(readProviderEntitlement({...grace,providerConfirmsGrace:false},'2026-12-02T00:00:00Z').kind,'deny');
 assert.equal(readProviderEntitlement({...paid(),status:'trial_verified'},'2026-11-01T00:00:00Z').kind,'pending_policy');
 assert.equal(readProviderEntitlement({...paid(),status:'account_hold'},'2026-11-01T00:00:00Z').kind,'deny');
});
test('SA04-07 trusted transitive closure; reject unrelated, cycles and unknowns',()=>{
 const c=trustedDependencyClosure(graph(),'setting');assert.deepEqual(c.entries.map(e=>e.id),['item','setting','species','tree']);assert.equal(c.ids.has('unrelated'),false);
 const g=graph();g.tree.dependencies=['setting'];assert.throws(()=>trustedDependencyClosure(g,'setting'),/DEPENDENCY_CYCLE/);
 const h=graph();h.tree.dependencies=['missing'];assert.throws(()=>trustedDependencyClosure(h,'setting'),/UNREGISTERED_OR_UNRIGHTED_DEPENDENCY/);
});
test('SA04-08 source version and content rights changes invalidate closure',()=>{
 const f=fixture();f.owner.registry.tree.version='v2';assert.equal(decideAllowanceUse(f).allowed,false);
 const g=fixture();g.owner.registry.tree.rightsApproved=false;assert.equal(decideAllowanceUse(g).allowed,false);
});
test('SA04-09 current canonical subject, campaign and membership gate',()=>{
 assert.equal(use().allowed,true);
 for(const delta of [{subjectId:'other'},{campaignId:'campaign-B'},{resourceId:'unrelated'}])assert.equal(use({request:delta}).allowed,false);
 for(const field of ['gmRoleActive','playerMembershipActive','sourceRevisionCurrent']){const f=fixture();f.owner.access[field]=false;assert.equal(decideAllowanceUse(f).allowed,false,field)}
});
test('SA04-10 revocation, epoch, ruleset and issuer subscription changes deny use',()=>{
 for(const delta of [{state:'revoked'},{grantEpoch:3},{entitlementRulesetVersion:'r1'}]){const f=fixture();Object.assign(f.owner.slot,delta);assert.equal(decideAllowanceUse(f).allowed,false)}
 for(const status of ['expired','revoked_refunded','account_hold']){const f=fixture();f.owner.verifiedGmSubscription.status=status;assert.equal(decideAllowanceUse(f).allowed,false)}
});
test('SA04-11 prohibited export, transfer, publication, source copy and offline use',()=>{
 for(const action of ['export-outside-campaign','transfer-restricted-character','copy-source','publish','entitlement.issue','use-in-other-campaign'])assert.equal(use({request:{action}}).allowed,false,action);
 assert.equal(use({request:{offline:true}}).allowed,false);
});
test('SA04-12 eligibility is NOT issuance; only owner DB transaction may reserve slot',()=>{
 const f=fixture();const req={issuerSubjectId:'gm',playerSubjectId:'player',campaignId:'campaign-A',rootReleaseId:'setting',rootKind:'custom-setting',now:'2026-11-01T00:00:00Z'};
 const answer=decideAllowanceIssuance({request:req,owner:f.owner});assert.equal(answer.allowed,true);assert.equal(answer.reason,'ELIGIBLE_FOR_ATOMIC_OWNER_TRANSACTION_ONLY');
 assert.equal(decideAllowanceIssuance({request:{...req,issuerSubjectId:'other'},owner:f.owner}).allowed,false);
 assert.equal(decideAllowanceIssuance({request:{...req,rootKind:'unknown'},owner:f.owner}).allowed,false);
 assert.equal(decideAllowanceIssuance({request:{...req,offline:true},owner:f.owner}).allowed,false);
});
test('SA04-13 closure digest cannot be reused if premium source substituted',()=>{
 const f=fixture();f.owner.slot.rootReleaseId='unrelated';assert.equal(decideAllowanceUse(f).allowed,false);
});
test('SA04-14 256-entry graph cap rejects deep/unbounded dependencies',()=>{
 const g={};for(let i=0;i<270;i++)g['n'+i]={version:'v1',active:true,rightsApproved:true,dependencies:i===269?[]:['n'+(i+1)]};
 assert.throws(()=>trustedDependencyClosure(g,'n0'),/DEPENDENCY_LIMIT/);
});
test('SA04-15 explore 1200 seeded adversarial flips without accidental transfer',()=>{
 let seed=725143;const rnd=()=>{seed=(1664525*seed+1013904223)>>>0;return seed;};
 for(let i=0;i<1200;i++){
  const f=fixture(),choice=rnd()%7;
  if(choice===0)f.request.campaignId='other';
  if(choice===1)f.request.subjectId='other';
  if(choice===2)f.request.action='transfer-restricted-character';
  if(choice===3)f.owner.access.gmRoleActive=false;
  if(choice===4)f.owner.access.playerMembershipActive=false;
  if(choice===5)f.owner.slot.grantEpoch=3;
  if(choice===6)f.owner.verifiedGmSubscription.status='expired';
  assert.equal(decideAllowanceUse(f).allowed,false,'iteration '+i);
 }
});
