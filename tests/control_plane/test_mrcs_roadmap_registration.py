import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_mrcs_registered_as_future_interstitial_without_activation():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    registry = j("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    backlog = j("governance/application-planning/multiversal-rules-content-studio/MRCS_PROGRAM_BACKLOG.json")

    planned = {x["program_id"]: x for x in index["planned_programs"]}
    assert planned["MRCS"]["status"] == "owner_approved_planned"
    assert planned["MRCS"]["activation_after"] == "MSAS-21"
    assert planned["MRCS"]["successor"] == "GPR-01"
    assert planned["MRCS"]["implementation_authority"] is False
    assert planned["MRCS"]["execution_units"] == 21
    assert planned["MSAS"]["successor"] == "MRCS-01"

    assert backlog["implementation_authority"] is False
    assert backlog["successor"] == "GPR-01"
    assert backlog["strict_order"] == [f"MRCS-{i:02d}" for i in range(1, 22)]
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])

    assert index["current"]["source_program"] == "ARI"
    assert index["current"]["status"] == "selected_not_started"
    assert index["current"]["implementation_authority"] is False
    assert index["current"]["implementation_branch"] is None
    assert registry["active_planning_work"]["work_item"] == index["current"]["work_item_id"]
    assert registry["active_planning_work"]["implementation_authority"] is False


def test_mrcs_dependency_placement_and_successors():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    msas = j("governance/application-planning/multiversal-sound-audio-studio/MSAS_PROGRAM_BACKLOG.json")
    mrcs = j("governance/application-planning/multiversal-rules-content-studio/MRCS_PROGRAM_BACKLOG.json")
    gpr = j("governance/application-planning/gameplay-pattern-runtime/GPR_PROGRAM_BACKLOG.json")

    expected = "MNCS-01..24 → MAS-01..21 → MSAS-01..21 → MRCS-01..21 → GPR-01..16 → MERA-01..24 → MBES-01..24 → SMB-08 → SMB-09"
    assert expected in index["effective_forward_order"]
    assert index["mrcs_execution_order"] == [f"MRCS-{i:02d}" for i in range(1, 22)]
    assert msas["successor"] == "MRCS-01"
    assert mrcs["successor"] == "GPR-01"
    assert gpr["activation_after"] == "MRCS-21"

    amendment = t("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_GPR_AMENDMENT_2026-09-11.md")
    successor = t("governance/application-planning/multiversal-rules-content-studio/MRCS_GPR_SUCCESSOR_AMENDMENT_2026-09-11.md")
    assert "MRCS-01..21 → GPR-01..16 → MERA-01..24 → MBES-01..24" in amendment
    assert "MRCS-01..21 → GPR-01..16 → MERA-01..24 → MBES-01..24" in successor


def test_mrcs_preserves_content_forge_cab_and_owner_boundaries():
    backlog = j("governance/application-planning/multiversal-rules-content-studio/MRCS_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()
    for owner in ("content forge", "cab", "cni", "ari", "action/event", "mcs", "mccs", "mas", "msas", "gpr", "mera", "mbes"):
        assert owner in boundaries

    benchmark = t("governance/application-planning/multiversal-rules-content-studio/MRCS_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    program = t("governance/application-planning/multiversal-rules-content-studio/MRCS_MULTIVERSAL_RULES_CONTENT_STUDIO_PROGRAM.md").lower()
    forge = t("docs/FORGE_SYSTEM_DESIGN_v8.md").lower()
    assert "clean-room" in benchmark
    assert "not permission to copy" in benchmark
    assert "the author thinks in creative terms" in forge
    assert "not a new canonical rules engine" in program
    assert "definition is not instance" in program
    assert "cab" in program
    assert "no mrcs runtime preflight or implementation authority exists now" in program


def test_mrcs_requires_pack_dependency_balance_and_legacy_evidence():
    backlog = j("governance/application-planning/multiversal-rules-content-studio/MRCS_PROGRAM_BACKLOG.json")
    names = "\n".join(x["name"] for x in backlog["tranches"]).lower()
    boundaries = "\n".join(backlog["boundaries"]).lower()
    program = t("governance/application-planning/multiversal-rules-content-studio/MRCS_MULTIVERSAL_RULES_CONTENT_STUDIO_PROGRAM.md").lower()

    for term in ("dependency", "balance", "bulk import", "pack lists", "system extension", "ability", "species", "item", "spell", "creature"):
        assert term in names
    assert "legacy import" in program
    assert "provenance" in boundaries
    assert "unrestricted scripting" in boundaries
    assert "paid/cloud provider" in boundaries
