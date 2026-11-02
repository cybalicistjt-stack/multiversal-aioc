/**
 * SA-BILL-03 — EXACT-APPLICATION-SOURCE CHARACTERIZATION, not product acceptance.
 * Snapshot: Multiversal-app main db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f
 * Git blob: 11e9a377a2231dc4c8305df36a299aca37b36de9
 *
 * These tests deliberately assert the CURRENT insecure behavior for identified
 * defects. A passing characterization test is evidence of a gap, never proof
 * that subscription billing or allowance authorization is safe or deployed.
 *
 * Run with Node 22+: node --experimental-strip-types --test tests/control_plane/test_sa_bill03_app_evaluator.mjs
 */
import test from "node:test";
import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {readFileSync} from "node:fs";
import {fileURLToPath} from "node:url";
import {evaluateEntitlements} from "../fixtures/sa-bill-03/entitlement-evaluator.ts";

const fixturePath=fileURLToPath(new URL("../fixtures/sa-bill-03/entitlement-evaluator.ts", import.meta.url));
const expectedBlob="11e9a377a2231dc4c8305df36a299aca37b36de9";
const base={
  subjectId:"player-a", evaluatedAt:"2026-10-31T23:00:00Z",
  subscriptions:[], sponsoredMonths:[], campaignGrants:[],
};
const sub=(patch={})=>({
  subscriptionId:"verified-sub",subjectId:"player-a",status:"active",
  startsAt:"2026-10-01T00:00:00Z",endsAt:"2026-12-01T00:00:00Z",...patch,
});
const sponsored=(patch={})=>({
  sponsoredMonthId:"sponsor-1",campaignId:"campaign-X",subjectId:"player-a",
  status:"active",grantedAt:"2026-10-01T00:00:00Z",
  expiresAt:"2026-12-01T00:00:00Z",...patch,
});
const grant=(patch={})=>({
  grantId:"allowance-1",campaignId:"campaign-X",subjectId:"player-a",
  startsAt:"2026-10-01T00:00:00Z",endsAt:"2026-12-01T00:00:00Z",...patch,
});
const call=(patch={})=>evaluateEntitlements({...base,...patch});
const asInstant=value=>Date.parse(value);

test("SA03-00 exact unmodified app source is pinned by Git blob digest",()=>{
  const source=readFileSync(fixturePath);
  const digest=createHash("sha1").update("blob "+source.length+"\0").update(source).digest("hex");
  assert.equal(digest,expectedBlob);
});

test("SA03-01 accepted baseline paid term and free baseline",()=>{
  assert.equal(call().tier,"free");
  assert.equal(call({subscriptions:[sub()]}).tier,"subscriber");
});

test("SA03-02 OBSERVED SOURCE DEFECT: offset expiry grants access beyond actual UTC end",()=>{
  const end="2026-11-01T00:00:00+02:00";
  const now="2026-10-31T23:00:00Z";
  assert.ok(asInstant(end)<asInstant(now),"fixture truly expired in UTC");
  // Known bug: lexical UTC/timezone comparison in CURRENT source.
  assert.equal(call({subscriptions:[sub({endsAt:end})]}).tier,"subscriber");
});

test("SA03-03 OBSERVED SOURCE DEFECT: cancellation wrongly strips still-paid access",()=>{
  const result=call({subscriptions:[sub({status:"cancelled"})]});
  assert.ok(asInstant(base.evaluatedAt)<asInstant("2026-12-01T00:00:00Z"));
  // This is CURRENT behavior, not the desired provider-verified semantics.
  assert.equal(result.tier,"free");
});

test("SA03-04 OBSERVED SOURCE GAP: campaign-less sponsored access can lift tier",()=>{
  const result=call({sponsoredMonths:[sponsored()]}); // no campaignId
  assert.equal(result.tier,"subscriber");
  assert.ok(result.capabilities.includes("campaign-premium-content"));
  // May be legitimate global sponsored-month policy, but NOT a campaign-only allowance.
});

test("SA03-05 OBSERVED SOURCE GAP: campaign-only grant has no issuer/registered root/dependency proof",()=>{
  const r=call({campaignId:"campaign-X",campaignGrants:[grant()]});
  assert.ok(r.capabilities.includes("campaign-premium-content"));
  assert.equal(r.tier,"free"); // grant is not a self-paid subscription
  // This pure evaluator assumes trusted input; no live entitlement authority claimed.
});

test("SA03-06 campaign grant is not effective in a different campaign or subject",()=>{
  assert.ok(!call({campaignId:"campaign-Y",campaignGrants:[grant()]})
    .capabilities.includes("campaign-premium-content"));
  assert.ok(!call({campaignId:"campaign-X",campaignGrants:[grant({subjectId:"player-b"})]})
    .capabilities.includes("campaign-premium-content"));
});

test("SA03-07 OBSERVED SOURCE DEFECT: malformed timestamp may extend subscription",()=>{
  const r=call({subscriptions:[sub({endsAt:"nonsense"})]});
  assert.equal(r.tier,"subscriber");
  assert.ok(Number.isNaN(Date.parse("nonsense")));
});

test("SA03-08 OBSERVED SOURCE GAP: duplicate source IDs are repeated, not deduplicated",()=>{
  const r=call({subscriptions:[sub(),sub()]});
  assert.deepEqual(r.activeRecordIds,["verified-sub","verified-sub"]);
});

test("SA03-09 OBSERVED SOURCE DEFECT: nextChangeAt sorts by string, not earliest UTC instant",()=>{
  const left="2026-11-10T00:00:00+10:00"; // Nov 9, 14:00 UTC
  const right="2026-11-09T23:00:00Z";    // Nov 9, 23:00 UTC
  const r=call({evaluatedAt:"2026-11-09T12:00:00Z",subscriptions:[
    sub({subscriptionId:"first",endsAt:left}),
    sub({subscriptionId:"second",endsAt:right}),
  ]});
  assert.ok(asInstant(left)<asInstant(right));
  assert.equal(r.nextChangeAt,right); // current SOURCE chooses wrong earliest
});

test("SA03-10 OBSERVED SOURCE LIMIT: no slot cardinality or recursive dependency enforcement",()=>{
  const r=call({campaignId:"campaign-X",campaignGrants:[
    grant({grantId:"slot-A"}),grant({grantId:"slot-B"}),
  ]});
  assert.deepEqual(r.activeRecordIds,["slot-A","slot-B"]);
  assert.ok(r.capabilities.includes("campaign-premium-content"));
});

test("SA03-11 same-campaign expired or revoked grant correctly withholds premium content",()=>{
  assert.ok(!call({campaignId:"campaign-X",campaignGrants:[grant({revokedAt:"2026-10-30T00:00:00Z"})]})
    .capabilities.includes("campaign-premium-content"));
  assert.ok(!call({campaignId:"campaign-X",campaignGrants:[grant({endsAt:"2026-10-30T00:00:00Z"})]})
    .capabilities.includes("campaign-premium-content"));
});
