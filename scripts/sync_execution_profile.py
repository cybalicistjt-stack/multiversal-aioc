#!/usr/bin/env python3
"""Keep copied execution-objective literals as generated projections of EXECUTION_PROFILE.json."""
from __future__ import annotations
import argparse,ast,json
from pathlib import Path
from pprint import pformat
PROFILE=Path("governance/ai/runtime/EXECUTION_PROFILE.json");HEALTH=Path("scripts/validate_repository_health.py");PREFIX="REQUIRED_SERVICE_OBJECTIVE = "
def objective(root):
 v=json.loads((root/PROFILE).read_text(encoding="utf-8")).get("service_objective")
 if not isinstance(v,dict):raise ValueError("execution profile service_objective missing")
 return v
def health_literal(text):
 tree=ast.parse(text)
 for node in tree.body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="REQUIRED_SERVICE_OBJECTIVE" for t in node.targets):
   v=ast.literal_eval(node.value)
   if not isinstance(v,dict):raise ValueError("REQUIRED_SERVICE_OBJECTIVE must be dict")
   return v
 raise ValueError("REQUIRED_SERVICE_OBJECTIVE not found")
def rewrite(text,value):
 tree=ast.parse(text);target=next((n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="REQUIRED_SERVICE_OBJECTIVE" for t in n.targets)),None)
 if target is None:raise ValueError("REQUIRED_SERVICE_OBJECTIVE not found")
 lines=text.splitlines();lines[target.lineno-1:target.end_lineno]=(PREFIX+pformat(value,width=88,sort_dicts=False)).splitlines();return "\n".join(lines)+"\n"
def main():
 p=argparse.ArgumentParser();p.add_argument("--root",default=".");p.add_argument("--check",action="store_true");p.add_argument("--write",action="store_true");a=p.parse_args();root=Path(a.root);value=objective(root);path=root/HEALTH;text=path.read_text(encoding="utf-8")
 if a.write:path.write_text(rewrite(text,value),encoding="utf-8");return 0
 if health_literal(text)!=value:print("validate_repository_health.py generated service-objective projection is stale");return 1
 print("execution profile projections synchronized");return 0
if __name__=="__main__":raise SystemExit(main())
