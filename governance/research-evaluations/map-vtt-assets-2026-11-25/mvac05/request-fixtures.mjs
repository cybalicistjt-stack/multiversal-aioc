export function sampleRequest(action,resources,overrides={}){
 const request={action,subjectId:'synthetic:owner',campaignId:action==='session-delivery'?'synthetic:campaign':null,audience:['private-use','modify'].includes(action)?'self':action==='session-delivery'?'campaign':'public',commercial:false,includeAttribution:true,asOf:'2026-11-25',...overrides};
 request.expectedLicenseRevisions=overrides.expectedLicenseRevisions??Object.fromEntries(resources.map(r=>[r.resourceId,r.license.revision]));
 request.policyReceipts=overrides.policyReceipts??Object.fromEntries(resources.map(r=>[r.resourceId,{state:'allowed',subjectId:request.subjectId,action,resourceRevision:r.resourceRevision,campaignId:request.campaignId,evidenceId:'synthetic:policy:'+r.resourceId}]));
 return request;
}
