import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_pdcp_is_design_only_and_cannot_select_product_work():
    current = j("operations/CURRENT.json")
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")

    assert ledger["project_id"] == "PDCP"
    assert ledger["implementation_authority"] is False
    assert ledger["ops3_current_mutation"] is False
    assert "PDCP" not in graph["nodes"]
    assert current["lanes"]["product-development"]["selected_work_item"] != "PDCP"


def test_pdcp_excludes_mas_and_snapshots_all_newer_future_families():
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")
    families = {row["program_id"]: row["baseline_tranche_count"] for row in ledger["families"]}

    assert ledger["excluded_programs"] == ["MAS"]
    assert "MAS" not in families
    assert families == {
        "MCS": 21,
        "MCCS": 21,
        "MNCS": 24,
        "MSAS": 21,
        "MRCS": 21,
        "GPR": 16,
        "MERA": 24,
        "MBES": 24,
        "MSLR": 18,
        "MSWI": 18,
    }
    assert sum(families.values()) == 208
    assert ledger["baseline_snapshot"]["baseline_total_tranches"] == 208
    assert ledger["baseline_snapshot"]["effective_reduced_total"] is None


def test_pdcp_baseline_sources_exist_and_are_still_future_planned_at_snapshot():
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")

    for row in ledger["families"]:
        backlog = j(row["backlog_path"])
        assert backlog["program_id"] == row["program_id"]
        assert backlog["status"] == "owner_approved_planned"
        assert backlog["implementation_authority"] is False
        assert len(backlog["strict_order"]) == row["baseline_tranche_count"]
        assert len(backlog["tranches"]) == row["baseline_tranche_count"]


def test_pdcp_reduction_contract_preserves_scope_and_ops3_gates():
    project = t("governance/application-planning/preimplementation-design-closure/PDCP_PREIMPLEMENTATION_DESIGN_CLOSURE_PROJECT.md").lower()
    contract = t("governance/application-planning/preimplementation-design-closure/PDCP_DESIGN_CLOSURE_CONTRACT.md").lower()
    amendment = t("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_PDCP_AMENDMENT_2026-09-16.md").lower()
    combined = project + "\n" + contract + "\n" + amendment

    for required in (
        "operations/current.json",
        "roadmap_dependency_graph.json",
        "golden proof",
        "implementation authority",
        "before/after",
        "capability",
        "mas is excluded",
    ):
        assert required in combined

    assert "no predetermined reduction percentage" in project
    assert "research/design closure is not software completion" in project
    assert "do not mutate `operations/current.json`" in contract


def test_pdcp_cross_family_register_tracks_eight_initial_packets():
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")
    register = t("governance/application-planning/preimplementation-design-closure/PDCP_BENCHMARK_CAPABILITY_REGISTER.md").lower()

    assert len(ledger["cross_family_capability_packets"]) == 8
    for phrase in (
        "social interaction grammar",
        "systemic investigation",
        "autonomous actors",
        "semantic affordances",
        "persistent history",
        "multi-resolution simulation",
        "creator/gm execution ux",
        "formal validation",
    ):
        assert phrase in register
