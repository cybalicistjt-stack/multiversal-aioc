from __future__ import annotations

import csv
import hashlib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/stage-a-a7"
SCOPE = BASE / "A7_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv"
HANDOFF = BASE / "STAGE_A_A7_CURRENT_REPOSITORY_REVALIDATION_v0.3.0.md"

EXPECTED_SCOPE_SHA = "e0643fce17d27d05d49a0c34389b189865a726957a6f12e9e167d59d72686517"
EXPECTED_RECOVERED_PREIMPLEMENTATION_SHA = "752020c7e5f7fd328fac9ee075865fc69dbd4c425440c31697a94dc12860307a"
EXPECTED_RECOVERED_COMPATIBILITY_SHA = "8bfcddd2d97c73c7dd298404dd03492313a47fc67a86ddf72286c8818cb7b6b2"
EXPECTED_HISTORICAL_PLAN_SHA = "e38bcd8bd50c1fe394a89b04b12118daf7fe4d86c06f98a3550738eb20faf6af"
EXPECTED_APP_PRODUCT_PREDECESSOR = "79425943f25cce347abcfd2c0abb721005d7a772"
EXPECTED_APP_CURRENT_MAIN = "6272a19d09145f4a3e76af74f00f8733a13301f9"
EXPECTED_ROWS = 95
EXPECTED_COUNTS = Counter({"CREATE": 47, "REUSE": 45, "WRAP": 2, "MODIFY_BOUNDED": 1})

A7_CONTRACT_PATHS = [
    "packages/contracts/src/a7/combat-encounter-port.ts",
    "packages/contracts/src/a7/combat-participant-port.ts",
    "packages/contracts/src/a7/combat-controller-assignment-port.ts",
    "packages/contracts/src/a7/combat-order-timing-port.ts",
    "packages/contracts/src/a7/combat-action-adapter.ts",
    "packages/contracts/src/a7/combat-targeting-port.ts",
    "packages/contracts/src/a7/combat-position-port.ts",
    "packages/contracts/src/a7/combat-cost-reservation-port.ts",
    "packages/contracts/src/a7/combat-effect-processor-port.ts",
    "packages/contracts/src/a7/combat-condition-port.ts",
    "packages/contracts/src/a7/combat-reaction-port.ts",
    "packages/contracts/src/a7/combat-hazard-environment-port.ts",
    "packages/contracts/src/a7/combat-outcome-port.ts",
    "packages/contracts/src/a7/combat-completion-port.ts",
    "packages/contracts/src/a7/combat-atomic-result-coordinator.ts",
    "packages/contracts/src/a7/combat-projection-port.ts",
    "packages/contracts/src/a7/combat-event-port.ts",
    "packages/contracts/src/a7/combat-reconnect-port.ts",
    "packages/contracts/src/a7/encounter-bootstrap-port.ts",
    "packages/contracts/src/a7/combat-history-export-port.ts",
]

errors: list[str] = []

if not SCOPE.is_file():
    errors.append("missing current A7 changed-path scope")
