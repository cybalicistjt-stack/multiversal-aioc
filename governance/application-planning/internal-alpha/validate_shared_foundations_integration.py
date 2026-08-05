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

EXPECTED_FEATURES = [
    "MV-IA-F002",
    "MV-IA-F020",
    "MV-IA-F003",
    "MV-IA-F021",
    "MV-IA-F025",
]
EXPECTED_ROLES = [
    "invited-tester",
    "player",
    "game-master",
    "assistant-gm",
    "content-creator",
    "observer",
    "owner-admin",
    "service-actor",
]
EXPECTED_CRITERIA = [f"SFI-AC-{number:03d}" for number in range(1, 21)]


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


def validate_source_matrices(errors: list[str]) -> None:
    f003 = load_json(PACKETS / "MV-IA-F003_IDENTITY_WORKSPACE_MATRIX.json", errors)
    f020 = load_json(PACKETS / "MV-IA-F020_PERMISSION_SURFACE_MATRIX.json", errors)
    f021 = load_json(PACKETS / "MV-IA-F021_RECOVERY_AND_OFFLINE_MATRIX.json", errors)
    f025 = load_json(PACKETS / "MV-IA-F025_ONBOARDING_SUPPORT_MATRIX.json", errors)

    if f003.get("defaultWorkspaceDecision") != "deny":
        errors.append("MV-IA-F003 must retain defaultWorkspaceDecision=deny")
    if len(f003.get("roles", [])) < 8:
        errors.append("MV-IA-F003 must retain at least eight role definitions")
    context_fields = set(f003.get("contextReceiptRequiredFields", []))
    if not ({"permissionVersion", "permissionsVersion"} & context_fields):
        errors.append("MV-IA-F003 context receipt lacks a permission-version field")
    if not ({"entitlementVersion", "entitlementRulesetVersion"} & context_fields):
        errors.append("MV-IA-F003 context receipt lacks an entitlement-version field")

    if f020.get("defaultDecision") != "deny":
        errors.append("MV-IA-F020 must retain defaultDecision=deny")
    if len(f020.get("visibilityClasses", [])) < 10:
        errors.append("MV-IA-F020 must retain at least ten visibility classes")
    if len(f020.get("surfaces", [])) < 25:
        errors.append("MV-IA-F020 must retain at least twenty-five protected surfaces")

    principle = f021.get("authoritativePrinciple", "").lower()
    if "nonauthoritative" not in principle:
        errors.append("MV-IA-F021 must retain the nonauthoritative client-state principle")
    if len(f021.get("stateVocabulary", [])) < 16:
        errors.append("MV-IA-F021 must retain at least sixteen recovery states")
    if len(f021.get("interruptionPoints", [])) < 15:
        errors.append("MV-IA-F021 must retain at least fifteen interruption points")

    if f025.get("defaultDiagnosticDecision") != "exclude":
        errors.append("MV-IA-F025 must retain defaultDiagnosticDecision=exclude")
    if f025.get("defaultIssueDecision") != "deny":
        errors.append("MV-IA-F025 must retain defaultIssueDecision=deny")
    if f025.get("attachmentRules", {}).get("automaticCapture") is not False:
        errors.append("MV-IA-F025 must prohibit automatic attachment capture")
    if len(f025.get("protectedDiagnosticSurfaces", [])) < 20:
        errors.append("MV-IA-F025 must retain at least twenty protected diagnostic surfaces")


