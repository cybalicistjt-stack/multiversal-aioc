import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


SURVIVORS = ["MSWI-01", "MSWI-03", "MSWI-04", "MSWI-06", "MSWI-07", "MSWI-14", "MSWI-18"]


def test_mswi_is_future_planned_without_current_authority():
    current = j("operations/CURRENT.json")
    backlog = j("governance/application-planning/multiversal-systemic-worldplay-integration/MSWI_PROGRAM_BACKLOG.json")

    product = current["lanes"]["product-development"]
    assert product["selected_work_item"] != "MSWI-01"
    assert backlog["status"] == "owner_approved_planned"
    assert backlog["implementation_authority"] is False
    assert backlog["activation_after"] == "MSLR-18"
    assert backlog["successor"] == "SMB-08"


def test_mswi_uses_pdcp_reduced_bounded_one_continue_family_design():
    backlog = j("governance/application-planning/multiversal-systemic-worldplay-integration/MSWI_PROGRAM_BACKLOG.json")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MSWI_REDUCTION_RECEIPT.json")

    assert backlog["tranche_execution_target_minutes"] == 24
    assert backlog["minimum_closeout_reserve_minutes"] == 8
    assert backlog["split_before_start_if_target_not_credible"] is True
    assert backlog["strict_order"] == SURVIVORS
    assert [x["id"] for x in backlog["tranches"]] == SURVIVORS
    assert all(x["estimated_active_minutes"] <= 16 for x in backlog["tranches"])

    assert backlog["pdcp_reduction"]["baseline_tranche_count"] == 18
    assert backlog["pdcp_reduction"]["reduced_tranche_count"] == 7
    assert backlog["pdcp_reduction"]["stable_start_gate"] == "MSWI-01"
    assert backlog["pdcp_reduction"]["stable_golden_gate"] == "MSWI-18"
    assert backlog["pdcp_reduction"]["capability_loss_detected"] is False

    assert receipt["status"] == "family_reduction_resolved"
    assert receipt["baseline_tranche_count"] == 18
    assert receipt["reduced_tranche_count"] == 7
    assert receipt["tranches_removed_or_merged"] == 11
    assert receipt["effective_strict_order"] == SURVIVORS
    assert receipt["capability_loss_check"] == "pass"
    assert len(receipt["baseline_rows"]) == 18
    assert all(row["capability_loss_check"] == "pass" for row in receipt["baseline_rows"])

    design = "\n".join(backlog["execution_design"].values()).lower()
    assert "one owner continue" in design
    assert "dependency closure" in design
    assert "reserve" in design
    assert "unchanged deterministic failure" in design


def test_mswi_preserves_dag_start_and_golden_gates_after_reduction():
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")

    assert graph["status"] == "CURRENT_PLANNING_AUTHORITY"
    assert graph["nodes"]["MSWI"]["implementation_authority"] is False
    assert "MBES" in graph["program_edges"]["MSWI"]["hard_requires"]
    assert "MSLR" in graph["program_edges"]["MSWI"]["hard_requires"]
    assert "MSLR-18" in graph["program_edges"]["MSWI"]["start_requires"]
    assert "GPR-16" in graph["program_edges"]["MSWI"]["start_requires"]
    assert "MNCS-24" in graph["program_edges"]["MSWI"]["start_requires"]
    assert graph["program_edges"]["MSWI"]["golden_proof_requires"] == ["MSWI-18"]
    assert "MSWI-18" in graph["program_edges"]["SMB08"]["start_requires"]
    assert graph["milestone_gates"]["rotation"]["MSWI-01"] == ["MSLR-18", "GPR-16", "MNCS-24"]


def test_mswi_reduction_resolves_intra_and_cross_family_overlap():
    backlog = j("governance/application-planning/multiversal-systemic-worldplay-integration/MSWI_PROGRAM_BACKLOG.json")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MSWI_REDUCTION_RECEIPT.json")
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")
    program = t("governance/application-planning/multiversal-systemic-worldplay-integration/MSWI_MULTIVERSAL_SYSTEMIC_WORLDPLAY_INTEGRATION_PROGRAM.md").lower()
    dcp = t("governance/application-planning/preimplementation-design-closure/PDCP_MSWI_FAMILY_DESIGN_CLOSURE.md").lower()
    overlap = t("governance/application-planning/preimplementation-design-closure/PDCP_CROSS_FAMILY_OVERLAP_REGISTER.md").lower()
    boundaries = "\n".join(backlog["boundaries"]).lower()

    clusters = receipt["intra_family_overlap_clusters"]
    assert ["MSWI-01", "MSWI-02"] in clusters
    assert ["MSWI-04", "MSWI-05"] in clusters
    assert ["MSWI-07", "MSWI-08"] in clusters
    assert ["MSWI-14", "MSWI-15", "MSWI-16"] in clusters
    assert ["MSWI-17", "MSWI-18"] in clusters

    disposition = {row["baseline_id"]: row["disposition"] for row in receipt["baseline_rows"]}
    for absorbed in ("MSWI-09", "MSWI-10", "MSWI-11", "MSWI-12", "MSWI-13"):
        assert disposition[absorbed] == "ABSORB_EXISTING_OWNER"

    for owner in ("dpl", "gpr", "project/time", "religion/culture/organization", "pca-12", "pca-02/pca-03", "mcs", "mas", "msas"):
        assert owner in (boundaries + "\n" + program + "\n" + dcp)

    assert "pursuit" in dcp and "gpr" in dcp
    assert "interaction density" in dcp or "interaction-density" in dcp
    assert "no universal ecological equation" in dcp
    assert "permission filtering" in dcp
    assert "accessible" in dcp
    assert "36" in dcp
    assert "result: **18 → 7**" in overlap

    mswi = next(x for x in ledger["families"] if x["program_id"] == "MSWI")
    assert mswi["reduction_status"] == "resolved"
    assert mswi["reduced_tranche_count"] == 7
    assert mswi["overlap_audit_complete"] is True
    assert mswi["capability_loss_detected"] is False


def test_mswi_clean_room_and_provider_off_guards_remain():
    backlog = j("governance/application-planning/multiversal-systemic-worldplay-integration/MSWI_PROGRAM_BACKLOG.json")
    matrix = t("governance/application-planning/multiversal-systemic-worldplay-integration/MSWI_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    dcp = t("governance/application-planning/preimplementation-design-closure/PDCP_MSWI_FAMILY_DESIGN_CLOSURE.md").lower()
    boundaries = "\n".join(backlog["boundaries"]).lower()

    assert "protected code" in matrix
    assert "clean-room" in boundaries
    assert "no paid/cloud provider" in boundaries
    assert "optional ai" in boundaries
    assert "provider-off" in dcp
