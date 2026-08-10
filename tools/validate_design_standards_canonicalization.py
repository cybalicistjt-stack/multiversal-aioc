#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
BASE = REPO / "governance" / "design-standards" / "canonicalization"
CANDIDATES = BASE / "CANONICAL_CANDIDATE_MANIFEST.json"
LEGACY = BASE / "LEGACY_AND_DUPLICATE_DISPOSITIONS.json"
AUDIT = BASE / "DS_CANONICALIZATION_AUDIT_v1.0.0.md"

EXPECTED_FINAL = {
    "DS-008": (
        "DS-008_ACCESSIBILITY_STANDARDS (4).md",
        "DS-008_ACCESSIBILITY_STANDARDS.md",
        "795846072e4dc4f24dfe2ba62060e10bd74fa385cca0594fa2479632409df193",
    ),
    "DS-009": (
        "DS-009_TOKEN_STANDARDS.md",
        "DS-009_TOKEN_STANDARDS.md",
        "43d2601def89d9a1019de7d482d544617d874020b72abe73918d8125a6024545",
    ),
    "DS-010": (
        "DS-010_FLUTTER_IMPLEMENTATION_STANDARDS.md",
        "DS-010_FLUTTER_IMPLEMENTATION_STANDARDS.md",
        "1225fcde9305834a06644d74178804ed31d3d3d2c2d4e4530d0efc74bc6ddf97",
    ),
    "DS-011": (
        "DS-011_TESTING_STANDARDS.md",
        "DS-011_TESTING_STANDARDS.md",
        "1d70803c6f55220e44bf775f8793bfbf712c1dd7586ea42dc8b35aa56f7d3af1",
    ),
    "DS-012": (
        "DS-012_VISUAL_LANGUAGE_STANDARDS.md",
        "DS-012_VISUAL_LANGUAGE_STANDARDS.md",
        "f2d3ee12d65ce7cf1ce5bd5720cedb183c930e8f86debfdbe06c26c4a785ff2d",
    ),
}


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    for path in (CANDIDATES, LEGACY, AUDIT):
        if not path.is_file():
            fail(f"missing required canonicalization artifact: {path.relative_to(REPO)}")

    candidates = json.loads(CANDIDATES.read_text(encoding="utf-8"))
    legacy = json.loads(LEGACY.read_text(encoding="utf-8"))
    audit_text = AUDIT.read_text(encoding="utf-8")

    finals = candidates.get("validated_ds008_012")
    if not isinstance(finals, list) or len(finals) != 5:
        fail("validated_ds008_012 must contain exactly five final standards")

    by_standard = {row.get("standard"): row for row in finals}
    if set(by_standard) != set(EXPECTED_FINAL):
        fail(f"unexpected final standard set: {sorted(by_standard)}")

    for standard, (source_file, canonical_filename, expected_hash) in EXPECTED_FINAL.items():
        row = by_standard[standard]
        expected = {
            "source_file": source_file,
            "canonical_filename": canonical_filename,
            "sha256": expected_hash,
            "validation": "PASS",
            "disposition": "FINAL_VALIDATED",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                fail(f"{standard} {key} mismatch: {row.get(key)!r} != {value!r}")
        if expected_hash not in audit_text:
            fail(f"audit does not contain final hash for {standard}")

    note = candidates.get("note", "")
    if "repository ingestion required" not in note.lower():
        fail("candidate manifest must explicitly say repository ingestion is required")

    audit_lower = audit_text.lower()
    if "canonical ingestion required" not in audit_lower or "does not" not in audit_lower or "canonical" not in audit_lower:
        fail("audit must explicitly retain the canonical-ingestion boundary")

    ds006 = candidates.get("ds006_selected") or []
    ds007 = candidates.get("ds007_selected") or []
    if len(ds006) != 14:
        fail(f"DS-006 selected set must contain 14 entries, got {len(ds006)}")
    if len(ds007) != 10:
        fail(f"DS-007 selected set must contain 10 entries, got {len(ds007)}")

    required_ds007 = {
        "67/DS-007A_Responsive_Architecture_Foundations_v1.0_FINAL.zip",
        "67/DS-007G_Landscape_Portrait_Behavior_v1.1_FINAL.zip",
        "67/DS-007H_Accessibility_Zoom_Large_Text_Responsive_Rules_v1.0_FINAL.zip",
        "67/DS-007I_Adaptive_Breakpoints_Density_Recomposition_Rules_v1.0_FINAL.zip",
        "67/DS-007J_Responsive_QA_Acceptance_Standards_v1.0_FINAL.zip",
    }
    missing = required_ds007 - set(ds007)
    if missing:
        fail(f"selected DS-007 set missing required current versions: {sorted(missing)}")
    if any("v0.2" in entry for entry in ds007):
        fail("selected DS-007 set must not contain superseded v0.2 DS-007A")

    legacy_by_file = {row.get("file"): row for row in legacy}
    required_legacy = {
        "DS-008_ACCESSIBILITY_STANDARDS.md": "OLDER_DRAFT",
        "DS-008_Audio_and_Haptic_System_v0.1.md": "LEGACY_NUMBERING",
        "DS-009_Accessibility_System_v0.1.md": "LEGACY_NUMBERING",
        "DS-010_Layout_Architecture_v0.1.md": "LEGACY_NUMBERING",
        "DS-011_Navigation_Architecture_v0.1.md": "LEGACY_NUMBERING",
        "67/DS-006_Iconography_System_v0.1.md": "LEGACY_NUMBERING",
        "67/DS-007_Motion_System_v0.1.md": "LEGACY_NUMBERING",
        "67/DS-007A_Responsive_Architecture_Foundations_v0.2_FINAL.zip": "SUPERSEDED_VERSION",
        "67.zip": "DUPLICATE_TRANSPORT_CONTAINER",
    }
    for filename, disposition in required_legacy.items():
        row = legacy_by_file.get(filename)
        if row is None:
            fail(f"legacy disposition missing: {filename}")
        if row.get("disposition") != disposition:
            fail(f"legacy disposition mismatch for {filename}: {row.get('disposition')} != {disposition}")

    old_ds008 = legacy_by_file["DS-008_ACCESSIBILITY_STANDARDS.md"].get("sha256")
    if old_ds008 == EXPECTED_FINAL["DS-008"][2]:
        fail("old unnumbered DS-008 draft must not equal the final validated DS-008 hash")

    selected_paths = set(ds006) | set(ds007)
    for row in legacy:
        if row.get("file") in selected_paths:
            fail(f"legacy artifact appears in selected candidate set: {row.get('file')}")

    print("Design Standards canonicalization validation: PASS")
    print("- final DS-008 through DS-012 hashes/dispositions: PASS")
    print("- DS-006 selected package set: PASS")
    print("- DS-007 selected current-version set: PASS")
    print("- legacy/duplicate exclusion: PASS")
    print("- repository-ingestion boundary: PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"Design Standards canonicalization validation: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
