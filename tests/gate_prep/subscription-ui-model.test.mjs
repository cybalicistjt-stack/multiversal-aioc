import test from "node:test";
import assert from "node:assert/strict";
import {subscriptionScreen,checkoutDisclosureReady} from "./subscription-ui-model.mjs";
const baseline={accountVerified:true,offerApproved:true,currencyKnown:true,disclosuresApproved:true,chargingRail:"direct",subscriptionSource:"subscription",now:1000,paidThrough:2000,autoRenew:true};
test("checkout requires verified consent, merchant, price, legal copy and supported rail",()=>{
 const v={offerApproved:true,customerConsent:true,disclosuresApproved:true,merchantKnown:true,billingRailValid:true,priceMinor:499,currency:"USD"};
 assert.equal(checkoutDisclosureReady(v),true);
 for(const key of ["customerConsent","disclosuresApproved","merchantKnown","billingRailValid","offerApproved"])assert.equal(checkoutDisclosureReady({...v,[key]:false}),false);
 assert.equal(checkoutDisclosureReady({...v,priceMinor:null}),false);
});
test("cancellation retains paid-through and correctly routes buyer",()=>{
 const v=subscriptionScreen({...baseline,autoRenew:false,chargingRail:"google-play"});
 assert.equal(v.screen,"paid-through-cancel-scheduled");
 assert.equal(v.manage,"google-play-subscriptions");
 assert.equal(v.paidThrough,2000);
 assert.equal(subscriptionScreen({...baseline,chargingRail:"us-play-alternative"}).manage,"developer-billing-management");
 assert.equal(subscriptionScreen({...baseline,chargingRail:"apple-iap"}).manage,"apple-subscriptions");
});
test("Campaign allowance never masquerades as subscriber tier or checkout",()=>{
 const x=subscriptionScreen({...baseline,subscriptionSource:"allowance"});
 assert.equal(x.screen,"campaign-access-only");
 assert.equal(x.canPurchase,false);
});
test("not verified, no approved price/copy, suspended or expired fail safely",()=>{
 assert.equal(subscriptionScreen({...baseline,accountVerified:false}).screen,"sign-in");
 assert.equal(subscriptionScreen({...baseline,offerApproved:false}).screen,"offer-unavailable");
 assert.equal(subscriptionScreen({...baseline,disclosuresApproved:false}).screen,"disclosure-pending");
 assert.equal(subscriptionScreen({...baseline,knownAccountSuspension:true}).screen,"locked");
 assert.equal(subscriptionScreen({...baseline,now:2000}).screen,"expired-or-unverified");
});
