import test from "node:test";
import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {SessionLab,FictionalEconomyLab,dependencyClosure,canTransferDefinition,featureCensus,auditParity,
 validateInstallerPreflight,syntheticGoldenRun} from "./prep-model.mjs";
const golden=JSON.parse(readFileSync(new URL("./golden-campaign.json",import.meta.url),"utf8"));
const make=()=>new SessionLab();

test("PREP02 proposed action never mutates HP before GM adjudicates",()=>{
 const s=make(),original=s.s.hp.guardian;
 const p=s.proposal({commandId:"c1",actor:"Raven2",kind:"strike",target:"guardian",cost:1,expectedRevision:0});
 assert.equal(p.actor,"Raven2");assert.equal(s.s.hp.guardian,original);
 assert.throws(()=>s.adjudicate({commandId:"c1",gm:"Raven2",decision:"approve"}),/GM_ONLY/);
 const r=s.adjudicate({commandId:"c1",gm:"Raven1",decision:"approve",roll:18});
 assert.equal(r.roll,18);assert.equal(s.s.hp.guardian,original-2);assert.equal(s.s.stamina.Raven2,3);
 assert.equal(s.adjudicate({commandId:"c1",gm:"Raven1",decision:"approve",roll:18}).commandId,"c1");
 assert.equal(s.s.hp.guardian,original-2);
});
test("PREP02 duplicate command is idempotent, altered content conflicts and stale revision fails",()=>{
 const s=make(),c={commandId:"same",actor:"Raven2",kind:"inspect",target:"sigil",cost:0,expectedRevision:0};
 assert.equal(s.proposal(c).commandId,"same");assert.equal(s.proposal(c).commandId,"same");
 assert.throws(()=>s.proposal({...c,target:"treasure"}),/COMMAND_CONFLICT/);
 assert.throws(()=>s.proposal({...c,commandId:"new"}),/STALE_REVISION/);
 assert.throws(()=>s.proposal({...c,actor:"stranger",commandId:"bad"}),/NOT_MEMBER/);
});
test("PREP02 GM-only hidden decision preserves event sequence with withheld projection",()=>{
 const s=make();
 s.proposal({commandId:"inspect",actor:"Raven2",kind:"inspect",target:"clue",cost:0,expectedRevision:0});
 s.adjudicate({commandId:"inspect",gm:"Raven1",decision:"approve",roll:5});
 const player=s.project("Raven2"),gm=s.project("Raven1");
 assert.equal(player.sequence,2);assert.deepEqual(player.events.map(e=>e.sequence),[1,2]);
 assert.equal(player.events[0].kind,"withheld");assert.equal(player.events[1].kind,"withheld");
 assert.equal(gm.events[0].kind,"proposal");assert.equal(gm.events[1].kind,"decision");
});
test("PREP02 resume detects altered checkpoint and protects one canonical synthetic sequence",()=>{
 const s=make();const p=s.checkpoint();
 assert.equal(SessionLab.restore(p).s.sequence,0);
 p.state.hp.guardian=0;assert.throws(()=>SessionLab.restore(p),/TAMPER/);
});
test("PREP03 staged adventure has six deterministic phases and unchanged replay fingerprint",()=>{
 const a=syntheticGoldenRun(golden),b=syntheticGoldenRun(golden);
 assert.equal(a.status,"SIMULATED_ONLY");assert.equal(a.events,5);
 assert.equal(a.checkpoint,b.checkpoint);assert.equal(a.phase,"completed");
 const bad={...golden,steps:[...golden.steps]};bad.steps[0]={...bad.steps[0],from:"combat"};
 assert.throws(()=>syntheticGoldenRun(bad),/BAD_TRANSITION/);
});
test("PREP04 Campaign wager affects only imaginary campaign ledger",()=>{
 const l=new FictionalEconomyLab();
 l.place({id:"w1",actor:"Raven2",mode:"campaign",stake:{kind:"fictional-credits",amount:10},market:"race-1"});
 assert.equal(l.balance("campaign","Raven2"),90);assert.equal(l.balance("free","Raven2"),100);
 const r=l.settle({id:"w1",result:"win",ownerReceipt:{id:"race-result-1",verifiedFixture:true,market:"race-1"},regulator:"off"});
 assert.equal(r.levy,0);assert.equal(l.balance("campaign","Raven2"),110);
 assert.equal(l.settle({id:"w1",result:"win",ownerReceipt:{id:"race-result-1",verifiedFixture:true,market:"race-1"}}).net,20);
 assert.equal(l.balance("campaign","Raven2"),110);
});
test("PREP04 Free Play resets in isolated wallet, not campaign assets",()=>{
 const l=new FictionalEconomyLab();
 l.place({id:"w2",actor:"Raven2",mode:"free",stake:{kind:"fictional-credits",amount:20},market:"table-1"});
 assert.equal(l.balance("free","Raven2"),80);l.resetFree("Raven2");
 assert.equal(l.balance("free","Raven2"),100);assert.equal(l.balance("campaign","Raven2"),100);
});
test("PREP04 real-money, purchased/convertible stakes and forged event receipts denied",()=>{
 const l=new FictionalEconomyLab();
 for(const stake of [{kind:"real-money",amount:1},{kind:"subscription-token",amount:1},{kind:"fictional-credits",amount:3,redeemable:true},
 {kind:"fictional-credits",amount:3,purchased:true}]){
  assert.throws(()=>l.place({id:"x"+stake.kind+JSON.stringify(stake),actor:"Raven2",mode:"campaign",stake,market:"race"}),/DENIED/);
 }
 l.place({id:"verified",actor:"Raven2",mode:"campaign",stake:{kind:"fictional-credits",amount:5},market:"race"});
 assert.throws(()=>l.settle({id:"verified",result:"win",ownerReceipt:{id:"fake",market:"race"}}),/NO_OWNER_RESULT/);
 assert.throws(()=>l.place({id:"verified",actor:"Raven2",mode:"free",stake:{kind:"fictional-credits",amount:5},market:"race"}),/REPLAY_CHANGED/);
});
test("PREP04 MRC full overlay adds optional fictional levy, off preserves market",()=>{
 const l=new FictionalEconomyLab();
 for(const id of ["off","full"])l.place({id,actor:"Raven1",mode:"campaign",stake:{kind:"fictional-credits",amount:10},market:"mrc-race"});
 const a=l.settle({id:"off",result:"win",ownerReceipt:{id:"r-off",verifiedFixture:true,market:"mrc-race"},regulator:"off"});
 const b=l.settle({id:"full",result:"win",ownerReceipt:{id:"r-full",verifiedFixture:true,market:"mrc-race"},regulator:"full"});
 assert.equal(a.levy,0);assert.equal(b.levy,2);assert.equal(l.house,2);
});
test("PREP05 transitive dependency root closure and rejection of cyclic/missing/unlicensed pack",()=>{
 const n=(required=[],extra={})=>({required,trusted:true,licensed:true,...extra});
 assert.deepEqual(dependencyClosure({setting:n(["species","tree"]),species:n(["core"]),tree:n(["core"]),core:n([])},"setting"),["core","setting","species","tree"]);
 assert.throws(()=>dependencyClosure({a:n(["b"]),b:n(["a"])},"a"),/CYCLE/);
 assert.throws(()=>dependencyClosure({a:n(["b"])},"a"),/MISSING/);
 assert.throws(()=>dependencyClosure({a:n(["b"]),b:n([],{licensed:false})},"a"),/UNTRUSTED/);
});
test("PREP05 restricted nested lineage never becomes freely transferable through rewrap",()=>{
 const target={subject:"Raven2",rightsVerified:true};
 assert.equal(canTransferDefinition({owner:"Raven2",provenanceKnown:true,restricted:true},target),false);
 assert.equal(canTransferDefinition({owner:"Raven2",provenanceKnown:true,nestedRestricted:true},target),false);
 assert.equal(canTransferDefinition({owner:"Raven2",provenanceKnown:false},target),false);
 assert.equal(canTransferDefinition({owner:"Raven2",provenanceKnown:true},target),true);
});
test("PREP05 source observed does not count as product integrated",()=>{
 const a=featureCensus([{id:"APW",path:"apw",owner:"APW"},{id:"KFR",path:"kfr",owner:"KFR",productRouteEvidence:true,ownerProof:true}]);
 assert.equal(a[0].disposition,"source-observed-not-integrated");
 assert.equal(a[1].disposition,"candidate-integrated-needs-runtime");
 assert.throws(()=>featureCensus([{id:"S",path:"p",owner:"x"},{id:"S",path:"p2",owner:"y"}]),/DUPLICATE/);
});
test("PREP06 same player GM creator actions and accessibility on phone and desktop",()=>{
 const screens=["player","gm","creator"].map(id=>({id,phoneActions:["save","inspect","submit"],desktopActions:["submit","inspect","save"],focusVisible:true,keyboardFallback:true,screenReaderLabel:true,touchTargetPx:44,precisionDragOnly:false}));
 assert.equal(auditParity(screens).ok,true);
 assert.deepEqual(auditParity([{...screens[0],phoneActions:["save"],precisionDragOnly:true}]).defects,
 ["player:ACTION_MISMATCH","player:DRAG_ONLY"]);
 assert.equal(auditParity([{...screens[1],touchTargetPx:40}]).ok,false);
});
test("PREP07 mock installer hashes are only preflight, never certified installs",()=>{
 const p={platform:"win",sourceHead:"abc",buildId:"mock-1",sha256:"a".repeat(64)};
 assert.deepEqual(validateInstallerPreflight(p),{ok:false,reason:"NOT_INSTALLED_VERIFICATION",preflightOnly:true});
 assert.equal(validateInstallerPreflight({...p,sha256:"not-hex"}).reason,"MISSING_PACKAGE_PROVENANCE");
});
