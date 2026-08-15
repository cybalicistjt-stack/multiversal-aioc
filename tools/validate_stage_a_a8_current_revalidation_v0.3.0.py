from __future__ import annotations

import csv
import hashlib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/stage-a-a8"
SCOPE = BASE / "A8_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv"
AUTHORITY = BASE / "A8_CURRENT_AUTHORITY_DISPOSITION_v0.3.0.csv"
HANDOFF = BASE / "STAGE_A_A8_CURRENT_REPOSITORY_REVALIDATION_v0.3.0.md"
R0 = BASE / "supplemental-authority/STAGE_A_A8_R0_COMPLETION_RECEIPT.json"

EXPECTED_SCOPE_SHA = "959d967ca83b1b96d88fa67393f851b117be10b3d7e1da2a2aca8c4627103247"
EXPECTED_AUTHORITY_SHA = "f526aed72745052885f129ed77edc0fbabed0823c893b388b63cf24a9bf3f142"
EXPECTED_PREIMPLEMENTATION_SHA = "692bae390c47dffc3d6104739fc9a7cb4087a3226b115612bea0ac02cc0a4af6"
EXPECTED_COMPATIBILITY_SHA = "985319ccbf6f41655a94fbc0e4a1cb1af65c23547cf3a8d0df0ab6433d149bdf"
EXPECTED_HISTORICAL_PLAN_SHA = "5d1c7aa918720a4194969b3a1c12b5d28665aa9888f0aba648fd57b9d7d3326f"
EXPECTED_APP_PRODUCT_PREDECESSOR = "2821fd41c06a61983c0cfb96d374c298dcb3fc48"
EXPECTED_APP_CURRENT_MAIN = "8239a5119c3cda3982bf35075cfd744ff951d21b"
EXPECTED_AIOC_BASELINE = "0a88fc31aacd51e670941779c76ba2374f6e9c40"
EXPECTED_R0_MERGE = "08e0ec54808b901a62bfcc537b3dac395ca46490"
EXPECTED_SCOPE_ROWS = 102
EXPECTED_AUTHORITY_ROWS = 79
EXPECTED_OPERATION_COUNTS = Counter({"CREATE":62,"REUSE":30,"REUSE_CONTEXT":7,"WRAP":2,"MODIFY_BOUNDED":1})

errors: list[str] = []

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

if not SCOPE.is_file():
    errors.append("missing A8 current changed-path scope")
