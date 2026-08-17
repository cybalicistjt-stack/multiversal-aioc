from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/game-content-preparation/items"
SUMMARY = BASE / "ITEM_CORPUS_TAXONOMY_COVERAGE_SUMMARY_v0.1.0.json"
CROSSWALK_SUMMARY = BASE / "ITEM_CORPUS_CURRENT_DEFINITION_CROSSWALK_SUMMARY_v0.1.0.json"
WEAPONS_CROSSWALK = BASE / "WEAPONS_AMMO_SOURCE_AND_IDENTITY_CROSSWALK_v0.1.0.csv"
AUDIT = BASE / "ITEM_CORPUS_TAXONOMY_COVERAGE_AUDIT.md"
PLAN = BASE / "ITEM_CORPUS_TAXONOMY_EXECUTION_PLAN.md"
CHECKPOINT = ROOT / "governance/ai/work-state/ITEM-CORPUS-AUDIT-001-attempt-001.json"
GENERATOR = ROOT / "tools/build_item_corpus_row_accounting.py"

errors: list[str] = []
for p in (SUMMARY, CROSSWALK_SUMMARY, WEAPONS_CROSSWALK, AUDIT, PLAN, CHECKPOINT, GENERATOR):
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

    cross = json.loads(CROSSWALK_SUMMARY.read_text(encoding="utf-8"))
    results = cross["results"]
    if results["one_exact_anchor_definition_candidate_rows"] != 466:
        errors.append("exact-one definition candidate row count must remain 466")
    if results["multiple_exact_anchor_definition_candidate_rows"] != 13:
        errors.append("multiple-definition candidate row count must remain 13")
    if results["no_exact_anchor_definition_evidence_rows"] != 4910:
        errors.append("no-exact-definition-evidence row count must remain 4910")
    if results["rows_with_any_exact_anchor_definition_candidate"] != 479:
        errors.append("rows with exact occurrence candidates must remain 479")
    repeated = cross["repeated_name_review"]
    if repeated["normalized_name_groups"] != 55 or repeated["participating_rows"] != 119:
        errors.append("repeated-name review must remain 55 groups / 119 rows")
    if len(cross["multiple_candidate_conflicts"]) != 13:
        errors.append("multiple-candidate conflict list must contain 13 entries")

    with WEAPONS_CROSSWALK.open(encoding="utf-8", newline="") as handle:
        weapon_rows = list(csv.DictReader(handle))
    if len(weapon_rows) != 36:
        errors.append("Weapons_Ammo crosswalk must contain 36 source rows")
    recovered = sum(row["source_note_state"] == "recovered_from_8E008G" for row in weapon_rows)
    reference_only = sum(row["current_definition_relation"] == "source_reference_only_no_current_definition" for row in weapon_rows)
    linked_or_mode = [row for row in weapon_rows if row["current_definition_id"]]
    unique_definition_ids = {row["current_definition_id"] for row in linked_or_mode}
    if recovered != 28:
        errors.append(f"Weapons_Ammo recovered provenance count must be 28, got {recovered}")
    if len(linked_or_mode) != 33:
        errors.append(f"Weapons_Ammo definition-linked/mode-reference rows must be 33, got {len(linked_or_mode)}")
    if len(unique_definition_ids) != 31:
        errors.append(f"Weapons_Ammo unique current Definition IDs must be 31, got {len(unique_definition_ids)}")
    if reference_only != 3:
        errors.append(f"Weapons_Ammo source-reference-only rows must be 3, got {reference_only}")
    if any(row["v0_12_taxonomy_status"] != "not_projected" for row in weapon_rows):
        errors.append("Weapons_Ammo crosswalk must not claim v0.12 taxonomy projection")

if errors:
    raise SystemExit("ITEM-CORPUS-AUDIT-001: FAIL\n- " + "\n- ".join(errors))
print("ITEM-CORPUS-AUDIT-001: PASS")
print("datasets=9 source_rows=5389 exact_definition_candidates=479 repeated_name_groups=55")
print("weapons_ammo=36 provenance_recovered=28 linked_rows=33 reference_only=3")
print("verified_v0_12_adopted=0 prepared_work_items=5443")
