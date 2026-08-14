from __future__ import annotations
import csv, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCOPE = ROOT / "governance/application-planning/stage-a-a4/A4_CURRENT_CHANGED_PATH_SCOPE_v0.3.1.csv"
AMENDMENT = ROOT / "governance/application-planning/stage-a-a4/STAGE_A_A4_SCOPE_AMENDMENT_v0.3.1.md"
EXPECTED = "9145d0dea1f312174e6e23958d08e03433d0bfc0337068c0680d555c05498072"
errors: list[str] = []

if hashlib.sha256(SCOPE.read_bytes()).hexdigest() != EXPECTED:
    errors.append("scope sha mismatch")
rows = list(csv.DictReader(SCOPE.open(encoding="utf-8", newline="")))
counts: dict[str, int] = {}
for row in rows:
    counts[row["Disposition"]] = counts.get(row["Disposition"], 0) + 1
if len(rows) != 53:
    errors.append(f"expected 53 scope rows, got {len(rows)}")
if counts != {"CREATE": 36, "MODIFY_BOUNDED": 3, "REUSE": 13, "PRESERVE": 1}:
    errors.append(f"unexpected disposition counts {counts}")
match = [r for r in rows if r["Path"] == "apps/client-ui/src/App.test.tsx"]
if len(match) != 1 or match[0]["Disposition"] != "MODIFY_BOUNDED":
    errors.append("App.test.tsx bounded amendment missing")
text = AMENDMENT.read_text(encoding="utf-8")
for phrase in (EXPECTED, "product behavior is frozen", "Campaign and Character entry remain separate fresh authorization decisions"):
    if phrase not in text:
        errors.append(f"amendment missing: {phrase}")
if errors:
    raise SystemExit("A4 SCOPE AMENDMENT: FAIL\n- " + "\n- ".join(errors))
print("A4 SCOPE AMENDMENT: PASS")
print("scope_rows=53 create=36 modify_bounded=3 reuse=13 preserve=1")
