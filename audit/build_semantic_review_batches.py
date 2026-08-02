#!/usr/bin/env python3
"""Build balanced, provenance-backed semantic review batches.

Consumes family parser candidates and knowledge graph metrics. Rejects headings,
tables, prose fragments, family/path mismatches, and structurally weak records
before human review. Outputs remain non-canonical.
"""
from __future__ import annotations
import argparse, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

FAMILIES=("ability","creature","item","species","npc","vehicle","environment","world","faction","adventure","rule")
GENERIC=re.compile(r"^(?:introduction|overview|description|background|history|notes?|table|results?|effects?|chapter|section|tier|level|attributes?|statistics?|contents?|appendix|examples?|summary|conclusion)$",re.I)
NUMBERED=re.compile(r"^\s*\d+(?:\.\d+)*[.)]?\s+")
NUMERIC_NOISE=re.compile(r"^(?:\d+\s*){2,}|\bXP\d|\d+(?:st|nd|rd|th)\s+\d",re.I)
ROLLISH=re.compile(r"\b(?:1d\d+|d100|roll|result|random table)\b",re.I)
SECTIONISH=re.compile(r"\b(?:how to|types? (?:and|&) traits?|choosing|limits? by|production rate|starting facilities|reference tables?|modules?|components?|categories|guidelines?|procedures?)\b",re.I)
SENTENCE_END=re.compile(r"[.!?]$")
OBJECT_SIGNAL={
 "ability":re.compile(r"\b(?:ability|power|spell|feat|technique|maneuver|ritual|perk|once per|activation|duration|range|cost)\b",re.I),
 "creature":re.compile(r"\b(?:creature|monster|beast|aberration|construct|undead|dragon|demon|HP|AC|attack|damage|habitat)\b",re.I),
 "item":re.compile(r"\b(?:item|weapon|armor|artifact|relic|tool|potion|cost|weight|equipment|component)\b",re.I),
 "species":re.compile(r"\b(?:species|subspecies|ancestry|heritage|racial|culture|appearance|adaptation|trait)\b",re.I),
 "npc":re.compile(r"\b(?:NPC|merchant|warden|soldier|medic|scout|engineer|trader|role|affiliation)\b",re.I),
 "vehicle":re.compile(r"\b(?:vehicle|ship|starship|mecha|mount|drone|walker|crew|frame|engine|speed)\b",re.I),
 "environment":re.compile(r"\b(?:environment|terrain|hazard|weather|biome|travel|climate|zone)\b",re.I),
 "world":re.compile(r"\b(?:world|realm|dimension|region|city|location|setting|culture|history)\b",re.I),
 "faction":re.compile(r"\b(?:faction|organization|guild|corporation|religion|empire|members?|goals?|allies|enemies)\b",re.I),
 "adventure":re.compile(r"\b(?:adventure|quest|encounter|scene|objective|clue|investigation|hook)\b",re.I),
 "rule":re.compile(r"\b(?:rule|check|save|action|reaction|round|turn|procedure|DC\s*\d+|must|may)\b",re.I),
}
PATH_HINTS={
 "ability":("ability","abilities","magic","spells","powers","feats"),
 "creature":("creature","creatures","monster","bestiary","aberration"),
 "item":("item","items","equipment","weapons","armor","computers"),
 "species":("species","ancestry","heritage","races"),
 "npc":("npc","npcs","characters"),
 "vehicle":("vehicle","vehicles","ships","racing"),
 "environment":("environment","environments","terrain","hazards"),
 "world":("world","worlds","setting","lore","locations"),
 "faction":("faction","factions","organizations","guilds"),
 "adventure":("adventure","adventures","quests","modules"),
 "rule":("rules","system","creation","combat","downtime"),
}

