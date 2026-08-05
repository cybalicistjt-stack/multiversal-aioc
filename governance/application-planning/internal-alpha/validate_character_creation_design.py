#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKETS = ROOT / "feature-packets"
PACKET = PACKETS / "MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md"
MATRIX = PACKETS / "MV-IA-F004_CHARACTER_CREATION_MATRIX.json"
TRACE = PACKETS / "MV-IA-F004_IMPLEMENTATION_TRACEABILITY.json"
REVIEW = PACKETS / "MV-IA-F004_REVIEW_RECEIPT.md"
READINESS = PACKETS / "MV-IA-F004_READINESS_RECORD.md"
COMPLETION = PACKETS / "MV-IA-F004_COMPLETION_RECORD.json"
EXPECTED_CRITERIA = [f"CCA-AC-{number:03d}" for number in range(1, 21)]


def load_json(path: Path, errors: list[str]) -> dict:
    if not path.is_file():
        errors.append(f"missing required JSON artifact: {path.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}


def require_text(text: str, phrases: list[str], label: str, errors: list[str]) -> None:
    lower = text.lower()
    for phrase in phrases:
        if phrase.lower() not in lower:
            errors.append(f"{label} missing required phrase {phrase!r}")


def main() -> int:
    errors: list[str] = []

    for path in [PACKET, MATRIX, TRACE, REVIEW, READINESS, COMPLETION]:
        if not path.is_file():
            errors.append(f"missing required Character artifact: {path.relative_to(ROOT)}")

    packet_text = PACKET.read_text(encoding="utf-8") if PACKET.is_file() else ""
    review_text = REVIEW.read_text(encoding="utf-8") if REVIEW.is_file() else ""
    readiness_text = READINESS.read_text(encoding="utf-8") if READINESS.is_file() else ""
    matrix = load_json(MATRIX, errors)
    trace = load_json(TRACE, errors)
    completion = load_json(COMPLETION, errors)

    if not packet_text.startswith("# MV-IA-F004 — Character Creation and Advancement"):
        errors.append("Character packet title is incorrect")
    for exact in [
        "**Feature ID:** MV-IA-F004",
        "**Design status:** implementation-ready",
        "**Owner:** John Brandon Turner",
        "Silence is not approval.",
    ]:
        if exact not in packet_text:
            errors.append(f"Character packet missing exact content {exact!r}")

    sections: list[int] = []
    for line in packet_text.splitlines():
        match = re.match(r"^## (\d+)\. ", line)
        if match:
            sections.append(int(match.group(1)))
    if sections != list(range(1, 25)):
        errors.append(f"Character packet must contain sections 1-24 exactly once and in order; got {sections}")

    require_text(
        packet_text,
        [
            "stable ID",
            "pack-lock digest",
            "selected-context receipt",
            "character control",
            "authoritative validation",
            "calculation trace",
            "advancement ledger",
            "correction or respec",
            "historical entitlement",
            "silent last-write-wins",
            "status-unknown",
            "no offline authoritative mutation",
            "diagnostic generation defaults to exclude",
            "zero AI",
            "zero paid services",
            "implementation remains dependency-gated",
            "IA-D02-006",
            "IA-D03-002",
        ],
        "Character packet",
        errors,
    )

    for criterion in EXPECTED_CRITERIA:
        if criterion not in packet_text:
            errors.append(f"Character packet missing acceptance criterion {criterion}")

    if matrix.get("programId") != "MV-IA-001":
        errors.append("Character matrix has incorrect programId")
    if matrix.get("featureId") != "MV-IA-F004":
        errors.append("Character matrix has incorrect featureId")
    if matrix.get("owner") != "John Brandon Turner":
        errors.append("Character matrix has incorrect owner")
    if matrix.get("defaultCharacterDecision") != "deny":
        errors.append("Character matrix defaultCharacterDecision must be deny")
    if "nonauthoritative" not in matrix.get("authoritativePrinciple", "").lower():
        errors.append("Character matrix must retain the nonauthoritative client-state principle")
    if len(matrix.get("lifecycleStates", [])) < 12:
        errors.append("Character matrix must define at least twelve lifecycle states")
    if len(matrix.get("fieldClasses", [])) < 7:
        errors.append("Character matrix must define at least seven field classes")
    if len(matrix.get("validationClasses", [])) < 18:
        errors.append("Character matrix must define at least eighteen validation classes")
    if len(matrix.get("operationTypes", [])) < 16:
        errors.append("Character matrix must define at least sixteen operation types")
    if len(matrix.get("requiredDeniedCases", [])) < 24:
        errors.append("Character matrix must define at least twenty-four denied cases")
    if len(matrix.get("requiredEventTypes", [])) < 18:
        errors.append("Character matrix must define at least eighteen Event types")
    if matrix.get("acceptanceCriteria") != EXPECTED_CRITERIA:
        errors.append("Character matrix acceptance criteria are incomplete")
    prohibited = matrix.get("offlineCapabilities", {}).get("prohibited", [])
    for required in ["character-activation", "advancement-commit", "migration-commit"]:
        if required not in prohibited:
            errors.append(f"Character matrix offline prohibition missing {required}")
    for flag in [
        "implementationAuthorized",
        "realUserDataCollectionAuthorized",
        "paidServicesAuthorized",
        "productionCredentialsAuthorized",
        "internalAlphaReleaseAuthorized",
        "productionAuthorized",
        "publicReleaseAuthorized",
    ]:
        if matrix.get("authorizations", {}).get(flag) is not False:
            errors.append(f"Character matrix authorization flag {flag} must be false")

    if trace.get("featureId") != "MV-IA-F004":
        errors.append("Character traceability has incorrect featureId")
    if "IA-D02-006" not in trace.get("dependencies", []):
        errors.append("Character traceability must depend on IA-D02-006")
    if trace.get("acceptanceCriteria") != EXPECTED_CRITERIA:
        errors.append("Character traceability acceptance criteria are incomplete")
    if len(trace.get("downstreamCallers", [])) < 10:
        errors.append("Character traceability downstream callers are incomplete")

    require_text(
        review_text,
        [
            "stable-ID governed selections",
            "no silent last-write-wins",
            "no offline authoritative mutation",
            "history-preserving advancement",
            "implementation remains dependency-gated",
            "CCA-AC-001 through CCA-AC-020",
        ],
        "Character review receipt",
        errors,
    )
    require_text(
        readiness_text,
        [
            "IMPLEMENTATION-READY DESIGN",
            "application implementation remains dependency-gated",
            "IA-D03-002",
        ],
        "Character readiness record",
        errors,
    )

    if completion.get("status") != "complete":
        errors.append("Character completion record status must be complete")
    if completion.get("owner") != "John Brandon Turner":
        errors.append("Character completion record owner is incorrect")
    result = completion.get("result", {})
    expected_counts = {
        "acceptanceCriteriaCount": 20,
        "lifecycleStateCount": 12,
        "validationClassCount": 18,
        "operationTypeCount": 16,
        "deniedCaseCount": 26,
        "blockingFindingCount": 0,
    }
    for key, value in expected_counts.items():
        if result.get(key) != value:
            errors.append(f"Character completion record {key} must be {value}")
    if not completion.get("nextDesignItem", "").startswith("IA-D03-002"):
        errors.append("Character completion record must advance to IA-D03-002")
    for flag in [
        "implementationAuthorized",
        "realUserDataCollectionAuthorized",
        "paidServicesAuthorized",
        "internalAlphaReleaseAuthorized",
        "productionAuthorized",
        "publicReleaseAuthorized",
    ]:
        if completion.get(flag) is not False:
            errors.append(f"Character completion record {flag} must be false")

    combined = packet_text + review_text + readiness_text + json.dumps(matrix) + json.dumps(trace) + json.dumps(completion)
    if "prophecy" in combined.lower():
        errors.append("corrected autocorrect term appears in MV-IA-F004 artifacts")

    if errors:
        raise SystemExit(
            "MV-IA-F004 CHARACTER DESIGN VALIDATION: FAIL\n"
            + "\n".join(f"- {message}" for message in errors)
        )

    print("MV-IA-F004 CHARACTER DESIGN VALIDATION: PASS")
    print("Acceptance criteria: 20")
    print(f"Lifecycle states: {len(matrix['lifecycleStates'])}")
    print(f"Validation classes: {len(matrix['validationClasses'])}")
    print(f"Operation types: {len(matrix['operationTypes'])}")
    print(f"Denied cases: {len(matrix['requiredDeniedCases'])}")
    print("Blocking findings: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
