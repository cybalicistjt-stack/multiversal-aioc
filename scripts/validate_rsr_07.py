#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/source-material/recovered-legacy/now-this-2026-08-21"
RSR01 = BASE / "RSR-01_DISPOSITION_REGISTRY.json"
RSR06_ROUTING = BASE / "RSR-06_DOWNSTREAM_ROUTING.json"
REGISTRY = BASE / "RSR-07_MSS_RECONCILIATION_REGISTRY.json"
QUEUE = BASE / "RSR-07_SUPERNATURAL_CANDIDATE_AND_CONFLICT_QUEUE.json"
ROUTING = BASE / "RSR-07_DOWNSTREAM_ROUTING.json"
REPORT = BASE / "RSR-07_COMPLETION_REPORT.md"
MSS_BACKLOG = ROOT / "governance/application-planning/magic-supernatural-systems/MSS_PROGRAM_BACKLOG.json"

EXPECTED_ORIGINAL = {
    "rsr01:sharra",
    "rsr01:pencrona-world",
    "rsr01:consortium-and-30-winds",
    "rsr01:magen-galaxy-mana-powered-civilization",
}
EXPECTED_PREVIOUS = {
    "rsr01:sharra",
    "rsr01:serpentine-empire-structure-analysis",
    "rsr01:eldritch-hollow",
    "rsr01:traigan-astrological-interpretations",
    "rsr01:kola-ha-bioengineering",
    "rsr01:sherazzalla-world",
    "rsr01:carnival-world",
    "rsr01:helldiving-in-multiversal-realities",
    "rsr01:consortium-s-manipulation-revealed",
    "rsr01:pencrona-world",
    "rsr01:consortium-and-30-winds",
    "rsr01:magen-galaxy-mana-powered-civilization",
}
EXPECTED_COUNTS = {
    "original_rsr01_route_count": 4,
    "previous_route_count": 12,
    "material_signal_count": 22,
    "supplemental_material_signal_count": 10,
    "no_material_signal_count": 2,
}
REQUIRED_BOUNDARY_KINDS = {
    "owner-over-assistant", "mss-taxonomy-axes", "resource-formula",
    "resolution-owner", "rune-boundary", "mss05-preservation",
    "world-timeline-portals", "character-owner", "item-owner",
    "biotech-boundary", "magen-owner-requirement", "pencrona-temporal-portals",
    "thirty-winds-hidden-history", "serpent-psychic-evidence",
    "ocularum-mechanism-unresolved", "helldiving-trans-portal-intent",
    "stable-identities", "future-mss-authority",
}


def load(path: Path):
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


rsr01 = load(RSR01)
rsr06_routing = load(RSR06_ROUTING)
reg = load(REGISTRY)
queue = load(QUEUE)
routing = load(ROUTING)
mss = load(MSS_BACKLOG)
report = REPORT.read_text(encoding="utf-8")

assert reg["work_item"] == "RSR-07"
assert reg["archive_sha256"] == rsr01["archive_sha256"]
assert reg["source_count"] == 24
assert len(reg["records"]) == 24
assert reg["canonical_mss_mutation"] is False
assert reg["mss05_completion_weakened"] is False
assert reg["new_mss_stable_ids"] == 0

r1 = {s["source_id"]: (s["filename"], s["mht_sha256"]) for s in rsr01["sources"]}
r7 = {r["source_id"]: (r["filename"], r["mht_sha256"]) for r in reg["records"]}
assert set(r7) == set(r1), "RSR-07 source-id coverage differs from RSR-01"
assert r7 == r1, "RSR-07 filename/checksum alignment differs from RSR-01"

original = {r["source_id"] for r in reg["records"] if r["originally_routed_to_rsr07"]}
previous = {r["source_id"] for r in reg["records"] if r["previously_routed_to_rsr07"]}
assert original == EXPECTED_ORIGINAL, original
assert previous == EXPECTED_PREVIOUS, previous
r6_route_set = {r["source_id"] for r in rsr06_routing["routes"] if "RSR-07" in r["routes"]}
assert r6_route_set == EXPECTED_PREVIOUS, r6_route_set
for source in rsr01["sources"]:
    if source["source_id"] in EXPECTED_ORIGINAL:
        assert "RSR-07" in source["routes"]

material = [r for r in reg["records"] if r["relevance"] != "none"]
no_material = [r for r in reg["records"] if r["relevance"] == "none"]
supplemental = [r for r in material if not r["previously_routed_to_rsr07"]]
actual_counts = {
    "original_rsr01_route_count": len(original),
    "previous_route_count": len(previous),
    "material_signal_count": len(material),
    "supplemental_material_signal_count": len(supplemental),
    "no_material_signal_count": len(no_material),
}
assert actual_counts == EXPECTED_COUNTS, actual_counts
assert reg["counts"] == EXPECTED_COUNTS
for rec in reg["records"]:
    assert rec["automatic_canon_promotion"] is False
    assert rec["canonical_mss_mutation"] is False
    assert "SGC" in rec["routes"]
    assert rec["assigned_existing_mss_stable_ids"] == []

assert queue["candidate_count"] == 18
assert len(queue["candidates"]) == 18
assert queue["authority_boundary_count"] == 18
assert len(queue["authority_boundaries"]) == 18
assert queue["canonical_mss_mutation"] is False
assert queue["new_mss_stable_ids"] == 0
candidate_ids = [c["candidate_id"] for c in queue["candidates"]]
assert len(candidate_ids) == len(set(candidate_ids))
assert all(cid.startswith("rsr07:") for cid in candidate_ids)
for candidate in queue["candidates"]:
    assert candidate["canonical_status"] == "noncanonical-proposal"
    assert candidate["automatic_canon_promotion"] is False
assert {b["kind"] for b in queue["authority_boundaries"]} == REQUIRED_BOUNDARY_KINDS

assert routing["source_count"] == 24
assert routing["implementation_authority_granted"] is False
assert routing["mss06_implementation_started"] is False
assert {r["source_id"] for r in routing["routes"]} == set(r1)
for route in routing["routes"]:
    assert route["implementation_authority_granted"] is False
    assert "SGC" in route["routes"]

tranches = {t["id"]: t for t in mss["tranches"]}
for ident in ["MSS-01", "MSS-02", "MSS-03", "MSS-04", "MSS-05"]:
    assert tranches[ident]["status"] == "completed_verified"
assert tranches["MSS-06"]["status"] == "planned"
assert tranches["MSS-06"]["activation_after"] == "RSR-07"
assert mss["completed_through"] == "MSS-05"
assert mss["status"] == "paused_for_recovered_source_reconciliation"

required_report_phrases = [
    "24 / 24",
    "original RSR-01 routes to RSR-07: **4**",
    "sources already routed to RSR-07 before this pass: **12**",
    "material supernatural/MSS-adjacent signals: **22**",
    "supplemental material signals recovered beyond prior routes: **10**",
    "explicit no-material-MSS decisions: **2**",
    "source-bound noncanonical supernatural candidates: **18**",
    "explicit authority/uncertainty boundaries: **18**",
    "new MSS stable IDs: **0**",
    "MSS-05 completion weakened: **no**",
    "MSS-06 must be selected_not_started, not implemented in the same tranche",
]
for phrase in required_report_phrases:
    assert phrase in report, f"completion report missing: {phrase}"

print("RSR-07 reconciliation integrity: PASS")
