#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
IA = ROOT / "governance" / "application-planning" / "internal-alpha"

REQUIRED = [
    "IA-D09_INTERNAL_ALPHA_RELEASE_DESIGN_PACKAGE.md",
    "IA-D09_RELEASE_TRACEABILITY.json",
    "IA-D09_FIXTURE_CATALOG.json",
    "IA-D09_PERMISSION_ACCESSIBILITY_RECOVERY_MATRIX.md",
    "IA-D09_BUDGETS_AND_TESTER_ENTRY.md",
    "IA-D09_IMPLEMENTATION_QUEUE.json",
    "IA-D09_OWNER_DECISION_REGISTER.md",
    "IA-D09_DESIGN_COMPLETION_REVIEW.md",
]

def fail(msg):
    print(f"FAIL: {msg}")
    return False

def main():
    ok = True
    for name in REQUIRED:
        path = IA / name
        if not path.is_file():
            ok = fail(f"missing {name}") and ok
        elif path.stat().st_size < 200:
            ok = fail(f"underspecified {name}") and ok

    if not ok:
        return 1

    trace = json.loads((IA / "IA-D09_RELEASE_TRACEABILITY.json").read_text())
    series = {row["series"] for row in trace.get("coverage", [])}
    expected = {f"IA-D0{i}" for i in range(1, 10)}
    # IA-D09 is represented by this package itself; traceability source coverage must include D01-D08.
    if not {f"IA-D0{i}" for i in range(1, 9)}.issubset(series):
        ok = fail("traceability does not cover IA-D01 through IA-D08") and ok

    fixtures = json.loads((IA / "IA-D09_FIXTURE_CATALOG.json").read_text())
    if fixtures.get("bounded") is not True or fixtures.get("complete_game_corpus") is not False:
        ok = fail("fixture catalog must be explicitly bounded and non-complete") and ok
    ids = [x.get("id") for x in fixtures.get("fixtures", [])]
    if len(ids) < 24 or len(ids) != len(set(ids)):
        ok = fail("fixture catalog must contain at least 24 unique fixtures") and ok

    queue = json.loads((IA / "IA-D09_IMPLEMENTATION_QUEUE.json").read_text())
    slices = queue.get("slices", [])
    slice_ids = {s.get("id") for s in slices}
    if len(slices) < 12 or len(slice_ids) != len(slices):
        ok = fail("implementation queue must contain at least 12 unique slices") and ok
    for s in slices:
        for dep in s.get("depends_on", []):
            if dep not in slice_ids:
                ok = fail(f"unknown dependency {dep} in {s.get('id')}") and ok
    if any(s.get("required_for_candidate") and "optional" in s.get("name", "").lower() for s in slices):
        ok = fail("optional capability slice incorrectly required for candidate") and ok

    package = (IA / "IA-D09_INTERNAL_ALPHA_RELEASE_DESIGN_PACKAGE.md").read_text()
    matrix = (IA / "IA-D09_PERMISSION_ACCESSIBILITY_RECOVERY_MATRIX.md").read_text()
    budgets = (IA / "IA-D09_BUDGETS_AND_TESTER_ENTRY.md").read_text()
    owner = (IA / "IA-D09_OWNER_DECISION_REGISTER.md").read_text()
    review = (IA / "IA-D09_DESIGN_COMPLETION_REVIEW.md").read_text()

    required_phrases = {
        "package": ["release not authorized", "all-optionals-off", "owner-only decision"],
        "matrix": ["unauthorized hidden information", "keyboard", "screen reader", "reauthorize"],
        "budgets": ["< 2 s", "zero optional AI-provider spend", "Tester-entry prerequisites"],
        "owner": ["authorize Internal Alpha tester access", "production credentials", "public release"],
        "review": ["P9-06-008-attempt-002", "Design Standards Completion", "completed_verified"],
    }
    texts = {"package": package, "matrix": matrix, "budgets": budgets, "owner": owner, "review": review}
    for key, phrases in required_phrases.items():
        for phrase in phrases:
            if phrase.lower() not in texts[key].lower():
                ok = fail(f"{key} missing required boundary phrase: {phrase}") and ok

    if ok:
        print("PASS: IA-D09 Internal Alpha release-design package")
        print(f"files={len(REQUIRED)} fixtures={len(ids)} slices={len(slices)} series={len(series)}")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(main())
