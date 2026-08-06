from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SPEC = ROOT / "feature-packets" / "MV-IA-F015_WORLD_SETTING_MANAGEMENT.md"
MATRIX = ROOT / "feature-packets" / "MV-IA-F015_WORLD_SETTING_MATRIX.json"
TRACE = ROOT / "IA-D07-001_WORLD_SETTING_TRACEABILITY.md"
READY = ROOT / "IA-D07-001_WORLD_SETTING_READINESS.md"
COMPLETE = ROOT / "IA-D07-001_WORLD_SETTING_COMPLETION.md"
BACKLOG = ROOT / "INTERNAL_ALPHA_DESIGN_BACKLOG.md"

errors: list[str] = []
for path in (SPEC, MATRIX, TRACE, READY, COMPLETE, BACKLOG):
    if not path.exists():
        errors.append(f"missing {path.name}")

if not errors:
    spec = SPEC.read_text(encoding="utf-8")
    data = json.loads(MATRIX.read_text(encoding="utf-8"))
    backlog = BACKLOG.read_text(encoding="utf-8")
    required = [
        "Campaign-local overlays",
        "Hidden entries are filtered before search",
        "semantic geography",
        "snapshot-plus-tail recovery",
        "P9-06-008-attempt-002",
    ]
    for token in required:
        if token not in spec:
            errors.append(f"spec missing {token}")
    if data.get("workItemId") != "IA-D07-001":
        errors.append("workItemId")
    if data.get("featureId") != "MV-IA-F015":
        errors.append("featureId")
    if len(data.get("fixtures", [])) != 24:
        errors.append("fixtures count")
    if len(data.get("implementationSlices", [])) != 8:
        errors.append("implementationSlices count")
    if len(data.get("acceptanceCriteria", [])) != 28:
        errors.append("acceptanceCriteria count")
    if data.get("blockingFindings") != []:
        errors.append("blocking findings")
    if data.get("nextWorkItemId") != "IA-D07-002":
        errors.append("next item")
    if "IA-D07-001 — MV-IA-F015 World and Setting Management — complete" not in backlog:
        errors.append("backlog completion")
    if "IA-D07-002 — MV-IA-F017 Adventure and Module Management — next" not in backlog:
        errors.append("backlog next")

if errors:
    print("IA-D07-001 WORLD/SETTING VALIDATION: FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("IA-D07-001 WORLD/SETTING VALIDATION: PASS")
