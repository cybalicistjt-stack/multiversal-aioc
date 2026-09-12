import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_gpr_registered_as_future_interstitial_without_current_authority():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    registry = j("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    backlog = j("governance/application-planning/gameplay-pattern-runtime/GPR_PROGRAM_BACKLOG.json")
    planned = {x["program_id"]: x for x in index["planned_programs"]}

    assert planned["GPR"]["status"] == "owner_approved_planned"
    assert planned["GPR"]["activation_after"] == "MRCS-21"
    assert planned["GPR"]["successor"] == "MERA-01"
    assert planned["GPR"]["implementation_authority"] is False
    assert planned["GPR"]["execution_units"] == 16
    assert planned["MRCS"]["successor"] == "GPR-01"
    assert planned["MERA"]["activation_after"] == "GPR-16"

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == [f"GPR-{i:02d}" for i in range(1, 17)]
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])

    assert index["current"]["work_item_id"] == "ARI-16"
    assert index["current"]["status"] == "selected_not_started"
    assert index["current"]["implementation_authority"] is False
    assert registry["active_planning_work"]["work_item"] == "ARI-16"
    assert registry["active_planning_work"]["implementation_authority"] is False


def test_gpr_baseline_preserves_verified_scope_and_rights_boundary():
    baseline = j("governance/application-planning/gameplay-pattern-runtime/GPR_RESEARCH_BASELINE_v3.6.json")
    program = t("governance/application-planning/gameplay-pattern-runtime/GPR_MULTIVERSAL_GAMEPLAY_PATTERN_RUNTIME_PROGRAM.md").lower()
    backlog = j("governance/application-planning/gameplay-pattern-runtime/GPR_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()

    assert baseline["source_package"]["sha256"] == "e27eaeb46d26cd6693c6bf359a80196c5c73210ae6554df02816292f9fd567a3"
    assert baseline["corpus"]["games"] == 175
    assert baseline["corpus"]["reusable_patterns"] == 168
    assert baseline["corpus"]["gameplay_primitives"] == 461
    assert baseline["corpus"]["mechanics_api_modules"] == 29
    assert baseline["corpus"]["primitive_bound_operations_exercised"] == 85
    assert baseline["runtime_conformance"]["variant_cases_passed"] == 672
    assert len(baseline["delivery_modes"]) == 7
    assert "reference/evidence only" in boundaries
    assert "mal-01..10 remain completed_verified and frozen" in boundaries
    assert "source-rom assets" in boundaries
    assert "composition instead of game forks" in program


def test_gpr_dependency_position_and_handoffs():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    mrcs = j("governance/application-planning/multiversal-rules-content-studio/MRCS_PROGRAM_BACKLOG.json")
    gpr = j("governance/application-planning/gameplay-pattern-runtime/GPR_PROGRAM_BACKLOG.json")
    mera = j("governance/application-planning/multiversal-engineering-refit-assembly/MERA_PROGRAM_BACKLOG.json")

    assert "MRCS-01..21 → GPR-01..16 → MERA-01..24 → MBES-01..24 → SMB-08" in index["effective_forward_order"]
    assert index["gpr_execution_order"] == [f"GPR-{i:02d}" for i in range(1, 17)]
    assert mrcs["successor"] == "GPR-01"
    assert gpr["activation_after"] == "MRCS-21"
    assert gpr["successor"] == "MERA-01"
    assert mera["activation_after"] == "GPR-16"

    amendment = t("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_GPR_AMENDMENT_2026-09-11.md")
    assert "supersedes only the MRCS→MERA direct successor wiring" in amendment
    assert "ARI-16 remains the selected live work item" in amendment


def test_gpr_covers_runtime_authoring_delivery_and_conformance():
    backlog = j("governance/application-planning/gameplay-pattern-runtime/GPR_PROGRAM_BACKLOG.json")
    names = "\n".join(x["name"] for x in backlog["tranches"]).lower()
    program = t("governance/application-planning/gameplay-pattern-runtime/GPR_MULTIVERSAL_GAMEPLAY_PATTERN_RUNTIME_PROGRAM.md").lower()

    for term in ("semantic gameplay registry", "deterministic state kernel", "loop-mini contract", "seven delivery modes",
                 "asset-role binding", "multiplayer/co-op", "snapshot migration", "creator/gm loop studio",
                 "168-pattern", "golden cross-system gameplay runtime"):
        assert term in names
    for mode in ("direct play", "cozy", "gm-led", "world-map / ttrpg", "embedded minigame", "user-authored", "roster injection"):
        assert mode in program
    assert "no gpr runtime preflight, branch or implementation authority exists now" in program
