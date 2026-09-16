import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_packet02_is_design_only_and_does_not_select_product_work():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_02_SYSTEMIC_EVIDENCE_CLOSURE.json"
    )
    current = j("operations/CURRENT.json")
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")

    assert closure["project_id"] == "PDCP"
    assert closure["packet_id"] == "PDCP-PACKET-02"
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


def test_packet02_preserves_existing_investigation_and_event_owners():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_02_SYSTEMIC_EVIDENCE_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_02_SYSTEMIC_EVIDENCE_DESIGN_CLOSURE.md"
    ).lower()
    ppia09 = t(
        "governance/application-planning/parallel-preimplementation/"
        "PPIA-09_COMPLETION_REPORT.md"
    ).lower()

    assert "status: **completed_verified**" in ppia09
    assert any("PPIA-09" in owner for owner in closure["absorbed_existing_owners"])
    assert any("Action/Event" in owner for owner in closure["absorbed_existing_owners"])
    assert "ppia-09 remains authoritative" in dcp
    assert "action/event" in dcp
    assert "source-domain owner" in dcp
    assert "does not create a second investigation system" in dcp
    assert "does not copy these records into an investigation ledger" in dcp


def test_packet02_closes_trace_emission_lifecycle_and_forgery_semantics():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_02_SYSTEMIC_EVIDENCE_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_02_SYSTEMIC_EVIDENCE_DESIGN_CLOSURE.md"
    ).lower()

    assert closure["trace_commit_modes"] == ["atomic_with_origin", "causal_followup"]
    for required in (
        "evidencetraceprofiledefinition",
        "traceemissionrule",
        "tracelifecycleprofiledefinition",
        "evidencetraceemissionreceipt",
        "witnessperceptionreceipt",
        "aggregatetracebundlereceipt",
        "evidencerouteavailabilitydiagnostic",
        "forgery",
        "contamination",
        "no universal decay clock",
        "no retroactive trace invention",
    ):
        assert required in dcp

    assert "there is no unrecorded “best effort” mode" in dcp
    assert "a forgery can successfully mislead characters without rewriting protected actual provenance" in dcp


def test_packet02_routes_only_to_existing_future_families():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_02_SYSTEMIC_EVIDENCE_CLOSURE.json"
    )

    assert set(closure["affected_future_families"]) == {"MNCS", "MRCS", "GPR", "MSWI"}
    assert closure["no_direct_obligation_families"] == [
        "MCS",
        "MCCS",
        "MSAS",
        "MERA",
        "MBES",
        "MSLR",
    ]

    expected = {
        "MNCS": {"MNCS-07", "MNCS-09", "MNCS-18", "MNCS-20", "MNCS-22", "MNCS-24"},
        "MRCS": {"MRCS-05", "MRCS-14", "MRCS-17", "MRCS-18", "MRCS-20", "MRCS-21"},
        "GPR": {"GPR-04", "GPR-05", "GPR-08", "GPR-12", "GPR-13", "GPR-14", "GPR-16"},
        "MSWI": {"MSWI-03", "MSWI-10", "MSWI-17", "MSWI-18"},
    }
    for family, tranche_ids in expected.items():
        assert set(closure["affected_future_families"][family]) == tranche_ids


def test_packet02_has_28_contiguous_golden_vectors_and_accessibility_proof():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_02_SYSTEMIC_EVIDENCE_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_02_SYSTEMIC_EVIDENCE_DESIGN_CLOSURE.md"
    )

    expected = [f"PDCP-EVD-{i:03d}" for i in range(1, 29)]
    assert closure["golden_vector_ids"] == expected
    for vector_id in expected:
        assert vector_id in dcp
    assert "accessible nonvisual parity" in dcp.lower()


def test_packet02_register_is_closed_and_packet03_remains_next_open_packet():
    register = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_BENCHMARK_CAPABILITY_REGISTER.md"
    ).lower()

    assert "2 — systemic investigation & evidence | `design_closed`" in register
    assert "pdcp_packet_02_systemic_evidence_design_closure.md" in register
    assert "3 — autonomous actors, threats & offscreen action | `open`" in register
