#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKETS = ROOT / "feature-packets"
SELF = Path(__file__)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"ASSEMBLY FAIL: expected exactly one {label}; found {count}")
    return text.replace(old, new, 1)


# Ensure the packet records the next design item required by its validator.
packet_path = PACKETS / "MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md"
packet = packet_path.read_text(encoding="utf-8")
next_item = "**Next design item:** IA-D03-002 — Design MV-IA-F005, Campaign, Scene, and Session Builder."
if next_item not in packet:
    packet_path.write_text(packet.rstrip() + "\n\n" + next_item + "\n", encoding="utf-8")

# Mark F004 implementation-ready in the feature registry.
registry_path = ROOT / "INTERNAL_ALPHA_FEATURE_REGISTRY.json"
registry = json.loads(registry_path.read_text(encoding="utf-8"))
registry["version"] = "0.8.0"
feature = next((item for item in registry["features"] if item["featureId"] == "MV-IA-F004"), None)
if feature is None:
    raise SystemExit("ASSEMBLY FAIL: MV-IA-F004 missing from registry")
feature.update(
    {
        "designStatus": "implementation-ready",
        "packetPath": "feature-packets/MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md",
        "packetVersion": "0.1.0",
        "companionFiles": ["feature-packets/MV-IA-F004_CHARACTER_CREATION_MATRIX.json"],
        "implementationBoundary": (
            "Design complete; application implementation remains dependency-gated by "
            "the active P9-06 sequence, IA-D02-006 conformance, and concrete Character, "
            "entitlement, pack, persistence, migration, backup, restore, provider-exit, "
            "and downstream caller-workflow foundations."
        ),
    }
)
registry_path.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Complete IA-D03-001 and advance the backlog.
backlog_path = ROOT / "INTERNAL_ALPHA_DESIGN_BACKLOG.md"
backlog = backlog_path.read_text(encoding="utf-8")
backlog = re.sub(r"\*\*Version:\*\* 0\.7\.0", "**Version:** 0.8.0", backlog, count=1)
backlog = replace_once(
    backlog,
    """1. **IA-D03-001 — MV-IA-F004 Character Creation and Advancement packet — next**
2. IA-D03-002 — MV-IA-F005 Campaign, Scene, and Session Builder packet""",
    """1. **IA-D03-001 — MV-IA-F004 Character Creation and Advancement packet — complete**
   - packet: `feature-packets/MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md`
   - matrix: `feature-packets/MV-IA-F004_CHARACTER_CREATION_MATRIX.json`
   - traceability: `feature-packets/MV-IA-F004_IMPLEMENTATION_TRACEABILITY.json`
   - completion: `feature-packets/MV-IA-F004_COMPLETION_RECORD.json`
   - status: implementation-ready design; implementation not started and dependency-gated
   - validation: twenty blocking acceptance criteria, twelve lifecycle states, eighteen validation classes, sixteen operation types, twenty-six denied cases, and zero blocking findings
2. **IA-D03-002 — MV-IA-F005 Campaign, Scene, and Session Builder packet — next**""",
    "IA-D03 tranche marker",
)
backlog = replace_once(
    backlog,
    """## Current next design item

**IA-D03-001 — Design MV-IA-F004, Character Creation and Advancement.**

F004 is next because Character creation is the first major domain packet that consumes the complete shared-foundation contract baseline.""",
    """## IA-D03-001 completion record

MV-IA-F004 now defines:

- Campaign-, rules-profile-, creation-policy-, advancement-policy-, and pack-lock-bound Character drafts;
- stable-ID species, form, origin, attribute, skill, proficiency, Ability, Action, Effect, Condition, Resource, and initial-equipment selections;
- authoritative prerequisite, exclusivity, budget, grant, entitlement, pack, lifecycle, and compatibility validation;
- source-linked deterministic calculation traces;
- explicit Character-control grants separate from identity, membership, role, ownership, and entitlement;
- role-safe Character, history, export, diagnostic, and AI projections;
- local draft, authoritative save, submission, activation, award, advancement, correction, migration, retirement, archival, and recovery states;
- idempotency, expected versions, status lookup, conflict preservation, Event-gap recovery, and no offline authoritative mutation;
- history-preserving advancement, correction, migration, and historical entitlement behavior;
- responsive and accessible creation and advancement flows;
- twenty blocking acceptance criteria and deterministic fixture requirements.

The packet is implementation-ready as a design artifact. Application implementation remains dependency-gated by the active P9-06 sequence and does not authorize paid services, production credentials, real-user data collection, internal-alpha release, production, or public release.

## Current next design item

**IA-D03-002 — Design MV-IA-F005, Campaign, Scene, and Session Builder.**

F005 is next because it consumes the completed Character and shared-foundation contracts to define GM preparation, Campaign policy, Scene composition, hidden information, participant invitations, and Session launch.""",
    "backlog current-next block",
)
backlog_path.write_text(backlog, encoding="utf-8")

