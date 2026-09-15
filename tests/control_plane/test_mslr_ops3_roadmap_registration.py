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


def test_mslr_uses_bounded_one_continue_family_design():
    backlog = j("governance/application-planning/multiversal-spatial-law-runtime/MSLR_PROGRAM_BACKLOG.json")
    assert backlog["tranche_execution_target_minutes"] == 24
    assert backlog["minimum_closeout_reserve_minutes"] == 8
    assert backlog["split_before_start_if_target_not_credible"] is True
    assert backlog["strict_order"] == [f"MSLR-{i:02d}" for i in range(1, 19)]
    assert all(x["estimated_active_minutes"] <= 16 for x in backlog["tranches"])
    design = "\n".join(backlog["execution_design"].values()).lower()
    assert "one owner continue" in design
    assert "dependency closure" in design
    assert "reserve" in design
    assert "unchanged deterministic failure" in design


def test_mslr_is_officially_between_mbes_and_mswi():
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
    assert "MSLR-01..18 completed_verified" in mswi["required_upstream"]


def test_mslr_preserves_existing_owner_domains_and_key_distinctions():
    backlog = j("governance/application-planning/multiversal-spatial-law-runtime/MSLR_PROGRAM_BACKLOG.json")
    program = t("governance/application-planning/multiversal-spatial-law-runtime/MSLR_MULTIVERSAL_SPATIAL_LAW_RUNTIME_PROGRAM.md").lower()
    matrix = t("governance/application-planning/multiversal-spatial-law-runtime/MSLR_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    boundaries = "\n".join(backlog["boundaries"]).lower()

    for owner in ("ssa", "mcs", "env", "gpr", "mbes", "mswi"):
        assert owner in boundaries
    for concept in (
        "dynamic topology", "true, observable, known", "fuzzy boundaries", "metric geometry",
        "recursive scale", "gravity frames", "memory", "procedural impossible-space",
        "liminal sensory", "multi-resolution"
    ):
        assert concept in (program + "\n" + matrix)
    assert "topology and metric geometry are different" in program
    assert "bleed" in boundaries and "traversability" in boundaries
    assert "protected code" in matrix
    assert "pending validation" in matrix
