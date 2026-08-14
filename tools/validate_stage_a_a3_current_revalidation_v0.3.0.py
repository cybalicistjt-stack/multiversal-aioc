#!/usr/bin/env python3
"""Validate the current STAGE-A-A3 repository revalidation package."""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/stage-a-a3"
JSON_PATH = BASE / "STAGE_A_A3_CURRENT_REPOSITORY_REVALIDATION_v0.3.0.json"
MD_PATH = BASE / "STAGE_A_A3_CURRENT_REPOSITORY_REVALIDATION_v0.3.0.md"
SCOPE_PATH = BASE / "A3_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"A3 CURRENT REVALIDATION v0.3.0: FAIL — {message}")


data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
rows = list(csv.DictReader(SCOPE_PATH.open(encoding="utf-8", newline="")))
md = MD_PATH.read_text(encoding="utf-8")

require(data["schemaVersion"] == "0.3.0", "schema version")
require(data["stage"] == "STAGE-A-A3", "stage id")
require(data["status"] == "REVALIDATED_READY_FOR_BOUNDED_ACTIVATION", "status")
require(data["activationGate"]["verdict"] == "PASS — READY_FOR_BOUNDED_A3_ACTIVATION", "activation verdict")
require(data["historicalSource"]["sourceBytesVerified"] is True, "historical source bytes not verified")
require(data["historicalSource"]["historicalValidator"] == "PASS", "historical validator")
require(data["historicalSource"]["sha256"] == "b0396d3945a0c200a2b7d3821bb851c06c57fbc83a29373fc0a5758df32bf1b7", "historical artifact hash")
require(data["currentAuthority"]["a2Status"] == "COMPLETED_VERIFIED", "A2 completion boundary")
require(data["repositoryDeltaSinceA2Merge"]["productSourceChanged"] is False, "unexpected product-source delta")
require(len(data["repositoryDeltaSinceA2Merge"]["changedPaths"]) == 5, "post-A2 delta count")
require(data["historicalAnchorRevalidation"]["anchors"] == 22, "anchor count")
require(data["historicalAnchorRevalidation"]["exactBlobAnchorsUnchanged"] == 12, "unchanged exact anchor count")
require(data["historicalAnchorRevalidation"]["presenceAnchorsStillPresent"] == 8, "presence anchor count")
require(data["historicalAnchorRevalidation"]["intentionallyChangedAnchors"] == 2, "changed anchor count")
require(len(data["p9RegressionValidation"]) == 7, "P9 regression count")
require(all(item["status"] == "PASS" for item in data["p9RegressionValidation"]), "P9 regression failure")
require([item["id"] for item in data["gapRevalidation"]] == [f"A3-GAP-{i:03d}" for i in range(1, 11)], "gap ids")
require(len(data["newA2ReuseSeams"]) >= 6, "A2 reuse seams")

counts = Counter(row["Disposition"] for row in rows)
expected = {"CREATE": 31, "MODIFY_BOUNDED": 1, "REUSE": 15, "PRESERVE": 2}
require(len(rows) == 49, "scope row count")
require(dict(counts) == expected, f"scope disposition counts {dict(counts)!r}")
require(data["changedPathScope"]["rows"] == len(rows), "JSON/CSV row mismatch")
for key, disposition in (("create", "CREATE"), ("modifyBounded", "MODIFY_BOUNDED"), ("reuse", "REUSE"), ("preserve", "PRESERVE")):
    require(data["changedPathScope"][key] == counts[disposition], f"JSON/CSV {disposition} mismatch")

modified = [row for row in rows if row["Disposition"] == "MODIFY_BOUNDED"]
require(modified[0]["Path"] == "apps/client-ui/src/App.tsx", "only bounded modification must be App.tsx")
require(not any("pnpm-lock" in row["Path"] for row in rows), "lockfile scope is forbidden")
package_rows = [row for row in rows if row["Path"] == "apps/client-ui/package.json"]
require(len(package_rows) == 1 and package_rows[0]["Disposition"] == "PRESERVE", "client package must be preserved")
require(not any("provider" in row["Path"].lower() and row["Disposition"] in {"CREATE", "MODIFY_BOUNDED"} for row in rows), "provider-specific path introduced")

for key in (
    "a2CompletedVerified",
    "historicalSourceBytesVerified",
    "historicalPackageValidatorPass",
    "currentProductSourceStableSinceA2Merge",
    "providerNeutralFoundationsPresent",
    "p9RegressionsPass",
):
    require(data["activationGate"][key] is True, f"activation prerequisite {key}")
for key in (
    "a3NamespaceCollision",
    "newRuntimeDependencyRequired",
    "productionIdentityProviderRequired",
    "databaseVendorDecisionRequired",
    "paidServiceRequired",
    "releaseAuthorized",
    "deploymentAuthorized",
):
    require(data["activationGate"][key] is False, f"forbidden activation condition {key}")

for token in (
    "PASS — READY_FOR_BOUNDED_A3_ACTIVATION",
    "cdd0713864edc6b6fc3ad78c66b3d2edb5491b2d",
    "92f3f2e029ca041d2e0fdb739c614d58c7e913e8",
    "A3_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv",
    "No dependency or lockfile change is planned.",
):
    require(token in md, f"handoff token missing: {token}")

print("STAGE-A-A3 CURRENT REPOSITORY REVALIDATION v0.3.0: PASS")
print(f"scope_rows={len(rows)} create={counts['CREATE']} modify={counts['MODIFY_BOUNDED']} reuse={counts['REUSE']} preserve={counts['PRESERVE']}")
print("p9_regressions=7/7 gaps=10/10 activation_gate=PASS")
