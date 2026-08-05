#!/usr/bin/env python3
"""Integrate the completed MV-IA-F005 design package into MV-IA-001 indexes."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKETS = ROOT / "feature-packets"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"ASSEMBLY FAIL: expected exactly one {label}; found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    registry_path = ROOT / "INTERNAL_ALPHA_FEATURE_REGISTRY.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    registry["version"] = "0.9.0"
    feature = next((item for item in registry["features"] if item.get("featureId") == "MV-IA-F005"), None)
    if not feature:
        raise SystemExit("ASSEMBLY FAIL: MV-IA-F005 registry entry missing")
    feature.update(
        {
            "designStatus": "implementation-ready",
            "packetPath": "feature-packets/MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md",
            "packetVersion": "0.1.0",
            "companionFiles": [
                "feature-packets/MV-IA-F005_CAMPAIGN_SCENE_SESSION_MATRIX.json",
                "feature-packets/MV-IA-F005_IMPLEMENTATION_TRACEABILITY.json",
            ],
            "implementationBoundary": (
                "Design complete; application implementation remains dependency-gated by the active "
                "P9-06 sequence, IA-D02-006 conformance, MV-IA-F004 Character contracts, and concrete "
                "Campaign, Scene, Session, entitlement, pack, persistence, migration, backup, restore, "
                "provider-exit, realtime, and downstream action-resolution foundations."
            ),
        }
    )
    registry_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")

    backlog_path = ROOT / "INTERNAL_ALPHA_DESIGN_BACKLOG.md"
    backlog = backlog_path.read_text(encoding="utf-8")
    backlog = replace_once(backlog, "**Version:** 0.8.0", "**Version:** 0.9.0", "backlog version")
    backlog = replace_once(
        backlog,
        "2. **IA-D03-002 — MV-IA-F005 Campaign, Scene, and Session Builder packet — next**\n3. IA-D03-003 — MV-IA-F012 Encounter Builder and Balance Lab packet",
        "2. **IA-D03-002 — MV-IA-F005 Campaign, Scene, and Session Builder packet — complete**\n"
        "   - packet: `feature-packets/MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md`\n"
        "   - matrix: `feature-packets/MV-IA-F005_CAMPAIGN_SCENE_SESSION_MATRIX.json`\n"
        "   - traceability: `feature-packets/MV-IA-F005_IMPLEMENTATION_TRACEABILITY.json`\n"
        "   - completion: `feature-packets/MV-IA-F005_COMPLETION_RECORD.json`\n"
        "   - status: implementation-ready design; implementation not started and dependency-gated\n"
        "   - validation: twenty blocking acceptance criteria, twenty-four shared contracts, at least twenty-four validation classes, thirty-one operation types, thirty-one Event types, forty-two denied cases, and zero blocking findings\n"
        "3. **IA-D03-003 — MV-IA-F012 Encounter Builder and Balance Lab packet — next**",
        "IA-D03-002 backlog row",
    )
    completion_section = """## IA-D03-002 completion record

MV-IA-F005 now defines:

- Campaign identity, rules-profile binding, schema identity, entitlement policy, and immutable pack-lock state;
- invitation, membership, active-role, Character-control, observer, and Assistant-GM delegation boundaries;
- Scene drafts, Campaign-local placements, explicit field visibility, accessible map alternatives, and server-generated Player previews;
- authoritative validation of stable-ID references, permissions, entitlements, dependencies, Character eligibility, and launch readiness;
- immutable launch snapshots that separate mutable preparation from active Session state;
- Session launch, entry, pause, resume, close, Event history, current projection, and reconnect behavior;
- idempotency, expected versions, ambiguous-failure lookup, conflict preservation, revocation, and no offline authoritative mutation;
- realtime as advisory and durable ordered Events plus server projections as authoritative;
- role-safe export, diagnostics, optional AI proposals, accessibility, responsive behavior, and zero-paid-service operation;
- twenty blocking acceptance criteria and deterministic Campaign, Scene, invitation, launch, visibility, and recovery fixtures.

The packet is implementation-ready as a design artifact. Application implementation remains dependency-gated by the active P9-06 sequence and does not authorize paid services, production credentials, real-user data collection, internal-alpha release, production, or public release.

"""
    if "## IA-D03-002 completion record" not in backlog:
        backlog = replace_once(backlog, "## Current next design item\n", completion_section + "## Current next design item\n", "backlog next heading")
    backlog = replace_once(
        backlog,
        "**IA-D03-002 — Design MV-IA-F005, Campaign, Scene, and Session Builder.**\n\nF005 is next because it consumes the completed Character and shared-foundation contracts to define GM preparation, Campaign policy, Scene composition, hidden information, participant invitations, and Session launch.",
        "**IA-D03-003 — Design MV-IA-F012, Encounter Builder and Balance Lab.**\n\nF012 is next because it consumes the completed Campaign, Scene, Session, Character, object, permission, recovery, and pack contracts to define bounded encounter composition, dependency validation, pressure estimates, uncertainty, and source-grounded warnings without guaranteed-balance claims.",
        "backlog current-next block",
    )
    backlog_path.write_text(backlog, encoding="utf-8")

    program_path = ROOT / "README.md"
    program = program_path.read_text(encoding="utf-8")
    program = replace_once(program, "**Version:** 0.8.0", "**Version:** 0.9.0", "program version")
    campaign_section = """## IA-D03-002 — Campaign, Scene, and Session Builder

