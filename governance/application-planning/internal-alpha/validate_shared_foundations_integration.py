#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKETS = ROOT / "feature-packets"
REVIEW = PACKETS / "IA-D02-006_SHARED_FOUNDATIONS_INTEGRATION_REVIEW.md"
MATRIX = PACKETS / "IA-D02-006_SHARED_FOUNDATIONS_CONTRACT_MATRIX.json"
COMPLETION = PACKETS / "IA-D02-006_COMPLETION_RECORD.json"
RECEIPT = PACKETS / "IA-D02-006_REVIEW_RECEIPT.md"

EXPECTED_FEATURES = ["MV-IA-F002", "MV-IA-F020", "MV-IA-F003", "MV-IA-F021", "MV-IA-F025"]
EXPECTED_ROLES = [
    "invited-tester", "player", "game-master", "assistant-gm",
    "content-creator", "observer", "owner-admin", "service-actor",
]
EXPECTED_CRITERIA = [f"SFI-AC-{number:03d}" for number in range(1, 21)]
EXPECTED_CONTRACTS = [f"SFI-C{number:03d}" for number in range(1, 25)]
EXPECTED_JOURNEYS = [f"SFI-J{number:03d}" for number in range(1, 6)]
EXPECTED_FINDINGS = [f"SFI-F{number:03d}" for number in range(1, 9)]


