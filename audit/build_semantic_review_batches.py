#!/usr/bin/env python3
"""Build balanced, provenance-backed semantic review batches.

Consumes family parser candidates and knowledge graph metrics. Rejects obvious
headings, table labels, prose fragments, and weak provenance before human review.
Outputs remain non-canonical.
"""
from __future__ import annotations
import argparse, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

FAMILIES=("ability","creature","item","species","npc","vehicle","environment","world","faction","adventure","rule")
GENERIC=re.compile(r"^(?:introduction|overview|description|background|history|notes?|table|results?|effects?|chapter|section|tier|level|attributes?|statistics?)$",re.I)
NUMBERED=re.compile(r"^\s*\d+[.)]\s+")
ROLLISH=re.compile(r"\b(?:1d\d+|d100|roll|result|random table)\b",re.I)
SENTENCE_END=re.compile(r"[.!?]$")

def load_jsonl(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def usable_provenance(row):
    for p in row.get("provenance") or []:
        if str(p.get("sourcePath") or "").strip() and (p.get("locator") or p.get("page") or p.get("findingId")):
            return True
    return False

def good_name(name):
    n=" ".join(str(name or "").split()).strip()
    if not (2 <= len(n) <= 90) or GENERIC.match(n): return False
    if NUMBERED.match(n) or SENTENCE_END.search(n): return False
    if len(n.split()) > 12: return False
    if n[:1].islower(): return False
    if ROLLISH.search(n) and any(x in n.lower() for x in ("table","effects","results","encounter")): return False
    return True

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--parsed",type=Path,required=True);ap.add_argument("--graph",type=Path,required=True);ap.add_argument("--out",type=Path,required=True);ap.add_argument("--limit",type=int,default=220);ap.add_argument("--batch-size",type=int,default=50);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    rows=load_jsonl(a.parsed/"family-parser-candidates.jsonl")
    graph=json.loads((a.graph/"canonical-knowledge-graph.json").read_text(encoding="utf-8"))
    degree=Counter()
    for e in graph.get("edges",[]):
        degree[e.get("source")]+=1; degree[e.get("target")]+=1
    accepted=[]; rejected=Counter(); by_family=defaultdict(list)
    for r in rows:
        if not usable_provenance(r): rejected["missing-provenance"]+=1; continue
        if not good_name(r.get("name")): rejected["bad-name"]+=1; continue
        typ=r.get("objectType")
        if typ not in FAMILIES: rejected["unsupported-family"]+=1; continue
        missing=len(r.get("missingFields") or [])
        rels=len(r.get("relationships") or [])
        evidence_bonus=8
        connectivity=min(12,degree.get(r.get("candidateId"),0)*3)
        score=max(0,min(100,float(r.get("readinessScore") or 0)+evidence_bonus+connectivity-missing*2-rels))
        row={**r,"semanticQualityScore":round(score,2),"graphDegree":degree.get(r.get("candidateId"),0),"reviewState":"unreviewed","reviewChecks":["distinct canonical identity","correct family parser","source text preserves mechanics","relationships resolve to canonical IDs","pack placement confirmed"],"authority":"Semantic review candidate only; no canonical write is authorized."}
        by_family[typ].append(row)
    for typ in by_family: by_family[typ].sort(key=lambda x:(-x["semanticQualityScore"],x["name"].lower()))
    active=[f for f in FAMILIES if by_family[f]]
    quota=max(1,a.limit//max(1,len(active)))
    for f in active: accepted.extend(by_family[f][:quota])
    leftovers=[x for f in active for x in by_family[f][quota:]]
    leftovers.sort(key=lambda x:(-x["semanticQualityScore"],x["objectType"],x["name"].lower()))
    accepted.extend(leftovers[:max(0,a.limit-len(accepted))]);accepted=accepted[:a.limit]
    accepted.sort(key=lambda x:(x["objectType"],-x["semanticQualityScore"],x["name"].lower()))
    batches=[]
    for i in range(0,len(accepted),a.batch_size):
        chunk=accepted[i:i+a.batch_size];bid=f"semantic-review-{i//a.batch_size+1:03d}"
        payload={"format":"multiversal-semantic-review-batch","version":"1.0.0","batchId":bid,"candidateCount":len(chunk),"familyCounts":dict(Counter(x["objectType"] for x in chunk)),"candidates":chunk}
        (a.out/f"{bid}.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        batches.append({"batchId":bid,"candidateCount":len(chunk),"familyCounts":payload["familyCounts"]})
    summary={"format":"multiversal-semantic-review-index","version":"1.0.0","generatedAt":datetime.now(timezone.utc).isoformat(),"candidateCount":len(accepted),"familyCounts":dict(Counter(x["objectType"] for x in accepted)),"batchCount":len(batches),"batches":batches,"rejectedCounts":dict(rejected),"averageQualityScore":round(sum(x["semanticQualityScore"] for x in accepted)/max(1,len(accepted)),2),"publishedSample":accepted[:220],"authorityNote":"Semantic review batches are non-canonical and require human approval."}
    (a.out/"semantic-review-index.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({k:summary[k] for k in ("candidateCount","familyCounts","batchCount","rejectedCounts","averageQualityScore")},indent=2))
if __name__=="__main__":main()
