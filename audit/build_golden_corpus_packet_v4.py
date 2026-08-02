#!/usr/bin/env python3
"""Create a stratified Golden Corpus annotation packet from v4 candidates."""
from __future__ import annotations
import argparse, json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

def load(p): return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--candidates',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--per-family',type=int,default=20);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 rows=load(a.candidates/'canonical-candidates-v4.jsonl'); by=defaultdict(list)
 for x in rows: by[x['type']].append(x)
 records=[]
 for family in sorted(by):
  ranked=sorted(by[family],key=lambda x:(-x['recovery']['completenessScore'],-x['recovery']['familyMargin'],x['name']))
  for x in ranked[:a.per_family]:
   records.append({'goldenId':'golden-pending-'+x['id'],'verificationStatus':'pending','shouldExtract':True,'objectType':x['type'],'name':x['name'],'sourcePath':(x.get('provenance') or [{}])[0].get('sourcePath'),'candidateId':x['id'],'reviewChecks':['Distinct object identity','Correct object family','Complete object boundary','Correct child-section assembly','Accurate fields','Accurate relationships','Complete provenance'],'decision':None,'notes':''})
 payload={'format':'multiversal-golden-corpus-v4-annotation-packet','version':'4.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'recordCount':len(records),'familyCounts':{k:min(a.per_family,len(v)) for k,v in sorted(by.items())},'instructions':['Review against the cited source.','Set verificationStatus to verified only after checking the source.','Set shouldExtract false for headings, fragments, containers, examples, and duplicate representations.','Correct objectType and name when necessary.','This packet validates extraction and does not authorize canonical import.'],'records':records}
 (a.out/'golden-corpus-annotation-packet.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({'records':len(records),'families':payload['familyCounts']},indent=2))
if __name__=='__main__':main()
