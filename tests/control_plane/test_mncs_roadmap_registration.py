import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


EXPECTED = [
    "MNCS-01",
    "MNCS-04",
    "MNCS-05",
    "MNCS-06",
    "MNCS-08",
    "MNCS-10",
    "MNCS-12",
    "MNCS-14",
    "MNCS-15",
    "MNCS-18",
    "MNCS-20",
    "MNCS-22",
    "MNCS-24",
]


def test_mncs_pdcp_reduced_contract_is_complete_and_non_authoritative():
    backlog = j("governance/application-planning/multiversal-npc-creature-studio/MNCS_PROGRAM_BACKLOG.json")
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MNCS_REDUCTION_RECEIPT.json")
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == EXPECTED
    assert [x["id"] for x in backlog["tranches"]] == EXPECTED
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])

    assert backlog["pdcp_reduction"]["baseline_tranche_count"] == 24
    assert backlog["pdcp_reduction"]["reduced_tranche_count"] == 13
    assert backlog["pdcp_reduction"]["capability_loss_detected"] is False

    assert receipt["status"] == "resolved"
    assert receipt["baseline_tranche_count"] == 24
    assert receipt["reduced_tranche_count"] == 13
    assert receipt["removed_standalone_tranches"] == 11
    assert receipt["surviving_tranche_ids"] == EXPECTED
    assert len(receipt["dispositions"]) == 24
    assert {x["baseline_id"] for x in receipt["dispositions"]} == {f"MNCS-{i:02d}" for i in range(1, 25)}
    assert receipt["golden_vector_count"] == 48
    assert receipt["capability_loss_detected"] is False
    assert receipt["implementation_authority"] is False
    assert receipt["ops3_current_mutation"] is False

    family = next(x for x in ledger["families"] if x["program_id"] == "MNCS")
    assert family["reduction_status"] == "resolved"
    assert family["reduced_tranche_count"] == 13
    assert family["surviving_tranche_ids"] == EXPECTED


def test_mncs_stable_dag_milestones_and_progressive_resolution_contract():
    dag = j("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")
    program = t("governance/application-planning/multiversal-npc-creature-studio/MNCS_MULTIVERSAL_NPC_CREATURE_STUDIO_PROGRAM.md").lower()
    backlog = j("governance/application-planning/multiversal-npc-creature-studio/MNCS_PROGRAM_BACKLOG.json")

    assert dag["milestone_gates"]["rotation"]["MNCS-01"] == ["MCCS-01"]
    assert "MCCS-01" in dag["program_edges"]["MNCS"]["start_requires"]
    assert "MCCS-02" not in dag["program_edges"]["MNCS"]["start_requires"]
    assert "MNCS-24" in dag["program_edges"]["MSWI"]["start_requires"]

    names = "\n".join(x["name"] for x in backlog["tranches"]).lower()
    for term in (
        "instant improv",
        "knowledge",
        "reputation",
        "ecology",
        "behavior",
        "population",
        "conversation",
        "resolution management",
        "runtime handoff",
    ):
        assert term in names

    assert "one identity, progressive resolution" in program
    assert "passing extra" in program
    assert "population → group/herd/pack/swarm" in program
    assert "selective regeneration" in program
    assert "does not modify `operations/current.json`" in program


def test_mncs_cross_family_absorptions_are_explicit():
    receipt = j("governance/application-planning/preimplementation-design-closure/PDCP_MNCS_REDUCTION_RECEIPT.json")
    dispositions = {x["baseline_id"]: x for x in receipt["dispositions"]}
    absorption_text = "\n".join(
        f"{x['concern']} {x['owner']} {x['mncs_residual']}" for x in receipt["cross_family_absorptions"]
    ).lower()

    assert dispositions["MNCS-09"]["disposition"] == "ABSORB_EXISTING_OWNER"
    assert "dpl" in dispositions["MNCS-09"]["residual_target"].lower()
    assert dispositions["MNCS-23"]["disposition"] == "ABSORB_EXISTING_OWNER"
    assert "ari/pca" in dispositions["MNCS-23"]["residual_target"].lower()

    for term in (
        "pca-02/pca-03",
        "ppia-02",
        "mccs",
        "mib-09",
        "dpl",
        "packet 06",
        "packet 07",
        "ari/pca",
        "reduced gpr",
    ):
        assert term in absorption_text


def test_mncs_party_association_reputation_is_scoped_and_attributable():
    program = t("governance/application-planning/multiversal-npc-creature-studio/MNCS_MULTIVERSAL_NPC_CREATURE_STUDIO_PROGRAM.md").lower()
    amendment = t("governance/application-planning/multiversal-implementation-backbone/MIB09_MNCS_PARTY_REPUTATION_INTEGRATION_AMENDMENT_2026-09-11.md").lower()
    backlog = j("governance/application-planning/multiversal-npc-creature-studio/MNCS_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()

    for text in (program, amendment, boundaries):
        assert "campaign" in text
        assert "party" in text
        assert "association" in text
        assert "reputation" in text

    assert "universal shared-party score" in program
    assert "direct reputation" in program
    assert "event/actor/party/campaign attribution" in program
    assert "no account-global or cross-campaign spillover" in amendment
    assert "cannot leak across campaigns" in program


def test_mncs_preserves_owner_clean_room_and_no_digital_human_scope():
    program = t("governance/application-planning/multiversal-npc-creature-studio/MNCS_MULTIVERSAL_NPC_CREATURE_STUDIO_PROGRAM.md").lower()
    benchmark = t("governance/application-planning/multiversal-npc-creature-studio/MNCS_BENCHMARK_CAPABILITY_MATRIX.md").lower()
    backlog = j("governance/application-planning/multiversal-npc-creature-studio/MNCS_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()

    for owner in ("ppia-02", "mib-09", "dpl", "world/environment", "mccs", "mas", "ari/pca"):
        assert owner in program

    assert "fictional npc" in program
    assert "real-person reproduction" in program
    assert "does not implement real-person reproduction" in boundaries
    assert "clean-room" in benchmark
    assert "npc suite" in benchmark
    assert "exact product identity was not unambiguously resolved" in benchmark
    assert "paid/cloud ai provider" in boundaries
