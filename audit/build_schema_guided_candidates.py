#!/usr/bin/env python3
"""Build schema-guided candidates from hierarchical evidence.

This deterministic stage is the reproducible foundation for optional NLP/LLM adapters.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

FAMILIES=('rule','ability','creature','item','species','npc','vehicle','environment','world','faction','adventure')
CONTAINERS={'actions','traits','effects','statistics','objectives','equipment','attacks','abilities','variants','prerequisites','origin','description','history','notes'}
SCALAR=re.compile(r"^(?:DC\s*\d+|\d+(?:\.\d+)?\s*(?:ft|feet|miles?|hours?|minutes?|rounds?|turns?|XP|MC)|\d+d\d+(?:\s*[+-]\s*\d+)?)$",re.I)
SIGNALS={
'rule':r'\b(?:rule|check|save|must|may|DC\s*\d+|procedure|round|turn)\b','ability':r'\b(?:ability|spell|power|activation|duration|range|cost|prerequisite)\b','creature':r'\b(?:creature|HP|AC|attack|damage|habitat|multiattack)\b','item':r'\b(?:item|weapon|armor|equipment|cost|weight|artifact|component)\b','species':r'\b(?:species|ancestry|heritage|appearance|culture|adaptation|racial)\b','npc':r'\b(?:NPC|merchant|role|affiliation|personality)\b','vehicle':r'\b(?:vehicle|ship|crew|frame|engine|speed|upgrade)\b','environment':r'\b(?:environment|terrain|hazard|weather|climate|biome)\b','world':r'\b(?:world|realm|dimension|region|city|setting|history)\b','faction':r'\b(?:faction|organization|guild|members|goals|allies|enemies)\b','adventure':r'\b(?:adventure|quest|encounter|scene|objective|clue|hook)\b'}
SIGNALS={k:re.compile(v,re.I) for k,v in SIGNALS.items()}

def rows(path): return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]
def stable(*x): return hashlib.sha256('\n'.join(map(str,x)).encode()).hexdigest()[:20]
def clean_title(x): return re.sub(r'^\s*[\W_]+|\s+',' ',str(x or '')).strip(' :-')
def family_scores(n):
    text=' '.join([str(n.get('title') or ''),str(n.get('text') or ''),str(n.get('sourceRelativePath') or '')])
    base={k:int((n.get('familyScores') or {}).get(k,0)) for k in FAMILIES}
    for k,p in SIGNALS.items(): base[k]+=min(8,len(p.findall(text))*2)
    return base

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--structure',type=Path,required=True);ap.add_argument('--tables',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    nodes=rows(a.structure/'hierarchical-nodes.jsonl'); kv=rows(a.tables/'reconstructed-key-values.jsonl'); bynode={}
    for x in kv: bynode.setdefault(x['nodeId'],[]).append(x)
    out=[]; rejected=Counter()
    for n in nodes:
        title=clean_title(n.get('title'))
        if not n.get('provenanceComplete'): rejected['missing-provenance']+=1;continue
        if n.get('sectionRole') in ('container','table') or title.lower() in CONTAINERS: rejected['container-or-table']+=1;continue
        if not n.get('identityEligible') or len(title)<3 or not str(n.get('text') or '').strip(): rejected['not-identity-evidence']+=1;continue
        scores=family_scores(n); ranked=sorted(scores.items(),key=lambda x:(-x[1],x[0])); family,top=ranked[0]; margin=top-ranked[1][1]
        if top<5 or margin<2: rejected['family-ambiguous']+=1;continue
        fields={x['key']:x['value'] for x in bynode.get(n['nodeId'],[]) if not x['valueIsScalar'] or x['key'].lower() not in ('requires','belongs to','used by','located in')}
        rel=[]
        for key,value in fields.items():
            if key.lower() in ('requires','prerequisite','belongs to','used by','located in') and not SCALAR.match(value): rel.append({'type':key.lower().replace(' ','-'),'targetName':value,'evidenceNodeId':n['nodeId']})
        confidence=min(99,55+top*3+margin*2+(8 if n.get('sectionRole')=='object-section' else 0))
        out.append({'candidateId':'schema-'+family+'-'+stable(n['nodeId'],title),'objectType':family,'name':title,'status':'schema-guided-candidate','authority':'Non-canonical; independent verification required.','provenance':[{'sourcePath':n.get('sourceRelativePath'),'pageStart':n.get('pageStart'),'pageEnd':n.get('pageEnd'),'locator':n.get('locator'),'findingId':n.get('findingId')}],'parentContext':{'parentId':n.get('parentId'),'parentObjectTitle':n.get('parentObjectTitle'),'headingPath':n.get('headingPath') or []},'sourceEvidence':[{'nodeId':n['nodeId'],'text':n.get('text'),'contentHash':n.get('contentHash')}],'extractionMethod':['hierarchical-deterministic','regex','key-value-reconstruction'],'confidence':confidence,'fieldConfidence':{k:85 for k in fields},'specification':{'summary':n.get('text'),'fields':fields,'mechanicSignals':n.get('mechanicSignals') or []},'relationships':rel,'familyScores':scores,'familyMargin':margin,'reviewRoute':'verification-required'})
    summary={'format':'multiversal-schema-guided-candidate-index','version':'1.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'candidateCount':len(out),'familyCounts':dict(Counter(x['objectType'] for x in out)),'rejectedCounts':dict(rejected),'publishedSample':out[:200],'probabilisticAdapterContract':{'input':['targetSchema','evidenceBlocks','parentContext'],'output':['schemaFields','evidenceSpans','fieldConfidence','uncertainties'],'rule':'Unsupported fields must be null; no canonical write.'}}
    (a.out/'schema-guided-candidate-index.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
    with (a.out/'schema-guided-candidates.jsonl').open('w',encoding='utf-8') as f:
        for x in out:f.write(json.dumps(x,ensure_ascii=False)+'\n')
    print(json.dumps({'candidates':len(out),'families':summary['familyCounts'],'rejected':summary['rejectedCounts']},indent=2))
if __name__=='__main__':main()
