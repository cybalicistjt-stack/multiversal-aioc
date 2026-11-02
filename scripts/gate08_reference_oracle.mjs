// GATE-08 fixture runner: no real payments, tax, merchant quotes, legal determination, store accounts, or release.
import {readFileSync} from 'node:fs';
const f=JSON.parse(readFileSync(new URL('../governance/application-planning/governed-access-transactions-entitlements/GATE_08_STOREFRONT_FIXTURES.json',import.meta.url),'utf8'));
const selectRail=function selectRail(s){
 if(s.offerApproved!==true)return "HOLD_UNAPPROVED_OFFER";
 if(s.customerConsentVerified!==true)return "HOLD_CONSENT";
 if(s.storefrontMapped!==true)return "HOLD_STOREFRONT";
 if(s.regionSupported!==true)return "HOLD_REGION";
 if(s.merchantResponsibleKnown!==true)return "HOLD_MERCHANT";
 if(s.taxPolicyReviewed!==true)return "HOLD_TAX";
 if(s.accountBindingValid!==true)return "HOLD_ACCOUNT";
 if(s.verifiedPaidEvidence!==true)return "NO_PAID_ENTITLEMENT_YET";
 if(s.channel==="windows-direct")return "ELIGIBLE_DIRECT_WINDOWS_SCOPE";
 if(s.channel==="web-direct")return "ELIGIBLE_DIRECT_WEB_SCOPE";
 if(s.channel==="android-play"){
  if(s.rail==="play-billing")return s.playTokenVerified===true?"ELIGIBLE_PLAY_SCOPE":"HOLD_PLAY_TOKEN";
  if(s.rail==="alternative-us"){
   if(s.usUser!==true)return "HOLD_ALT_REGION";
   if(s.playProgramEnrolled!==true)return "HOLD_PLAY_ENROLLMENT";
   if(s.playReportingReady!==true)return "HOLD_PLAY_REPORTING";
   if(s.playManagementReady!==true)return "HOLD_PLAY_MANAGEMENT";
   return "ELIGIBLE_US_ALTERNATIVE_REVIEWED";
  }
  return "HOLD_UNSUPPORTED_RAIL";
 }
 if(s.channel==="ios-app-store"){
  if(s.rail==="apple-iap")return s.appleTransactionVerified===true?"ELIGIBLE_APPLE_IAP_SCOPE":"HOLD_APPLE_TRANSACTION";
  if(s.rail==="external-link-us"){
   if(s.usUser!==true)return "HOLD_APPLE_LINK_REGION";
   if(s.appleCurrentPolicyReviewed!==true)return "HOLD_APPLE_CURRENT_REVIEW";
   return "ELIGIBLE_US_APPLE_LINK_REVIEWED";
  }
  return "HOLD_UNSUPPORTED_RAIL";
 }
 return "HOLD_UNSUPPORTED_CHANNEL";
};
const economics=function economics(v){
 const a=["priceMinor","taxCollectedMinor","processorFeeMinor","billingFeeMinor","storeFeeMinor","providerOtherFeeMinor","serviceCostMinor","supportCostMinor","expectedRefundMinor","riskReserveMinor"];
 if(a.some(k=>!Number.isSafeInteger(v[k])||v[k]<0))return {status:"INVALID_INPUT"};
 if(v.taxCollectedMinor>v.priceMinor)return {status:"INVALID_TAX"};
 if(v.platformTaxRemits===true&&v.merchantTaxRemits===true)return {status:"AMBIGUOUS_TAX_LIABILITY"};
 const subtotal=v.priceMinor-v.processorFeeMinor-v.billingFeeMinor-v.storeFeeMinor-v.providerOtherFeeMinor-v.serviceCostMinor-v.supportCostMinor-v.expectedRefundMinor-v.riskReserveMinor;
 const net=subtotal-(v.merchantTaxRemits===true?v.taxCollectedMinor:0);
 return {status:"VALID_SCENARIO_ONLY",netMinor:net};
};
let fails=0;
for(const r of f.rail_cases){const got=selectRail(r.input);if(got!==r.expected){console.error(r.id,got,r.expected);fails++;}}
for(const e of f.cost_cases){const got=economics(e.input);if(JSON.stringify(got)!==JSON.stringify(e.expected)){console.error(e.id,got,e.expected);fails++;}}
if(fails)process.exitCode=1;else console.log(`GATE08 SOURCE-ONLY PASS ${f.rail_cases.length} rail cases + ${f.cost_cases.length} fictional cost cases. NO legal/store/provider proof.`);
