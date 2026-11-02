/**
 * SA-BILL-08 pinned actual-app-source characterization AND synthetic endpoint
 * negative integrations. Not a live API / production WSS, AI or search test.
 * Only the 3 source characterization functions are copied verbatim from app.
 * The single import specifier is patched in a throwaway Node module directory
 * for Node's extension resolution, AFTER exact Git-blob checks.
 */
import test,{before,after} from "node:test";
import assert from "node:assert/strict";
import {readFileSync,writeFileSync,mkdtempSync,mkdirSync,rmSync} from "node:fs";
import {tmpdir} from "node:os";
import {join,dirname} from "node:path";
import {pathToFileURL,fileURLToPath} from "node:url";
import {createHash} from "node:crypto";
import {SyntheticOwnerService,SyntheticEndpointSurface} from "./sa_bill08_boundary_gateway.mjs";
import {trustedDependencyClosure} from "./sa_bill04_reference.mjs";

const here=dirname(fileURLToPath(import.meta.url));
const base=join(here,"../fixtures/sa-bill08/app-src");
const pinned={
  "authorization/campaign-authorization-policy.ts":"b7b038b63774b7e4e8c1deb72c9ed09d35bc48b6",
  "session/hidden-information-response-filter.ts":"d948d92c06560fb9a560fcf4325ba4a258216e2a",
  "session/authoritative-session-command-handler.ts":"8b0ec123e99ccbbfc00fdc0c4e1e38aa42c71656",
};
const sourceModules={};
let tmp,filterModule,commandModule;
const hashBlob = b => createHash("sha1").update("blob "+b.length+"\0").update(b).digest("hex");
const at="2026-11-01T12:00:00Z";
const gmPaid=()=>({origin:"verified-billing-ledger",payerSubjectId:"gm",
  boundSubjectId:"gm",provider:"synthetic-test-provider",purchaseBindingId:"fake-bound",
  productId:"fake-SKU",sourceRevision:"rev1",status:"verified_active",
  entitledFrom:"2026-10-01T00:00:00Z",entitledUntil:"2026-12-01T00:00:00Z"});
