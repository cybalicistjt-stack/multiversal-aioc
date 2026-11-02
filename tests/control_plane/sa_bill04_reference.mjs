/**
 * SA-BILL-04 / RESEARCH-ONLY fail-closed reference. NOT an application patch,
 * payment verifier, revocation authority, or a production authorization port.
 * Values labelled "owner" must be supplied by an independently trusted
 * canonical service. A client supplied owner object is never trustworthy.
 */
import {createHash} from 'node:crypto';

const TZ = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(?:\.(\d{1,3}))?(Z|([+-])(\d{2}):(\d{2}))$/;
export function parseInstant(value) {
  if (typeof value !== 'string') return null;
  const m = TZ.exec(value);
  if (!m) return null;
  const [y,mo,d,h,mi,s] = m.slice(1,7).map(Number);
  const ms=Number((m[7]||'').padEnd(3,'0'));
  const offH=Number(m[10]||0),offM=Number(m[11]||0);
  if(y<1||mo<1||mo>12||d<1||d>31||h>23||mi>59||s>59||offH>14||offM>59||(offH===14&&offM!==0)) return null;
  const local=Date.UTC(y,mo-1,d,h,mi,s,ms);
  const check = new Date(local);
  // Date.UTC interprets 0..99 as 1900..1999. Reject those years instead
  // of treating a different calendar year as an authorized time.
  if(y<100||!Number.isFinite(local)||check.getUTCFullYear()!==y||check.getUTCMonth()+1!==mo||check.getUTCDate()!==d) return null;
  const signedMinutes=(m[9]==='-'?-1:1)*(offH*60+offM);
  const epoch=local-signedMinutes*60000;
  return Number.isSafeInteger(epoch)?epoch:null;
}
export function windowActive(start,end,now){
  const a=parseInstant(start),b=parseInstant(end),t=parseInstant(now);
  return a!==null&&b!==null&&t!==null&&b>a&&t>=a&&t<b;
}
export function readProviderEntitlement(owner, now) {
  if(!owner || owner.origin!=='verified-billing-ledger' || !owner.payerSubjectId ||
    owner.payerSubjectId!==owner.boundSubjectId || !owner.productId ||
    !owner.sourceRevision || !owner.provider || !owner.purchaseBindingId) {
    return {kind:'deny',reason:'SOURCE_NOT_VERIFIED'};
  }
  // Provider-confirmed grace may extend AFTER the original paid term.
  // The provider-grace clock must be separately verified and bounded.
  const insidePaidTerm=windowActive(owner.entitledFrom,owner.entitledUntil,now);
  if(owner.status!=='grace_entitled' && !insidePaidTerm)
    return {kind:'deny',reason:'OUTSIDE_VERIFIED_TERM'};
  switch(owner.status){
    case 'verified_active':
    case 'cancel_scheduled':
      return {kind:'allow',reason:'VERIFIED_PAID_TERM',issueAllowance:true};
    case 'grace_entitled':{
      const nowTs=parseInstant(now),until=parseInstant(owner.providerGraceUntil);
      const start=parseInstant(owner.entitledFrom),paidEnd=parseInstant(owner.entitledUntil);
      if(owner.providerConfirmsGrace!==true||nowTs===null||until===null||start===null||paidEnd===null||
        paidEnd<=start||until<=paidEnd||nowTs<paidEnd||nowTs>=until)
        return {kind:'deny',reason:'UNVERIFIED_GRACE'};
      return {kind:'allow',reason:'VERIFIED_GRACE',issueAllowance:false};
    }
    case 'trial_verified': return {kind:'pending_policy',reason:'TRIAL_GRANT_POLICY_UNSELECTED',issueAllowance:false};
    default: return {kind:'deny',reason:'STATE_NOT_ENTITLED'};
  }
}

export function trustedDependencyClosure(registry,root,limit=256){
  if(!registry || typeof registry!=='object'||typeof root!=='string'||!root) throw Error('UNREGISTERED_ROOT');
  const visited=new Set(),visiting=new Set();
  function walk(id){
    if(visiting.has(id)) throw Error('DEPENDENCY_CYCLE');
    if(visited.has(id))return;
    const rec=Object.hasOwn(registry,id)?registry[id]:null;
    if(!rec||!rec.active||!rec.version||!rec.rightsApproved||!Array.isArray(rec.dependencies)) throw Error('UNREGISTERED_OR_UNRIGHTED_DEPENDENCY');
    if(visited.size+visiting.size>=limit)throw Error('DEPENDENCY_LIMIT');
    visiting.add(id);
    for(const child of rec.dependencies){if(typeof child!=='string'||!child)throw Error('INVALID_DEPENDENCY');walk(child);}
    visiting.delete(id);visited.add(id);
  }
  walk(root);
  const entries=[...visited].sort().map(id=>({id,version:registry[id].version}));
  const digest='sha256:'+createHash('sha256').update(JSON.stringify(entries)).digest('hex');
  return Object.freeze({entries,digest,ids:new Set(visited)});
}

