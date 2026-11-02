// GATE-PREP-04: route/state-only mock. No checkout, provider SDK or approved price.
export function subscriptionScreen(data) {
 if(!data||data.accountVerified!==true)return {screen:"sign-in",canPurchase:false};
 if(!data.offerApproved)return {screen:"offer-unavailable",canPurchase:false};
 if(data.currencyKnown!==true||data.disclosuresApproved!==true)return {screen:"disclosure-pending",canPurchase:false};
 if(data.subscriptionSource==="allowance")return {screen:"campaign-access-only",canPurchase:false,manage:"campaign-gm"};
 const management={
   "google-play":"google-play-subscriptions",
   "direct":"merchant-account-portal",
   "apple-iap":"apple-subscriptions",
   "us-play-alternative":"developer-billing-management"
 }[data.chargingRail]||"contact-support";
 const hasPaidTime=Number.isSafeInteger(data.paidThrough)&&Number.isSafeInteger(data.now)&&data.now<data.paidThrough;
 if(data.knownAccountSuspension)return {screen:"locked",canPurchase:false,manage:management};
 if(hasPaidTime)return {screen:data.autoRenew===false?"paid-through-cancel-scheduled":"active",canPurchase:false,manage:management,paidThrough:data.paidThrough};
 return {screen:"expired-or-unverified",canPurchase:true,manage:management};
}
export function checkoutDisclosureReady(data) {
 return data.offerApproved===true && data.customerConsent===true &&
    data.disclosuresApproved===true && data.merchantKnown===true &&
    data.billingRailValid===true && Number.isSafeInteger(data.priceMinor) &&
    data.priceMinor>=0 && typeof data.currency==="string" && data.currency.length===3;
}
