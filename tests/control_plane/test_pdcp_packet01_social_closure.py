import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_packet01_is_design_closed_without_product_authority():
    record = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_01_SOCIAL_INTERACTION_CLOSURE.json"
    )
    current = j("operations/CURRENT.json")

    assert record["project_id"] == "PDCP"
    assert record["packet_id"] == "PDCP-PACKET-01"
    assert record["status"] == "design_closed"
    assert record["implementation_authority"] is False
    assert record["roadmap_count_mutation"] is False
    assert record["ops3_current_changed"] is False
    assert record["new_family_required"] is False
    assert record["capability_loss_detected"] is False
    assert current["lanes"]["product-development"]["selected_work_item"] != "PDCP-PACKET-01"


def test_packet01_preserves_existing_social_owners_and_excludes_mas():
    record = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_01_SOCIAL_INTERACTION_CLOSURE.json"
    )
    dcp = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_01_SOCIAL_INTERACTION_DESIGN_CLOSURE.md"
    ).lower()

    assert "MAS" in record["excluded_programs"]
    for owner in ("ppia-10", "mv-ia-f010", "mib-09", "odl"):
        assert owner in dcp
    for forbidden in (
        "universal numeric willingness formula",
        "universal culture hierarchy",
        "persuasion is not mind control",
        "compliance is not consent",
    ):
        assert forbidden in dcp


def test_packet01_closes_typed_influence_and_norm_contracts():
    record = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_01_SOCIAL_INTERACTION_CLOSURE.json"
    )

    assert record["influence_modes"] == [
        "command",
        "delegated_instruction",
        "request",
        "bargain",
        "incentive",
        "persuasion",
        "social_pressure",
        "threat_coercion",
        "deception",
        "autonomous_choice",
    ]
    assert "SocialDecisionPolicyDefinition" in record["new_contracts_closed"]
    assert "SocialNormProfileDefinition" in record["new_contracts_closed"]
    assert "WitnessInterpretationCandidate" in record["new_contracts_closed"]
    assert len(record["golden_vector_ids"]) == 18
    assert record["golden_vector_ids"][0] == "PDCP-SOC-001"
    assert record["golden_vector_ids"][-1] == "PDCP-SOC-018"


def test_packet01_maps_residual_work_only_to_existing_future_families():
    record = j(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_PACKET_01_SOCIAL_INTERACTION_CLOSURE.json"
    )

    assert set(record["affected_future_families"]) == {"MNCS", "MRCS", "GPR", "MSWI"}
    assert set(record["no_direct_obligation_families"]) == {
        "MCS",
        "MCCS",
        "MSAS",
        "MERA",
        "MBES",
        "MSLR",
    }
    assert "MNCS-06" in record["affected_future_families"]["MNCS"]
    assert "MRCS-08" in record["affected_future_families"]["MRCS"]
    assert "GPR-06" in record["affected_future_families"]["GPR"]
    assert "MSWI-09" in record["affected_future_families"]["MSWI"]


def test_register_points_to_packet01_closure():
    register = t(
        "governance/application-planning/preimplementation-design-closure/"
        "PDCP_BENCHMARK_CAPABILITY_REGISTER.md"
    ).lower()

    assert "packet 1 — social interaction grammar" in register
    assert "`design_closed` — 2026-09-16" in register
    assert "pdcp_packet_01_social_interaction_design_closure.md" in register
    assert "no new family and no standalone implementation tranche" in register
