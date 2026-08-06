#!/usr/bin/env python3
"""Validate the MV-IA-F012 Encounter Builder and Balance Lab design package."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKETS = ROOT / "feature-packets"
PACKET = PACKETS / "MV-IA-F012_ENCOUNTER_BUILDER_AND_BALANCE_LAB.md"
MATRIX = PACKETS / "MV-IA-F012_ENCOUNTER_BALANCE_MATRIX.json"
TRACE = PACKETS / "MV-IA-F012_IMPLEMENTATION_TRACEABILITY.json"
REVIEW = PACKETS / "MV-IA-F012_REVIEW_RECEIPT.md"
READINESS = PACKETS / "MV-IA-F012_READINESS_RECORD.md"
COMPLETION = PACKETS / "MV-IA-F012_COMPLETION_RECORD.json"
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

    require(packet_text.startswith("# MV-IA-F012 — Encounter Builder and Balance Lab"), "Packet title mismatch", errors)
    require("**Design status:** implementation-ready" in packet_text, "Packet is not implementation-ready", errors)
    require("IA-D02-006" in packet_text and "MV-IA-F004" in packet_text and "MV-IA-F005" in packet_text,
            "Packet does not consume shared-foundation, Character, and Campaign/Scene contracts", errors)
    require("guaranteed-balance" in packet_text.lower(), "Packet lacks explicit guaranteed-balance prohibition", errors)
    require("source-grounded warnings" in packet_text.lower(), "Packet lacks source-grounded warning contract", errors)
    require("uncertainty" in packet_text.lower(), "Packet lacks uncertainty contract", errors)
    require("deterministic bounded simulation" in packet_text.lower(), "Packet lacks deterministic bounded simulation contract", errors)
    require("IA-D03-004" in packet_text, "Packet does not identify IA-D03-004 next action", errors)

    for section in range(1, 25):
        require(f"## {section}." in packet_text, f"Packet missing section {section}", errors)

    criterion_ids = [f"EBL-AC-{index:03d}" for index in range(1, 21)]
    for criterion_id in criterion_ids:
        require(criterion_id in packet_text, f"Packet missing {criterion_id}", errors)

    require(matrix.get("featureId") == "MV-IA-F012", "Matrix featureId mismatch", errors)
    require(matrix.get("workItemId") == "IA-D03-003", "Matrix workItemId mismatch", errors)
    require(matrix.get("status") == "implementation-ready-design", "Matrix status mismatch", errors)
    require(len(matrix.get("requiredSharedContracts", [])) == 24, "Matrix must consume 24 shared contracts", errors)
    require(len(matrix.get("aggregateTypes", [])) >= 12, "Matrix aggregate coverage is incomplete", errors)
    require(len(matrix.get("fieldClasses", [])) >= 14, "Matrix field-class coverage is incomplete", errors)
    require(len(matrix.get("pressureDimensions", [])) >= 12, "Matrix pressure-dimension coverage is incomplete", errors)
    require(len(matrix.get("uncertaintyClasses", [])) >= 8, "Matrix uncertainty coverage is incomplete", errors)
    require(len(matrix.get("warningClasses", [])) >= 20, "Matrix warning coverage is incomplete", errors)
    require(len(matrix.get("validationClasses", [])) >= 32, "Matrix validation coverage is incomplete", errors)
    require(len(matrix.get("operationTypes", [])) >= 33, "Matrix operation coverage is incomplete", errors)
    require(len(matrix.get("eventTypes", [])) >= 32, "Matrix Event coverage is incomplete", errors)
    require(len(matrix.get("deniedCases", [])) >= 48, "Matrix denied-case coverage is incomplete", errors)
    require(len(matrix.get("fixtures", [])) >= 10, "Matrix fixture coverage is incomplete", errors)
    require(len(matrix.get("acceptanceCriteria", [])) == 20, "Matrix must contain 20 acceptance criteria", errors)
    require(all(item.get("blocking") is True for item in matrix.get("acceptanceCriteria", [])),
            "All acceptance criteria must be blocking", errors)
    require(matrix.get("blockingFindings") == [], "Matrix contains blocking findings", errors)

    matrix_criteria = {item.get("criterionId") for item in matrix.get("acceptanceCriteria", [])}
    require(matrix_criteria == set(criterion_ids), "Matrix acceptance-criterion IDs are incomplete", errors)

    forbidden_claim_fragments = [
        '"balanced": true', '"fair": true', '"safe": true', '"winnable": true',
        "certifies balance", "guarantees victory", "guarantees survival"
    ]
    lower_packet = packet_text.lower()
    serialized_matrix = json.dumps(matrix).lower()
    for fragment in forbidden_claim_fragments:
        require(fragment not in lower_packet and fragment not in serialized_matrix,
                f"Forbidden guarantee claim found: {fragment}", errors)

    require(trace.get("featureId") == "MV-IA-F012", "Traceability featureId mismatch", errors)
    traced = {item.get("criterionId") for item in trace.get("acceptanceTraceability", [])}
    require(traced == set(criterion_ids), "Traceability does not cover all acceptance criteria", errors)
    require(len(trace.get("implementationSlices", [])) >= 10, "Implementation decomposition is incomplete", errors)

    require(completion.get("workItemId") == "IA-D03-003", "Completion work item mismatch", errors)
    require(completion.get("featureId") == "MV-IA-F012", "Completion featureId mismatch", errors)
    require(completion.get("status") == "complete-design-implementation-ready", "Completion status mismatch", errors)
    metrics = completion.get("metrics", {})
    require(metrics.get("acceptanceCriteria") == 20, "Completion acceptance metric mismatch", errors)
    require(metrics.get("pressureDimensions", 0) >= 12, "Completion pressure metric mismatch", errors)
    require(metrics.get("blockingFindings") == 0, "Completion reports blocking findings", errors)

    features = {item.get("featureId"): item for item in registry.get("features", [])}
    f012 = features.get("MV-IA-F012", {})
    require(registry.get("version") == "0.10.0", "Registry version must be 0.10.0", errors)
    require(f012.get("designStatus") == "implementation-ready", "Registry does not mark F012 implementation-ready", errors)
    require(f012.get("packetPath") == "feature-packets/MV-IA-F012_ENCOUNTER_BUILDER_AND_BALANCE_LAB.md",
            "Registry packet path mismatch", errors)
    companions = set(f012.get("companionFiles", []))
    require("feature-packets/MV-IA-F012_ENCOUNTER_BALANCE_MATRIX.json" in companions,
            "Registry missing F012 matrix companion", errors)
    require("feature-packets/MV-IA-F012_IMPLEMENTATION_TRACEABILITY.json" in companions,
            "Registry missing F012 traceability companion", errors)

    for text_name, text in [("review", review_text), ("readiness", readiness_text)]:
        require("implementation-ready" in text.lower(), f"{text_name} record lacks readiness decision", errors)
        require("IA-D03-004" in text, f"{text_name} record lacks next action", errors)
        require("guaranteed" in text.lower(), f"{text_name} record lacks guarantee boundary", errors)

    require("IA-D03-003 — MV-IA-F012 Encounter Builder and Balance Lab packet — complete" in backlog_text,
            "Backlog does not mark IA-D03-003 complete", errors)
    require("IA-D03-004 — alpha content and fixture specification — next" in backlog_text,
            "Backlog does not advance to IA-D03-004", errors)
    require("**IA-D03-004 — Define the internal-alpha content and deterministic fixture specification.**" in backlog_text,
            "Backlog current-next statement mismatch", errors)
    require("**Version:** 0.10.0" in backlog_text, "Backlog version must be 0.10.0", errors)

    require("## IA-D03-003 — Encounter Builder and Balance Lab" in program_text,
            "Program README lacks IA-D03-003 result", errors)
    require("**IA-D03-004 — Define the internal-alpha content and deterministic fixture specification.**" in program_text,
            "Program README next action mismatch", errors)
    require("**Version:** 0.10.0" in program_text, "Program README version must be 0.10.0", errors)

    require("| MV-IA-F012 | Encounter Builder and Balance Lab |" in packet_index_text,
            "Packet index lacks F012", errors)
    require("`MV-IA-F012_ENCOUNTER_BALANCE_MATRIX.json`" in packet_index_text,
            "Packet index lacks F012 matrix", errors)
    require("IA-D03-004" in packet_index_text, "Packet index does not advance next item", errors)

    if errors:
        print("MV-IA-F012 ENCOUNTER BUILDER/BALANCE LAB DESIGN VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("MV-IA-F012 ENCOUNTER BUILDER/BALANCE LAB DESIGN VALIDATION: PASS")
    print(f"Acceptance criteria: {len(criterion_ids)}")
    print(f"Shared contracts: {len(matrix['requiredSharedContracts'])}")
    print(f"Pressure dimensions: {len(matrix['pressureDimensions'])}")
    print(f"Uncertainty classes: {len(matrix['uncertaintyClasses'])}")
    print(f"Validation classes: {len(matrix['validationClasses'])}")
    print(f"Operation types: {len(matrix['operationTypes'])}")
    print(f"Event types: {len(matrix['eventTypes'])}")
    print(f"Denied cases: {len(matrix['deniedCases'])}")
    print(f"Fixtures: {len(matrix['fixtures'])}")
    print("Blocking findings: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