const FORBIDDEN=new Set(['export-outside-campaign','transfer-restricted-character','copy-source','publish','entitlement.issue','use-in-other-campaign']);
export function decideAllowanceUse({request,owner}){
  // Every policy input must be owner-side; pure model cannot authenticate it.
  if(!request||!owner) return {allowed:false,reason:'MISSING_AUTHORITY'};
  if(request.offline) return {allowed:false,reason:'OFFLINE_REQUIRES_SEPARATE_CRYPTO_LEASE'};
  if(FORBIDDEN.has(request.action)) return {allowed:false,reason:'PROHIBITED_TRANSFER'};
  if(!['campaign-read','campaign-use'].includes(request.action)) return {allowed:false,reason:'UNKNOWN_ACTION'};
  const slot=owner.slot,access=owner.access;
  if(!slot||!access||!owner.registry) return {allowed:false,reason:'MISSING_OWNER_EVIDENCE'};
  if(!request.subjectId||request.subjectId!==slot.playerSubjectId||request.campaignId!==slot.campaignId||
      request.campaignId!==access.campaignId||request.subjectId!==access.playerSubjectId)
    return {allowed:false,reason:'SUBJECT_OR_CAMPAIGN_MISMATCH'};
  if(slot.state!=='active'||!slot.issuerGmSubjectId||slot.issuerGmSubjectId!==access.currentGmSubjectId||
    access.gmRoleActive!==true||access.playerMembershipActive!==true||access.sourceRevisionCurrent!==true||
    slot.grantEpoch!==access.currentGrantEpoch||slot.entitlementRulesetVersion!==access.entitlementRulesetVersion)
    return {allowed:false,reason:'REVOKED_STALE_OR_MISSING_ROLE'};
  const paid=readProviderEntitlement(owner.verifiedGmSubscription,request.now);
  if(paid.kind!=='allow')return {allowed:false,reason:'ISSUER_NOT_ENTITLED'};
  let closure;
  try{closure=trustedDependencyClosure(owner.registry,slot.rootReleaseId);}catch{return{allowed:false,reason:'BAD_SOURCE_DEPENDENCY_GRAPH'};}
  if(closure.digest!==slot.closureDigest || !closure.ids.has(request.resourceId))
    return {allowed:false,reason:'RESOURCE_OUTSIDE_TRUSTED_ROOT'};
  const resource=owner.registry[request.resourceId];
  if(resource.canUseInCampaign!==true) return {allowed:false,reason:'RESOURCE_RIGHTS_DENIED'};
  return {allowed:true,reason:'CURRENT_CAMPAIGN_SCOPED_GRANT'};
}

export function decideAllowanceIssuance({request,owner}){
  if(!request||!owner||!owner.access||!owner.registry)return {allowed:false,reason:'MISSING_OWNER_EVIDENCE'};
  if(request.offline)return {allowed:false,reason:'OFFLINE_ISSUANCE_FORBIDDEN'};
  if(request.issuerSubjectId!==owner.access.currentGmSubjectId ||
     owner.access.gmRoleActive!==true || owner.access.playerMembershipActive!==true ||
     request.playerSubjectId!==owner.access.playerSubjectId ||
     request.campaignId!==owner.access.campaignId) return {allowed:false,reason:'GM_OR_PLAYER_NOT_AUTHORIZED'};
  const paid=readProviderEntitlement(owner.verifiedGmSubscription,request.now);
  if(paid.kind!=='allow'||paid.issueAllowance!==true)return{allowed:false,reason:'GM_NOT_ELIGIBLE_TO_ISSUE'};
  if(!['custom-setting','registered-species','registered-item-set','registered-ability-tree'].includes(request.rootKind))
    return {allowed:false,reason:'TARGET_NOT_ALLOWED'};
  const root=owner.registry[request.rootReleaseId];
  if(!root||root.kind!==request.rootKind||!root.ownerAllowedAsGrantRoot)return{allowed:false,reason:'ROOT_NOT_REGISTERED'};
  try{trustedDependencyClosure(owner.registry,request.rootReleaseId);}catch{return{allowed:false,reason:'BAD_SOURCE_DEPENDENCY_GRAPH'};}
  // This is only PRE-TRANSACTION eligibility. No count, unique key, lock,
  // receipt, or issued grant is minted by this pure decision function.
  return {allowed:true,reason:'ELIGIBLE_FOR_ATOMIC_OWNER_TRANSACTION_ONLY'};
}
