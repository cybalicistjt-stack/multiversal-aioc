import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


EXPECTED = ["GPR-01", "GPR-03", "GPR-05", "GPR-06", "GPR-07", "GPR-08", "GPR-09", "GPR-10", "GPR-12", "GPR-16"]


def test_gpr_pdcp_reduction_is_complete_and_non_authoritative():
    backlog = j("governance/application-planning/gameplay-pattern-runtime/GPR_PROGRAM_BACKLOG.json")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_GPR_REDUCTION_RECEIPT.json")
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == EXPECTED
    assert len(backlog["tranches"]) == 10
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])
    assert backlog["pdcp_reduction"]["baseline_tranche_count"] == 16
    assert backlog["pdcp_reduction"]["reduced_tranche_count"] == 10
    assert backlog["pdcp_reduction"]["stable_start_gate"] == "GPR-01"
    assert backlog["pdcp_reduction"]["stable_rotation_gate"] == "GPR-05"
    assert backlog["pdcp_reduction"]["stable_golden_gate"] == "GPR-16"
    assert backlog["pdcp_reduction"]["capability_loss_detected"] is False

    assert receipt["status"] == "resolved"
    assert receipt["implementation_authority"] is False
    assert receipt["baseline_tranche_count"] == 16
    assert receipt["reduced_tranche_count"] == 10
    assert receipt["removed_standalone_future_tranches"] == 6
    assert receipt["surviving_tranche_ids"] == EXPECTED
    assert len(receipt["baseline_dispositions"]) == 16
    assert {row["id"] for row in receipt["baseline_dispositions"]} == {f"GPR-{i:02d}" for i in range(1, 17)}
    assert receipt["golden_vector_count"] == 48
    assert receipt["dag_reconciliation"]["required"] is False

    gpr = next(x for x in ledger["families"] if x["program_id"] == "GPR")
    assert gpr["reduction_status"] == "resolved"
    assert gpr["reduced_tranche_count"] == 10
    assert gpr["surviving_tranche_ids"] == EXPECTED
    assert ledger["baseline_snapshot"]["effective_reduced_total"] == 153
    assert ledger["baseline_snapshot"]["approved_family_reductions"] == 5
    assert ledger["baseline_snapshot"]["removed_standalone_future_tranches"] == 55
    mrcs = next(x for x in ledger["families"] if x["program_id"] == "MRCS")
    assert mrcs["reduction_status"] == "next_selected_for_pdcp_review"


def test_gpr_fold_map_and_cross_owner_boundaries_are_explicit():
    backlog = j("governance/application-planning/gameplay-pattern-runtime/GPR_PROGRAM_BACKLOG.json")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_GPR_REDUCTION_RECEIPT.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()
    rows = {x["id"]: x for x in receipt["baseline_dispositions"]}

    assert rows["GPR-02"]["absorbed_into"] == "GPR-01"
    assert rows["GPR-04"]["absorbed_into"] == "GPR-05"
    assert rows["GPR-11"]["absorbed_into"] == "GPR-10"
    assert rows["GPR-13"]["absorbed_into"] == "GPR-12"
    assert rows["GPR-14"]["absorbed_into"] == "GPR-09"
    assert rows["GPR-15"]["disposition"] == "DESIGN_CLOSED_NO_STANDALONE"
    assert rows["GPR-15"]["absorbed_into"] == "GPR-16"

    for phrase in (
        "mal-01..10 remain completed_verified and frozen",
        "mrcs and canonical definition owners retain rule/content-definition authority",
        "action/event and canonical domain owners retain mutation truth",
        "packet 07 owns generic proposal/preview/dry-run/commit",
        "pca-12 and pdcp packet 08 own generic simulation/formal-analysis machinery",
        "ari/pca retain generic resource identity, rights",
        "gpr-15 no longer exists as a standalone tranche",
        "unknown owner data remains unknown",
    ):
        assert phrase in boundaries


def test_gpr_research_baseline_and_dag_milestones_are_preserved():
    baseline = j("governance/application-planning/gameplay-pattern-runtime/GPR_RESEARCH_BASELINE_v3.6.json")
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")
    backlog = j("governance/application-planning/gameplay-pattern-runtime/GPR_PROGRAM_BACKLOG.json")

    assert baseline["source_package"]["sha256"] == "e27eaeb46d26cd6693c6bf359a80196c5c73210ae6554df02816292f9fd567a3"
    assert baseline["corpus"]["games"] == 175
    assert baseline["corpus"]["reusable_patterns"] == 168
    assert baseline["corpus"]["gameplay_primitives"] == 461
    assert baseline["corpus"]["mechanics_api_modules"] == 29
    assert baseline["corpus"]["primitive_bound_operations_exercised"] == 85
    assert baseline["runtime_conformance"]["variant_cases_passed"] == 672
    assert len(baseline["delivery_modes"]) == 7

    assert graph["milestone_gates"]["rotation"]["GPR-01"] == ["MRCS-05"]
    assert "GPR-05" in graph["milestone_gates"]["rotation"]["MERA-01"]
    assert "GPR-16" in graph["milestone_gates"]["rotation"]["MSLR-01"]
    assert "GPR-16" in graph["milestone_gates"]["rotation"]["MSWI-01"]
    assert backlog["implementation_authority"] is False


def test_gpr_design_closure_preserves_delivery_conformance_and_accessibility():
    dcp = t("governance/application-planning/preimplementation-design-closure/PDCP_GPR_FAMILY_DESIGN_CLOSURE.md")
    program = t("governance/application-planning/gameplay-pattern-runtime/GPR_MULTIVERSAL_GAMEPLAY_PATTERN_RUNTIME_PROGRAM.md").lower()

    for i in range(1, 49):
        assert f"GPR-PDCP-{i:03d}" in dcp

    for mode in (
        "direct play",
        "cozy/low-pressure play",
        "gm-led play",
        "world-map/ttrpg bridge",
        "embedded minigame",
        "user-authored reusable loop mini",
        "multiversal roster injection",
    ):
        assert mode in program

    for phrase in (
        "168-pattern/85-operation/672-variant",
        "provider-off local operation",
        "equivalent nonvisual flow",
        "rights-safe presentation binding",
        "deterministic replay",
        "snapshot/restore",
        "successful reusable handoff to mera, mbes, mslr, mswi and smb",
    ):
        assert phrase in program

    assert "no gpr runtime branch or implementation authority exists" in program
