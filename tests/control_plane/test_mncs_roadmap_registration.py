import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_mncs_registered_without_changing_live_authority():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    registry = j("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    backlog = j("governance/application-planning/multiversal-npc-creature-studio/MNCS_PROGRAM_BACKLOG.json")
    planned = {x["program_id"]: x for x in index["planned_programs"]}

    assert planned["MNCS"]["status"] == "owner_approved_planned"
    assert planned["MNCS"]["activation_after"] == "MCCS-21"
    assert planned["MNCS"]["successor"] == "MAS-01"
    assert planned["MNCS"]["implementation_authority"] is False
    assert planned["MNCS"]["execution_units"] == 24
    assert planned["MCCS"]["successor"] == "MNCS-01"
    assert planned["MAS"]["activation_after"] == "MNCS-24"

    assert backlog["strict_order"] == [f"MNCS-{i:02d}" for i in range(1, 25)]
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])
    assert backlog["implementation_authority"] is False

    assert index["current"]["work_item_id"] == "ARI-16"
    assert index["current"]["status"] == "selected_not_started"
    assert index["current"]["implementation_authority"] is False
    assert index["current"]["implementation_branch"] is None
    assert registry["active_planning_work"]["work_item"] == "ARI-16"
    assert registry["active_planning_work"]["implementation_authority"] is False


def test_mncs_placement_and_progressive_resolution_contract():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    program = t("governance/application-planning/multiversal-npc-creature-studio/MNCS_MULTIVERSAL_NPC_CREATURE_STUDIO_PROGRAM.md").lower()
    backlog = j("governance/application-planning/multiversal-npc-creature-studio/MNCS_PROGRAM_BACKLOG.json")

    expected = "MCS-01..21 → MCCS-01..21 → MNCS-01..24 → MAS-01..21 → MSAS-01..21"
    assert expected in index["effective_forward_order"]
    assert index["mncs_execution_order"] == [f"MNCS-{i:02d}" for i in range(1, 25)]

    names = "\n".join(x["name"] for x in backlog["tranches"]).lower()
    for term in ("instant improv", "knowledge", "reputation", "profession", "ecology", "behavior", "population", "conversation", "promotion", "runtime handoff"):
        assert term in names

    assert "one identity, progressive generation resolution" in program
    assert "passing extra" in program
    assert "population → group/herd/pack/swarm" in program
    assert "selective regeneration" in program
    assert "no mncs implementation authority exists now" in program


def test_mncs_party_association_reputation_is_scoped_and_attributable():
    program = t("governance/application-planning/multiversal-npc-creature-studio/MNCS_MULTIVERSAL_NPC_CREATURE_STUDIO_PROGRAM.md").lower()
    amendment = t("governance/application-planning/multiversal-implementation-backbone/MIB09_MNCS_PARTY_REPUTATION_INTEGRATION_AMENDMENT_2026-09-11.md").lower()
    backlog = j("governance/application-planning/multiversal-npc-creature-studio/MNCS_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()

    for text in (program, amendment, boundaries):
        assert "campaign" in text
        assert "party" in text
        assert "association" in text
        assert "reputation" in text

    assert "not one universal shared-party score" in program
    assert "direct reputation" in program
    assert "source event" in program
    assert "no account-global or cross-campaign spillover" in amendment
    assert "does not automatically erase past reputation consequences" in program
    assert "second campaign" in program


def test_mncs_preserves_owner_clean_room_and_no_digital_human_scope():
    program = t("governance/application-planning/multiversal-npc-creature-studio/MNCS_MULTIVERSAL_NPC_CREATURE_STUDIO_PROGRAM.md").lower()
    benchmark = t("governance/application-planning/multiversal-npc-creature-studio/MNCS_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    backlog = j("governance/application-planning/multiversal-npc-creature-studio/MNCS_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()

    for owner in ("ppia-02", "mib-09", "dpl", "world", "inventory", "mccs", "mas", "ari"):
        assert owner in program

    assert "fictional ttrpg" in program
    assert "digital-human reconstruction" in program
    assert "does not implement real-person reproduction" in boundaries
    assert "clean-room" in benchmark
    assert "npc suite" in benchmark
    assert "exact product identity was not unambiguously resolved" in benchmark
    assert "paid/cloud ai provider" in boundaries
