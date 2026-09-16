import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


BACKLOG = "governance/application-planning/multiversal-sound-audio-studio/MSAS_PROGRAM_BACKLOG.json"
RECEIPT = "governance/application-planning/preimplementation-design-closure/PDCP_MSAS_REDUCTION_RECEIPT.json"
DCP = "governance/application-planning/preimplementation-design-closure/PDCP_MSAS_FAMILY_DESIGN_CLOSURE.md"
LEDGER = "governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json"
DAG = "governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json"


EXPECTED_ORDER = [
    "MSAS-01", "MSAS-03", "MSAS-04", "MSAS-05", "MSAS-07", "MSAS-09",
    "MSAS-12", "MSAS-14", "MSAS-15", "MSAS-18", "MSAS-21",
]


def test_msas_pdcp_reduction_is_complete_and_non_authoritative():
    backlog = j(BACKLOG)
    receipt = j(RECEIPT)

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == EXPECTED_ORDER
    assert len(backlog["tranches"]) == 11
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])
    assert backlog["pdcp_reduction"]["baseline_tranche_count"] == 21
    assert backlog["pdcp_reduction"]["reduced_tranche_count"] == 11
    assert backlog["pdcp_reduction"]["capability_loss_detected"] is False

    assert receipt["status"] == "resolved"
    assert receipt["baseline_tranche_count"] == 21
    assert receipt["reduced_tranche_count"] == 11
    assert receipt["removed_standalone_tranches"] == 10
    assert receipt["implementation_authority"] is False
    assert receipt["ops3_current_mutation"] is False
    assert receipt["dag_mutation_required"] is False
    assert receipt["surviving_tranche_ids"] == EXPECTED_ORDER
    assert receipt["capability_loss_detected"] is False
    assert len(receipt["dispositions"]) == 21
    assert {x["baseline_id"] for x in receipt["dispositions"]} == {f"MSAS-{i:02d}" for i in range(1, 22)}


def test_msas_fold_map_and_cross_owner_absorptions_are_explicit():
    backlog = j(BACKLOG)
    receipt = j(RECEIPT)
    by_id = {x["id"]: x for x in backlog["tranches"]}

    assert by_id["MSAS-01"]["absorbs_baseline"] == ["MSAS-01", "MSAS-02"]
    assert by_id["MSAS-04"]["absorbs_baseline"] == ["MSAS-04", "MSAS-16"]
    assert by_id["MSAS-05"]["absorbs_baseline"] == ["MSAS-05", "MSAS-06"]
    assert by_id["MSAS-07"]["absorbs_baseline"] == ["MSAS-07", "MSAS-08"]
    assert by_id["MSAS-09"]["absorbs_baseline"] == ["MSAS-09", "MSAS-10", "MSAS-11"]
    assert by_id["MSAS-12"]["absorbs_baseline"] == ["MSAS-12", "MSAS-13"]
    assert by_id["MSAS-18"]["absorbs_baseline"] == ["MSAS-18", "MSAS-19", "MSAS-20"]

    disposition = {x["baseline_id"]: x for x in receipt["dispositions"]}
    assert disposition["MSAS-17"]["disposition"] == "ABSORB_EXISTING_OWNER"
    assert "PCA-09" in disposition["MSAS-17"]["residual_target"]
    owners = "\n".join(x["owner"] for x in receipt["cross_family_absorptions"])
    for owner in ("AAI", "PCA-07", "PCA-08", "PCA-09", "PCA-13", "ARI/PCA", "DWC speech"):
        assert owner in owners


def test_msas_preserves_audio_truth_rights_accessibility_and_local_first_boundaries():
    backlog = j(BACKLOG)
    boundaries = "\n".join(backlog["boundaries"]).lower()
    dcp = t(DCP).lower()

    for term in (
        "aai", "dwc", "ari", "pca-07", "pca-08", "pca-09", "pca-13",
        "action/event", "never prove", "consent", "caption", "non-audio", "paid/cloud",
    ):
        assert term in boundaries

    for term in (
        "prepared cue", "generated audio remains candidate", "voice identity", "local-first",
        "unsupported import", "48 vectors",
    ):
        assert term in dcp


def test_msas_dag_milestones_and_family_ledger_remain_consistent():
    dag = j(DAG)
    ledger = j(LEDGER)

    assert dag["nodes"]["MSAS"]["implementation_authority"] is False
    msas_edges = dag["program_edges"]["MSAS"]
    for req in ("AAI completed_verified", "PCA-07", "PCA-08", "PCA-15", "ARI"):
        assert req in msas_edges["start_requires"]

    family = next(x for x in ledger["families"] if x["program_id"] == "MSAS")
    assert family["reduction_status"] == "resolved"
    assert family["reduced_tranche_count"] == 11
    assert family["surviving_tranche_ids"] == EXPECTED_ORDER
    assert family["capability_loss_detected"] is False


def test_msas_golden_vectors_and_program_contract_are_present():
    dcp = t(DCP)
    program = t("governance/application-planning/multiversal-sound-audio-studio/MSAS_MULTIVERSAL_SOUND_AUDIO_STUDIO_PROGRAM.md").lower()

    assert dcp.count("\n1. create/open/save") == 1
    for i in range(1, 49):
        assert f"\n{i}. " in dcp
    assert "pdcp-reduced" in program
    assert "21 tranches" in program
    assert "11 tranches" in program
    assert "no dag milestone rewrite is required" not in program
    assert "no msas implementation authority" not in program
