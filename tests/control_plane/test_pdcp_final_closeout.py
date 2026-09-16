import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PREFIXES = ("MCS", "MCCS", "MNCS", "MSAS", "MRCS", "GPR", "MERA", "MBES", "MSLR", "MSWI")
TRANCHE_RE = re.compile(r"\b(?:" + "|".join(PREFIXES) + r")-\d+\b")


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_all_ten_pdcp_family_receipts_match_effective_backlogs_and_totals():
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")
    assert len(ledger["families"]) == 10
    assert all(x["reduction_status"] == "resolved" for x in ledger["families"])
    assert all(x["overlap_audit_complete"] is True for x in ledger["families"])
    assert all(x["capability_loss_detected"] is False for x in ledger["families"])

    effective_total = 0
    baseline_total = 0
    for family in ledger["families"]:
        backlog = j(family["backlog_path"])
        receipt = j(family["reduction_receipt"])
        assert backlog["strict_order"] == family["surviving_tranche_ids"]
        assert [x["id"] for x in backlog["tranches"]] == family["surviving_tranche_ids"]
        assert receipt["surviving_tranche_ids"] == family["surviving_tranche_ids"]
        assert receipt["reduced_tranche_count"] == len(family["surviving_tranche_ids"])
        assert receipt["capability_loss_detected"] is False
        assert receipt["overlap_audit_complete"] is True
        effective_total += receipt["reduced_tranche_count"]
        baseline_total += receipt["baseline_tranche_count"]

    snap = ledger["baseline_snapshot"]
    assert baseline_total == snap["baseline_total_tranches"] == 208
    assert effective_total == snap["effective_reduced_total"] == 105
    assert baseline_total - effective_total == snap["removed_standalone_future_tranches"] == 103
    assert snap["approved_family_reductions"] == 10


def test_live_dag_and_parallel_map_reference_only_surviving_reduced_tranche_ids():
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")
    allowed = {
        tranche_id
        for family in ledger["families"]
        for tranche_id in family["surviving_tranche_ids"]
    }

    dag_text = t("governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json")
    parallel_text = t("governance/application-planning/PARALLEL_PRODUCT_EXECUTION_MAP.md")
    live_refs = set(TRANCHE_RE.findall(dag_text + "\n" + parallel_text))
    retired_live_refs = sorted(x for x in live_refs if x not in allowed)

    assert retired_live_refs == [], f"live control surfaces still reference retired PDCP tranches: {retired_live_refs}"


def test_pdcp_never_claims_product_implementation_authority():
    current = j("operations/CURRENT.json")
    ledger = j("governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json")
    assert ledger["implementation_authority"] is False
    assert ledger["ops3_current_mutation"] is False
    assert current["lanes"]["product-development"]["selected_work_item"] == "PCA-03"
    assert current["lanes"]["product-development"]["implementation_authority"] is False
