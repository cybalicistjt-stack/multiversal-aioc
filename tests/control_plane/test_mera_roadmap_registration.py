import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


EXPECTED = ["MERA-01", "MERA-03", "MERA-05", "MERA-06", "MERA-07", "MERA-10", "MERA-12", "MERA-13", "MERA-16", "MERA-24"]


def test_mera_pdcp_reduction_is_complete_and_non_authoritative():
    backlog = j("governance/application-planning/multiversal-engineering-refit-assembly/MERA_PROGRAM_BACKLOG.json")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MERA_REDUCTION_RECEIPT.json")
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == EXPECTED
    assert len(backlog["tranches"]) == 10
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])
    assert backlog["pdcp_reduction"]["baseline_tranche_count"] == 24
    assert backlog["pdcp_reduction"]["reduced_tranche_count"] == 10
    assert backlog["pdcp_reduction"]["stable_start_gate"] == "MERA-01"
    assert backlog["pdcp_reduction"]["stable_golden_gate"] == "MERA-24"
    assert backlog["pdcp_reduction"]["capability_loss_detected"] is False

    assert receipt["status"] == "resolved"
    assert receipt["implementation_authority"] is False
    assert receipt["baseline_tranche_count"] == 24
    assert receipt["reduced_tranche_count"] == 10
    assert receipt["removed_standalone_future_tranches"] == 14
    assert receipt["surviving_tranche_ids"] == EXPECTED
    assert len(receipt["baseline_dispositions"]) == 24
    assert {row["id"] for row in receipt["baseline_dispositions"]} == {f"MERA-{i:02d}" for i in range(1, 25)}
    assert receipt["golden_vector_count"] == 48
    assert receipt["dag_reconciliation"]["required"] is False

    mera = next(x for x in ledger["families"] if x["program_id"] == "MERA")
    assert mera["reduction_status"] == "resolved"
    assert mera["reduced_tranche_count"] == 10
    assert mera["surviving_tranche_ids"] == EXPECTED
    assert ledger["baseline_snapshot"]["effective_reduced_total"] == 159
    assert ledger["baseline_snapshot"]["approved_family_reductions"] == 4
    assert ledger["baseline_snapshot"]["removed_standalone_future_tranches"] == 49


def test_mera_cross_owner_absorptions_and_shared_substrate_are_explicit():
    backlog = j("governance/application-planning/multiversal-engineering-refit-assembly/MERA_PROGRAM_BACKLOG.json")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MERA_REDUCTION_RECEIPT.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()
    rows = {x["id"]: x for x in receipt["baseline_dispositions"]}

    for tranche in ("MERA-17", "MERA-18", "MERA-19", "MERA-21"):
        assert rows[tranche]["disposition"] == "ABSORB_EXISTING_OWNER"
        assert rows[tranche]["survives_as"] is None

    for owner in (
        "lss", "mib-12", "ppia-03", "d17", "mib-14", "ppia-04", "f014",
        "apw/d26", "dpl/profession", "mrcs", "gpr", "pca-12", "packet 08",
        "packet 07", "ari/pca", "reduced mbes"
    ):
        assert owner in boundaries

    assert "vehicle, mecha and starship engineering use one ppia-04-backed adapter family" in boundaries
    assert "machinery/robotics/construct/industrial engineering remains a distinct adapter seam" in boundaries
    assert "unknown or source-unspecified" in boundaries
    assert "no universal formula" in boundaries


def test_mera_dag_milestones_remain_stable():
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")
    backlog = j("governance/application-planning/multiversal-engineering-refit-assembly/MERA_PROGRAM_BACKLOG.json")

    assert "MERA-04" in graph["program_edges"]["MBES"]["start_requires"]
    assert "MERA-24" in graph["program_edges"]["MBES"]["golden_proof_requires"]
    assert graph["milestone_gates"]["rotation"]["MERA-01"] == ["GPR-05", "MRCS-13"]
    assert backlog["implementation_authority"] is False


def test_mera_design_closure_preserves_golden_scope_and_accessibility():
    dcp = t("governance/application-planning/preimplementation-design-closure/PDCP_MERA_FAMILY_DESIGN_CLOSURE.md")
    program = t("governance/application-planning/multiversal-engineering-refit-assembly/MERA_MULTIVERSAL_ENGINEERING_REFIT_ASSEMBLY_PROGRAM.md").lower()

    for i in range(1, 49):
        assert f"MERA-PDCP-{i:03d}" in dcp

    for phrase in (
        "damaged ordinary item",
        "weapon/armor proposal",
        "compatible donor component",
        "vehicle/mecha/starship engineering flow",
        "machinery/robotics/construct flow",
        "partial teardown",
        "incompatible and unknown-source",
        "provider-off local operation",
        "equivalent nonvisual operation",
        "handoff into reduced mbes",
    ):
        assert phrase in program

    assert "no 3d renderer" in program
    assert "optional ai is advisory only" in program
    assert "no mera implementation authority exists" in program
