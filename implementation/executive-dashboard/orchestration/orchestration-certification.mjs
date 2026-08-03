const severities={info:0,warning:1,blocking:2};
const normalize=x=>Array.isArray(x)?x:[];
export function certifyOrchestration({certification,queue=[],approvals=[],interventions=[],dispatchEvents=[]}={}){
 const findings=[];
 if(!certification||certification.executionAllowed!==true) findings.push({code:'continuity.blocked',severity:'blocking',message:'Continuity certification does not permit execution.'});
 const pending=queue.filter(x=>['queued','leased','awaiting-approval'].includes(x.status));
 for(const job of pending){
  if(!job.id||!job.workItemId) findings.push({code:'job.identity',severity:'blocking',jobId:job.id??null,message:'Queued jobs require identity and work item.'});
  if(job.requiresApproval){
   const approval=approvals.find(a=>a.jobId===job.id&&a.status==='approved');
   if(!approval) findings.push({code:'approval.missing',severity:'blocking',jobId:job.id,message:'Required approval is missing.'});
   else if(!approval.actor||!approval.at||!normalize(approval.evidence).length) findings.push({code:'approval.evidence',severity:'blocking',jobId:job.id,message:'Approval lacks actor, timestamp, or evidence.'});
  }
  if(job.status==='leased'&&!job.lease?.workerId) findings.push({code:'lease.owner',severity:'blocking',jobId:job.id,message:'Leased job lacks worker ownership.'});
 }
 for(const intervention of interventions){
  if(!intervention.actor||!intervention.reason) findings.push({code:'intervention.audit',severity:'blocking',message:'Interventions require actor and reason.'});
  if(intervention.action==='alter-result'&&!normalize(intervention.evidence).length) findings.push({code:'intervention.evidence',severity:'blocking',message:'Result alterations require evidence.'});
 }
 const eventIds=new Set();
 for(const event of dispatchEvents){
  if(!event.id||eventIds.has(event.id)) findings.push({code:'event.integrity',severity:'blocking',message:'Dispatch event identifiers must be unique.'});
  eventIds.add(event.id);
 }
 findings.sort((a,b)=>severities[b.severity]-severities[a.severity]||a.code.localeCompare(b.code));
 const blocked=findings.some(f=>f.severity==='blocking');
 return {schemaVersion:'1.0.0',result:blocked?'FAIL':findings.length?'PASS WITH WARNINGS':'PASS',executionAllowed:!blocked,findings,counts:{queued:pending.length,approvals:approvals.length,interventions:interventions.length,events:dispatchEvents.length}};
}
export function assertOrchestrationCertified(input){const result=certifyOrchestration(input);if(!result.executionAllowed){const e=new Error('Orchestration certification failed');e.code='orchestration.certification';e.result=result;throw e;}return result;}
