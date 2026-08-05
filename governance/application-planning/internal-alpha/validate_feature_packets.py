#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "INTERNAL_ALPHA_FEATURE_REGISTRY.json"
READY_STATUSES = {"implementation-ready", "implemented", "validated", "alpha-ready"}
REQUIRED_SECTIONS = list(range(1, 25))


def fail(messages: list[str]) -> None:
    raise SystemExit("MV-IA FEATURE PACKET VALIDATION: FAIL\n" + "\n".join(f"- {m}" for m in messages))


def validate_companion_files(feature: dict, errors: list[str]) -> None:
    feature_id = feature.get("featureId", "<missing>")
    for companion_path in feature.get("companionFiles", []):
        path = ROOT / companion_path
        if not path.is_file():
            errors.append(f"{feature_id}: companion file does not exist at {companion_path}.")
            continue
        if path.suffix == ".json":
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{feature_id}: invalid companion JSON {companion_path}: {exc}.")
                continue
            if payload.get("featureId") != feature_id:
                errors.append(f"{feature_id}: companion {companion_path} has wrong featureId.")
            if payload.get("owner") != "John Brandon Turner":
                errors.append(f"{feature_id}: companion {companion_path} has incorrect owner.")
            if "prophecy" in path.read_text(encoding="utf-8").lower():
                errors.append(f"{feature_id}: corrected autocorrect term appears in {companion_path}.")


def require_phrases(feature_id: str, text: str, phrases: list[str], errors: list[str]) -> None:
    lower = text.lower()
    for phrase in phrases:
        if phrase.lower() not in lower:
            errors.append(f"{feature_id}: missing required phrase {phrase!r}.")


def validate_criteria(feature_id: str, text: str, prefix: str, count: int, errors: list[str]) -> None:
    for number in range(1, count + 1):
        criterion = f"{prefix}-AC-{number:03d}"
        if criterion not in text:
            errors.append(f"{feature_id}: missing acceptance criterion {criterion}.")