def main() -> int:
    errors: list[str] = []

    for path in [REVIEW, MATRIX, COMPLETION, RECEIPT]:
        if not path.is_file():
            errors.append(f"missing required integration artifact: {path.relative_to(ROOT)}")

    review_text = REVIEW.read_text(encoding="utf-8") if REVIEW.is_file() else ""
    receipt_text = RECEIPT.read_text(encoding="utf-8") if RECEIPT.is_file() else ""
    matrix = load_json(MATRIX, errors)
    completion = load_json(COMPLETION, errors)

    if review_text and not review_text.startswith("# IA-D02-006 — Shared-Foundations Integration Review"):
        errors.append("integration review title is incorrect")
    if "**Owner and final authority:** John Brandon Turner" not in review_text:
        errors.append("integration review owner is missing or incorrect")
    if "**Status:** COMPLETE — DESIGN INTEGRATION REVIEW" not in review_text:
        errors.append("integration review status is missing or incorrect")

    seen_sections: list[int] = []
    for line in review_text.splitlines():
        match = re.match(r"^## (\d+)\. ", line)
        if match:
            seen_sections.append(int(match.group(1)))
    if seen_sections != list(range(1, 21)):
        errors.append(f"integration review must contain sections 1-20 exactly once and in order; got {seen_sections}")

    require_text(
        review_text,
        [
            "default decision is deny",
            "selected-context receipt is a navigation and recovery aid",
            "nonauthoritative",
            "authorization and entitlement filtering occur before",
            "status using the original operation or command ID",
            "silent last-write-wins is prohibited",
            "no offline authoritative mutation",
            "diagnostic generation defaults to exclude",
            "issue report does not grant support access",
            "zero paid identity provider",
            "zero AI",
            "No blocking integration finding remains open",
            "Silence is not approval",
            "IA-D03-001",
        ],
        "integration review",
        errors,
    )

    for criterion in EXPECTED_CRITERIA:
        if criterion not in review_text:
            errors.append(f"integration review missing acceptance criterion {criterion}")

    if matrix.get("programId") != "MV-IA-001":
        errors.append("integration matrix has incorrect programId")
    if matrix.get("reviewId") != "IA-D02-006":
        errors.append("integration matrix has incorrect reviewId")
    if matrix.get("owner") != "John Brandon Turner":
        errors.append("integration matrix has incorrect owner")
    if matrix.get("status") != "complete-design-integration-review":
        errors.append("integration matrix has incorrect status")
    if matrix.get("reviewedFeatures") != EXPECTED_FEATURES:
        errors.append("integration matrix reviewedFeatures are incomplete or out of order")
    if matrix.get("canonicalRoles") != EXPECTED_ROLES:
        errors.append("integration matrix canonicalRoles are incomplete or out of order")

    non_user_actors = {item.get("actorId"): item for item in matrix.get("nonUserActors", [])}
    if non_user_actors.get("ai", {}).get("classification") != "optional-assistive-service-actor":
        errors.append("AI must be classified as an optional assistive service actor")

    aliases = matrix.get("compatibilityAliases", {})
    expected_aliases = {
        "permissionsVersion": "permissionVersion",
        "entitlementRulesetVersion": "entitlementVersion",
        "gameSessionId": "sessionId",
        "gm": "game-master",
    }
    for alias, canonical in expected_aliases.items():
        if aliases.get(alias) != canonical:
            errors.append(f"integration matrix alias {alias!r} must normalize to {canonical!r}")

    fields = matrix.get("canonicalContractFields", [])
    for field in [
        "subjectId",
        "selectedContextReceiptId",
        "permissionVersion",
        "entitlementVersion",
        "operationId",
        "idempotencyKey",
        "expectedVersion",
        "lastAcknowledgedSequence",
        "userSafeReasonCode",
    ]:
        if field not in fields:
            errors.append(f"integration matrix missing canonical field {field}")
    if len(fields) < 25:
        errors.append("integration matrix must define at least twenty-five canonical contract fields")

    contracts = matrix.get("contractOwnership", [])
    contract_ids = [item.get("contractId") for item in contracts]
    if contract_ids != [f"SFI-C{number:03d}" for number in range(1, 25)]:
        errors.append("integration matrix must define SFI-C001 through SFI-C024 exactly once and in order")
    if any(not item.get("controller") or not item.get("rule") for item in contracts):
        errors.append("every shared-foundation contract must define controller and rule")

    journeys = matrix.get("integrationJourneys", [])
    if [item.get("journeyId") for item in journeys] != [f"SFI-J{number:03d}" for number in range(1, 6)]:
        errors.append("integration matrix must define SFI-J001 through SFI-J005 exactly once and in order")
    known_contracts = set(contract_ids)
    for journey in journeys:
        if not journey.get("steps"):
            errors.append(f"{journey.get('journeyId')} has no steps")
        unknown = set(journey.get("requiredContracts", [])) - known_contracts
        if unknown:
            errors.append(f"{journey.get('journeyId')} references unknown contracts: {sorted(unknown)}")

    findings = matrix.get("resolvedFindings", [])
    if [item.get("findingId") for item in findings] != [f"SFI-F{number:03d}" for number in range(1, 9)]:
        errors.append("integration matrix must define SFI-F001 through SFI-F008 exactly once and in order")
    if matrix.get("blockingFindings") != []:
        errors.append("integration matrix must not claim completion with blocking findings")
    if len(matrix.get("downstreamRequiredClauses", [])) < 12:
        errors.append("integration matrix downstream obligations are incomplete")
    if matrix.get("acceptanceCriteria") != EXPECTED_CRITERIA:
        errors.append("integration matrix acceptance criteria are incomplete")

    for flag in [
        "implementationAuthorized",
        "internalAlphaReleaseAuthorized",
        "productionAuthorized",
        "publicReleaseAuthorized",
    ]:
        if matrix.get(flag) is not False:
            errors.append(f"integration matrix {flag} must be false")

    if completion.get("status") != "complete":
        errors.append("completion record status must be complete")
    if completion.get("owner") != "John Brandon Turner":
        errors.append("completion record owner is incorrect")
    result = completion.get("result", {})
    if result.get("contractCount") != 24:
        errors.append("completion record contractCount must be 24")
    if result.get("integrationJourneyCount") != 5:
        errors.append("completion record integrationJourneyCount must be 5")
    if result.get("resolvedFindingCount") != 8:
        errors.append("completion record resolvedFindingCount must be 8")
    if result.get("blockingFindingCount") != 0:
        errors.append("completion record blockingFindingCount must be 0")
    if result.get("acceptanceCriteriaCount") != 20:
        errors.append("completion record acceptanceCriteriaCount must be 20")
    if not completion.get("nextDesignItem", "").startswith("IA-D03-001"):
        errors.append("completion record must advance to IA-D03-001")

    for flag in [
        "implementationAuthorized",
        "realTesterDiagnosticsAuthorized",
        "internalAlphaReleaseAuthorized",
        "productionAuthorized",
        "publicReleaseAuthorized",
    ]:
        if completion.get(flag) is not False:
            errors.append(f"completion record {flag} must be false")

    require_text(
        receipt_text,
        [
            "PASS — DESIGN INTEGRATION COMPLETE",
            "twenty-four controlling shared contracts",
            "zero blocking findings",
            "issue reporting never grants support access",
            "implementation remains dependency-gated",
            "Silence is not approval",
            "IA-D03-001",
        ],
        "review receipt",
        errors,
    )

    combined = (review_text + receipt_text + json.dumps(matrix) + json.dumps(completion)).lower()
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
