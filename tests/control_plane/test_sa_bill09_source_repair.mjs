/**
 * SA-BILL-09 TEST-FIRST historical-app-source hardening proposal.
 * Baseline mode: assertion failures document source deficiencies (RED).
 * Fixed mode: apply research-only patch to temporary copies (GREEN).
 * Neither mode modifies or deploys the Multiversal-app repository.
 *
 * Run RED:  SA_BILL09_MODE=baseline node --experimental-strip-types --test tests/control_plane/test_sa_bill09_source_repair.mjs
 * Run GREEN: SA_BILL09_MODE=fixed node --experimental-strip-types --test tests/control_plane/test_sa_bill09_source_repair.mjs
 */
import test,{before,after} from "node:test";
import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {readFileSync,mkdtempSync,mkdirSync,writeFileSync,rmSync} from "node:fs";
import {tmpdir} from "node:os";
import {dirname,join} from "node:path";
import {fileURLToPath,pathToFileURL} from "node:url";

const here=dirname(fileURLToPath(import.meta.url)),root=join(here,"../fixtures/sa-bill08/app-src");
const paths={
 "authorization/campaign-authorization-policy.ts":"b7b038b63774b7e4e8c1deb72c9ed09d35bc48b6",
 "session/hidden-information-response-filter.ts":"d948d92c06560fb9a560fcf4325ba4a258216e2a",
 "session/authoritative-session-command-handler.ts":"8b0ec123e99ccbbfc00fdc0c4e1e38aa42c71656",
};
const hashBlob=b=>createHash("sha1").update("blob "+b.length+"\0").update(b).digest("hex");
const fixed=process.env.SA_BILL09_MODE==="fixed";
let temp,handle,filter;
before(async()=>{
 temp=mkdtempSync(join(tmpdir(),"sa-bill09-"));
 let patchSource=null;
 if(fixed)({patchSource}=await import("./sa_bill09_source_patch.mjs"));
 for(const [rel,sha] of Object.entries(paths)){
  const raw=readFileSync(join(root,rel));
  assert.equal(hashBlob(raw),sha,rel+" pinned app source unexpectedly changed");
  let source=raw.toString("utf8");
  if(fixed)source=patchSource(rel,source);
  // Loader-only import extension repair, not counted as semantic patch.
  source=source.replaceAll('"../authorization/campaign-authorization-policy"',
        '"../authorization/campaign-authorization-policy.ts"');
  const out=join(temp,rel);mkdirSync(dirname(out),{recursive:true});writeFileSync(out,source);
 }
 handle=await import(pathToFileURL(join(temp,"session/authoritative-session-command-handler.ts")).href);
 filter=await import(pathToFileURL(join(temp,"session/hidden-information-response-filter.ts")).href);
});
after(()=>{if(temp)rmSync(temp,{recursive:true,force:true})});
const at="2026-11-01T18:00:00Z";
const membership=(subject="p1",role="player")=>({subjectId:subject,campaignId:"X",role});
const state=(overrides={})=>({
 sessionId:"S",campaignId:"X",campaignOwnerSubjectId:"gm",revision:4,lastSequence:4,
 processedCommandIds:[],...overrides,
});
const command=(overrides={})=>({
 commandId:"cmd1",sessionId:"S",actorId:"p1",type:"secret-gear-choice",
 expectedRevision:4,submittedAt:at,
 payload:{sourceData:"GM_LICENSING_SECRET_DO_NOT_FORWARD"},...overrides,
});
const receipt=()=>({commandId:"cmd1",accepted:true,resultingRevision:4,emittedEventIds:["e1"]});
const replay=(overrides={},ctx={})=>{
 const original=command();
 return handle.handleAuthoritativeSessionCommand(
   state({processedCommandIds:["cmd1"]}),command(overrides),{
    membership:membership(),existingReceipt:receipt(),
    originalAcceptedCommand:original,...ctx,
   });
};
const context=(membershipInput=membership())=>({
 viewerSubjectId:"p1",sessionId:"S",
 campaign:{campaignId:"X",ownerSubjectId:"gm"},membership:membershipInput,
});
const e=(id,visibility,payload)=>({
 eventId:id,sessionId:"S",sequence:1,revision:1,type:"fixture",payload,
 occurredAt:at,visibility,
});
test("SA09-01 original app source blobs exactly pinned",()=>{
 for(const [p,hash] of Object.entries(paths))assert.equal(hashBlob(readFileSync(join(root,p))),hash);
});
test("SA09-02 replay without current Campaign membership must be unauthorized",()=>{
 const r=replay({}, {membership:undefined});
 assert.equal(r.accepted,false);
 assert.equal(r.reason,"unauthorized");
});
test("SA09-03 replay with another actor is rejected even with same command ID",()=>{
 const r=replay({actorId:"p2"},{membership:membership("p2")});
 assert.equal(r.accepted,false);
 assert.equal(r.reason,"duplicate-without-receipt");
});
test("SA09-04 replay with changed payload cannot reuse a prior receipt",()=>{
 const r=replay({payload:{sourceData:"DIFFERENT"}});assert.equal(r.accepted,false);
});
test("SA09-05 replay with forged different receipt command ID is rejected",()=>{
 const r=replay({}, {existingReceipt:{...receipt(),commandId:"other-command"}});
 assert.equal(r.accepted,false);
});
test("SA09-06 replay without server persisted original accepted command is denied",()=>{
 const r=replay({}, {originalAcceptedCommand:undefined});
 assert.equal(r.accepted,false);
});
test("SA09-07 true current, same actor+body, authenticated idempotent replay remains valid",()=>{
 const r=replay();assert.equal(r.accepted,true);
 assert.equal(r.replayed,true);assert.equal(r.events.length,0);
 assert.equal(r.receipt.commandId,"cmd1");
});
test("SA09-08 generic public accepted event must not include raw command body",()=>{
 const r=handle.handleAuthoritativeSessionCommand(state(),command(),{membership:membership()});
 assert.equal(r.accepted,true);
 assert.equal(r.events[0].visibility.kind,"public");
 assert.equal(JSON.stringify(r.events).includes("GM_LICENSING_SECRET_DO_NOT_FORWARD"),false);
 assert.equal(Object.hasOwn(r.events[0].payload,"commandPayload"),false);
});
test("SA09-09 authorized A9 event projection also omits protected payload",()=>{
 const r=handle.handleAuthoritativeSessionCommand(state(),command(),{membership:membership()});
 const safe=handle.projectAcceptedSessionCommandForA9(r);
 assert.equal(JSON.stringify(safe).includes("GM_LICENSING_SECRET_DO_NOT_FORWARD"),false);
});
test("SA09-10 generic event projection must omit hidden cardinality",()=>{
 const events=[e("public",{kind:"public"},{ok:1}),
    e("secret",{kind:"gm_only"},{secret:"HIDDEN_GM_DATA"})];
 const r=filter.filterSessionEventsForViewer(events,context());
 assert.equal(r.ok,true);
 assert.equal(r.value.visibleEvents.length,1);
 assert.equal("hiddenEventCount" in r.value,false);
 assert.equal(JSON.stringify(r).includes("HIDDEN_GM_DATA"),false);
});
test("SA09-11 A9 event projection must omit protected payload and count",()=>{
 const events=[e("public",{kind:"public"},{ok:1}),
    e("secret",{kind:"gm_only"},{secret:"HIDDEN_GM_DATA"})];
 const r=filter.filterSessionEventsForA9(events,context());
 assert.equal(r.ok,true);assert.equal("hiddenEventCount" in r.value,false);
 assert.equal(JSON.stringify(r).includes("HIDDEN_GM_DATA"),false);
});
test("SA09-12 GM still sees GM-only payload when independently authorized",()=>{
 const events=[e("secret",{kind:"gm_only"},{secret:"GM_ONLY"})];
 const r=filter.filterSessionEventsForViewer(events,context(membership("p1","gm")));
 assert.equal(r.ok,true);assert.equal(r.value.visibleEvents.length,1);
});
test("SA09-13 outsider and cross-Session input still fail closed",()=>{
 const events=[e("public",{kind:"public"},{ok:1})];
 const denied=filter.filterSessionEventsForViewer(events,context(undefined));
 // context(undefined) uses default membership; explicit missing below.
 const noMember={...context(),membership:undefined};
 assert.equal(filter.filterSessionEventsForViewer(events,noMember).ok,false);
 assert.equal(filter.filterSessionEventsForViewer(
   [{...events[0],sessionId:"OTHER"}],context()).ok,false);
});
test("SA09-14 fresh authorized command retains idempotency and revision semantics",()=>{
 const r=handle.handleAuthoritativeSessionCommand(state(),command(),{membership:membership()});
 assert.equal(r.accepted,true);assert.equal(r.nextState.revision,5);
 const stale=handle.handleAuthoritativeSessionCommand(state(),command({expectedRevision:2}),{membership:membership()});
 assert.equal(stale.accepted,false);assert.equal(stale.reason,"stale-revision");
});
test("SA09-15 malformed or cross-session commands denied before replay",()=>{
 const cross=handle.handleAuthoritativeSessionCommand(state({processedCommandIds:["cmd1"]}),command({sessionId:"OTHER"}),{
  membership:membership(),existingReceipt:receipt(),originalAcceptedCommand:command(),
 });
 assert.equal(cross.accepted,false);assert.equal(cross.reason,"wrong-session");
});
