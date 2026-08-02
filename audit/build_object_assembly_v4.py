#!/usr/bin/env python3
"""Assemble hierarchical evidence into object-centric recovery records.

V4.2.1 separates true game-object identities from taxonomy pages, procedures,
examples, generators, tables, and fragments before canonical candidate creation.
Outputs are non-canonical evidence only.
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
CONTAINERS={"actions","traits","effects","statistics","objectives","equipment","attacks","abilities","variants","prerequisites","origin","description","history","notes","ecology","habitat","appearance","culture","progression","upgrades","components","scenes","encounters","clues","rewards","goals","members","allies","enemies","weather","hazards","properties","procedure","examples","requirements"}
GENERIC={"overview","introduction","summary","background","contents","table of contents","key distinctions","mechanics","core themes","common traits","universal traits","body types","native realm","language","alignment","role","roles","types","categories"}
NON_OBJECT_PATTERNS=[
 re.compile(r"^(?:example|examples|suggested|sample|quick reference|step\s+\d+|how to|choosing|creating|building|using|installing|casting|resolving)\b",re.I),
 re.compile(r"\b(?:generator|worksheet|printable|table|chart|progression|costs? by|limits? by|body types?|universal traits?|creature type)\b",re.I),
 re.compile(r"^(?:native realm|source of|effect on|magic interaction|identity/memory|spiritual/emotional)\b",re.I),
]
FRAGMENT_PATTERNS=[
 re.compile(r"[,;:]$"),
 re.compile(r"^(?:adds?|boosts?|enhances?|embeds?|feeds?|sealed|bound|encased)\b",re.I),
 re.compile(r"\b(?:the|a|an|or|and|of|to|with|inside|bypassing)$",re.I),
]
FAMILY_HINTS={
 "creature":r"\b(?:creature|monster|beast|aberration|hp|ac|multiattack|melee weapon attack|challenge rating)\b",
 "ability":r"\b(?:ability|spell|power|activation|duration|range|prerequisite|mana cost|effect:)\b",
 "item":r"\b(?:item|weapon|armor|equipment|artifact|weight|price|component|rarity)\b",
 "species":r"\b(?:species|ancestry|heritage|culture|adaptation|racial trait|appearance)\b",
 "npc":r"\b(?:npc|merchant|personality|affiliation|occupation|named character)\b",
 "vehicle":r"\b(?:vehicle|ship|crew|engine|frame|vehicle speed|pilot)\b",
 "environment":r"\b(?:environment|terrain|climate|hazard|weather|biome)\b",
 "world":r"\b(?:world|realm|dimension|setting|region|city|continent)\b",
 "faction":r"\b(?:faction|organization|guild|allies|enemies|members|leadership)\b",
 "adventure":r"\b(?:adventure|quest|hook|scene|encounter|clue|objective|reward)\b",
 "rule":r"\b(?:rule|check|saving throw|procedure|must|may|dc\s*\d+|resolution)\b",
}
FAMILY_HINTS={k:re.compile(v,re.I) for k,v in FAMILY_HINTS.items()}

def load_jsonl(p:Path):
 return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
def stable(*parts): return hashlib.sha256("\n".join(map(str,parts)).encode()).hexdigest()[:20]
def norm(s): return re.sub(r"\s+"," ",str(s or "")).strip()
def title_key(s): return re.sub(r"[^a-z0-9]+"," ",norm(s).lower()).strip()
def node_identity_eligible(node):
 """Honor an explicit flag when present; otherwise derive eligibility from node structure."""
 if "identityEligible" in node:
  return bool(node.get("identityEligible"))
 role=node.get("sectionRole")
 block=node.get("blockType")
 title=norm(node.get("title")); text=norm(node.get("text"))
 return bool(title and text and role not in ("container","table") and block!="table")
def identity_reason(node):
 title=norm(node.get("title")); text=norm(node.get("text")); key=title_key(title)
 if not title or not text: return "empty-title-or-text"
 if key in CONTAINERS or key in GENERIC: return "container-or-generic"
 if node.get("sectionRole") in ("container","table") or node.get("blockType")=="table": return "table-or-container"
 if len(title)<4 or len(title)>90 or len(title.split())>12: return "malformed-title"
 if any(p.search(title) for p in NON_OBJECT_PATTERNS): return "non-object-section"
 if any(p.search(title) for p in FRAGMENT_PATTERNS): return "fragment-title"
 if len(text)<35: return "insufficient-evidence"
 if title.endswith(('.', '!', '?')): return "sentence-title"
 return None

def choose_family(root, children):
 text=" ".join([root.get("title", ""),root.get("text", ""),root.get("sourceRelativePath","")]+[c.get("title","")+" "+c.get("text","") for c in children])
 scores={f:int((root.get("familyScores") or {}).get(f,0)) for f in FAMILIES}
 for f,p in FAMILY_HINTS.items(): scores[f]+=min(14,2*len(p.findall(text)))
 ranked=sorted(scores.items(),key=lambda x:(-x[1],x[0]))
 return ranked[0][0],ranked[0][1]-ranked[1][1],scores

def candidate_kind(title,text):
 joined=f"{title} {text}".lower()
 if re.search(r"\b(?:generator|roll 1d\d+|worksheet|random table)\b",joined): return "generator"
 if re.search(r"\b(?:procedure|how to|step\s+\d+|installation|crafting process)\b",joined): return "procedure"
 if re.search(r"\b(?:creature type|species type|taxonomy|universal traits|body types)\b",joined): return "taxonomy"
 if re.search(r"\b(?:example|sample|suggested)\b",joined): return "example"
 return "content-object"

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--structure",type=Path,required=True);ap.add_argument("--out",type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 nodes=load_jsonl(a.structure/"hierarchical-nodes.jsonl")
 children=defaultdict(list)
 for n in nodes:
  if n.get("parentId"): children[n["parentId"]].append(n)
 roots=[]; rejected=Counter(); eligibility=Counter()
 for n in nodes:
  if not n.get("provenanceComplete"): eligibility["missing-provenance"]+=1; continue
  if not node_identity_eligible(n): eligibility["not-identity-eligible"]+=1; continue
  if n.get("parentObjectTitle"): eligibility["has-parent-object"]+=1; continue
  reason=identity_reason(n)
  if reason: rejected[reason]+=1; continue
  if n.get("sectionRole")=="object-section" or n.get("blockType") in ("stat-block","mechanic-block","prose"):
   roots.append(n)
  else: eligibility["unsupported-root-structure"]+=1
 assembled=[]; seen_source_names=set()
 for root in roots:
  desc=[]; stack=list(children.get(root["nodeId"],[])); seen=set()
  while stack:
   c=stack.pop(0)
   if c["nodeId"] in seen: continue
   seen.add(c["nodeId"]); desc.append(c); stack.extend(children.get(c["nodeId"],[]))
  family,margin,scores=choose_family(root,desc)
  if margin<3: rejected["family-ambiguous"]+=1; continue
  name=norm(root.get("title")); dedupe=(root.get("sourceRelativePath"),title_key(name),family)
  if dedupe in seen_source_names: rejected["duplicate-source-identity"]+=1; continue
  seen_source_names.add(dedupe)
  kind=candidate_kind(name,norm(root.get("text")))
  if kind!="content-object": rejected[f"kind-{kind}"]+=1; continue
  sections=defaultdict(list); root_text=norm(root.get("text")); sections["description"].append(root_text)
  for c in desc:
   ctext=norm(c.get("text"))
   if not ctext: continue
   key=title_key(c.get("title")) or c.get("sectionRole") or "details"
   if key in CONTAINERS: key=key.replace(" ","_")
   sections[key].append(ctext)
  grammar=GRAMMARS[family]; present={"name":True,"description":bool(root_text)}
  if family=="ability": present["effect"]=bool(re.search(r"\b(?:effect|damage|gain|create|target|becomes?|must|may)\b",root_text,re.I))
  if family=="rule": present["procedure"]=bool(re.search(r"\b(?:must|make a|roll|check|save|when|if|then|dc\s*\d+)\b",root_text,re.I))
  for field in set(grammar["required"]+grammar["expected"]):
   if field in present: continue
   present[field]=any(field in k or k in field for k in sections)
  required_ok=sum(1 for f in grammar["required"] if present.get(f)); expected_ok=sum(1 for f in grammar["expected"] if present.get(f))
  completeness=round(100*(0.7*required_ok/max(1,len(grammar["required"]))+0.3*expected_ok/max(1,len(grammar["expected"]))))
  if required_ok<len(grammar["required"]): rejected["missing-required-identity-fields"]+=1; continue
  evidence=[root]+desc; provenance=[]
  for e in evidence:
   provenance.append({"sourcePath":e.get("sourceRelativePath"),"pageStart":e.get("pageStart"),"pageEnd":e.get("pageEnd"),"locator":e.get("locator"),"findingId":e.get("findingId"),"nodeId":e.get("nodeId"),"contentHash":e.get("contentHash")})
  missing=[f for f in grammar["required"]+grammar["expected"] if not present.get(f)]
  identity_conf=min(99,45+scores[family]*3+margin*3+(10 if root.get("sectionRole")=="object-section" else 0)+(8 if root.get("blockType")=="stat-block" else 0))
  assembled.append({"assemblyId":"assembly-"+stable(root["nodeId"],family),"objectType":family,"name":name,"candidateKind":kind,"documentGrammar":family,"rootNodeId":root["nodeId"],"childNodeIds":[x["nodeId"] for x in desc],"sectionMap":dict(sections),"specification":{"summary":root_text,"sections":dict(sections),"mechanicSignals":sum([(x.get("mechanicSignals") or []) for x in evidence],[])},"completenessScore":completeness,"identityConfidence":identity_conf,"presentFields":present,"missingFields":missing,"familyScores":scores,"familyMargin":margin,"provenance":provenance,"status":"assembled-noncanonical","authority":"Recovery evidence only; independent verification and owner approval required."})
 family_counts=dict(Counter(x["objectType"] for x in assembled))
 summary={"format":"multiversal-object-assembly-v4-index","version":"4.2.1","generatedAt":datetime.now(timezone.utc).isoformat(),"inputNodeCount":len(nodes),"rootCandidateCount":len(roots),"assembledObjectCount":len(assembled),"familyCounts":family_counts,"averageCompleteness":round(sum(x["completenessScore"] for x in assembled)/max(1,len(assembled)),2),"averageIdentityConfidence":round(sum(x["identityConfidence"] for x in assembled)/max(1,len(assembled)),2),"eligibilityCounts":dict(eligibility),"rejectedCounts":dict(rejected),"survivalGates":{"rootsExist":len(roots)>0,"objectsExist":len(assembled)>0,"multipleFamilies":len(family_counts)>=3},"publishedSample":assembled[:200]}
 (a.out/"object-assembly-v4-index.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n")
 with (a.out/"assembled-objects.jsonl").open("w",encoding="utf-8") as f:
  for x in assembled:f.write(json.dumps(x,ensure_ascii=False)+"\n")
 print(json.dumps({k:summary[k] for k in ("rootCandidateCount","assembledObjectCount","familyCounts","averageCompleteness","averageIdentityConfidence","eligibilityCounts","rejectedCounts","survivalGates")},indent=2))
if __name__=="__main__":main()