const registered=()=>({
  setting:{version:"v1",kind:"custom-setting",active:true,rightsApproved:true,
    canUseInCampaign:true,ownerAllowedAsGrantRoot:true,dependencies:["relic","tree"]},
  relic:{version:"v1",kind:"registered-item-set",active:true,rightsApproved:true,
    canUseInCampaign:true,dependencies:[]},
  tree:{version:"v1",kind:"registered-ability-tree",active:true,rightsApproved:true,
    canUseInCampaign:true,dependencies:[]},
  unrelated:{version:"v1",kind:"registered-species",active:true,rightsApproved:true,
    canUseInCampaign:true,dependencies:[]},
});
function fixture() {
  const registry=registered(),dig=trustedDependencyClosure(registry,"setting").digest;
  const ownerState={
    registry,slot:{rootReleaseId:"setting",closureDigest:dig,campaignId:"X",
      playerSubjectId:"p1",issuerGmSubjectId:"gm",state:"active",
      grantEpoch:4,entitlementRulesetVersion:"v1"},
    access:{currentGmSubjectId:"gm",gmRoleActive:true,playerMembershipActive:true,
      sourceRevisionCurrent:true,currentGrantEpoch:4,
      campaignId:"X",playerSubjectId:"p1",entitlementRulesetVersion:"v1"},
    verifiedGmSubscription:gmPaid(),
  };
  const resources={
    character:{id:"character",campaignId:"X",ownerSubjectId:"p1",
      safeLabel:"Hero",protectedPayload:"RESTRICTED HERO STATS",selfAuthoredRawNote:"My independently written biography",
      sourceReleaseId:null,dependencies:["weapon"]},
    weapon:{id:"weapon",campaignId:"X",ownerSubjectId:"gm",
      safeLabel:"Sponsored relic",protectedPayload:"LICENSED RELIC DATA",
      ownerRestricted:true,sourceReleaseId:"relic",dependencies:["power"]},
    power:{id:"power",campaignId:"X",ownerSubjectId:"gm",safeLabel:"Gifted ability",
      protectedPayload:"LICENSED ABILITY DATA",ownerRestricted:true,
      sourceReleaseId:"tree",dependencies:[]},
    unrelated:{id:"unrelated",campaignId:"X",ownerSubjectId:"gm",safeLabel:"Unrelated premium",
      protectedPayload:"UNLICENSED PACK",ownerRestricted:true,
      sourceReleaseId:"unrelated",dependencies:[]},
    other:{id:"other",campaignId:"X",ownerSubjectId:"p2",safeLabel:"Another Hero",
      protectedPayload:"OTHER PLAYER SECRET",sourceReleaseId:null,dependencies:[]},
    elsewhere:{id:"elsewhere",campaignId:"Y",ownerSubjectId:"gm",safeLabel:"Other Campaign relic",
      protectedPayload:"OTHER CAMPAIGN SECRET",sourceReleaseId:"relic",dependencies:[]},
  };
  const owner=new SyntheticOwnerService({accounts:{
    "good-token":{subjectId:"p1",campaignId:"X"},
    "p2-token":{subjectId:"p2",campaignId:"X"},
    "other-campaign-token":{subjectId:"p1",campaignId:"Y"},
  },resources,ownerState});
  return {owner,surface:new SyntheticEndpointSurface(owner)};
}
const req=(extra={})=>({token:"good-token",campaignId:"X",resourceId:"character",now:at,epoch:4,...extra});
before(async()=>{
  tmp=mkdtempSync(join(tmpdir(),"sa-bill08-app-"));
  for(const [rel,digest] of Object.entries(pinned)){
    const raw=readFileSync(join(base,rel));
    assert.equal(hashBlob(raw),digest,"actual app blob drifted: "+rel);
    sourceModules[rel]=raw.toString("utf8");
    const dest=join(tmp,rel);mkdirSync(dirname(dest),{recursive:true});
    // Import-only rewrite; original bytes/digest remain separately pinned.
    const patched=raw.toString("utf8").replaceAll(
      '"../authorization/campaign-authorization-policy"',
      '"../authorization/campaign-authorization-policy.ts"');
    writeFileSync(dest,patched);
  }
  filterModule=await import(pathToFileURL(join(tmp,"session/hidden-information-response-filter.ts")).href);
  commandModule=await import(pathToFileURL(join(tmp,"session/authoritative-session-command-handler.ts")).href);
});
after(()=>{if(tmp)rmSync(tmp,{recursive:true,force:true});});
const context=(membership)=>({
  viewerSubjectId:"player",sessionId:"s1",
  campaign:{campaignId:"X",ownerSubjectId:"gm"},
  membership,
});
const event=(id,visibility,payload)=>({eventId:id,sessionId:"s1",
  sequence:1,revision:1,type:"fixture",payload,visibility,
  occurredAt:at});
const roleMember=(subject="player",role="player")=>({subjectId:subject,campaignId:"X",role});

