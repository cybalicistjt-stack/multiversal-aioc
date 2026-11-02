// GATE-05 synthetic reference contract only; no PostgreSQL, no payments, no real concurrency.
import { readFileSync } from 'node:fs';
const fixtures=JSON.parse(readFileSync(new URL('../governance/application-planning/governed-access-transactions-entitlements/GATE_05_LEDGER_FIXTURES.json',import.meta.url),'utf8'));
const check=function check(v){
 if(v.type==="event") {
  if(v.authenticated!==true)return "REJECT_EVENT";
  if(v.environmentValid!==true)return "REJECT_ENV";
  if(v.sameEventKey===true)return "ACK_DUPLICATE";
  if(v.customerBound!==true)return "QUARANTINE_CUSTOMER";
  if(v.revisionNewer!==true)return "PRESERVE_PROJECTION_REFRESH";
  if(v.currentProviderVerified!==true)return "RETRY_LOOKUP_NO_GRANT";
  return "ACCEPT_VERIFIED_FACT_ONCE";
 }
 if(v.type==="claim") {
  if(v.subjectVerified!==true)return "DENY_IDENTITY";
  if(v.providerBound!==true)return "DENY_PROVIDER_OWNER";
  if(v.offerAllowed!==true)return "HOLD_OFFER";
  if(v.idempotencyReplayOtherSubject===true)return "DENY_REPLAY_OTHER_SUBJECT";
  if(v.subscriptionClaimAlreadyBound===true)return "RETURN_EXISTING_BINDING";
  return "CREATE_UNIQUE_BINDING";
 }
 if(v.type==="allowance") {
  if(v.actorGm!==true)return "DENY_NOT_GM";
  if(v.gmVerifiedSubscriber!==true)return "DENY_GM_NOT_SUBSCRIBED";
  if(v.beneficiaryMember!==true)return "DENY_NOT_CAMPAIGN_MEMBER";
  if(v.rootClosureValidated!==true)return "DENY_INVALID_CLOSURE";
  if(v.slotExists===true)return "RETURN_OCCUPIED_SLOT";
  return "ISSUE_ONE_SLOT";
 }
 if(v.type==="grant") {
  if(v.accountSuspended===true)return "DENY_KNOWN_SUSPENSION";
  if(v.revocationEpochStale===true)return "DENY_STALE_GRANT";
  if(v.hasFinitePaidThrough!==true)return "DENY_NO_FINITE_PERIOD";
  if(v.revoked===true)return "DENY_REVOKED";
  if(v.subjectMatches!==true)return "DENY_CROSS_SUBJECT";
  if(v.campaignScopeValid!==true)return "DENY_CAMPAIGN";
  if(v.sourceProofValid!==true)return "DENY_SOURCE";
  return "DERIVE_SCOPED_GRANT";
 }
 if(v.type==="money") {
  if(v.verifiedProviderFact!==true)return "HOLD_UNVERIFIED_MONEY";
  if(v.currencyValid!==true)return "HOLD_CURRENCY";
  if(v.duplicateExternalLine===true)return "ACK_ALREADY_POSTED";
  if(v.positiveMinorAmount!==true)return "REJECT_AMOUNT";
  if(v.correspondingLiability!==true)return "REJECT_UNBALANCED";
  return "POST_BALANCED_FACT";
 }
 if(v.type==="outbox") {
  if(v.transactionCommitted!==true)return "NO_OUTBOX_VISIBLE";
  if(v.publishedOnce===true)return "ACK_DELIVERY";
  if(v.consumerIdempotent!==true)return "RETRY_SAME_EVENT_ID";
  return "PUBLISH_OUTBOX_MESSAGE";
 }
 return "UNSUPPORTED";
};
let fail=0;
for(const test of fixtures.cases){
 const actual=check(test.input);
 if(actual!==test.expected){console.error(test.id,"expected",test.expected,"actual",actual);fail++;}
}
// Sequential toy: does NOT test concurrent database transactions or SQL uniqueness.
const slots=new Set();let inserted=0,conflicts=0;
for(let i=0;i<100;i++){const key='campaign-1|player-A';if(slots.has(key))conflicts++;else{slots.add(key);inserted++;}}
if(inserted!==1||conflicts!==99){console.error("100-attempt toy failure");fail++;}
if(fail)process.exitCode=1;
else console.log(`GATE-05 source-only fixtures PASS ${fixtures.cases.length}/${fixtures.cases.length}; 100-attempt sequential toy: 1 slot/99 conflicts. PostgreSQL concurrency NOT_RUN.`);
