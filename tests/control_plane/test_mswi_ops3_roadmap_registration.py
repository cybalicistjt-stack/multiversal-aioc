import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_mswi_is_future_planned_without_current_authority():
    current = j("operations/CURRENT.json")
    backlog = j("governance/application-planning/multiversal-systemic-worldplay-integration/MSWI_PROGRAM_BACKLOG.json")

    assert current["lanes"]["product-development"]["selected_work_item"] == "MAS-01"
    assert current["lanes"]["product-development"]["state"] == "selected_not_started"
    assert current["lanes"]["product-development"]["implementation_authority"] is False

    assert backlog["status"] == "owner_approved_planned"
    assert backlog["implementation_authority"] is False
    assert backlog["activation_after"] == "MBES-24"
    assert backlog["successor"] == "SMB-08"


def test_mswi_uses_bounded_one_continue_family_design():
    backlog = j("governance/application-planning/multiversal-systemic-worldplay-integration/MSWI_PROGRAM_BACKLOG.json")
    assert backlog["tranche_execution_target_minutes"] == 24
    assert backlog["minimum_closeout_reserve_minutes"] == 8
    assert backlog["split_before_start_if_target_not_credible"] is True
    assert backlog["strict_order"] == [f"MSWI-{i:02d}" for i in range(1, 19)]
    assert all(x["estimated_active_minutes"] <= 16 for x in backlog["tranches"])
    design = "\n".join(backlog["execution_design"].values()).lower()
    assert "one owner continue" in design
    assert "dependency closure" in design
    assert "reserve" in design
    assert "unchanged deterministic failure" in design


def test_mswi_is_in_dependency_graph_between_mbes_and_smb08():
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")
    mbes = j("governance/application-planning/multiversal-built-environment-settlement/MBES_PROGRAM_BACKLOG.json")

    assert graph["status"] == "CURRENT_PLANNING_AUTHORITY"
    assert graph["nodes"]["MSWI"]["implementation_authority"] is False
    assert "MBES" in graph["program_edges"]["MSWI"]["hard_requires"]
    assert "MBES-24" in graph["program_edges"]["MSWI"]["start_requires"]
    assert "GPR-16" in graph["program_edges"]["MSWI"]["start_requires"]
    assert "MNCS-24" in graph["program_edges"]["MSWI"]["start_requires"]
    assert graph["program_edges"]["MSWI"]["golden_proof_requires"] == ["MSWI-18"]
    assert "MSWI-18" in graph["program_edges"]["SMB08"]["start_requires"]
    assert graph["milestone_gates"]["rotation"]["MSWI-01"] == ["MBES-24", "GPR-16", "MNCS-24"]
    assert mbes["successor"] == "MSWI-01"


def test_mswi_deduplicates_existing_owner_domains():
    backlog = j("governance/application-planning/multiversal-systemic-worldplay-integration/MSWI_PROGRAM_BACKLOG.json")
    program = t("governance/application-planning/multiversal-systemic-worldplay-integration/MSWI_MULTIVERSAL_SYSTEMIC_WORLDPLAY_INTEGRATION_PROGRAM.md").lower()
    matrix = t("governance/application-planning/multiversal-systemic-worldplay-integration/MSWI_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    boundaries = "\n".join(backlog["boundaries"]).lower()

    for owner in ("dpl", "mncs", "gpr", "mera", "mbes", "mcs", "mas", "mccs", "msas"):
        assert owner in boundaries
    for concept in ("world-transformation", "composite", "anatomy", "doctrine", "pursuit", "diegetic", "grand/world projects", "procedural site", "interaction-density"):
        assert concept in (program + "\n" + matrix)
    assert "protected code" in matrix
    assert "not" in matrix and "cop" in matrix
