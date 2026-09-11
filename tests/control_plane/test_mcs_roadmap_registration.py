import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_mcs_registered_as_future_interstitial_without_activation():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    registry = j("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    backlog = j("governance/application-planning/multiversal-cartography-studio/MCS_PROGRAM_BACKLOG.json")

    planned = {x["program_id"]: x for x in index["planned_programs"]}
    assert planned["MCS"]["status"] == "owner_approved_planned"
    assert planned["MCS"]["activation_after"] == "PCA-16"
    assert planned["MCS"]["successor"] == "MCCS-01"
    assert planned["MCS"]["implementation_authority"] is False
    assert planned["MCS"]["execution_units"] == 21
    assert planned["PCA"]["successor"] == "MCS-01"

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == [f"MCS-{i:02d}" for i in range(1, 22)]
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])

    # Future planning must not seize the live authority plane or pin this test to a stale ARI unit.
    assert index["current"]["source_program"] == "ARI"
    assert index["current"]["implementation_authority"] is False
    assert registry["active_planning_work"]["work_item"] == index["current"]["work_item_id"]
    assert registry["active_planning_work"]["implementation_authority"] is False


def test_mcs_dependency_placement_and_successors():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    pca = j("governance/application-planning/production-capability-acceleration/PCA_PROGRAM_BACKLOG.json")

    expected = "CNI-01..13 → PCA-01..16 → MCS-01..21 → MCCS-01..21 → SMB-08 → SMB-09"
    assert expected in index["effective_forward_order"]
    assert index["mcs_execution_order"] == [f"MCS-{i:02d}" for i in range(1, 22)]
    assert pca["successor"] == "MCS-01"

    amendment = t("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_MCS_AMENDMENT_2026-09-11.md")
    successor = t("governance/application-planning/multiversal-cartography-studio/MCS_MCCS_SUCCESSOR_AMENDMENT_2026-09-11.md")
    assert "PCA-01..16 → MCS-01..21 → SMB-08" in amendment
    assert "MCS-01..21 → MCCS-01..21 → SMB-08" in successor


def test_mcs_preserves_owner_and_clean_room_boundaries():
    backlog = j("governance/application-planning/multiversal-cartography-studio/MCS_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()
    for owner in ("ari", "mai", "ise", "ssa", "vti", "world", "scene", "combat", "exploration", "visibility"):
        assert owner in boundaries

    benchmark = t("governance/application-planning/multiversal-cartography-studio/MCS_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    program = t("governance/application-planning/multiversal-cartography-studio/MCS_MULTIVERSAL_CARTOGRAPHY_STUDIO_PROGRAM.md").lower()
    assert "clean-room" in benchmark
    assert "does not copy" in benchmark
    assert "presentation-only" in program
    assert "no mcs implementation authority exists now" in program
