import test from "node:test";
import assert from "node:assert/strict";
import {FakeBillingLedger} from "./fake-billing-ledger.mjs";
const evt=(id="evt1")=>({provider:"fake",environment:"sandbox",eventId:id,customer:"cust-A",verified:true});
const paid=(revision=1,extra={})=>({provider:"fake",environment:"sandbox",customer:"cust-A",subject:"Raven1",revision,invoicePaid:true,invoiceId:"inv"+revision,paidThrough:2000,autoRenew:true,billingStatus:"active",...extra});
test("verified current paid invoice grants only the bound subject",()=>{
 const l=new FakeBillingLedger();l.bind({provider:"fake",environment:"sandbox",customer:"cust-A",subject:"Raven1"});
 assert.equal(l.ingest(evt(),()=>paid()).kind,"APPLIED_CURRENT");
 assert.equal(l.evaluate({provider:"fake",environment:"sandbox",customer:"cust-A",subject:"Raven1",now:1500}),true);
 assert.equal(l.evaluate({provider:"fake",environment:"sandbox",customer:"cust-A",subject:"Raven2",now:1500}),false);
 assert.equal(l.evaluate({provider:"fake",environment:"sandbox",customer:"cust-A",subject:"Raven1",now:2000}),false);
 assert.equal(l.outbox.length,1);
});
test("cancellation and failed next renewal cannot remove verified paid-through",()=>{
 const l=new FakeBillingLedger();l.bind({provider:"fake",environment:"sandbox",customer:"cust-A",subject:"Raven1"});
 l.ingest(evt(),()=>paid());
 const result=l.ingest(evt("e2"),()=>paid(2,{invoicePaid:false,autoRenew:false,billingStatus:"past_due",paidThrough:0}));
 assert.equal(result.projection.paidThrough,2000);
 assert.equal(result.projection.autoRenew,false);
 assert.equal(l.evaluate({provider:"fake",environment:"sandbox",customer:"cust-A",subject:"Raven1",now:1999}),true);
});
test("fake provider notification cannot bypass verification, duplicate, ordering or ownership",()=>{
 const l=new FakeBillingLedger();l.bind({provider:"fake",environment:"sandbox",customer:"cust-A",subject:"Raven1"});
 assert.equal(l.ingest({...evt(),verified:false},()=>paid()).kind,"REJECT_UNVERIFIED");
 assert.equal(l.ingest(evt(),()=>paid()).kind,"APPLIED_CURRENT");
 assert.equal(l.ingest(evt(),()=>paid(99)).kind,"ACK_DUPLICATE");
 assert.equal(l.ingest({...evt(),extra:"mutated"},()=>paid(99)).kind,"QUARANTINE_CONFLICT");
 assert.equal(l.ingest(evt("old"),()=>paid()).kind,"STALE_CURRENT_SNAPSHOT");
 assert.equal(l.ingest(evt("wrong"),()=>paid(3,{subject:"Raven2"})).kind,"QUARANTINE_SNAPSHOT");
 assert.throws(()=>l.bind({provider:"fake",environment:"sandbox",customer:"cust-A",subject:"Raven2"}),/OTHER_SUBJECT/);
 assert.equal(l.projections.size,1);
});
test("lookup outage never grants rights; refund/dispute is held until owner policy",()=>{
 const l=new FakeBillingLedger();l.bind({provider:"fake",environment:"sandbox",customer:"cust-A",subject:"Raven1"});
 assert.equal(l.ingest(evt(),()=>{throw Error("offline")}).kind,"RETRY_LOOKUP");
 assert.equal(l.projections.size,0);
 assert.equal(l.ingest(evt(),()=>paid()).kind,"APPLIED_CURRENT");
 assert.equal(l.ingest(evt(),()=>paid()).kind,"ACK_DUPLICATE");
 const q=l.ingest(evt("refund"),()=>paid(2,{refundOrDispute:true}));
 assert.equal(q.projection.refundPolicyPending,true);
 assert.equal(l.evaluate({provider:"fake",environment:"sandbox",customer:"cust-A",subject:"Raven1",now:1500}),false);
});
