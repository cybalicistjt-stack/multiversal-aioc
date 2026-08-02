#!/usr/bin/env python3
"""Assemble hierarchical evidence into object-centric recovery records.

Groups object roots with child/container sections, applies document-family grammars,
computes completeness, and preserves evidence/provenance. Never writes canon.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

FAMILIES=("rule","ability","creature","item","species","npc","vehicle","environment","world","faction","adventure")
GRAMMARS={
 "creature":{"required":["name","description"],"expected":["statistics","traits","actions","habitat","ecology","variants"]},
 "ability":{"required":["name","effect"],"expected":["activation","cost","range","duration","target","scaling","prerequisites"]},
 "item":{"required":["name","description"],"expected":["category","cost","weight","properties","crafting","upgrades"]},
 "species":{"required":["name","description"],"expected":["appearance","culture","traits","adaptations","progression","variants"]},
 "npc":{"required":["name","description"],"expected":["role","personality","affiliation","statistics","equipment","relationships"]},
 "vehicle":{"required":["name","description"],"expected":["class","crew","statistics","components","weapons","upgrades"]},
 "environment":{"required":["name","description"],"expected":["terrain","climate","hazards","weather","adaptations","encounters"]},
 "world":{"required":["name","description"],"expected":["regions","cultures","factions","history","locations","species"]},
 "faction":{"required":["name","description"],"expected":["goals","members","structure","allies","enemies","resources"]},
 "adventure":{"required":["name","description"],"expected":["hook","objectives","scenes","encounters","clues","rewards"]},
 "rule":{"required":["name","procedure"],"expected":["scope","trigger","resolution","exceptions","examples"]},
}
CONTAINERS={"actions","traits","effects","statistics","objectives","equipment","attacks","abilities","variants","prerequisites","origin","description","history","notes","ecology","habitat","appearance","culture","progression","upgrades","components","scenes","encounters","clues","rewards","goals","members","allies","enemies","weather","hazards"}
FAMILY_HINTS={
 "creature":r"\b(?:creature|monster|beast|aberration|hp|ac|multiattack|melee weapon attack)\b",
 "ability":r"\b(?:ability|spell|power|activation|duration|range|prerequisite|cost)\b",
 "item":r"\b(?:item|weapon|armor|equipment|artifact|weight|price|component)\b",
 "species":r"\b(?:species|ancestry|heritage|culture|adaptation|racial trait)\b",
 "npc":r"\b(?:npc|merchant|personality|affiliation|occupation)\b",
 "vehicle":r"\b(?:vehicle|ship|crew|engine|frame|vehicle speed)\b",
 "environment":r"\b(?:environment|terrain|climate|hazard|weather|biome)\b",
 "world":r"\b(?:world|realm|dimension|setting|region|city|continent)\b",
 "faction":r"\b(?:faction|organization|guild|allies|enemies|members)\b",
 "adventure":r"\b(?:adventure|quest|hook|scene|encounter|clue|objective)\b",
 "rule":r"\b(?:rule|check|saving throw|procedure|must|may|dc\s*\d+)\b",
}
FAMILY_HINTS={k:re.compile(v,re.I) for k,v in FAMILY_HINTS.items()}

def load_jsonl(p:Path):
 return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
def stable(*parts): return hashlib.sha256("\n".join(map(str,parts)).encode()).hexdigest()[:20]
def norm(s): return re.sub(r"\s+"," ",str(s or "")).strip()
def choose_family(root, children):
 text=" ".join([root.get("title", ""),root.get("text", ""),root.get("sourceRelativePath","")]+[c.get("title","")+" "+c.get("text","") for c in children])
 scores={f:int((root.get("familyScores") or {}).get(f,0)) for f in FAMILIES}
 for f,p in FAMILY_HINTS.items(): scores[f]+=min(12,2*len(p.findall(text)))
 ranked=sorted(scores.items(),key=lambda x:(-x[1],x[0]))
 return ranked[0][0],ranked[0][1]-ranked[1][1],scores

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--structure",type=Path,required=True);ap.add_argument("--out",type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 nodes=load_jsonl(a.structure/"hierarchical-nodes.jsonl")
 by_id={n["nodeId"]:n for n in nodes}; children=defaultdict(list)
 for n in nodes:
  if n.get("parentId"): children[n["parentId"]].append(n)
 roots=[]
 for n in nodes:
  title=norm(n.get("title")); role=n.get("sectionRole")
  if not n.get("provenanceComplete") or not title or not norm(n.get("text")): continue
  if role=="object-section" or (n.get("identityEligible") and title.lower() not in CONTAINERS and not n.get("parentObjectTitle")):
   roots.append(n)
 assembled=[]; rejected=Counter()
 for root in roots:
  desc=[]; stack=list(children.get(root["nodeId"],[])); seen=set()
  while stack:
   c=stack.pop(0)
   if c["nodeId"] in seen: continue
   seen.add(c["nodeId"]); desc.append(c); stack.extend(children.get(c["nodeId"],[]))
  family,margin,scores=choose_family(root,desc)
  if margin<2: rejected["family-ambiguous"]+=1; continue
  sections=defaultdict(list)
  sections["description"].append(norm(root.get("text")))
  for c in desc:
   key=norm(c.get("title")).lower() or c.get("sectionRole") or "details"
   sections[key].append(norm(c.get("text")))
  grammar=GRAMMARS[family]; present={"name":bool(norm(root.get("title"))),"description":bool(norm(root.get("text")))}
  for field in set(grammar["required"]+grammar["expected"]):
   if field in present: continue
   present[field]=any(field in k or k in field for k in sections)
  required_ok=sum(1 for f in grammar["required"] if present.get(f)); expected_ok=sum(1 for f in grammar["expected"] if present.get(f))
  completeness=round(100*(0.65*required_ok/max(1,len(grammar["required"]))+0.35*expected_ok/max(1,len(grammar["expected"]))))
  evidence=[root]+desc
  provenance=[]
  for e in evidence:
   provenance.append({"sourcePath":e.get("sourceRelativePath"),"pageStart":e.get("pageStart"),"pageEnd":e.get("pageEnd"),"locator":e.get("locator"),"findingId":e.get("findingId"),"nodeId":e.get("nodeId"),"contentHash":e.get("contentHash")})
  missing=[f for f in grammar["required"]+grammar["expected"] if not present.get(f)]
  assembled.append({"assemblyId":"assembly-"+stable(root["nodeId"],family),"objectType":family,"name":norm(root.get("title")),"documentGrammar":family,"rootNodeId":root["nodeId"],"childNodeIds":[x["nodeId"] for x in desc],"sectionMap":dict(sections),"specification":{"summary":norm(root.get("text")),"sections":dict(sections),"mechanicSignals":sum([(x.get("mechanicSignals") or []) for x in evidence],[])},"completenessScore":completeness,"presentFields":present,"missingFields":missing,"familyScores":scores,"familyMargin":margin,"provenance":provenance,"status":"assembled-noncanonical","authority":"Recovery evidence only; independent verification and owner approval required."})
 summary={"format":"multiversal-object-assembly-v4-index","version":"4.0.0","generatedAt":datetime.now(timezone.utc).isoformat(),"inputNodeCount":len(nodes),"rootCandidateCount":len(roots),"assembledObjectCount":len(assembled),"familyCounts":dict(Counter(x["objectType"] for x in assembled)),"averageCompleteness":round(sum(x["completenessScore"] for x in assembled)/max(1,len(assembled)),2),"rejectedCounts":dict(rejected),"publishedSample":assembled[:200]}
 (a.out/"object-assembly-v4-index.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n")
 with (a.out/"assembled-objects.jsonl").open("w",encoding="utf-8") as f:
  for x in assembled:f.write(json.dumps(x,ensure_ascii=False)+"\n")
 print(json.dumps({k:summary[k] for k in ("assembledObjectCount","familyCounts","averageCompleteness","rejectedCounts")},indent=2))
if __name__=="__main__":main()
