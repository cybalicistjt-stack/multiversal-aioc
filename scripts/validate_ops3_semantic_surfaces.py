#!/usr/bin/env python3
"""Semantic guard against reintroducing the retired Operations V2 control plane."""
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

if errors:
    for error in errors:
        print(error, file=sys.stderr)
    raise SystemExit(1)
print("OPS3 semantic surface audit: PASS")
