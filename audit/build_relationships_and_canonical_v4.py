#!/usr/bin/env python3
"""Build typed relationships and canonical candidate envelopes from assembled objects."""
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
SCALAR=re.compile(r"^(?:DC\s*\d+|\d+(?:\.\d+)?\s*(?:ft|feet|miles?|hours?|minutes?|rounds?|turns?|XP|MC)|\d+d\d+(?:\s*[+-]\s*\d+)?)$",re.I)
PATTERNS=[("requires",re.compile(r"\b(?:requires?|prerequisite)\s*[:\-]?\s*([A-Z][A-Za-z0-9 '&’\-]{2,60})",re.I)),("locatedIn",re.compile(r"\b(?:located in|native to|found in)\s+([A-Z][A-Za-z0-9 '&’\-]{2,60})",re.I)),("belongsTo",re.compile(r"\b(?:belongs to|member of|part of)\s+([A-Z][A-Za-z0-9 '&’\-]{2,60})",re.I)),("usedBy",re.compile(r"\b(?:used by|available to)\s+([A-Z][A-Za-z0-9 '&’\-]{2,60})",re.I))]
def load(p): return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
def stable(*x): return hashlib.sha256('\n'.join(map(str,x)).encode()).hexdigest()[:20]
def slug(s): return re.sub(r'[^a-z0-9]+','-',str(s).lower()).strip('-')[:72]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--assembly',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 rows=load(a.assembly/'assembled-objects.jsonl'); aliases=defaultdict(list)
 for x in rows: aliases[re.sub(r'\W+','',x['name'].lower())].append(x)
 out=[]; edge_count=0; unresolved=0
 for x in rows:
  text=' '.join([x['name'],x['specification'].get('summary','')]+[v for vals in x.get('sectionMap',{}).values() for v in vals])
  rel=[]
  for typ,pat in PATTERNS:
   for m in pat.finditer(text):
    target=m.group(1).strip(' .,:;')
    if SCALAR.match(target): continue
    key=re.sub(r'\W+','',target.lower()); matches=aliases.get(key,[])
    if len(matches)==1 and matches[0]['assemblyId']!=x['assemblyId']:
     rel.append({'relationshipType':typ,'targetId':matches[0]['assemblyId'],'targetName':matches[0]['name'],'resolution':'exact-alias','confidence':92}) ; edge_count+=1
    else:
     rel.append({'relationshipType':typ,'targetId':None,'targetName':target,'resolution':'unresolved','confidence':55}); unresolved+=1
  cid=f"mv.{x['objectType']}.{slug(x['name'])}.{stable(x['assemblyId'])[:8]}"
  gates={'identityConfirmed':False,'sourceVerified':False,'duplicateResolved':False,'relationshipsReviewed':not any(r['targetId'] is None for r in rel),'schemaValidated':True,'designerApproved':False,'ownerApproved':False}
  out.append({'id':cid,'type':x['objectType'],'name':x['name'],'lifecycleStatus':'candidate','authority':'Non-canonical v4 candidate; no automatic import or merge.','specification':x['specification'],'relationships':rel,'provenance':x['provenance'],'recovery':{'assemblyId':x['assemblyId'],'documentGrammar':x['documentGrammar'],'completenessScore':x['completenessScore'],'missingFields':x['missingFields'],'familyMargin':x['familyMargin']},'validation':{'schemaValid':True,'gates':gates},'reviewRoute':'expert-sample' if x['completenessScore']>=75 and x['familyMargin']>=3 else 'human-review'})
 summary={'format':'multiversal-canonical-candidate-v4-index','version':'4.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'candidateCount':len(out),'familyCounts':dict(Counter(x['type'] for x in out)),'resolvedRelationshipCount':edge_count,'unresolvedRelationshipCount':unresolved,'expertSampleCount':sum(x['reviewRoute']=='expert-sample' for x in out),'humanReviewCount':sum(x['reviewRoute']=='human-review' for x in out),'publishedSample':out[:200]}
 (a.out/'canonical-candidate-v4-index.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
 with (a.out/'canonical-candidates-v4.jsonl').open('w',encoding='utf-8') as f:
  for x in out:f.write(json.dumps(x,ensure_ascii=False)+'\n')
 print(json.dumps({k:summary[k] for k in ('candidateCount','familyCounts','resolvedRelationshipCount','unresolvedRelationshipCount','expertSampleCount')},indent=2))
if __name__=='__main__':main()
