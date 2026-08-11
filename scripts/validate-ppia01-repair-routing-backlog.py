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
QUANTUM = PROGRAM / "PPIA-01_OWNER_EYE_QUANTUM_WEAVER.md"
R1_RECOVERY = PROGRAM / "PPIA-01_8E-008G-R1_RECOVERY_CLOSURE.md"


def main() -> int:
    backlog = json.loads(BACKLOG.read_text(encoding="utf-8"))
    unresolved = json.loads(UNRESOLVED.read_text(encoding="utf-8"))
    p1_review = json.loads(P1_REVIEW.read_text(encoding="utf-8"))
    quantum = QUANTUM.read_text(encoding="utf-8")
    r1 = R1_RECOVERY.read_text(encoding="utf-8")

    if backlog.get("format") != "multiversal-ppia01-repair-and-routing-backlog":
        raise SystemExit("unexpected repair/routing backlog format")
    if backlog.get("version") != "0.1.0" or backlog.get("work_item") != "PPIA-01":
        raise SystemExit("repair/routing backlog identity mismatch")

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
        if item.get("count") != count or item.get("status") != status or not item.get("evidence"):
            raise SystemExit(f"completed backlog mismatch for {item_id}: {item}")

    routes = {item["id"]: item for item in backlog.get("routed_followup") or []}
    expected_counts = {
        "PPIA-01-RTE-001": 1, "PPIA-01-RTE-002": 1, "PPIA-01-RTE-003": 73,
        "PPIA-01-RTE-004": 183, "PPIA-01-RTE-005": 239, "PPIA-01-RTE-006": 385,
        "PPIA-01-RTE-007": 350, "PPIA-01-RTE-008": 8554, "PPIA-01-RTE-009": 370,
        "PPIA-01-RTE-010": 403, "PPIA-01-RTE-011": 7, "PPIA-01-RTE-012": 3,
        "PPIA-01-RTE-013": 1,
    }
    if set(routes) != set(expected_counts):
        raise SystemExit("repair/routing follow-up set changed")
    for route_id, count in expected_counts.items():
        route = routes[route_id]
        if route.get("count") != count or not route.get("destination") or not route.get("status") or not route.get("required_behavior"):
            raise SystemExit(f"route mismatch for {route_id}")

    if routes["PPIA-01-RTE-002"].get("status") != "owner_approved_authored_completion":
        raise SystemExit("Quantum Weaver owner resolution is not frozen")
    if "OWNER-APPROVED AUTHORED COMPLETION" not in quantum or "does **not** retroactively turn them into source-derived facts" not in quantum:
        raise SystemExit("Quantum Weaver owner/source boundary is missing")

    routed_inference_count = sum(routes[item_id]["count"] for item_id in (
        "PPIA-01-RTE-003", "PPIA-01-RTE-004", "PPIA-01-RTE-005",
        "PPIA-01-RTE-006", "PPIA-01-RTE-007", "PPIA-01-RTE-008",
        "PPIA-01-RTE-009", "PPIA-01-RTE-010",
    ))
    if routed_inference_count + 36 + 1 != 10594:
        raise SystemExit("inference routing coverage mismatch")

    if p1_review.get("summary", {}).get("p1_high_core_rows_reviewed") != 36:
        raise SystemExit("P1 source review no longer covers 36 high-core rows")
    if p1_review.get("summary", {}).get("source_conflicts_found") != 1:
        raise SystemExit("P1 source review lost the single source conflict")
    combat = next((g for g in p1_review.get("groups") or [] if g.get("group_id") == "PPIA-01-P1-ADVANCED-COMBAT-ITEMS"), None)
    taser = next((x for x in (combat or {}).get("record_dispositions", []) if x.get("name") == "Taser"), None)
    if not taser or taser.get("finding") != "source_conflict_two_published_variants" or "Do not auto-merge" not in taser.get("recommendation", ""):
        raise SystemExit("Taser source-variant conflict is not preserved")

    summary = unresolved.get("summary") or {}
    if summary.get("current_registry_explicit_high_priority_gaps_without_closure") != 0:
        raise SystemExit("explicit high-priority current-registry gaps remain unresolved")
    if summary.get("current_registry_owner_eye_records") != 0 or summary.get("owner_resolved_authored_completion_records") != 1:
        raise SystemExit("Quantum Weaver resolution counts changed")
    if summary.get("current_registry_source_unspecified_capacity_records") != 7:
        raise SystemExit("source-unspecified capacity count changed")
    if summary.get("current_registry_source_reference_only_records") != 3:
        raise SystemExit("source-reference-only record count changed")
    if summary.get("historical_provenance_audit_questions") != 0 or summary.get("historical_provenance_closures_recovered") != 1:
        raise SystemExit("historical R1 closure state changed")

    provenance = unresolved.get("provenance_resolutions") or []
    if len(provenance) != 1 or provenance[0].get("id") != "PPIA-01-USR-004":
        raise SystemExit("historical R1 provenance resolution missing")
    closure = provenance[0].get("closure_result") or {}
    if closure.get("status") != "PASS" or closure.get("acceptance_checks_passed") != 101:
        raise SystemExit("R1 acceptance result changed")
    if closure.get("structural_candidates_accounted") != 7144 or closure.get("formerly_unbound_candidates_closed") != 2766:
        raise SystemExit("R1 structural closure counts changed")
    if closure.get("unbound_source_sections_remaining") != 0 or closure.get("formally_deferred_candidates") != 1671:
        raise SystemExit("R1 unbound/deferral counts changed")
    if "93 creature candidates" not in r1:
        raise SystemExit("R1 creature deferral routing is missing")

    trace = backlog.get("feature_surface_traceability") or {}
    if set(trace) != {"STAGE-A-A2", "SD-1007", "SD-1107"}:
        raise SystemExit(f"feature-surface traceability changed: {sorted(trace)}")

    boundaries = backlog.get("boundaries") or {}
    for key in (
        "raw_csv_modified", "application_runtime_mutation_authorized", "automatic_identity_merge_authorized",
        "a2_activation_authorized", "canonical_promotion_authorized", "release_authorized",
    ):
        if boundaries.get(key) is not False:
            raise SystemExit(f"repair/routing backlog violates boundary {key}")

    print(json.dumps({
        "completedEvidenceItems": len(completed),
        "routedFollowups": len(routes),
        "inferenceRowsAccounted": 10594,
        "explicitHighPriorityGapsWithoutClosure": 0,
        "ownerEyeRecords": 0,
        "ownerResolvedAuthoredCompletions": 1,
        "historicalProvenanceQuestions": 0,
        "historicalProvenanceClosuresRecovered": 1,
        "r1AcceptanceChecksPassed": 101,
        "p1SourceReviewed": 36,
        "sourceConflictsPreserved": 1,
        "result": "PASS",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
