import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_mslr_is_future_planned_and_does_not_select_itself():
    current = j("operations/CURRENT.json")
    backlog = j("governance/application-planning/multiversal-spatial-law-runtime/MSLR_PROGRAM_BACKLOG.json")

    assert current["lanes"]["product-development"]["selected_work_item"] != "MSLR-01"
    assert backlog["status"] == "owner_approved_planned"
    assert backlog["implementation_authority"] is False
    assert backlog["activation_after"] == "MBES-24"
    assert backlog["successor"] == "MSWI-01"


def test_mslr_uses_bounded_one_continue_family_design_after_pdcp_reduction():
    backlog = j("governance/application-planning/multiversal-spatial-law-runtime/MSLR_PROGRAM_BACKLOG.json")
    expected = ["MSLR-01", "MSLR-03", "MSLR-04", "MSLR-07", "MSLR-08", "MSLR-13", "MSLR-14", "MSLR-16", "MSLR-18"]

    assert backlog["tranche_execution_target_minutes"] == 24
    assert backlog["minimum_closeout_reserve_minutes"] == 8
    assert backlog["split_before_start_if_target_not_credible"] is True
    assert backlog["strict_order"] == expected
    assert [x["id"] for x in backlog["tranches"]] == expected
    assert backlog["pdcp_reduction"]["baseline_tranche_count"] == 18
    assert backlog["pdcp_reduction"]["reduced_tranche_count"] == 9
    assert backlog["pdcp_reduction"]["stable_start_gate"] == "MSLR-01"
    assert backlog["pdcp_reduction"]["stable_golden_gate"] == "MSLR-18"
    assert backlog["pdcp_reduction"]["capability_loss_detected"] is False
    assert all(x["estimated_active_minutes"] <= 16 for x in backlog["tranches"])
    design = "\n".join(backlog["execution_design"].values()).lower()
    assert "one owner continue" in design
    assert "dependency closure" in design
    assert "reserve" in design
    assert "unchanged deterministic failure" in design


def test_mslr_is_officially_between_mbes_and_mswi_with_stable_gates():
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")
    mbes = j("governance/application-planning/multiversal-built-environment-settlement/MBES_PROGRAM_BACKLOG.json")
    mswi = j("governance/application-planning/multiversal-systemic-worldplay-integration/MSWI_PROGRAM_BACKLOG.json")

    assert graph["status"] == "CURRENT_PLANNING_AUTHORITY"
    assert graph["nodes"]["MSLR"]["implementation_authority"] is False
    assert graph["program_edges"]["MSLR"]["hard_requires"] == ["MBES"]
    for dependency in ("MBES-24", "GPR-16", "MCS-21", "SSA-10", "ENV-16"):
        assert dependency in graph["program_edges"]["MSLR"]["start_requires"]
    assert graph["program_edges"]["MSLR"]["golden_proof_requires"] == ["MSLR-18"]
    assert "MSLR" in graph["program_edges"]["MSWI"]["hard_requires"]
    assert "MSLR-18" in graph["program_edges"]["MSWI"]["start_requires"]
    assert graph["milestone_gates"]["rotation"]["MSLR-01"] == ["MBES-24", "GPR-16", "MCS-21"]
    assert graph["milestone_gates"]["rotation"]["MSWI-01"][0] == "MSLR-18"
    assert mbes["successor"] == "MSLR-01"
    assert mswi["activation_after"] == "MSLR-18"
    assert "MSLR effective PDCP-reduced strict order completed_verified with MSLR-18 golden proof" in mswi["required_upstream"]


def test_mslr_preserves_existing_owner_domains_and_key_distinctions():
    backlog = j("governance/application-planning/multiversal-spatial-law-runtime/MSLR_PROGRAM_BACKLOG.json")
    program = t("governance/application-planning/multiversal-spatial-law-runtime/MSLR_MULTIVERSAL_SPATIAL_LAW_RUNTIME_PROGRAM.md").lower()
    matrix = t("governance/application-planning/multiversal-spatial-law-runtime/MSLR_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    boundaries = "\n".join(backlog["boundaries"]).lower()

    for owner in ("ssa", "mcs", "env", "gpr", "mbes", "mswi"):
        assert owner in boundaries
    for concept in (
        "dynamic topology", "true/observable/known/suspected", "fuzzy", "metric",
        "recursive", "gravity", "memory", "procedural impossible-space",
        "sensory", "multi-resolution"
    ):
        assert concept in (program + "\n" + matrix)
    assert "topology, metric, containment/scale and orientation are different dimensions" in program
    assert "bleed" in boundaries and "traversability" in boundaries
    assert "protected code" in matrix
    assert "pending validation" in matrix


def test_mslr_pdcp_reduction_keeps_every_baseline_tranche_mapped_once():
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MSLR_REDUCTION_RECEIPT.json")
    backlog = j("governance/application-planning/multiversal-spatial-law-runtime/MSLR_PROGRAM_BACKLOG.json")

    assert receipt["baseline_tranche_count"] == 18
    assert receipt["reduced_tranche_count"] == 9
    assert receipt["tranches_removed_or_merged"] == 9
    assert len(receipt["baseline_rows"]) == 18
    assert [row["baseline_id"] for row in receipt["baseline_rows"]] == [f"MSLR-{i:02d}" for i in range(1, 19)]
    assert all(row["capability_loss_check"] == "pass" for row in receipt["baseline_rows"])
    assert set(x["id"] for x in receipt["surviving_tranches"]) == set(backlog["strict_order"])
    assert receipt["golden_proof_preserved"] is True
    assert receipt["capability_loss_detected"] is False
    assert receipt["dag_updates"] == []


def test_mslr_pdcp_reduction_proves_overlap_and_shared_owner_absorption():
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MSLR_REDUCTION_RECEIPT.json")
    overlap = t("governance/application-planning/preimplementation-design-closure/PDCP_CROSS_FAMILY_OVERLAP_REGISTER.md").lower()

    expected_clusters = {
        ("MSLR-01", "MSLR-02"),
        ("MSLR-03", "MSLR-06"),
        ("MSLR-04", "MSLR-05", "MSLR-11"),
        ("MSLR-07", "MSLR-12"),
        ("MSLR-08", "MSLR-09", "MSLR-10"),
        ("MSLR-13", "MSLR-15"),
        ("MSLR-14", "MSLR-17"),
    }
    assert {tuple(x) for x in receipt["intra_family_overlap_clusters"]} == expected_clusters
    concerns = {x["concern"] for x in receipt["cross_family_absorptions"]}
    for concern in (
        "preview_debug_intervention_reversal",
        "solver_simulation_formal_analysis",
        "procedural_graph_recipe_engine",
        "cartographic_projection",
        "generic_gameplay_execution_replay",
        "audio_visual_presentation",
        "systemic_consequence_fanout",
    ):
        assert concern in concerns
    assert "result: **18 → 9**" in overlap
    assert "every pdcp family reduction pass must perform both" in overlap