else:
    if digest(SCOPE) != EXPECTED_SCOPE_SHA:
        errors.append(f"scope sha mismatch: {digest(SCOPE)}")
    rows = list(csv.DictReader(SCOPE.open(encoding="utf-8", newline="")))
    if len(rows) != EXPECTED_SCOPE_ROWS:
        errors.append(f"scope rows {len(rows)} != {EXPECTED_SCOPE_ROWS}")
    paths = [r["Path"] for r in rows]
    if len(paths) != len(set(paths)):
        errors.append("scope contains duplicate paths")
    counts = Counter(r["Operation"] for r in rows)
    if counts != EXPECTED_OPERATION_COUNTS:
        errors.append(f"scope operation counts unexpected: {dict(counts)}")
    path_set = set(paths)
    required = {
        "database/migrations/0006_a8_asset_foundations.json",
        "packages/contracts/src/inventory-equipment/asset-instance-port.ts",
        "packages/contracts/src/shared-assets/shared-asset-port.ts",
        "packages/contracts/src/entity-catalog/product-identity-port.ts",
        "packages/contracts/src/entity-catalog/creator-origin-port.ts",
        "packages/contracts/src/entity-catalog/content-context-port.ts",
        "packages/contracts/src/entity-catalog/compatibility-evaluation-port.ts",
        "packages/contracts/src/authoring-provenance/source-state-reference-port.ts",
        "packages/contracts/src/entity-catalog/product-lineage-port.ts",
        "packages/contracts/src/entity-catalog/market-context-metadata-port.ts",
        "packages/contracts/src/authoring-provenance/remechanization-candidate-reference.ts",
        "packages/contracts/src/shared-assets/a8-cross-domain-result-coordinator.ts",
        "packages/contracts/src/shared-assets/vehicle-asset-port.ts",
        "packages/contracts/src/shared-assets/vehicle-crew-station-port.ts",
        "packages/contracts/src/shared-assets/vehicle-movement-port.ts",
        "packages/contracts/src/shared-assets/vehicle-system-resource-port.ts",
        "packages/contracts/src/shared-assets/vehicle-action-adapter.ts",
        "packages/contracts/src/shared-assets/vehicle-damage-capture-port.ts",
        "packages/contracts/src/shared-assets/asset-operation-status-port.ts",
        "packages/contracts/src/a2/object-contracts.ts",
        "packages/contracts/src/a3/stable-subject-session-port.ts",
        "packages/contracts/src/a4/character-control-port.ts",
        "packages/contracts/src/a6/action-result-handoff.ts",
        "packages/contracts/src/a7/combat-atomic-result-coordinator.ts",
        "packages/contracts/src/session/authoritative-session-command-handler.ts",
        "packages/contracts/src/session/hidden-information-response-filter.ts",
        "packages/contracts/src/session/checkpoint-reconnect-restoration.ts",
        "packages/contracts/src/observability/structured-audit-telemetry.ts",
        "packages/contracts/src/backup-restore-export.ts",
        "packages/entitlements/src/entitlement-service-port.ts",
        "apps/client-ui/src/a8/a8.supplemental-boundaries.test.ts",
        "apps/client-ui/src/App.tsx",
        "tools/verify_stage_a_a8.py",
        ".github/workflows/validate-stage-a-a8-assets-vehicles.yml",
        "docs/evidence/stage-a-a8/**",
        "receipts/STAGE-A-A8-CLOSURE.json",
    }
    missing = sorted(required - path_set)
    if missing:
        errors.append(f"scope missing required paths: {missing}")
    if any("<next>" in p for p in path_set):
        errors.append("historical <next> migration placeholder remains")
    if "packages/contracts/src/shared-assets/vehicle-profile-port.ts" in path_set:
        errors.append("historical mixed vehicle-profile path must be superseded")
    if any(r["Operation"] in {"DELETE","REWRITE","REPLACE"} for r in rows):
        errors.append("destructive operation present")
    wraps = {r["Path"] for r in rows if r["Operation"] == "WRAP"}
    expected_wraps = {
        "packages/contracts/src/session/authoritative-session-command-handler.ts",
        "packages/contracts/src/session/hidden-information-response-filter.ts",
    }
    if wraps != expected_wraps:
        errors.append(f"wrapper set unexpected: {sorted(wraps)}")
    context = {r["Path"]:r for r in rows if r["Operation"] == "REUSE_CONTEXT"}
    for p in ("packages/contracts/src/authority-control/README.md","packages/contracts/src/downtime-projects/README.md"):
        if p not in context:
            errors.append(f"placeholder must be context-only: {p}")
    closure = [r for r in rows if r["Path"] == "receipts/STAGE-A-A8-CLOSURE.json"]
    if len(closure) != 1 or "completion-only" not in closure[0]["Purpose"].lower():
        errors.append("A8 closure receipt must remain completion-only")

if not AUTHORITY.is_file():
    errors.append("missing A8 authority disposition matrix")
else:
    if digest(AUTHORITY) != EXPECTED_AUTHORITY_SHA:
        errors.append(f"authority sha mismatch: {digest(AUTHORITY)}")
    arows = list(csv.DictReader(AUTHORITY.open(encoding="utf-8", newline="")))
    if len(arows) != EXPECTED_AUTHORITY_ROWS:
        errors.append(f"authority rows {len(arows)} != {EXPECTED_AUTHORITY_ROWS}")
    hist = [r for r in arows if r["Source"] == "HISTORICAL_55_PATH_PLAN"]
    supp = [r for r in arows if r["Source"] == "A8_R0_SUPPLEMENTAL_MATRIX"]
    if len(hist) != 55:
        errors.append(f"historical classifications {len(hist)} != 55")
    if len(supp) != 24:
        errors.append(f"supplemental classifications {len(supp)} != 24")
    expected_ids = {f"A8S-{i:03d}" for i in range(1,25)}
    got_ids = {r["Authority_ID"] for r in supp}
    if got_ids != expected_ids:
        errors.append(f"supplemental IDs unexpected: {sorted(got_ids)}")
    expected_class = {
      "A8S-001":"ADOPT_SUPPLEMENT","A8S-002":"ADOPT_SUPPLEMENT","A8S-003":"ADOPT_SUPPLEMENT","A8S-004":"ADOPT_SUPPLEMENT",
      "A8S-005":"ADOPT_SUPPLEMENT","A8S-006":"ADOPT_SUPPLEMENT","A8S-007":"ADOPT_SUPPLEMENT","A8S-008":"ADOPT_SUPPLEMENT","A8S-009":"ADOPT_SUPPLEMENT",
      "A8S-010":"ADOPT_CURRENT","A8S-011":"ADD_DORMANT","A8S-012":"ADD_DORMANT","A8S-013":"ADD_DORMANT","A8S-014":"DEFER","A8S-015":"ADD_DORMANT",
      "A8S-016":"DEFER","A8S-017":"DEFER","A8S-018":"DEFER","A8S-019":"PROHIBIT_DUPLICATION","A8S-020":"PROHIBIT_DUPLICATION",
      "A8S-021":"PROHIBIT_DUPLICATION","A8S-022":"PROHIBIT_DUPLICATION","A8S-023":"REUSE_IMPLEMENTED","A8S-024":"REUSE_IMPLEMENTED",
    }
    for r in supp:
        if expected_class[r["Authority_ID"]] != r["Classification"]:
            errors.append(f"{r['Authority_ID']} classification {r['Classification']} unexpected")
    hist_map = {r["Source_Item"]: r for r in hist}
    if hist_map.get("packages/contracts/src/shared-assets/vehicle-profile-port.ts",{}).get("Classification") != "CONFLICT_REQUIRES_REDESIGN":
        errors.append("vehicle-profile historical path not classified CONFLICT_REQUIRES_REDESIGN")
    if hist_map.get("packages/contracts/src/authority-control/**",{}).get("Classification") != "CONFLICT_REQUIRES_REDESIGN":
        errors.append("authority-control wildcard not classified for redesign")
    if hist_map.get("packages/contracts/src/downtime-projects/**",{}).get("Classification") != "DEFER":
        errors.append("downtime-projects wildcard not deferred")

