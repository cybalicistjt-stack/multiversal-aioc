#!/usr/bin/env python3
"""Create a quality-stratified Golden Corpus annotation packet from v4 candidates."""
from __future__ import annotations
import argparse, json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

def load(p): return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
def score(x):
 r=x.get('recovery',{})
 return (r.get('identityConfidence',0),r.get('completenessScore',0),r.get('familyMargin',0),-len(x.get('relationships',[])))
def record(x,kind,default_extract):
 return {'goldenId':'golden-pending-'+x['id'],'sampleKind':kind,'verificationStatus':'pending','shouldExtract':default_extract,'objectType':x['type'],'name':x['name'],'sourcePath':(x.get('provenance') or [{}])[0].get('sourcePath'),'candidateId':x['id'],'qualitySnapshot':{'reviewRoute':x.get('reviewRoute'),'identityConfidence':x.get('recovery',{}).get('identityConfidence'),'completenessScore':x.get('recovery',{}).get('completenessScore'),'familyMargin':x.get('recovery',{}).get('familyMargin'),'relationshipCount':len(x.get('relationships',[]))},'reviewChecks':['Distinct object identity','Correct object family','Complete object boundary','Correct child-section assembly','Accurate fields','Accurate relationships','Complete provenance'],'decision':None,'notes':''}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--candidates',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--per-family',type=int,default=12);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 rows=load(a.candidates/'canonical-candidates-v4.jsonl'); by=defaultdict(list)
 for x in rows: by[x['type']].append(x)
 records=[]; counts=Counter()
 for family in sorted(by):
  ranked=sorted(by[family],key=lambda x:(-score(x)[0],-score(x)[1],-score(x)[2],x['name']))
  positives=[x for x in ranked if x.get('reviewRoute')=='expert-sample'][:min(8,a.per_family)]
  remaining=[x for x in ranked if x not in positives]
  challenges=[]
  if remaining:
   challenges.append(remaining[0])
   challenges.append(remaining[len(remaining)//2])
   challenges.append(remaining[-1])
  unique=[]; seen=set()
  for x in positives+challenges:
   if x['id'] in seen: continue
   seen.add(x['id']); unique.append(x)
  for x in unique[:a.per_family]:
   kind='probable-positive' if x in positives else 'boundary-challenge'
   records.append(record(x,kind,kind=='probable-positive'));counts[family]+=1
 payload={'format':'multiversal-golden-corpus-v4-annotation-packet','version':'4.2.0','generatedAt':datetime.now(timezone.utc).isoformat(),'recordCount':len(records),'familyCounts':dict(counts),'sampleKindCounts':dict(Counter(x['sampleKind'] for x in records)),'instructions':['Review against the cited source.','Probable-positive records test precision; boundary-challenge records test rejection and correction behavior.','Set verificationStatus to verified only after checking the source.','Set shouldExtract false for headings, fragments, containers, examples, generators, taxonomy pages, procedures, and duplicate representations.','Correct objectType and name when necessary.','This packet validates extraction and does not authorize canonical import.'],'records':records}
 (a.out/'golden-corpus-annotation-packet.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({'records':len(records),'families':payload['familyCounts'],'sampleKinds':payload['sampleKindCounts']},indent=2))
if __name__=='__main__':main()
