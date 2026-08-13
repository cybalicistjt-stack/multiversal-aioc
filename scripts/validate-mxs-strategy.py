#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/multiversal-experience-superset"

REQUIRED = [
    BASE / "MXS_MULTIVERSAL_EXPERIENCE_SUPERSET_STRATEGY_PROGRAM.md",
    BASE / "MXS-02_03_PLAYSTYLE_AND_PLAY_PRIMITIVE_ATLAS_v0.1.0.md",
    BASE / "MXS-04_08_HUMAN_EXPERIENCE_GM_SOCIAL_LEARNING_AND_MEANINGFUL_PROGRESS_v0.1.0.md",
    BASE / "MXS-09_11_CREATOR_SPATIAL_AND_SIGNATURE_EXPERIENCE_ARCHITECTURE_v0.1.0.md",
    BASE / "MXS-12_PRODUCT_SUPERSET_STAGE_A_RECONCILIATION_v0.1.0.md",
    BASE / "MXS_PROGRAM_STATE_v0.1.0.json",
    ROOT / "governance/application-planning/STAGE_A_PREIMPLEMENTATION_RECOVERY_MATRIX_2026-08-13.md",
    ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md",
    ROOT / "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md",
    ROOT / "governance/ai/runtime/ROADMAP_INDEX.json",
]


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    failures: list[str] = []
    for path in REQUIRED:
        require(path.is_file(), f"missing required artifact: {path.relative_to(ROOT)}", failures)
    if failures:
        for failure in failures:
            print(f"MXS VALIDATION: FAIL — {failure}")
        return 1

    state = json.loads(text(BASE / "MXS_PROGRAM_STATE_v0.1.0.json"))
    roadmap_index = json.loads(text(ROOT / "governance/ai/runtime/ROADMAP_INDEX.json"))
    program = text(BASE / "MXS_MULTIVERSAL_EXPERIENCE_SUPERSET_STRATEGY_PROGRAM.md")
    atlas = text(BASE / "MXS-02_03_PLAYSTYLE_AND_PLAY_PRIMITIVE_ATLAS_v0.1.0.md")
    human = text(BASE / "MXS-04_08_HUMAN_EXPERIENCE_GM_SOCIAL_LEARNING_AND_MEANINGFUL_PROGRESS_v0.1.0.md")
    creator = text(BASE / "MXS-09_11_CREATOR_SPATIAL_AND_SIGNATURE_EXPERIENCE_ARCHITECTURE_v0.1.0.md")
    reconcile = text(BASE / "MXS-12_PRODUCT_SUPERSET_STAGE_A_RECONCILIATION_v0.1.0.md")
    recovery = text(ROOT / "governance/application-planning/STAGE_A_PREIMPLEMENTATION_RECOVERY_MATRIX_2026-08-13.md")
    roadmap = text(ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md")
    bootstrap = text(ROOT / "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md")

    expected_items = [f"MXS-{n:02d}" for n in range(1, 13)]
    actual_items = [item.get("id") for item in state.get("work_items", [])]
    require(actual_items == expected_items, f"work item sequence mismatch: {actual_items}", failures)

    expected_contracts = [f"MXC-{n:02d}" for n in range(1, 15)]
    actual_contracts = [item.get("id") for item in state.get("cross_cutting_contracts", [])]
    require(actual_contracts == expected_contracts, f"cross-cutting contract sequence mismatch: {actual_contracts}", failures)
    require(state.get("current_application_item") == "STAGE-A-A2", "current application item is not STAGE-A-A2", failures)
    require(state.get("current_application_item_changed") is False, "MXS claims it changed the application item", failures)
    require(state.get("implementation_authority_changed") is False, "MXS claims new implementation authority", failures)

    for token in ("Parity Gate", "Integration Gate", "Multiversal Gate", "build-first", "Play Experience Profile"):
        require(token.lower() in program.lower(), f"program missing concept: {token}", failures)

    play_families = [
        "Tactical / positional",
        "Fiction-first / narrative",
        "Investigation / mystery",
        "Heist / caper",
        "Horror / psychological",
        "Survival / scarcity",
        "Social / relationship",
        "Domain / faction",
        "Crafting / research",
        "Vehicle / mecha",
        "Exploration / discovery",
        "Lifepath / career",
        "Solo / co-op / GMless",
        "Rules-light / rulings-oriented",
        "Theater-of-the-mind / cinematic",
    ]
    for family in play_families:
        require(family in atlas, f"playstyle atlas missing family: {family}", failures)

    for token in ("Autonomy", "Competence", "Relatedness", "Contextual GM Cockpit", "Playstyle Compass", "World Pulse", "Progressive Complexity"):
        require(token in human, f"human experience architecture missing: {token}", failures)

    for token in ("Level C0", "Level C5", "S0 — Nonspatial", "S6 — Advanced/3D", "World Pulse", "Why Engine", "Living World Fabric", "Governed AI over Structured Truth"):
        require(token in creator, f"creator/spatial/signature architecture missing: {token}", failures)

    for stage in range(2, 13):
        token = f"STAGE-A-A{stage}"
        require(token in reconcile, f"MXS-12 missing stage reconciliation: {token}", failures)
        require(f"| A{stage} |" in recovery or token in recovery, f"recovery matrix missing A{stage}", failures)

    require("**Version:** 2.8.0" in roadmap, "roadmap version is not 2.8.0", failures)
    require("PPIA AND CAPP COMPLETED_VERIFIED" in roadmap, "roadmap does not project PPIA/CAPP completion", failures)
    require("## MXS — Multiversal Experience Superset Strategy" in roadmap, "roadmap missing MXS section", failures)
    require("STAGE-A-A2 remains the authorized current application item" in roadmap, "roadmap does not preserve A2 current authority", failures)
    for n in range(1, 13):
        require(f"CAPP-{n:02d}" in roadmap and "COMPLETED_VERIFIED" in roadmap, f"roadmap missing CAPP-{n:02d} closure projection", failures)

    require("**Version:** 5.6.0" in bootstrap, "bootstrap version is not 5.6.0", failures)
    require("## MXS strategic authority rule" in bootstrap, "bootstrap missing MXS strategic authority rule", failures)
    require("build first, integrate second" in bootstrap, "bootstrap missing owner-approved tranche execution rule", failures)
    require("CAPP — Character Appearance Production Preparation is completed_verified" in bootstrap, "bootstrap still treats CAPP as active", failures)

    entries = roadmap_index.get("entries", [])
    require(sum(1 for e in entries if e.get("work_item_id") == "MXS") == 1, "ROADMAP_INDEX must contain exactly one MXS entry", failures)
    require(sum(1 for e in entries if e.get("work_item_id") == "STAGE-A-A2") == 1, "ROADMAP_INDEX must contain exactly one STAGE-A-A2 entry", failures)

    forbidden_claims = [
        "MXS activates STAGE-A-A2",
        "MXS authorizes release",
        "MXS authorizes deployment",
        "MXS authorizes marketplace launch",
        "MXS authorizes autonomous AI",
    ]
    joined = "\n".join((program, atlas, human, creator, reconcile, roadmap, bootstrap))
    for claim in forbidden_claims:
        require(claim not in joined, f"forbidden authority claim found: {claim}", failures)

    if failures:
        for failure in failures:
            print(f"MXS VALIDATION: FAIL — {failure}")
        print(f"MXS VALIDATION: FAIL count={len(failures)}")
        return 1

    print(
        "MXS VALIDATION: PASS "
        f"work_items={len(actual_items)} contracts={len(actual_contracts)} "
        f"signatures={len(state.get('signature_experiences', []))} "
        f"spatial_levels={len(state.get('spatial_maturity', []))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
