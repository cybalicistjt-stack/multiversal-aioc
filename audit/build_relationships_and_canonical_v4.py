#!/usr/bin/env python3
"""Build typed relationships and canonical candidate envelopes from assembled objects."""
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
SCALAR=re.compile(r"^(?:DC\s*\d+|\d+(?:\.\d+)?\s*(?:ft|feet|miles?|hours?|minutes?|rounds?|turns?|XP|MC)|\d+d\d+(?:\s*[+-]\s*\d+)?)$",re.I)
PATTERNS=[
 ("requires",re.compile(r"\b(?:requires?|prerequisite(?:s)?)\s*[:\-]?\s*([^.;\n]{3,80})",re.I)),
 ("locatedIn",re.compile(r"\b(?:located in|native to|found in|originates? from)\s+([^.;\n]{3,80})",re.I)),
 ("belongsTo",re.compile(r"\b(?:belongs to|member of|part of|associated with)\s+([^.;\n]{3,80})",re.I)),
 ("usedBy",re.compile(r"\b(?:used by|available to|exclusive to)\s+([^.;\n]{3,80})",re.I)),
]
STOP={"the","a","an","this","that","characters","creatures","players","target","user","caster"}
def load(p): return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
def stable(*x): return hashlib.sha256('\n'.join(map(str,x)).encode()).hexdigest()[:20]
def slug(s): return re.sub(r'[^a-z0-9]+','-',str(s).lower()).strip('-')[:72]
def norm(s): return re.sub(r'[^a-z0-9]+',' ',str(s).lower()).strip()
def aliases_for(name):
 base=norm(name); out={base,re.sub(r'\b(?:the|a|an)\b',' ',base).strip(),re.sub(r'\([^)]*\)',' ',base).strip()}
 if ':' in name: out|={norm(name.split(':',1)[0]),norm(name.split(':',1)[1])}
 return {re.sub(r'\s+',' ',x).strip() for x in out if len(x.strip())>=3}
def token_similarity(a,b):
 sa=set(norm(a).split());sb=set(norm(b).split())
 return len(sa&sb)/len(sa|sb) if sa and sb else 0.0
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--assembly',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 rows=load(a.assembly/'assembled-objects.jsonl');aliases=defaultdict(list)
 for x in rows:
  for key in aliases_for(x['name']):aliases[key].append(x)
 out=[];edge_count=unresolved=scalar_blocked=0
 for x in rows:
  text=' '.join([x['name'],x['specification'].get('summary','')]+[v for vals in x.get('sectionMap',{}).values() for v in vals]);rel=[];seen=set()
  for typ,pat in PATTERNS:
   for m in pat.finditer(text):
    target=m.group(1).strip(' .,:;–—-');target=re.split(r'\b(?:and must|and may|when|if|while|which|who|that)\b',target,1,flags=re.I)[0].strip()
    if not target or SCALAR.match(target) or norm(target) in STOP:scalar_blocked+=1;continue
    key=norm(target);matches=[z for z in aliases.get(key,[]) if z['assemblyId']!=x['assemblyId']];chosen=None;resolution='unresolved';confidence=52
    if len(matches)==1:chosen=matches[0];resolution='exact-alias';confidence=94
    elif not matches:
     scored=[]
     for ak,vals in aliases.items():
      sim=token_similarity(key,ak)
      if sim>=0.85:
       for z in vals:
        if z['assemblyId']!=x['assemblyId']:scored.append((sim,z))
     scored.sort(key=lambda q:(-q[0],q[1]['name']))
     if scored and (len(scored)==1 or scored[0][0]>scored[1][0]):chosen=scored[0][1];resolution='fuzzy-alias';confidence=round(70+20*scored[0][0])
    sig=(typ,chosen['assemblyId'] if chosen else None,key)
    if sig in seen:continue
    seen.add(sig)
    if chosen:rel.append({'relationshipType':typ,'targetId':chosen['assemblyId'],'targetName':chosen['name'],'resolution':resolution,'confidence':confidence});edge_count+=1
    else:rel.append({'relationshipType':typ,'targetId':None,'targetName':target,'resolution':'unresolved','confidence':52});unresolved+=1
  cid=f"mv.{x['objectType']}.{slug(x['name'])}.{stable(x['assemblyId'])[:8]}";unresolved_here=any(r['targetId'] is None for r in rel)
  evidence_count=len(x.get('provenance') or []);section_count=len(x.get('sectionMap') or {})
  expert=(x.get('identityConfidence',0)>=92 and x['completenessScore']>=80 and x['familyMargin']>=6 and not unresolved_here and (evidence_count>=2 or section_count>=2))
  reviewable=(x.get('identityConfidence',0)>=75 and x['familyMargin']>=4)
  route='expert-sample' if expert else ('human-review' if reviewable else 'evidence-only')
  gates={'identityConfirmed':False,'sourceVerified':False,'duplicateResolved':False,'relationshipsReviewed':not unresolved_here,'schemaValidated':True,'designerApproved':False,'ownerApproved':False}
  out.append({'id':cid,'type':x['objectType'],'name':x['name'],'lifecycleStatus':'candidate','authority':'Non-canonical v4 candidate; no automatic import or merge.','specification':x['specification'],'relationships':rel,'provenance':x['provenance'],'recovery':{'assemblyId':x['assemblyId'],'candidateKind':x.get('candidateKind'),'documentGrammar':x['documentGrammar'],'completenessScore':x['completenessScore'],'identityConfidence':x.get('identityConfidence',0),'boundaryEvidenceCount':evidence_count,'sectionCount':section_count,'missingFields':x['missingFields'],'familyMargin':x['familyMargin']},'validation':{'schemaValid':True,'gates':gates},'reviewRoute':route})
 summary={'format':'multiversal-canonical-candidate-v4-index','version':'4.3.0','generatedAt':datetime.now(timezone.utc).isoformat(),'candidateCount':len(out),'familyCounts':dict(Counter(x['type'] for x in out)),'resolvedRelationshipCount':edge_count,'unresolvedRelationshipCount':unresolved,'scalarRelationshipBlockedCount':scalar_blocked,'expertSampleCount':sum(x['reviewRoute']=='expert-sample' for x in out),'humanReviewCount':sum(x['reviewRoute']=='human-review' for x in out),'evidenceOnlyCount':sum(x['reviewRoute']=='evidence-only' for x in out),'publishedSample':out[:200]}
 (a.out/'canonical-candidate-v4-index.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
 with (a.out/'canonical-candidates-v4.jsonl').open('w',encoding='utf-8') as f:
  for x in out:f.write(json.dumps(x,ensure_ascii=False)+'\n')
 print(json.dumps({k:summary[k] for k in ('candidateCount','familyCounts','resolvedRelationshipCount','unresolvedRelationshipCount','expertSampleCount','humanReviewCount','evidenceOnlyCount')},indent=2))
if __name__=='__main__':main()
