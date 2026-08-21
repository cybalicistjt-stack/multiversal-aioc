#!/usr/bin/env python3
"""Validate permanent RSR-01 archive/provenance/disposition artifacts."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/source-material/recovered-legacy/now-this-2026-08-21"
ARCHIVE_SHA = "2a5eae712f483d1fb33ff9fb0087e96c4eb8b71b287cc707c196a4c17a2f78f4"
ALLOWED = {
    "existing-covered",
    "existing-needs-reconciliation",
    "new-candidate",
    "conflict-owner-review",
    "proposal-only",
    "visual-reference",
    "inert",
}


def load(name: str) -> dict:
    path = BASE / name
    assert path.is_file(), f"missing RSR-01 artifact: {path.relative_to(ROOT)}"
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), f"expected object JSON: {name}"
    return value


def main() -> int:
    manifest_path = BASE / "SOURCE_MANIFEST.md"
    report_path = BASE / "RSR-01_COMPLETION_REPORT.md"
    assert manifest_path.is_file(), "source manifest missing"
    assert report_path.is_file(), "completion report missing"
    manifest = manifest_path.read_text(encoding="utf-8")
    report = report_path.read_text(encoding="utf-8")
    assert ARCHIVE_SHA in manifest
    assert ARCHIVE_SHA in report

    manifest_rows = dict(re.findall(r"\| `([^`]+\.mht)` \| `([0-9a-f]{64})` \|", manifest))
    assert len(manifest_rows) == 24, f"manifest must contain 24 MHT checksums, got {len(manifest_rows)}"

    receipt = load("RSR-01_EXTRACTION_RECEIPT.json")
    assert receipt["archive_sha256"] == ARCHIVE_SHA
    assert receipt["constituent_count"] == 24
    assert receipt["extracted_turn_count"] == 102
    assert receipt["owner_turn_count"] == 47
    assert receipt["assistant_turn_count"] == 55
    assert receipt["unique_embedded_media_count"] == 12
    assert receipt["substantive_unique_media_count"] == 11
    assert receipt["exact_source_bytes_retained_outside_repository"] is True
    assert receipt["source_bytes_reconstructed_or_replaced"] is False
    receipt_rows = {row["filename"]: row["sha256"] for row in receipt["constituents"]}
    assert receipt_rows == manifest_rows, "receipt constituent checksums must exactly match source manifest"

    messages = load("RSR-01_MESSAGE_PROVENANCE_INDEX.json")
    assert messages["archive_sha256"] == ARCHIVE_SHA
    assert messages["source_count"] == 24
    assert messages["message_count"] == 102
    assert messages["owner_turn_count"] == 47
    assert messages["assistant_turn_count"] == 55
    message_files = {row["file"] for row in messages["sources"]}
    assert message_files == set(manifest_rows), "message index must cover exactly the 24 retained sources"
    owner = assistant = total = 0
    for row in messages["sources"]:
        roles = row["roles"]
        hashes = row["turn_sha256s"]
        assert roles and set(roles) <= {"O", "P"}, f"invalid role stream for {row['file']}"
        assert len(hashes) == len(roles) * 64, f"turn hash stream length mismatch for {row['file']}"
        assert re.fullmatch(r"[0-9a-f]+", hashes), f"invalid turn hash characters for {row['file']}"
        total += len(roles)
        owner += roles.count("O")
        assistant += roles.count("P")
    assert (total, owner, assistant) == (102, 47, 55)
    assert "proposal-only" in messages["authority_rule"]

    media = load("RSR-01_MEDIA_PROVENANCE_INDEX.json")
    assert media["archive_sha256"] == ARCHIVE_SHA
    assert media["unique_media_count"] == 12
    assert media["substantive_unique_media_count"] == 11
    assert len(media["media"]) == 12
    classifications = Counter(row["classification"] for row in media["media"])
    assert classifications["ui-non-substantive-repeated-profile-thumbnail"] == 1
    assert classifications["substantive-embedded-media"] == 11
    ui = next(row for row in media["media"] if row["classification"] == "ui-non-substantive-repeated-profile-thumbnail")
    assert ui["byte_size"] == 7929 and len(ui["occurrences"]) == 24

    dispositions = load("RSR-01_DISPOSITION_REGISTRY.json")
    assert dispositions["archive_sha256"] == ARCHIVE_SHA
    assert dispositions["source_count"] == 24
    rows = dispositions["sources"]
    assert len(rows) == 24
    assert {row["filename"] for row in rows} == set(manifest_rows)
    assert {row["mht_sha256"] for row in rows} == set(manifest_rows.values())
    assert all(row["primary_disposition"] in ALLOWED for row in rows)
    assert all(row["automatic_canon_promotion"] is False for row in rows)
    assert all(row["routes"] for row in rows)
    counts = Counter(row["primary_disposition"] for row in rows)
    assert counts == Counter({"existing-needs-reconciliation": 14, "new-candidate": 10}), counts
    assert dispositions["next_tranche"] == "RSR-02"

    for required in (
        "102 (47 owner/user; 55 assistant)",
        "14",
        "10",
        "RSR-02",
        "assistant-generated-proposal",
        "not reconstructed",
    ):
        assert required in report, f"completion report missing required boundary/evidence: {required}"

    print("RSR-01 archive/provenance/disposition verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
