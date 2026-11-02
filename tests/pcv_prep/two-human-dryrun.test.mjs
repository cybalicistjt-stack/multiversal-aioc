import test from "node:test";
import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {twoHumanFixtureRun} from "./two-human-dryrun.mjs";
const fixture=JSON.parse(readFileSync(new URL("./golden-campaign.json",import.meta.url),"utf8"));
test("PREP07 scripted two-distinct-actor journey includes noncombat, combat, replay and fictional wagers",()=>{
 const a=twoHumanFixtureRun(fixture),b=twoHumanFixtureRun(fixture);
 assert.equal(a.grade,"SYNTHETIC_ONLY_NOT_INSTALLED");
 assert.deepEqual(a.actors,["Raven1","Raven2"]);
 assert.equal(a.actionReceipts,1);assert.equal(a.health,6);
 assert.equal(a.stepEvents,5);assert.equal(a.state,"completed");
 assert.equal(a.resumeCount,1);assert.ok(a.checkpointDigest);
 assert.equal(a.finalDigest,b.finalDigest);
 assert.ok(a.denials.includes("NOT_MEMBER"));
 assert.ok(a.denials.includes("GM_ONLY"));
 assert.equal(a.gmEventCount,a.playerEventCount);
 assert.equal(a.campaignBalance,105);
 assert.equal(a.freeBalance,100);
});
test("PREP07 rejects same principal impersonating two-human test evidence",()=>{
 assert.throws(()=>twoHumanFixtureRun(fixture,{gm:"Raven1",player:"Raven1"}),/NOT_TWO_DISTINCT/);
 assert.throws(()=>twoHumanFixtureRun({...fixture,kind:"OFFICIAL_FIRST_PARTY"}),/NOT_TWO_DISTINCT/);
});
