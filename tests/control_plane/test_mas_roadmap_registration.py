import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_mas_registered_as_future_interstitial_without_activation():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    registry = j("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    backlog = j("governance/application-planning/multiversal-adventure-studio/MAS_PROGRAM_BACKLOG.json")

    planned = {x["program_id"]: x for x in index["planned_programs"]}
    assert planned["MAS"]["status"] == "owner_approved_planned"
    assert planned["MAS"]["activation_after"] == "MNCS-24"
    assert planned["MAS"]["successor"] == "MSAS-01"
    assert planned["MAS"]["implementation_authority"] is False
    assert planned["MAS"]["execution_units"] == 21
    assert planned["MNCS"]["successor"] == "MAS-01"

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == [f"MAS-{i:02d}" for i in range(1, 22)]
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])

    assert index["current"]["source_program"] == "ARI"
    assert index["current"]["status"] == "selected_not_started"
    assert index["current"]["implementation_authority"] is False
    assert index["current"]["implementation_branch"] is None
    assert registry["active_planning_work"]["work_item"] == index["current"]["work_item_id"]


def test_mas_dependency_placement_and_successors():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    mccs = j("governance/application-planning/multiversal-character-creature-studio/MCCS_PROGRAM_BACKLOG.json")
    mncs = j("governance/application-planning/multiversal-npc-creature-studio/MNCS_PROGRAM_BACKLOG.json")
    mas = j("governance/application-planning/multiversal-adventure-studio/MAS_PROGRAM_BACKLOG.json")

    expected = "MCS-01..21 → MCCS-01..21 → MNCS-01..24 → MAS-01..21 → MSAS-01..21"
    assert expected in index["effective_forward_order"]
    assert index["mas_execution_order"] == [f"MAS-{i:02d}" for i in range(1, 22)]
    assert mccs["successor"] == "MNCS-01"
    assert mncs["successor"] == "MAS-01"
    assert mas["successor"] == "MSAS-01"

    amendment = t("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_MNCS_AMENDMENT_2026-09-11.md")
    predecessor = t("governance/application-planning/multiversal-adventure-studio/MAS_MNCS_PREDECESSOR_AMENDMENT_2026-09-11.md")
    msas_successor = t("governance/application-planning/multiversal-adventure-studio/MAS_MSAS_SUCCESSOR_AMENDMENT_2026-09-11.md")
    assert "MCCS-01..21 → MNCS-01..24 → MAS-01..21" in amendment
    assert "MCCS-01..21 → MNCS-01..24 → MAS-01..21" in predecessor
    assert "MAS-01..21 → MSAS-01..21 → SMB-08" in msas_successor


def test_mas_preserves_story_runtime_and_clean_room_boundaries():
    backlog = j("governance/application-planning/multiversal-adventure-studio/MAS_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()
    for owner in ("csw", "cni", "story", "adventure", "scene", "session", "ari", "mcs", "mccs", "mncs", "msas"):
        assert owner in boundaries

    benchmark = t("governance/application-planning/multiversal-adventure-studio/MAS_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    program = t("governance/application-planning/multiversal-adventure-studio/MAS_MULTIVERSAL_ADVENTURE_STUDIO_PROGRAM.md").lower()
    assert "clean-room" in benchmark
    assert "does not copy" in benchmark
    assert "prepared content" in program
    assert "live run state" in program
    assert "no mas implementation authority exists now" in program
