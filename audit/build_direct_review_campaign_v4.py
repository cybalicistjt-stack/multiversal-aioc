#!/usr/bin/env python3
"""Build direct semantic-review packets from Semantic Recovery v4 candidates.

Outputs review evidence only. It never modifies or certifies canonical content.
"""
from __future__ import annotations
import argparse, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

NON_RULE_ORDER = ['creature','npc','item','species','vehicle','world','environment','faction','adventure','ability']

def load(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]

def norm(s: object) -> str:
    return re.sub(r'[^a-z0-9]+',' ',str(s or '').lower()).strip()

def pattern_key(row: dict) -> str:
    name=str(row.get('name') or '')
    name=re.sub(r'\d+','<n>',name)
    name=re.sub(r'\([^)]*\)','(<detail>)',name)
    words=norm(name).split()
    return ' '.join(words[:5]) or 'unnamed'

def review_record(row: dict) -> dict:
    r=row.get('recovery') or {}
    p=(row.get('provenance') or [{}])[0]
    return {
        'candidateId':row.get('id'),'proposedType':row.get('type'),'proposedName':row.get('name'),
        'summary':(row.get('specification') or {}).get('summary'),'sections':(row.get('specification') or {}).get('sections'),
        'relationships':row.get('relationships') or [],'source':p,'reviewRoute':row.get('reviewRoute'),
        'identityConfidence':r.get('identityConfidence'),'completenessScore':r.get('completenessScore'),
        'familyMargin':r.get('familyMargin'),'boundaryEvidenceCount':r.get('boundaryEvidenceCount'),
        'decision':{'disposition':'pending','correctType':None,'correctName':None,'boundaryAction':None,'notes':''}
    }

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument('--candidates',type=Path,required=True); ap.add_argument('--out',type=Path,required=True); ap.add_argument('--batch-size',type=int,default=30)
    a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
    rows=load(a.candidates/'canonical-candidates-v4.jsonl')
    by=defaultdict(list)
    for row in rows: by[row.get('type','unknown')].append(row)
    manifest={'format':'multiversal-direct-review-campaign-v4','version':'1.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'candidateCount':len(rows),'familyCounts':dict(Counter(r.get('type') for r in rows)),'packets':[],'authority':'Review evidence only; no decision changes canon.'}
    # Complete non-rule family packets.
    for family in NON_RULE_ORDER:
        items=sorted(by.get(family,[]),key=lambda x:(str((x.get('provenance') or [{}])[0].get('sourcePath','')),str(x.get('name',''))))
        for i in range(0,len(items),a.batch_size):
            batch=items[i:i+a.batch_size]; name=f'{family}-batch-{i//a.batch_size+1:02d}.json'
            payload={'family':family,'batch':i//a.batch_size+1,'recordCount':len(batch),'records':[review_record(x) for x in batch]}
            (a.out/name).write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
            manifest['packets'].append({'file':name,'family':family,'count':len(batch),'mode':'complete-family-review'})
    # Rules grouped by source and normalized title pattern.
    clusters=defaultdict(list)
    for row in by.get('rule',[]):
        source=str((row.get('provenance') or [{}])[0].get('sourcePath') or 'unknown')
        clusters[(source,pattern_key(row))].append(row)
    cluster_rows=[]
    for (source,pattern),items in sorted(clusters.items(),key=lambda kv:(kv[0][0],kv[0][1])):
        cluster_rows.append({'sourcePath':source,'pattern':pattern,'count':len(items),'representatives':[review_record(x) for x in items[:5]],'allCandidateIds':[x.get('id') for x in items]})
    for i in range(0,len(cluster_rows),a.batch_size):
        batch=cluster_rows[i:i+a.batch_size]; name=f'rule-clusters-{i//a.batch_size+1:02d}.json'
        (a.out/name).write_text(json.dumps({'batch':i//a.batch_size+1,'clusterCount':len(batch),'clusters':batch},indent=2,ensure_ascii=False)+'\n')
        manifest['packets'].append({'file':name,'family':'rule','count':len(batch),'mode':'cluster-review'})
    (a.out/'direct-review-campaign-index.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'candidateCount':len(rows),'packetCount':len(manifest['packets']),'familyCounts':manifest['familyCounts']},indent=2))
if __name__=='__main__': main()
