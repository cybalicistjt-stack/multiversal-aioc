import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


SURVIVORS = ["MBES-01", "MBES-03", "MBES-05", "MBES-08", "MBES-12", "MBES-14", "MBES-18", "MBES-20", "MBES-24"]


def test_mbes_is_pdcp_reduced_future_work_without_authority():
    current = j("operations/CURRENT.json")
    backlog = j("governance/application-planning/multiversal-built-environment-settlement/MBES_PROGRAM_BACKLOG.json")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MBES_REDUCTION_RECEIPT.json")

    assert backlog["status"] == "owner_approved_planned"
    assert backlog["implementation_authority"] is False
    assert backlog["pdcp_reduction"]["baseline_tranche_count"] == 24
    assert backlog["pdcp_reduction"]["reduced_tranche_count"] == 9
    assert backlog["pdcp_reduction"]["capability_loss_detected"] is False
    assert backlog["strict_order"] == SURVIVORS
    assert [x["id"] for x in backlog["tranches"]] == SURVIVORS
    assert all(x["estimated_active_minutes"] <= 16 for x in backlog["tranches"])

    assert receipt["status"] == "family_reduction_resolved"
    assert receipt["surviving_strict_order"] == SURVIVORS
    assert len(receipt["baseline_rows"]) == 24
    assert all(x["capability_loss_check"] == "pass" for x in receipt["baseline_rows"])

    assert current["lanes"]["product-development"]["selected_work_item"] != "MBES-01"


def test_mbes_preserves_current_dag_milestones():
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")
    backlog = j("governance/application-planning/multiversal-built-environment-settlement/MBES_PROGRAM_BACKLOG.json")

    assert graph["status"] == "CURRENT_PLANNING_AUTHORITY"
    assert graph["nodes"]["MBES"]["implementation_authority"] is False
    assert "MERA" in graph["program_edges"]["MBES"]["hard_requires"]
    assert "MERA-03" in graph["program_edges"]["MBES"]["start_requires"]
    assert "MERA-04" not in graph["program_edges"]["MBES"]["start_requires"]
    assert "MRCS-14" in graph["program_edges"]["MBES"]["start_requires"]
    assert graph["program_edges"]["MBES"]["golden_proof_requires"] == ["MERA-24", "reactive-world proof"]
    assert graph["milestone_gates"]["rotation"]["MBES-01"] == ["MERA-03", "MRCS-14"]
    assert "MBES-24" in graph["program_edges"]["MSLR"]["start_requires"]
    assert graph["milestone_gates"]["rotation"]["MSLR-01"][0] == "MBES-24"

    assert backlog["pdcp_reduction"]["stable_start_gate"] == "MBES-01"
    assert backlog["pdcp_reduction"]["stable_golden_gate"] == "MBES-24"


def test_mbes_cross_family_absorptions_and_overlap_folds_are_explicit():
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MBES_REDUCTION_RECEIPT.json")
    rows = {x["baseline_id"]: x for x in receipt["baseline_rows"]}

    assert rows["MBES-11"]["disposition"] == "ABSORB_EXISTING_OWNER"
    assert rows["MBES-17"]["disposition"] == "ABSORB_EXISTING_OWNER"
    assert rows["MBES-22"]["disposition"] == "ABSORB_EXISTING_OWNER"

    expected_clusters = {
        ("MBES-01", "MBES-02"),
        ("MBES-03", "MBES-04"),
        ("MBES-05", "MBES-06", "MBES-07"),
        ("MBES-08", "MBES-09", "MBES-10"),
        ("MBES-12", "MBES-13"),
        ("MBES-14", "MBES-15", "MBES-16"),
        ("MBES-18", "MBES-19"),
        ("MBES-20", "MBES-21", "MBES-23"),
    }
    assert {tuple(x) for x in receipt["intra_family_overlap_clusters"]} == expected_clusters

    cross_text = json.dumps(receipt["cross_family_absorptions"]).lower()
    for owner in ("mera", "gpr", "pca-12", "mcs", "mswi", "dpl", "odl", "mib-13", "icf"):
        assert owner in cross_text


def test_mbes_preserves_owner_boundaries_reactive_world_and_resolution():
    backlog = j("governance/application-planning/multiversal-built-environment-settlement/MBES_PROGRAM_BACKLOG.json")
    program = t("governance/application-planning/multiversal-built-environment-settlement/MBES_MULTIVERSAL_BUILT_ENVIRONMENT_SETTLEMENT_PROGRAM.md").lower()
    dcp = t("governance/application-planning/preimplementation-design-closure/PDCP_MBES_FAMILY_DESIGN_CLOSURE.md").lower()
    boundaries = "\n".join(backlog["boundaries"]).lower()

    for owner in ("mib-14", "mcs", "mrcs", "mera", "gpr", "pca-12", "apw/d26", "mib-12", "mib-13", "icf", "odl", "dpl", "world", "environment", "action/event", "mswi"):
        assert owner in boundaries
    for level in ("settlement/district", "site/parcel", "structure", "level/zone", "space/room", "component/fixture", "connection/network"):
        assert level in boundaries

    assert "oara" in program
    assert "planetary sentience" in program
    assert "equivalent development" in program
    assert "definition is not construction" in program
    assert "geometry is not construction truth" in dcp
    assert "no universal real-world structural formula" in dcp
    assert "48" in dcp and "pdcp-mbes-048" in dcp


def test_mbes_historical_count_snapshot_remains_provenance():
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MBES_REDUCTION_RECEIPT.json")
    assert receipt["baseline_tranche_count"] == 24
    assert receipt["reduced_tranche_count"] == 9
