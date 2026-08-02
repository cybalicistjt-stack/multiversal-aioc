#!/usr/bin/env python3
"""Reconstruct tables and key-value structures from hierarchical nodes.

Deterministic, provenance-preserving, and intentionally conservative.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

KV=re.compile(r"^\s*([^:]{2,60})\s*:\s*(.+?)\s*$")
SEP=re.compile(r"\s{2,}|\t|\s*\|\s*")
SCALAR=re.compile(r"^(?:DC\s*\d+|\d+(?:\.\d+)?\s*(?:ft|feet|miles?|hours?|minutes?|rounds?|turns?|XP|MC)|\d+d\d+(?:\s*[+-]\s*\d+)?)$",re.I)

def load(path):
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]
def stable(*x): return hashlib.sha256('\n'.join(map(str,x)).encode()).hexdigest()[:20]
def cells(line):
    parts=[p.strip() for p in SEP.split(line.strip()) if p.strip()]
    return parts if len(parts)>=2 else []
def likely_header(row, following):
    if not row or not following:return False
    alpha=sum(any(ch.isalpha() for ch in c) for c in row)
    numeric=sum(bool(re.search(r'\d',c)) for c in row)
    return alpha>=max(1,len(row)-1) and numeric<=1 and len(row)==len(following)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--structure',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    nodes=load(a.structure/'hierarchical-nodes.jsonl')
    tables=[]; kvs=[]; rejected=Counter()
    for n in nodes:
        lines=[x.strip() for x in str(n.get('text') or '').splitlines() if x.strip()]
        rowset=[cells(x) for x in lines]; rowset=[x for x in rowset if x]
        is_table=n.get('sectionRole')=='table' or n.get('blockType')=='table' or (len(rowset)>=2 and Counter(map(len,rowset)).most_common(1)[0][1]>=2)
        if is_table and rowset:
            width=Counter(map(len,rowset)).most_common(1)[0][0]
            normalized=[r for r in rowset if len(r)==width]
            if len(normalized)>=2:
                header=normalized[0] if likely_header(normalized[0],normalized[1]) else []
                body=normalized[1:] if header else normalized
                tables.append({'tableId':'table-'+stable(n['nodeId'],n.get('contentHash')),'nodeId':n['nodeId'],'sourceRelativePath':n.get('sourceRelativePath'),'pageStart':n.get('pageStart'),'pageEnd':n.get('pageEnd'),'locator':n.get('locator'),'headingPath':n.get('headingPath') or [],'parentObjectTitle':n.get('parentObjectTitle'),'caption':n.get('title'),'columnCount':width,'headers':header,'rows':[{'rowIndex':i,'cells':[{'columnIndex':j,'text':v,'isScalar':bool(SCALAR.match(v))} for j,v in enumerate(r)]} for i,r in enumerate(body)],'confidence':90 if header else 75,'authority':'Reconstructed evidence only.'})
            else: rejected['irregular-table']+=1
        for line in lines:
            m=KV.match(line)
            if not m: continue
            key,value=m.groups()
            if len(key.split())>10 or len(value)>500:continue
            kvs.append({'pairId':'kv-'+stable(n['nodeId'],key,value),'nodeId':n['nodeId'],'key':key.strip(),'value':value.strip(),'valueIsScalar':bool(SCALAR.match(value.strip())),'sourceRelativePath':n.get('sourceRelativePath'),'page':n.get('pageStart'),'locator':n.get('locator'),'headingPath':n.get('headingPath') or [],'parentObjectTitle':n.get('parentObjectTitle'),'confidence':85,'authority':'Reconstructed evidence only.'})
    summary={'format':'multiversal-table-form-reconstruction-index','version':'1.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'tableCount':len(tables),'keyValuePairCount':len(kvs),'tablesWithHeaders':sum(bool(x['headers']) for x in tables),'scalarValueCount':sum(x['valueIsScalar'] for x in kvs),'rejectedCounts':dict(rejected),'publishedTableSample':tables[:100],'publishedKeyValueSample':kvs[:150]}
    (a.out/'table-form-reconstruction-index.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
    for name,rows in [('reconstructed-tables.jsonl',tables),('reconstructed-key-values.jsonl',kvs)]:
        with (a.out/name).open('w',encoding='utf-8') as f:
            for x in rows:f.write(json.dumps(x,ensure_ascii=False)+'\n')
    print(json.dumps({k:summary[k] for k in ('tableCount','keyValuePairCount','tablesWithHeaders','scalarValueCount')},indent=2))
if __name__=='__main__':main()
