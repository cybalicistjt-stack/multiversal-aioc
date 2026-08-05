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
                errors.append(
                    f"{feature_id}: companion {companion_path} has featureId {payload.get('featureId')!r}."
                )
            if payload.get("owner") != "John Brandon Turner":
                errors.append(f"{feature_id}: companion {companion_path} has incorrect owner.")
            if "prophecy" in path.read_text(encoding="utf-8").lower():
                errors.append(f"{feature_id}: corrected autocorrect term appears in {companion_path}.")


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
        if "**Design status:** implementation-ready" not in text and feature["designStatus"] == "implementation-ready":
            errors.append(f"{feature_id}: packet status does not match implementation-ready registry state.")
        if "**Owner:** John Brandon Turner" not in text:
            errors.append(f"{feature_id}: owner is missing or incorrect.")
        if "prophecy" in lower:
            errors.append(f"{feature_id}: corrected autocorrect term appears in a feature packet.")

        seen_sections: list[int] = []
        for line in text.splitlines():
            match = re.match(r"^## (\d+)\. ", line)
            if match:
                seen_sections.append(int(match.group(1)))
        if seen_sections != REQUIRED_SECTIONS:
            errors.append(
                f"{feature_id}: expected sections 1-24 exactly once and in order; got {seen_sections}."
            )

        required_phrases = [
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
        for phrase in required_phrases:
            if phrase not in text:
                errors.append(f"{feature_id}: missing required packet content: {phrase!r}.")

        validate_companion_files(feature, errors)

        if feature_id == "MV-IA-F002":
            for number in range(1, 16):
                criterion = f"UOX-AC-{number:03d}"
                if criterion not in text:
                    errors.append(f"{feature_id}: missing acceptance criterion {criterion}.")
            for phrase in [
                "stable ID",
                "Character caller",
                "Scene caller",
                "role-safe",
                "provenance",
                "relationship",
                "exact stable-ID lookup",
                "zero AI",
                "zero paid search services",
            ]:
                if phrase.lower() not in lower:
                    errors.append(f"{feature_id}: missing Universal Object requirement {phrase!r}.")

        if feature_id == "MV-IA-F003":
            for number in range(1, 21):
                criterion = f"IDW-AC-{number:03d}"
                if criterion not in text:
                    errors.append(f"{feature_id}: missing acceptance criterion {criterion}.")
            for phrase in [
                "stable internal subject",
                "selected-context receipt",
                "invitation",
                "no enumeration",
                "Player and GM",
                "role switch",
                "deep link",
                "recent-work",
                "provider-neutral",
                "zero paid identity provider",
            ]:
                if phrase.lower() not in lower:
                    errors.append(f"{feature_id}: missing Identity/Workspace requirement {phrase!r}.")

            matrix_path = ROOT / "feature-packets/MV-IA-F003_IDENTITY_WORKSPACE_MATRIX.json"
            if matrix_path.is_file():
                matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
                if matrix.get("defaultWorkspaceDecision") != "deny":
                    errors.append(f"{feature_id}: identity matrix defaultWorkspaceDecision must be 'deny'.")
                if len(matrix.get("roles", [])) < 8:
                    errors.append(f"{feature_id}: identity matrix must define at least eight role contexts.")
                if len(matrix.get("protectedDiscoverySurfaces", [])) < 20:
                    errors.append(f"{feature_id}: identity matrix must define at least twenty discovery surfaces.")
                if len(matrix.get("requiredDeniedCases", [])) < 20:
                    errors.append(f"{feature_id}: identity matrix must define at least twenty denied cases.")
                if matrix.get("acceptanceCriteria") != [f"IDW-AC-{number:03d}" for number in range(1, 21)]:
                    errors.append(f"{feature_id}: identity matrix acceptance criteria are incomplete or out of order.")
                if len(matrix.get("contextReceiptRequiredFields", [])) < 15:
                    errors.append(f"{feature_id}: selected-context receipt field list is incomplete.")

        if feature_id == "MV-IA-F020":
            for number in range(1, 21):
                criterion = f"PHI-AC-{number:03d}"
                if criterion not in text:
                    errors.append(f"{feature_id}: missing acceptance criterion {criterion}.")
            for phrase in [
                "deny-by-default",
                "not-found-or-unavailable",
                "Player-private notes",
                "server-generated",
                "database isolation",
                "revocation",
                "exact stable-ID",
                "Owner/Admin",
                "zero AI",
                "fail closed",
            ]:
                if phrase.lower() not in lower:
                    errors.append(f"{feature_id}: missing Permissions requirement {phrase!r}.")

            matrix_path = ROOT / "feature-packets/MV-IA-F020_PERMISSION_SURFACE_MATRIX.json"
            if matrix_path.is_file():
                matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
                if matrix.get("defaultDecision") != "deny":
                    errors.append(f"{feature_id}: permission matrix defaultDecision must be 'deny'.")
                if len(matrix.get("visibilityClasses", [])) < 10:
                    errors.append(f"{feature_id}: permission matrix must define at least ten visibility classes.")
                if len(matrix.get("surfaces", [])) < 25:
                    errors.append(f"{feature_id}: permission matrix must define at least twenty-five protected surfaces.")
                if len(matrix.get("requiredDeniedCases", [])) < 20:
                    errors.append(f"{feature_id}: permission matrix must define at least twenty denied cases.")
                if matrix.get("acceptanceCriteria") != [f"PHI-AC-{number:03d}" for number in range(1, 21)]:
                    errors.append(f"{feature_id}: permission matrix acceptance criteria are incomplete or out of order.")

    if checked == 0:
        errors.append("No implementation-ready or later feature packet was checked.")

    if errors:
        fail(errors)

    print("MV-IA FEATURE PACKET VALIDATION: PASS")
    print(f"Ready packets checked: {checked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
