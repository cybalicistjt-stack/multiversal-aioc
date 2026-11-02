// GATE-07 offline authorization source-only tests; no native app, signed crypto, Keystore, Windows DPAPI, service or payment.
import {readFileSync} from 'node:fs';
const cases=JSON.parse(readFileSync(new URL('../governance/application-planning/governed-access-transactions-entitlements/GATE_07_OFFLINE_FIXTURES.json',import.meta.url),'utf8'));
const check=function check(v){
 if(v.kind==="offline_runtime"){
  if(v.accountVerified!==true)return "DENY_ACCOUNT";
  if(v.localLock===true)return "DENY_LOCAL_LOCK";
  if(v.sessionContinuity!==true)return "DENY_SWITCHED_SESSION";
  if(v.signatureValid!==true)return "DENY_SIGNATURE";
  if(v.issuerAudienceValid!==true)return "DENY_ISSUER_AUDIENCE";
  if(v.credentialMatches!==true)return "DENY_DEVICE_CREDENTIAL";
  if(v.subjectMatches!==true)return "DENY_SUBJECT";
  if(v.resourceAllowed!==true)return "DENY_RESOURCE";
  if(v.campaignRequired===true&&v.campaignMatches!==true)return "DENY_CAMPAIGN";
  if(v.manifestMatches!==true)return "DENY_MANIFEST";
  if(v.securityEpochStale===true)return "DENY_KNOWN_REVOKED";
  if(v.trustedClock===false||v.clockRollback===true)return "DENY_TIME_UNCERTAIN";
  if(v.knownFinitePaidThrough!==true||v.leaseFinite!==true)return "DENY_NOT_FINITE";
  if(v.leaseUnexpired!==true||v.paidThroughUnexpired!==true)return "DENY_EXPIRED";
  if(v.cacheEnvelopeScoped!==true)return "DENY_CACHE_KEY";
  return "ALLOW_CACHED_SCOPE";
 }
 if(v.kind==="retained_character"){
  if(v.accountVerified!==true)return "DENY_ACCOUNT";
  if(v.localLock===true)return "DENY_LOCAL_LOCK";
  if(v.subjectOwnsCharacter!==true)return "DENY_NOT_OWNER";
  if(v.keyScope==="runtime")return "DENY_RUNTIME_FROM_VIEW";
  if(v.keyScope!=="character-view")return "DENY_WRONG_VIEW_KEY";
  if(v.gmPrivate===true)return "DENY_GM_PRIVATE";
  if(v.viewOnly!==true)return "DENY_EXTRA_ACTION";
  if(v.sessionContinuity!==true)return "DENY_SWITCHED_SESSION";
  if(v.leaseViewScopeValid!==true)return "DENY_VIEW_SCOPE";
  return "ALLOW_RETAINED_PROJECTION";
 }
 if(v.kind==="reconnect"){
  if(v.signedIn!==true)return "DENY_REAUTH";
  if(v.sourceAcceptedByServer===false)return "REJECT_SERVER_RESTRICTED";
  if(v.currentRightsKnown!==true)return "HOLD_FOR_REFRESH";
  if(v.serverGrantCurrent!==true)return "REJECT_STALE_GRANT";
  if(v.serverMembershipCurrent!==true)return "REJECT_MEMBERSHIP";
  if(v.sourceDestinationRights!==true)return "REJECT_TRANSFER";
  if(v.idempotencyAlreadyAccepted===true)return "RECONCILE_EXISTING_ACK";
  return "ACCEPT_SERVER_VALIDATED_DRAFT";
 }
 if(v.kind==="outage"){
  if(v.localLock===true)return "DENY_LOCAL_LOCK";
  if(v.knownDenial===true)return "DENY_KNOWN";
  if(v.leaseScopeValid!==true)return "DENY_SCOPE";
  if(v.leaseFiniteUnexpired!==true)return "DENY_EXPIRED";
  if(v.transportTimeout===true)return "KEEP_PREVIOUS_VERIFIED_SCOPE";
  return "NEEDS_CURRENT_SERVER_CHECK";
 }
 if(v.kind==="delivery"){
  if(v.subjectAuthenticated!==true)return "DENY_AUTH";
  if(v.serverEntitlementVerified!==true)return "DENY_ENTITLEMENT";
  if(v.resourceRights!==true)return "DENY_RIGHTS";
  if(v.publicInstallerSecret===true)return "DENY_PUBLIC_SECRET";
  if(v.accountDeviceEnvelope!==true)return "DENY_ENVELOPE";
  if(v.clientSuppliedSignature===true)return "DENY_CLIENT_MINT";
  return "ISSUE_SCOPED_KEY_WRAP";
 }
 return "DENY_UNDEFINED";
};
const timeModel=function(v){
 if(!Number.isSafeInteger(v.now)||!Number.isSafeInteger(v.issued)||!Number.isSafeInteger(v.leaseEnd)||!Number.isSafeInteger(v.paidEnd))return "INVALID_TIME";
 if(v.issued>=v.leaseEnd||v.leaseEnd>v.paidEnd)return "INVALID_LEASE_WINDOW";
 if(v.now<v.issued)return "PREISSUE";
 if(v.now>=v.leaseEnd||v.now>=v.paidEnd)return "EXPIRED";
 return "ALLOW_WINDOW";
};
let fail=0;
for(const c of cases.decision_cases){const actual=check(c.input);if(actual!==c.expected){console.error(c.id,actual,c.expected);fail++;}}
for(const t of cases.time_cases){const actual=timeModel(t.input);if(actual!==t.expected){console.error(t.id,actual,t.expected);fail++;}}
if(fail)process.exitCode=1;
else console.log(`GATE-07 source-only checks PASS: ${cases.decision_cases.length} policy + ${cases.time_cases.length} time. No native/cryptographic proof.`);
