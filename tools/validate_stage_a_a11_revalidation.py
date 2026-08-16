#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/stage-a-a11/current-revalidation"
ACCOUNTING = BASE / "A11_CURRENT_REVALIDATION_SOURCE_ACCOUNTING.json"
VERDICT = BASE / "STAGE_A_A11_CURRENT_REPOSITORY_REVALIDATION.md"
CHECKPOINT = ROOT / "governance/ai/work-state/STAGE-A-A11-current-revalidation-attempt-001.json"

APP_BASELINE = "f023c7feab49910b02abccf3ae87fd4b581c64c8"
PRE_SHA = "d6b00706621684f568555949ddb52ea6f539c7cc15f5097d7be1992dbdc96503"
COMPAT_SHA = "443dc2a6f74764666dafd827edf8d4ba7e27c4143cc9d50e44261ef7b0b5e473"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def expand(spec: dict) -> list[str]:
    return [f"{spec['prefix']}{i:0{spec['width']}d}" for i in range(spec["start"], spec["end"] + 1)]


def require_text(text: str, *markers: str) -> None:
    for marker in markers:
        assert marker in text, f"missing verdict marker: {marker}"


def main() -> int:
    a = read_json(ACCOUNTING)
    cp = read_json(CHECKPOINT)
    text = VERDICT.read_text(encoding="utf-8")

    assert a["schema_version"] == "1.0.0"
    assert a["work_item_id"] == "STAGE-A-A11"
    assert a["application_baseline"] == APP_BASELINE
    packages = {row["name"]: row["sha256"] for row in a["historical_packages"]}
    assert packages["STAGE_A_A11_CONTEXTUAL_AI_PREIMPLEMENTATION_v0.1.0.zip"] == PRE_SHA
    assert packages["STAGE_A_A11_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip"] == COMPAT_SHA

    expected_slices = [*(f"AI-S{i:02d}" for i in range(1, 9)), *(f"AIG-S{i:02d}" for i in range(1, 9)), *(f"ISO-S{i:02d}" for i in range(1, 9))]
    got_slices = [row["slice_id"] for row in a["slices"]]
    assert a["slice_count"] == 24 and got_slices == expected_slices
    assert all(row["source_status"] == "PREIMPLEMENTATION_ONLY" for row in a["slices"])

    fixture_ids = {family: expand(spec) for family, spec in a["fixture_id_schemes"].items()}
    assert fixture_ids["AI"] == [f"SOURCE-ORDINAL-{i:02d}" for i in range(1, 25)]
    assert fixture_ids["AIG"] == [f"SOURCE-ORDINAL-{i:02d}" for i in range(1, 25)]
    assert fixture_ids["ISO"] == [f"ISO-FX-{i:03d}" for i in range(1, 25)]
    assert a["fixture_count"] == 72
    assert a["fixture_family_counts"] == {"AI": 24, "AIG": 24, "ISO": 24}
    assert a["all_fixtures_blocking"] is True

    acceptance = {family: expand(spec) for family, spec in a["acceptance_key_schemes"].items()}
    assert acceptance["AI"] == [f"SOURCE-ORDINAL-{i:02d}" for i in range(1, 29)]
    assert acceptance["AIG"] == [f"SOURCE-ORDINAL-{i:02d}" for i in range(1, 29)]
    assert acceptance["ISO"] == [f"SOURCE-CRITERION-{i:02d}" for i in range(1, 21)]
    assert a["blocking_acceptance_count"] == 76
    assert a["acceptance_family_counts"] == {"AI": 28, "AIG": 28, "ISO": 20}
    assert a["all_acceptance_blocking"] is True
    assert a["all_acceptance_entries_invented_text_no"] is True
    assert "not invented" in a["source_acceptance_text_note"]

    gaps = a["gap_revalidation"]
    assert a["historical_gap_count"] == len(gaps) == 24
    assert [g["gap_id"] for g in gaps] == [f"A11-GAP-{i:03d}" for i in range(1, 25)]
    dispositions = Counter(g["disposition"] for g in gaps)
    assert dispositions == {"STILL_VALID": 18, "CHANGED": 4, "SUPERSEDED": 2}
    assert "NEWLY_BLOCKED" not in dispositions

    contracts = a["planned_contracts"]
    assert a["planned_contract_count"] == len(contracts) == 26
    assert [c["contract_id"] for c in contracts] == [f"A11-CON-{i:03d}" for i in range(1, 27)]
    assert contracts[5]["contract"] == "AiProviderPort"
    assert contracts[17]["contract"] == "AiSafeTelemetryPort"
    assert all(c["proposed_path"].startswith("packages/contracts/src/optional-ai/") for c in contracts)

    assert a["revalidation_verdict"] == "PASS_READY_FOR_BOUNDED_A11_ACTIVATION"
    assert a["implementation_activated"] is False
    assert a["provider_selected"] is False
    assert a["paid_execution_authorized"] is False
    assert a["real_user_data_authorized"] is False

    require_text(
        text,
        "PASS — READY FOR BOUNDED A11 ACTIVATION",
        "Implementation state:** **NOT ACTIVATED",
        APP_BASELINE,
        PRE_SHA,
        COMPAT_SHA,
        "24 slices",
        "72 deterministic fixtures",
        "76 blocking source acceptance keys",
        "2 superseded, 4 changed, 18 still valid, 0 newly blocked",
        "0009_a11_optional_ai_orchestration.json",
        "filterSessionEventsForA9",
        "AiSafeTelemetryPort",
        "semantic/vector/remote retrieval is not authorized",
        "there is no mandatory global chatbot route",
    )

    assert cp["work_item_id"] == "STAGE-A-A11"
    assert cp["attempt_id"] == "STAGE-A-A11-current-revalidation-attempt-001"
    assert cp["application_baseline"] == APP_BASELINE
    assert cp["historical_preparation"]["source_slice_count"] == 24
    assert cp["historical_preparation"]["source_fixture_count"] == 72
    assert cp["historical_preparation"]["blocking_source_acceptance_criteria_count"] == 76
    assert cp["restrictions"]["a11_activated"] is False
    assert cp["restrictions"]["a11_application_branch_created"] is False
    assert cp["restrictions"]["provider_selected"] is False
    assert cp["restrictions"]["provider_credentials_authorized"] is False
    assert cp["restrictions"]["paid_execution_authorized"] is False
    assert cp["restrictions"]["real_user_prompt_collection_authorized"] is False
    assert cp["restrictions"]["semantic_vector_remote_ai_search_baseline_authorized"] is False
    assert cp["restrictions"]["autonomous_mutation_authorized"] is False
    assert cp["restrictions"]["release_authorized"] is False
    assert cp["restrictions"]["deployment_authorized"] is False
    assert cp["restrictions"]["canonical_promotion_authorized"] is False

    print("STAGE-A-A11 CURRENT-REPOSITORY REVALIDATION: PASS")
    print("slices=24 fixtures=72 acceptance=76 gaps=24 contracts=26")
    print("verdict=PASS_READY_FOR_BOUNDED_A11_ACTIVATION implementation_activated=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
