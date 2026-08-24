#!/usr/bin/env python3
"""Deterministic Multiversal canonical-state health validator."""
from __future__ import annotations
import argparse, copy, importlib.util, json
from pathlib import Path
from typing import Any

def _module(name:str,path:Path):
    spec=importlib.util.spec_from_file_location(name,path); assert spec and spec.loader
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

HERE=Path(__file__).resolve().parent
base=_module("multiversal_repository_health_v1_6",HERE/"_validate_repository_health_v1_6.py")
gcl04=_module("multiversal_gcl04_repository_health",HERE/"_gcl04_repository_health.py")

# GCL-03 is a predecessor after GCL-04 activation. Reuse the frozen 1.6 semantic
# checker while presenting it a read-only predecessor view of the GCL backlog.
_original_scene=base.check_gcl_scene_library
def _completed_gcl03(root:Path)->dict[str,Any]:
    real_read=base.read_json
    def read(path:Path):
        value=real_read(path)
        if path.name=="GCL_PROGRAM_BACKLOG.json" and value.get("program_id")=="GCL":
            value=copy.deepcopy(value); value["current_item"]="GCL-03"; value["current_item_status"]="completed_verified"
        return value
    base.read_json=read
    try: return _original_scene(root)
    finally: base.read_json=real_read
base.check_gcl_scene_library=_completed_gcl03
_original_aioc=base.check_aioc

def check_aioc(root:Path,errors:list[str])->dict[str,Any]:
    result=_original_aioc(root,errors)
    if errors: return result
    try: result["gcl_encounter_library"]=gcl04.check(root,base)
    except Exception as exc: errors.append(f"AIOC: {exc}")
    return result

def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("--root",default="."); p.add_argument("--app-root"); p.add_argument("--output"); a=p.parse_args()
    root=Path(a.root).resolve(); errors=[]; aioc=check_aioc(root,errors); audit=base.read_json(root/"governance/repository-health/CANONICAL_STATE_AUDIT.json"); app=None
    if a.app_root: app=base.check_app(Path(a.app_root).resolve(),audit,errors)
    result={"schema_version":"1.7.0","validator":"scripts/validate_repository_health.py","status":"FAIL" if errors else "PASS","aioc":aioc,"application":app,"errors":errors}
    payload=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if a.output: Path(a.output).write_text(payload,encoding="utf-8")
    print(payload,end=""); return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
