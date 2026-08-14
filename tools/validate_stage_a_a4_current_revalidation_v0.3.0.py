from __future__ import annotations
import csv, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "governance/application-planning/stage-a-a4"
SCOPE = DIR / "A4_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv"
REPORT = DIR / "STAGE_A_A4_CURRENT_REPOSITORY_REVALIDATION_v0.3.0.md"
STATE = DIR / "STAGE_A_A4_CURRENT_REPOSITORY_REVALIDATION_v0.3.0.json"
EXPECTED_SCOPE_SHA = "489b38e60ec3401a81dc9702a14a48dab692f9aca67022ba01e72aaa2c80da79"
EXPECTED_COMPAT_SHA = "340791f2eae9f1db50904d455aa18de8246463b08d0394da02b3a38f91ae8439"
EXPECTED_BASE_SHA = "b3f207e1cae8649afda372d902579bdaade5e3f07470a0ecb149de3978d2c7d9"

errors: list[str] = []
for path in (SCOPE, REPORT, STATE):
    if not path.is_file(): errors.append(f"missing {path.relative_to(ROOT)}")
if errors:
    raise SystemExit("\n".join(errors))

scope_sha = hashlib.sha256(SCOPE.read_bytes()).hexdigest()
if scope_sha != EXPECTED_SCOPE_SHA: errors.append(f"scope sha mismatch {scope_sha}")
rows = list(csv.DictReader(SCOPE.open(newline="", encoding="utf-8")))
counts: dict[str, int] = {}
for row in rows: counts[row["Disposition"]] = counts.get(row["Disposition"], 0) + 1
expected_counts = {"CREATE": 36, "MODIFY_BOUNDED": 2, "REUSE": 13, "PRESERVE": 1}
if len(rows) != 52: errors.append(f"scope rows {len(rows)} != 52")
if counts != expected_counts: errors.append(f"scope counts {counts} != {expected_counts}")

paths = {(r["Disposition"], r["Path"]) for r in rows}
required = {
    ("CREATE", "database/migrations/0002_character_workspace.json"),
    ("REUSE", "apps/client-ui/src/a2/picker/ObjectPicker.tsx"),
    ("REUSE", "packages/contracts/src/a3/selected-context-receipt.ts"),
    ("REUSE", "packages/contracts/src/a3/workspace-entry-port.ts"),
    ("MODIFY_BOUNDED", "apps/client-ui/src/App.tsx"),
    ("MODIFY_BOUNDED", "apps/client-ui/src/a3/services/localAlphaIdentityAdapter.ts"),
    ("PRESERVE", "apps/client-ui/package.json"),
}
missing = required - paths
if missing: errors.append(f"missing required scope rows: {sorted(missing)}")

state = json.loads(STATE.read_text(encoding="utf-8"))
if state.get("verdict") != "PASS — READY_FOR_BOUNDED_A4_ACTIVATION": errors.append("bad verdict")
if state["historicalSources"]["compatibilitySha256"] != EXPECTED_COMPAT_SHA: errors.append("bad compatibility sha")
if state["historicalSources"]["preimplementationSha256"] != EXPECTED_BASE_SHA: errors.append("bad preimplementation sha")
if state["changedPathScope"]["sha256"] != EXPECTED_SCOPE_SHA: errors.append("state scope sha mismatch")
if state["changedPathScope"]["rows"] != 52: errors.append("state scope row mismatch")
if state["dependencies"]["a2"] != "completed_verified" or state["dependencies"]["a3"] != "completed_verified": errors.append("predecessor status mismatch")
if state["persistenceRecheck"]["nextLogicalMigration"] != "database/migrations/0002_character_workspace.json": errors.append("migration decision mismatch")
for flag in ("newRuntimeDependencyRequired", "productionProviderRequired", "paidServiceRequired", "releaseAuthorized", "deploymentAuthorized"):
    if state.get(flag) is not False: errors.append(f"{flag} must be false")

text = REPORT.read_text(encoding="utf-8")
for phrase in (
    "PASS — READY_FOR_BOUNDED_A4_ACTIVATION",
    EXPECTED_COMPAT_SHA,
    EXPECTED_BASE_SHA,
    EXPECTED_SCOPE_SHA,
    "A4-GAP-003 and A4-GAP-004 are resolved",
    "0002_character_workspace.json",
    "build-first rule",
):
    if phrase not in text: errors.append(f"report missing {phrase}")

if errors:
    raise SystemExit("STAGE-A-A4 CURRENT REVALIDATION: FAIL\n- " + "\n- ".join(errors))
print("STAGE-A-A4 CURRENT REVALIDATION: PASS")
print(f"scope_rows={len(rows)} create={counts['CREATE']} modify_bounded={counts['MODIFY_BOUNDED']} reuse={counts['REUSE']} preserve={counts['PRESERVE']}")
