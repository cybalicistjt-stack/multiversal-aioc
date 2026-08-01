#!/usr/bin/env python3
"""Build a balanced, evidence-backed substantive content-review queue.

Broad rule fragments remain excluded. Candidates must have usable provenance and
object-like names; table labels, sentence fragments, and navigation headings are
rejected. Outputs never modify canon.
"""
from __future__ import annotations
import argparse, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

PRIORITY_TYPES=("ability","creature","item","species","npc","vehicle","environment","world","faction","adventure")
TYPE_WEIGHT={t:len(PRIORITY_TYPES)-i for i,t in enumerate(PRIORITY_TYPES)}
GENERIC={"overview","introduction","description","table","results","attributes","attribute selection","abilities","traits","species perks","local fauna or creatures","exotic boost effects"}
TABLE_WORDS=re.compile(r"\b(?:roll|result|description|effect|effects|table|1d\d+|d\d+)\b",re.I)
SENTENCE_START=re.compile(r"^(?:across|and|as|because|but|during|for|from|if|in|of|on|or|the|through|to|when|while|with)\b",re.I)

def load(p): return json.loads(p.read_text(encoding="utf-8"))

def candidates(root):
 out=[]
 for p in sorted(root.glob("*-recovery-*.json")):
  if p.name.endswith("index.json"): continue
  out.extend(load(p).get("candidates",[]))
 return out

def usable_provenance(c):
 evidence=c.get("evidence") or c.get("provenance") or c.get("canonicalEnvelope",{}).get("provenance") or []
 return [x for x in evidence if isinstance(x,dict) and (str(x.get("sourcePath") or "").strip() or x.get("findingId") or x.get("locator"))]

def good_name(name,typ):
 n=re.sub(r"\s+"," ",name).strip(); low=n.lower().strip(" .:-")
 reasons=[]; words=n.split()
 if not n or low in GENERIC: reasons.append("generic")
 if len(n)<3 or len(words)>12: reasons.append("length")
 if n.endswith((",",";",":")): reasons.append("fragment-punctuation")
 if SENTENCE_START.search(n): reasons.append("sentence-fragment")
 if sum(ch in ",.;" for ch in n)>=2: reasons.append("prose-fragment")
 if re.match(r"^\d+[.)]?\s+",n) and (TABLE_WORDS.search(n) or "(" in n): reasons.append("numbered-table-label")
 if TABLE_WORDS.search(n) and typ not in ("ability","item"): reasons.append("table-label")
 if re.search(r"\bv(?:alpha|beta)?\d*\b",low): reasons.append("version-suffix")
 return not reasons,reasons

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--recovery",type=Path,required=True); ap.add_argument("--out",type=Path,required=True); ap.add_argument("--limit",type=int,default=200); ap.add_argument("--batch-size",type=int,default=50); a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
 pools=defaultdict(list); rejected=Counter()
 for c in candidates(a.recovery):
  typ=str(c.get("objectType") or c.get("canonicalEnvelope",{}).get("objectType") or "unknown")
  name=str(c.get("name") or c.get("canonicalEnvelope",{}).get("name") or "").strip()
  if typ not in PRIORITY_TYPES: continue
  provenance=usable_provenance(c)
  if not provenance: rejected["missing-usable-provenance"]+=1; continue
  ok,issues=good_name(name,typ)
  if not ok:
   for issue in issues: rejected[issue]+=1
   continue
  readiness=float(c.get("readinessScore") or c.get("readiness",{}).get("score") or 0)
  missing=c.get("missingFields") or []
  relationships=c.get("relationshipCandidates") or c.get("relationships") or c.get("proposedRelationships") or []
  score=readiness+TYPE_WEIGHT.get(typ,0)*2+min(len(provenance),5)-len(missing)*1.5-min(len(relationships),10)*0.5
  pools[typ].append({"candidateId":c.get("candidateId"),"objectType":typ,"name":name,"priorityScore":round(score,2),"readinessScore":readiness,"recommendedPack":c.get("recommendedPack"),"provenance":provenance,"recoveredSpec":c.get("recoveredSpec") or c.get("specializedSpec") or {},"relationships":relationships,"missingFields":missing,"reviewDecision":"unreviewed","reviewQuestions":["Is this a distinct canonical object?","Is the proposed object type correct?","Does the recovered specification preserve the source mechanics?","Are duplicate and relationship candidates resolved?","Is the recommended Pack correct?"],"authority":"Priority review candidate only; no canonical write is authorized."})
 for typ in pools: pools[typ].sort(key=lambda x:(-x["priorityScore"],x["name"].lower()))
 # Balanced round-robin prevents one family from consuming the entire queue.
 rows=[]; order=list(PRIORITY_TYPES); cursor=0
 while len(rows)<a.limit and any(pools.values()):
  typ=order[cursor%len(order)]; cursor+=1
  if pools[typ]: rows.append(pools[typ].pop(0))
 batches=[]
 for i in range(0,len(rows),a.batch_size):
  chunk=rows[i:i+a.batch_size]; bid=f"priority-content-{i//a.batch_size+1:03d}"
  (a.out/f"{bid}.json").write_text(json.dumps({"format":"multiversal-priority-content-review-batch","version":"1.2.0","batchId":bid,"candidateCount":len(chunk),"candidates":chunk},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
  batches.append({"batchId":bid,"candidateCount":len(chunk),"objectTypeCounts":dict(Counter(x["objectType"] for x in chunk))})
 summary={"format":"multiversal-priority-content-review-index","version":"1.2.0","generatedAt":datetime.now(timezone.utc).isoformat(),"candidateCount":len(rows),"batchCount":len(batches),"batchSize":a.batch_size,"objectTypeCounts":dict(Counter(x["objectType"] for x in rows)),"rejectedCounts":dict(rejected),"batches":batches,"publishedSample":rows[:200],"excludedFirstPassTypes":["rule"],"selectionPolicy":{"usableProvenanceRequired":True,"objectLikeNameRequired":True,"balancedAcrossFamilies":True},"authorityNote":"This queue starts substantive human content review and does not modify canon."}
 (a.out/"priority-content-review-index.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps({k:summary[k] for k in ("candidateCount","batchCount","objectTypeCounts","rejectedCounts")},indent=2))
if __name__=="__main__": main()