else:
    digest = hashlib.sha256(SCOPE.read_bytes()).hexdigest()
    if digest != EXPECTED_SCOPE_SHA:
        errors.append(f"scope sha mismatch: {digest}")
    rows = list(csv.DictReader(SCOPE.open(encoding="utf-8", newline="")))
    if len(rows) != EXPECTED_ROWS:
        errors.append(f"scope rows {len(rows)} != {EXPECTED_ROWS}")
    counts = Counter(row["Disposition"] for row in rows)
    if counts != EXPECTED_COUNTS:
        errors.append(f"scope disposition counts unexpected: {dict(counts)}")

    paths = [row["Path"] for row in rows]
    path_set = set(paths)
    if len(paths) != len(path_set):
        errors.append("scope contains duplicate paths")

    required = set(A7_CONTRACT_PATHS) | {
        "database/migrations/0005_a7_combat_runtime.json",
        "packages/contracts/src/a7/runtime-utilities.ts",
        "packages/contracts/src/a6/action-result-handoff.ts",
        "packages/contracts/src/a6/action-proposal-port.ts",
        "packages/contracts/src/a6/action-validation-port.ts",
        "packages/contracts/src/a6/action-decision-port.ts",
        "packages/contracts/src/a6/atomic-action-commit-port.ts",
        "packages/contracts/src/a6/action-status-port.ts",
        "packages/contracts/src/a6/action-reconnect-port.ts",
        "packages/contracts/src/a6/action-event-port.ts",
        "packages/contracts/src/a6/action-projection-port.ts",
        "packages/contracts/src/a6/gm-actor-action-port.ts",
        "apps/client-ui/src/a2/picker/**",
        "apps/client-ui/src/a2/inspector/**",
        "packages/contracts/src/a3/stable-subject-session-port.ts",
        "packages/contracts/src/a3/delegation-support-access.ts",
        "packages/contracts/src/a3/selected-context-receipt.ts",
        "packages/contracts/src/a3/workspace-entry-port.ts",
        "packages/contracts/src/a4/character-control-port.ts",
        "packages/contracts/src/a4/character-repository-port.ts",
        "packages/contracts/src/a4/character-projection-port.ts",
        "packages/contracts/src/a5/launch-snapshot-port.ts",
        "packages/contracts/src/a5/session-repository-port.ts",
        "packages/contracts/src/a5/scene-session-handoff.ts",
        "packages/contracts/src/a5/authorization-projection-port.ts",
        "packages/contracts/src/session/authoritative-session-command-handler.ts",
        "packages/contracts/src/session/hidden-information-response-filter.ts",
        "packages/contracts/src/session/ordered-realtime-event-delivery.ts",
        "packages/contracts/src/session/checkpoint-reconnect-restoration.ts",
        "packages/contracts/src/observability/structured-audit-telemetry.ts",
        "packages/entitlements/src/entitlement-service-port.ts",
        "packages/contracts/src/combat-initiative/README.md",
        "apps/client-ui/src/a7/a7.contract.test.ts",
        "apps/client-ui/src/a7/a7.targeting-position.test.ts",
        "apps/client-ui/src/a7/a7.atomicity.test.ts",
        "apps/client-ui/src/a7/a7.reactions.test.ts",
        "apps/client-ui/src/a7/a7.authority-privacy.test.ts",
        "apps/client-ui/src/a7/a7.recovery.test.ts",
        "apps/client-ui/src/a7/a7.a11y.test.tsx",
        "apps/client-ui/src/a7/a7.integration.test.tsx",
        "apps/client-ui/src/App.tsx",
        "tools/verify_stage_a_a7.py",
        ".github/workflows/validate-stage-a-a7-full-combat.yml",
        "docs/evidence/stage-a-a7/**",
        "receipts/STAGE-A-A7-CLOSURE.json",
    }
    missing = sorted(required - path_set)
    if missing:
        errors.append(f"scope missing required current paths: {missing}")

    if any("<next>" in path for path in path_set):
        errors.append("historical <next> migration placeholder remains in current scope")
    forbidden_broad = {
        "packages/contracts/src/a6/**",
        "packages/contracts/src/a4/**",
        "apps/client-ui/src/a2/**",
        "tests/a7/**",
    }
    broad = sorted(forbidden_broad & path_set)
    if broad:
        errors.append(f"historical broad/disconnected paths remain: {broad}")

    destructive = [row for row in rows if row["Disposition"] in {"DELETE", "REWRITE", "REPLACE"}]
    if destructive:
        errors.append(f"destructive dispositions present: {destructive}")

    wrap_paths = {row["Path"] for row in rows if row["Disposition"] == "WRAP"}
    expected_wrap_paths = {
        "packages/contracts/src/session/authoritative-session-command-handler.ts",
        "packages/contracts/src/session/hidden-information-response-filter.ts",
    }
    if wrap_paths != expected_wrap_paths:
        errors.append(f"A7 wrapper set unexpected: {sorted(wrap_paths)}")

    if any(row["Disposition"] != "CREATE" for row in rows if row["Path"] in A7_CONTRACT_PATHS):
        errors.append("all 20 provider-neutral A7 contract paths must be CREATE")

    placeholder = [row for row in rows if row["Path"] == "packages/contracts/src/combat-initiative/README.md"]
    if len(placeholder) != 1 or placeholder[0]["Disposition"] != "REUSE" or "placeholder" not in placeholder[0]["Purpose"].lower():
        errors.append("WP-006 combat-initiative placeholder must remain REUSE context only")

if not HANDOFF.is_file():
    errors.append("missing current A7 revalidation handoff")
else:
    text = HANDOFF.read_text(encoding="utf-8")
    required_phrases = (
        "PASS — READY_FOR_BOUNDED_A7_ACTIVATION",
        EXPECTED_SCOPE_SHA,
        EXPECTED_RECOVERED_PREIMPLEMENTATION_SHA,
        EXPECTED_RECOVERED_COMPATIBILITY_SHA,
        EXPECTED_HISTORICAL_PLAN_SHA,
        EXPECTED_APP_PRODUCT_PREDECESSOR,
        EXPECTED_APP_CURRENT_MAIN,
        "0005_a7_combat_runtime.json",
        "A7-GAP-003 A2 not implemented | RESOLVED",
        "A7-GAP-004 A3 not implemented | RESOLVED",
        "A7-GAP-005 A4 not implemented | RESOLVED",
        "A7-GAP-006 A5 not implemented | RESOLVED",
        "A7-GAP-007 A6 not implemented | RESOLVED + BOUNDARY STRENGTHENED",
        "`resultAuthoritative: true` and `combatBreadthAuthority: false`",
        "full command payload in a public `command.accepted:*` Event",
        "generic hidden-information response filter still returns `hiddenEventCount`",
        "A6 remains the sole Action proposal/GM review/approve-deny-modify/decision receipt/atomic accepted-result authority",
        "reaction/interrupt claims are advisory until accepted",
        "zero Resource is never universal death",
        "does not itself grant loot, Assets, XP, advancement, faction standing or canonical changes",
        "build meaningful bounded slices before broad CI",
        "releaseAuthorized=false",
        "deploymentAuthorized=false",
        "providerVendorPaidServiceAuthorized=false",
    )
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"revalidation handoff missing phrase: {phrase}")

if errors:
    raise SystemExit("STAGE-A-A7 CURRENT REVALIDATION: FAIL\n- " + "\n- ".join(errors))

print("STAGE-A-A7 CURRENT REVALIDATION: PASS")
print("historical_actions=46 current_scope_rows=95 create=47 reuse=45 wrap=2 modify_bounded=1")
print(f"app_product_predecessor={EXPECTED_APP_PRODUCT_PREDECESSOR}")
print(f"app_current_main={EXPECTED_APP_CURRENT_MAIN}")
print("next_migration=0005_a7_combat_runtime.json")
print("activation=READY_FOR_BOUNDED_A7_ACTIVATION release=false deployment=false provider_vendor_paid=false")
