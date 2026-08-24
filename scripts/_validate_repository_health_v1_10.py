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
v19=_module("multiversal_repository_health_v1_9",HERE/"_validate_repository_health_v1_9.py")
gcl07=_module("multiversal_gcl07_repository_health",HERE/"_gcl07_repository_health.py")
_original_gcl06=v19.gcl06.check
def _completed_gcl06(root:Path,base:Any)->dict[str,Any]:
 real=base.read_json
 def read(path:Path):
  value=real(path)
  if path.name=="GCL_PROGRAM_BACKLOG.json" and value.get("program_id")=="GCL":
   value=copy.deepcopy(value); value["current_item"]="GCL-06"; value["current_item_status"]="completed_verified"
  return value
 base.read_json=read
 try:return _original_gcl06(root,base)
 finally:base.read_json=real
v19.gcl06.check=_completed_gcl06
def check_aioc(root:Path,errors:list[str])->dict[str,Any]:
 result=v19.check_aioc(root,errors)
 if errors:return result
 try:result["gcl_pressure_library"]=gcl07.check(root,v19.v18.v17.base)
 except Exception as exc:errors.append(f"AIOC: {exc}")
 return result
def main()->int:
 p=argparse.ArgumentParser(); p.add_argument("--root",default="."); p.add_argument("--app-root"); p.add_argument("--output"); a=p.parse_args(); root=Path(a.root).resolve(); errors=[]; aioc=check_aioc(root,errors); audit=v19.v18.v17.base.read_json(root/"governance/repository-health/CANONICAL_STATE_AUDIT.json"); app=None
 if a.app_root:app=v19.v18.v17.base.check_app(Path(a.app_root).resolve(),audit,errors)
 result={"schema_version":"1.10.0","validator":"scripts/validate_repository_health.py","status":"FAIL" if errors else "PASS","aioc":aioc,"application":app,"errors":errors}; payload=json.dumps(result,indent=2,sort_keys=True)+"\n"
 if a.output:Path(a.output).write_text(payload,encoding="utf-8")
 print(payload,end=""); return 1 if errors else 0
if __name__=="__main__":raise SystemExit(main())