def load_jsonl(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def provenance(row):
    return (row.get("provenance") or [{}])[0]

def usable_provenance(row):
    p=provenance(row)
    return bool(str(p.get("sourcePath") or "").strip() and (p.get("locator") or p.get("page") or p.get("findingId")))

def normalized_name(name):
    n=" ".join(str(name or "").split()).strip()
    return NUMBERED.sub("",n).strip(" -:•")

def good_name(name):
    n=normalized_name(name)
    if not (3 <= len(n) <= 78) or GENERIC.match(n): return False
    if SENTENCE_END.search(n) or NUMERIC_NOISE.search(n): return False
    if len(n.split()) > 9 or n[:1] in "+-=*/": return False
    if n[:1].islower() or SECTIONISH.search(n): return False
    if ROLLISH.search(n): return False
    if sum(ch.isalpha() for ch in n) < max(3,len(n)//3): return False
    return True

def family_consistent(row):
    typ=row.get("objectType")
    text=(str(row.get("name") or "")+" "+str((row.get("spec") or {}).get("summary") or ""))[:1400]
    if not OBJECT_SIGNAL[typ].search(text): return False
    path=str(provenance(row).get("sourcePath") or "").lower().replace("\\","/")
    hints=PATH_HINTS.get(typ,())
    positive=any(h in path for h in hints)
    conflicting=[]
    for other,other_hints in PATH_HINTS.items():
        if other!=typ and any(h in path for h in other_hints): conflicting.append(other)
    return positive or not conflicting

def substantive(row):
    spec=row.get("spec") or {}
    summary=str(spec.get("summary") or "")
    if len(summary) < 80: return False
    if row.get("sourceBlockType")=="table" and not (spec.get("mechanicSignals") or []): return False
    alpha_words=re.findall(r"[A-Za-z]{3,}",summary)
    return len(alpha_words)>=12

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--parsed",type=Path,required=True);ap.add_argument("--graph",type=Path,required=True);ap.add_argument("--out",type=Path,required=True);ap.add_argument("--limit",type=int,default=220);ap.add_argument("--batch-size",type=int,default=50);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    rows=load_jsonl(a.parsed/"family-parser-candidates.jsonl")
    graph=json.loads((a.graph/"canonical-knowledge-graph.json").read_text(encoding="utf-8"))
    degree=Counter()
    for e in graph.get("edges",[]):
        if e.get("type")!="supportedBy":
            degree[e.get("source")]+=1;degree[e.get("target")]+=1
    accepted=[];rejected=Counter();by_family=defaultdict(list)
    for r in rows:
        if not usable_provenance(r): rejected["missing-provenance"]+=1;continue
        if not good_name(r.get("name")): rejected["bad-name"]+=1;continue
        typ=r.get("objectType")
        if typ not in FAMILIES: rejected["unsupported-family"]+=1;continue
        if not family_consistent(r): rejected["family-mismatch"]+=1;continue
        if not substantive(r): rejected["non-substantive"]+=1;continue
        missing=len(r.get("missingFields") or []);rels=len(r.get("relationships") or [])
        connectivity=min(10,degree.get(r.get("candidateId"),0)*4)
        score=max(0,min(100,float(r.get("readinessScore") or 0)+8+connectivity-missing*3-rels*2))
        if score<68: rejected["quality-below-68"]+=1;continue
        row={**r,"name":normalized_name(r.get("name")),"semanticQualityScore":round(score,2),"graphDegree":degree.get(r.get("candidateId"),0),"reviewState":"unreviewed","reviewChecks":["distinct canonical identity","correct family parser","source text preserves mechanics","relationships resolve to canonical IDs","pack placement confirmed"],"authority":"Semantic review candidate only; no canonical write is authorized."}
        by_family[typ].append(row)
    for typ in by_family:by_family[typ].sort(key=lambda x:(-x["semanticQualityScore"],-x["graphDegree"],x["name"].lower()))
    active=[f for f in FAMILIES if by_family[f]];quota=max(1,a.limit//max(1,len(active)))
    for f in active:accepted.extend(by_family[f][:quota])
    leftovers=[x for f in active for x in by_family[f][quota:]];leftovers.sort(key=lambda x:(-x["semanticQualityScore"],-x["graphDegree"],x["objectType"],x["name"].lower()))
    accepted.extend(leftovers[:max(0,a.limit-len(accepted))]);accepted=accepted[:a.limit];accepted.sort(key=lambda x:(x["objectType"],-x["semanticQualityScore"],x["name"].lower()))
    batches=[]
    for i in range(0,len(accepted),a.batch_size):
        chunk=accepted[i:i+a.batch_size];bid=f"semantic-review-{i//a.batch_size+1:03d}"
        payload={"format":"multiversal-semantic-review-batch","version":"1.1.0","batchId":bid,"candidateCount":len(chunk),"familyCounts":dict(Counter(x["objectType"] for x in chunk)),"candidates":chunk}
        (a.out/f"{bid}.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        batches.append({"batchId":bid,"candidateCount":len(chunk),"familyCounts":payload["familyCounts"]})
    summary={"format":"multiversal-semantic-review-index","version":"1.1.0","generatedAt":datetime.now(timezone.utc).isoformat(),"candidateCount":len(accepted),"familyCounts":dict(Counter(x["objectType"] for x in accepted)),"batchCount":len(batches),"batches":batches,"rejectedCounts":dict(rejected),"averageQualityScore":round(sum(x["semanticQualityScore"] for x in accepted)/max(1,len(accepted)),2),"connectedCandidateCount":sum(x["graphDegree"]>0 for x in accepted),"publishedSample":accepted[:220],"authorityNote":"Semantic review batches are non-canonical and require human approval."}
    (a.out/"semantic-review-index.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({k:summary[k] for k in ("candidateCount","familyCounts","batchCount","rejectedCounts","averageQualityScore","connectedCandidateCount")},indent=2))
if __name__=="__main__":main()
