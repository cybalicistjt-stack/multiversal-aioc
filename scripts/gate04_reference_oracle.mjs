// GATE-04 synthetic reference only; no payment provider, no real database or entitlement enforcement.
import { readFileSync } from 'node:fs';
const cases=JSON.parse(readFileSync(new URL('../governance/application-planning/governed-access-transactions-entitlements/GATE_04_TEMPORAL_FIXTURES.json',import.meta.url),'utf8')).cases;
const period=function period(s) {
 if(s.accountVerified!==true)return "DENY_ACCOUNT";
 if(s.providerVerified!==true)return "HOLD_UNVERIFIED_SOURCE";
 if(s.customerBindingValid!==true)return "HOLD_ACCOUNT_BINDING";
 if(s.currentSnapshotFetched!==true)return "HOLD_CURRENT_PROVIDER";
 if(s.productMappingValid!==true)return "HOLD_PRODUCT_MAPPING";
 if(s.currencyMatches!==true)return "HOLD_CURRENCY";
 if(s.knownRevoked===true)return "DENY_KNOWN_REVOCATION";
 if(s.refundState==="full")return "HOLD_REFUND_POLICY";
 if(s.refundState==="partial")return "HOLD_PARTIAL_REFUND_POLICY";
 if(s.disputeOpen===true)return "HOLD_DISPUTE_POLICY";
 if(s.subjectSuspended===true)return "DENY_ACCOUNT_SUSPENDED";
 if(s.sourceKind!=="personal_subscription")return "HOLD_WRONG_ENTITLEMENT_CAUSE";
 if(!Number.isSafeInteger(s.now)||!Number.isSafeInteger(s.periodFrom)||!Number.isSafeInteger(s.paidThrough)||s.paidThrough<=s.periodFrom)return "HOLD_INVALID_PAID_WINDOW";
 if(s.now<s.periodFrom)return "DENY_NOT_STARTED";
 if(s.now>=s.paidThrough)return "DENY_PAID_THROUGH_EXPIRED";
 if(s.invoicePaid!==true)return "HOLD_NO_PAID_INVOICE";
 if(s.billingStatus==="active")return s.autoRenew===false?"ALLOW_PAID_ENDING":"ALLOW_PAID_ACTIVE";
 if(s.billingStatus==="past_due")return "ALLOW_EXISTING_PAID_PERIOD_ONLY";
 if(s.billingStatus==="canceled"&&s.cancelEffectiveAtPeriodEnd===true)return "ALLOW_PAID_ENDING";
 if(s.billingStatus==="trialing")return "HOLD_TRIAL_POLICY";
 if(s.billingStatus==="paused")return "HOLD_PAUSE_POLICY";
 if(s.billingStatus==="unpaid")return "HOLD_UNPAID_POLICY";
 if(s.billingStatus==="incomplete"||s.billingStatus==="incomplete_expired")return "DENY_INCOMPLETE";
 if(s.billingStatus==="canceled")return "DENY_TERMINATED";
 return "HOLD_UNKNOWN_STATUS";
};
const ingress=function ingress(e){
 if(e.signatureVerified!==true)return "REJECT_UNAUTHENTICATED";
 if(e.environmentMatches!==true)return "REJECT_WRONG_ENVIRONMENT";
 if(e.eventIdValid!==true)return "REJECT_BAD_EVENT_ID";
 if(e.eventIdAlreadySeen===true)return "ACK_DUPLICATE_NO_EFFECT";
 if(e.customerBindingValid!==true)return "QUARANTINE_WRONG_ACCOUNT";
 if(e.providerObjectMapped!==true)return "QUARANTINE_UNKNOWN_OBJECT";
 if(e.oldNotification===true)return "ACK_AND_REFRESH_CURRENT";
 if(e.currentLookupAvailable!==true)return "PERSIST_AND_RETRY_LOOKUP";
 return "PERSIST_AND_FETCH_CURRENT";
};
let failures=0;
for(const c of cases){
 const actual=c.kind==="period"?period(c.input):ingress(c.input);
 if(actual!==c.expected){console.error(c.id,"expected",c.expected,"actual",actual);failures++;}
}
if(failures)process.exitCode=1;
else console.log(`GATE-04 source-only temporal and event cases: PASS ${cases.length}/${cases.length}. NOT deployed provider/database/security proof.`);
