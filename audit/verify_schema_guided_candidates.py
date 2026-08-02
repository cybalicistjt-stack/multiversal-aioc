#!/usr/bin/env python3
"""Independently verify schema-guided candidates and assign review routes."""
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

GENERIC={'actions','traits','effects','statistics','objectives','equipment','attacks','abilities','variants','prerequisites','origin','description','history','notes'}
SCALAR=re.compile(r"^(?:DC\s*\d+|\d+(?:\.\d+)?\s*(?:ft|feet|miles?|hours?|minutes?|rounds?|turns?|XP|MC)|\d+d\d+(?:\s*[+-]\s*\d+)?)$",re.I)
CLAUSE=re.compile(r"\b(?:may include|can be|allows? you to|adds? |provides? |used to|how to)\b",re.I)

def rows(path): return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]
def norm(s): return re.sub(r'[^a-z0-9]+',' ',str(s or '').lower()).strip()
def stable(*x): return hashlib.sha256('\n'.join(map(str,x)).encode()).hexdigest()[:20]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--candidates',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    data=rows(a.candidates/'schema-guided-candidates.jsonl'); seen=defaultdict(list); verified=[]
    for c in data:
        p=(c.get('provenance') or [{}])[0]; key=(c.get('objectType'),norm(c.get('name')),p.get('sourcePath'),p.get('pageStart'));seen[key].append(c['candidateId'])
    routes=Counter(); reasons=Counter(); family=Counter()
    for c in data:
        problems=[]; warnings=[]; name=str(c.get('name') or '').strip(); p=(c.get('provenance') or [{}])[0]; ev=(c.get('sourceEvidence') or [{}])[0]
        if not name or norm(name) in GENERIC: problems.append('generic-or-container-identity')
        if CLAUSE.search(name) or name[:1] in '+-=*/': problems.append('fragment-identity')
        if not p.get('sourcePath') or not p.get('locator'): problems.append('incomplete-provenance')
        if not str(ev.get('text') or '').strip(): problems.append('missing-source-evidence')
        if len(seen[(c.get('objectType'),norm(name),p.get('sourcePath'),p.get('pageStart'))])>1: problems.append('duplicate-source-identity')
        for rel in c.get('relationships') or []:
            if SCALAR.match(str(rel.get('targetName') or '')): problems.append('scalar-relationship-target')
        if c.get('familyMargin',0)<3: warnings.append('weak-family-margin')
        if c.get('confidence',0)<85: warnings.append('confidence-below-85')
        if len(str((c.get('specification') or {}).get('summary') or ''))<80: warnings.append('thin-evidence')
        schema_valid=all(k in c for k in ('candidateId','objectType','name','provenance','sourceEvidence','specification','confidence'))
        if not schema_valid: problems.append('schema-invalid')
        if problems: route='rejected-evidence-only'
        elif warnings: route='human-review'
        else: route='ready-for-expert-sample'
        routes[route]+=1;family[c.get('objectType')]+=1
        for x in problems+warnings: reasons[x]+=1
        verified.append({**c,'validation':{'verificationId':'verify-'+stable(c['candidateId'],route),'schemaValid':schema_valid,'problems':problems,'warnings':warnings,'verifiedAt':datetime.now(timezone.utc).isoformat(),'verifierMethod':'independent-deterministic-v1'},'reviewRoute':route})
    ready=[x for x in verified if x['reviewRoute']=='ready-for-expert-sample']; review=[x for x in verified if x['reviewRoute']=='human-review']; rejected=[x for x in verified if x['reviewRoute']=='rejected-evidence-only']
    summary={'format':'multiversal-schema-guided-verification-index','version':'1.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'candidateCount':len(verified),'routeCounts':dict(routes),'familyCounts':dict(family),'reasonCounts':dict(reasons),'schemaValidCount':sum(x['validation']['schemaValid'] for x in verified),'scalarRelationshipViolationCount':reasons['scalar-relationship-target'],'publishedReadySample':ready[:120],'publishedHumanReviewSample':review[:120],'publishedRejectedSample':rejected[:80],'authorityNote':'Verification routes do not authorize canonical ingestion.'}
    (a.out/'schema-guided-verification-index.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
    for filename,items in [('verified-ready.jsonl',ready),('verified-human-review.jsonl',review),('verified-rejected.jsonl',rejected)]:
        with (a.out/filename).open('w',encoding='utf-8') as f:
            for x in items:f.write(json.dumps(x,ensure_ascii=False)+'\n')
    print(json.dumps({'candidates':len(verified),'routes':summary['routeCounts'],'reasons':summary['reasonCounts']},indent=2))
if __name__=='__main__':main()
