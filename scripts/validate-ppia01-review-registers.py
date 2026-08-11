#!/usr/bin/env python3
"""Validate PPIA-01 durable review registers against deterministic triage output."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "governance/application-planning/parallel-preimplementation"
UNRESOLVED = PROGRAM / "PPIA-01_UNRESOLVED_SOURCE_REGISTER.json"
REVIEW_MD = PROGRAM / "PPIA-01_INFERENCE_THIN_CONTENT_REVIEW_REGISTER.md"
OWNER_MD = PROGRAM / "PPIA-01_OWNER_EYE_QUANTUM_WEAVER.md"
P1_REVIEW = PROGRAM / "PPIA-01_P1_CORE_MECHANICAL_SOURCE_REVIEW_v0.1.0.json"
R1_RECOVERY = PROGRAM / "PPIA-01_8E-008G-R1_RECOVERY_CLOSURE.md"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--triage", required=True)
    args = parser.parse_args()

    triage = json.loads(Path(args.triage).read_text(encoding="utf-8"))
    unresolved = json.loads(UNRESOLVED.read_text(encoding="utf-8"))
    p1_review = json.loads(P1_REVIEW.read_text(encoding="utf-8"))
    review = REVIEW_MD.read_text(encoding="utf-8")
    owner = OWNER_MD.read_text(encoding="utf-8")
    r1 = R1_RECOVERY.read_text(encoding="utf-8")

    if triage.get("format") != "multiversal-ppia01-inference-thin-content-triage" or triage.get("version") != "0.3.0":
        raise SystemExit("unexpected triage identity/version")
    expected = {
        "inferenceEstimateRows": 10594,
        "delegatedBalanceEstimateRows": 8554,
        "delegatedMissingFieldCompletionRows": 370,
        "delegatedMetadataInferenceRows": 403,
        "systematicMagicCompletionRows": 385,
        "systematicBaseEngineeringCompletionRows": 350,
        "mechanicalInterpretationReviewRows": 531,
        "p1HighCoreMechanicalRows": 36,
        "p2SubstantiveCoreMechanicalRows": 73,
        "p3BoundedCoreMechanicalRows": 183,
        "p4LifecycleMetadataOnlyRows": 239,
        "sourceRecoveryReviewRows": 1,
        "structuralBlankRows": 33,
        "structuralBlankCells": 76,
    }
    s = triage.get("summary") or {}
    if s != expected:
        raise SystemExit(f"triage summary changed: {s}")

    candidates = triage.get("ownerAttentionCandidates") or []
    if len(candidates) != 1 or candidates[0].get("name") != "Quantum Weaver" or candidates[0].get("sourceRow") != 9:
        raise SystemExit("Quantum Weaver historical triage identity changed")
    if candidates[0].get("priority") != "P0-owner-eye-useful":
        raise SystemExit("Quantum Weaver historical priority changed")

    if len(triage.get("p1HighCoreMechanicalReview") or []) != 36:
        raise SystemExit("P1 high-core queue count changed")
    if len(triage.get("p2SubstantiveCoreMechanicalReview") or []) != 73:
        raise SystemExit("P2 substantive-core queue count changed")
    if len(triage.get("p3BoundedCoreMechanicalReview") or []) != 183:
        raise SystemExit("P3 bounded-core queue count changed")
    if len(triage.get("p4LifecycleMetadataOnlyReview") or []) != 239:
        raise SystemExit("P4 lifecycle/metadata queue count changed")

    if unresolved.get("format") != "multiversal-ppia01-unresolved-source-register" or unresolved.get("version") != "0.1.3":
        raise SystemExit("unexpected unresolved-source register identity/version")
    summary = unresolved.get("summary") or {}
    expected_summary = {
        "current_registry_owner_eye_records": 0,
        "owner_resolved_authored_completion_records": 1,
        "current_registry_source_unspecified_capacity_records": 7,
        "current_registry_source_reference_only_records": 3,
        "historical_provenance_audit_questions": 0,
        "historical_provenance_closures_recovered": 1,
        "current_registry_explicit_high_priority_gaps_without_closure": 0,
    }
    if summary != expected_summary:
        raise SystemExit(f"unresolved-source summary changed: {summary}")

    owner_resolutions = unresolved.get("owner_resolutions") or []
    if len(owner_resolutions) != 1 or owner_resolutions[0].get("id") != "PPIA-01-USR-001":
        raise SystemExit("Quantum Weaver owner resolution missing")

    records = {item["id"]: item for item in unresolved.get("records") or []}
    if set(records) != {"PPIA-01-USR-002", "PPIA-01-USR-003"}:
        raise SystemExit(f"current unresolved record set changed: {sorted(records)}")
    if records["PPIA-01-USR-002"].get("records") != [
        "Laser Sniper Rifle", "Plasma Rifle", "Plasma Shotgun", "Ion Blaster",
        "Handheld Laser", "Plasma Pistol", "Sonic Rifle",
    ]:
        raise SystemExit("capacity-source limitation record set changed")
    source_only_names = [item["name"] for item in records["PPIA-01-USR-003"].get("records") or []]
    if source_only_names != ["Energy Sniper Rifle", "Plasma Carbine", "Cryo Blaster"]:
        raise SystemExit("ammo-reference-only record set changed")

    provenance = unresolved.get("provenance_resolutions") or []
    if len(provenance) != 1 or provenance[0].get("id") != "PPIA-01-USR-004":
        raise SystemExit("R1 provenance resolution missing")
    resolution = provenance[0]
    if resolution.get("owner_supplied_wrapper_sha256") != "daa8d2eed1d23400812c8a003fbee5c6680041227d42dc90555ebc2031715a18":
        raise SystemExit("R1 recovered wrapper hash changed")
    result = resolution.get("closure_result") or {}
    expected_r1 = {
        "status": "PASS",
        "acceptance_checks": 101,
        "acceptance_checks_passed": 101,
        "structural_candidates_accounted": 7144,
        "formerly_unbound_candidates_closed": 2766,
        "unbound_source_sections_remaining": 0,
        "authoritative_records_provenance_accounted": 158189,
        "authoritative_records_unaccounted": 0,
        "foundational_inventory_records_accounted": 1347,
        "canonical_page_bindings_added": 254,
        "supporting_or_layout_dispositions": 841,
        "formally_deferred_candidates": 1671,
        "deferred_domain_candidates": 447,
        "deferred_unclassified_candidates": 1224,
    }
    if result != expected_r1:
        raise SystemExit(f"R1 closure result changed: {result}")

    for phrase in (
        "10,594", "P1 high-core", "36", "P2 substantive-core", "73",
        "P3 bounded-core", "183", "P4 lifecycle/metadata-only", "239",
        "Quantum Weaver", "STAGE-A-A2", "SD-1007", "SD-1107",
    ):
        if phrase not in review:
            raise SystemExit(f"review register missing required phrase {phrase!r}")

    if "feeds on energy fields and needs exposure to power sources" not in owner:
        raise SystemExit("Quantum Weaver note lost source-supported core fact")
    if "RESOLVED — OWNER-APPROVED AUTHORED COMPLETION" not in owner:
        raise SystemExit("Quantum Weaver owner resolution is not recorded")
    if "does **not** retroactively turn them into source-derived facts" not in owner:
        raise SystemExit("Quantum Weaver source/authored distinction is missing")

    for phrase in ("101 acceptance checks", "7,144 / 7,144", "1,671 candidates", "93 creature candidates"):
        if phrase not in r1:
            raise SystemExit(f"R1 recovery note missing {phrase!r}")

    if p1_review.get("format") != "multiversal-ppia01-p1-core-mechanical-source-review" or p1_review.get("version") != "0.1.0":
        raise SystemExit("unexpected P1 source-review identity/version")
    p1_summary = p1_review.get("summary") or {}
    if p1_summary.get("p1_high_core_rows_reviewed") != 36 or p1_summary.get("source_conflicts_found") != 1:
        raise SystemExit("P1 source-review summary changed")
    combat = next((g for g in p1_review.get("groups") or [] if g.get("group_id") == "PPIA-01-P1-ADVANCED-COMBAT-ITEMS"), None)
    taser = next((x for x in (combat or {}).get("record_dispositions", []) if x.get("name") == "Taser"), None)
    if not taser or taser.get("finding") != "source_conflict_two_published_variants" or "Do not auto-merge" not in taser.get("recommendation", ""):
        raise SystemExit("Taser source-variant conflict is not preserved")

    boundaries = unresolved.get("boundaries") or {}
    for key in (
        "raw_csv_modified", "automatic_identity_merge_authorized", "source_absence_may_be_filled_as_source_fact",
        "historical_2766_candidates_are_current_missing_mechanics", "formal_deferral_is_public_canon_completion",
        "canonical_promotion_authorized_by_this_register",
    ):
        if boundaries.get(key) is not False:
            raise SystemExit(f"unresolved register violates boundary {key}")

    print(json.dumps({
        "inferenceEstimateRows": 10594,
        "ownerEyeRecords": 0,
        "ownerResolvedAuthoredCompletions": 1,
        "historicalProvenanceQuestions": 0,
        "historicalProvenanceClosuresRecovered": 1,
        "r1AcceptanceChecksPassed": 101,
        "r1UnboundSourceSectionsRemaining": 0,
        "result": "PASS",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
