#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "INTERNAL_ALPHA_FEATURE_REGISTRY.json"

REQUIRED_FILES = [
    "README.md",
    "INTERNAL_ALPHA_SCOPE.md",
    "INTERNAL_ALPHA_FEATURE_REGISTRY.json",
    "INTERNAL_ALPHA_DEPENDENCY_MAP.md",
    "INTERNAL_ALPHA_USER_JOURNEYS.md",
    "INTERNAL_ALPHA_SHARED_SYSTEMS.md",
    "INTERNAL_ALPHA_ACCEPTANCE_MATRIX.md",
    "INTERNAL_ALPHA_DEFERRED_FEATURES.md",
    "INTERNAL_ALPHA_CONTENT_AND_FIXTURES.md",
    "INTERNAL_ALPHA_OWNER_DECISIONS.md",
    "INTERNAL_ALPHA_DESIGN_BACKLOG.md",
    "feature-packets/FEATURE_PACKET_TEMPLATE.md",
]

ALLOWED_CLASSES = {
    "entry-critical",
    "alpha-required",
    "experimental",
    "deferred",
}

ALLOWED_STATUSES = {
    "registered",
    "packet-in-progress",
    "implementation-ready",
    "implemented",
    "validated",
    "alpha-ready",
    "deferred",
}

REQUIRED_FEATURE_FIELDS = {
    "featureId",
    "name",
    "classification",
    "stageA",
    "area",
    "historicalModule",
    "summary",
    "dependencies",
    "alphaSlice",
    "fullScopeDeferred",
    "designOrder",
    "designStatus",
}


def fail(message: str) -> None:
    raise SystemExit(f"MV-IA-001 VALIDATION: FAIL\n{message}")


def main() -> int:
    missing_files = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing_files:
        fail(f"Missing required files: {missing_files}")

    try:
        payload = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Registry cannot be read: {exc}")

    if payload.get("programId") != "MV-IA-001":
        fail("Registry programId must be MV-IA-001.")

    features = payload.get("features")
    if not isinstance(features, list) or not features:
        fail("Registry must contain a non-empty features array.")

    ids: list[str] = []
    names: list[str] = []
    errors: list[str] = []

    for index, feature in enumerate(features):
        if not isinstance(feature, dict):
            errors.append(f"Feature at index {index} is not an object.")
            continue

        missing = sorted(REQUIRED_FEATURE_FIELDS - set(feature))
        if missing:
            errors.append(f"Feature at index {index} is missing fields: {missing}")
            continue

        feature_id = feature["featureId"]
        name = feature["name"]
        ids.append(feature_id)
        names.append(name)

        if not isinstance(feature_id, str) or not feature_id.startswith("MV-IA-F"):
            errors.append(f"Invalid featureId: {feature_id!r}")
        if feature["classification"] not in ALLOWED_CLASSES:
            errors.append(f"{feature_id}: invalid classification {feature['classification']!r}")
        if feature["designStatus"] not in ALLOWED_STATUSES:
            errors.append(f"{feature_id}: invalid designStatus {feature['designStatus']!r}")
        if not isinstance(feature["dependencies"], list):
            errors.append(f"{feature_id}: dependencies must be an array.")
        if not isinstance(feature["designOrder"], int) or feature["designOrder"] < 1:
            errors.append(f"{feature_id}: designOrder must be a positive integer.")
        if not isinstance(feature["fullScopeDeferred"], bool):
            errors.append(f"{feature_id}: fullScopeDeferred must be boolean.")
        if not str(feature["alphaSlice"]).strip():
            errors.append(f"{feature_id}: alphaSlice must not be empty.")

    if len(ids) != len(set(ids)):
        errors.append("Feature IDs must be unique.")
    if len(names) != len(set(names)):
        errors.append("Feature names must be unique.")

    known_ids = set(ids)
    for feature in features:
        if not isinstance(feature, dict) or "featureId" not in feature:
            continue
        for dependency in feature.get("dependencies", []):
            if dependency not in known_ids:
                errors.append(
                    f"{feature['featureId']}: dependency {dependency!r} is not registered."
                )
            if dependency == feature["featureId"]:
                errors.append(f"{feature['featureId']}: feature cannot depend on itself.")

    combined_text = "\n".join(
        (ROOT / relative).read_text(encoding="utf-8")
        for relative in REQUIRED_FILES
        if relative.endswith((".md", ".json"))
    ).lower()

    # The mistaken word is allowed only in explicit correction records.
    correction_files = {
        "README.md",
        "INTERNAL_ALPHA_DEFERRED_FEATURES.md",
        "INTERNAL_ALPHA_OWNER_DECISIONS.md",
    }
    for relative in REQUIRED_FILES:
        if not relative.endswith((".md", ".json")) or relative in correction_files:
            continue
        contents = (ROOT / relative).read_text(encoding="utf-8").lower()
        if "prophecy" in contents:
            errors.append(
                f"{relative}: contains the corrected autocorrect term outside an explicit correction record."
            )

    if "relationship tracker" not in combined_text:
        errors.append("Relationship Tracker must remain represented.")
    if "first playable action" not in combined_text:
        errors.append("First playable Action and approval loop must remain represented.")

    entry_critical = [
        feature for feature in features if feature["classification"] == "entry-critical"
    ]
    alpha_required = [
        feature for feature in features if feature["classification"] == "alpha-required"
    ]
    if not entry_critical:
        errors.append("At least one entry-critical feature is required.")
    if not alpha_required:
        errors.append("At least one alpha-required feature is required.")

    if errors:
        fail("\n".join(f"- {error}" for error in errors))

    print("MV-IA-001 VALIDATION: PASS")
    print(f"Features: {len(features)}")
    print(f"Entry-critical: {len(entry_critical)}")
    print(f"Alpha-required: {len(alpha_required)}")
    print(
        "Experimental: "
        f"{sum(1 for feature in features if feature['classification'] == 'experimental')}"
    )
    print(
        "Deferred: "
        f"{sum(1 for feature in features if feature['classification'] == 'deferred')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
