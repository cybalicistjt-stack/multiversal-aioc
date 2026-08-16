#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/stage-a-a12/current-revalidation"
ACCOUNTING = BASE / "A12_CURRENT_REVALIDATION_SOURCE_ACCOUNTING.json"
VERDICT = BASE / "STAGE_A_A12_CURRENT_REPOSITORY_REVALIDATION.md"
CHECKPOINT = ROOT / "governance/ai/work-state/STAGE-A-A12-current-revalidation-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"

APP = "16c8018cc7ae06657cdcd3176d2ee16ad9edb36e"
A11 = "bf54f36737fe02041f02ab44a69f45c3b0b294ac"
PRE = "e0bd345664481063606a9399313b339e47e3f70fa46380ae885ad2127090fff5"
COMPAT = "f7e80038c26b94b5641ae9afc222c3f987776313fc636d45e94442f4cf149859"
SECURITY = "9d65ac51f6ffd9f9221b1c05ae52f46edbc31ec521e453e06e1f67f5f4498295"
REFERENCE = "bea56f266449f8b89d855bca9e36973c20c3dd95dfb79897fe1132c94df457f6"


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require_text(text: str, *markers: str) -> None:
    for marker in markers:
        assert marker in text, f"missing verdict marker: {marker}"


def main() -> int:
    a = read(ACCOUNTING)
    cp = read(CHECKPOINT)
    p = read(POINTER)
    text = VERDICT.read_text(encoding="utf-8")

    assert a["schema_version"] == "1.0.0"
    assert a["work_item_id"] == "STAGE-A-A12"
    assert a["application_baseline"] == APP
    assert a["verified_a11_product_merge"] == A11
    packages = a["historical_packages"]
    assert packages["STAGE_A_A12_INTERNAL_ALPHA_HARDENING_PREIMPLEMENTATION_v0.1.0.zip"] == PRE
    assert packages["STAGE_A_A12_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip"] == COMPAT
    assert packages["STAGE_A_GLOBAL_ADVERSARIAL_SECURITY_CORPUS_v0.1.0.zip"] == SECURITY
    assert packages["STAGE_A_TESTER_REFERENCE_CAMPAIGN_KIT_v0.1.0.zip"] == REFERENCE

    counts = a["source_counts"]
    expected = {
        "hardening_dimensions": 11,
        "runtime_performance_budget_rows": 9,
        "ia_d09_bounded_release_fixtures": 24,
        "ia_d09_implementation_queue_slices": 12,
        "a12_source_slices": 12,
        "a12_blocking_release_gates": 22,
        "owner_only_decision_gates": 8,
        "required_candidate_evidence_classes": 17,
        "security_threat_families": 30,
        "security_scenarios": 90,
        "security_evidence_classes": 15,
        "historical_gaps": 26,
        "planned_acceptance_contracts": 26,
        "historical_exact_path_actions": 66,
        "validation_ci_lanes": 37,
        "implementation_invariants": 40,
        "repository_compatibility_gates": 15,
    }
    assert counts == expected
    assert a["slice_ids"] == [f"A12-S{i:02d}" for i in range(1, 13)]
    assert a["blocking_release_gate_ids"] == [f"A12-GATE-{i:03d}" for i in range(1, 23)]
    assert len(a["owner_decision_gates"]) == 8
    assert len(a["required_candidate_evidence_classes"]) == 17
    assert len(a["planned_contracts"]) == 26
    assert a["planned_contracts"][0] == "CandidateBuildIdentity"
    assert a["planned_contracts"][-1] == "HardeningScopeRegistry"
    assert a["planned_contract_root"] == "packages/contracts/src/acceptance/"

    gaps = a["gap_revalidation"]
    assert gaps["SUPERSEDED"] == ["A12-GAP-002", "A12-GAP-005"]
    assert len(gaps["CHANGED"]) == 13
    assert len(gaps["STILL_VALID"]) == 11
    assert gaps["NEWLY_BLOCKED"] == []
    all_gap_ids = set(gaps["SUPERSEDED"] + gaps["CHANGED"] + gaps["STILL_VALID"])
    assert all_gap_ids == {f"A12-GAP-{i:03d}" for i in range(1, 27)}

    assert a["revalidation_verdict"] == "PASS_READY_FOR_BOUNDED_A12_ACTIVATION"
    for key in (
        "implementation_activated",
        "candidate_built_claimed",
        "candidate_validated_claimed",
        "release_approved_claimed",
        "tester_access_authorized",
        "real_user_data_authorized",
        "production_credentials_authorized",
        "paid_provider_authorized",
        "release_authorized",
        "deployment_authorized",
        "canonical_promotion_authorized",
    ):
        assert a[key] is False

    require_text(
        text,
        "PASS — READY FOR BOUNDED A12 ACTIVATION",
        "Implementation state:** **NOT ACTIVATED",
        APP,
        A11,
        PRE,
        COMPAT,
        SECURITY,
        REFERENCE,
        "2 superseded, 13 changed, 11 still valid, 0 newly blocked",
        "DT-006",
        "DT-007",
        "DT-008",
        "DT-009",
        "DT-010",
        "30-family / 90-scenario",
        "release_approved",
    )

    assert cp["work_item_id"] == "STAGE-A-A12"
    assert cp["attempt_id"] == "STAGE-A-A12-current-revalidation-attempt-001"
    assert cp["application_baseline"] == APP
    assert cp["verified_predecessor"]["implementation_merge_commit"] == A11
    assert cp["historical_preparation"]["source_slice_count"] == 12
    assert cp["historical_preparation"]["security_scenario_count"] == 90
    assert cp["revalidation_verdict"] == "PASS_READY_FOR_BOUNDED_A12_ACTIVATION"
    assert cp["restrictions"]["a12_activated"] is False
    assert cp["restrictions"]["a12_application_branch_created"] is False
    assert cp["restrictions"]["candidate_built_claimed"] is False
    assert cp["restrictions"]["candidate_validated_claimed"] is False
    assert cp["restrictions"]["release_approved"] is False

    assert p["primary_attempt_id"] == "STAGE-A-A12-current-revalidation-attempt-001"
    entry = next(x for x in p["active_attempts"] if x["attempt_id"] == p["primary_attempt_id"])
    assert entry["branch"] == cp["branch"]
    assert entry["status"] == cp["status"]
    assert entry["owner_selected"] is True

    print("STAGE-A-A12 CURRENT-REPOSITORY REVALIDATION: PASS")
    print("slices=12 release_gates=22 owner_gates=8 evidence_classes=17 security=30_families/90_scenarios gaps=26 contracts=26")
    print("gaps=2_superseded/13_changed/11_still_valid/0_newly_blocked")
    print("verdict=PASS_READY_FOR_BOUNDED_A12_ACTIVATION implementation_activated=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
