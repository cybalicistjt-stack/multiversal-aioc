#!/usr/bin/env python3
"""Build/check the compact derived tranche-readiness index."""
from __future__ import annotations
import argparse,json
from pathlib import Path
SOURCE=Path("governance/ai/runtime/TRANCHE_READINESS_SOURCE.json");OUTPUT=Path("governance/ai/runtime/TRANCHE_READINESS_INDEX.json");HOT={"ARI-18","ARI-19","ARI-20","ARI-21","ARI-22A","ARI-22B","ARI-22C","MIB-16","MIB-17","MIB-18"}
def build(root):
 src=json.loads((root/SOURCE).read_text(encoding="utf-8"));programs={};ids=[]
 for program,row in src["programs"].items():
  work=row["work_items"];ids.extend(work)
  if len(work)!=row["count"]:raise ValueError(f"{program} count drift")
  programs[program]={"count":len(work),"work_items":work,"default_readiness":"prepared","hot_ready_overrides":[x for x in work if x in HOT]}
 if len(ids)!=src["total_tranches"] or len(set(ids))!=len(ids):raise ValueError("readiness identity/count drift")
 return {"schema_version":"1.1.0","status":"DERIVED_CURRENT","source":str(SOURCE).replace("\\","/"),"total_tranches":len(ids),"branch_policy":{"created_before_governed_start":False,"reserved_branch_template":"implementation/{work_item_id_lower}"},"authority_policy":{"implementation_authority":False,"readiness_never_grants_authority":True},"programs":programs}
def main():
 p=argparse.ArgumentParser();p.add_argument("--root",default=".");p.add_argument("--check",action="store_true");a=p.parse_args();root=Path(a.root);expected=build(root);target=root/OUTPUT
 if a.check:
  try:observed=json.loads(target.read_text(encoding="utf-8"))
  except (OSError,json.JSONDecodeError):print("tranche readiness derived artifact missing/invalid");return 1
  if observed!=expected:print("tranche readiness derived artifact drift");return 1
 else:target.write_text(json.dumps(expected,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(expected,indent=2));return 0
if __name__=="__main__":raise SystemExit(main())
