#!/usr/bin/env python3
"""Build specialized recovery queues, relationship candidates, and coverage maps.

Consumes Object Factory batches. Outputs remain non-canonical and require review.
"""
from __future__ import annotations
import argparse, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

FAMILIES=("rule","ability","creature","item","species","world","npc","vehicle","environment","adventure","faction")
RELATION_PATTERNS={
 "requires":re.compile(r"\b(?:requires?|prerequisite)\s*[:\-]?\s*([A-Z][A-Za-z0-9 '&-]{2,60})",re.I),
 "belongsTo":re.compile(r"\b(?:tree|discipline|school|style|category)\s*[:\-]?\s*([A-Z][A-Za-z0-9 '&-]{2,60})",re.I),
 "usedBy":re.compile(r"\b(?:used by|available to|for)\s+([A-Z][A-Za-z0-9 '&-]{2,60})",re.I),
 "locatedIn":re.compile(r"\b(?:found in|located in|native to|from)\s+([A-Z][A-Za-z0-9 '&-]{2,60})",re.I),
}

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def clean(v): return re.sub(r"\s+"," ",str(v or '')).strip()
def source_group(path):
 p=clean(path).replace('\\','/')
 parts=p.split('/')
 return '/'.join(parts[:3]) if len(parts)>=3 else p

def recover(candidate):
 env=candidate.get('canonicalEnvelope') or {}
 spec=env.get('spec') or {}; text=clean(spec.get('legacyText'))
 typ=env.get('objectType') or 'rule'; name=clean(env.get('name'))
 rel=[]
 for kind,pat in RELATION_PATTERNS.items():
  for m in pat.finditer(text):
   target=clean(m.group(1)).rstrip('.,;:')
   if target and target.lower()!=name.lower(): rel.append({'type':kind,'targetName':target,'status':'candidate'})
 fields={'summary':text[:500],'mechanicSignals':spec.get('mechanicSignals') or []}
 if typ=='ability': fields.update({'cost':None,'activation':None,'range':None,'duration':None,'prerequisites':[],'scaling':[]})
 elif typ=='rule': fields.update({'procedure':[],'exceptions':[],'optional':bool(re.search(r'\boptional\b',text,re.I))})
 elif typ=='creature': fields.update({'statBlock':{},'attacks':[],'traits':[],'ecology':None,'variants':[]})
 elif typ=='item': fields.update({'itemCategory':None,'cost':None,'weight':None,'effects':[],'crafting':None})
 elif typ=='species': fields.update({'traits':[],'adaptations':[],'progression':[]})
 elif typ=='world': fields.update({'locations':[],'cultures':[],'factions':[],'rules':[]})
 elif typ=='npc': fields.update({'role':None,'speciesId':None,'affiliations':[],'abilities':[]})
 elif typ=='vehicle': fields.update({'vehicleClass':None,'crew':None,'components':[],'upgrades':[]})
 elif typ=='environment': fields.update({'hazards':[],'adaptations':[],'travelRules':[]})
 elif typ=='adventure': fields.update({'scenes':[],'encounters':[],'clues':[],'objectives':[]})
 elif typ=='faction': fields.update({'goals':[],'members':[],'relationships':[]})
 missing=[k for k,v in fields.items() if v in (None,[],{}) and k not in ('mechanicSignals',)]
 evidence=env.get('provenance') or []
 return {'candidateId':candidate.get('candidateId'),'objectType':typ,'name':name,'recommendedPack':candidate.get('recommendedPack'),'sourceTier':candidate.get('candidateTier'),'evidence':evidence,'recoveredSpec':fields,'relationshipCandidates':rel,'missingFields':missing,'readinessScore':max(0,100-len(missing)*8-(0 if evidence else 25)),'status':'recovery-candidate','authority':'Non-canonical until reviewed and owner approved.'}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--factory',type=Path,required=True); ap.add_argument('--out',type=Path,required=True); ap.add_argument('--batch-size',type=int,default=50); a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
 rows=[]
 for p in sorted(a.factory.glob('factory-*.json')): rows.extend(load(p).get('candidates',[]))
 recovered=[recover(x) for x in rows]; recovered.sort(key=lambda x:(x['objectType'], -x['readinessScore'], x['name'].lower()))
 by_family=defaultdict(list)
 for r in recovered: by_family[r['objectType']].append(r)
 relations=[{'sourceCandidateId':r['candidateId'],'sourceName':r['name'],**rel} for r in recovered for rel in r['relationshipCandidates']]
 coverage=[]
 groups=defaultdict(lambda:Counter())
 for r in recovered:
  src=(r['evidence'][0].get('sourcePath') if r['evidence'] else 'unknown')
  g=source_group(src); groups[g]['candidates']+=1; groups[g]['ready']+=int(r['readinessScore']>=76); groups[g]['relationships']+=len(r['relationshipCandidates'])
 for g,c in sorted(groups.items()): coverage.append({'sourceGroup':g,'candidateCount':c['candidates'],'readyCount':c['ready'],'relationshipCount':c['relationships'],'coveragePercent':round(100*c['ready']/max(1,c['candidates']),2)})
 batches=[]
 for family,items in sorted(by_family.items()):
  for i in range(0,len(items),a.batch_size):
   bid=f'{family}-recovery-{i//a.batch_size+1:04d}'; chunk=items[i:i+a.batch_size]
   (a.out/f'{bid}.json').write_text(json.dumps({'format':'multiversal-recovery-batch','version':'1.0.0','batchId':bid,'family':family,'candidateCount':len(chunk),'candidates':chunk},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
   batches.append({'batchId':bid,'family':family,'candidateCount':len(chunk),'readyCount':sum(x['readinessScore']>=76 for x in chunk)})
 summary={'format':'multiversal-canonical-recovery-index','version':'1.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'candidateCount':len(recovered),'familyCounts':dict(Counter(x['objectType'] for x in recovered)),'readyForDesignerReview':sum(x['readinessScore']>=76 for x in recovered),'needsStructure':sum(x['readinessScore']<76 for x in recovered),'relationshipCandidateCount':len(relations),'batchCount':len(batches),'batches':batches,'coverage':coverage,'publishedSample':recovered[:250],'relationshipSample':relations[:250],'authorityNote':'Recovery outputs are proposed structures only; they do not modify canon.'}
 (a.out/'recovery-index.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(json.dumps({k:summary[k] for k in ('candidateCount','familyCounts','readyForDesignerReview','relationshipCandidateCount','batchCount')},indent=2))
if __name__=='__main__': main()
