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

    if checked == 0:
        errors.append("No implementation-ready or later feature packet was checked.")

    if errors:
        fail(errors)

    print("MV-IA FEATURE PACKET VALIDATION: PASS")
    print(f"Ready packets checked: {checked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
