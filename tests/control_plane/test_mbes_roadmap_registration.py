import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_mbes_registered_as_future_interstitial_without_activation():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    registry = j("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    backlog = j("governance/application-planning/multiversal-built-environment-settlement/MBES_PROGRAM_BACKLOG.json")
    planned = {x["program_id"]: x for x in index["planned_programs"]}
    assert planned["MBES"]["status"] == "owner_approved_planned"
    assert planned["MBES"]["activation_after"] == "MRCS-21"
    assert planned["MBES"]["successor"] == "SMB-08"
    assert planned["MBES"]["implementation_authority"] is False
    assert planned["MBES"]["execution_units"] == 24
    assert planned["MRCS"]["successor"] == "MBES-01"
    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == [f"MBES-{i:02d}" for i in range(1, 25)]
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])
    assert index["current"]["source_program"] == "ARI"
    assert index["current"]["status"] == "selected_not_started"
    assert index["current"]["implementation_authority"] is False
    assert index["current"]["implementation_branch"] is None
    assert registry["active_planning_work"]["work_item"] == index["current"]["work_item_id"]
    assert registry["active_planning_work"]["implementation_authority"] is False


def test_mbes_dependency_placement_and_successors():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    mrcs = j("governance/application-planning/multiversal-rules-content-studio/MRCS_PROGRAM_BACKLOG.json")
    expected = "MAS-01..21 → MSAS-01..21 → MRCS-01..21 → MBES-01..24 → SMB-08 → SMB-09"
    assert expected in index["effective_forward_order"]
    assert index["mbes_execution_order"] == [f"MBES-{i:02d}" for i in range(1, 25)]
    assert mrcs["successor"] == "MBES-01"
    amendment = t("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_MBES_AMENDMENT_2026-09-11.md")
    successor = t("governance/application-planning/multiversal-rules-content-studio/MRCS_MBES_SUCCESSOR_AMENDMENT_2026-09-11.md")
    smb = t("governance/application-planning/system-maturation-buildout/SMB_MBES_INTERSTITIAL_INTEGRATION_AMENDMENT_2026-09-11.md")
    for doc in (amendment, successor, smb):
        assert "MRCS-01..21 → MBES-01..24 → SMB-08" in doc


def test_mbes_preserves_boundaries_and_world_reactivity():
    backlog = j("governance/application-planning/multiversal-built-environment-settlement/MBES_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()
    program = t("governance/application-planning/multiversal-built-environment-settlement/MBES_MULTIVERSAL_BUILT_ENVIRONMENT_SETTLEMENT_PROGRAM.md").lower()
    benchmark = t("governance/application-planning/multiversal-built-environment-settlement/MBES_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    for owner in ("mib-14", "mcs", "mrcs", "apw/d26", "mib-12", "mib-13", "icf", "odl", "scl", "world", "environment", "action/event"):
        assert owner in boundaries
    for level in ("settlement/district", "site/parcel", "structure", "level/zone", "space/room", "component/fixture", "connection/network"):
        assert level in boundaries
    assert "planetary sentience" in boundaries
    assert "pollution and over-development" in boundaries
    assert "generic reactive-world hooks" in boundaries
    assert "different branches, realities, worlds and environments" in boundaries
    assert "oara has planetary sentience" in program
    assert "equivalent development" in program
    assert "definition is not construction" in program
    assert "geometry is not truth" in program
    assert "clean-room" in benchmark
    assert "not permission to copy" in benchmark
    assert "no mbes runtime preflight or implementation authority exists now" in program


def test_mbes_golden_proof_spans_personal_to_regional_scale():
    program = t("governance/application-planning/multiversal-built-environment-settlement/MBES_MULTIVERSAL_BUILT_ENVIRONMENT_SETTLEMENT_PROGRAM.md").lower()
    for case in ("personalized player home", "homestead/farm/workshop", "hostile-environment", "manufacturing facility", "settlement/city district", "underground or submerged", "hydrology engineering", "multi-settlement regional network", "oara"):
        assert case in program
    assert "summary↔detail" in program
    assert "functional-space derivation" in program
    assert "local/offline" in program