test("SA08-01 all three unmodified application source Git blob IDs are exact",()=>{
  for(const [rel,digest] of Object.entries(pinned))
    assert.equal(hashBlob(readFileSync(join(base,rel))),digest);
});
test("SA08-02 actual app generic hidden event filter exposes hidden-event cardinality",()=>{
  const events=[event("public",{kind:"public"},{safe:"ok"}),
    event("secret",{kind:"gm_only"},{secret:"GM ONLY DATA"})];
  const r=filterModule.filterSessionEventsForViewer(events,context(roleMember()));
  assert.equal(r.ok,true);assert.deepEqual(r.value.visibleEvents.map(x=>x.eventId),["public"]);
  assert.equal(r.value.hiddenEventCount,1); // known lower-level exposure
});
test("SA08-03 actual app A9 wrapper removes hidden count and secret payload",()=>{
  const events=[event("public",{kind:"public"},{safe:"ok"}),
    event("secret",{kind:"gm_only"},{secret:"GM ONLY DATA"})];
  const r=filterModule.filterSessionEventsForA9(events,context(roleMember()));
  assert.equal(r.ok,true);assert.ok(!("hiddenEventCount" in r.value));
  assert.ok(!JSON.stringify(r).includes("GM ONLY DATA"));
});
test("SA08-04 actual app denies missing membership and cross-session event batch",()=>{
  const events=[event("public",{kind:"public"},{safe:"ok"})];
  assert.equal(filterModule.filterSessionEventsForViewer(events,context()).ok,false);
  const cross=[{...events[0],sessionId:"s2"}];
  assert.equal(filterModule.filterSessionEventsForViewer(cross,context(roleMember())).ok,false);
});
test("SA08-05 actual lower-level handler emits accepted command payload as public event",()=>{
  const state={sessionId:"s1",campaignId:"X",campaignOwnerSubjectId:"gm",
    revision:1,lastSequence:1,processedCommandIds:[]};
  const command={commandId:"c1",sessionId:"s1",actorId:"player",
    expectedRevision:1,type:"scenario",payload:{untrustedSecret:"PRIVATE COMMAND BYTES"},submittedAt:at};
  const r=commandModule.handleAuthoritativeSessionCommand(state,command,{membership:roleMember()});
  assert.equal(r.accepted,true);
  assert.equal(r.events[0].visibility.kind,"public");
  assert.ok(JSON.stringify(r.events).includes("PRIVATE COMMAND BYTES"));
  const safe=commandModule.projectAcceptedSessionCommandForA9(r);
  assert.ok(!JSON.stringify(safe).includes("PRIVATE COMMAND BYTES"));
});
test("SA08-06 actual lower-level replay branch accepts cached receipt before membership authorization",()=>{
  const state={sessionId:"s1",campaignId:"X",campaignOwnerSubjectId:"gm",revision:2,lastSequence:2,
    processedCommandIds:["c1"]};
  const command={commandId:"c1",sessionId:"s1",actorId:"former-player",
    expectedRevision:1,type:"fixture",payload:{secret:"REPLAY"},submittedAt:at};
  const r=commandModule.handleAuthoritativeSessionCommand(state,command,{
    membership:undefined,existingReceipt:{
      commandId:"c1",accepted:true,resultingRevision:2,emittedEventIds:["e1"]},
  });
  assert.equal(r.accepted,true);assert.equal(r.replayed,true);
  // A genuine server endpoint must reauthorize before replay receipt exposure.
});
test("SA08-07 synthetic authorized REST read returns only requested resource",()=>{
  const {surface}=fixture();const res=surface.directRead(req());
  assert.equal(res.status,200);assert.equal(res.body.payload,"RESTRICTED HERO STATS");
  assert.ok(!JSON.stringify(res).includes("LICENSED RELIC DATA"));
});
test("SA08-08 synthetic direct guessed ID has same safe denial for different subject and campaign",()=>{
  const {surface}=fixture();
  for(const r of [req({token:"p2-token"}),req({campaignId:"Y"}),req({resourceId:"missing"})]){
    assert.deepEqual(surface.directRead(r),{status:404,body:{error:"not-found-or-forbidden"}});
  }
});
test("SA08-09 synthetic search and count strip unauthorized names, IDs and hidden cardinality",()=>{
  const {surface}=fixture();
  assert.deepEqual(surface.search({...req(),query:"Unrelated"}),{results:[]});
  assert.deepEqual(surface.searchCount({...req(),query:"Unrelated"}),{count:0});
  const full=surface.search({...req(),query:"Hero"});
  assert.deepEqual(full,{results:[{id:"character",safeLabel:"Hero"}]});
});
test("SA08-10 synthetic AI retrieval never includes unrelated premium or other-player bytes",()=>{
  const {surface}=fixture(),result=surface.aiRetrieve(req());
  const json=JSON.stringify(result);
  assert.ok(json.includes("RESTRICTED HERO STATS"));
  assert.ok(!json.includes("UNLICENSED PACK"));
  assert.ok(!json.includes("OTHER PLAYER SECRET"));
  assert.ok(!json.includes("OTHER CAMPAIGN SECRET"));
});
test("SA08-11 synthetic WSS event stream drops material after current GM role revocation",()=>{
  const {owner,surface}=fixture();
  assert.equal(surface.wssPoll(req()).events.length,1);
  owner.revokeGm();
  assert.deepEqual(surface.wssPoll(req()),{events:[]});
});
test("SA08-12 synthetic GM downgrade revokes direct REST, search, counts, AI and WSS",()=>{
  const {owner,surface}=fixture();owner.revokeGm();
  assert.equal(surface.directRead(req()).status,404);
  assert.deepEqual(surface.search({...req(),query:"Hero"}),{results:[]});
  assert.deepEqual(surface.searchCount({...req(),query:"Hero"}),{count:0});
  assert.deepEqual(surface.aiRetrieve(req()),{context:[]});
  assert.deepEqual(surface.wssPoll(req()),{events:[]});
});
test("SA08-13 synthetic subscription refund, Player removal and stale grant epoch deny",()=>{
  for(const f of [x=>x.owner.revokeSubscription(),x=>x.owner.revokeMembership(),x=>x.owner.rotateEpoch()]){
    const x=fixture();f(x);assert.equal(x.surface.directRead(req()).status,404);
  }
});
test("SA08-14 synthetic nested unauthorized release taints entire derived character",()=>{
  const x=fixture();x.owner.resources.weapon.dependencies.push("unrelated");
  assert.equal(x.surface.directRead(req()).status,404);
  assert.deepEqual(x.surface.aiRetrieve(req()),{context:[]});
});
test("SA08-15 synthetic cross-campaign dependency and cycle prevent projections",()=>{
  for(const child of ["elsewhere","character"]){
    const x=fixture();x.owner.resources.power.dependencies.push(child);
    assert.equal(x.surface.directRead(req()).status,404,child);
  }
});
test("SA08-16 synthetic source owner revocation or altered version denies derived character",()=>{
  const x=fixture();x.owner.ownerState.registry.tree.rightsApproved=false;
  assert.equal(x.surface.directRead(req()).status,404);
  const y=fixture();y.owner.ownerState.registry.relic.version="v2";
  assert.equal(y.surface.directRead(req()).status,404);
});
test("SA08-17 synthetic external export and Character transfer denied, not retroactively licensed",()=>{
  const {surface}=fixture();
  for(const action of ["export-outside-campaign","transfer-restricted-character","download-protected-asset"])
    assert.equal(surface.export({...req(),action}).status,403);
});
test("SA08-18 synthetic personal raw-note recovery retains independent authorship on lapse",()=>{
  const {surface,owner}=fixture();owner.revokeSubscription();
  assert.equal(surface.directRead(req()).status,404);
  const recovered=surface.recoverOwnRawNote(req());
  assert.deepEqual(recovered,{status:200,body:{rawNote:"My independently written biography"}});
  assert.equal(surface.recoverOwnRawNote(req({token:"p2-token"})).status,404);
});
test("SA08-19 synthetic frontend claims never override canonical source owner state",()=>{
  const x=fixture();x.owner.revokeGm();
  assert.equal(x.surface.directRead(req({clientFlags:{
    gmSubscriptionActive:true,playerMember:true,role:"gm",grantEpoch:999}})).status,404);
});
test("SA08-20 synthetic command replay is denied BEFORE calling vulnerable actual lower-level branch",()=>{
  const x=fixture();x.owner.revokeMembership();let called=0;
  const r=x.surface.command(req(),()=>{called++;return{accepted:true,receipt:{commandId:"c1"},replayed:true}});
  assert.equal(r.status,404);assert.equal(called,0);
});
test("SA08-21 fixture denial survives 700 seeded hostile surface/action combinations",()=>{
  let seed=4070526;
  const next=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed;};
  for(let i=0;i<700;i++){
    const x=fixture(),which=next()%7;
    if(which===0)x.owner.revokeGm();
    if(which===1)x.owner.revokeMembership();
    if(which===2)x.owner.revokeSubscription();
    if(which===3)x.owner.rotateEpoch();
    if(which===4)x.owner.ownerState.registry.tree.rightsApproved=false;
    if(which===5)x.owner.resources.weapon.dependencies.push("unrelated");
    if(which===6)x.owner.resources.power.dependencies.push("elsewhere");
    assert.equal(x.surface.directRead(req()).status,404,"case "+i);
    assert.deepEqual(x.surface.searchCount({...req(),query:"Hero"}),{count:0},"case "+i);
  }
});
