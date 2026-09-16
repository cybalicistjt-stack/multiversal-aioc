import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


EXPECTED = [
    "MCCS-01",
    "MCCS-03",
    "MCCS-05",
    "MCCS-06",
    "MCCS-09",
    "MCCS-11",
    "MCCS-13",
    "MCCS-16",
    "MCCS-18",
    "MCCS-19",
    "MCCS-21",
]


def test_mccs_pdcp_reduced_contract_is_complete_and_non_authoritative():
    backlog = j("governance/application-planning/multiversal-character-creature-studio/MCCS_PROGRAM_BACKLOG.json")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MCCS_REDUCTION_RECEIPT.json")
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == EXPECTED
    assert [x["id"] for x in backlog["tranches"]] == EXPECTED
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])

    assert backlog["pdcp_reduction"]["baseline_tranche_count"] == 21
    assert backlog["pdcp_reduction"]["reduced_tranche_count"] == 11
    assert backlog["pdcp_reduction"]["capability_loss_detected"] is False

    assert receipt["status"] == "resolved"
    assert receipt["baseline_tranche_count"] == 21
    assert receipt["reduced_tranche_count"] == 11
    assert receipt["removed_standalone_tranches"] == 10
    assert receipt["surviving_tranche_ids"] == EXPECTED
    assert len(receipt["dispositions"]) == 21
    assert {x["baseline_id"] for x in receipt["dispositions"]} == {f"MCCS-{i:02d}" for i in range(1, 22)}
    assert receipt["golden_vector_count"] == 48
    assert receipt["capability_loss_detected"] is False
    assert receipt["implementation_authority"] is False
    assert receipt["ops3_current_mutation"] is False
    assert receipt["dag_mutation_required"] is True

    family = next(x for x in ledger["families"] if x["program_id"] == "MCCS")
    assert family["reduction_status"] == "resolved"
    assert family["reduced_tranche_count"] == 11
    assert family["surviving_tranche_ids"] == EXPECTED


def test_mccs_equivalent_mncs_rotation_gate_and_owner_boundaries():
    dag = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MCCS_REDUCTION_RECEIPT.json")
    backlog = j("governance/application-planning/multiversal-character-creature-studio/MCCS_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()

    assert dag["milestone_gates"]["rotation"]["MNCS-01"] == ["MCCS-01"]
    assert "MCCS-01" in dag["program_edges"]["MNCS"]["start_requires"]
    assert "MCCS-02" not in dag["program_edges"]["MNCS"]["start_requires"]
    assert receipt["dag_gate_replacement"]["removed_milestone"] == "MCCS-02"
    assert receipt["dag_gate_replacement"]["replacement_milestone"] == "MCCS-01"

    for owner in ("capp/ppia", "papt/pca", "mncs", "ari/pca", "animation/scene/combat/dialogue", "p3d"):
        assert owner in boundaries


def test_mccs_folded_seams_and_cross_family_absorptions_are_explicit():
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MCCS_REDUCTION_RECEIPT.json")
    dispositions = {x["baseline_id"]: x for x in receipt["dispositions"]}
    absorption_text = "\n".join(
        f"{x['concern']} {x['owner']} {x['mccs_residual']}" for x in receipt["cross_family_absorptions"]
    ).lower()

    assert dispositions["MCCS-02"]["residual_target"] == "MCCS-01"
    assert dispositions["MCCS-14"]["residual_target"] == "MCCS-13"
    assert dispositions["MCCS-15"]["residual_target"] == "MCCS-13"
    assert dispositions["MCCS-17"]["disposition"] == "ABSORB_EXISTING_OWNER"
    assert "mncs" in dispositions["MCCS-17"]["residual_target"].lower()
    assert dispositions["MCCS-20"]["residual_target"] == "MCCS-19"

    for term in ("character/npc/creature", "capp/ppia", "papt/pca", "mncs", "ari/pca", "packet 07", "p3d"):
        assert term in absorption_text


def test_mccs_preserves_topology_presentation_clean_room_and_p3d_boundaries():
    program = t("governance/application-planning/multiversal-character-creature-studio/MCCS_MULTIVERSAL_CHARACTER_CREATURE_STUDIO_PROGRAM.md").lower()
    benchmark = t("governance/application-planning/multiversal-character-creature-studio/MCCS_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    dcp = t("governance/application-planning/preimplementation-design-closure/PDCP_MCCS_FAMILY_DESIGN_CLOSURE.md").lower()

    assert "topology-first" in program
    assert "presentation-only" in program
    assert "does not activate p3d" in program
    assert "no mccs implementation authority exists now" in program
    assert "clean-room" in benchmark
    assert "does not copy" in benchmark
    assert "48 proof vectors" in dcp
    assert "atomic equivalent gate rewrite" in dcp
