// GATE-PREP-02: independent fake-provider engine, NEVER production authority.
// Provider snapshots are trusted only inside a TEST fixture. No real signature checks.
export class FakeBillingLedger {
  constructor() {
    this.customerBindings = new Map();
    this.inbox = new Map();
    this.appliedEvents = new Set();
    this.projections = new Map();
    this.outbox = [];
    this.quarantine = [];
  }
  bind({provider, environment, customer, subject}) {
    if (![provider, environment, customer, subject].every(x => typeof x === "string" && x.length)) throw Error("INVALID_BINDING");
    const k = JSON.stringify([provider, environment, customer]);
    const existing = this.customerBindings.get(k);
    if (existing && existing !== subject) throw Error("CUSTOMER_ALREADY_BOUND_TO_OTHER_SUBJECT");
    this.customerBindings.set(k, subject);
  }
  ingest(event, fakeFetchCurrent) {
    if (event.verified !== true) return {kind:"REJECT_UNVERIFIED"};
    if (!["provider","environment","eventId","customer"].every(x=>typeof event[x]==="string"&&event[x].length)) return {kind:"REJECT_BAD_EVENT"};
    const eventKey=JSON.stringify([event.provider,event.environment,event.eventId]);
    const digest=JSON.stringify(event);
    const seen=this.inbox.get(eventKey);
    if (seen !== undefined) {
      if (seen !== digest) {this.quarantine.push({eventKey,reason:"CONFLICTING_DUPLICATE"});return {kind:"QUARANTINE_CONFLICT"};}
      if (this.appliedEvents.has(eventKey)) return {kind:"ACK_DUPLICATE"};
      // Persisted inbox but provider lookup previously failed: retry safely.
    }
    const owner=this.customerBindings.get(JSON.stringify([event.provider,event.environment,event.customer]));
    if (!owner) return {kind:"QUARANTINE_UNKNOWN_CUSTOMER"};
    this.inbox.set(eventKey,digest);
    let snapshot;
    try {snapshot=fakeFetchCurrent(event);} catch {return {kind:"RETRY_LOOKUP"};}
    if (!snapshot || snapshot.provider!==event.provider || snapshot.environment!==event.environment ||
        snapshot.customer!==event.customer || snapshot.subject!==owner || !Number.isSafeInteger(snapshot.revision) ||
        snapshot.revision<1) {this.quarantine.push({eventKey,reason:"BAD_CURRENT_SNAPSHOT"});return {kind:"QUARANTINE_SNAPSHOT"};}
    const pkey=JSON.stringify([event.provider,event.environment,event.customer]);
    const prev=this.projections.get(pkey);
    if(prev && snapshot.revision<=prev.revision) {this.appliedEvents.add(eventKey);return {kind:"STALE_CURRENT_SNAPSHOT"};}
    const paidPeriod= snapshot.invoicePaid===true && typeof snapshot.invoiceId==="string" &&
       Number.isSafeInteger(snapshot.paidThrough) && snapshot.paidThrough>0;
    const paidThrough=paidPeriod ? Math.max(prev?.paidThrough??0,snapshot.paidThrough) : (prev?.paidThrough??0);
    const projection={subject:owner,revision:snapshot.revision,paidThrough,
       autoRenew:snapshot.autoRenew===true,billingStatus:snapshot.billingStatus,
       securityHold:snapshot.securityHold===true,
       refundPolicyPending:snapshot.refundOrDispute===true};
    this.projections.set(pkey,projection);
    this.appliedEvents.add(eventKey);
    this.outbox.push({eventId:"fake-billing:"+pkey+":"+projection.revision, subject:owner, revision:projection.revision});
    return {kind:"APPLIED_CURRENT",projection};
  }
  evaluate({provider,environment,customer,subject,now,scopeAllowed=true}) {
    const pkey=JSON.stringify([provider,environment,customer]);
    const p=this.projections.get(pkey);
    if(!p||p.subject!==subject||scopeAllowed!==true||!Number.isSafeInteger(now))return false;
    return p.securityHold!==true && p.refundPolicyPending!==true && p.paidThrough>now;
  }
}
