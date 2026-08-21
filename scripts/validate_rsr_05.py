#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/source-material/recovered-legacy/now-this-2026-08-21"

def load(name):
    return json.loads((BASE / name).read_text(encoding="utf-8"))

registry = load("RSR-05_LSS_RECONCILIATION_REGISTRY.json")
queue = load("RSR-05_CANDIDATE_AND_BOUNDARY_QUEUE.json")
routing = load("RSR-05_DOWNSTREAM_ROUTING.json")

assert registry["work_item"] == "RSR-05"
assert registry["archive_sha256"] == "2a5eae712f483d1fb33ff9fb0087e96c4eb8b71b287cc707c196a4c17a2f78f4"
assert registry["source_count"] == 24
assert len(registry["records"]) == 24
assert len({r["source_id"] for r in registry["records"]}) == 24
assert len({r["filename"] for r in registry["records"]}) == 24
assert registry["counts"] == {
    "previous_route_count": 4,
    "material_signal_count": 9,
    "supplemental_material_signal_count": 5,
    "no_material_signal_count": 15,
}
assert registry["canonical_lss_or_inventory_mutation"] is False
assert sum(1 for r in registry["records"] if r["previously_routed_to_rsr05"]) == 4
assert sum(1 for r in registry["records"] if r["relevance"] != "none") == 9
for rec in registry["records"]:
    assert rec["automatic_canon_promotion"] is False
    assert rec["canonical_lss_or_inventory_mutation"] is False
    assert len(rec["mht_sha256"]) == 64

assert queue["work_item"] == "RSR-05"
assert queue["canonical"] is False
assert queue["canonical_lss_or_inventory_mutation"] is False
assert queue["candidate_count"] == 8 == len(queue["candidates"])
assert queue["boundary_count"] == 12 == len(queue["boundaries"])
assert all(c["canonical"] is False for c in queue["candidates"])
assert any(c["candidate_id"] == "rsr05:helldiving-faction-equipment-intent" for c in queue["candidates"])
assert any(b["issue_id"] == "rsr05:boundary:biological-harvest-stays-icf07" for b in queue["boundaries"])
assert any(b["issue_id"] == "rsr05:boundary:no-universal-drop-tables" for b in queue["boundaries"])

assert routing["work_item"] == "RSR-05"
owners = {r["owner"] for r in routing["routes"]}
assert {"RSR-07", "CCP", "DPL", "WCI", "SGC"} <= owners
assert "RSR-06" in routing["unauthorized_successors"]
assert "MSS-06" in routing["unauthorized_successors"]

report = (BASE / "RSR-05_COMPLETION_REPORT.md").read_text(encoding="utf-8")
for token in ["24 / 24", "D17", "ICF-07", "universal drop table", "RSR-07", "SGC"]:
    assert token in report

print("RSR-05 validation: PASS")
