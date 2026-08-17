from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import re
import zipfile
from pathlib import Path

MASTER_SHA256 = "c5732c5b4c3cdf5eca1d19eef7354289d1f92a87397b56aa7623b3f0a24177ec"
AUDIT_SHA256 = "4a98058b03d3ced252f01dac3026997de2dfd0b064be6a691debb93a0c485fff"
SOURCE_BASE = "MV_Master_01_Core/03_CSV_Sources/"
DATASETS = [
    ("expanded_melee_weapons_all_genres.csv", "Melee_Weapons.csv", "Weapon", 327),
    ("expanded_ranged_weapons_catalog.csv", "Ranged_Weapons.csv", "Weapon", 230),
    ("weapons_and_ammo.csv", "Weapons_Ammo.csv", "Weapon", 36),
    ("expanded_items_all_genres.csv", "Items.csv", "Item", 761),
    ("expanded_magitech_items_all_genres.csv", "Magitech_Items.csv", "Item", 532),
    ("expanded_eva_suits_and_modules_all_genres.csv", "EVA_Suits.csv", "Item", 430),
    ("expanded_computers_all_genres.csv", "Computers.csv", "Item_Name", 1000),
    ("expanded_living_spellbooks_and_magic_charge_holders_all_genres.csv", "Living_Spellbooks.csv", "Item_Name", 1501),
    ("expanded_symbiotes_and_cybernetics_all_genres.csv", "Symbiotes_Cybernetics.csv", "Item", 572),
]
TOTAL = 5389


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def norm(value: str) -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"[™®©]", "", value)
    return re.sub(r"\s+", " ", value)


def row_fingerprint(row: dict[str, str]) -> str:
    payload = "\x1f".join(f"{key}\x1e{value or ''}" for key, value in row.items())
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def first(row: dict[str, str], names: list[str]) -> str:
    for name in names:
        if name in row and (row.get(name) or "").strip():
            return (row.get(name) or "").strip()
    return ""


def anchor_label(anchor: str) -> str:
    value = (anchor or "").strip()
    if ":" in value:
        prefix, suffix = value.split(":", 1)
        if re.search(r"\b(page|row)\b", prefix, re.I):
            value = suffix.strip()
    return norm(value)


def read_sources(master: Path) -> list[dict[str, object]]:
    if sha256_file(master) != MASTER_SHA256:
        raise SystemExit("master source snapshot SHA-256 mismatch")
    rows: list[dict[str, object]] = []
    with zipfile.ZipFile(master) as archive:
        for governed, filename, name_column, expected_rows in DATASETS:
            raw = archive.read(SOURCE_BASE + filename).decode("utf-8-sig")
            source_rows = list(csv.DictReader(io.StringIO(raw)))
            if len(source_rows) != expected_rows:
                raise SystemExit(f"row-count mismatch for {filename}")
            for row_number, row in enumerate(source_rows, start=2):
                rows.append({
                    "governed_dataset": governed,
                    "source_file": filename,
                    "source_row_number": row_number,
                    "source_display_name": (row.get(name_column) or "").strip(),
                    "normalized_name": norm(row.get(name_column) or ""),
                    "row": row,
                })
    if len(rows) != TOTAL:
        raise SystemExit(f"source total mismatch: {len(rows)} != {TOTAL}")
    return rows


def read_occurrence_candidates(audit_zip: Path) -> dict[str, list[str]]:
    if sha256_file(audit_zip) != AUDIT_SHA256:
        raise SystemExit("8E-008G audit package SHA-256 mismatch")
    with zipfile.ZipFile(audit_zip) as archive:
        member = next(name for name in archive.namelist() if name.endswith("Multiversal_8E-008G_Source_Reference_Occurrence_Map.csv"))
        occurrences = csv.DictReader(io.StringIO(archive.read(member).decode("utf-8-sig")))
        mapping: dict[str, set[str]] = collections.defaultdict(set)
        for occurrence in occurrences:
            if occurrence["record_type"] not in {"mv.object.item-definition", "item"}:
                continue
            label = anchor_label(occurrence["anchor"])
            if label:
                mapping[label].add(occurrence["record_id"])
    return {key: sorted(values) for key, values in mapping.items()}


def provenance_flags(text: str) -> str:
    low = (text or "").lower()
    flags: list[str] = []
    for label, marker in [
        ("expanded-design", "expanded design"),
        ("best-judgment", "best judgment"),
        ("inferred", "infer"),
        ("completed-fields", "completed"),
        ("ammo-only", "ammo-only"),
        ("malformed-source-completion", "malformed"),
    ]:
        if marker in low:
            flags.append(label)
    return "|".join(flags)


def build(master: Path, audit_zip: Path, output: Path) -> None:
    rows = read_sources(master)
    candidates = read_occurrence_candidates(audit_zip)
    name_counts = collections.Counter(str(row["normalized_name"]) for row in rows if row["normalized_name"])
    result: list[dict[str, object]] = []
    for source in rows:
        row = source["row"]
        assert isinstance(row, dict)
        name = str(source["normalized_name"])
        definition_ids = candidates.get(name, [])
        candidate_state = (
            "one_exact_anchor_definition_candidate" if len(definition_ids) == 1
            else "multiple_exact_anchor_definition_candidates" if len(definition_ids) > 1
            else "no_exact_anchor_definition_evidence"
        )
        provenance = first(row, ["Origin", "Source Notes", "Source_PDF", "Source PDF"])
        result.append({
            "source_file": source["source_file"],
            "governed_dataset": source["governed_dataset"],
            "source_row_number": source["source_row_number"],
            "source_row_fingerprint_sha256": row_fingerprint(row),
            "explicit_source_id": first(row, ["Item_ID", "Catalog_ID", "ID", "Item ID"]),
            "source_record_kind_raw": first(row, ["Record_Type", "Item Type", "Upgrade Class", "Category"]),
            "normalized_name_occurrence_count": name_counts.get(name, 0),
            "identity_review_required": name_counts.get(name, 0) > 1 or len(definition_ids) != 1,
            "current_definition_candidate_state": candidate_state,
            "current_definition_candidate_ids": "|".join(definition_ids),
            "provenance_transformation_signals": provenance_flags(provenance),
            "taxonomy_registry_state": "exact_v0_12_registry_unavailable",
            "v0_12_projection_status": "blocked_before_taxonomy_assignment",
            "v0_12_taxonomy_assertions": "",
            "v0_12_content_context_assertions": "",
            "v0_12_product_identity_assertions": "",
            "v0_12_creator_origin_assertions": "",
            "required_next_step": "load_checksum_verified_v0_12_registry_and_prepared_crosswalks",
        })
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(result[0]))
        writer.writeheader()
        writer.writerows(result)
    print(f"ITEM-CORPUS-PREPROJECTION: PASS rows={len(result)} sha256={sha256_file(output)}")
    print("taxonomy_assignments=0 source_mutation=false exact_registry_required=true")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the source-only Item preprojection envelope without inventing v0.12.0 taxonomy values.")
    parser.add_argument("--source-zip", required=True, type=Path)
    parser.add_argument("--audit-zip", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    build(args.source_zip, args.audit_zip, args.output)


if __name__ == "__main__":
    main()
