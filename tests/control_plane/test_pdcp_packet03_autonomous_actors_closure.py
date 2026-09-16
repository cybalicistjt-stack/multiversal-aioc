import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_packet03_is_design_only_and_does_not_select_product_work():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_03_AUTONOMOUS_ACTORS_CLOSURE.json"
    )
    current = j("operations/CURRENT.json")
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")

    assert closure["project_id"] == "PDCP"
    assert closure["packet_id"] == "PDCP-PACKET-03"
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


def test_packet03_preserves_completed_organization_command_and_mas_boundaries():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_03_AUTONOMOUS_ACTORS_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_03_AUTONOMOUS_ACTORS_DESIGN_CLOSURE.md"
    ).lower()

    for owner_token in ("ODL", "SCL", "MAS-08", "Action/Event", "Project/time"):
        assert any(owner_token in owner for owner in closure["absorbed_existing_owners"])

    assert "packet 03 does not add a second strategic order resolver" in dcp
    assert "packet 03 creates no generic plan-state ledger" in dcp
    assert "it may not directly increment a prepared mas clock as hidden side state" in dcp
    assert "selection is not commitment" in dcp


def test_packet03_closes_non_omniscient_legal_filtered_autonomy_contracts():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_03_AUTONOMOUS_ACTORS_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_03_AUTONOMOUS_ACTORS_DESIGN_CLOSURE.md"
    ).lower()

    required_contracts = {
        "AutonomyPolicyDefinition",
        "AutonomyDecisionTriggerDefinition",
        "AutonomousDecisionContext",
        "LegalAutonomousOperationCandidate",
        "AutonomousSelectionPolicy",
        "AutonomyEvaluationReceipt",
        "AutonomousPlanTemplateDefinition",
        "AutonomousHandoffRequest",
        "AutonomousInterruptionReceipt",
        "OffscreenAutonomyBatchReceipt",
    }
    assert required_contracts.issubset(set(closure["new_contracts_closed"]))
    assert "actor-relative rather than omniscient decision context" in dcp
    assert "legal-action filtering precedes ranking" in dcp
    assert "no language model is required for blocking behavior" in dcp
    assert "a player-controlled character must never receive consequential autonomous action selection" in dcp
    assert "closing the app for three real-world days does not itself advance a campaign by three days" in dcp


def test_packet03_routes_residual_work_only_to_existing_future_families():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_03_AUTONOMOUS_ACTORS_CLOSURE.json"
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

    assert "MNCS-22" in closure["affected_future_families"]["MNCS"]
    assert "MRCS-12" in closure["affected_future_families"]["MRCS"]
    assert "GPR-07" in closure["affected_future_families"]["GPR"]
    assert "MSWI-17" in closure["affected_future_families"]["MSWI"]


def test_packet03_has_32_contiguous_golden_vectors_and_accessibility_security_proof():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_03_AUTONOMOUS_ACTORS_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_03_AUTONOMOUS_ACTORS_DESIGN_CLOSURE.md"
    )

    expected = [f"PDCP-AUT-{i:03d}" for i in range(1, 33)]
    assert closure["golden_vector_ids"] == expected
    for vector_id in expected:
        assert vector_id in dcp
    assert "semantic nonvisual equivalents" in dcp.lower()
    assert "permission/visibility filtering occurs before" in dcp.lower()


def test_packet03_register_is_closed_and_packet04_is_next_open_packet():
    register = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_BENCHMARK_CAPABILITY_REGISTER.md"
    ).lower()

    assert "3 — autonomous actors, threats & offscreen action | `design_closed`" in register
    assert "pdcp_packet_03_autonomous_actors_design_closure.md" in register
    assert "4 — semantic affordances & composable effects | `open`" in register
