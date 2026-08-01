#!/usr/bin/env python3
"""Publish bounded audit, recovery, acceptance, readiness, and owner-review results."""
from __future__ import annotations
import argparse, json, shutil
from datetime import datetime, timezone
from pathlib import Path
COMPACT_FILES=("corpus-status.json","archive-inventory.json","document-batch-schedule.json","reconciliation-report.json","csv-schema-registry.json","duplicate-groups.json","candidate-matches.json","audit-summary.json")
REFINED_FILES=("refinement-summary.json","likely-existing.json","possible-existing.json","possibly-existing.json","likely-new.json","ambiguous.json")
def read_json(path):
 try:return json.loads(path.read_text(encoding='utf-8'))
 except Exception:return None
def write_json(path,payload):
 path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def bounded_index(src,dst,sample_keys):
 payload=read_json(src)
 if not isinstance(payload,dict):return None
 for key,limit in sample_keys.items():payload[key]=list(payload.get(key) or [])[:limit]
 write_json(dst,payload);return payload
def publish_list(src,dst,limit,published,label):
 payload=read_json(src)
 if payload is None:return None
 if isinstance(payload,list):payload=payload[:limit]
 write_json(dst,payload);published.append(label);return payload
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,default=Path('audit-output'));ap.add_argument('--destination',type=Path,default=Path('v2/audit-data'));ap.add_argument('--source-sha',default='');a=ap.parse_args();a.destination.mkdir(parents=True,exist_ok=True);published=[]
 for name in COMPACT_FILES:
  src=a.source/name
  if src.exists():shutil.copy2(src,a.destination/name);published.append(name)
 for name in REFINED_FILES:publish_list(a.source/'refined'/name,a.destination/'refined'/name,250,published,'refined/'+name)
 promotion=bounded_index(a.source/'promotion'/'promotion-index.json',a.destination/'promotion'/'promotion-index.json',{'publishedCandidateSample':250});
 if promotion:published.append('promotion/promotion-index.json')
 factory=bounded_index(a.source/'object-factory'/'object-factory-index.json',a.destination/'object-factory'/'object-factory-index.json',{'publishedSample':200});
 if factory:published.append('object-factory/object-factory-index.json')
 recovery=bounded_index(a.source/'recovery'/'recovery-index.json',a.destination/'recovery'/'recovery-index.json',{'publishedSample':250,'relationshipSample':250});
 if recovery:published.append('recovery/recovery-index.json')
 handoff=bounded_index(a.source/'handoffs'/'recovery-handoff-index.json',a.destination/'handoffs'/'recovery-handoff-index.json',{'publishedSample':200});
 if handoff:published.append('handoffs/recovery-handoff-index.json')
 for name in ('relationship-resolution-queue.json','source-completion-receipts.json'):publish_list(a.source/'handoffs'/name,a.destination/'handoffs'/name,300,published,'handoffs/'+name)
 staging=bounded_index(a.source/'production-staging'/'production-staging-index.json',a.destination/'production-staging'/'production-staging-index.json',{'publishedSample':150,'blockedSample':150});
 if staging:published.append('production-staging/production-staging-index.json')
 acceptance=bounded_index(a.source/'canonical-acceptance'/'canonical-acceptance-index.json',a.destination/'canonical-acceptance'/'canonical-acceptance-index.json',{'publishedAcceptanceSample':150,'publishedResolutionSample':150});
 if acceptance:published.append('canonical-acceptance/canonical-acceptance-index.json')
 for name in ('blocker-resolution-queue.json','source-closure-receipts.json'):publish_list(a.source/'canonical-acceptance'/name,a.destination/'canonical-acceptance'/name,300,published,'canonical-acceptance/'+name)
 merge=bounded_index(a.source/'merge-readiness'/'merge-readiness-index.json',a.destination/'merge-readiness'/'merge-readiness-index.json',{'publishedPlanSample':150,'publishedReadinessSample':150});
 if merge:published.append('merge-readiness/merge-readiness-index.json')
 for name in ('source-merge-readiness.json','post-import-validation-receipts.json'):publish_list(a.source/'merge-readiness'/name,a.destination/'merge-readiness'/name,300,published,'merge-readiness/'+name)
 owner=bounded_index(a.source/'owner-review'/'owner-review-index.json',a.destination/'owner-review'/'owner-review-index.json',{'publishedReviewSample':150,'publishedClosureSample':150});
 if owner:published.append('owner-review/owner-review-index.json')
 for name in ('merge-decision-ledger.json','final-source-closure-certificates.json'):publish_list(a.source/'owner-review'/name,a.destination/'owner-review'/name,300,published,'owner-review/'+name)
 status=read_json(a.source/'corpus-status.json') or {};refinement=read_json(a.source/'refined'/'refinement-summary.json') or {}
 summary={'archiveCount':status.get('archiveCount',0),'pdfCount':status.get('pdfCount',0),'totalPages':status.get('totalPages',0),'completedPages':status.get('completedPages',0),'reviewCandidateCount':refinement.get('reviewCandidateCount',0),'promotionCandidateCount':(promotion or {}).get('candidateCount',0),'factoryCandidateCount':(factory or {}).get('consolidatedCandidateCount',0),'recoveryCandidateCount':(recovery or {}).get('candidateCount',0),'productionStagedCount':(staging or {}).get('stagedCount',0),'productionBlockedCount':(staging or {}).get('blockedCount',0),'acceptanceCandidateCount':(acceptance or {}).get('acceptanceCandidateCount',0),'mergePlanCount':(merge or {}).get('acceptanceEntryCount',0),'mergeOpenBlockerCount':(merge or {}).get('openBlockerCount',0),'ownerReviewPacketCount':(owner or {}).get('reviewPacketCount',0),'ownerReviewBatchCount':(owner or {}).get('reviewBatchCount',0),'finalSourceClosureCount':(owner or {}).get('sourceClosureCertificateCount',0),'machineScanComplete':bool(status.get('automaticAuditComplete') or status.get('machineScanComplete')),'humanReviewComplete':bool(status.get('humanReviewComplete')),'canonicalPromotionComplete':bool(status.get('canonicalPromotionComplete'))}
 manifest={'format':'multiversal-static-audit-publication','version':'1.9.0','publishedAt':datetime.now(timezone.utc).isoformat(),'sourceCommit':a.source_sha,'publishedFiles':published,'summary':summary}
 write_json(a.destination/'publication-manifest.json',manifest);print(json.dumps(manifest,indent=2))
if __name__=='__main__':main()
