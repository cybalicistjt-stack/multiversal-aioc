#!/usr/bin/env python3
"""Evaluate v4 candidates against a versioned Golden Corpus manifest.

The manifest may contain verified examples or pending annotation targets. Pending
records are sampled but do not count toward precision/recall gates.
"""
from __future__ import annotations
import argparse, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

def load_jsonl(p): return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
def norm(s): return re.sub(r'\W+','',str(s or '').lower())
def safe_div(a,b): return a/b if b else 0.0

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--candidates',type=Path,required=True);ap.add_argument('--golden',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 candidates=load_jsonl(a.candidates/'canonical-candidates-v4.jsonl'); manifest=json.loads(a.golden.read_text(encoding='utf-8'))
 verified=[x for x in manifest.get('records',[]) if x.get('verificationStatus')=='verified']; pending=[x for x in manifest.get('records',[]) if x.get('verificationStatus')!='verified']
 by_key=defaultdict(list)
 for c in candidates: by_key[(c['type'],norm(c['name']))].append(c)
 tp=fp=fn=0; family=defaultdict(lambda:{'tp':0,'fp':0,'fn':0}); details=[]
 expected_keys={(g['objectType'],norm(g['name'])) for g in verified if g.get('shouldExtract',True)}
 for g in verified:
  key=(g['objectType'],norm(g['name'])); matches=by_key.get(key,[]); should=g.get('shouldExtract',True)
  if should and matches:
   tp+=1;family[g['objectType']]['tp']+=1;details.append({'goldenId':g['goldenId'],'result':'true-positive','candidateIds':[m['id'] for m in matches]})
  elif should:
   fn+=1;family[g['objectType']]['fn']+=1;details.append({'goldenId':g['goldenId'],'result':'false-negative'})
  elif matches:
   fp+=len(matches);family[g['objectType']]['fp']+=len(matches);details.append({'goldenId':g['goldenId'],'result':'false-positive','candidateIds':[m['id'] for m in matches]})
  else: details.append({'goldenId':g['goldenId'],'result':'true-negative'})
 # Only evaluate extra false positives in documents represented by verified records.
 verified_docs={g.get('sourcePath') for g in verified if g.get('sourcePath')}
 for c in candidates:
  docs={p.get('sourcePath') for p in c.get('provenance',[])}
  if docs & verified_docs and (c['type'],norm(c['name'])) not in expected_keys:
   fp+=1;family[c['type']]['fp']+=1
 precision=safe_div(tp,tp+fp);recall=safe_div(tp,tp+fn);f1=safe_div(2*precision*recall,precision+recall)
 family_metrics={}
 for k,v in sorted(family.items()):
  p=safe_div(v['tp'],v['tp']+v['fp']);r=safe_div(v['tp'],v['tp']+v['fn']);family_metrics[k]={**v,'precision':round(p,4),'recall':round(r,4),'f1':round(safe_div(2*p*r,p+r),4)}
 gates={'verifiedCorpusExists':len(verified)>=25,'familyCoverage':len({x['objectType'] for x in verified})>=5,'precisionAtLeast090':precision>=.90,'recallAtLeast080':recall>=.80,'f1AtLeast085':f1>=.85}
 report={'format':'multiversal-golden-corpus-v4-evaluation','version':'4.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'verifiedRecordCount':len(verified),'pendingAnnotationCount':len(pending),'candidateCount':len(candidates),'truePositive':tp,'falsePositive':fp,'falseNegative':fn,'precision':round(precision,4),'recall':round(recall,4),'f1':round(f1,4),'familyMetrics':family_metrics,'gates':gates,'engineeringConvergencePassed':all(gates.values()),'details':details[:500],'pendingAnnotationSample':pending[:100]}
 (a.out/'golden-corpus-evaluation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({k:report[k] for k in ('verifiedRecordCount','pendingAnnotationCount','precision','recall','f1','gates','engineeringConvergencePassed')},indent=2))
if __name__=='__main__':main()