def main() -> int:
    payload = json.loads(REGISTRY.read_text(encoding="utf-8"))
    errors: list[str] = []
    checked = 0

    for feature in payload.get("features", []):
        if feature.get("designStatus") not in READY_STATUSES:
            continue

        feature_id = feature.get("featureId", "<missing>")
        packet_path = feature.get("packetPath")
        packet_version = feature.get("packetVersion")

        if not packet_path:
            errors.append(f"{feature_id}: ready feature must define packetPath.")
            continue
        if not packet_version:
            errors.append(f"{feature_id}: ready feature must define packetVersion.")

        path = ROOT / packet_path
        if not path.is_file():
            errors.append(f"{feature_id}: packet does not exist at {packet_path}.")
            continue

        checked += 1
        text = path.read_text(encoding="utf-8")
        lower = text.lower()

        if not text.startswith(f"# {feature_id} — {feature['name']}"):
            errors.append(f"{feature_id}: packet title does not match registry identity.")
        if f"**Feature ID:** {feature_id}" not in text:
            errors.append(f"{feature_id}: packet does not repeat the feature ID.")
        if feature["designStatus"] == "implementation-ready" and "**Design status:** implementation-ready" not in text:
            errors.append(f"{feature_id}: packet status does not match registry.")
        if "**Owner:** John Brandon Turner" not in text:
            errors.append(f"{feature_id}: owner is missing or incorrect.")
        if "prophecy" in lower:
            errors.append(f"{feature_id}: corrected autocorrect term appears in a feature packet.")

        seen_sections = []
        for line in text.splitlines():
            match = re.match(r"^## (\d+)\. ", line)
            if match:
                seen_sections.append(int(match.group(1)))
        if seen_sections != REQUIRED_SECTIONS:
            errors.append(f"{feature_id}: expected sections 1-24 exactly once and in order; got {seen_sections}.")

        required = [
            "## 1. Problem and user outcome",
            "## 2. Alpha slice",
            "## 3. Roles and authority",
            "## 4. Dependencies",
            "## 5. Object and state model",
            "## 8. Failure, empty, and recovery states",
            "## 9. Permissions and hidden information",
            "## 10. Entitlements",
            "## 11. Persistence and history",
            "## 14. Accessibility",
            "## 18. Test scenarios",
            "## 19. Acceptance criteria",
            "## 21. Security, privacy, cost, and risk",
            "## 22. Owner review points",
            "## 23. Implementation handoff",
            "## 24. Readiness decision",
            "Silence is not approval.",
            "implementation remains dependency-gated",
        ]
        for phrase in required:
            if phrase not in text:
                errors.append(f"{feature_id}: missing required packet content: {phrase!r}.")

        validate_companion_files(feature, errors)

        if feature_id == "MV-IA-F002":
            validate_criteria(feature_id, text, "UOX", 15, errors)
            require_phrases(feature_id, text, [
                "stable ID","Character caller","Scene caller","role-safe","provenance",
                "relationship","exact stable-ID lookup","zero AI","zero paid search services"
            ], errors)

        if feature_id == "MV-IA-F003":
            validate_criteria(feature_id, text, "IDW", 20, errors)
            require_phrases(feature_id, text, [
                "stable internal subject","selected-context receipt","invitation","no enumeration",
                "Player and GM","role switch","deep link","recent-work","provider-neutral",
                "zero paid identity provider"
            ], errors)
            matrix_path = ROOT / "feature-packets/MV-IA-F003_IDENTITY_WORKSPACE_MATRIX.json"
            if matrix_path.is_file():
                matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
                if matrix.get("defaultWorkspaceDecision") != "deny":
                    errors.append(f"{feature_id}: identity matrix defaultWorkspaceDecision must be 'deny'.")
                if len(matrix.get("roles", [])) < 8:
                    errors.append(f"{feature_id}: identity matrix must define at least eight roles.")
                if len(matrix.get("protectedDiscoverySurfaces", [])) < 20:
                    errors.append(f"{feature_id}: identity matrix must define at least twenty discovery surfaces.")
                if len(matrix.get("requiredDeniedCases", [])) < 20:
                    errors.append(f"{feature_id}: identity matrix must define at least twenty denied cases.")
                if matrix.get("acceptanceCriteria") != [f"IDW-AC-{n:03d}" for n in range(1, 21)]:
                    errors.append(f"{feature_id}: identity matrix acceptance criteria incomplete.")

        if feature_id == "MV-IA-F020":
            validate_criteria(feature_id, text, "PHI", 20, errors)
            require_phrases(feature_id, text, [
                "deny-by-default","not-found-or-unavailable","Player-private notes","server-generated",
                "database isolation","revocation","exact stable-ID","Owner/Admin","zero AI","fail closed"
            ], errors)
            matrix_path = ROOT / "feature-packets/MV-IA-F020_PERMISSION_SURFACE_MATRIX.json"
            if matrix_path.is_file():
                matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
                if matrix.get("defaultDecision") != "deny":
                    errors.append(f"{feature_id}: permission matrix defaultDecision must be 'deny'.")
                if len(matrix.get("visibilityClasses", [])) < 10:
                    errors.append(f"{feature_id}: permission matrix must define at least ten visibility classes.")
                if len(matrix.get("surfaces", [])) < 25:
                    errors.append(f"{feature_id}: permission matrix must define at least twenty-five surfaces.")
                if len(matrix.get("requiredDeniedCases", [])) < 20:
                    errors.append(f"{feature_id}: permission matrix must define at least twenty denied cases.")
                if matrix.get("acceptanceCriteria") != [f"PHI-AC-{n:03d}" for n in range(1, 21)]:
                    errors.append(f"{feature_id}: permission matrix acceptance criteria incomplete.")

        if feature_id == "MV-IA-F021":
            validate_criteria(feature_id, text, "REC", 20, errors)
            require_phrases(feature_id, text, [
                "local draft","authoritative save","submitted command","accepted Event",
                "idempotent","last acknowledged sequence","pending GM","selected-context",
                "no offline authoritative mutation","zero paid"
            ], errors)
            matrix_path = ROOT / "feature-packets/MV-IA-F021_RECOVERY_AND_OFFLINE_MATRIX.json"
            if matrix_path.is_file():
                matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
                if len(matrix.get("stateVocabulary", [])) < 16:
                    errors.append(f"{feature_id}: recovery matrix must define at least sixteen states.")
                if len(matrix.get("interruptionPoints", [])) < 15:
                    errors.append(f"{feature_id}: recovery matrix must define at least fifteen interruption points.")
                if len(matrix.get("requiredDeniedCases", [])) < 20:
                    errors.append(f"{feature_id}: recovery matrix must define at least twenty denied cases.")
                if matrix.get("acceptanceCriteria") != [f"REC-AC-{n:03d}" for n in range(1, 21)]:
                    errors.append(f"{feature_id}: recovery matrix acceptance criteria incomplete.")

        if feature_id == "MV-IA-F025":
            validate_criteria(feature_id, text, "OHD", 20, errors)
            require_phrases(feature_id, text, [
                "release identity","role-specific","contextual help","known limitations",
                "structured issue","diagnostic preview","explicit consent","idempotent submission",
                "portable issue","support access","zero AI","zero paid"
            ], errors)
            matrix_path = ROOT / "feature-packets/MV-IA-F025_ONBOARDING_SUPPORT_MATRIX.json"
            if matrix_path.is_file():
                matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
                if matrix.get("defaultDiagnosticDecision") != "exclude":
                    errors.append(f"{feature_id}: defaultDiagnosticDecision must be 'exclude'.")
                if matrix.get("defaultIssueDecision") != "deny":
                    errors.append(f"{feature_id}: defaultIssueDecision must be 'deny'.")
                if len(matrix.get("roles", [])) < 8:
                    errors.append(f"{feature_id}: support matrix must define at least eight roles.")
                if len(matrix.get("onboardingStages", [])) < 10:
                    errors.append(f"{feature_id}: support matrix must define at least ten onboarding stages.")
                if len(matrix.get("protectedDiagnosticSurfaces", [])) < 20:
                    errors.append(f"{feature_id}: support matrix must define at least twenty diagnostic surfaces.")
                if len(matrix.get("requiredDeniedCases", [])) < 24:
                    errors.append(f"{feature_id}: support matrix must define at least twenty-four denied cases.")
                if matrix.get("acceptanceCriteria") != [f"OHD-AC-{n:03d}" for n in range(1, 21)]:
                    errors.append(f"{feature_id}: support matrix acceptance criteria incomplete.")
                for field in ["releaseIdentityRequiredFields","issueReportRequiredFields","diagnosticManifestRequiredFields","issueReceiptRequiredFields"]:
                    if len(matrix.get(field, [])) < 8:
                        errors.append(f"{feature_id}: support matrix {field} is incomplete.")
                if matrix.get("attachmentRules", {}).get("automaticCapture") is not False:
                    errors.append(f"{feature_id}: automatic attachment capture must be false.")

    if checked == 0:
        errors.append("No implementation-ready or later feature packet was checked.")

    if errors:
        fail(errors)

    print("MV-IA FEATURE PACKET VALIDATION: PASS")
    print(f"Ready packets checked: {checked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
