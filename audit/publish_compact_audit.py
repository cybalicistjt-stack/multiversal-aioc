#!/usr/bin/env python3
"""Publish bounded forensic, factory, recovery, and handoff results to the static AIOC."""
from __future__ import annotations
import argparse, json, shutil
from datetime import datetime, timezone
from pathlib import Path
COMPACT_FILES=("corpus-status.json","archive-inventory.json","document-batch-schedule.json","reconciliation-report.json","csv-schema-registry.json","duplicate-groups.json","candidate-matches.json","audit-summary.json")
REFINED_FILES=("refinement-summary.json","likely-existing.json","possible-existing.json","possibly-existing.json","likely-new.json","ambiguous.json")

def read_json(path):
 try:return json.loads(path.read_text(encoding='utf-8'))
 except Exception:return None
def write_json(path,payload): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def bounded_index(src,dst,sample_key,limit):
 p=read_json(src)
 if not isinstance(p,dict): return None
 p[sample_key]=list(p.get(sample_key) or [])[:limit]; write_json(dst,p); return p

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source',type=Path,default=Path('audit-output')); ap.add_argument('--destination',type=Path,default=Path('v2/audit-data')); ap.add_argument('--source-sha',default=''); a=ap.parse_args(); a.destination.mkdir(parents=True,exist_ok=True); published=[]
 for n in COMPACT_FILES:
  s=a.source/n
  if s.exists(): shutil.copy2(s,a.destination/n); published.append(n)
 for n in REFINED_FILES:
  p=read_json(a.source/'refined'/n)
  if p is not None:
   if isinstance(p,list): p=p[:250]
   write_json(a.destination/'refined'/n,p); published.append('refined/'+n)
 promotion=bounded_index(a.source/'promotion'/'promotion-index.json',a.destination/'promotion'/'promotion-index.json','publishedCandidateSample',250)
 if promotion: published.append('promotion/promotion-index.json')
 factory=bounded_index(a.source/'object-factory'/'object-factory-index.json',a.destination/'object-factory'/'object-factory-index.json','publishedSample',200)
 if factory: published.append('object-factory/object-factory-index.json')
 recovery=bounded_index(a.source/'recovery'/'recovery-index.json',a.destination/'recovery'/'recovery-index.json','publishedSample',250)
 if recovery:
  recovery['relationshipSample']=list(recovery.get('relationshipSample') or [])[:250]; write_json(a.destination/'recovery'/'recovery-index.json',recovery); published.append('recovery/recovery-index.json')
 handoff=bounded_index(a.source/'handoffs'/'recovery-handoff-index.json',a.destination/'handoffs'/'recovery-handoff-index.json','publishedSample',200)
 if handoff: published.append('handoffs/recovery-handoff-index.json')
 for n in ('relationship-resolution-queue.json','source-completion-receipts.json'):
  p=read_json(a.source/'handoffs'/n)
  if p is not None:
   if isinstance(p,list): p=p[:300]
   write_json(a.destination/'handoffs'/n,p); published.append('handoffs/'+n)
 status=read_json(a.source/'corpus-status.json') or {}; refinement=read_json(a.source/'refined'/'refinement-summary.json') or {}
 manifest={'format':'multiversal-static-audit-publication','version':'1.5.0','publishedAt':datetime.now(timezone.utc).isoformat(),'sourceCommit':a.source_sha,'publishedFiles':published,'summary':{'archiveCount':status.get('archiveCount',0),'pdfCount':status.get('pdfCount',0),'totalPages':status.get('totalPages',0),'completedPages':status.get('completedPages',0),'reviewCandidateCount':refinement.get('reviewCandidateCount',0),'promotionCandidateCount':(promotion or {}).get('candidateCount',0),'factoryCandidateCount':(factory or {}).get('consolidatedCandidateCount',0),'recoveryCandidateCount':(recovery or {}).get('candidateCount',0),'readyForDesignerReview':(recovery or {}).get('readyForDesignerReview',0),'relationshipCandidateCount':(recovery or {}).get('relationshipCandidateCount',0),'handoffCandidateCount':(handoff or {}).get('candidateCount',0),'handoffReadyForReview':(handoff or {}).get('readyForReviewCount',0),'unresolvedRelationshipCount':(handoff or {}).get('unresolvedRelationshipCount',0),'sourceGroupCount':(handoff or {}).get('sourceGroupCount',0),'machineScanComplete':bool(status.get('automaticAuditComplete') or status.get('machineScanComplete')),'humanReviewComplete':bool(status.get('humanReviewComplete')),'canonicalPromotionComplete':bool(status.get('canonicalPromotionComplete'))}}
 write_json(a.destination/'publication-manifest.json',manifest); print(json.dumps(manifest,indent=2))
if __name__=='__main__': main()
