from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/game-content-preparation/items"
SUMMARY = BASE / "ITEM_CORPUS_TAXONOMY_COVERAGE_SUMMARY_v0.1.0.json"
AUDIT = BASE / "ITEM_CORPUS_TAXONOMY_COVERAGE_AUDIT.md"
PLAN = BASE / "ITEM_CORPUS_TAXONOMY_EXECUTION_PLAN.md"
CHECKPOINT = ROOT / "governance/ai/work-state/ITEM-CORPUS-AUDIT-001-attempt-001.json"

errors: list[str] = []
for p in (SUMMARY, AUDIT, PLAN, CHECKPOINT):
    if not p.is_file():
        errors.append(f"missing {p.relative_to(ROOT)}")

if not errors:
    data = json.loads(SUMMARY.read_text(encoding="utf-8"))
    corpus = data["corpus"]
    if corpus["total_rows"] != 5389:
        errors.append("total Item corpus rows must remain 5389")
    if corpus["dataset_count"] != 9:
        errors.append("direct Item dataset count must remain 9")
    if corpus["genre_all_genres"] + corpus["genre_specific"] + corpus["genre_blank"] != 5389:
        errors.append("Genre preview accounting must equal 5389")
    if sum(d["rows"] for d in data["datasets"]) != 5389:
        errors.append("dataset row totals must equal 5389")
    prepared = data["prepared_item_system"]
    expected = {
        "taxonomy_axes": 10,
        "taxonomy_controlled_values": 171,
        "content_context_facets": 9,
        "content_context_controlled_values": 241,
        "coverage_domains": 35,
        "coverage_profiles": 28,
        "coverage_expectation_rows": 980,
        "source_linked_provenance_occurrences": 1050,
        "recovered_armor_material_concepts": 55,
        "missing_armor_material_concepts": 54,
        "enrichment_remechanization_work_items": 5443,
    }
    for key, value in expected.items():
        if prepared.get(key) != value:
            errors.append(f"{key} expected {value}, got {prepared.get(key)!r}")
    app = data["canonical_application_evidence"]
    if app["content_context_registry_values_embedded"] is not False:
        errors.append("audit must preserve A8 non-embedding of Content Context registry values")
    if app["full_5389_shadow_projection_evidence_found"] is not False:
        errors.append("audit must not claim a full shadow projection without new evidence")
    verdict = data["audit_verdict"]
    if verdict["source_rows_accounted"] != 5389:
        errors.append("source rows accounted must be 5389")
    if verdict["rows_with_verified_full_v0_12_governed_adoption"] != 0:
        errors.append("verified full v0.12 adoption count must remain evidence-backed, currently 0")
    phases = {row["phase"]: row["assessment"] for row in data["phase_assessment"]}
    if set(phases) != {f"IA-I{i}" for i in range(13)}:
        errors.append("phase assessment must cover IA-I0 through IA-I12")
    if phases["IA-I4"] != "not_verified":
        errors.append("IA-I4 must remain not_verified until a full 5389-row projection receipt exists")
    if phases["IA-I11"] != "not_verified":
        errors.append("IA-I11 must remain not_verified until the 5443-work-item queue has execution evidence")

if errors:
    raise SystemExit("ITEM-CORPUS-AUDIT-001: FAIL\n- " + "\n- ".join(errors))
print("ITEM-CORPUS-AUDIT-001: PASS")
print("datasets=9 source_rows=5389 verified_v0_12_adopted=0 prepared_work_items=5443")
