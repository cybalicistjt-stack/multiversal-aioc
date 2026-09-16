import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


EXPECTED = [
    "MCS-01",
    "MCS-03",
    "MCS-05",
    "MCS-07",
    "MCS-08",
    "MCS-10",
    "MCS-13",
    "MCS-14",
    "MCS-15",
    "MCS-18",
    "MCS-19",
    "MCS-21",
]


def test_mcs_pdcp_reduced_contract_is_complete_and_non_authoritative():
    backlog = j("governance/application-planning/multiversal-cartography-studio/MCS_PROGRAM_BACKLOG.json")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MCS_REDUCTION_RECEIPT.json")
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == EXPECTED
    assert [x["id"] for x in backlog["tranches"]] == EXPECTED
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])

    assert backlog["pdcp_reduction"]["baseline_tranche_count"] == 21
    assert backlog["pdcp_reduction"]["reduced_tranche_count"] == 12
    assert backlog["pdcp_reduction"]["capability_loss_detected"] is False

    assert receipt["status"] == "resolved"
    assert receipt["baseline_tranche_count"] == 21
    assert receipt["reduced_tranche_count"] == 12
    assert receipt["removed_standalone_tranches"] == 9
    assert receipt["surviving_tranche_ids"] == EXPECTED
    assert len(receipt["dispositions"]) == 21
    assert {x["baseline_id"] for x in receipt["dispositions"]} == {f"MCS-{i:02d}" for i in range(1, 22)}
    assert receipt["golden_vector_count"] == 48
    assert receipt["capability_loss_detected"] is False
    assert receipt["implementation_authority"] is False
    assert receipt["ops3_current_mutation"] is False
    assert receipt["dag_mutation_required"] is False

    family = next(x for x in ledger["families"] if x["program_id"] == "MCS")
    assert family["reduction_status"] == "resolved"
    assert family["reduced_tranche_count"] == 12
    assert family["surviving_tranche_ids"] == EXPECTED
    assert ledger["baseline_snapshot"]["effective_reduced_total"] == 105
    assert ledger["baseline_snapshot"]["removed_standalone_future_tranches"] == 103
    assert ledger["baseline_snapshot"]["approved_family_reductions"] == 10


def test_mcs_dag_milestones_and_parallel_activation_are_preserved():
    dag = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")
    backlog = j("governance/application-planning/multiversal-cartography-studio/MCS_PROGRAM_BACKLOG.json")

    assert set(dag["parallel_safe_sets"][0]) == {"MCS", "MCCS", "MRCS", "MSAS"}
    for gate in ("FOUR_LANE_RELEASE_BARRIER", "PCA-03", "PCA-04", "PCA-15"):
        assert gate in dag["program_edges"]["MCS"]["start_requires"]
    assert "PCA-16" in dag["program_edges"]["MCS"]["golden_proof_requires"]
    assert "MCS-21" in dag["program_edges"]["MSLR"]["start_requires"]
    assert dag["milestone_gates"]["rotation"]["MSLR-01"] == ["MBES-24", "GPR-16", "MCS-21"]
    assert backlog["activation_after"].startswith("ROADMAP_DEPENDENCY_GRAPH")


def test_mcs_cross_family_absorptions_are_explicit():
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MCS_REDUCTION_RECEIPT.json")
    program = t("governance/application-planning/multiversal-cartography-studio/MCS_MULTIVERSAL_CARTOGRAPHY_STUDIO_PROGRAM.md").lower()
    absorption = "\n".join(
        f"{x['concern']} {x['owner']} {x['mcs_residual']}" for x in receipt["cross_family_absorptions"]
    ).lower()

    for term in (
        "pca-02/pca-03",
        "pca-12",
        "pca-09",
        "ari/pca",
        "mai",
        "ise/scene/tabletop",
        "ssa/world/scene",
        "mbes",
        "combat/visibility/exploration",
    ):
        assert term in absorption

    assert "pixels, vectors, labels, generator results" in program
    assert "map-specific procedural world proposal workbench" in program
    assert "no mcs implementation authority exists now" in program


def test_mcs_preserves_map_authoring_and_clean_room_boundaries():
    backlog = j("governance/application-planning/multiversal-cartography-studio/MCS_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()
    benchmark = t("governance/application-planning/multiversal-cartography-studio/MCS_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    program = t("governance/application-planning/multiversal-cartography-studio/MCS_MULTIVERSAL_CARTOGRAPHY_STUDIO_PROGRAM.md").lower()

    for owner in ("ari", "mai", "ise", "ssa", "world", "scene", "combat", "exploration", "visibility", "pca", "mbes", "mslr"):
        assert owner in boundaries or owner in program

    assert "clean-room" in benchmark
    assert "does not copy" in benchmark
    assert "presentation" in program
    assert "paid/cloud mapping providers" in program