if not R0.is_file():
    errors.append("missing A8-R0 completion receipt")
else:
    import json
    r0 = json.loads(R0.read_text(encoding="utf-8"))
    if r0.get("state") != "completed_verified": errors.append("A8-R0 not completed_verified")
    if r0.get("merge_commit") != EXPECTED_R0_MERGE: errors.append("A8-R0 merge mismatch")
    if r0.get("authority_outcome",{}).get("a8_activated") is not False: errors.append("A8-R0 must not activate A8")
    if r0.get("validation",{}).get("triggered_workflows_passed") != 23: errors.append("A8-R0 23/23 workflow evidence missing")

if not HANDOFF.is_file():
    errors.append("missing A8 current revalidation handoff")
else:
    text = HANDOFF.read_text(encoding="utf-8")
    required_phrases = (
        "PASS — READY_FOR_BOUNDED_A8_ACTIVATION",
        EXPECTED_SCOPE_SHA, EXPECTED_AUTHORITY_SHA,
        EXPECTED_PREIMPLEMENTATION_SHA, EXPECTED_COMPATIBILITY_SHA, EXPECTED_HISTORICAL_PLAN_SHA,
        EXPECTED_APP_PRODUCT_PREDECESSOR, EXPECTED_APP_CURRENT_MAIN, EXPECTED_AIOC_BASELINE, EXPECTED_R0_MERGE,
        "0006_a8_asset_foundations.json",
        "A8-R0 is not repeated",
        "55 historical path assumptions + 24 A8-R0 supplemental rows",
        "vehicle-profile-port.ts` is `CONFLICT_REQUIRES_REDESIGN",
        "D04 `authority-control` remains a placeholder",
        "D26 `downtime-projects` remains a placeholder",
        "exact 241-value shared Content Context registry remains checksum-bound",
        "must not reconstruct or seed the registry from memory or semantic extracts",
        "A6 remains the sole Action proposal/review/decision/atomic accepted-result authority",
        "A7 remains the combat timing/semantic-position/combat-event/combat-result/reconnect authority",
        "CAPP-06 renderer fit is presentation-only",
        "full Reality topology/laws/community features remain deferred",
        "releaseAuthorized=false",
        "deploymentAuthorized=false",
        "providerVendorPaidServiceAuthorized=false",
    )
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"revalidation handoff missing phrase: {phrase}")

if errors:
    raise SystemExit("STAGE-A-A8 CURRENT REVALIDATION: FAIL\n- " + "\n- ".join(errors))

print("STAGE-A-A8 CURRENT REVALIDATION: PASS")
print("historical_paths=55 supplemental_authority_rows=24 authority_rows=79")
print("current_scope_rows=102 create=62 reuse=30 reuse_context=7 wrap=2 modify_bounded=1")
print(f"scope_sha={EXPECTED_SCOPE_SHA} authority_sha={EXPECTED_AUTHORITY_SHA}")
print(f"app_product_predecessor={EXPECTED_APP_PRODUCT_PREDECESSOR} app_current_main={EXPECTED_APP_CURRENT_MAIN}")
print("next_migration=0006_a8_asset_foundations.json")
print("activation=READY_FOR_BOUNDED_A8_ACTIVATION release=false deployment=false provider_vendor_paid=false")
