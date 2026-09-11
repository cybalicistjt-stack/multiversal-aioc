import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_mccs_registered_as_future_interstitial_without_activation():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    registry = j("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    backlog = j("governance/application-planning/multiversal-character-creature-studio/MCCS_PROGRAM_BACKLOG.json")

    planned = {x["program_id"]: x for x in index["planned_programs"]}
    assert planned["MCCS"]["status"] == "owner_approved_planned"
    assert planned["MCCS"]["activation_after"] == "MCS-21"
    assert planned["MCCS"]["successor"] == "SMB-08"
    assert planned["MCCS"]["implementation_authority"] is False
    assert planned["MCCS"]["execution_units"] == 21
    assert planned["MCS"]["successor"] == "MCCS-01"

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == [f"MCCS-{i:02d}" for i in range(1, 22)]
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])

    # Future planning must not seize the live authority plane.
    assert index["current"]["source_program"] == "ARI"
    assert index["current"]["status"] == "selected_not_started"
    assert index["current"]["implementation_authority"] is False
    assert index["current"]["implementation_branch"] is None
    assert registry["active_planning_work"]["work_item"] == index["current"]["work_item_id"]
    assert registry["active_planning_work"]["implementation_authority"] is False


def test_mccs_dependency_placement_and_successors():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    mcs = j("governance/application-planning/multiversal-cartography-studio/MCS_PROGRAM_BACKLOG.json")
    pca = j("governance/application-planning/production-capability-acceleration/PCA_PROGRAM_BACKLOG.json")

    expected = "CNI-01..13 → PCA-01..16 → MCS-01..21 → MCCS-01..21 → SMB-08 → SMB-09"
    assert expected in index["effective_forward_order"]
    assert index["mccs_execution_order"] == [f"MCCS-{i:02d}" for i in range(1, 22)]
    assert pca["successor"] == "MCS-01"
    assert mcs["successor"] == "MCCS-01"

    amendment = t("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_MCCS_AMENDMENT_2026-09-11.md")
    mcs_amendment = t("governance/application-planning/multiversal-cartography-studio/MCS_MCCS_SUCCESSOR_AMENDMENT_2026-09-11.md")
    smb = t("governance/application-planning/system-maturation-buildout/SMB_MCCS_INTERSTITIAL_INTEGRATION_AMENDMENT_2026-09-11.md")
    for doc in (amendment, mcs_amendment, smb):
        assert "MCS-01..21 → MCCS-01..21 → SMB-08" in doc


def test_mccs_preserves_appearance_owner_and_clean_room_boundaries():
    backlog = j("governance/application-planning/multiversal-character-creature-studio/MCCS_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()
    for owner in ("character", "species", "form", "capp", "papt", "pca", "ari", "p3d"):
        assert owner in boundaries

    benchmark = t("governance/application-planning/multiversal-character-creature-studio/MCCS_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    program = t("governance/application-planning/multiversal-character-creature-studio/MCCS_MULTIVERSAL_CHARACTER_CREATURE_STUDIO_PROGRAM.md").lower()
    assert "clean-room" in benchmark
    assert "does not copy" in benchmark
    assert "topology-first" in program
    assert "presentation-only" in program
    assert "no mccs implementation authority exists now" in program
    assert "does not activate p3d" in program
