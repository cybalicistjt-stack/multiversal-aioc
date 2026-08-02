#!/usr/bin/env python3
"""Mine v4 candidates for regression tests and Golden Corpus seed examples.

Outputs diagnostics and review evidence only. It never modifies canon or certifies records.
"""
from __future__ import annotations
import argparse, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

STAT = re.compile(r"^(?:AC|HP|DR|EP|MP|SP|CR|DC|Speed|STR|DEX|CON|INT|WIS|CHA|Saving Throws?|Skills?)\s*[:=]", re.I)
CONTEXT = re.compile(r"\b(?:campaign use|investigation hooks|design notes|gm notes|frequency|weighted|table|chart|example|sample)\b", re.I)
FRAGMENT = re.compile(r"(?:[,;:]$|^\W|\b(?:and|or|of|to|with)$)", re.I)

def load(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]

def score(row: dict) -> int:
    r=row.get('recovery') or {}
    return int(r.get('identityConfidence',0)) + int(r.get('completenessScore',0)) + 3*int(r.get('familyMargin',0)) + 4*int(r.get('boundaryEvidenceCount',0))

def anomaly(row: dict) -> list[str]:
    name=str(row.get('name') or '').strip(); r=row.get('recovery') or {}; out=[]
    if STAT.search(name): out.append('stat-field-identity')
    if CONTEXT.search(name): out.append('contextual-or-table-heading')
    if FRAGMENT.search(name): out.append('fragment-name')
    if int(r.get('boundaryEvidenceCount',0)) <= 1: out.append('single-block-boundary')
    if int(r.get('completenessScore',0)) < 75: out.append('low-completeness')
    if int(r.get('familyMargin',0)) < 6: out.append('family-ambiguity')
    if any(rel.get('targetId') is None for rel in row.get('relationships') or []): out.append('unresolved-relationship')
    return out

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument('--candidates',type=Path,required=True); ap.add_argument('--out',type=Path,required=True); ap.add_argument('--per-family',type=int,default=12)
    a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
    rows=load(a.candidates/'canonical-candidates-v4.jsonl'); by=defaultdict(list)
    for row in rows: by[row.get('type','unknown')].append(row)
    positive=[]; negative=[]; anomaly_counts=Counter()
    for family,items in sorted(by.items()):
        ranked=sorted(items,key=lambda x:(-score(x),x.get('name','')))
        clean=[x for x in ranked if not anomaly(x)]
        risky=[x for x in ranked if anomaly(x)]
        for x in clean[:a.per_family]: positive.append({'label':'probable-positive','family':family,'candidate':x})
        for x in risky[:a.per_family]:
            reasons=anomaly(x); anomaly_counts.update(reasons)
            negative.append({'label':'boundary-challenge','family':family,'reasons':reasons,'candidate':x})
    tests=[]
    for row in negative:
        c=row['candidate']; tests.append({'candidateId':c.get('id'),'name':c.get('name'),'proposedType':c.get('type'),'expectedDisposition':'reject-or-correct','regressionReasons':row['reasons'],'source':(c.get('provenance') or [{}])[0]})
    packet={'format':'multiversal-regression-mining-v4','version':'4.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'candidateCount':len(rows),'familyCount':len(by),'probablePositiveCount':len(positive),'boundaryChallengeCount':len(negative),'anomalyCounts':dict(anomaly_counts),'probablePositives':positive,'boundaryChallenges':negative,'regressionTests':tests,'authority':'Diagnostic evidence only; no record is verified or canonical.'}
    (a.out/'regression-mining-v4.json').write_text(json.dumps(packet,indent=2,ensure_ascii=False)+'\n')
    index={k:packet[k] for k in ('format','version','generatedAt','candidateCount','familyCount','probablePositiveCount','boundaryChallengeCount','anomalyCounts','authority')}
    (a.out/'regression-mining-v4-index.json').write_text(json.dumps(index,indent=2)+'\n')
    print(json.dumps(index,indent=2))
if __name__=='__main__': main()
