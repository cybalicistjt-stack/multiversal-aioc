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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--triage", required=True)
    args = parser.parse_args()

    triage = json.loads(Path(args.triage).read_text(encoding="utf-8"))
    unresolved = json.loads(UNRESOLVED.read_text(encoding="utf-8"))
    p1_review = json.loads(P1_REVIEW.read_text(encoding="utf-8"))
    review = REVIEW_MD.read_text(encoding="utf-8")
    owner = OWNER_MD.read_text(encoding="utf-8")

    if triage.get("format") != "multiversal-ppia01-inference-thin-content-triage" or triage.get("version") != "0.3.0":
        raise SystemExit("unexpected triage identity/version")
    s = triage["summary"]
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
    if s != expected:
        raise SystemExit(f"triage summary changed: {s}")

    if len(triage.get("ownerAttentionCandidates") or []) != 1:
        raise SystemExit("expected exactly one owner-eye candidate")
    quantum = triage["ownerAttentionCandidates"][0]
    if quantum.get("name") != "Quantum Weaver" or quantum.get("sourceRow") != 9:
        raise SystemExit("Quantum Weaver owner-eye identity changed")
    if quantum.get("priority") != "P0-owner-eye-useful":
        raise SystemExit("Quantum Weaver priority changed")

    p1_rows = triage.get("p1HighCoreMechanicalReview") or []
    if len(p1_rows) != 36:
        raise SystemExit("P1 high-core queue count changed")
    if len(triage.get("p2SubstantiveCoreMechanicalReview") or []) != 73:
        raise SystemExit("P2 substantive-core queue count changed")
    if len(triage.get("p3BoundedCoreMechanicalReview") or []) != 183:
        raise SystemExit("P3 bounded-core queue count changed")
    if len(triage.get("p4LifecycleMetadataOnlyReview") or []) != 239:
        raise SystemExit("P4 lifecycle/metadata queue count changed")

    if unresolved.get("format") != "multiversal-ppia01-unresolved-source-register" or unresolved.get("version") != "0.1.1":
        raise SystemExit("unexpected unresolved-source register identity/version")
    summary = unresolved.get("summary") or {}
    if summary != {
        "current_registry_owner_eye_records": 1,
        "current_registry_source_unspecified_capacity_records": 7,
        "current_registry_source_reference_only_records": 3,
        "historical_provenance_audit_questions": 1,
        "current_registry_explicit_high_priority_gaps_without_closure": 0,
    }:
        raise SystemExit(f"unresolved-source summary changed: {summary}")

    records = {item["id"]: item for item in unresolved.get("records") or []}
    if set(records) != {"PPIA-01-USR-001", "PPIA-01-USR-002", "PPIA-01-USR-003", "PPIA-01-USR-004"}:
        raise SystemExit("unresolved-source record set changed")
    if records["PPIA-01-USR-001"].get("name") != "Quantum Weaver":
        raise SystemExit("unresolved register lost Quantum Weaver")
    if records["PPIA-01-USR-002"].get("records") != [
        "Laser Sniper Rifle",
        "Plasma Rifle",
        "Plasma Shotgun",
        "Ion Blaster",
        "Handheld Laser",
        "Plasma Pistol",
        "Sonic Rifle",
    ]:
        raise SystemExit("capacity-source limitation record set changed")
    source_only_names = [item["name"] for item in records["PPIA-01-USR-003"].get("records") or []]
    if source_only_names != ["Energy Sniper Rifle", "Plasma Carbine", "Cryo Blaster"]:
        raise SystemExit("ammo-reference-only record set changed")

    historical = records["PPIA-01-USR-004"]
    package = historical.get("historical_package_evidence") or {}
    if package.get("exact_package_name") != "Multiversal_8E-008G-R1_Source_Boundary_and_Provenance_Closure_v0.1.0":
        raise SystemExit("historical R1 package identity changed")
    if package.get("historical_container_name") != "Aaac (1).zip":
        raise SystemExit("historical R1 container identity changed")
    if historical.get("historical_result", {}).get("candidates_without_formal_disposition") != 2766:
        raise SystemExit("historical 8E-008G blocker count changed")
    if historical.get("blocking") is not False or historical.get("current_registry_gap_count") != 0:
        raise SystemExit("historical provenance question was incorrectly promoted into a current CSV blocker")

    required_review_phrases = [
        "10,594",
        "P1 high-core",
        "36",
        "P2 substantive-core",
        "73",
        "P3 bounded-core",
        "183",
        "P4 lifecycle/metadata-only",
        "239",
        "Quantum Weaver",
        "Aaac (1).zip",
        "STAGE-A-A2",
        "SD-1007",
        "SD-1107",
    ]
    for phrase in required_review_phrases:
        if phrase not in review:
            raise SystemExit(f"review register missing required phrase {phrase!r}")

    if "feeds on energy fields and needs exposure to power sources" not in owner:
        raise SystemExit("Quantum Weaver owner-eye note lost exact source-supported core fact")
    if "OPTIONAL OWNER REVIEW — NOT A BLOCKER" not in owner:
        raise SystemExit("Quantum Weaver owner-eye note incorrectly changed its blocking status")

    if p1_review.get("format") != "multiversal-ppia01-p1-core-mechanical-source-review" or p1_review.get("version") != "0.1.0":
        raise SystemExit("unexpected P1 source-review identity/version")
    p1_policy = p1_review.get("policy") or {}
    if p1_policy.get("preserve_raw_csv") is not True or p1_policy.get("automatic_identity_merge") is not False:
        raise SystemExit("P1 source review violates raw-source/identity boundary")
    if p1_policy.get("source_facts_distinct_from_recommendations") is not True:
        raise SystemExit("P1 source review collapses recommendations into source facts")
    if p1_policy.get("owner_review_required") is not False or p1_policy.get("later_balance_review") != "PPIA-11":
        raise SystemExit("P1 source-review owner/balance routing changed")

    triage_p1 = {(row["dataset"], row["name"]) for row in p1_rows}
    reviewed_p1: set[tuple[str, str]] = set()
    for group in p1_review.get("groups") or []:
        dataset = group.get("dataset")
        names = group.get("records") or []
        if group.get("count") != len(names):
            raise SystemExit(f"P1 group count mismatch for {group.get('group_id')}")
        for name in names:
            key = (dataset, name)
            if key in reviewed_p1:
                raise SystemExit(f"duplicate P1 source-review identity {key}")
            reviewed_p1.add(key)
    if reviewed_p1 != triage_p1:
        raise SystemExit(
            f"P1 source-review coverage mismatch missing={sorted(triage_p1-reviewed_p1)} extra={sorted(reviewed_p1-triage_p1)}"
        )

    p1_summary = p1_review.get("summary") or {}
    if p1_summary != {
        "p1_high_core_rows_reviewed": 36,
        "explicit_core_source_support_rows": 26,
        "narrative_seed_only_rows": 7,
        "source_fusion_core_support_rows": 3,
        "source_conflicts_found": 1,
        "automatic_identity_merges": 0,
        "raw_csv_rows_modified": 0,
        "owner_blockers": 0,
    }:
        raise SystemExit(f"P1 source-review summary changed: {p1_summary}")

    combat_group = next(group for group in p1_review["groups"] if group["group_id"] == "PPIA-01-P1-ADVANCED-COMBAT-ITEMS")
    taser = next(item for item in combat_group["record_dispositions"] if item["name"] == "Taser")
    if taser.get("finding") != "source_conflict_two_published_variants":
        raise SystemExit("Taser source-conflict finding disappeared")
    if "Do not auto-merge" not in taser.get("recommendation", ""):
        raise SystemExit("Taser source-conflict recommendation no longer preserves identity boundary")

    boundaries = unresolved.get("boundaries") or {}
    if boundaries.get("raw_csv_modified") is not False:
        raise SystemExit("unresolved register claims raw CSV mutation")
    if boundaries.get("historical_2766_candidates_are_current_missing_mechanics") is not False:
        raise SystemExit("historical 2,766 candidates were incorrectly promoted into current missing mechanics")
    if boundaries.get("canonical_promotion_authorized_by_this_register") is not False:
        raise SystemExit("review register incorrectly authorizes canonical promotion")

    print(json.dumps({
        "triageVersion": triage["version"],
        "inferenceEstimateRows": s["inferenceEstimateRows"],
        "p1HighCoreMechanicalRows": s["p1HighCoreMechanicalRows"],
        "p1SourceReviewedRows": p1_summary["p1_high_core_rows_reviewed"],
        "sourceConflictsFound": p1_summary["source_conflicts_found"],
        "ownerEyeRecords": summary["current_registry_owner_eye_records"],
        "historicalProvenanceQuestions": summary["historical_provenance_audit_questions"],
        "result": "PASS",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
