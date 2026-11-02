// GATE-02 synthetic DESIGN oracle only. Never import into production authorization.
import { readFileSync } from 'node:fs';
const cases = JSON.parse(readFileSync(new URL('../governance/application-planning/governed-access-transactions-entitlements/GATE_02_POLICY_FIXTURES.json', import.meta.url), 'utf8')).cases;
const decide = function decide(v){
 const role=v.role??"player",action=v.action,verified=v.verified!==false;
 if(!verified)return "AUTH_REQUIRED";
 if(v.accountSuspended===true)return "ACCOUNT_LOCKED";
 if(v.hiddenGm===true&&role!=="gm"&&role!=="owner")return "HIDDEN_INFORMATION";
 if(v.restricted===true&&["transfer_object","clone_character","export_restricted","import_elsewhere","archive_clone"].includes(action))return "RESTRICTED_TRANSFER_DENIED";
 if(action==="issue_allowance"){
   if(role!=="gm"||v.gmAuthority!==true)return "GM_ROLE_REQUIRED";
   if(v.subscriber!==true)return "SUBSCRIBED_GM_REQUIRED";
   if(v.slotAvailable!==true)return "ALLOWANCE_SLOT_OCCUPIED";
   if(v.issuerMayShare===false)return "CONTENT_LICENSE_DENIED";
   return "ALLOW_GM_ISSUANCE_ELIGIBLE";
 }
 if(action==="inspect_character"){
   if(v.owner!==true)return "NOT_CHARACTER_OWNER";
   return v.restricted===true?"ALLOW_RETAINED_PROJECTION":"ALLOW_OWNED_CHARACTER";
 }
 if(action==="read_authored"){
   return v.owner===true?"ALLOW_OWNED_DATA":"NOT_DATA_OWNER";
 }
 if(action==="export_owned"){
   if(v.owner!==true)return "NOT_DATA_OWNER";
   return v.independent===true&&v.restricted!==true&&v.mixedProtected!==true?"ALLOW_INDEPENDENT_EXPORT":"PROTECTED_EXPORT_DENIED";
 }
 if(action==="browse_catalog"){
   if(v.canonicalLicenseValid===false)return "CONTENT_LICENSE_DENIED";
   if(v.protected!==true)return "ALLOW_FREE_CATALOG";
   return v.subscriber===true||v.sponsored===true?"ALLOW_PERSONAL_CATALOG":"PERSONAL_ENTITLEMENT_REQUIRED";
 }
 if(action==="gm_admin"){
   if(role!=="gm"||v.gmAuthority!==true)return "GM_ROLE_REQUIRED";
   return "ALLOW_GM_ROLE";
 }
 if(["ability_tier","use_content","execute_authored"].includes(action)){
   if(v.canonicalLicenseValid===false)return "CONTENT_LICENSE_DENIED";
   if(v.campaignBound===true&&v.campaignMember!==true)return "CAMPAIGN_MEMBERSHIP_REQUIRED";
   if(v.campaignRolePermits===false)return "CAMPAIGN_ACTION_DENIED";
   if(v.restricted===true&&v.campaignIdMatches!==true)return "RESTRICTED_CAMPAIGN_CONTEXT_REQUIRED";
   const tier=v.abilityTier??0;
   if(action==="ability_tier"&&tier>=1&&tier<=2&&v.protected!==true&&v.freeContentEligible!==false)return "ALLOW_FREE_TIER";
   if(v.protected!==true&&action!=="execute_authored")return "ALLOW_FREE_CONTENT";
   if(v.subscriber===true)return "ALLOW_PERSONAL_SUBSCRIBER";
   if(v.sponsored===true)return "ALLOW_ACCOUNT_SPONSORED";
   if(v.allowanceValid===true&&v.campaignBound===true&&v.campaignMember===true&&v.campaignIdMatches===true&&v.rootInClosure===true)return "ALLOW_CAMPAIGN_ROOT";
   return "ENTITLEMENT_REQUIRED";
 }
 return "ACTION_NOT_DEFINED";
};
let failed=0;
for (const entry of cases) {
  const actual=decide(entry.input);
  if(actual!==entry.expected){
    process.stderr.write(`${entry.id}: expected ${entry.expected}, got ${actual}\n`);
    failed++;
  }
}
if(failed)process.exitCode=1;
else console.log(`GATE-02 synthetic source-policy cases OK: ${cases.length}; NOT product/security proof.`);
