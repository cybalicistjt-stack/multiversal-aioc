#!/usr/bin/env python3
"""Build the first substantive content-review queue from recovery candidates.

Prioritizes named game objects with strong provenance and readiness. Broad rule
fragments are kept out of this first queue because they require a separate rule
decomposition pass. Outputs remain review candidates and never modify canon.
"""
from __future__ import annotations
import argparse, json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

PRIORITY_TYPES=("ability","creature","item","species","npc","vehicle","environment","world","faction","adventure")
TYPE_WEIGHT={t:len(PRIORITY_TYPES)-i for i,t in enumerate(PRIORITY_TYPES)}

def load(p): return json.loads(p.read_text(encoding="utf-8"))

def candidates(root):
 out=[]
 # Recovery files are named ability-recovery-0001.json, creature-recovery-0001.json, etc.
 for p in sorted(root.glob("*-recovery-*.json")):
  if p.name.endswith("index.json"): continue
  payload=load(p)
  out.extend(payload.get("candidates",[]))
 return out

def get(c,key,default=None):
 return c.get(key,c.get("canonicalEnvelope",{}).get(key,default))

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--recovery",type=Path,required=True); ap.add_argument("--out",type=Path,required=True); ap.add_argument("--limit",type=int,default=200); ap.add_argument("--batch-size",type=int,default=50); a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
 rows=[]
 for c in candidates(a.recovery):
  typ=str(get(c,"objectType","unknown")); name=str(get(c,"name","")).strip(); readiness=float(c.get("readinessScore") or c.get("readiness",{}).get("score") or 0)
  provenance=c.get("provenance") or c.get("evidence") or c.get("canonicalEnvelope",{}).get("provenance") or []
  if typ not in PRIORITY_TYPES or not name or not provenance: continue
  score=readiness + TYPE_WEIGHT.get(typ,0)*2 + min(len(provenance),5)
  rows.append({"candidateId":c.get("candidateId") or get(c,"id"),"objectType":typ,"name":name,"priorityScore":round(score,2),"readinessScore":readiness,"recommendedPack":c.get("recommendedPack"),"provenance":provenance,"recoveredSpec":c.get("recoveredSpec") or c.get("specializedSpec") or {},"relationships":c.get("relationships") or c.get("proposedRelationships") or c.get("relationshipCandidates") or [],"missingFields":c.get("missingFields") or [],"reviewDecision":"unreviewed","reviewQuestions":["Is this a distinct canonical object?","Is the proposed object type correct?","Does the recovered specification preserve the source mechanics?","Are duplicate and relationship candidates resolved?","Is the recommended Pack correct?"],"authority":"Priority review candidate only; no canonical write is authorized."})
 rows.sort(key=lambda x:(-x["priorityScore"],x["objectType"],x["name"].lower()))
 rows=rows[:a.limit]
 batches=[]
 for i in range(0,len(rows),a.batch_size):
  chunk=rows[i:i+a.batch_size]; bid=f"priority-content-{i//a.batch_size+1:03d}"
  (a.out/f"{bid}.json").write_text(json.dumps({"format":"multiversal-priority-content-review-batch","version":"1.1.0","batchId":bid,"candidateCount":len(chunk),"candidates":chunk},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
  batches.append({"batchId":bid,"candidateCount":len(chunk),"objectTypeCounts":dict(Counter(x["objectType"] for x in chunk))})
 summary={"format":"multiversal-priority-content-review-index","version":"1.1.0","generatedAt":datetime.now(timezone.utc).isoformat(),"candidateCount":len(rows),"batchCount":len(batches),"batchSize":a.batch_size,"objectTypeCounts":dict(Counter(x["objectType"] for x in rows)),"batches":batches,"publishedSample":rows[:200],"excludedFirstPassTypes":["rule"],"authorityNote":"This queue starts substantive human content review and does not modify canon."}
 (a.out/"priority-content-review-index.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps({k:summary[k] for k in ("candidateCount","batchCount","objectTypeCounts")},indent=2))
if __name__=="__main__": main()
