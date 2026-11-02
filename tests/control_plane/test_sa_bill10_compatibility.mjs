import test,{before,after} from "node:test";
import assert from "node:assert/strict";
import {readFileSync,writeFileSync,mkdirSync,mkdtempSync,rmSync} from "node:fs";
import {join,dirname} from "node:path";
import {tmpdir} from "node:os";
import {fileURLToPath,pathToFileURL} from "node:url";
import {createHash} from "node:crypto";
import {spawnSync} from "node:child_process";
import {patchSource} from "./sa_bill09_source_patch.mjs";
import {protectedCommandBoundary,protectedEventBoundary} from "./sa_bill10_safe_boundary.mjs";

const here=dirname(fileURLToPath(import.meta.url));
const src=join(here,"../fixtures/sa-bill08/app-src");
const legacy=join(here,"../fixtures/sa-bill10/app-src");
const pin={
 "authorization/campaign-authorization-policy.ts":"b7b038b63774b7e4e8c1deb72c9ed09d35bc48b6",
 "session/hidden-information-response-filter.ts":"d948d92c06560fb9a560fcf4325ba4a258216e2a",
 "session/authoritative-session-command-handler.ts":"8b0ec123e99ccbbfc00fdc0c4e1e38aa42c71656"
};
const otherPins={
 "fixtures/session/p9-06-016-authoritative-command-handler.json":"cc4d195b905bf90a858c796f6dc28b35f6364024",
 "fixtures/session/p9-06-018-hidden-information-response-filter.json":"4dc7d0e8c0acefa48bd3f44adda84633fe68812e",
 "tools/verify_p9_06_016.py":"51d3b88b15b3a13f260ccd9f0bdd5fc6ffe47c60",
 "tools/verify_p9_06_018.py":"3954686a99de0307944cd1769c3b20c56aa8416e"
};
const hash=b=>createHash("sha1").update("blob "+b.length+"\0").update(b).digest("hex");
let temp,baseline,patched;
const command=(v={})=>({commandId:"c6",sessionId:"s1",actorId:"p1",expectedRevision:5,
    type:"roll",payload:{die:20,secret:"DO_NOT_LEAK"},submittedAt:"2026-11-02T00:00:00Z",...v});
const current=()=>({trustedCurrent:true,authenticatedSubjectId:"p1",activeCampaignId:"cx",
  sessionId:"s1",roleEpochCurrent:true,activeMembership:true,entitlementEpochCurrent:true,
  membership:{campaignId:"cx",subjectId:"p1",role:"player"}});
const state=()=>({sessionId:"s1",campaignId:"cx",campaignOwnerSubjectId:"gm",
  revision:6,lastSequence:10,processedCommandIds:["c6"]});
const receipt=()=>({commandId:"c6",accepted:true,resultingRevision:6,emittedEventIds:["event-c6"]});
const context=()=>({viewerSubjectId:"p1",sessionId:"s1",
  campaign:{campaignId:"cx",ownerSubjectId:"gm"},membership:{campaignId:"cx",subjectId:"p1",role:"player"}});
