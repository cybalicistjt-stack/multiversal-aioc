from __future__ import annotations

import csv
import hashlib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/stage-a-a5"
SCOPE = BASE / "A5_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv"
HANDOFF = BASE / "STAGE_A_A5_CURRENT_REPOSITORY_REVALIDATION_v0.3.0.md"
EXPECTED_SCOPE_SHA = "89082bb72bb8097e5f3066c0b88b158e94b3e5b2676bfb7865ff2580e494fd03"
EXPECTED_RECOVERED_PACKAGE_SHA = "fd5afc623feed86ea1af88cd915c881fe64b315f50032c2f2a28c92a936cf36e"
EXPECTED_HISTORICAL_PLAN_SHA = "72f6c3ee18a028734ba2112e4a921f28768368fd03059a63d8993d74f4a8561c"
EXPECTED_APP_BASELINE = "90f84cfd4b9f00be3eee560530560a6c3cc28ab6"

errors: list[str] = []

if not SCOPE.is_file():
    errors.append("missing current A5 changed-path scope")
else:
    digest = hashlib.sha256(SCOPE.read_bytes()).hexdigest()
    if digest != EXPECTED_SCOPE_SHA:
        errors.append(f"scope sha mismatch: {digest}")
    rows = list(csv.DictReader(SCOPE.open(encoding="utf-8", newline="")))
    if len(rows) != 57:
        errors.append(f"scope rows {len(rows)} != 57")
    counts = Counter(row["Disposition"] for row in rows)
    expected_counts = Counter({"CREATE": 42, "REUSE": 14, "MODIFY_BOUNDED": 1})
    if counts != expected_counts:
        errors.append(f"scope disposition counts unexpected: {dict(counts)}")
    paths = {row["Path"] for row in rows}
    required = {
        "database/migrations/0003_a5_campaign_scene.json",
        "apps/client-ui/src/a2/picker/**",
        "packages/contracts/src/a3/invitation-port.ts",
        "packages/contracts/src/a3/delegation-support-access.ts",
        "packages/contracts/src/a3/workspace-entry-port.ts",
        "packages/contracts/src/a4/character-control-port.ts",
        "packages/contracts/src/a4/character-scene-reference.ts",
        "packages/contracts/src/session/authoritative-session-command-handler.ts",
        "packages/contracts/src/session/ordered-realtime-event-delivery.ts",
        "packages/contracts/src/session/checkpoint-reconnect-restoration.ts",
        "packages/contracts/src/a5/launch-snapshot-port.ts",
        "packages/contracts/src/a5/launch-session-port.ts",
        "packages/contracts/src/a5/scene-session-handoff.ts",
        "apps/client-ui/src/a5/a5.privacy-recovery.test.ts",
        "apps/client-ui/src/a5/a5.a11y.test.tsx",
        "apps/client-ui/src/a5/a5.integration.test.tsx",
        "apps/client-ui/src/App.tsx",
    }
    missing = sorted(required - paths)
    if missing:
        errors.append(f"scope missing required current paths: {missing}")
    if any("<next>" in path for path in paths):
        errors.append("historical <next> migration placeholder remains in current scope")
    if any(path == "database/migrations/0002_character_workspace.json" for path in paths if next((r["Disposition"] for r in rows if r["Path"] == path), "") == "CREATE"):
        errors.append("A5 may not recreate A4 migration 0002")

if not HANDOFF.is_file():
    errors.append("missing current A5 revalidation handoff")
else:
    text = HANDOFF.read_text(encoding="utf-8")
    required_phrases = (
        "PASS — READY_FOR_BOUNDED_A5_ACTIVATION",
        EXPECTED_SCOPE_SHA,
        EXPECTED_RECOVERED_PACKAGE_SHA,
        EXPECTED_HISTORICAL_PLAN_SHA,
        EXPECTED_APP_BASELINE,
        "0003_a5_campaign_scene.json",
        "A5-GAP-003 A2 not implemented | RESOLVED",
        "A5-GAP-004 A3 not implemented | RESOLVED",
        "A5-GAP-005 A4 not implemented | RESOLVED",
        "PPIA-08 is `COMPLETED_VERIFIED`",
        "permission filtering occurs before protected reference lookup",
        "A5 stops at the launched Session shell; A6 owns action proposal/GM approval/result authority",
        "build meaningful slices before broad CI",
        "releaseAuthorized=false",
        "deploymentAuthorized=false",
    )
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"revalidation handoff missing phrase: {phrase}")

if errors:
    raise SystemExit("STAGE-A-A5 CURRENT REVALIDATION: FAIL\n- " + "\n- ".join(errors))

print("STAGE-A-A5 CURRENT REVALIDATION: PASS")
print("historical_actions=40 current_scope_rows=57 create=42 reuse=14 modify_bounded=1")
print(f"app_baseline={EXPECTED_APP_BASELINE}")
print("next_migration=0003_a5_campaign_scene.json")
print("activation=READY_FOR_BOUNDED_A5_ACTIVATION release=false deployment=false")
