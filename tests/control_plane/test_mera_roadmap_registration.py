import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_mera_registered_without_current_authority():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    registry = j("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    backlog = j("governance/application-planning/multiversal-engineering-refit-assembly/MERA_PROGRAM_BACKLOG.json")
    planned = {x["program_id"]: x for x in index["planned_programs"]}

    assert planned["MERA"]["status"] == "owner_approved_planned"
    assert planned["MERA"]["activation_after"] == "MRCS-21"
    assert planned["MERA"]["successor"] == "MBES-01"
    assert planned["MERA"]["implementation_authority"] is False
    assert planned["MERA"]["execution_units"] == 24
    assert planned["MRCS"]["successor"] == "MERA-01"
    assert planned["MBES"]["activation_after"] == "MERA-24"

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == [f"MERA-{i:02d}" for i in range(1, 25)]
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])

    assert index["current"]["work_item_id"] == "ARI-16"
    assert index["current"]["status"] == "selected_not_started"
    assert index["current"]["implementation_authority"] is False
    assert index["current"]["implementation_branch"] is None
    assert registry["active_planning_work"]["work_item"] == "ARI-16"
    assert registry["active_planning_work"]["implementation_authority"] is False


def test_mera_order_and_crosslinks():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    mrcs = j("governance/application-planning/multiversal-rules-content-studio/MRCS_PROGRAM_BACKLOG.json")
    mera = j("governance/application-planning/multiversal-engineering-refit-assembly/MERA_PROGRAM_BACKLOG.json")
    mbes = j("governance/application-planning/multiversal-built-environment-settlement/MBES_PROGRAM_BACKLOG.json")

    assert "MRCS-01..21 → MERA-01..24 → MBES-01..24 → SMB-08" in index["effective_forward_order"]
    assert index["mera_execution_order"] == [f"MERA-{i:02d}" for i in range(1, 25)]
    assert mrcs["successor"] == "MERA-01"
    assert mera["successor"] == "MBES-01"
    assert mbes["activation_after"] == "MERA-24"

    amendment = t("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_MERA_AMENDMENT_2026-09-11.md")
    successor = t("governance/application-planning/multiversal-rules-content-studio/MRCS_MERA_SUCCESSOR_AMENDMENT_2026-09-11.md")
    predecessor = t("governance/application-planning/multiversal-built-environment-settlement/MBES_MERA_PREDECESSOR_AMENDMENT_2026-09-11.md")
    for doc in (amendment, successor, predecessor):
        assert "MRCS-01..21 → MERA-01..24 → MBES-01..24" in doc


def test_mera_preserves_owner_boundaries_and_resolution_ladder():
    backlog = j("governance/application-planning/multiversal-engineering-refit-assembly/MERA_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()
    program = t("governance/application-planning/multiversal-engineering-refit-assembly/MERA_MULTIVERSAL_ENGINEERING_REFIT_ASSEMBLY_PROGRAM.md").lower()
    benchmark = t("governance/application-planning/multiversal-engineering-refit-assembly/MERA_BENCHMARK_CAPABILITY_MATRIX.md").lower()

    for owner in ("lss", "ppia-03", "d17", "mib-12", "mib-13", "mib-14", "ppia-04", "f014", "apw/d26", "dpl", "mrcs", "ari", "mbes"):
        assert owner in boundaries

    for level in ("asset", "system", "assembly", "subassembly", "component", "interface/connection", "governed network"):
        assert level in boundaries

    assert "unknown or source-unspecified" in boundaries
    assert "blueprint, proposed configuration, dry-run or simulation is non-authoritative" in boundaries
    assert "no 3d renderer" in boundaries
    assert "schematic and semantic" in program
    assert "simulation before commitment" in program
    assert "unknown is not zero" in program
    assert "no mera runtime preflight or implementation authority exists now" in program
    assert "clean-room" in benchmark
    assert "not permission to copy" in benchmark


def test_mera_golden_proof_spans_items_vehicles_mecha_and_starships():
    program = t("governance/application-planning/multiversal-engineering-refit-assembly/MERA_MULTIVERSAL_ENGINEERING_REFIT_ASSEMBLY_PROGRAM.md").lower()
    for case in (
        "damaged ordinary item",
        "weapon or armor configuration",
        "vehicle repaired with a compatible donor component",
        "mecha refit",
        "starship subsystem failure",
        "jury-rigged repair",
        "partial teardown",
        "condition changes recoverability",
        "incompatible configuration",
        "unknown source data",
        "project/profession/tool/workstation/time",
        "local/offline",
        "nonvisual engineering",
        "handoff into mbes",
    ):
        assert case in program
