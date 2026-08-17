from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import re
import zipfile
from pathlib import Path

EXPECTED_MASTER_SHA256 = "c5732c5b4c3cdf5eca1d19eef7354289d1f92a87397b56aa7623b3f0a24177ec"
BASE = "MV_Master_01_Core/03_CSV_Sources/"
DATASETS = [
    ("expanded_melee_weapons_all_genres.csv", "Melee_Weapons.csv", "Weapon", "9c6de3cba7254fd0c4928cc644d127a23993bced533b64bc40b414016ab109ed", 327),
    ("expanded_ranged_weapons_catalog.csv", "Ranged_Weapons.csv", "Weapon", "ecafc340c204847555db0e8a4f87fe8bf3980c87c739c1c8491f8e80f8934846", 230),
    ("weapons_and_ammo.csv", "Weapons_Ammo.csv", "Weapon", "d6d3d80b208ad40dd812a22d8234b0e3a5395526da90d8f4da7e944ea180d719", 36),
    ("expanded_items_all_genres.csv", "Items.csv", "Item", "f67a02a7d36e39f4837dbca4c2b75e3773fe6a0a8de58c278b2703c2b45d5cee", 761),
    ("expanded_magitech_items_all_genres.csv", "Magitech_Items.csv", "Item", "9835233c515f90917d022e540cce221df724320775a8c6fbbc8e0f27c8cd3a55", 532),
    ("expanded_eva_suits_and_modules_all_genres.csv", "EVA_Suits.csv", "Item", "e81d19f521d956a4955e418a9701db761a781911fd697c5b92fcde3ad61512b1", 430),
    ("expanded_computers_all_genres.csv", "Computers.csv", "Item_Name", "ec20b7ba6967a8c0533f6ca2ccf6f46b9bb72151ba3d3723432c4b6cdbfeee9d", 1000),
    ("expanded_living_spellbooks_and_magic_charge_holders_all_genres.csv", "Living_Spellbooks.csv", "Item_Name", "9330cb953171667374e7233c9dbf70fcc2261c163006c7832d33a8976d7e353d", 1501),
    ("expanded_symbiotes_and_cybernetics_all_genres.csv", "Symbiotes_Cybernetics.csv", "Item", "37af1a950d1f7642c65c00475a96545b70225622c8b2c86f9f399b585e57d8a2", 572),
]
EXPECTED_TOTAL_ROWS = 5389


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def norm_name(value: str) -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"\s+", " ", value)
    return re.sub(r"[™®©]", "", value)


def first(row: dict[str, str], candidates: list[str]) -> str:
    for name in candidates:
        if name in row:
            return (row.get(name) or "").strip()
    return ""


def serialize_row(row: dict[str, str]) -> bytes:
    text = "\x1f".join(f"{k}\x1e{(v or '')}" for k, v in row.items())
    return text.encode("utf-8")


def load_rows(source_zip: Path) -> list[dict[str, object]]:
    if sha256_file(source_zip) != EXPECTED_MASTER_SHA256:
        raise SystemExit("source snapshot SHA-256 mismatch")
    output: list[dict[str, object]] = []
    with zipfile.ZipFile(source_zip) as zf:
        for governed, filename, name_col, expected_sha, expected_rows in DATASETS:
            raw = zf.read(BASE + filename)
            if sha256_bytes(raw) != expected_sha:
                raise SystemExit(f"source member SHA-256 mismatch: {filename}")
            rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
            if len(rows) != expected_rows:
                raise SystemExit(f"row-count mismatch: {filename}: {len(rows)} != {expected_rows}")
            for row_number, row in enumerate(rows, start=2):
                name = norm_name(row.get(name_col) or "")
                genre = first(row, ["Genre"])
                genre_state = "blank"
                if genre:
                    genre_state = "all-genres-source-signal" if "all genre" in genre.lower() else "specific-source-signal"
                output.append({
                    "governed_dataset": governed,
                    "source_file": filename,
                    "source_row_number": row_number,
                    "row_fingerprint_sha256": sha256_bytes(serialize_row(row)),
                    "_norm_name": name,
                    "explicit_source_id_present": bool(first(row, ["Item_ID", "Catalog_ID", "ID", "Item ID"])),
                    "category_like_present": bool(first(row, ["Category", "Record_Type", "Item Type", "Upgrade Class"])),
                    "subcategory_like_present": bool(first(row, ["Subcategory", "Module Family", "Family", "Subtype"])),
                    "technology_or_tier_present": bool(first(row, ["Tech Tier", "Tech or Bio Tier", "Tech_Magic_Tier", "Tier"])),
                    "rarity_present": bool(first(row, ["Rarity"])),
                    "origin_or_source_present": bool(first(row, ["Origin", "Source_PDF", "Source PDF", "Source Notes"])),
                    "genre_signal_state": genre_state,
                })
    if len(output) != EXPECTED_TOTAL_ROWS:
        raise SystemExit(f"total-row mismatch: {len(output)} != {EXPECTED_TOTAL_ROWS}")
    return output


def build_ledger(rows: list[dict[str, object]], output: Path) -> None:
    counts = collections.Counter(str(r["_norm_name"]) for r in rows if r["_norm_name"])
    dataset_sets: dict[str, set[str]] = {}
    for name, count in counts.items():
        if count > 1:
            dataset_sets[name] = {str(r["governed_dataset"]) for r in rows if r["_norm_name"] == name}
    clean: list[dict[str, object]] = []
    for row in rows:
        name = str(row.pop("_norm_name"))
        count = counts.get(name, 0)
        clean.append({
            **row,
            "normalized_name_occurrence_count": count,
            "same_normalized_name_review_required": count > 1,
            "cross_dataset_same_name_review_required": count > 1 and len(dataset_sets.get(name, set())) > 1,
            "v0_12_projection_status": "not_verified_projected",
            "v0_12_adoption_status": "not_verified_adopted",
            "required_next_state": "project_from_exact_v0_12_registry_then_review",
        })
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(clean[0]))
        writer.writeheader()
        writer.writerows(clean)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a source-safe 5,389-row Item corpus accounting ledger without assigning taxonomy values.")
    parser.add_argument("--source-zip", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    rows = load_rows(args.source_zip)
    build_ledger(rows, args.output)
    digest = sha256_file(args.output)
    print(f"ITEM-CORPUS-ROW-ACCOUNTING: PASS rows={len(rows)} sha256={digest}")
    print("taxonomy_projection=not_performed taxonomy_adoption=not_performed source_mutation=false")


if __name__ == "__main__":
    main()
