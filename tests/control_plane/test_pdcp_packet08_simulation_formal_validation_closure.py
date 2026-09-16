import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_packet08_is_design_only_and_does_not_select_product_work():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_08_SIMULATION_FORMAL_VALIDATION_CLOSURE.json"
    )
    current = j("operations/CURRENT.json")
    graph = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")

    assert closure["project_id"] == "PDCP"
    assert closure["packet_id"] == "PDCP-PACKET-08"
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


def test_packet08_absorbs_general_workbench_into_pca12_without_new_truth_owner():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_08_SIMULATION_FORMAL_VALIDATION_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_08_SIMULATION_FORMAL_VALIDATION_DESIGN_CLOSURE.md"
    ).lower()

    assert any("PCA-12" in owner for owner in closure["absorbed_existing_owners"])
    assert closure["existing_roadmap_owner_targets"]["PCA"] == ["PCA-12", "PCA-14", "PCA-16"]
    assert "analysis consumes governed owner projections and emits evidence" in dcp
    assert "analysis state never skips from layer 3–5 directly to layer 7" in dcp
    assert "no new family or standalone tranche is required" in dcp


def test_packet08_closes_shared_analysis_contracts_and_method_classes():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_08_SIMULATION_FORMAL_VALIDATION_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_08_SIMULATION_FORMAL_VALIDATION_DESIGN_CLOSURE.md"
    ).lower()

    required = [
        "AnalysisModelDescriptor",
        "AnalysisInputSnapshot",
        "AnalysisAssumption",
        "AnalysisObjective",
        "AnalysisConstraint",
        "AnalysisRunDefinition",
        "AnalysisRunReceipt",
        "AnalysisFinding",
        "CounterexampleWitness",
        "FeasibilityWitness",
        "UnsatCoreReceipt",
        "StatisticalAnalysisReceipt",
        "AnalysisComparisonReceipt",
    ]
    assert set(required).issubset(set(closure["new_contracts_closed"]))
    for name in required:
        assert name.lower() in dcp

    assert closure["analysis_method_classes"] == [
        "deterministic_validation",
        "bounded_exhaustive_search",
        "graph_analysis",
        "sat_smt_constraint_analysis",
        "optimization_routing_scheduling",
        "stochastic_monte_carlo",
        "agent_based_simulation",
        "parameter_sweep_sensitivity",
        "regression_baseline_comparison",
    ]
    assert closure["claim_strength_classes"] == [
        "exact_within_declared_model",
        "bounded_exact",
        "statistical_estimate",
        "heuristic_indicator",
        "inconclusive",
    ]


def test_packet08_preserves_proof_strength_and_optimization_boundaries():
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_08_SIMULATION_FORMAL_VALIDATION_DESIGN_CLOSURE.md"
    ).lower()

    for phrase in (
        "exact within the declared model",
        "statistical estimates never become deterministic golden proof",
        "`unknown`/timeout remains inconclusive",
        "no optimization runs without explicit objectives or satisfy-only mode",
        "a tool cannot silently weaken a hard constraint",
        "permission/visibility filtering occurs before",
        "there is no `apply_result_to_live_state` shortcut",
        "all blocking functionality works with ai disabled",
    ):
        assert phrase in dcp


def test_packet08_routes_residuals_to_existing_families_only():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_08_SIMULATION_FORMAL_VALIDATION_CLOSURE.json"
    )

    expected = {"MRCS", "GPR", "MERA", "MBES", "MSLR", "MSWI"}
    assert set(closure["affected_future_families"]) == expected
    assert closure["no_direct_obligation_families"] == ["MCS", "MCCS", "MNCS", "MSAS"]
    for family, tranche_ids in closure["affected_future_families"].items():
        assert tranche_ids
        assert all(x.startswith(f"{family}-") for x in tranche_ids)


def test_packet08_has_56_contiguous_golden_vectors_and_accessibility_proof():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_08_SIMULATION_FORMAL_VALIDATION_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_08_SIMULATION_FORMAL_VALIDATION_DESIGN_CLOSURE.md"
    )

    expected = [f"PDCP-SFV-{i:03d}" for i in range(1, 57)]
    assert closure["golden_vector_ids"] == expected
    for vector_id in expected:
        assert vector_id in dcp
    assert "screen-reader" in dcp.lower()
    assert "keyboard" in dcp.lower()
    assert "non-color" in dcp.lower()


def test_packet08_permission_filtering_happens_before_analysis_model_construction():
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_08_SIMULATION_FORMAL_VALIDATION_DESIGN_CLOSURE.md"
    ).lower()

    assert "filter before extraction" in dcp
    assert "model-variable creation" in dcp
    assert "graph node/edge creation" in dcp
    assert "solver input" in dcp
    assert "optional-ai context" in dcp
    assert "it cannot simply redact labels from a privileged graph" in dcp


def test_packet08_closes_benchmark_packet_series_and_register_has_no_open_packet():
    closure = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_08_SIMULATION_FORMAL_VALIDATION_CLOSURE.json"
    )
    register = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_BENCHMARK_CAPABILITY_REGISTER.md"
    ).lower()

    assert closure["benchmark_packet_series_complete"] is True
    assert "8 — simulation & formal validation laboratory | `design_closed`" in register
    assert "pdcp_packet_08_simulation_formal_validation_design_closure.md" in register
    assert "| `open` |" not in register.split("## packet status", 1)[1].split("## packet 1", 1)[0]
    assert "benchmark-derived packet series is now design-closed" in register
