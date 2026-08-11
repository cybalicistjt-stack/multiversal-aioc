#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
MATRIX = BASE / "PPIA-04_VEHICLE_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-04_REFERENCE_CASES_v0.1.0.json"
TAXONOMY = BASE / "PPIA-04_VEHICLE_EXPERIENCE_TAXONOMY_v0.1.0.json"
INVENTORY = BASE / "PPIA-04_SOURCE_AND_DESIGN_INVENTORY.md"


def fail(msg: str) -> None:
    raise SystemExit(f"PPIA-04 INSPECTOR/REFERENCE: FAIL — {msg}")


def require(condition: bool, msg: str) -> None:
    if not condition:
        fail(msg)


def main() -> None:
    for path in (MATRIX, CASES, TAXONOMY, INVENTORY):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    cases_doc = json.loads(CASES.read_text(encoding="utf-8"))
    taxonomy = json.loads(TAXONOMY.read_text(encoding="utf-8"))
    inventory = INVENTORY.read_text(encoding="utf-8")

    require(matrix.get("format") == "multiversal-ppia04-vehicle-inspector-projection-matrix", "wrong matrix format")
    require(matrix.get("inherits") == TAXONOMY.name, "matrix must inherit PPIA-04 taxonomy")

    expected_groups = [
        "identity_definition", "variant_configuration", "component_system_definition",
        "owned_vehicle_instance", "installed_configuration", "deployment_placement",
        "live_operational", "authority_control", "crew_stations", "cargo_carried_craft",
        "damage_failure", "resources_power", "movement_docking_environment", "provenance_recovery",
    ]
    groups = matrix.get("field_groups", [])
    require([group.get("id") for group in groups] == expected_groups, "field group set/order changed")

    actions = matrix.get("action_contracts", [])
    require(len(actions) == 14, "expected 14 action contracts")
    action_ids = {action.get("id") for action in actions}
    for action_id in (
        "configure_install_uninstall", "assign_station", "load_unload_transfer", "deploy_recall",
        "move_navigate", "attack_scan_operate", "route_power_manage_resource", "apply_damage_repair",
        "dock_board_launch", "capture_salvage", "history_export_recovery",
    ):
        require(action_id in action_ids, f"missing action contract {action_id}")

    roles = matrix.get("role_projection", {})
    require(set(roles) == {"player", "gm", "assistant_gm", "creator_owner_admin", "service_ai"}, "role projection set changed")

    principles = " ".join(matrix.get("principles", [])).lower()
    for phrase in ("unknown", "source-unspecified", "name similarity", "semantic movement", "nonvisual"):
        require(phrase in principles, f"missing principle {phrase!r}")

    all_matrix = json.dumps(matrix, ensure_ascii=False)
    for phrase in (
        "Hidden occupants", "name similarity", "station authority", "operation ID/status lookup",
        "zero hull/frame", "Detailed power-grid", "map pointing",
    ):
        require(phrase in all_matrix, f"missing matrix invariant {phrase!r}")

    require(cases_doc.get("format") == "multiversal-ppia04-vehicle-reference-cases", "wrong case format")
    require(cases_doc.get("inherits") == TAXONOMY.name, "cases must inherit PPIA-04 taxonomy")
    policy = cases_doc.get("policy", {})
    require(policy.get("automatic_identity_merge") is False, "automatic identity merge must be false")
    require(policy.get("name_similarity_creates_parent_link") is False, "name-similarity parent links must be false")
    require(policy.get("synthetic_qa_records_are_canonical") is False, "synthetic QA cannot be canonical")
    require(policy.get("deferred_simulation_features_are_operational") is False, "deferred simulation cannot be operational")
    require(policy.get("unknown_source_value_is_zero") is False, "unknown source value cannot be zero")

    cases = cases_doc.get("cases", [])
    require(len(cases) == 20, f"expected 20 reference cases, got {len(cases)}")
    require([case.get("case_id") for case in cases] == [f"PPIA04-RC-{n:03d}" for n in range(1, 21)], "case IDs must be continuous 001-020")

    titles = " | ".join(case.get("title", "") for case in cases).lower()
    for phrase in (
        "definition versus owned", "name-similarity", "owner is not automatically", "hidden occupants",
        "semantic movement", "source-unspecified", "subsystem damage", "docking, boarding and launch",
        "capture/salvage", "ambiguous network", "authority revocation", "accessible nonvisual", "deferred simulation",
    ):
        require(phrase in titles, f"missing required reference case {phrase!r}")

    all_cases = json.dumps(cases_doc, ensure_ascii=False)
    for phrase in (
        "Carrier Class.PDF", "Mecha Hangars v2.PDF", "CSV_VEHICLE_PARENT_RECONCILIATION_CONTRACT.json",
        "MV-IA-F013", "MV-IA-F014", "MV-IA-F020/F021", "operation ID/status",
    ):
        require(phrase in all_cases, f"missing source/contract anchor {phrase!r}")

    require("24 PDFs / 608 pages" in inventory, "foundation source inventory count changed")
    require("5,628 rows" in inventory, "foundation vehicle row count changed")
    require(taxonomy.get("authority", {}).get("vehicle_csv_rows") == 5628, "taxonomy vehicle row count changed")
    require(len(taxonomy.get("identity_state_layers", [])) == 14, "taxonomy must retain 14 layers")

    summary = cases_doc.get("summary", {})
    require(summary.get("cases") == 20, "summary case count must be 20")
    require(summary.get("contract_grounded_cases") == 9, "contract-grounded count must be 9")
    require(summary.get("synthetic_qa_cases") == 8, "synthetic QA count must be 8")
    require(summary.get("guardrail_cases") == 3, "guardrail count must be 3")
    require(summary.get("canonical_synthetic_records") == 0, "synthetic cases must not be canonical")

    print("PPIA-04 INSPECTOR/REFERENCE: PASS")
    print("field_groups=14")
    print("action_contracts=14")
    print("reference_cases=20")
    print("contract_grounded_cases=9")
    print("synthetic_qa_cases=8")
    print("guardrail_cases=3")


if __name__ == "__main__":
    main()
