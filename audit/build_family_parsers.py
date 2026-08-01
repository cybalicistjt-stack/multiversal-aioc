#!/usr/bin/env python3
"""Parse structural blocks into typed, non-canonical game-object candidates."""
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

FAMILIES=('ability','creature','item','species','npc','vehicle','environment','world','faction','adventure','rule')
HINTS={
'ability':('ability','power','spell','feat','technique','maneuver','ritual','perk'),
'creature':('creature','monster','beast','animal','undead','construct','dragon','demon'),
'item':('item','weapon','armor','artifact','relic','tool','potion','wand','ring'),
'species':('species','subspecies','ancestry','heritage','race'),
'npc':('npc','merchant','warden','soldier','medic','scout','engineer','trader'),
'vehicle':('vehicle','ship','starship','mecha','mount','drone','walker'),
'environment':('environment','terrain','hazard','weather','biome','underwater','desert','arctic'),
'world':('world','realm','dimension','region','city','location','setting'),
'faction':('faction','organization','guild','corporation','religion','empire','culture'),
'adventure':('adventure','quest','encounter','scene','objective','clue','investigation'),
'rule':('rule','check','save','action','reaction','round','turn','procedure')}
BAD_TITLE=re.compile(r"^(?:\d+[.)]?\s*)?(?:roll|result|description|effect|table|chapter|section|tier|level|notes?)$",re.I)
SENTENCE=re.compile(r"[.!?]$")
FIELD_PATTERNS={
'cost':re.compile(r"\bcost\s*[:=]\s*([^\n.;]+)",re.I),'range':re.compile(r"\brange\s*[:=]\s*([^\n.;]+)",re.I),'duration':re.compile(r"\bduration\s*[:=]\s*([^\n.;]+)",re.I),'activation':re.compile(r"\b(?:activation|action)\s*[:=]\s*([^\n.;]+)",re.I),'damage':re.compile(r"\bdamage\s*[:=]\s*([^\n.;]+)",re.I),'hp':re.compile(r"\bHP\s*[:=]\s*([^\n,;]+)",re.I),'ac':re.compile(r"\bAC\s*[:=]\s*([^\n,;]+)",re.I),'speed':re.compile(r"\bspeed\s*[:=]\s*([^\n,;]+)",re.I)}

def load_jsonl(p): return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
def clean(s): return re.sub(r"\s+"," ",str(s or '')).strip()
def stable(*p): return hashlib.sha256('\n'.join(p).encode('utf-8','ignore')).hexdigest()[:16]
def title(block):
    h=clean(block.get('heading'))
    if h and not BAD_TITLE.match(h) and len(h)<=90 and len(h.split())<=12:return re.sub(r"^\d+[.)]\s*",'',h)
    for line in str(block.get('text') or '').splitlines()[:8]:
        x=clean(line).strip('•*-: ')
        if 2<=len(x)<=90 and 1<=len(x.split())<=12 and not BAD_TITLE.match(x) and not SENTENCE.search(x):return re.sub(r"^\d+[.)]\s*",'',x)
    return ''
def family(block,name):
    text=(name+' '+clean(block.get('text'))[:1200]).lower(); scores={f:sum(text.count(h) for h in hs)+(block.get('familyScores') or {}).get(f,0)*2 for f,hs in HINTS.items()}
    best=max(scores,key=scores.get); return best if scores[best]>0 else None