def load_json(path: Path, errors: list[str]) -> dict:
    if not path.is_file():
        errors.append(f"missing required JSON artifact: {path.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}


def require_phrases(text: str, phrases: list[str], label: str, errors: list[str]) -> None:
    lower = text.lower()
    for phrase in phrases:
        if phrase.lower() not in lower:
            errors.append(f"{label} missing required phrase {phrase!r}")


def validate_source_matrices(errors: list[str]) -> None:
    f003 = load_json(PACKETS / "MV-IA-F003_IDENTITY_WORKSPACE_MATRIX.json", errors)
    f020 = load_json(PACKETS / "MV-IA-F020_PERMISSION_SURFACE_MATRIX.json", errors)
    f021 = load_json(PACKETS / "MV-IA-F021_RECOVERY_AND_OFFLINE_MATRIX.json", errors)
    f025 = load_json(PACKETS / "MV-IA-F025_ONBOARDING_SUPPORT_MATRIX.json", errors)

    if f003.get("defaultWorkspaceDecision") != "deny" or len(f003.get("roles", [])) < 8:
        errors.append("MV-IA-F003 identity/workspace baseline is incomplete")
    context_fields = set(f003.get("contextReceiptRequiredFields", []))
    if not ({"permissionVersion", "permissionsVersion"} & context_fields):
        errors.append("MV-IA-F003 context receipt lacks a permission-version field")
    if not ({"entitlementVersion", "entitlementRulesetVersion"} & context_fields):
        errors.append("MV-IA-F003 context receipt lacks an entitlement-version field")

    if f020.get("defaultDecision") != "deny":
        errors.append("MV-IA-F020 must retain defaultDecision=deny")
    if len(f020.get("visibilityClasses", [])) < 10 or len(f020.get("surfaces", [])) < 25:
        errors.append("MV-IA-F020 protected projection baseline is incomplete")

    if "nonauthoritative" not in f021.get("authoritativePrinciple", "").lower():
        errors.append("MV-IA-F021 must retain the nonauthoritative client-state principle")
    if len(f021.get("stateVocabulary", [])) < 16 or len(f021.get("interruptionPoints", [])) < 15:
        errors.append("MV-IA-F021 recovery baseline is incomplete")

    if f025.get("defaultDiagnosticDecision") != "exclude" or f025.get("defaultIssueDecision") != "deny":
        errors.append("MV-IA-F025 diagnostic or issue default is incorrect")
    if f025.get("attachmentRules", {}).get("automaticCapture") is not False:
        errors.append("MV-IA-F025 must prohibit automatic attachment capture")
    if len(f025.get("protectedDiagnosticSurfaces", [])) < 20:
        errors.append("MV-IA-F025 diagnostic surface baseline is incomplete")


def main() -> int:
    errors: list[str] = []
    for path in [REVIEW, MATRIX, COMPLETION, RECEIPT]:
        if not path.is_file():
            errors.append(f"missing required integration artifact: {path.relative_to(ROOT)}")

    review = REVIEW.read_text(encoding="utf-8") if REVIEW.is_file() else ""
    receipt = RECEIPT.read_text(encoding="utf-8") if RECEIPT.is_file() else ""
    matrix = load_json(MATRIX, errors)
    completion = load_json(COMPLETION, errors)

    if not review.startswith("# IA-D02-006 — Shared-Foundations Integration Review"):
        errors.append("integration review title is incorrect")
    if "**Owner and final authority:** John Brandon Turner" not in review:
        errors.append("integration review owner is missing or incorrect")
    if "**Status:** COMPLETE — DESIGN INTEGRATION REVIEW" not in review:
        errors.append("integration review status is missing or incorrect")

    sections = [
        int(match.group(1))
        for line in review.splitlines()
        if (match := re.match(r"^## (\d+)\. ", line))
    ]
    if sections != list(range(1, 21)):
        errors.append(f"integration review must contain sections 1-20 exactly once and in order; got {sections}")

    require_phrases(review, [
        "default decision is deny",
        "selected-context receipt is a navigation and recovery aid",
        "nonauthoritative",
        "authorization and entitlement filtering occur before",
        "status using the original operation or command ID",
        "silent last-write-wins is prohibited",
        "cannot perform authoritative mutation",
        "diagnostic generation defaults to exclude",
        "issue report does not grant support access",
        "zero paid identity provider",
        "zero AI",
        "No blocking integration finding remains open",
        "Silence is not approval",
        "IA-D03-001",
    ], "integration review", errors)

    for criterion in EXPECTED_CRITERIA:
        if criterion not in review:
            errors.append(f"integration review missing acceptance criterion {criterion}")

    if matrix.get("programId") != "MV-IA-001" or matrix.get("reviewId") != "IA-D02-006":
        errors.append("integration matrix identity is incorrect")
    if matrix.get("owner") != "John Brandon Turner":
        errors.append("integration matrix owner is incorrect")
    if matrix.get("status") != "complete-design-integration-review":
        errors.append("integration matrix status is incorrect")
    if matrix.get("reviewedFeatures") != EXPECTED_FEATURES:
        errors.append("integration matrix reviewedFeatures are incomplete or out of order")
    if matrix.get("canonicalRoles") != EXPECTED_ROLES:
        errors.append("integration matrix canonicalRoles are incomplete or out of order")

    actors = {item.get("actorId"): item for item in matrix.get("nonUserActors", [])}
    if actors.get("ai", {}).get("classification") != "optional-assistive-service-actor":
        errors.append("AI must be an optional assistive service actor")

    expected_aliases = {
        "permissionsVersion": "permissionVersion",
        "entitlementRulesetVersion": "entitlementVersion",
        "gameSessionId": "sessionId",
        "gm": "game-master",
    }
    aliases = matrix.get("compatibilityAliases", {})
    for alias, canonical in expected_aliases.items():
        if aliases.get(alias) != canonical:
            errors.append(f"alias {alias!r} must normalize to {canonical!r}")

    fields = matrix.get("canonicalContractFields", [])
    required_fields = {
        "subjectId", "selectedContextReceiptId", "permissionVersion", "entitlementVersion",
        "operationId", "idempotencyKey", "expectedVersion", "lastAcknowledgedSequence",
        "userSafeReasonCode",
    }
    missing_fields = required_fields - set(fields)
    if missing_fields or len(fields) < 25:
        errors.append(f"canonical contract fields are incomplete: {sorted(missing_fields)}")

    contracts = matrix.get("contractOwnership", [])
    contract_ids = [item.get("contractId") for item in contracts]
    if contract_ids != EXPECTED_CONTRACTS:
        errors.append("integration matrix must define SFI-C001 through SFI-C024 in order")
    if any(not item.get("controller") or not item.get("rule") for item in contracts):
        errors.append("every shared contract must define controller and rule")

    journeys = matrix.get("integrationJourneys", [])
    if [item.get("journeyId") for item in journeys] != EXPECTED_JOURNEYS:
        errors.append("integration matrix must define SFI-J001 through SFI-J005 in order")
    known_contracts = set(contract_ids)
    for journey in journeys:
        if not journey.get("steps"):
            errors.append(f"{journey.get('journeyId')} has no steps")
        unknown = set(journey.get("requiredContracts", [])) - known_contracts
        if unknown:
            errors.append(f"{journey.get('journeyId')} references unknown contracts: {sorted(unknown)}")

    findings = matrix.get("resolvedFindings", [])
    if [item.get("findingId") for item in findings] != EXPECTED_FINDINGS:
        errors.append("integration matrix must define SFI-F001 through SFI-F008 in order")
    if matrix.get("blockingFindings") != []:
        errors.append("completion cannot retain blocking findings")
    if len(matrix.get("downstreamRequiredClauses", [])) < 12:
        errors.append("downstream obligations are incomplete")
    if matrix.get("acceptanceCriteria") != EXPECTED_CRITERIA:
        errors.append("integration matrix acceptance criteria are incomplete")

    for flag in ["implementationAuthorized", "internalAlphaReleaseAuthorized", "productionAuthorized", "publicReleaseAuthorized"]:
        if matrix.get(flag) is not False:
            errors.append(f"integration matrix {flag} must be false")

    if completion.get("status") != "complete" or completion.get("owner") != "John Brandon Turner":
        errors.append("completion record identity or status is incorrect")
    result = completion.get("result", {})
    expected_counts = {
        "contractCount": 24,
        "integrationJourneyCount": 5,
        "resolvedFindingCount": 8,
        "blockingFindingCount": 0,
        "acceptanceCriteriaCount": 20,
    }
    for field, expected in expected_counts.items():
        if result.get(field) != expected:
            errors.append(f"completion record {field} must be {expected}")
    if not completion.get("nextDesignItem", "").startswith("IA-D03-001"):
        errors.append("completion record must advance to IA-D03-001")
    for flag in [
        "implementationAuthorized", "realTesterDiagnosticsAuthorized",
        "internalAlphaReleaseAuthorized", "productionAuthorized", "publicReleaseAuthorized",
    ]:
        if completion.get(flag) is not False:
            errors.append(f"completion record {flag} must be false")

    require_phrases(receipt, [
        "PASS — DESIGN INTEGRATION COMPLETE",
        "twenty-four controlling shared contracts",
        "zero blocking findings",
        "issue reporting never grants support access",
        "implementation remains dependency-gated",
        "Silence is not approval",
        "IA-D03-001",
    ], "review receipt", errors)

    combined = (review + receipt + json.dumps(matrix) + json.dumps(completion)).lower()
    if "prophecy" in combined:
        errors.append("corrected autocorrect term appears in IA-D02-006 artifacts")

    validate_source_matrices(errors)

    if errors:
        raise SystemExit(
            "IA-D02-006 SHARED-FOUNDATIONS INTEGRATION VALIDATION: FAIL\n"
            + "\n".join(f"- {message}" for message in errors)
        )

    print("IA-D02-006 SHARED-FOUNDATIONS INTEGRATION VALIDATION: PASS")
    print(f"Reviewed features: {len(EXPECTED_FEATURES)}")
    print(f"Shared contracts: {len(contracts)}")
    print(f"Integrated journeys: {len(journeys)}")
    print(f"Resolved findings: {len(findings)}")
    print("Blocking findings: 0")
    print(f"Acceptance criteria: {len(EXPECTED_CRITERIA)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
