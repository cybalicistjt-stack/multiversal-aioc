import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_packet07_is_design_only_and_does_not_select_product_work():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_07_CREATOR_GM_EXECUTION_CLOSURE.json"
    )
    current = j("operations/CURRENT.json")
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")

    assert closure["project_id"] == "PDCP"
    assert closure["packet_id"] == "PDCP-PACKET-07"
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


def test_packet07_preserves_existing_shared_authority_and_no_super_runtime():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_07_CREATOR_GM_EXECUTION_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_07_CREATOR_GM_EXECUTION_DESIGN_CLOSURE.md"
    ).lower()

    for owner_fragment in (
        "MV-IA-F006",
        "IA-D04-002",
        "IA-D04-004",
        "MV-IA-F020",
        "MV-IA-F021",
        "MV-IA-F025",
        "Action/Event",
    ):
        assert any(owner_fragment in owner for owner in closure["absorbed_existing_owners"])

    for phrase in (
        "same semantics, different authority",
        "preview is not commitment",
        "diagnostics are projections",
        "gm tools do not create wildcard mutation authority",
        "undo is not history deletion",
        "advanced authoring is bounded",
    ):
        assert phrase in dcp


def test_packet07_closes_execution_inspection_contracts():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_07_CREATOR_GM_EXECUTION_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_07_CREATOR_GM_EXECUTION_DESIGN_CLOSURE.md"
    ).lower()

    required = [
        "CreatorRuntimeBindingProfile",
        "ExecutionContextSnapshot",
        "PreviewDryRunRequest",
        "PreviewDryRunReceipt",
        "ExplanationRequest",
        "ExplanationReceipt",
        "RuleEvaluationTrace",
        "DiagnosticLensDefinition",
        "StepThroughDiagnosticSession",
        "GMInterventionCapabilityDefinition",
        "GMInterventionRequest",
        "GMInterventionReceipt",
        "ReversibilityClassification",
        "UndoCompensationPlan",
        "UndoCompensationRequest",
        "UndoCompensationReceipt",
        "LiveControlBindingDefinition",
        "CollaborationReviewBinding",
        "AuthoringDiagnosticReceipt",
        "CounterfactualPreviewReceipt",
    ]
    assert set(required).issubset(set(closure["new_contracts_closed"]))
    for name in required:
        assert name.lower() in dcp

    assert closure["diagnostic_depths"] == ["overview", "standard", "deep"]
    assert set(closure["reversibility_classes"]) == {
        "draft_revert",
        "owner_inverse_operation",
        "owner_compensation_operation",
        "snapshot_restore_permitted",
        "gm_adjudication_required",
        "irreversible",
    }


def test_packet07_routes_to_all_existing_pdcp_families_only():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_07_CREATOR_GM_EXECUTION_CLOSURE.json"
    )

    expected_families = {
        "MCS", "MCCS", "MNCS", "MSAS", "MRCS",
        "GPR", "MERA", "MBES", "MSLR", "MSWI",
    }
    assert set(closure["affected_future_families"]) == expected_families
    assert closure["no_direct_obligation_families"] == []
    for family, tranche_ids in closure["affected_future_families"].items():
        assert tranche_ids
        assert all(x.startswith(f"{family}-") for x in tranche_ids)


def test_packet07_has_48_contiguous_golden_vectors_and_accessibility_proof():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_07_CREATOR_GM_EXECUTION_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_07_CREATOR_GM_EXECUTION_DESIGN_CLOSURE.md"
    )

    expected = [f"PDCP-GMX-{i:03d}" for i in range(1, 49)]
    assert closure["golden_vector_ids"] == expected
    for vector_id in expected:
        assert vector_id in dcp
    assert "screen-reader" in dcp.lower()
    assert "keyboard" in dcp.lower()
    assert "non-color" in dcp.lower()


def test_packet07_safety_boundaries_are_explicit():
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_07_CREATOR_GM_EXECUTION_DESIGN_CLOSURE.md"
    ).lower()

    assert "there is no generic `force_set_any_field` intervention" in dcp
    assert "canonical events are not deleted by undo" in dcp
    assert "previewing" in dcp and "does not reserve, transfer or consume" in dcp
    assert "filtering occurs before" in dcp
    assert "all blocking functionality works with ai disabled" in dcp


def test_packet07_register_is_closed_and_packet08_is_next_open_packet():
    register = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_BENCHMARK_CAPABILITY_REGISTER.md"
    ).lower()

    assert "7 — creator/gm execution ux & debuggability | `design_closed`" in register
    assert "pdcp_packet_07_creator_gm_execution_design_closure.md" in register
    assert "8 — simulation & formal validation laboratory | `open`" in register
