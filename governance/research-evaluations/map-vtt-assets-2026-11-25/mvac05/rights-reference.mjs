// MVAC-05 reference design: evaluates sample evidence. Never grants runtime authority.
export const ACTIONS=['private-use','modify','session-delivery','flattened-map-export','raw-redistribution'];
export const REQUIRED_CAPS={
 'private-use':['private-use'],modify:['private-use','transform'],
 'session-delivery':['campaign-use'],'flattened-map-export':['export','transform'],
 'raw-redistribution':['export','redistribution']
};
export function decideRights(resourceId,request,resources,ari){
 const traces=[],credits=[],seen=new Set();
 const finish=(status,reasons)=>({status,reasons,traces,credits:[...new Set(credits)],runtimeAuthorizationProved:false,ownerMutationPerformed:false,licenseInferred:false});
 if(!ACTIONS.includes(request.action))return finish('blocked',['unsupported-action']);
 if(typeof request.subjectId!=='string'||!request.subjectId||!['self','campaign','public','player'].includes(request.audience)||typeof request.commercial!=='boolean')return finish('blocked',['invalid-request']);
 function visit(id,pin,depth){
  if(depth>32||seen.has(id))return ['blocked','cyclic-or-excessive-lineage'];
  const r=resources.find(x=>x.resourceId===id);if(!r)return ['unresolved','missing-dependency:'+id];
  const receipt=request.policyReceipts?.[id];
  if(!receipt||receipt.state!=='allowed')return ['blocked','audience-policy-not-allowed:'+id];
  if(receipt.subjectId!==request.subjectId||receipt.action!==request.action||receipt.resourceRevision!==r.resourceRevision||receipt.campaignId!==(request.campaignId??null))return ['blocked','policy-scope-mismatch:'+id];
  if(r.visibility==='gm-only'&&request.audience==='player')return ['blocked','private-resource-excluded:'+id];
  if(pin&&(pin.resourceRevision!==r.resourceRevision||pin.licenseRevision!==r.license.revision))return ['unresolved','stale-evidence-pin:'+id];
  if(!r.provenance?.evidenceId||!r.license?.evidenceId||r.license.state!=='recorded')return ['unresolved','license-evidence-unknown:'+id];
  if(r.license.revision!==request.expectedLicenseRevisions?.[id])return ['unresolved','stale-license-revision:'+id];
  const matrix=ari.buildAri11UseCapabilityMatrix({resourceId:id,evidence:r.capabilityEvidence,resourceExists:true,priorImportAccepted:true});
  const caps=[...REQUIRED_CAPS[request.action],...(request.commercial?['commercial-use']:[])];
  for(const cap of caps){const result=ari.evaluateAri11Capability(matrix,cap);traces.push({resourceId:id,kind:'ARI-11',capability:cap,state:result.state,evidenceIds:matrix.capabilities.find(x=>x.capability===cap)?.evidenceIds||[]});if(!result.allowed)return [result.state==='unknown'?'unresolved':'blocked','capability-'+result.state+':'+cap+':'+id];}
  const grants=r.actionEvidence.filter(e=>e.action===request.action);
  if(!grants.length)return ['unresolved','action-evidence-unknown:'+id];
  const matching=grants.filter(e=>e.resourceRevision===r.resourceRevision&&e.licenseRevision===r.license.revision&&e.subjectId===request.subjectId&&e.audiences.includes(request.audience)&&(!e.campaignId||e.campaignId===request.campaignId));
  if(!matching.length)return ['blocked','action-scope-mismatch:'+id];
  const scoped=ari.buildAri11UseCapabilityMatrix({resourceId:id,evidence:matching.map(e=>({evidenceId:e.evidenceId,source:e.source,capability:'private-use',state:e.state}))});
  const state=ari.evaluateAri11Capability(scoped,'private-use').state;
  traces.push({resourceId:id,kind:'action-scope',action:request.action,state,evidenceIds:matching.map(x=>x.evidenceId)});
  if(state!=='allowed')return [state==='unknown'?'unresolved':'blocked','action-'+state+':'+id];
  if(request.commercial&&matching.some(e=>e.state==='allowed'&&e.commercial!=='any'))return ['blocked','commercial-scope-not-granted:'+id];
  if(matching.some(e=>e.validUntil&&(!request.asOf||request.asOf>e.validUntil)))return ['blocked','expired-action-evidence:'+id];
  if(['session-delivery','flattened-map-export','raw-redistribution'].includes(request.action)){
   if(r.attribution.state==='unknown')return ['unresolved','attribution-obligations-unknown:'+id];
   if(r.attribution.state==='required'){
    const missing=r.attribution.requiredFields.filter(f=>!r.attribution.values?.[f]);
    if(missing.length)return ['unresolved','missing-attribution-fields:'+id+':'+missing.join(',')];
    const text=r.attribution.requiredFields.map(f=>f+': '+r.attribution.values[f]).join(' · ');
    credits.push(text);if(!request.includeAttribution)return ['blocked','attribution-output-required:'+id];
   }
  }
  if(['modify','session-delivery','flattened-map-export','raw-redistribution'].includes(request.action)&&r.bytes.state!=='byte-present')return ['unresolved','source-bytes-unavailable:'+id];
  seen.add(id);
  for(const dep of r.parents){const v=visit(dep.resourceId,dep,depth+1);if(v[0]!=='permitted-by-sample-evidence'){seen.delete(id);return v;}}
  seen.delete(id);return ['permitted-by-sample-evidence'];
 }
 const r=visit(resourceId,null,0);return finish(r[0],r.slice(1));
}
