/**
 * SA-BILL-08 research adapter over SYNTHETIC owner facts, not a production
 * service, REST gateway, A3 session verifier, WSS implementation, or asset CDN.
 * Does not authorize a new product feature. The read/command adapters below
 * use reference-only current role, entitlement and source rights inputs.
 */
import {decideAllowanceUse} from "./sa_bill04_reference.mjs";

const UNSAFE_ACTIONS = new Set([
  "export-outside-campaign","transfer-restricted-character",
  "copy-source","download-protected-asset","publish",
]);
const PROTECTED_READS = new Set(["rest.read","search","search.count","ai.retrieve","wss.event","campaign-use"]);
const MAX_DEPENDENCIES=128;

export class SyntheticOwnerService {
  constructor({accounts,resources,ownerState}) {
    this.accounts=structuredClone(accounts);
    this.resources=structuredClone(resources);
    this.ownerState=structuredClone(ownerState);
  }
  revokeGm(){this.ownerState.access.gmRoleActive=false;this.ownerState.access.sourceRevisionCurrent=false;}
  revokeMembership(){this.ownerState.access.playerMembershipActive=false;}
  revokeSubscription(){this.ownerState.verifiedGmSubscription.status="revoked_refunded";}
  rotateEpoch(){this.ownerState.access.currentGrantEpoch++;}
  authenticate(token){
    // Fixture-only opaque bearer mapping. Production A3 authentication and
    // token-to-canonical-subject binding MUST be independently verified.
    return this.accounts[token] || null;
  }
  inspectDependencyClosure(id){
    const visited=new Set(),visiting=new Set();
    const walk=(current,depth)=>{
      if(depth>MAX_DEPENDENCIES||visiting.has(current))return false;
      if(visited.has(current))return true;
      const record=this.resources[current];
      if(!record)return false;
      visiting.add(current);
      for(const child of record.dependencies||[]){
        const nested=this.resources[child];
        if(!nested||nested.campaignId!==record.campaignId||!walk(child,depth+1))return false;
      }
      visiting.delete(current);visited.add(current);return true;
    };
    return walk(id,0)?[...visited].map(id=>this.resources[id]):null;
  }
  authorize({token,campaignId,resourceId,action,now,epoch,clientFlags}){
    const identity=this.authenticate(token);
    const resource=this.resources[resourceId];
    if(!identity||!resource||identity.subjectId!==this.ownerState.slot.playerSubjectId)
      return {allowed:false,reason:"HIDDEN_OR_FORBIDDEN"};
    if(campaignId!==resource.campaignId || identity.campaignId!==campaignId)
      return {allowed:false,reason:"HIDDEN_OR_FORBIDDEN"};
    // Independent Player-authored objects do not become shared just because
    // their Campaign has a separate GM-sponsored entitlement.
    if(resource.ownerSubjectId!==identity.subjectId && resource.sourceReleaseId===null)
      return {allowed:false,reason:"HIDDEN_OR_FORBIDDEN"};
    if(!PROTECTED_READS.has(action) || UNSAFE_ACTIONS.has(action))
      return {allowed:false,reason:"HIDDEN_OR_FORBIDDEN"};
    if(epoch!==this.ownerState.slot.grantEpoch)
      return {allowed:false,reason:"HIDDEN_OR_FORBIDDEN"};
    const dependencies=this.inspectDependencyClosure(resourceId);
    if(!dependencies||dependencies.some(r=>r.ownerRestricted===true && r.sourceReleaseId!==null &&
       !(this.ownerState.registry[r.sourceReleaseId]?.rightsApproved)))
      return {allowed:false,reason:"HIDDEN_OR_FORBIDDEN"};
    const owner=this.ownerState;
    for(const item of dependencies){
      if(item.sourceReleaseId===null)continue;
      const decision=decideAllowanceUse({
        request:{subjectId:identity.subjectId,campaignId,
          resourceId:item.sourceReleaseId,action:"campaign-read",now},
        owner,
      });
      if(!decision.allowed)return {allowed:false,reason:"HIDDEN_OR_FORBIDDEN"};
    }
    // No clientFlags are ever used as owner-sourced evidence.
    return {allowed:true,reason:"AUTHORIZED_PROJECTION"};
  }
}

export class SyntheticEndpointSurface {
  constructor(owner){this.owner=owner;}
  _permitted(req,action,item){
    return this.owner.authorize({...req,action,resourceId:item.id}).allowed;
  }
  directRead(req){
    const r=this.owner.resources[req.resourceId];
    if(!r||!this._permitted(req,"rest.read",r))
      return {status:404,body:{error:"not-found-or-forbidden"}};
    return {status:200,body:{id:r.id,safeLabel:r.safeLabel,payload:r.protectedPayload}};
  }
  search(req){
    const found=Object.values(this.owner.resources)
      .filter(r=>r.safeLabel.toLowerCase().includes(req.query.toLowerCase()))
      .filter(r=>this._permitted(req,"search",r))
      .map(r=>({id:r.id,safeLabel:r.safeLabel}));
    return {results:found}; // no hidden count/hidden IDs
  }
  searchCount(req){
    return {count:this.search(req).results.length};
  }
  aiRetrieve(req){
    // An AI context request must authorize the explicitly requested root and
    // all of its dependencies, not broaden retrieval to unrelated objects.
    const r=this.owner.resources[req.resourceId];
    if(!r||!this._permitted(req,"ai.retrieve",r))return {context:[]};
    return {context:[{citation:r.id,text:r.protectedPayload}]};
  }
  wssPoll(req){
    const result=this.owner.resources[req.resourceId];
    return this._permitted(req,"wss.event",result||{id:req.resourceId})
      ?{events:[{resourceId:result.id,payload:result.protectedPayload}]}:{events:[]};
  }
  export(req){
    return {status:403,body:{error:"restricted-campaign-transfer"}};
  }
  recoverOwnRawNote(req){
    const identity=this.owner.authenticate(req.token),r=this.owner.resources[req.resourceId];
    return identity && r && identity.subjectId===r.ownerSubjectId
      ?{status:200,body:{rawNote:r.selfAuthoredRawNote||""}}
      :{status:404,body:{error:"not-found-or-forbidden"}};
  }
  command(req,lowerLevelCommandHandler){
    // Command replay MUST be freshly authorized before a lower-level
    // idempotent command receipt is projected to any client.
    const r=this.owner.resources[req.resourceId];
    if(!r||!this._permitted(req,"campaign-use",r))
      return {status:404,body:{error:"not-found-or-forbidden"}};
    // Source-aligned A9 response strips even authorized command body/secret.
    const decision=lowerLevelCommandHandler();
    if(!decision.accepted)return {status:409,body:{error:decision.reason}};
    return {status:200,body:{commandId:decision.receipt.commandId,
      resultingRevision:decision.receipt.resultingRevision,replayed:decision.replayed}};
  }
}
