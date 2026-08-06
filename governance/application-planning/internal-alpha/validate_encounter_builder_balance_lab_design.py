#!/usr/bin/env python3
"""Validate the completed MV-IA-F012 design without freezing later milestones."""

from __future__ import annotations

import json
import re
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


def version_tuple(value: str) -> tuple[int, ...]:
    try:
        return tuple(int(part) for part in value.split("."))
    except (AttributeError, ValueError):
        return ()


def document_version(text: str) -> tuple[int, ...]:
    match = re.search(r"\*\*Version:\*\* ([0-9]+(?:\.[0-9]+)+)", text)
    return version_tuple(match.group(1)) if match else ()


def main() -> int:
    errors: list[str] = []
    required = [PACKET, MATRIX, TRACE, REVIEW, READINESS, COMPLETION, REGISTRY, BACKLOG, PROGRAM, PACKET_INDEX]
    for path in required:
        require(path.exists(), f"Missing required file: {path.relative_to(ROOT)}", errors)
    if errors:
        print("\n".join(f"- {e}" for e in errors))
        return 1

    packet = PACKET.read_text(encoding="utf-8")
    review = REVIEW.read_text(encoding="utf-8")
    readiness = READINESS.read_text(encoding="utf-8")
    backlog = BACKLOG.read_text(encoding="utf-8")
    program = PROGRAM.read_text(encoding="utf-8")
    packet_index = PACKET_INDEX.read_text(encoding="utf-8")
    matrix = load_json(MATRIX, errors)
    trace = load_json(TRACE, errors)
    completion = load_json(COMPLETION, errors)
    registry = load_json(REGISTRY, errors)

    require(packet.startswith("# MV-IA-F012 — Encounter Builder and Balance Lab"), "Packet title mismatch", errors)
    require("**Design status:** implementation-ready" in packet, "Packet is not implementation-ready", errors)
    for phrase in ["IA-D02-006", "MV-IA-F004", "MV-IA-F005", "guaranteed-balance", "source-grounded warnings", "uncertainty", "deterministic bounded simulation", "IA-D03-004"]:
        require(phrase.lower() in packet.lower(), f"Packet missing required contract or handoff: {phrase}", errors)
    for section in range(1, 25):
        require(f"## {section}." in packet, f"Packet missing section {section}", errors)

    criteria = [f"EBL-AC-{i:03d}" for i in range(1, 21)]
    for criterion in criteria:
        require(criterion in packet, f"Packet missing {criterion}", errors)

    require(matrix.get("featureId") == "MV-IA-F012", "Matrix featureId mismatch", errors)
    require(matrix.get("workItemId") == "IA-D03-003", "Matrix workItemId mismatch", errors)
    require(matrix.get("status") == "implementation-ready-design", "Matrix status mismatch", errors)
    requirements = {
        "requiredSharedContracts": 24, "aggregateTypes": 12, "fieldClasses": 14,
        "pressureDimensions": 12, "uncertaintyClasses": 8, "warningClasses": 20,
        "validationClasses": 32, "operationTypes": 33, "eventTypes": 32,
        "deniedCases": 48, "fixtures": 10,
    }
    for key, minimum in requirements.items():
        require(len(matrix.get(key, [])) >= minimum, f"Matrix {key} coverage is incomplete", errors)
    require(len(matrix.get("acceptanceCriteria", [])) == 20, "Matrix must contain 20 acceptance criteria", errors)
    require(all(item.get("blocking") is True for item in matrix.get("acceptanceCriteria", [])), "All acceptance criteria must be blocking", errors)
    require({item.get("criterionId") for item in matrix.get("acceptanceCriteria", [])} == set(criteria), "Matrix criterion IDs mismatch", errors)
    require(matrix.get("blockingFindings") == [], "Matrix contains blocking findings", errors)

    serialized = json.dumps(matrix).lower()
    for fragment in ['"balanced": true', '"fair": true', '"safe": true', '"winnable": true', "certifies balance", "guarantees victory", "guarantees survival"]:
        require(fragment not in packet.lower() and fragment not in serialized, f"Forbidden guarantee claim found: {fragment}", errors)

    require(trace.get("featureId") == "MV-IA-F012", "Traceability featureId mismatch", errors)
    require(trace.get("owner") == "John Brandon Turner", "Traceability owner mismatch", errors)
    require({item.get("criterionId") for item in trace.get("acceptanceTraceability", [])} == set(criteria), "Traceability criterion coverage mismatch", errors)
    require(len(trace.get("implementationSlices", [])) >= 10, "Implementation decomposition incomplete", errors)

    require(completion.get("workItemId") == "IA-D03-003", "Completion work item mismatch", errors)
    require(completion.get("featureId") == "MV-IA-F012", "Completion featureId mismatch", errors)
    require(completion.get("status") == "complete-design-implementation-ready", "Completion status mismatch", errors)
    metrics = completion.get("metrics", {})
    require(metrics.get("acceptanceCriteria") == 20 and metrics.get("pressureDimensions", 0) >= 12 and metrics.get("blockingFindings") == 0, "Completion metrics mismatch", errors)

    features = {item.get("featureId"): item for item in registry.get("features", [])}
    f012 = features.get("MV-IA-F012", {})
    require(version_tuple(registry.get("version", "")) >= (0, 10, 0), "Registry version must be at least 0.10.0", errors)
    require(f012.get("designStatus") == "implementation-ready", "Registry does not mark F012 implementation-ready", errors)
    require(f012.get("packetPath") == "feature-packets/MV-IA-F012_ENCOUNTER_BUILDER_AND_BALANCE_LAB.md", "Registry packet path mismatch", errors)
    companions = set(f012.get("companionFiles", []))
    require("feature-packets/MV-IA-F012_ENCOUNTER_BALANCE_MATRIX.json" in companions, "Registry missing F012 matrix", errors)
    require("feature-packets/MV-IA-F012_IMPLEMENTATION_TRACEABILITY.json" in companions, "Registry missing F012 traceability", errors)

    for name, text in [("review", review), ("readiness", readiness)]:
        require("implementation-ready" in text.lower(), f"{name} lacks readiness decision", errors)
        require("IA-D03-004" in text, f"{name} lacks original IA-D03-004 handoff", errors)
        require("guaranteed" in text.lower(), f"{name} lacks guarantee boundary", errors)

    require("IA-D03-003 — MV-IA-F012 Encounter Builder and Balance Lab — complete" in backlog or "IA-D03-003 — MV-IA-F012 Encounter Builder and Balance Lab packet — complete" in backlog, "Backlog does not preserve IA-D03-003 completion", errors)
    require("IA-D03-004" in backlog and "fixture" in backlog.lower(), "Backlog does not preserve IA-D03-004 handoff or result", errors)
    require(document_version(backlog) >= (0, 10, 0), "Backlog version must be at least 0.10.0", errors)

    require("## IA-D03-003 — Encounter Builder and Balance Lab" in program, "Program README lacks IA-D03-003 result", errors)
    require("IA-D03-004" in program and "fixture" in program.lower(), "Program README does not preserve IA-D03-004 handoff or result", errors)
    require(document_version(program) >= (0, 10, 0), "Program README version must be at least 0.10.0", errors)

    require("| MV-IA-F012 | Encounter Builder and Balance Lab |" in packet_index, "Packet index lacks F012", errors)
    require("`MV-IA-F012_ENCOUNTER_BALANCE_MATRIX.json`" in packet_index, "Packet index lacks F012 matrix", errors)
    require("IA-D03-004" in packet_index, "Packet index does not preserve the F012-to-IA-D03-004 handoff", errors)

    if errors:
        print("MV-IA-F012 ENCOUNTER BUILDER/BALANCE LAB DESIGN VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("MV-IA-F012 ENCOUNTER BUILDER/BALANCE LAB DESIGN VALIDATION: PASS")
    print("Acceptance criteria: 20")
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