# Update the program index.
readme_path = ROOT / "README.md"
readme = readme_path.read_text(encoding="utf-8")
readme = re.sub(r"\*\*Version:\*\* 0\.7\.0", "**Version:** 0.8.0", readme, count=1)
character_block = """## IA-D03-001 — Character Creation and Advancement

Complete at design level with:

- Campaign-, rules-profile-, policy-, and pack-lock-bound Character drafts;
- stable-ID governed selections and source-linked option inspection;
- authoritative validation and deterministic calculation traces;
- separate Character-control grants;
- role-safe Character, history, export, diagnostic, and optional AI projections;
- local draft, authoritative save, activation, advancement, correction, migration, retirement, archival, reconnect, and recovery contracts;
- history-preserving entitlement, correction, and migration behavior;
- twenty blocking acceptance criteria and a machine-readable Character matrix.

Application implementation remains dependency-gated.

"""
if "## IA-D03-001 — Character Creation and Advancement" not in readme:
    readme = replace_once(readme, "## File map\n", character_block + "## File map\n", "README File map heading")
readme = readme.replace(
    "implementation-ready F002, F020, F003, F021, and F025 packets and companion artifacts",
    "implementation-ready F002, F020, F003, F021, F025, and F004 packets and companion artifacts",
)
readme = replace_once(
    readme,
    """## Current next design action

**IA-D03-001 — Design MV-IA-F004, Character Creation and Advancement.**

The Character packet must consume the IA-D02-006 shared-foundation contract matrix rather than creating private identity, permission, picker, save, recovery, diagnostic, or support behavior.""",
    """## Current next design action

**IA-D03-002 — Design MV-IA-F005, Campaign, Scene, and Session Builder.**

F005 must consume IA-D02-006 and MV-IA-F004 rather than redefining identity, Character control, stable-ID selection, authorization, persistence, recovery, diagnostics, accessibility, or provider boundaries.""",
    "README current-next block",
)
readme_path.write_text(readme, encoding="utf-8")

# Update the packet index.
index_path = PACKETS / "README.md"
index = index_path.read_text(encoding="utf-8")
anchor = "| MV-IA-F025 | Onboarding, Help, Diagnostics, and Issue Reporting | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F025_ONBOARDING_HELP_DIAGNOSTICS_AND_ISSUE_REPORTING.md` | `MV-IA-F025_ONBOARDING_SUPPORT_MATRIX.json` |"
if "| MV-IA-F004 | Character Creation and Advancement |" not in index:
    index = replace_once(
        index,
        anchor,
        anchor + "\n| MV-IA-F004 | Character Creation and Advancement | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md` | `MV-IA-F004_CHARACTER_CREATION_MATRIX.json` |",
        "F025 packet-index row",
    )
character_result = """## Completed Character preparation result

MV-IA-F004 establishes:

- Campaign- and rules-profile-bound Character identity and build state;
- stable-ID governed selection and source-linked calculation;
- explicit controller authority and role-safe projections;
- validation, activation, advancement, correction, migration, retirement, archival, and export contracts;
- idempotency, conflict preservation, reconnect, and bounded offline behavior;
- historical entitlement and append-only history requirements;
- accessible and responsive Character creation and advancement;
- twenty acceptance criteria and deterministic fixtures.

"""
if "## Completed Character preparation result" not in index:
    index = replace_once(index, "## Next item\n", character_result + "## Next item\n", "packet-index Next item heading")
index = replace_once(
    index,
    "`MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md` under IA-D03-001.",
    "`MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md` under IA-D03-002.",
    "packet-index next item",
)
index_path.write_text(index, encoding="utf-8")

# Remove temporary governance scripts only. Workflow cleanup is performed through the governed GitHub connector.
for name in [
    "assemble_ia_d03_001.py",
    "assemble_ia_d03_001_wrapper.py",
    "repair_ia_d03_001.py",
    "assemble_ia_d03_001_no_workflow.py",
]:
    path = ROOT / name
    if path.exists():
        path.unlink()

print("IA-D03-001 NON-WORKFLOW ASSEMBLY: PASS")
