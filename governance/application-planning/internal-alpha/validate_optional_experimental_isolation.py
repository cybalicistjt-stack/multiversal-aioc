#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
PACKAGE = ROOT / "IA-D08-005_OPTIONAL_EXPERIMENTAL_ISOLATION_REVIEW.md"
FIXTURES = ROOT / "IA-D08-005_ISOLATION_FIXTURE_MATRIX.md"
TRACE = ROOT / "IA-D08-005_ISOLATION_TRACEABILITY.md"
READY = ROOT / "IA-D08-005_ISOLATION_READINESS.md"
COMPLETE = ROOT / "IA-D08-005_COMPLETION_RECORD.md"
BACKLOG = ROOT / "INTERNAL_ALPHA_DESIGN_BACKLOG.md"

errors = []
for path in (PACKAGE, FIXTURES, TRACE, READY, COMPLETE, BACKLOG):
    if not path.is_file():
        errors.append(f"missing {path.name}")

if not errors:
    package = PACKAGE.read_text(encoding="utf-8")
    fixtures = FIXTURES.read_text(encoding="utf-8")
    trace = TRACE.read_text(encoding="utf-8")
    ready = READY.read_text(encoding="utf-8")
    complete = COMPLETE.read_text(encoding="utf-8")
    backlog = BACKLOG.read_text(encoding="utf-8")

    required = [
        "Optional means removable without breaking the core",
        "I0 — Core-required",
        "I1 — Optional supported",
        "I2 — Experimental gated",
        "I3 — Deferred preserved",
        "I4 — Prohibited coupling",
        "Manual fallback",
        "Provider neutrality",
        "Unknown processors",
        "Removal test",
        "IA-D09 — Internal-alpha release-design package",
        "P9-06-008-attempt-002",
    ]
    for token in required:
        if token not in package:
            errors.append(f"package missing: {token}")

    ids = re.findall(r"ISO-FX-\d{3}", fixtures)
    if len(set(ids)) != 24:
        errors.append(f"expected 24 unique fixtures, found {len(set(ids))}")

    for token in ("disabled", "unavailable", "incompatible", "hidden", "accessibility", "offline", "provider"):
        if token.lower() not in fixtures.lower():
            errors.append(f"fixture coverage missing: {token}")

    for token in ("IA-D08-001", "IA-D08-002", "IA-D08-003", "IA-D08-004", "IA-D08-005", "IA-D09"):
        if token not in trace:
            errors.append(f"traceability missing: {token}")

    if "zero blocking findings" not in ready.lower():
        errors.append("readiness does not record zero blocking findings")
    if "READY FOR REVIEW" not in complete:
        errors.append("completion record is not ready for review")
    if "IA-D08-005 — optional and experimental isolation review — package complete; merge verification pending." not in backlog:
        errors.append("backlog does not mark IA-D08-005 package complete pending merge")
    if "IA-D09 — Internal-alpha release-design package — next after IA-D08-005 merge verification." not in backlog:
        errors.append("backlog does not preserve IA-D09 handoff")

if errors:
    print("IA-D08-005 OPTIONAL/EXPERIMENTAL ISOLATION VALIDATION: FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("IA-D08-005 OPTIONAL/EXPERIMENTAL ISOLATION VALIDATION: PASS")
print("fixtures: 24")
print("isolation classes: 5")
print("blocking findings: 0")
