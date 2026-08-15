#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/stage-a-a8/supplemental-authority"


def fail(message: str) -> None:
    raise SystemExit(f"A8 SUPPLEMENT: FAIL — {message}")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def main() -> None:
    required = [
        BASE / "README.md",
        BASE / "STAGE_A_A8_SUPPLEMENTAL_AUTHORITY_RECONCILIATION.md",
        BASE / "STAGE_A_A8_SUPPLEMENTAL_SOURCE_MANIFEST.json",
        BASE / "STAGE_A_A8_SUPPLEMENTAL_AUTHORITY_MATRIX.csv",
        BASE / "SHARED_CONTENT_CONTEXT_CONTRACT.md",
        ROOT / "governance/ai/work-state/STAGE-A-A8-R0-attempt-001.json",
    ]
    for path in required:
        require(path.is_file(), f"missing {path.relative_to(ROOT)}")

    manifest = json.loads((BASE / "STAGE_A_A8_SUPPLEMENTAL_SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    expected_sources = {
        "platform-v0.11.0": "621b498b6d0fa1b99c86a96eac7446f682c715cb576cf0803d233ec2ffe0bdb6",
        "item-v0.12.0": "d12feab1375930e1ef5c121d485aee8622f2abfc34c05f23babb26a293ee47ca",
        "reality-v0.14.0": "928aaacbd84082d88ea9e64fc6c3506a321f26633bce718cfb46199b5364f4d6",
        "adding-conversation-bundle": "a550ed965e4433dc9a3d800ef7aebda4f699c363db8ef8037d104a4a844d6277",
    }
    got_sources = {row["source_id"]: row["sha256"] for row in manifest["sources"]}
    require(got_sources == expected_sources, "source archive hash manifest mismatch")
    require(all(not row["archive_bytes_in_repository"] for row in manifest["sources"]), "binary archive transfer state must remain explicit")

    for entry in manifest["extracted_contracts"]:
        path = BASE / entry["path"]
        require(path.is_file(), f"missing extracted contract {entry['path']}")
        require(sha256(path) == entry["sha256"], f"checksum mismatch for {entry['path']}")

    with (BASE / "STAGE_A_A8_SUPPLEMENTAL_AUTHORITY_MATRIX.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    require(len(rows) >= 24, "authority matrix must contain at least 24 governed decisions")
    by_area = {row["area"]: row for row in rows}
    for area in [
        "item_definition_instance",
        "vehicle_model_instance",
        "shared_creator",
        "shared_content_context",
        "intrinsic_affinity_compatibility",
        "setting_context_adapter",
        "economy_boundary",
    ]:
        require(area in by_area, f"missing authority area {area}")
    require(by_area["full_reality_topology"]["decision"] == "DEFER", "full Reality topology must remain deferred")
    require(by_area["community_world_features"]["decision"] == "DEFER", "community features must remain deferred")
    require(by_area["campaign_setting_state"]["decision"] == "PROHIBIT_DUPLICATION", "PPIA-08 boundary missing")

    shared = (BASE / "SHARED_CONTENT_CONTEXT_CONTRACT.md").read_text(encoding="utf-8")
    for phrase in [
        "Setting Family",
        "Genre Tradition",
        "Era / Development",
        "Technology Paradigm",
        "Power Paradigm",
        "Environment",
        "Play Domain",
        "Tone / Style",
        "Content Scale",
        "241 controlled values",
    ]:
        require(phrase in shared, f"shared content-context contract missing {phrase}")

    reconcile = (BASE / "STAGE_A_A8_SUPPLEMENTAL_AUTHORITY_RECONCILIATION.md").read_text(encoding="utf-8")
    for phrase in [
        "expand → project → validate → review → enable",
        "Item Definition vs Item Instance/Asset",
        "Platform/Vehicle Model vs Individual Vehicle Asset",
        "A8 must not absorb",
        "No A8 application mutation begins",
    ]:
        require(phrase in reconcile, f"reconciliation missing invariant: {phrase}")

    roadmap = (ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md").read_text(encoding="utf-8")
    require("**Version:** 2.13.0" in roadmap, "roadmap version not projected to 2.13.0")
    require("stage-a-a8/supplemental-authority/STAGE_A_A8_SUPPLEMENTAL_AUTHORITY_RECONCILIATION.md" in roadmap, "roadmap missing A8 supplemental authority path")
    require("A8 REVALIDATION NEXT" in roadmap, "roadmap must keep A8 revalidation next")

    bootstrap = (ROOT / "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md").read_text(encoding="utf-8")
    require("**Version:** 5.6.0" in bootstrap, "bootstrap version not projected to 5.6.0")
    require("stage-a-a8/supplemental-authority/STAGE_A_A8_SUPPLEMENTAL_AUTHORITY_RECONCILIATION.md" in bootstrap, "bootstrap missing A8 supplemental authority recovery rule")

    pointer = json.loads((ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json").read_text(encoding="utf-8"))
    require(pointer["primary_attempt_id"] == "STAGE-A-A8-R0-attempt-001", "pointer primary is not A8 R0")
    require(any(t.get("next_work_item_id") == "STAGE-A-A8" for t in pointer.get("deferred_tracks", [])), "pointer missing A8 next-work routing")

    status = json.loads((ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json").read_text(encoding="utf-8"))
    require(status["primary"]["work_item_id"] == "STAGE-A-A8-R0", "implementation status primary is not A8 R0")

    roadmap_index = json.loads((ROOT / "governance/ai/runtime/ROADMAP_INDEX.json").read_text(encoding="utf-8"))
    require(any(e.get("work_item_id") == "STAGE-A-A8" for e in roadmap_index["entries"]), "ROADMAP_INDEX missing STAGE-A-A8")

    checkpoint = json.loads((ROOT / "governance/ai/work-state/STAGE-A-A8-R0-attempt-001.json").read_text(encoding="utf-8"))
    require(checkpoint["status"] in {"ready_for_review", "completed_verified"}, "unexpected R0 checkpoint state")
    require(checkpoint["restrictions"]["a8_activated"] is False, "R0 must not activate A8")
    require(checkpoint["restrictions"]["full_reality_implementation_authorized"] is False, "R0 must not activate Reality")

    forbidden = list(BASE.rglob("*.zip")) + list(BASE.rglob("*.mht"))
    require(not forbidden, "raw binary/conversation archive must not be reconstructed in text-only transfer package")

    print(f"A8 SUPPLEMENT: PASS extracted_contracts={len(manifest['extracted_contracts'])} authority_rows={len(rows)}")


if __name__ == "__main__":
    main()
