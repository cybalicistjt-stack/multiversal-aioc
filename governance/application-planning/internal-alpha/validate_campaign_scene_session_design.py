#!/usr/bin/env python3
"""Validate the MV-IA-F005 Campaign, Scene, and Session Builder design package."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKETS = ROOT / "feature-packets"
PACKET = PACKETS / "MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md"
MATRIX = PACKETS / "MV-IA-F005_CAMPAIGN_SCENE_SESSION_MATRIX.json"
TRACE = PACKETS / "MV-IA-F005_IMPLEMENTATION_TRACEABILITY.json"
REVIEW = PACKETS / "MV-IA-F005_REVIEW_RECEIPT.md"
READINESS = PACKETS / "MV-IA-F005_READINESS_RECORD.md"
COMPLETION = PACKETS / "MV-IA-F005_COMPLETION_RECORD.json"
REGISTRY = ROOT / "INTERNAL_ALPHA_FEATURE_REGISTRY.json"
BACKLOG = ROOT / "INTERNAL_ALPHA_DESIGN_BACKLOG.md"
PROGRAM = ROOT / "README.md"
PACKET_INDEX = PACKETS / "README.md"


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Cannot parse {path.relative_to(ROOT)}: {exc}")
        return {}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    required = [PACKET, MATRIX, TRACE, REVIEW, READINESS, COMPLETION, REGISTRY, BACKLOG, PROGRAM, PACKET_INDEX]
    for path in required:
        require(path.exists(), f"Missing required file: {path.relative_to(ROOT)}", errors)

    if errors:
        for error in errors:
            print(f"- {error}")
        return 1

    packet_text = PACKET.read_text(encoding="utf-8")
    review_text = REVIEW.read_text(encoding="utf-8")
    readiness_text = READINESS.read_text(encoding="utf-8")
    backlog_text = BACKLOG.read_text(encoding="utf-8")
    program_text = PROGRAM.read_text(encoding="utf-8")
    packet_index_text = PACKET_INDEX.read_text(encoding="utf-8")

    matrix = load_json(MATRIX, errors)
    trace = load_json(TRACE, errors)
    completion = load_json(COMPLETION, errors)
    registry = load_json(REGISTRY, errors)

    require(packet_text.startswith("# MV-IA-F005 — Campaign, Scene, and Session Builder"), "Packet title mismatch", errors)
    require("**Design status:** implementation-ready" in packet_text, "Packet is not implementation-ready", errors)
    require("IA-D02-006" in packet_text and "MV-IA-F004" in packet_text, "Packet does not consume shared-foundation and Character contracts", errors)
    require("immutable launch snapshot" in packet_text.lower(), "Packet lacks immutable launch-snapshot rule", errors)
    require("realtime" in packet_text.lower() and "advisory" in packet_text.lower(), "Packet lacks realtime advisory rule", errors)
    require("no offline authoritative" in packet_text.lower() or "offline authoritative" in packet_text.lower(), "Packet lacks offline authority boundary", errors)
    require("IA-D03-003" in packet_text, "Packet does not identify IA-D03-003 next action", errors)

    for section in range(1, 25):
        require(f"## {section}." in packet_text, f"Packet missing section {section}", errors)

    criterion_ids = [f"CSS-AC-{index:03d}" for index in range(1, 21)]
    for criterion_id in criterion_ids:
        require(criterion_id in packet_text, f"Packet missing {criterion_id}", errors)

    require(matrix.get("featureId") == "MV-IA-F005", "Matrix featureId mismatch", errors)
    require(matrix.get("status") == "implementation-ready-design", "Matrix status mismatch", errors)
    require(len(matrix.get("requiredSharedContracts", [])) == 24, "Matrix must consume 24 shared contracts", errors)
    require(len(matrix.get("aggregateTypes", [])) >= 9, "Matrix aggregate type coverage is incomplete", errors)
    require(len(matrix.get("fieldClasses", [])) >= 10, "Matrix field-class coverage is incomplete", errors)
    require(len(matrix.get("validationClasses", [])) >= 24, "Matrix validation-class coverage is incomplete", errors)
    require(len(matrix.get("operationTypes", [])) >= 31, "Matrix operation coverage is incomplete", errors)
    require(len(matrix.get("eventTypes", [])) >= 31, "Matrix Event coverage is incomplete", errors)
    require(len(matrix.get("deniedCases", [])) >= 42, "Matrix denied-case coverage is incomplete", errors)
    require(len(matrix.get("acceptanceCriteria", [])) == 20, "Matrix must contain 20 acceptance criteria", errors)
    require(all(item.get("blocking") is True for item in matrix.get("acceptanceCriteria", [])), "All acceptance criteria must be blocking", errors)
    require(matrix.get("blockingFindings") == [], "Matrix contains blocking findings", errors)

    matrix_criteria = {item.get("criterionId") for item in matrix.get("acceptanceCriteria", [])}
    require(matrix_criteria == set(criterion_ids), "Matrix acceptance-criterion IDs are incomplete", errors)

    require(trace.get("featureId") == "MV-IA-F005", "Traceability featureId mismatch", errors)
    traced = {item.get("criterionId") for item in trace.get("acceptanceTraceability", [])}
    require(traced == set(criterion_ids), "Traceability does not cover all acceptance criteria", errors)
    require(len(trace.get("implementationSlices", [])) >= 8, "Implementation decomposition is incomplete", errors)

    require(completion.get("workItemId") == "IA-D03-002", "Completion work item mismatch", errors)
    require(completion.get("featureId") == "MV-IA-F005", "Completion featureId mismatch", errors)
    require(completion.get("status") == "complete-design-implementation-ready", "Completion status mismatch", errors)
    require(completion.get("metrics", {}).get("acceptanceCriteria") == 20, "Completion metric mismatch", errors)
    require(completion.get("metrics", {}).get("blockingFindings") == 0, "Completion reports blocking findings", errors)

    features = {item.get("featureId"): item for item in registry.get("features", [])}
    f005 = features.get("MV-IA-F005", {})
    require(registry.get("version") == "0.9.0", "Registry version must be 0.9.0", errors)
    require(f005.get("designStatus") == "implementation-ready", "Registry does not mark F005 implementation-ready", errors)
    require(f005.get("packetPath") == "feature-packets/MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md", "Registry packet path mismatch", errors)
    companions = set(f005.get("companionFiles", []))
    require("feature-packets/MV-IA-F005_CAMPAIGN_SCENE_SESSION_MATRIX.json" in companions, "Registry missing F005 matrix companion", errors)
    require("feature-packets/MV-IA-F005_IMPLEMENTATION_TRACEABILITY.json" in companions, "Registry missing F005 traceability companion", errors)

    for text_name, text in [("review", review_text), ("readiness", readiness_text)]:
        require("implementation-ready" in text.lower(), f"{text_name} record lacks readiness decision", errors)
        require("IA-D03-003" in text, f"{text_name} record lacks next action", errors)

    require("IA-D03-002 — MV-IA-F005 Campaign, Scene, and Session Builder packet — complete" in backlog_text, "Backlog does not mark IA-D03-002 complete", errors)
    require("IA-D03-003 — MV-IA-F012 Encounter Builder and Balance Lab packet — next" in backlog_text, "Backlog does not advance to IA-D03-003", errors)
    require("**IA-D03-003 — Design MV-IA-F012, Encounter Builder and Balance Lab.**" in backlog_text, "Backlog current-next statement mismatch", errors)
    require("**Version:** 0.9.0" in backlog_text, "Backlog version must be 0.9.0", errors)

    require("## IA-D03-002 — Campaign, Scene, and Session Builder" in program_text, "Program README lacks IA-D03-002 result", errors)
    require("**IA-D03-003 — Design MV-IA-F012, Encounter Builder and Balance Lab.**" in program_text, "Program README next action mismatch", errors)
    require("**Version:** 0.9.0" in program_text, "Program README version must be 0.9.0", errors)

    require("| MV-IA-F005 | Campaign, Scene, and Session Builder |" in packet_index_text, "Packet index lacks F005", errors)
    require("`MV-IA-F005_CAMPAIGN_SCENE_SESSION_MATRIX.json`" in packet_index_text, "Packet index lacks F005 matrix", errors)
    require("IA-D03-003" in packet_index_text, "Packet index does not advance next item", errors)

    forbidden_terms = ["prophecy content", "prophecy feature"]
    for term in forbidden_terms:
        require(term not in packet_text.lower(), f"Packet contains forbidden mistaken term: {term}", errors)

    if errors:
        print("MV-IA-F005 CAMPAIGN/SCENE/SESSION DESIGN VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("MV-IA-F005 CAMPAIGN/SCENE/SESSION DESIGN VALIDATION: PASS")
    print(f"Acceptance criteria: {len(criterion_ids)}")
    print(f"Shared contracts: {len(matrix['requiredSharedContracts'])}")
    print(f"Validation classes: {len(matrix['validationClasses'])}")
    print(f"Operation types: {len(matrix['operationTypes'])}")
    print(f"Event types: {len(matrix['eventTypes'])}")
    print(f"Denied cases: {len(matrix['deniedCases'])}")
    print("Blocking findings: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
