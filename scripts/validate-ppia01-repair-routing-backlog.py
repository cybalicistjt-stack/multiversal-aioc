#!/usr/bin/env python3
"""Validate the durable PPIA-01 repair/routing backlog against governed closure evidence."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = PROGRAM / "PPIA-01_REPAIR_AND_ROUTING_BACKLOG.json"
UNRESOLVED = PROGRAM / "PPIA-01_UNRESOLVED_SOURCE_REGISTER.json"
P1_REVIEW = PROGRAM / "PPIA-01_P1_CORE_MECHANICAL_SOURCE_REVIEW_v0.1.0.json"


def main() -> int:
    backlog = json.loads(BACKLOG.read_text(encoding="utf-8"))
    unresolved = json.loads(UNRESOLVED.read_text(encoding="utf-8"))
    p1_review = json.loads(P1_REVIEW.read_text(encoding="utf-8"))

    if backlog.get("format") != "multiversal-ppia01-repair-and-routing-backlog":
        raise SystemExit("unexpected repair/routing backlog format")
    if backlog.get("version") != "0.1.0" or backlog.get("work_item") != "PPIA-01":
        raise SystemExit("repair/routing backlog identity mismatch")
    if backlog.get("status") not in {"closure_ready_pending_exact_head_validation", "complete_routed"}:
        raise SystemExit(f"invalid repair/routing status: {backlog.get('status')}")

    completed = {item["id"]: item for item in backlog.get("completed_in_ppia01") or []}
    expected_completed = {
        "PPIA-01-BL-001": (84, "governed_closure_complete"),
        "PPIA-01-BL-002": (36, "source_review_complete"),
        "PPIA-01-BL-003": (10594, "deterministically_classified_and_routed"),
        "PPIA-01-BL-004": (33, "classified"),
    }
    if set(completed) != set(expected_completed):
        raise SystemExit("repair/routing completed evidence set changed")
    for item_id, (count, status) in expected_completed.items():
        item = completed[item_id]
        if item.get("count") != count or item.get("status") != status:
            raise SystemExit(f"completed backlog mismatch for {item_id}: {item}")
        if not item.get("evidence"):
            raise SystemExit(f"completed backlog item {item_id} lacks evidence")

    routes = {item["id"]: item for item in backlog.get("routed_followup") or []}
    expected_counts = {
        "PPIA-01-RTE-001": 1,
        "PPIA-01-RTE-002": 1,
        "PPIA-01-RTE-003": 73,
        "PPIA-01-RTE-004": 183,
        "PPIA-01-RTE-005": 239,
        "PPIA-01-RTE-006": 385,
        "PPIA-01-RTE-007": 350,
        "PPIA-01-RTE-008": 8554,
        "PPIA-01-RTE-009": 370,
        "PPIA-01-RTE-010": 403,
        "PPIA-01-RTE-011": 7,
        "PPIA-01-RTE-012": 3,
        "PPIA-01-RTE-013": 1,
    }
    if set(routes) != set(expected_counts):
        raise SystemExit("repair/routing follow-up set changed")
    for route_id, count in expected_counts.items():
        route = routes[route_id]
        if route.get("count") != count:
            raise SystemExit(f"route count mismatch for {route_id}: {route.get('count')} != {count}")
        if not route.get("destination") or not route.get("status") or not route.get("required_behavior"):
            raise SystemExit(f"route {route_id} lacks required routing fields")

    # The P2/P3/P4 + systematic/delegated inference categories must account for
    # all inference-bearing rows except the single Quantum Weaver source-recovery row.
    routed_inference_count = sum(routes[item_id]["count"] for item_id in (
        "PPIA-01-RTE-003", "PPIA-01-RTE-004", "PPIA-01-RTE-005",
        "PPIA-01-RTE-006", "PPIA-01-RTE-007", "PPIA-01-RTE-008",
        "PPIA-01-RTE-009", "PPIA-01-RTE-010",
    ))
    # 36 P1 rows were source-reviewed in PPIA-01 itself; Quantum Weaver is the one P0 record.
    if routed_inference_count + 36 + 1 != 10594:
        raise SystemExit(
            f"inference routing coverage mismatch: routed={routed_inference_count}, P1=36, P0=1"
        )

    if p1_review.get("summary", {}).get("p1_high_core_rows_reviewed") != 36:
        raise SystemExit("P1 source review no longer covers 36 high-core rows")
    if p1_review.get("summary", {}).get("source_conflicts_found") != 1:
        raise SystemExit("P1 source review lost the single source conflict")
    combat_group = next(
        (group for group in p1_review.get("groups") or [] if group.get("group_id") == "PPIA-01-P1-ADVANCED-COMBAT-ITEMS"),
        None,
    )
    if not combat_group:
        raise SystemExit("P1 combat-item source-review group missing")
    taser = next((item for item in combat_group.get("record_dispositions") or [] if item.get("name") == "Taser"), None)
    if not taser or taser.get("finding") != "source_conflict_two_published_variants":
        raise SystemExit("Taser source-variant conflict is not preserved")
    if "Do not auto-merge" not in taser.get("recommendation", ""):
        raise SystemExit("Taser routing no longer preserves the identity boundary")

    unresolved_summary = unresolved.get("summary") or {}
    if unresolved_summary.get("current_registry_explicit_high_priority_gaps_without_closure") != 0:
        raise SystemExit("explicit high-priority current-registry gaps remain unresolved")
    if unresolved_summary.get("current_registry_owner_eye_records") != 1:
        raise SystemExit("owner-eye register count changed")
    if unresolved_summary.get("current_registry_source_unspecified_capacity_records") != 7:
        raise SystemExit("source-unspecified capacity count changed")
    if unresolved_summary.get("current_registry_source_reference_only_records") != 3:
        raise SystemExit("source-reference-only record count changed")
    if unresolved_summary.get("historical_provenance_audit_questions") != 1:
        raise SystemExit("historical provenance-question count changed")

    trace = backlog.get("feature_surface_traceability") or {}
    if set(trace) != {"STAGE-A-A2", "SD-1007", "SD-1107"}:
        raise SystemExit(f"feature-surface traceability changed: {sorted(trace)}")

    boundaries = backlog.get("boundaries") or {}
    required_false = (
        "raw_csv_modified",
        "application_runtime_mutation_authorized",
        "automatic_identity_merge_authorized",
        "a2_activation_authorized",
        "canonical_promotion_authorized",
        "release_authorized",
    )
    for key in required_false:
        if boundaries.get(key) is not False:
            raise SystemExit(f"repair/routing backlog violates boundary {key}")

    print(json.dumps({
        "completedEvidenceItems": len(completed),
        "routedFollowups": len(routes),
        "inferenceRowsAccounted": 10594,
        "explicitHighPriorityGapsWithoutClosure": 0,
        "p1SourceReviewed": 36,
        "sourceConflictsPreserved": 1,
        "result": "PASS",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
