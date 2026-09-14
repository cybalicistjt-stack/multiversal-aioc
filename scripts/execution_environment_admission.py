#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Mapping

HEX40 = re.compile(r"^[0-9a-f]{40}$")
REQUIRED_TRUE_FIELDS = (
    "clean_worktree",
    "tracked_executable_line_endings_normalized",
    "validation_harness_ready",
    "validation_cache_policy_ready",
    "required_runner_lanes_available",
)


class EnvironmentAdmissionError(RuntimeError):
    pass


def _canonical_digest(payload: Mapping[str, Any]) -> str:
    material = {key: value for key, value in payload.items() if key != "admission_digest"}
    raw = json.dumps(material, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def assess_environment(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    repository = str(snapshot.get("repository") or "").strip()
    head_sha = str(snapshot.get("head_sha") or "").strip().lower()
    if "/" not in repository:
        raise EnvironmentAdmissionError("repository must be owner/name")
    if not HEX40.fullmatch(head_sha):
        raise EnvironmentAdmissionError("head_sha must be an exact 40-character lowercase hexadecimal SHA")

    checks = {field: snapshot.get(field) is True for field in REQUIRED_TRUE_FIELDS}
    failed = sorted(field for field, passed in checks.items() if not passed)
    decision = "ADMIT_PRODUCT_MUTATION" if not failed else "STOP_ENVIRONMENT_NOT_READY"
    receipt: dict[str, Any] = {
        "schema_version": "1.0.0",
        "decision": decision,
        "repository": repository,
        "expected_base_head_sha": head_sha,
        "checks": checks,
        "failed_checks": failed,
        "repair_lane": "separate_or_explicitly_classified_validation_harness_repair",
    }
    receipt["admission_digest"] = _canonical_digest(receipt)
    return receipt


def validate_admission_receipt(receipt: Mapping[str, Any]) -> dict[str, Any]:
    if receipt.get("decision") != "ADMIT_PRODUCT_MUTATION":
        raise EnvironmentAdmissionError("environment receipt does not authorize product mutation")
    digest = str(receipt.get("admission_digest") or "")
    if len(digest) != 64 or digest != _canonical_digest(receipt):
        raise EnvironmentAdmissionError("environment admission digest mismatch")
    checks = receipt.get("checks")
    if not isinstance(checks, Mapping) or any(checks.get(field) is not True for field in REQUIRED_TRUE_FIELDS):
        raise EnvironmentAdmissionError("environment admission is missing required passing checks")
    return {"status": "PASS", "repository": receipt.get("repository"), "expected_base_head_sha": receipt.get("expected_base_head_sha")}


def main() -> int:
    parser = argparse.ArgumentParser(description="Gate product mutation on validation-environment readiness")
    parser.add_argument("snapshot")
    args = parser.parse_args()
    data = json.loads(Path(args.snapshot).read_text(encoding="utf-8"))
    result = assess_environment(data)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "ADMIT_PRODUCT_MUTATION" else 2


if __name__ == "__main__":
    raise SystemExit(main())
