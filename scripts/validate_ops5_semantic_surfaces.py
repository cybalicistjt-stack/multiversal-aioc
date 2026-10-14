#!/usr/bin/env python3
"""Operations V5 semantic checks; inherited V4 mechanics remain unchanged."""
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
read=lambda p:(root/p).read_text(encoding="utf-8")
current=json.loads(read("operations/CURRENT.json"))
registry=json.loads(read("operations/CONTROL_SURFACE_REGISTRY.json"))
item=json.loads(read("operations/work-items/OPS5-01.json"))
door=read("operations/BOOTSTRAP.md")
contract=read("operations/OPERATING_CONTRACT.md")
workflow=read(".github/workflows/validate-repository-health.yml")
errors=[]
if current.get("system")!="OPS5" or current.get("schema_version")!="5.0.0":
    errors.append("CURRENT is not OPS5 version 5.0.0")
if registry.get("schema_version")!="5.0.0":
    errors.append("registry version mismatch")
if "Operations V5" not in door or "Operations V5" not in contract:
    errors.append("canonical door/contract version mismatch")
if "CI is an **acceptance system, not a remote REPL**" not in door+contract:
    errors.append("inherited CI feedback boundary lost")
for path in ("scripts/validate_operations_v5.py","scripts/validate_ops5_semantic_surfaces.py"):
    if path not in workflow:
        errors.append("missing workflow validation: "+path)
for path in ("scripts/ops4_execution_guard.py","scripts/ops4_ci_guard.py"):
    if not (root/path).is_file():
        errors.append("missing inherited guard: "+path)
if "tests/control_plane/test_ops4_ci_guard.py" not in workflow:
    errors.append("workflow omits inherited OPS4 CI/response guard regression")
registered={x.get("path"):x for x in registry.get("surfaces",[]) if isinstance(x,dict)}
for path in ("scripts/validate_operations_v5.py","scripts/validate_ops5_semantic_surfaces.py",
             "scripts/ops4_execution_guard.py","scripts/ops4_ci_guard.py"):
    if registered.get(path,{}).get("disposition")!="VALIDATION_ONLY":
        errors.append("missing validation-only surface: "+path)
for path in ("scripts/validate_operations_v3.py","scripts/validate_ops3_semantic_surfaces.py"):
    if registered.get(path,{}).get("disposition")!="HISTORICAL_INERT":
        errors.append("historical OPS3 authority restored: "+path)
resource=current.get("research_resource") or {}
if resource.get("source_commit")!=item.get("resource_commit"):
    errors.append("research resource and OPS5 item do not agree on source pin")
if resource.get("executionAllowed") is not False:
    errors.append("research resource must not grant execution")
if resource.get("canonical_work_selector")!="operations/CURRENT.json":
    errors.append("research resource created a second selector")
if not resource.get("fallback"):
    errors.append("no source-only fallback")
if "optional" not in (door+contract).lower():
    errors.append("research has become compulsory")
if errors:
    raise SystemExit("\n".join(errors))
print("OPS5 semantic audit: PASS")
