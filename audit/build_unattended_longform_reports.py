#!/usr/bin/env python3
"""Build unattended, non-canonical long-form analysis reports from Semantic Recovery v4.

The script consumes the latest canonical candidate JSONL and produces review-prep
artifacts only. It never modifies canonical content.
"""
from __future__ import annotations
import argparse, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

FAMILIES=("rule","ability","creature","item","species","npc","vehicle","environment","world","faction","adventure")
GENERIC={"overview","introduction","summary","background","campaign use","notes","examples","mechanics","traits","actions","statistics"}
STATISH=re.compile(r"^(?:AC|HP|CR|DC|Speed|STR|DEX|CON|INT|WIS|CHA|Saving Throws?|Skills?)\s*[:=]",re.I)

def load(path:Path):
 return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]
def norm(s): return re.sub(r'[^a-z0-9]+',' ',str(s or '').lower()).strip()
def write_json(path:Path,obj): path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def anomaly_reasons(x):
 out=[]; name=str(x.get('name') or '').strip(); r=x.get('recovery') or {}; spec=x.get('specification') or {}
 if STATISH.search(name): out.append('stat-field-identity')
 if norm(name) in GENERIC: out.append('generic-heading')
 if r.get('boundaryEvidenceCount',0)<=1: out.append('single-boundary-evidence')
 if r.get('sectionCount',0)<=1: out.append('single-section')
 if r.get('completenessScore',0)<75: out.append('low-completeness')
 if r.get('familyMargin',0)<6: out.append('weak-family-margin')
 if any(rel.get('targetId') is None for rel in x.get('relationships') or []): out.append('unresolved-relationship')
 return out

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--candidates',type=Path,required=True); ap.add_argument('--out',type=Path,required=True); ap.add_argument('--batch-size',type=int,default=40); a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
 rows=load(a.candidates/'canonical-candidates-v4.jsonl')
 by=defaultdict(list)
 for x in rows: by[x.get('type','unknown')].append(x)

 # Family review batches.
 packet_dir=a.out/'family-packets'; packet_dir.mkdir(exist_ok=True)
 packet_index=[]
 for family in sorted(by):
  ranked=sorted(by[family],key=lambda x:(x.get('reviewRoute')!='expert-sample',-(x.get('recovery') or {}).get('identityConfidence',0),-(x.get('recovery') or {}).get('completenessScore',0),x.get('name','')))
  for i in range(0,len(ranked),a.batch_size):
   chunk=ranked[i:i+a.batch_size]; fn=f'{family}-batch-{i//a.batch_size+1:03d}.json'
   write_json(packet_dir/fn,{'format':'multiversal-unattended-family-review-batch','family':family,'batchNumber':i//a.batch_size+1,'recordCount':len(chunk),'records':chunk})
   packet_index.append({'family':family,'file':fn,'recordCount':len(chunk)})

 # Duplicate clusters by normalized family/name.
 dup=defaultdict(list)
 for x in rows: dup[(x.get('type'),norm(x.get('name')))].append(x)
 clusters=[]
 for (family,name),vals in dup.items():
  if name and len(vals)>1:
   clusters.append({'family':family,'normalizedName':name,'count':len(vals),'candidateIds':[v.get('id') for v in vals],'sourcePaths':sorted({(v.get('provenance') or [{}])[0].get('sourcePath') for v in vals})})
 clusters.sort(key=lambda z:(-z['count'],z['family'],z['normalizedName']))
 write_json(a.out/'duplicate-clusters.json',{'format':'multiversal-unattended-duplicate-clusters','clusterCount':len(clusters),'clusters':clusters})

 # Boundary/anomaly diagnostics.
 anomalies=[]; reason_counts=Counter()
 for x in rows:
  reasons=anomaly_reasons(x)
  if reasons:
   reason_counts.update(reasons); anomalies.append({'candidateId':x.get('id'),'type':x.get('type'),'name':x.get('name'),'reviewRoute':x.get('reviewRoute'),'reasons':reasons,'source':(x.get('provenance') or [{}])[0],'recovery':x.get('recovery')})
 anomalies.sort(key=lambda z:(-len(z['reasons']),z['type'],z['name']))
 write_json(a.out/'boundary-anomalies.json',{'format':'multiversal-unattended-boundary-anomalies','recordCount':len(anomalies),'reasonCounts':dict(reason_counts),'records':anomalies})

 # Schema gaps and relationship diagnostics.
 gaps=defaultdict(Counter); rel=Counter(); unresolved=[]
 for x in rows:
  family=x.get('type'); gaps[family].update((x.get('recovery') or {}).get('missingFields') or [])
  for edge in x.get('relationships') or []:
   rel[edge.get('relationshipType','unknown')]+=1
   if edge.get('targetId') is None: unresolved.append({'candidateId':x.get('id'),'sourceName':x.get('name'),'relationshipType':edge.get('relationshipType'),'targetName':edge.get('targetName'),'source':(x.get('provenance') or [{}])[0]})
 write_json(a.out/'schema-gap-report.json',{'format':'multiversal-unattended-schema-gap-report','families':{f:dict(gaps[f]) for f in sorted(gaps)}})
 write_json(a.out/'relationship-diagnostics.json',{'format':'multiversal-unattended-relationship-diagnostics','relationshipTypeCounts':dict(rel),'unresolvedCount':len(unresolved),'unresolved':unresolved})

 # Prioritized backlog.
 backlog=[]
 for x in rows:
  r=x.get('recovery') or {}; reasons=anomaly_reasons(x)
  score=(100-r.get('identityConfidence',0))*2+(100-r.get('completenessScore',0))+len(reasons)*10+(15 if x.get('reviewRoute')=='evidence-only' else 0)
  backlog.append({'priorityScore':score,'candidateId':x.get('id'),'type':x.get('type'),'name':x.get('name'),'reviewRoute':x.get('reviewRoute'),'reasons':reasons,'source':(x.get('provenance') or [{}])[0]})
 backlog.sort(key=lambda z:(-z['priorityScore'],z['type'],z['name']))
 write_json(a.out/'prioritized-review-backlog.json',{'format':'multiversal-unattended-prioritized-review-backlog','recordCount':len(backlog),'records':backlog})

 summary={'format':'multiversal-unattended-longform-index','version':'1.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'candidateCount':len(rows),'familyCounts':dict(Counter(x.get('type') for x in rows)),'familyPacketCount':len(packet_index),'duplicateClusterCount':len(clusters),'anomalyCount':len(anomalies),'unresolvedRelationshipCount':len(unresolved),'outputs':['family-packets/','duplicate-clusters.json','boundary-anomalies.json','schema-gap-report.json','relationship-diagnostics.json','prioritized-review-backlog.json'],'authorityNote':'Diagnostics and review preparation only; no canonical writes or approvals.'}
 write_json(a.out/'unattended-longform-index.json',summary)
 print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
