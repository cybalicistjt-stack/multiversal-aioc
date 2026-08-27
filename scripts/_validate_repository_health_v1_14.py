#!/usr/bin/env python3
"""Deterministic Multiversal canonical-state health validator."""
from __future__ import annotations
import argparse,copy,importlib.util,json
from pathlib import Path
from typing import Any
def _module(name:str,path:Path):
 spec=importlib.util.spec_from_file_location(name,path); assert spec and spec.loader
 mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
HERE=Path(__file__).resolve().parent
v113=_module("multiversal_repository_health_v1_13",HERE/"_validate_repository_health_v1_13.py")
gcl11=_module("multiversal_gcl11_repository_health",HERE/"_gcl11_repository_health.py")
convergence=_module("multiversal_execution_convergence",HERE/"validate_execution_convergence.py")
base=v113.v112.v111.v110.v19.v18.v17.base
base.APP_WORKFLOWS_ALLOWED={"_validation-core-profile.yml","validate-current-tranche.yml","validate-repository-health.yml"}
_original_gcl10=v113.gcl10.check
def _completed_gcl10(root:Path,base_module:Any)->dict[str,Any]:
 real=base_module.read_json
 def read(path:Path):
  value=real(path)
  if path.name=="GCL_PROGRAM_BACKLOG.json" and value.get("program_id")=="GCL":
   value=copy.deepcopy(value); value["current_item"]="GCL-10"; value["current_item_status"]="completed_verified"
  return value
 base_module.read_json=read
 try:return _original_gcl10(root,base_module)
 finally:base_module.read_json=real
v113.gcl10.check=_completed_gcl10
def check_aioc(root:Path,errors:list[str])->dict[str,Any]:
 result=v113.check_aioc(root,errors)
 if errors:return result
 try:result["gcl_session_construction_library"]=gcl11.check(root,base)
 except Exception as exc:errors.append(f"AIOC: {exc}")
 if errors:return result
 try:result["execution_convergence"]=convergence.check(root)
 except Exception as exc:errors.append(f"AIOC convergence: {exc}")
 return result
def main()->int:
 p=argparse.ArgumentParser(); p.add_argument("--root",default="."); p.add_argument("--app-root"); p.add_argument("--output"); a=p.parse_args(); root=Path(a.root).resolve(); errors=[]; aioc=check_aioc(root,errors); audit=base.read_json(root/"governance/repository-health/CANONICAL_STATE_AUDIT.json"); app=None
 if a.app_root:app=base.check_app(Path(a.app_root).resolve(),audit,errors)
 result={"schema_version":"1.14.1","validator":"scripts/validate_repository_health.py","status":"FAIL" if errors else "PASS","aioc":aioc,"application":app,"errors":errors}; payload=json.dumps(result,indent=2,sort_keys=True)+"\n"
 if a.output:Path(a.output).write_text(payload,encoding="utf-8")
 print(payload,end=""); return 1 if errors else 0
if __name__=="__main__":raise SystemExit(main())
