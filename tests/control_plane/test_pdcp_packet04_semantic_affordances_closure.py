import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_packet04_is_design_only_and_does_not_select_product_work():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_04_SEMANTIC_AFFORDANCES_CLOSURE.json"
    )
    current = j("operations/CURRENT.json")
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")

    assert closure["project_id"] == "PDCP"
    assert closure["packet_id"] == "PDCP-PACKET-04"
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


def test_packet04_preserves_owner_boundaries_and_rejects_universal_physics():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_04_SEMANTIC_AFFORDANCES_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_04_SEMANTIC_AFFORDANCES_DESIGN_CLOSURE.md"
    ).lower()

    assert any("MIB-12" in owner for owner in closure["absorbed_existing_owners"])
    assert any("Action/Event" in owner for owner in closure["absorbed_existing_owners"])
    for phrase in (
        "no universal material table",
        "common-sense physics",
        "unknown or source-unspecified behavior remains unresolved",
        "evaluation never grants mutation authority",
        "does not define",
    ):
        assert phrase in dcp


def test_packet04_closes_affordance_response_and_effect_composition_contracts():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_04_SEMANTIC_AFFORDANCES_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_04_SEMANTIC_AFFORDANCES_DESIGN_CLOSURE.md"
    ).lower()

    for required in (
        "semanticaffordancedefinition",
        "interactioncapabilitybinding",
        "interactionresponseprofiledefinition",
        "effectinteractionrule",
        "interactionresolutionprofile",
        "interactionevaluationreceipt",
        "effectcompositionreceipt",
        "interactionpropagationreceipt",
        "operation parity rule",
        "abstract",
        "standard",
        "detailed",
    ):
        assert required in dcp

    expected_modes = {
        "coexist",
        "suppress",
        "cancel",
        "replace",
        "transform",
        "amplify",
        "attenuate",
        "trigger",
        "propagate",
        "merge_into_named_effect",
        "conflict_requires_resolution",
        "no_defined_interaction",
    }
    assert set(closure["effect_interaction_modes"]) == expected_modes
    assert closure["resolution_depths"] == ["abstract", "standard", "detailed"]


def test_packet04_routes_to_existing_future_families_only():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_04_SEMANTIC_AFFORDANCES_CLOSURE.json"
    )

    assert set(closure["affected_future_families"]) == {
        "MRCS", "GPR", "MERA", "MBES", "MSLR", "MSWI"
    }
    assert closure["no_direct_obligation_families"] == ["MCS", "MCCS", "MNCS", "MSAS"]

    expected = {
        "MRCS": {"MRCS-02", "MRCS-04", "MRCS-05", "MRCS-10", "MRCS-11", "MRCS-13", "MRCS-14", "MRCS-16", "MRCS-17", "MRCS-18", "MRCS-20", "MRCS-21"},
        "GPR": {"GPR-02", "GPR-03", "GPR-04", "GPR-06", "GPR-08", "GPR-09", "GPR-12", "GPR-13", "GPR-14", "GPR-15", "GPR-16"},
        "MERA": {"MERA-03", "MERA-04", "MERA-06", "MERA-07", "MERA-10", "MERA-11", "MERA-17", "MERA-18", "MERA-20", "MERA-22", "MERA-24"},
        "MBES": {"MBES-03", "MBES-08", "MBES-09", "MBES-12", "MBES-13", "MBES-15", "MBES-16", "MBES-18", "MBES-19", "MBES-24"},
        "MSLR": {"MSLR-02", "MSLR-06", "MSLR-08", "MSLR-10", "MSLR-12", "MSLR-16", "MSLR-18"},
        "MSWI": {"MSWI-03", "MSWI-07", "MSWI-08", "MSWI-10", "MSWI-15", "MSWI-17", "MSWI-18"},
    }
    for family, ids in expected.items():
        assert set(closure["affected_future_families"][family]) == ids


def test_packet04_has_40_contiguous_golden_vectors_and_accessibility_proof():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_04_SEMANTIC_AFFORDANCES_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_04_SEMANTIC_AFFORDANCES_DESIGN_CLOSURE.md"
    )

    expected = [f"PDCP-AFF-{i:03d}" for i in range(1, 41)]
    assert closure["golden_vector_ids"] == expected
    for vector_id in expected:
        assert vector_id in dcp
    assert "keyboard/text/structured explanation" in dcp.lower()


def test_packet04_register_is_closed_and_packet05_is_next_open_packet():
    register = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_BENCHMARK_CAPABILITY_REGISTER.md"
    ).lower()

    assert "4 — semantic affordances & composable effects | `design_closed`" in register
    assert "pdcp_packet_04_semantic_affordances_design_closure.md" in register
    assert "5 — persistent history, legacy, succession & delayed consequence | `open`" in register
