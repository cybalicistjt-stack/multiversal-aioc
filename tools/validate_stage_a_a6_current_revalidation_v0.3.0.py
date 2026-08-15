from __future__ import annotations

import csv
import hashlib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/stage-a-a6"
SCOPE = BASE / "A6_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv"
HANDOFF = BASE / "STAGE_A_A6_CURRENT_REPOSITORY_REVALIDATION_v0.3.0.md"

EXPECTED_SCOPE_SHA = "b1c7a5bbd41c5e908c57bbda9f05c3661efb921cd6273ae97b0971fb16dbc084"
EXPECTED_RECOVERED_PACKAGE_SHA = "ca80319e0282821f19b7fa4f43e439107bc845f0ececfa2937c8bc5418152d00"
EXPECTED_HISTORICAL_PLAN_SHA = "3d00b8b6738bfce3b82a041236075fd59655900a46f7fbeb11d5160287a2e8b7"
EXPECTED_APP_PRODUCT_BASELINE = "89c045b3cf1e04cc906dafac0be2c28c003ae892"
EXPECTED_APP_CURRENT_MAIN = "29b583ec89a70929e68793964ce49b0ed4a080fa"
EXPECTED_A5_HANDOFF_PATH = "packages/contracts/src/a5/scene-session-handoff.ts"

errors: list[str] = []

if not SCOPE.is_file():
    errors.append("missing current A6 changed-path scope")
else:
    digest = hashlib.sha256(SCOPE.read_bytes()).hexdigest()
    if digest != EXPECTED_SCOPE_SHA:
        errors.append(f"scope sha mismatch: {digest}")
    rows = list(csv.DictReader(SCOPE.open(encoding="utf-8", newline="")))
    if len(rows) != 68:
        errors.append(f"scope rows {len(rows)} != 68")
    counts = Counter(row["Disposition"] for row in rows)
    expected_counts = Counter({"CREATE": 42, "REUSE": 24, "WRAP": 1, "MODIFY_BOUNDED": 1})
    if counts != expected_counts:
        errors.append(f"scope disposition counts unexpected: {dict(counts)}")

    paths = {row["Path"] for row in rows}
    required = {
        "database/migrations/0004_a6_action_approval.json",
        "packages/contracts/src/a6/action-proposal-port.ts",
        "packages/contracts/src/a6/action-validation-port.ts",
        "packages/contracts/src/a6/available-action-projection-port.ts",
        "packages/contracts/src/a6/decision-queue-port.ts",
        "packages/contracts/src/a6/action-decision-port.ts",
        "packages/contracts/src/a6/modification-diff-port.ts",
        "packages/contracts/src/a6/atomic-action-commit-port.ts",
        "packages/contracts/src/a6/action-projection-port.ts",
        "packages/contracts/src/a6/action-status-port.ts",
        "packages/contracts/src/a6/action-reconnect-port.ts",
        "packages/contracts/src/a6/gm-actor-action-port.ts",
        "packages/contracts/src/a6/proposal-approval-shared-adapter.ts",
        "packages/contracts/src/a6/action-result-handoff.ts",
        "apps/client-ui/src/a2/picker/**",
        "apps/client-ui/src/a2/inspector/**",
        "packages/contracts/src/a3/delegation-support-access.ts",
        "packages/contracts/src/a3/selected-context-receipt.ts",
        "packages/contracts/src/a3/workspace-entry-port.ts",
        "packages/contracts/src/a4/character-control-port.ts",
        "packages/contracts/src/a5/launch-snapshot-port.ts",
        EXPECTED_A5_HANDOFF_PATH,
        "packages/contracts/src/a5/session-repository-port.ts",
        "packages/contracts/src/session/authoritative-session-command-handler.ts",
        "packages/contracts/src/session/hidden-information-response-filter.ts",
        "packages/contracts/src/session/ordered-realtime-event-delivery.ts",
        "packages/contracts/src/session/checkpoint-reconnect-restoration.ts",
        "packages/entitlements/src/entitlement-service-port.ts",
        "apps/client-ui/src/a6/a6.authority-privacy.test.ts",
        "apps/client-ui/src/a6/a6.atomicity.test.ts",
        "apps/client-ui/src/a6/a6.recovery.test.ts",
        "apps/client-ui/src/a6/a6.a11y.test.tsx",
        "apps/client-ui/src/a6/a6.integration.test.tsx",
        "apps/client-ui/src/App.tsx",
    }
    missing = sorted(required - paths)
    if missing:
        errors.append(f"scope missing required current paths: {missing}")

    if any("<next>" in path for path in paths):
        errors.append("historical <next> migration placeholder remains in current scope")
    if any(path == "packages/contracts/src/a6/**" for path in paths):
        errors.append("historical broad a6 wildcard remains; current scope must enumerate contracts")
    destructive = [row for row in rows if row["Disposition"] in {"DELETE", "REWRITE", "REPLACE"}]
    if destructive:
        errors.append(f"destructive dispositions present: {destructive}")
    hidden_rows = [row for row in rows if row["Path"] == "packages/contracts/src/session/hidden-information-response-filter.ts"]
    if len(hidden_rows) != 1 or hidden_rows[0]["Disposition"] != "WRAP":
        errors.append("hidden-information filter must be exactly one WRAP row")

if not HANDOFF.is_file():
    errors.append("missing current A6 revalidation handoff")
else:
    text = HANDOFF.read_text(encoding="utf-8")
    required_phrases = (
        "PASS — READY_FOR_BOUNDED_A6_ACTIVATION",
        EXPECTED_SCOPE_SHA,
        EXPECTED_RECOVERED_PACKAGE_SHA,
        EXPECTED_HISTORICAL_PLAN_SHA,
        EXPECTED_APP_PRODUCT_BASELINE,
        EXPECTED_APP_CURRENT_MAIN,
        "0004_a6_action_approval.json",
        "A6-GAP-002 A2 not implemented | RESOLVED",
        "A6-GAP-003 A3 not implemented | RESOLVED",
        "A6-GAP-004 A4 not implemented | RESOLVED",
        "A6-GAP-005 A5 not implemented | RESOLVED + BOUNDARY STRENGTHENED",
        "`A5ToA6SessionHandoff.actionResolutionAuthority` is explicitly `false`",
        "generic hidden-information response filter still returns `hiddenEventCount`",
        "protected cardinality is inference-safe",
        "accepted result writes are all-or-none",
        "build meaningful slices before broad CI",
        "releaseAuthorized=false",
        "deploymentAuthorized=false",
    )
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"revalidation handoff missing phrase: {phrase}")

if errors:
    raise SystemExit("STAGE-A-A6 CURRENT REVALIDATION: FAIL\n- " + "\n- ".join(errors))

print("STAGE-A-A6 CURRENT REVALIDATION: PASS")
print("historical_actions=42 current_scope_rows=68 create=42 reuse=24 wrap=1 modify_bounded=1")
print(f"app_product_baseline={EXPECTED_APP_PRODUCT_BASELINE}")
print(f"app_current_main={EXPECTED_APP_CURRENT_MAIN}")
print("next_migration=0004_a6_action_approval.json")
print("activation=READY_FOR_BOUNDED_A6_ACTIVATION release=false deployment=false")
