#!/usr/bin/env python3
"""Build fault-tolerant Semantic Foundry foundation artifacts.

Uses only the Python standard library. Optional integrations are reported, never
required. Outputs are diagnostic/non-canonical.
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

FAMILIES=("rule","ability","creature","item","species","npc","vehicle","environment","world","faction","adventure")
NEGATIVE_TYPES=("StatField","TableHeader","TableCell","ContainerHeading","ContextualHeading","ProcedureHeading","TaxonomyLabel","ExampleLabel","GeneratorInstruction","PageFurniture","SentenceFragment","ContinuationFragment","ScalarMechanic","DiceExpression","DurationValue","DistanceValue","DifficultyClass")
STAT=re.compile(r"^(?:AC|HP|DR|EP|MP|SP|CR|DC|Speed|Initiative|STR|DEX|CON|INT|WIS|CHA|Armor Class|Hit Points)\s*[:=]?",re.I)
SCALAR=re.compile(r"^(?:DC\s*\d+|\d+(?:\.\d+)?\s*(?:ft|feet|miles?|minutes?|hours?|rounds?|turns?|XP)|\d+d\d+(?:\s*[+-]\s*\d+)?)$",re.I)
CONTAINER={"actions","traits","effects","statistics","objectives","equipment","attacks","abilities","variants","prerequisites","description","notes","examples","campaign use","investigation hooks"}

def load_jsonl(p:Path):
    if not p.exists(): return []
    out=[]
    for line in p.read_text(encoding="utf-8").splitlines():
        try:
            if line.strip(): out.append(json.loads(line))
        except Exception: pass
    return out

def norm(v): return re.sub(r"\s+"," ",str(v or "")).strip()
def key(v): return re.sub(r"[^a-z0-9]+"," ",norm(v).lower()).strip()
def h(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,ensure_ascii=False).encode()).hexdigest()

def classify_negative(row):
    name=norm(row.get("name")); summary=norm((row.get("specification") or {}).get("summary"))
    if STAT.search(name): return "StatField"
    if key(name) in CONTAINER: return "ContainerHeading"
    if SCALAR.fullmatch(name): return "ScalarMechanic"
    if name.endswith((",",";",":")) or len(name)<3: return "SentenceFragment"
    if re.search(r"\b(?:table|chart|weighted|roll result)\b",name,re.I): return "TableHeader"
    if re.search(r"^(?:how to|choosing|creating|using|step \d+)\b",name,re.I): return "ProcedureHeading"
    if re.search(r"\b(?:taxonomy|types|categories|universal traits)\b",name,re.I): return "TaxonomyLabel"
    if re.search(r"^(?:example|sample|suggested)\b",name,re.I): return "ExampleLabel"
    if re.search(r"\b(?:generator|roll 1d\d+)\b",f"{name} {summary}",re.I): return "GeneratorInstruction"
    return None

def label_functions(row):
    labels=[]
    neg=classify_negative(row)
    if neg: labels.append({"function":"negative-element-classifier","label":"NOT_OBJECT","reason":neg})
    r=row.get("recovery") or {}
    if r.get("identityConfidence",0)>=92 and r.get("completenessScore",0)>=80: labels.append({"function":"high-identity-completeness","label":"PROBABLE_OBJECT"})
    if r.get("familyMargin",0)<6: labels.append({"function":"low-family-margin","label":"REVIEW"})
    if len(row.get("provenance") or [])==0: labels.append({"function":"missing-provenance","label":"NOT_READY"})
    if any((x.get("resolution")!="resolved") for x in row.get("relationships") or []): labels.append({"function":"unresolved-relationship","label":"REVIEW"})
    return labels

def active_score(row, labels):
    r=row.get("recovery") or {}; score=0
    score+=max(0,100-abs(85-int(r.get("identityConfidence",0))))
    score+=max(0,30-3*int(r.get("familyMargin",0)))
    score+=20 if any(x["label"]=="REVIEW" for x in labels) else 0
    score+=15 if row.get("type") in {"npc","faction","vehicle","adventure"} else 0
    score+=10 if len(row.get("relationships") or []) else 0
    return score

def semantic_diff(a,b):
    fields=("type","name","lifecycleStatus","reviewRoute")
    changes=[]
    for f in fields:
        if a.get(f)!=b.get(f): changes.append({"field":f,"before":a.get(f),"after":b.get(f)})
    if h(a.get("specification") or {})!=h(b.get("specification") or {}): changes.append({"field":"specification","kind":"semantic-content-change"})
    if h(a.get("relationships") or [])!=h(b.get("relationships") or []): changes.append({"field":"relationships","kind":"relationship-change"})
    if h(a.get("provenance") or [])!=h(b.get("provenance") or []): changes.append({"field":"provenance","kind":"evidence-change"})
    return changes

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--candidates",type=Path,required=True); ap.add_argument("--out",type=Path,required=True); ap.add_argument("--previous",type=Path)
    a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
    source=a.candidates/"canonical-candidates-v4.jsonl" if a.candidates.is_dir() else a.candidates
    rows=load_jsonl(source); previous=load_jsonl(a.previous) if a.previous else []
    labels=[]; neg=Counter(); lf=Counter(); family=Counter(); active=[]
    for row in rows:
        family[row.get("type","unknown")]+=1
        ls=label_functions(row)
        for x in ls: lf[f"{x['function']}:{x['label']}"]+=1
        n=classify_negative(row)
        if n: neg[n]+=1
        labels.append({"candidateId":row.get("id"),"labels":ls})
        active.append({"candidateId":row.get("id"),"type":row.get("type"),"name":row.get("name"),"selectionScore":active_score(row,ls),"reason":[x["function"] for x in ls],"provenance":row.get("provenance"),"recovery":row.get("recovery")})
    active.sort(key=lambda x:(-x["selectionScore"],x.get("type") or "",x.get("name") or ""))
    # cap per family for owner-efficient active-learning packet
    selected=[]; counts=Counter()
    for x in active:
        if counts[x["type"]]<8 and len(selected)<80:
            selected.append(x); counts[x["type"]]+=1
    prev={x.get("id"):x for x in previous}; diffs=[]
    for row in rows:
        if row.get("id") in prev:
            c=semantic_diff(prev[row["id"]],row)
            if c: diffs.append({"candidateId":row.get("id"),"changes":c})
    contracts={
      "$schema":"https://json-schema.org/draft/2020-12/schema","$id":"https://multiversal.invalid/schema/recovery-candidate-envelope-v1.json","title":"Multiversal Recovery Candidate Envelope","type":"object","additionalProperties":True,
      "required":["id","type","name","lifecycleStatus","specification","provenance","validation","reviewRoute"],
      "properties":{"id":{"type":"string","minLength":3},"type":{"enum":list(FAMILIES)},"name":{"type":"string","minLength":1},"lifecycleStatus":{"const":"candidate"},"provenance":{"type":"array","minItems":1},"reviewRoute":{"enum":["expert-sample","human-review","evidence-only"]}}
    }
    provenance={"format":"multiversal-semantic-foundry-provenance-manifest","generatedAt":datetime.now(timezone.utc).isoformat(),"inputPath":str(source),"inputSha256":h(rows),"recordCount":len(rows),"script":"audit/build_semantic_foundry_foundations.py","python":sys.version,"authority":"Diagnostics only; no canonical writes."}
    optional={name:False for name in ("pydantic","unstructured","sentence_transformers","faiss","rdflib","pyshacl","instructor","mlflow","opentelemetry")}
    for name in list(optional):
        try: __import__(name); optional[name]=True
        except Exception: pass
    outputs={
      "negative-semantic-ontology.json":{"types":list(NEGATIVE_TYPES),"constraints":["StatField cannot be ObjectIdentity","ScalarMechanic cannot be RelationshipTarget","ContainerHeading cannot be RootObject without independent evidence","TableCell cannot be RootObject before reconstruction","PageFurniture cannot be CandidateEvidence"]},
      "labeling-function-report.json":{"candidateCount":len(rows),"labelCounts":dict(lf),"negativeTypeCounts":dict(neg),"records":labels[:500]},
      "active-learning-packet.json":{"selectionCount":len(selected),"familyCounts":dict(counts),"records":selected},
      "semantic-diff-report.json":{"previousProvided":bool(a.previous),"changedCandidateCount":len(diffs),"records":diffs[:1000]},
      "recovery-candidate-envelope.schema.json":contracts,
      "provenance-manifest.json":provenance,
      "optional-capability-report.json":optional,
    }
    for name,obj in outputs.items(): (a.out/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    index={"format":"multiversal-semantic-foundry-foundation-index","generatedAt":provenance["generatedAt"],"candidateCount":len(rows),"familyCounts":dict(family),"negativeCounts":dict(neg),"activeLearningCount":len(selected),"semanticDiffCount":len(diffs),"optionalCapabilities":optional,"allCoreArtifactsProduced":all((a.out/x).exists() for x in outputs),"authority":"Non-canonical engineering diagnostics."}
    (a.out/"semantic-foundry-foundation-index.json").write_text(json.dumps(index,indent=2)+"\n")
    print(json.dumps(index,indent=2))
if __name__=="__main__": main()
