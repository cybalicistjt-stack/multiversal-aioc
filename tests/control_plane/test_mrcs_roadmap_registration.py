import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_mrcs_reduced_family_contract_and_no_authority():
    backlog = j("governance/application-planning/multiversal-rules-content-studio/MRCS_PROGRAM_BACKLOG.json")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MRCS_REDUCTION_RECEIPT.json")
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")

    expected = ["MRCS-01","MRCS-03","MRCS-04","MRCS-05","MRCS-08","MRCS-11","MRCS-12","MRCS-13","MRCS-14","MRCS-16","MRCS-17","MRCS-19","MRCS-21"]
    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == expected
    assert len(backlog["tranches"]) == 13
    assert all(x["estimated_active_minutes"] <= 16 for x in backlog["tranches"])
    assert backlog["pdcp_reduction"]["baseline_tranche_count"] == 21
    assert backlog["pdcp_reduction"]["reduced_tranche_count"] == 13
    assert backlog["pdcp_reduction"]["capability_loss_detected"] is False

    assert receipt["status"] == "resolved"
    assert receipt["implementation_authority"] is False
    assert receipt["baseline_tranche_count"] == 21
    assert receipt["reduced_tranche_count"] == 13
    assert receipt["removed_standalone_future_tranches"] == 8
    assert len(receipt["dispositions"]) == 21
    assert {x["baseline_id"] for x in receipt["dispositions"]} == {f"MRCS-{i:02d}" for i in range(1, 22)}
    assert receipt["surviving_tranche_ids"] == expected
    assert receipt["golden_vector_count"] == 48
    assert receipt["roadmap_dependency_graph_mutation_required"] is False
    assert receipt["ops3_current_mutation"] is False

    row = {x["program_id"]: x for x in ledger["families"]}["MRCS"]
    assert row["reduction_status"] == "resolved"
    assert row["reduced_tranche_count"] == 13
    assert row["surviving_tranche_ids"] == expected
    assert ledger["baseline_snapshot"]["effective_reduced_total"] == 145
    assert ledger["baseline_snapshot"]["removed_standalone_future_tranches"] == 63
    assert {x["program_id"] for x in ledger["families"] if x["reduction_status"] == "next_selected_for_pdcp_review"} == {"MSAS"}


def test_mrcs_preserves_stable_dag_milestones_and_owner_boundaries():
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")
    backlog = j("governance/application-planning/multiversal-rules-content-studio/MRCS_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()
    graph_text = json.dumps(graph)

    for milestone in ("MRCS-05", "MRCS-13", "MRCS-14", "MRCS-21"):
        assert milestone in graph_text
        assert milestone in set(backlog["strict_order"])

    for owner in ("content forge", "cab", "cni", "reduced gpr", "action/event", "pca-12", "packet 07", "ari/pca", "mcs", "mccs", "mncs", "msas", "mera", "mbes"):
        assert owner in boundaries

    assert "no mrcs implementation authority" in boundaries
    assert "unrestricted scripting" in boundaries
    assert "paid/cloud providers" in boundaries


def test_mrcs_reduction_keeps_distinct_high_risk_authoring_seams():
    backlog = j("governance/application-planning/multiversal-rules-content-studio/MRCS_PROGRAM_BACKLOG.json")
    names = "\n".join(x["name"] for x in backlog["tranches"]).lower()
    program = t("governance/application-planning/multiversal-rules-content-studio/MRCS_MULTIVERSAL_RULES_CONTENT_STUDIO_PROGRAM.md").lower()

    for term in (
        "schema-aware forms",
        "guided forge interviews",
        "expression workbench",
        "mechanical & advancement",
        "magic, power & casting-system",
        "creature, monster, npc role",
        "item, equipment, vehicle",
        "environment, hazard, encounter",
        "system extension, house rule",
        "dependency, impact, safe refactoring, balance",
        "import, repair, migration, pack",
        "golden cross-domain",
    ):
        assert term in names

    assert "definition authoring" in program
    assert "not a canonical rules engine" in program
    assert "13 surviving tranches" in program
    assert "full 48-vector pdcp battery" in program


def test_mrcs_dcp_preserves_all_golden_vectors_and_cross_owner_absorptions():
    dcp = t("governance/application-planning/preimplementation-design-closure/PDCP_MRCS_FAMILY_DESIGN_CLOSURE.md")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MRCS_REDUCTION_RECEIPT.json")

    assert dcp.count("`0") >= 8
    for n in range(1, 49):
        token = f"{n:03d}"
        assert token in dcp
    owners = "\n".join(x["owner"] for x in receipt["cross_family_absorptions"]).lower()
    assert "pca-12" in owners
    assert "packet 07" in owners
    assert "ari + pca" in owners
    assert "reduced gpr" in owners
