#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/source-material/recovered-legacy/now-this-2026-08-21"
RSR01 = BASE / "RSR-01_DISPOSITION_REGISTRY.json"
REGISTRY = BASE / "RSR-06_LNG_RECONCILIATION_REGISTRY.json"
QUEUE = BASE / "RSR-06_LINGUISTIC_CANDIDATE_AND_CONFLICT_QUEUE.json"
ROUTING = BASE / "RSR-06_DOWNSTREAM_ROUTING.json"
REPORT = BASE / "RSR-06_COMPLETION_REPORT.md"

EXPECTED_PREVIOUS = {
    "rsr01:serpentine-empire-structure-analysis",
    "rsr01:traigan-astrological-interpretations",
}
EXPECTED_COUNTS = {
    "previous_route_count": 2,
    "material_signal_count": 14,
    "supplemental_material_signal_count": 12,
    "no_material_signal_count": 10,
}
REQUIRED_BOUNDARY_KINDS = {
    "stable-identity", "proper-name", "assistant-language-claim", "script-glyph",
    "supernatural-communication", "owner-telepathy", "translation-infrastructure",
    "mechanical-translation-wording", "phrase-motto", "temporal-visibility",
    "family-intelligibility", "generated-names", "social-model", "external-owner-links",
}


def load(path: Path):
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


rsr01 = load(RSR01)
reg = load(REGISTRY)
queue = load(QUEUE)
routing = load(ROUTING)
report = REPORT.read_text(encoding="utf-8")

assert reg["work_item"] == "RSR-06"
assert reg["archive_sha256"] == rsr01["archive_sha256"]
assert reg["source_count"] == 24
assert len(reg["records"]) == 24
assert reg["canonical_lng_mutation"] is False

r1 = {s["source_id"]: (s["filename"], s["mht_sha256"]) for s in rsr01["sources"]}
r6 = {r["source_id"]: (r["filename"], r["mht_sha256"]) for r in reg["records"]}
assert set(r6) == set(r1), "RSR-06 source-id coverage differs from RSR-01"
assert r6 == r1, "RSR-06 filename/checksum alignment differs from RSR-01"

previous = {r["source_id"] for r in reg["records"] if r["previously_routed_to_rsr06"]}
assert previous == EXPECTED_PREVIOUS, previous
for source in rsr01["sources"]:
    if source["source_id"] in EXPECTED_PREVIOUS:
        assert "RSR-06" in source["routes"]
    else:
        assert "RSR-06" not in source["routes"]

material = [r for r in reg["records"] if r["relevance"] != "none"]
no_material = [r for r in reg["records"] if r["relevance"] == "none"]
supplemental = [r for r in material if not r["previously_routed_to_rsr06"]]
actual_counts = {
    "previous_route_count": len(previous),
    "material_signal_count": len(material),
    "supplemental_material_signal_count": len(supplemental),
    "no_material_signal_count": len(no_material),
}
assert actual_counts == EXPECTED_COUNTS, actual_counts
assert reg["counts"] == EXPECTED_COUNTS

for rec in reg["records"]:
    assert rec["automatic_canon_promotion"] is False
    assert rec["canonical_lng_mutation"] is False
    assert "SGC" in rec["routes"]
    assert rec["assigned_existing_lng_stable_ids"] == []

assert queue["candidate_count"] == 12
assert len(queue["candidates"]) == 12
assert queue["authority_boundary_count"] == 14
assert len(queue["authority_boundaries"]) == 14
assert queue["canonical_lng_mutation"] is False
candidate_ids = [c["candidate_id"] for c in queue["candidates"]]
assert len(candidate_ids) == len(set(candidate_ids))
assert all(cid.startswith("rsr06:") for cid in candidate_ids)
for candidate in queue["candidates"]:
    assert candidate["canonical_status"] == "noncanonical-proposal"
    assert candidate["automatic_canon_promotion"] is False
assert {b["kind"] for b in queue["authority_boundaries"]} == REQUIRED_BOUNDARY_KINDS

assert routing["source_count"] == 24
assert routing["implementation_authority_granted"] is False
assert routing["rsr07_implementation_started"] is False
assert routing["mss06_implementation_started"] is False
assert {r["source_id"] for r in routing["routes"]} == set(r1)
for route in routing["routes"]:
    assert route["implementation_authority_granted"] is False
    assert "SGC" in route["routes"]

authority_text = json.dumps(reg["authority"], sort_keys=True)
assert "LNG-01..06 completed_verified" in authority_text
assert "23b01927677ae4541ccc1c9430f837b8efce8ded" in authority_text

required_report_phrases = [
    "24 / 24",
    "prior explicit RSR-06 routes: **2**",
    "material LNG-adjacent signals: **14**",
    "supplemental material signals recovered beyond prior routes: **12**",
    "explicit no-material-LNG decisions: **10**",
    "source-bound noncanonical linguistic candidates: **12**",
    "explicit authority/uncertainty boundaries: **14**",
    "Existing Dominix future-reference language/stage identities are not reused",
    "Missing vocabulary and grammar remain unknown",
    "Future/historical/GM-hidden language material remains filtered",
    "RSR-07 must remain unstarted",
]
for phrase in required_report_phrases:
    assert phrase in report, f"completion report missing: {phrase}"

print("RSR-06 reconciliation integrity: PASS")
