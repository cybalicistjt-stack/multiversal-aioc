#!/usr/bin/env python3
"""Build document-qualified structural blocks from forensic findings.

Recognizes headings, prose, numbered lists, tables, stat blocks, and mechanic blocks.
Outputs are evidence structures only and never modify canon.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HEADING=re.compile(r"^(?:chapter\s+\d+|section\s+\d+|[A-Z][A-Z0-9 &'’:\-]{3,}|(?:\d+\.)?\s*[A-Z][^.!?]{2,70})$")
LIST=re.compile(r"^\s*(?:[-•*]|\d+[.)]|[A-Z][.)])\s+")
STAT=re.compile(r"\b(?:HP|AC|DR|EP|MP|SP|Speed|Attack|Damage|Range|Duration|Cost|Level|Tier)\s*[:=]",re.I)
MECH=re.compile(r"\b(?:\d+d\d+|DC\s*\d+|once per|bonus action|reaction|rounds?|turns?|feet|miles?)\b",re.I)
TABLE_SEP=re.compile(r"\s{2,}|\t|\s*\|\s*")

def load_jsonl(path):
    if not path.exists(): return []
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]
def stable(*parts): return hashlib.sha256('\n'.join(parts).encode('utf-8','ignore')).hexdigest()[:20]
def page_of(locator):
    m=re.search(r"page:(\d+)",str(locator or '')); return int(m.group(1)) if m else None
def clean(s): return re.sub(r"\s+"," ",str(s or '')).strip()
def classify(lines,text):
    non=[x for x in lines if clean(x)]
    list_ratio=sum(bool(LIST.match(x)) for x in non)/max(1,len(non))
    table_ratio=sum((x.count(',')>=2 or x.count('|')>=2 or len(re.split(r'\s{2,}',x.strip()))>=3) for x in non)/max(1,len(non))
    if table_ratio>=.45: return 'table'
    if STAT.search(text) and sum(1 for x in non if STAT.search(x))>=2: return 'stat-block'
    if list_ratio>=.45: return 'list'
    if MECH.search(text): return 'mechanic-block'
    return 'prose'
def split_blocks(text):
    lines=text.splitlines(); out=[]; current=[]; heading=None
    def flush():
        nonlocal current
        body='\n'.join(current).strip()
        if body: out.append((heading,body))
        current=[]
    for raw in lines:
        line=raw.strip()
        if not line:
            if current and len('\n'.join(current))>300: flush()
            continue
        if HEADING.match(line) and len(line)<=100 and len(line.split())<=14:
            flush(); heading=line.strip(' :-')
        else: current.append(raw)
    flush(); return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',type=Path,required=True); ap.add_argument('--out',type=Path,required=True); a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
    rows=load_jsonl(a.input/'findings.jsonl')+load_jsonl(a.input/'csv-findings.jsonl')
    grouped=defaultdict(list)
    for r in rows: grouped[(r.get('source_path') or 'unknown',page_of(r.get('locator')))].append(r)
    blocks=[]
    for (source,page),items in sorted(grouped.items(),key=lambda x:(x[0][0],x[0][1] or 0)):
        for item in items:
            for idx,(heading,body) in enumerate(split_blocks(item.get('text') or '')):
                lines=body.splitlines(); kind=classify(lines,body)
                bid='struct-'+stable(source,str(page),item.get('finding_id',''),str(idx),body[:300])
                blocks.append({'blockId':bid,'sourcePath':source,'page':page,'locator':item.get('locator'),'findingId':item.get('finding_id'),'heading':heading,'blockType':kind,'text':body,'lineCount':len(lines),'mechanicSignals':item.get('mechanic_signals') or [],'familyScores':item.get('family_scores') or {},'tableShape':item.get('table_shape'),'provenanceComplete':bool(source and source!='unknown' and item.get('locator'))})
    by_source=Counter(x['sourcePath'] for x in blocks); by_type=Counter(x['blockType'] for x in blocks)
    summary={'format':'multiversal-document-structure-index','version':'1.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'sourceCount':len(by_source),'blockCount':len(blocks),'blockTypeCounts':dict(by_type),'provenanceCompleteCount':sum(x['provenanceComplete'] for x in blocks),'publishedSample':blocks[:250],'authorityNote':'Structural blocks are source evidence, not canonical objects.'}
    (a.out/'document-structure-index.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    with (a.out/'structural-blocks.jsonl').open('w',encoding='utf-8') as f:
        for x in blocks:f.write(json.dumps(x,ensure_ascii=False)+'\n')
    print(json.dumps({k:summary[k] for k in ('sourceCount','blockCount','blockTypeCounts')},indent=2))
if __name__=='__main__': main()