Complete at design level with:

- Campaign rules-profile, schema, entitlement-policy, and pack-lock binding;
- explicit invitations, membership, role, Character-control, observer, and Assistant-GM delegation;
- Scene drafts, stable-ID object placement, Campaign-local overrides, role-scoped notes, and accessible map alternatives;
- server-generated Player and observer previews with hidden-information and inference protection;
- authoritative dependency, entitlement, permission, Character-eligibility, and launch-readiness validation;
- immutable launch snapshots and separate live Session state;
- launch, entry, pause, resume, close, Event recovery, conflict, revocation, export, and diagnostics contracts;
- realtime-advisory, server-authoritative, provider-neutral, zero-paid-service, and bounded-offline boundaries;
- twenty blocking acceptance criteria and a machine-readable Campaign/Scene/Session matrix.

Application implementation remains dependency-gated.

"""
    if "## IA-D03-002 — Campaign, Scene, and Session Builder" not in program:
        program = replace_once(program, "## File map\n", campaign_section + "## File map\n", "program file-map heading")
    program = replace_once(
        program,
        "- implementation-ready F002, F020, F003, F021, F025, and F004 packets and companion artifacts",
        "- implementation-ready F002, F020, F003, F021, F025, F004, and F005 packets and companion artifacts",
        "program packet list",
    )
    program = replace_once(
        program,
        "- `validate_shared_foundations_integration.py`\n- `.github/workflows/internal-alpha-design-validation.yml`",
        "- `validate_shared_foundations_integration.py`\n- `validate_character_creation_design.py`\n- `validate_campaign_scene_session_design.py`\n- `.github/workflows/internal-alpha-design-validation.yml`\n- `.github/workflows/campaign-scene-session-design-validation.yml`",
        "program validation list",
    )
    program = replace_once(
        program,
        "**IA-D03-002 — Design MV-IA-F005, Campaign, Scene, and Session Builder.**\n\nF005 must consume IA-D02-006 and MV-IA-F004 rather than redefining identity, Character control, stable-ID selection, authorization, persistence, recovery, diagnostics, accessibility, or provider boundaries.",
        "**IA-D03-003 — Design MV-IA-F012, Encounter Builder and Balance Lab.**\n\nF012 must consume IA-D02-006, MV-IA-F004, and MV-IA-F005 rather than redefining identity, Character control, stable-ID selection, Campaign policy, Scene placements, launch snapshots, authorization, persistence, recovery, diagnostics, accessibility, or provider boundaries.",
        "program current-next block",
    )
    program_path.write_text(program, encoding="utf-8")

    index_path = PACKETS / "README.md"
    index = index_path.read_text(encoding="utf-8")
    f004_row = "| MV-IA-F004 | Character Creation and Advancement | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md` | `MV-IA-F004_CHARACTER_CREATION_MATRIX.json` |"
    f005_row = "| MV-IA-F005 | Campaign, Scene, and Session Builder | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md` | `MV-IA-F005_CAMPAIGN_SCENE_SESSION_MATRIX.json`; `MV-IA-F005_IMPLEMENTATION_TRACEABILITY.json`; `MV-IA-F005_REVIEW_RECEIPT.md`; `MV-IA-F005_READINESS_RECORD.md`; `MV-IA-F005_COMPLETION_RECORD.json` |"
    if f005_row not in index:
        index = replace_once(index, f004_row, f004_row + "\n" + f005_row, "packet-index F004 row")
    campaign_result = """## Completed Campaign preparation result

MV-IA-F005 establishes:

- Campaign rules, packs, policy, membership, invitation, role, and Character-control boundaries;
- Scene drafts, stable-ID placements, local overrides, notes, maps, visibility, objectives, and launch configuration;
- server-generated Player and observer previews without protected existence or count leakage;
- immutable launch snapshots and separate authoritative Session state;
- idempotent saves and commands, conflict preservation, Event-gap recovery, revocation, and bounded offline behavior;
- realtime as advisory and durable Events plus current server projections as authority;
- role-safe exports and diagnostics, accessible and responsive preparation, and zero-paid-service operation;
- twenty acceptance criteria and deterministic fixtures.

"""
    if "## Completed Campaign preparation result" not in index:
        index = replace_once(index, "## Next item\n", campaign_result + "## Next item\n", "packet-index next heading")
    index = replace_once(
        index,
        "`MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md` under IA-D03-002.",
        "`MV-IA-F012_ENCOUNTER_BUILDER_AND_BALANCE_LAB.md` under IA-D03-003.",
        "packet-index next item",
    )
    index_path.write_text(index, encoding="utf-8")

    print("IA-D03-002 ASSEMBLY: PASS")


if __name__ == "__main__":
    main()
