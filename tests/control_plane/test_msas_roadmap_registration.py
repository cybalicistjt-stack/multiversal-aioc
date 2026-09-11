import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_msas_registered_as_future_interstitial_without_activation():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    registry = j("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    backlog = j("governance/application-planning/multiversal-sound-audio-studio/MSAS_PROGRAM_BACKLOG.json")

    planned = {x["program_id"]: x for x in index["planned_programs"]}
    assert planned["MSAS"]["status"] == "owner_approved_planned"
    assert planned["MSAS"]["activation_after"] == "MAS-21"
    assert planned["MSAS"]["successor"] == "SMB-08"
    assert planned["MSAS"]["implementation_authority"] is False
    assert planned["MSAS"]["execution_units"] == 21
    assert planned["MAS"]["successor"] == "MSAS-01"

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == [f"MSAS-{i:02d}" for i in range(1, 22)]
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])

    assert index["current"]["source_program"] == "ARI"
    assert index["current"]["status"] == "selected_not_started"
    assert index["current"]["implementation_authority"] is False
    assert index["current"]["implementation_branch"] is None
    assert registry["active_planning_work"]["work_item"] == index["current"]["work_item_id"]
    assert registry["active_planning_work"]["implementation_authority"] is False


def test_msas_dependency_placement_and_successors():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    mas = j("governance/application-planning/multiversal-adventure-studio/MAS_PROGRAM_BACKLOG.json")
    pca = j("governance/application-planning/production-capability-acceleration/PCA_PROGRAM_BACKLOG.json")

    expected = "CNI-01..13 → PCA-01..16 → MCS-01..21 → MCCS-01..21 → MAS-01..21 → MSAS-01..21 → SMB-08 → SMB-09"
    assert expected in index["effective_forward_order"]
    assert index["msas_execution_order"] == [f"MSAS-{i:02d}" for i in range(1, 22)]
    assert mas["successor"] == "MSAS-01"
    assert pca["successor"] == "MCS-01"

    amendment = t("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_MSAS_AMENDMENT_2026-09-11.md")
    successor = t("governance/application-planning/multiversal-adventure-studio/MAS_MSAS_SUCCESSOR_AMENDMENT_2026-09-11.md")
    smb = t("governance/application-planning/system-maturation-buildout/SMB_MSAS_INTERSTITIAL_INTEGRATION_AMENDMENT_2026-09-11.md")
    for doc in (amendment, successor, smb):
        assert "MAS-01..21 → MSAS-01..21 → SMB-08" in doc


def test_msas_preserves_audio_owners_clean_room_and_live_truth_boundaries():
    backlog = j("governance/application-planning/multiversal-sound-audio-studio/MSAS_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()
    for owner in ("aai", "dwc", "ari", "pca", "world", "environment", "scene", "adventure", "combat", "dialogue", "action/event"):
        assert owner in boundaries

    benchmark = t("governance/application-planning/multiversal-sound-audio-studio/MSAS_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    program = t("governance/application-planning/multiversal-sound-audio-studio/MSAS_MULTIVERSAL_SOUND_AUDIO_STUDIO_PROGRAM.md").lower()
    assert "clean-room" in benchmark
    assert "does not copy" in benchmark
    assert "prepared cue" in program
    assert "never proves" in program
    assert "local-first" in program
    assert "no msas implementation authority exists now" in program
