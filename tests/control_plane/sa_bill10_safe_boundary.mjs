/**
 * SA-BILL-10 ADDITIVE SECURITY ADAPTER RESEARCH ONLY.
 * The existing P9-06-016/P9-06-018 internal function contracts stay intact.
 * A server MUST create trustedCurrent, persistedCommand and persistedReceipt;
 * no caller-provided boolean/session is authentic evidence. No real A3/PCV
 * integration or cryptographic producer binding exists in this module.
 */
const FAILURE=Object.freeze({status:404,body:{error:"not-found-or-forbidden"}});
const stableObject=x=>{
  if(Array.isArray(x))return x.map(stableObject);
  if(x && typeof x==="object")return Object.fromEntries(Object.keys(x).sort()
    .map(key=>[key,stableObject(x[key])]));
  return x;
};
function sameCommand(a,b) {
  if(!a||!b) return false;
  try {return JSON.stringify(stableObject(a))===JSON.stringify(stableObject(b));}
  catch {return false;}
}
export function protectedCommandBoundary({command,state,owner,internalHandler,safeProjection}){
  // This *function* cannot authenticate owner itself. A trusted backend must
  // derive owner from session and external canonical A3, never request body.
  if(!command||!state||!owner?.trustedCurrent||!owner?.authenticatedSubjectId ||
     owner.authenticatedSubjectId!==command.actorId ||
     owner.activeCampaignId!==state.campaignId ||
     owner.sessionId!==state.sessionId || owner.roleEpochCurrent!==true ||
     owner.activeMembership!==true || owner.entitlementEpochCurrent!==true)
    return FAILURE;
  const exists=state.processedCommandIds?.includes(command.commandId);
  if(exists){
    if(!owner.persistedCommand || !owner.persistedReceipt ||
      !sameCommand(command,owner.persistedCommand) ||
      owner.persistedReceipt.commandId!==command.commandId ||
      owner.persistedReceipt.accepted!==true ||
      owner.persistedReceipt.resultingRevision>state.revision)
      return FAILURE;
  }
  const decision=internalHandler(state,command,{
    membership:owner.membership,
    existingReceipt:exists?owner.persistedReceipt:undefined,
  });
  if(!decision.accepted)return {status:409,body:{error:decision.reason}};
  const safe=safeProjection(decision);
  if(!safe || Object.hasOwn(safe,"rawCommandPayload") ||
     safe.events?.some(e=>Object.hasOwn(e,"payload")||Object.hasOwn(e,"visibility")))
    return FAILURE;
  return {status:200,body:safe};
}
export function protectedEventBoundary({events,context,owner,filterA9}){
  if(!owner?.trustedCurrent || !owner.activeMembership ||
     owner.roleEpochCurrent!==true||owner.entitlementEpochCurrent!==true ||
     !owner.authenticatedSubjectId ||
     owner.authenticatedSubjectId!==context?.viewerSubjectId ||
     owner.activeCampaignId!==context?.campaign?.campaignId ||
     owner.sessionId!==context?.sessionId) return FAILURE;
  const projected=filterA9(events,context);
  if(!projected.ok || "hiddenEventCount" in projected.value ||
     projected.value.visibleEvents?.some(x=>
       x.sessionId!==context.sessionId)) return FAILURE;
  // This A9 filter is necessary, not sufficient for premium dependency rights;
  // no direct raw provider-neutral projection can be exposed as-is.
  return {status:200,body:projected.value};
}
