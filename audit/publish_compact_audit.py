#!/usr/bin/env python3
"""Publish bounded audit and semantic-recovery results to the static AIOC."""
from __future__ import annotations
import argparse,json,shutil
from datetime import datetime,timezone
from pathlib import Path
COMPACT_FILES=("corpus-status.json","archive-inventory.json","document-batch-schedule.json","reconciliation-report.json","csv-schema-registry.json","duplicate-groups.json","candidate-matches.json","audit-summary.json")
REFINED_FILES=("refinement-summary.json","likely-existing.json","possible-existing.json","possibly-existing.json","likely-new.json","ambiguous.json")
def read_json(p):
 try:return json.loads(p.read_text(encoding='utf-8'))
 except Exception:return None
def write_json(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def bounded(src,dst,keys):
 x=read_json(src)
 if not isinstance(x,dict):return None
 for k,n in keys.items():x[k]=list(x.get(k) or [])[:n]
 write_json(dst,x);return x
def publish_list(src,dst,n,published,label):
 x=read_json(src)
 if x is None:return None
 if isinstance(x,list):x=x[:n]
 write_json(dst,x);published.append(label);return x
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,default=Path('audit-output'));ap.add_argument('--destination',type=Path,default=Path('v2/audit-data'));ap.add_argument('--source-sha',default='');a=ap.parse_args();a.destination.mkdir(parents=True,exist_ok=True);pub=[]
 for n in COMPACT_FILES:
  s=a.source/n
  if s.exists():shutil.copy2(s,a.destination/n);pub.append(n)
 structure=bounded(a.source/'document-structure'/'document-structure-index.json',a.destination/'semantic-recovery'/'document-structure-index.json',{'publishedSample':200})
 if structure:pub.append('semantic-recovery/document-structure-index.json')
 parsers=bounded(a.source/'family-parsers'/'family-parser-index.json',a.destination/'semantic-recovery'/'family-parser-index.json',{'publishedSample':250})
 if parsers:pub.append('semantic-recovery/family-parser-index.json')
 graph=bounded(a.source/'knowledge-graph'/'knowledge-graph-index.json',a.destination/'semantic-recovery'/'knowledge-graph-index.json',{'publishedNodeSample':150,'publishedEdgeSample':200,'publishedUnresolvedSample':150})
 if graph:pub.append('semantic-recovery/knowledge-graph-index.json')
 for n in REFINED_FILES:publish_list(a.source/'refined'/n,a.destination/'refined'/n,250,pub,'refined/'+n)
 promotion=bounded(a.source/'promotion'/'promotion-index.json',a.destination/'promotion'/'promotion-index.json',{'publishedCandidateSample':250}); factory=bounded(a.source/'object-factory'/'object-factory-index.json',a.destination/'object-factory'/'object-factory-index.json',{'publishedSample':200}); recovery=bounded(a.source/'recovery'/'recovery-index.json',a.destination/'recovery'/'recovery-index.json',{'publishedSample':250,'relationshipSample':250})
 if promotion:pub.append('promotion/promotion-index.json')
 if factory:pub.append('object-factory/object-factory-index.json')
 if recovery:pub.append('recovery/recovery-index.json')
 status=read_json(a.source/'corpus-status.json') or {}; refinement=read_json(a.source/'refined'/'refinement-summary.json') or {}
 summary={'archiveCount':status.get('archiveCount',0),'pdfCount':status.get('pdfCount',0),'totalPages':status.get('totalPages',0),'completedPages':status.get('completedPages',0),'structureBlockCount':(structure or {}).get('blockCount',0),'parsedCandidateCount':(parsers or {}).get('candidateCount',0),'parsedFamilyCount':len((parsers or {}).get('familyCounts',{})),'graphNodeCount':(graph or {}).get('nodeCount',0),'graphEdgeCount':(graph or {}).get('edgeCount',0),'graphUnresolvedCount':(graph or {}).get('unresolvedRelationshipCount',0),'reviewCandidateCount':refinement.get('reviewCandidateCount',0),'promotionCandidateCount':(promotion or {}).get('candidateCount',0),'factoryCandidateCount':(factory or {}).get('consolidatedCandidateCount',0),'recoveryCandidateCount':(recovery or {}).get('candidateCount',0),'machineScanComplete':bool(status.get('automaticAuditComplete') or status.get('machineScanComplete'))}
 manifest={'format':'multiversal-static-audit-publication','version':'2.0.0','publishedAt':datetime.now(timezone.utc).isoformat(),'sourceCommit':a.source_sha,'publishedFiles':pub,'summary':summary};write_json(a.destination/'publication-manifest.json',manifest);print(json.dumps(manifest,indent=2))
if __name__=='__main__':main()