def extract_fields(f,text):
    common={'summary':clean(text)[:900],'mechanicSignals':re.findall(r"\b(?:\d+d\d+(?:\s*[+\-]\s*\d+)?|DC\s*\d+|once per [^,.;]+|\d+\s*(?:feet|ft|rounds?|turns?|hours?))\b",text,re.I)[:30]}
    for k,p in FIELD_PATTERNS.items():
        m=p.search(text)
        if m:common[k]=clean(m.group(1))
    templates={'ability':{'prerequisites':[],'effects':[],'scaling':[]},'creature':{'attacks':[],'traits':[],'ecology':None,'variants':[]},'item':{'itemCategory':None,'weight':None,'properties':[],'crafting':None},'species':{'appearance':None,'culture':None,'traits':[],'adaptations':[],'progression':[]},'npc':{'role':None,'speciesId':None,'affiliations':[],'abilities':[]},'vehicle':{'vehicleClass':None,'crew':None,'components':[],'upgrades':[]},'environment':{'hazards':[],'weather':[],'adaptations':[],'travelRules':[]},'world':{'locations':[],'cultures':[],'factions':[],'rules':[]},'faction':{'goals':[],'members':[],'relationships':[]},'adventure':{'scenes':[],'encounters':[],'clues':[],'objectives':[]},'rule':{'procedure':[],'exceptions':[],'optional':bool(re.search(r'\boptional\b',text,re.I))}}
    return {**common,**templates[f]}
def relationships(name,text):
    pats={'requires':r"\b(?:requires?|prerequisite)\s*[:\-]?\s*([A-Z][A-Za-z0-9 &'’\-]{2,50})",'belongsTo':r"\b(?:tree|school|discipline|style|category)\s*[:\-]?\s*([A-Z][A-Za-z0-9 &'’\-]{2,50})",'locatedIn':r"\b(?:found in|located in|native to|from)\s+([A-Z][A-Za-z0-9 &'’\-]{2,50})",'usedBy':r"\b(?:used by|available to)\s+([A-Z][A-Za-z0-9 &'’\-]{2,50})"}
    out=[]
    for typ,pat in pats.items():
        for m in re.finditer(pat,text):
            target=clean(m.group(1)).rstrip('.,;:')
            if target and target.lower()!=name.lower() and len(target.split())<=8:out.append({'type':typ,'targetName':target,'confidence':65})
    return out[:20]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--structure',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    blocks=load_jsonl(a.structure/'structural-blocks.jsonl'); candidates=[]; rejected=Counter()
    for b in blocks:
        name=title(b)
        if not name: rejected['no-usable-title']+=1;continue
        f=family(b,name)
        if not f: rejected['no-family']+=1;continue
        if b.get('blockType')=='table' and f in ('species','world') and re.search(r"\(1d\d+\)|\broll\b",name,re.I): rejected['table-label']+=1;continue
        spec=extract_fields(f,b.get('text') or ''); missing=[k for k,v in spec.items() if v in (None,[],{}) and k not in ('mechanicSignals',)]
        cid=f"structured.{f}.{re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-')}.{stable(b['blockId'],name)}"
        candidates.append({'candidateId':cid,'objectType':f,'name':name,'sourceBlockId':b['blockId'],'sourceBlockType':b['blockType'],'provenance':[{'sourcePath':b['sourcePath'],'locator':b['locator'],'page':b['page'],'findingId':b['findingId']}],'spec':spec,'relationships':relationships(name,b.get('text') or ''),'missingFields':missing,'readinessScore':max(0,100-len(missing)*7),'status':'structured-candidate','authority':'Non-canonical until reviewed and approved.'})
    candidates.sort(key=lambda x:(x['objectType'],-x['readinessScore'],x['name'].lower()))
    with (a.out/'family-parser-candidates.jsonl').open('w',encoding='utf-8') as f:
        for x in candidates:f.write(json.dumps(x,ensure_ascii=False)+'\n')
    summary={'format':'multiversal-family-parser-index','version':'1.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'candidateCount':len(candidates),'familyCounts':dict(Counter(x['objectType'] for x in candidates)),'readyCount':sum(x['readinessScore']>=76 for x in candidates),'relationshipCount':sum(len(x['relationships']) for x in candidates),'rejectedCounts':dict(rejected),'publishedSample':candidates[:300],'authorityNote':'Parser candidates do not modify canon.'}
    (a.out/'family-parser-index.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');print(json.dumps({k:summary[k] for k in ('candidateCount','familyCounts','readyCount','relationshipCount')},indent=2))
if __name__=='__main__':main()
