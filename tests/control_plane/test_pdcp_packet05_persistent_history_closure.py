import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_packet05_is_design_only_and_does_not_select_product_work():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_05_PERSISTENT_HISTORY_CLOSURE.json"
    )
    current = j("operations/CURRENT.json")
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")

    assert closure["project_id"] == "PDCP"
    assert closure["packet_id"] == "PDCP-PACKET-05"
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


def test_packet05_preserves_history_and_owner_boundaries():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_05_PERSISTENT_HISTORY_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_05_PERSISTENT_HISTORY_DESIGN_CLOSURE.md"
    ).lower()

    for owner_fragment in ("Action/Event", "PPIA-08", "WCI-02", "APW/D26", "ODL-04", "MIB-09"):
        assert any(owner_fragment in owner for owner in closure["absorbed_existing_owners"])

    for phrase in (
        "past events are immutable evidence",
        "succession is transfer, not cloning",
        "institutional memory is not omniscience",
        "forgetting does not erase truth",
        "no hidden real-time simulation",
        "history burn-in is proposed until promoted",
    ):
        assert phrase in dcp


def test_packet05_closes_legacy_succession_delayed_and_burnin_contracts():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_05_PERSISTENT_HISTORY_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_05_PERSISTENT_HISTORY_DESIGN_CLOSURE.md"
    ).lower()

    for required in (
        "legacyprofiledefinition",
        "eventlegacybinding",
        "legacyprojectionreceipt",
        "successionplandefinition",
        "successionhandoffrequest",
        "successionhandoffreceipt",
        "deferredconsequencedefinition",
        "deferredconsequenceinstance",
        "deferredconsequenceevaluationreceipt",
        "institutionalmemoryprojection",
        "memorytransformationrule",
        "historicalstateprojectionrequest",
        "historicalstateprojectionreceipt",
        "historyburninplandefinition",
        "historyburninproposalset",
        "historyburninpromotionreceipt",
    ):
        assert required in dcp

    assert closure["history_resolution_depths"] == ["summary", "standard", "detailed"]
    assert set(closure["historical_projection_modes"]) == {
        "current", "as_of_event", "as_of_campaign_time", "snapshot", "alternate_hypothetical"
    }
    assert "wall clock is not campaign time" in dcp
    assert "dependency-closed" in dcp


def test_packet05_routes_only_to_existing_future_families():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_05_PERSISTENT_HISTORY_CLOSURE.json"
    )

    assert set(closure["affected_future_families"]) == {"MNCS", "MRCS", "GPR", "MSWI"}
    assert closure["no_direct_obligation_families"] == ["MCS", "MCCS", "MSAS", "MERA", "MBES", "MSLR"]

    expected = {
        "MNCS": {"MNCS-04", "MNCS-07", "MNCS-09", "MNCS-15", "MNCS-16", "MNCS-20", "MNCS-21", "MNCS-23", "MNCS-24"},
        "MRCS": {"MRCS-02", "MRCS-05", "MRCS-08", "MRCS-16", "MRCS-17", "MRCS-20", "MRCS-21"},
        "GPR": {"GPR-05", "GPR-08", "GPR-09", "GPR-12", "GPR-13", "GPR-14", "GPR-16"},
        "MSWI": {"MSWI-02", "MSWI-03", "MSWI-09", "MSWI-10", "MSWI-13", "MSWI-15", "MSWI-16", "MSWI-17", "MSWI-18"},
    }
    for family, ids in expected.items():
        assert set(closure["affected_future_families"][family]) == ids


def test_packet05_has_40_contiguous_golden_vectors_and_accessibility_proof():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_05_PERSISTENT_HISTORY_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_05_PERSISTENT_HISTORY_DESIGN_CLOSURE.md"
    )

    expected = [f"PDCP-HIS-{i:03d}" for i in range(1, 41)]
    assert closure["golden_vector_ids"] == expected
    for vector_id in expected:
        assert vector_id in dcp
    assert "screen-reader" in dcp.lower()
    assert "keyboard" in dcp.lower()


def test_packet05_register_is_closed_and_packet06_is_next_open_packet():
    register = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_BENCHMARK_CAPABILITY_REGISTER.md"
    ).lower()

    assert "5 — persistent history, legacy, succession & delayed consequence | `design_closed`" in register
    assert "pdcp_packet_05_persistent_history_design_closure.md" in register
    assert "6 — multi-resolution simulation & autonomous world evolution | `open`" in register
