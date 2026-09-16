import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_packet06_is_design_only_and_does_not_select_product_work():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_06_MULTIRES_SIMULATION_CLOSURE.json"
    )
    current = j("operations/CURRENT.json")
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")

    assert closure["project_id"] == "PDCP"
    assert closure["packet_id"] == "PDCP-PACKET-06"
    assert closure["status"] == "design_closed"
    assert closure["implementation_authority"] is False
    assert closure["roadmap_count_mutation"] is False
    assert closure["ops3_current_changed"] is False
    assert closure["new_family_required"] is False
    assert closure["new_standalone_tranche_required"] is False
    assert closure["capability_loss_detected"] is False
    assert closure["excluded_programs"] == ["MAS"]
    assert current["lanes"]["product-development"]["selected_work_item"] != "PDCP"
    assert "PDCP" not in graph["nodes"]


def test_packet06_preserves_owner_boundaries_and_resolution_invariants():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_06_MULTIRES_SIMULATION_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_06_MULTIRES_SIMULATION_DESIGN_CLOSURE.md"
    ).lower()

    for owner_fragment in ("MNCS", "PDCP Packet 03", "PDCP Packet 05", "MBES", "GPR", "MSWI"):
        assert any(owner_fragment in owner for owner in closure["absorbed_existing_owners"])

    for phrase in (
        "aggregate state is not a hidden crowd of invented people",
        "refinement cannot retroactively invent history",
        "persistent identity is owner-minted",
        "collapse reduces active detail, not identity",
        "no double counting across resolutions",
        "uncertainty cannot become false precision",
        "canonical time, not wall clock, drives world evolution",
        "performance pressure never grants authority",
    ):
        assert phrase in dcp


def test_packet06_closes_resolution_refinement_collapse_and_budget_contracts():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_06_MULTIRES_SIMULATION_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_06_MULTIRES_SIMULATION_DESIGN_CLOSURE.md"
    ).lower()

    for required in (
        "simulationfidelityprofiledefinition",
        "resolutionscopebinding",
        "aggregatepartitiondefinition",
        "aggregatestateprojection",
        "aggregatetransitiondefinition",
        "aggregateadvancereceipt",
        "refinementrequest",
        "refinementreceipt",
        "individualizationpromotionrequest",
        "individualizationpromotionreceipt",
        "collapserequest",
        "collapsereceipt",
        "representationcoveragereceipt",
        "crossresolutioninteractionrequest",
        "crossresolutioninteractionreceipt",
        "offscreencatchupplan",
        "offscreencatchupreceipt",
        "simulationbudgetprofile",
        "simulationbudgetdecisionreceipt",
        "worldevolutionstepreceipt",
    ):
        assert required in dcp

    assert closure["resolution_modes"] == [
        "projection_only", "aggregate", "cohort", "individual", "adaptive_mixed"
    ]
    assert set(closure["fidelity_dimensions"]) == {
        "identity", "state", "temporal", "spatial", "causal", "recording"
    }
    assert closure["quantity_certainty_classes"] == [
        "exact", "range", "band", "distribution", "unknown"
    ]


def test_packet06_routes_only_to_existing_future_families():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_06_MULTIRES_SIMULATION_CLOSURE.json"
    )

    assert set(closure["affected_future_families"]) == {"MNCS", "MRCS", "GPR", "MBES", "MSWI"}
    assert closure["no_direct_obligation_families"] == ["MCS", "MCCS", "MSAS", "MERA", "MSLR"]

    expected = {
        "MNCS": {"MNCS-01", "MNCS-02", "MNCS-03", "MNCS-09", "MNCS-12", "MNCS-13", "MNCS-15", "MNCS-16", "MNCS-17", "MNCS-20", "MNCS-21", "MNCS-22", "MNCS-23", "MNCS-24"},
        "MRCS": {"MRCS-02", "MRCS-04", "MRCS-12", "MRCS-14", "MRCS-16", "MRCS-18", "MRCS-20", "MRCS-21"},
        "GPR": {"GPR-03", "GPR-05", "GPR-07", "GPR-08", "GPR-09", "GPR-12", "GPR-13", "GPR-14", "GPR-15", "GPR-16"},
        "MBES": {"MBES-01", "MBES-10", "MBES-11", "MBES-14", "MBES-17", "MBES-20", "MBES-21", "MBES-22", "MBES-23", "MBES-24"},
        "MSWI": {"MSWI-02", "MSWI-03", "MSWI-04", "MSWI-05", "MSWI-10", "MSWI-13", "MSWI-14", "MSWI-17", "MSWI-18"},
    }
    for family, ids in expected.items():
        assert set(closure["affected_future_families"][family]) == ids


def test_packet06_has_40_contiguous_golden_vectors_and_accessibility_proof():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_06_MULTIRES_SIMULATION_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_06_MULTIRES_SIMULATION_DESIGN_CLOSURE.md"
    )

    expected = [f"PDCP-SIM-{i:03d}" for i in range(1, 41)]
    assert closure["golden_vector_ids"] == expected
    for vector_id in expected:
        assert vector_id in dcp
    assert "screen-reader" in dcp.lower()
    assert "keyboard" in dcp.lower()


def test_packet06_register_is_closed_and_packet07_is_next_open_packet():
    register = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_BENCHMARK_CAPABILITY_REGISTER.md"
    ).lower()

    assert "6 — multi-resolution simulation & autonomous world evolution | `design_closed`" in register
    assert "pdcp_packet_06_multires_simulation_design_closure.md" in register
    assert "7 — creator/gm execution ux & debuggability | `open`" in register