const events=()=>[
 {eventId:"public",sessionId:"s1",sequence:1,revision:1,type:"normal",payload:{ok:true},
  visibility:{kind:"public"},occurredAt:"2026-11-02T00:00:00Z"},
 {eventId:"hidden",sessionId:"s1",sequence:2,revision:2,type:"gm",payload:{secret:"GM_HIDDEN"},
  visibility:{kind:"gm_only"},occurredAt:"2026-11-02T00:00:00Z"},
];
async function load(sourceKind) {
 const out=join(temp,sourceKind);mkdirSync(out,{recursive:true});
 for(const rel of Object.keys(pin)){
  const b=readFileSync(join(src,rel));assert.equal(hash(b),pin[rel]);
  let contents=b.toString("utf8");
  if(sourceKind==="patched")contents=patchSource(rel,contents);
  contents=contents.replaceAll('"../authorization/campaign-authorization-policy"',
    '"../authorization/campaign-authorization-policy.ts"');
  const dest=join(out,"packages/contracts/src",rel);mkdirSync(dirname(dest),{recursive:true});writeFileSync(dest,contents);
 }
 for(const [rel,digest] of Object.entries(otherPins)){
  const b=readFileSync(join(legacy,rel));assert.equal(hash(b),digest);
  const dest=join(out,rel);mkdirSync(dirname(dest),{recursive:true});writeFileSync(dest,b);
 }
 // Exact original Python verification scripts and fixtures. Minimal workflow
 // sentinel is test scaffolding, not the actual app CI workflow.
 for(const id of ["016","018"]){
  const name="p9-06-"+id;
  const wf=join(out,".github/workflows/validate-"+name+".yml");
  mkdirSync(dirname(wf),{recursive:true});
  writeFileSync(wf,"name: isolated verifier fixture\n"+
    "run: python tools/verify_"+name.replaceAll("-","_")+".py\n"+
    "fixture: p9-06-018-hidden-information-response-filter.json\n");
 }
 return {
  root:out,
  handler:await import(pathToFileURL(join(out,"packages/contracts/src/session/authoritative-session-command-handler.ts")).href),
  filter:await import(pathToFileURL(join(out,"packages/contracts/src/session/hidden-information-response-filter.ts")).href)
 };
}
before(async()=>{temp=mkdtempSync(join(tmpdir(),"sa-bill10-"));baseline=await load("baseline");patched=await load("patched");});
after(()=>{if(temp)rmSync(temp,{recursive:true,force:true})});
test("SA10-01 actual source and legacy fixtures and verifiers remain blob-pinned",()=>{
 for(const [rel,digest] of Object.entries(otherPins))
  assert.equal(hash(readFileSync(join(legacy,rel))),digest);
});
test("SA10-02 existing P9-06-016 replay fixture succeeds in ORIGINAL implementation",()=>{
 const fixture=JSON.parse(readFileSync(join(legacy,"fixtures/session/p9-06-016-authoritative-command-handler.json")));
 const item=fixture.cases.find(c=>c.id==="duplicate-replayed");
 const r=baseline.handler.handleAuthoritativeSessionCommand(item.state,item.command,{
  membership:item.membership,existingReceipt:item.existingReceipt
 });
 assert.equal(r.accepted,true);assert.equal(r.replayed,true);
});
test("SA10-03 existing replay fixture FAILS under direct SA09 patch",()=>{
 const fixture=JSON.parse(readFileSync(join(legacy,"fixtures/session/p9-06-016-authoritative-command-handler.json")));
 const item=fixture.cases.find(c=>c.id==="duplicate-replayed");
 const r=patched.handler.handleAuthoritativeSessionCommand(item.state,item.command,{
  membership:item.membership,existingReceipt:item.existingReceipt
 });
 assert.equal(r.accepted,false);assert.equal(r.reason,"duplicate-without-receipt");
});
test("SA10-04 original generic event projection provides hidden count per legacy contract",()=>{
 const r=baseline.filter.filterSessionEventsForViewer(events(),context());
 assert.equal(r.ok,true);assert.equal(r.value.hiddenEventCount,1);
});
test("SA10-05 direct SA09 patch removes legacy generic hidden count",()=>{
 const r=patched.filter.filterSessionEventsForViewer(events(),context());
 assert.equal(r.ok,true);assert.equal("hiddenEventCount" in r.value,false);
});
test("SA10-06 existing Python validators pass BOTH incompatible behaviors: coverage gap",()=>{
 for(const variant of [baseline,patched]) {
  for(const id of ["016","018"]){
   const script="tools/verify_p9_06_"+id+".py";
   const run=spawnSync("python3",[join(variant.root,script)],{cwd:variant.root,encoding:"utf8"});
   assert.equal(run.status,0,JSON.stringify({variant:variant.root,id,stdout:run.stdout,stderr:run.stderr}));
  }
 }
});
test("SA10-07 additive A9 projection retains internal hidden count but exposes none",()=>{
 const native=baseline.filter.filterSessionEventsForViewer(events(),context());
 const result=protectedEventBoundary({events:events(),context:context(),
  owner:current(),filterA9:baseline.filter.filterSessionEventsForA9});
 assert.equal(native.value.hiddenEventCount,1);
 assert.equal(result.status,200);
 assert.equal("hiddenEventCount" in result.body,false);
 assert.equal(JSON.stringify(result).includes("GM_HIDDEN"),false);
});
test("SA10-08 wrapper preserves valid replay with persisted matching actor and command",()=>{
 const r=protectedCommandBoundary({state:state(),command:command(),
  owner:{...current(),persistedCommand:command(),persistedReceipt:receipt()},
  internalHandler:baseline.handler.handleAuthoritativeSessionCommand,
  safeProjection:baseline.handler.projectAcceptedSessionCommandForA9});
 assert.equal(r.status,200);assert.equal(r.body.replayed,true);
 assert.equal(JSON.stringify(r).includes("DO_NOT_LEAK"),false);
});
test("SA10-09 revoked member cannot fetch cached receipt through wrapped path",()=>{
 let called=0;
 const r=protectedCommandBoundary({state:state(),command:command(),
  owner:{...current(),activeMembership:false,persistedCommand:command(),persistedReceipt:receipt()},
  internalHandler:(...args)=>{called++;return baseline.handler.handleAuthoritativeSessionCommand(...args)},
  safeProjection:baseline.handler.projectAcceptedSessionCommandForA9});
 assert.equal(r.status,404);assert.equal(called,0);
});
test("SA10-10 replay payload actor receipt or owner mismatch denies before handler",()=>{
 const base={state:state(),command:command(),owner:{...current(),
   persistedCommand:command(),persistedReceipt:receipt()},
   internalHandler:()=>{throw Error("MUST NOT INVOKE")},
   safeProjection:baseline.handler.projectAcceptedSessionCommandForA9};
 for(const variant of [
   {command:command({payload:{die:6}})},
   {command:command({actorId:"p2"})},
   {command:command({commandId:"other"})},
   {owner:{...base.owner,persistedReceipt:{...receipt(),commandId:"other"}}},
   {owner:{...base.owner,persistedCommand:undefined}},
   {owner:{...base.owner,roleEpochCurrent:false}},
   {owner:{...base.owner,entitlementEpochCurrent:false}},
   {owner:{...base.owner,trustedCurrent:false}},
 ]){
   const r=protectedCommandBoundary({...base,...variant});
   assert.equal(r.status,404);
 }
});
test("SA10-11 fresh valid command preserves event internally, external strips payload",()=>{
 const st={...state(),processedCommandIds:[],revision:5};
 const r=protectedCommandBoundary({state:st,command:command(),owner:current(),
  internalHandler:baseline.handler.handleAuthoritativeSessionCommand,
  safeProjection:baseline.handler.projectAcceptedSessionCommandForA9});
 assert.equal(r.status,200);
 assert.equal(r.body.resultingRevision,6);
 assert.equal(JSON.stringify(r).includes("DO_NOT_LEAK"),false);
});
test("SA10-12 revoked viewer or cross-session request blocks external event projection",()=>{
 for(const owner of [
   {...current(),activeMembership:false},
   {...current(),roleEpochCurrent:false},
   {...current(),authenticatedSubjectId:"intruder"},
   {...current(),sessionId:"other"},
   {...current(),entitlementEpochCurrent:false},
 ]){
  const r=protectedEventBoundary({events:events(),context:context(),owner,
   filterA9:baseline.filter.filterSessionEventsForA9});
  assert.equal(r.status,404);
 }
});
test("SA10-13 Python static-verifier green does not prove TypeScript fixture replay",()=>{
 const py18=readFileSync(join(legacy,"tools/verify_p9_06_018.py"),"utf8");
 assert.ok(py18.includes('"hiddenEventCount"'));
 assert.ok(py18.includes('"hidden": len(events) - len(visible)'));
 const py16=readFileSync(join(legacy,"tools/verify_p9_06_016.py"),"utf8");
 assert.ok(py16.includes('"duplicate-replayed"'));
 assert.ok(py16.includes('"replayed: true"'));
});
