#!/usr/bin/env python3
"""Semantic guard for Operations V4 while preserving retired V2/V3 surfaces as inert history."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
DOOR = "operations/BOOTSTRAP.md"
BACKGROUND = "OPS3 BACKGROUND ONLY / NO OPERATIONAL AUTHORITY"
HISTORICAL = "OPS3 HISTORICAL REFERENCE / NO OPERATIONAL AUTHORITY"

errors = []

roadmap = (ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md").read_text(encoding="utf-8")
if BACKGROUND not in roadmap:
    errors.append("application dependency roadmap is not explicit OPS3 background-only")
for phrase in (
    "runtime authority remains bootstrap",
    "runtime selection lives in pointer/index",
    "continue executes the runtime-selected tranche",
    "current-work pointer",
):
    if phrase in roadmap.lower():
        errors.append(f"application roadmap retains retired semantic authority phrase: {phrase}")

DWC = ROOT / "governance/application-planning/dwc-speech/README.md"
dwc = DWC.read_text(encoding="utf-8")
if "OPS3 LANE REFERENCE / NO GLOBAL OPERATIONAL AUTHORITY" not in dwc:
    errors.append("DWC recovery entry lacks OPS3 lane-only authority banner")
if DOOR not in dwc or "operations/CURRENT.json" not in dwc:
    errors.append("DWC recovery entry does not route global authority through OPS3")
for phrase in ("current-work pointer", "CURRENT_WORK_POINTER.json"):
    if phrase.lower() in dwc.lower():
        errors.append(f"DWC recovery entry retains retired global route: {phrase}")

for relative in (
    "governance/ai/interaction-system/README.md",
    "governance/ai/interaction-system/pilot/AIOC_INTEGRATION.md",
):
    text = (ROOT / relative).read_text(encoding="utf-8")
    if HISTORICAL not in text:
        errors.append(f"interaction-system surface is not historical inert: {relative}")

scorecard = json.loads((ROOT / "governance/ai/interaction-system/live/EXECUTION_CONVERGENCE_SCORECARD.json").read_text(encoding="utf-8"))
if scorecard.get("ops3_disposition") != "HISTORICAL_INERT" or scorecard.get("operational_authority") is not False:
    errors.append("legacy execution convergence scorecard is not historical inert")

retired_patterns = (
    "scripts/validate-ppia*.py",
    "scripts/validate-capp*.py",
    "scripts/execution_integrity_gate.py",
    "scripts/sync-capp-roadmap-index.py",
    "tools/capp_*.py",
    "tools/validate_stage_a_*.py",
    "tools/validate_ia_d09_owner_decision_*.py",
)
for pattern in retired_patterns:
    for path in ROOT.glob(pattern):
        text = path.read_text(encoding="utf-8")
        if "retired" not in text.lower() or DOOR not in text or "SystemExit(2)" not in text:
            errors.append(f"legacy program executable is not fail-closed OPS3 historical stub: {path.relative_to(ROOT)}")

prompt_adapter_path = ROOT / "operations/adapters/GPT_PROJECT_INSTRUCTIONS.md"
prompt_adapter = prompt_adapter_path.read_text(encoding="utf-8")
for required in (
    "EXECUTOR ADAPTER / NON-AUTHORITATIVE",
    DOOR,
    "Owner Prompt Kit — NON-AUTHORITATIVE convenience",
    "cannot redefine `Continue`",
    "Neither section selects current work",
    "Sections B-E are an owner convenience library",
):
    if required not in prompt_adapter:
        errors.append(f"GPT owner prompt adapter missing non-authority invariant: {required}")
for forbidden in (
    "governance/ai/runtime/CURRENT_WORK_POINTER.json",
    "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json",
    "governance/ai/interaction-system/EXECUTION_TERMINATION_CONTRACT.json",
):
    if forbidden in prompt_adapter:
        errors.append(f"GPT owner prompt adapter contains retired live route: {forbidden}")

current = json.loads((ROOT / "operations/CURRENT.json").read_text(encoding="utf-8"))
door = (ROOT / "operations/BOOTSTRAP.md").read_text(encoding="utf-8")
contract = (ROOT / "operations/OPERATING_CONTRACT.md").read_text(encoding="utf-8")
workflow = (ROOT / ".github/workflows/validate-repository-health.yml").read_text(encoding="utf-8")
registry = json.loads((ROOT / "operations/CONTROL_SURFACE_REGISTRY.json").read_text(encoding="utf-8"))
if current.get("system") != "OPS4" or current.get("schema_version") != "4.0.0": errors.append("CURRENT is not canonical OPS4")
for required in ("Operations V4","CI is an **acceptance system, not a remote REPL**","scripts/ops4_ci_guard.py"):
    if required not in door + "\n" + contract: errors.append(f"OPS4 canonical surfaces missing feedback invariant: {required}")
for required in ("scripts/validate_operations_v4.py","scripts/validate_ops4_semantic_surfaces.py","tests/control_plane/test_ops4_ci_guard.py"):
    if required not in workflow: errors.append(f"OPS4 workflow missing required validator/regression: {required}")
by_path={row.get("path"):row for row in registry.get("surfaces",[]) if isinstance(row,dict)}
for required in ("scripts/validate_operations_v4.py","scripts/validate_ops4_semantic_surfaces.py","scripts/ops4_execution_guard.py","scripts/ops4_ci_guard.py"):
    if by_path.get(required,{}).get("disposition")!="VALIDATION_ONLY": errors.append(f"OPS4 validation surface is not registered VALIDATION_ONLY: {required}")
for historical in ("scripts/validate_operations_v3.py","scripts/validate_ops3_semantic_surfaces.py"):
    if by_path.get(historical,{}).get("disposition")!="HISTORICAL_INERT": errors.append(f"OPS3 validator is not retired as historical inert: {historical}")
if errors:
    for error in errors:
        print(error, file=sys.stderr)
    raise SystemExit(1)
print("OPS4 semantic surface audit: PASS")
