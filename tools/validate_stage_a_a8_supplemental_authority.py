#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/stage-a-a8/supplemental-authority"


def fail(message: str) -> None:
    raise SystemExit(f"A8 SUPPLEMENT: FAIL — {message}")


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
    require(manifest["schema_version"] == "1.1.0", "source manifest schema must be 1.1.0")
    expected_sources = {
        "platform-v0.11.0": "621b498b6d0fa1b99c86a96eac7446f682c715cb576cf0803d233ec2ffe0bdb6",
        "item-v0.12.0": "d12feab1375930e1ef5c121d485aee8622f2abfc34c05f23babb26a293ee47ca",
        "reality-v0.14.0": "928aaacbd84082d88ea9e64fc6c3506a321f26633bce718cfb46199b5364f4d6",
        "adding-conversation-bundle": "a550ed965e4433dc9a3d800ef7aebda4f699c363db8ef8037d104a4a844d6277",
    }
    got_sources = {row["source_id"]: row["sha256"] for row in manifest["sources"]}
    require(got_sources == expected_sources, "source archive hash manifest mismatch")
    require(all(not row["archive_bytes_in_repository"] for row in manifest["sources"]), "binary archive transfer state must remain explicit")
    require("not claimed byte-identical" in manifest["extract_identity_note"], "extract byte-identity limitation must be explicit")

    expected_extract_sources = {
        "source-extracts/platform/IA_INTEGRATION_HANDOFF.md": "41e012c8105e864a4e6cb04bebd51a4c2530eb56ad25a7cb0f79c1fdcc618cce",
        "source-extracts/platform/IA_FUTURE_DATA_MODEL_MANIFEST.csv": "c6f3b18c9997e9a07462d7fa871c9a4dd0278d081c495b89973cc840456b86db",
        "source-extracts/platform/IA_MIGRATION_SEQUENCE.csv": "2f9369ca5b23ac0ff742f2bf6e9880190067dd49af8c5c7a1193d532cd920a80",
        "source-extracts/item/IA_ITEM_INTEGRATION_HANDOFF.md": "914a6feb992eda7c6aa4e1830c446a2d4f1799302cf746b6dc43b6e48da779b0",
        "source-extracts/item/A8_ITEM_PRODUCT_BOUNDARY_MATRIX.csv": "be01ff37eb7cc6384596e93652010a819bae89c82b3047246cfc47a66bc7220c",
        "source-extracts/item/IA_ITEM_MIGRATION_SEQUENCE.csv": "9b5108c492ae44f67ac67cdbdca3df93983ce081b1109400a06e7bd4f3311d13",
        "source-extracts/item/INTRINSIC_AFFINITY_COMPATIBILITY_SYSTEM.md": "3c6c8b3092327094fd4a2e1e89615c6bfbc9a93c9f85f49cef6988d13e99b150",
        "source-extracts/reality/IA_REALITY_INTEGRATION_HANDOFF.md": "510b6d518137b77c114bed61b682848433349a3da967b8f569b195239891fd10",
        "source-extracts/reality/IA_REALITY_PREPARATION_LAYER_MAP.csv": "26233c6bdafd65db1bea09d30251b4b6358947fca94420357e1b0aa333964afa",
        "source-extracts/reality/IA_REALITY_CROSS_DOMAIN_HANDOFF_MATRIX.csv": "7f2557a55d107fc268227b9b3ea524e7c96c8bc4feba2f3ad32ea7f7f3a85b9e",
    }
    got_extracts = {row["path"]: row["source_file_sha256"] for row in manifest["extracted_contracts"]}
    require(got_extracts == expected_extract_sources, "source-file provenance hash map mismatch")
    for entry in manifest["extracted_contracts"]:
        path = BASE / entry["path"]
        require(path.is_file(), f"missing extracted contract {entry['path']}")
        require(path.stat().st_size > 100, f"extracted contract unexpectedly small: {entry['path']}")
        require(entry["repository_byte_identity_claimed"] is False, f"repository extract must not claim exact byte identity: {entry['path']}")

    # Semantic checks keep normalized repository projections tied to the source contracts
    # without misrepresenting newline/CSV normalization as byte identity.
    platform_handoff = (BASE / "source-extracts/platform/IA_INTEGRATION_HANDOFF.md").read_text(encoding="utf-8")
    for phrase in ["5,628", "2,984", "326", "legacy mechanics are non-authoritative", "expand → project → validate → review → enable", "H1v3 Model S Space Station"]:
        require(phrase in platform_handoff, f"platform extract missing invariant: {phrase}")

    item_handoff = (BASE / "source-extracts/item/IA_ITEM_INTEGRATION_HANDOFF.md").read_text(encoding="utf-8")
    for phrase in ["5,389", "171", "241", "54", "A8 remains sole authority for item instances", "not quotas"]:
        require(phrase in item_handoff, f"item extract missing invariant: {phrase}")

    compatibility = (BASE / "source-extracts/item/INTRINSIC_AFFINITY_COMPATIBILITY_SYSTEM.md").read_text(encoding="utf-8")
    for phrase in ["Intrinsic classification", "Affinity", "Compatibility", "Existence compatibility", "Operational compatibility", "Rules compatibility", "Contextual fit", "unknown"]:
        require(phrase in compatibility, f"compatibility extract missing invariant: {phrase}")

    reality_handoff = (BASE / "source-extracts/reality/IA_REALITY_INTEGRATION_HANDOFF.md").read_text(encoding="utf-8")
    for phrase in ["PPIA-12 remains", "PPIA-08 remains", "F020 remains", "F021 remains", "246", "175", "public community", "hard-off"]:
        require(phrase in reality_handoff, f"Reality extract missing boundary: {phrase}")

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
