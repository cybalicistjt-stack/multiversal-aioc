#!/usr/bin/env python3
"""Validate the canonical typed roadmap DAG and compile a deterministic planning projection."""
from __future__ import annotations
import argparse,json
from pathlib import Path
GRAPH=Path("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json");POINTER=Path("governance/ai/runtime/CURRENT_WORK_POINTER.json");OUTPUT=Path("governance/ai/runtime/ROADMAP_COMPILED_PROJECTION.json");EDGE_KEYS={"hard_requires","start_requires","late_bind_requires","golden_proof_requires"};INITIAL=("MCS","MCCS","MRCS","MSAS")
def load(p):
 v=json.loads(p.read_text(encoding="utf-8"))
 if not isinstance(v,dict):raise ValueError(f"{p} must contain an object")
 return v
def validate(g):
 if g.get("status")!="CURRENT_PLANNING_AUTHORITY":raise ValueError("typed roadmap graph is not CURRENT_PLANNING_AUTHORITY")
 e=g.get("program_edges")
 if not isinstance(e,dict) or not e:raise ValueError("program_edges missing")
 for n,r in e.items():
  if EDGE_KEYS-set(r):raise ValueError(f"{n} missing edge types")
  if any(not isinstance(r[k],list) for k in EDGE_KEYS):raise ValueError(f"{n} edge arrays invalid")
 deps={n:{x for x in r["hard_requires"] if x in e} for n,r in e.items()};tmp=set();done=set()
 def visit(n):
  if n in done:return
  if n in tmp:raise ValueError(f"hard dependency cycle at {n}")
  tmp.add(n)
  for d in sorted(deps[n]):visit(d)
  tmp.remove(n);done.add(n)
 for n in sorted(deps):visit(n)
 initial=set(INITIAL)
 for n in initial:
  if initial&(set(e[n]["hard_requires"])|set(e[n]["start_requires"])):raise ValueError(f"{n} serializes initial lanes")
 if "MERA" not in e["MBES"]["hard_requires"]:raise ValueError("MBES must preserve causal MERA dependency")
 if "SMB12" in e["SMB13"]["hard_requires"] or "SMB12" in e["SMB13"]["start_requires"]:raise ValueError("optional live AI must not gate alpha")
 if "PRE_ALPHA_SAFETY" not in e["SMB13"]["start_requires"]:raise ValueError("remote alpha lacks safety gate")
def compile_projection(g,p):
 validate(g);e=g["program_edges"];hard={n:{x for x in r["hard_requires"] if x in e} for n,r in e.items()};remaining=set(e);done=set();layers=[]
 while remaining:
  ready=sorted(n for n in remaining if hard[n]<=done)
  if not ready:raise ValueError("hard dependency graph cannot be layered")
  layers.append(ready);done.update(ready);remaining.difference_update(ready)
 a=p.get("active_attempt",{})
 return {"schema_version":"1.0.0","source_graph":str(GRAPH).replace("\\","/"),"current_selection":{"work_item_id":a.get("work_item_id"),"attempt_id":a.get("attempt_id"),"status":a.get("status"),"implementation_authority":a.get("implementation_authority")},"hard_dependency_layers":layers,"initial_parallel_product_lanes":list(INITIAL),"initial_parallel_lane_count":4,"foundation_overlap":{"CNI":["CNI-01","CNI-02","CNI-03..13"],"PCA_start_after":"CNI-02","PCA_16_is_golden_convergence":True},"rotation_start_milestones":g.get("milestone_gates",{}).get("rotation",{}),"smb_normalization":{"core_ux":"SMB10A","creator_saa_integration":"SMB10B","pre_alpha_safety":"PRE_ALPHA_SAFETY","optional_ai_nonblocking_for_alpha":True,"brp_between":"SMB16 -> BRP -> SMB17"}}
def main():
 p=argparse.ArgumentParser();p.add_argument("--root",default=".");p.add_argument("--check",action="store_true");p.add_argument("--output");a=p.parse_args();root=Path(a.root);expected=compile_projection(load(root/GRAPH),load(root/POINTER));target=root/(Path(a.output) if a.output else OUTPUT)
 if a.check:
  try:observed=json.loads(target.read_text(encoding="utf-8"))
  except (OSError,json.JSONDecodeError):print(f"roadmap compiled projection missing/invalid: {target}");return 1
  if observed!=expected:print(f"roadmap compiled projection drift: {target}");return 1
 else:target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(expected,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print(json.dumps(expected,indent=2,sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
