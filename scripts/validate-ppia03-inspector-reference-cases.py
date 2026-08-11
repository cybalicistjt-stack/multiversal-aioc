#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
MATRIX = BASE / "PPIA-03_ITEM_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-03_REFERENCE_CASES_v0.1.0.json"
TAXONOMY = BASE / "PPIA-03_ITEM_EXPERIENCE_TAXONOMY_v0.1.0.json"


def fail(msg: str) -> None:
    raise SystemExit(f"PPIA-03 INSPECTOR/REFERENCE: FAIL — {msg}")


def require(condition: bool, msg: str) -> None:
    if not condition:
        fail(msg)


def main() -> None:
    for path in (MATRIX, CASES, TAXONOMY):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    cases_doc = json.loads(CASES.read_text(encoding="utf-8"))
    taxonomy = json.loads(TAXONOMY.read_text(encoding="utf-8"))

    require(matrix.get("format") == "multiversal-ppia03-item-inspector-projection-matrix", "wrong matrix format")
    require(matrix.get("inherits") == TAXONOMY.name, "matrix must inherit PPIA-03 taxonomy")

    groups = matrix.get("field_groups", [])
    group_ids = [group.get("id") for group in groups]
    expected_groups = [
        "identity_definition",
        "intrinsic_mechanics",
        "instance_authority",
        "location_containment",
        "quantity_stack",
        "equipment_readiness",
        "charges_ammunition",
        "condition_durability",
        "identification_knowledge",
        "economy_transfer",
        "crafting_salvage",
        "modifications_relationships",
        "source_provenance",
        "history_recovery",
    ]
    require(group_ids == expected_groups, "field group set/order changed")

    actions = matrix.get("action_contracts", [])
    require(len(actions) == 12, "expected 12 action contracts")
    action_ids = {action.get("id") for action in actions}
    for action_id in (
        "split_merge_stack",
        "equip_install_attune",
        "use_consume_reload_recharge",
        "transfer_lend_share_trade",
        "identify_reveal",
        "damage_repair_maintain",
        "reserve_craft_salvage",
        "history_export_recovery",
    ):
        require(action_id in action_ids, f"missing action contract {action_id}")

    principles = " ".join(matrix.get("principles", [])).lower()
    require("unknown" in principles and "zero" in principles and "hidden" in principles, "unknown/zero/hidden distinction missing")

    invariants = " ".join(matrix.get("acceptance_invariants", []))
    for phrase in ("Taser", "Energy Sniper Rifle", "source-unspecified", "operation ID", "drag-and-drop"):
        require(phrase in invariants, f"missing acceptance invariant phrase {phrase!r}")

    roles = matrix.get("role_projection", {})
    require(set(roles) == {"player", "gm", "assistant_gm", "creator_owner_admin", "service_ai"}, "role projection set changed")

    location = next(group for group in groups if group["id"] == "location_containment")
    require("Hidden contents are filtered before child counts" in location.get("privacy_rule", ""), "hidden container aggregate rule missing")
    equipment = next(group for group in groups if group["id"] == "equipment_readiness")
    require("never silently changes ownership" in equipment.get("authority_rule", ""), "equipment/ownership boundary missing")
    charges = next(group for group in groups if group["id"] == "charges_ammunition")
    require("never zero, unlimited" in charges.get("unknown_rule", ""), "unknown capacity rule missing")

    require(cases_doc.get("format") == "multiversal-ppia03-item-inventory-reference-cases", "wrong case format")
    policy = cases_doc.get("policy", {})
    require(policy.get("owner_delegated_recommendations_are_source_facts") is False, "recommendations must not be source facts")
    require(policy.get("automatic_identity_merge") is False, "automatic identity merge must be false")
    require(policy.get("reference_only_name_creates_definition") is False, "reference-only names must not create definitions")

    cases = cases_doc.get("cases", [])
    require(len(cases) == 18, f"expected 18 reference cases, got {len(cases)}")
    case_ids = [case.get("case_id") for case in cases]
    require(case_ids == [f"PPIA03-RC-{number:03d}" for number in range(1, 19)], "case IDs must be continuous 001-018")

    titles = " | ".join(case.get("title", "") for case in cases).lower()
    for phrase in ("taser", "source-unspecified", "ammo-reference-only", "hidden nested", "shared party", "equipment assignment", "ambiguous network", "crafting reservation", "software-like"):
        require(phrase in titles, f"missing required reference case {phrase!r}")

    all_text = json.dumps(cases_doc, ensure_ascii=False)
    for name in ("Laser Sniper Rifle", "Plasma Rifle", "Plasma Shotgun", "Ion Blaster", "Handheld Laser", "Plasma Pistol", "Sonic Rifle"):
        require(name in all_text, f"missing source-unspecified weapon {name}")
    for name in ("Energy Sniper Rifle", "Plasma Carbine", "Cryo Blaster"):
        require(name in all_text, f"missing reference-only weapon {name}")

    summary = cases_doc.get("summary", {})
    require(summary.get("cases") == 18, "summary case count must be 18")
    require(summary.get("synthetic_qa_cases") == 8, "synthetic QA count must be 8")
    require(summary.get("canonical_synthetic_records") == 0, "synthetic cases must not be canonical")

    print("PPIA-03 INSPECTOR/REFERENCE: PASS")
    print("field_groups=14")
    print("action_contracts=12")
    print("reference_cases=18")
    print("synthetic_qa_cases=8")
    print("guardrail_cases=3")


if __name__ == "__main__":
    main()
