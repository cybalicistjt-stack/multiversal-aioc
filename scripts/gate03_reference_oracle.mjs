// Source-only GATE-03 provider contract reference. No network, credentials, payment or production authority.
import { readFileSync } from 'node:fs';
const cases=JSON.parse(readFileSync(new URL('../governance/application-planning/governed-access-transactions-entitlements/GATE_03_PROVIDER_CONTRACT_FIXTURES.json',import.meta.url),'utf8')).cases;
const evaluate=function contractCheck(v){
 const kind=v.kind??"checkout",auth=v.auth!==false,subjectMatch=v.subjectMatch!==false;
 if(kind==="checkout"){
  if(!auth)return "DENY_NO_AUTH_SESSION";
  if(v.emailVerified===false)return "DENY_UNVERIFIED_EMAIL";
  if(!subjectMatch)return "DENY_SUBJECT_MISMATCH";
  if(v.offerActive===false)return "DENY_UNAPPROVED_OFFER";
  if(v.regionEligible===false)return "DENY_REGION";
  if(v.storefrontEligible===false)return "DENY_STOREFRONT";
  if(v.intentNonceValid===false)return "DENY_INTENT_NONCE";
  if(v.termsVersionValid===false)return "DENY_TERMS";
  if(v.clientAmountOverride===true||v.clientPriceOverride===true)return "DENY_CLIENT_PRICE_OVERRIDE";
  if(v.idempotencySubjectMismatch===true)return "DENY_CROSS_SUBJECT_IDEMPOTENCY";
  if(v.reusedActiveIntent===true)return "RETURN_EXISTING_INTENT";
  return "ALLOW_CREATE_CHECKOUT_INTENT";
 }
 if(kind==="portal"){
  if(!auth)return "DENY_NO_AUTH_SESSION";
  if(!subjectMatch)return "DENY_SUBJECT_MISMATCH";
  if(v.customerMapped!==true||v.customerOwnerMatch!==true)return "DENY_CUSTOMER_NOT_OWNED";
  if(v.storefront==="play")return "DENY_WRONG_MANAGEMENT_RAIL";
  return "ALLOW_PORTAL_SESSION";
 }
 if(kind==="provider_event"){
  if(v.signatureVerified!==true)return "DENY_UNVERIFIED_PROVIDER_RECEIPT";
  if(v.providerEnvMatches===false)return "DENY_ENVIRONMENT_MISMATCH";
  if(v.eventIdKnown===true)return "IDEMPOTENT_NOOP";
  if(v.checkoutIntentFound!==true)return "HOLD_UNLINKED_PURCHASE";
  if(v.customerOwnerMatch!==true||!subjectMatch)return "DENY_ACCOUNT_MISMATCH";
  if(v.offerMappingValid!==true)return "HOLD_PRODUCT_MAPPING_MISMATCH";
  if(v.currencyValid!==true)return "HOLD_CURRENCY_MISMATCH";
  if(v.storefrontEligible===false)return "HOLD_STOREFRONT_MISMATCH";
  if(v.currentProviderFetched!==true)return "HOLD_PROVIDER_UNAVAILABLE";
  if(v.providerPaidThroughVerified!==true)return "PENDING_PROVIDER_PAYMENT";
  if(v.sourceVersionStale===true)return "RECONCILE_LATEST_NO_GRANT";
  return "RECONCILE_VERIFIED_PAID_PERIOD";
 }
 if(kind==="client_redirect"){
  return "NO_ENTITLEMENT_FROM_REDIRECT";
 }
 return "UNSUPPORTED";
};
let failures=0;
for(const test of cases){const actual=evaluate(test.input);if(actual!==test.expected){console.error(test.id,actual,'!=',test.expected);failures++;}}
if(failures)process.exitCode=1;
else console.log(`GATE-03 source-only contract cases PASS ${cases.length}/${cases.length}; no provider/server proof.`);
