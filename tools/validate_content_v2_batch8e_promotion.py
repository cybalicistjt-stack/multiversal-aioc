#!/usr/bin/env python3
"""Validate governed repository promotion of Content v2 Batch 8E.

This validator is intentionally blocking until the exact promotion ZIP has been
committed. It verifies the release boundary rather than treating evidence-only
handoff files as completed promotion.
"""

from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "governance/content-recovery/releases/content-v2-batch8e-v1.6.0"
ZIP_NAME = "CONTENT_V2_BATCH8E_GOVERNED_PROMOTION_COLLECTION_v1.0.0.zip"
EXPECTED_ZIP_SHA256 = "660a2a7b2ca8301e64d992bcf759b8ca29e7b4a52f09c681ed5ae2c58a1733c0"
EXPECTED_SOURCE_SHA256 = "f9d0d04334ae0c4ef75bbe8ceb466a468a77a88aed54849db697965bec331d3e"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_json(name: str) -> dict:
    path = RELEASE / name
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON {name}: {exc}")


def read_csv(name: str) -> list[dict[str, str]]:
    path = RELEASE / name
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    manifest = load_json("BATCH8E_PROMOTION_INPUT_MANIFEST.json")
    metrics = load_json("BATCH8E_CROSS_DOMAIN_METRICS_v1.0.0.json")
    validation = read_csv("BATCH8E_CROSS_DOMAIN_VALIDATION_v1.0.0.csv")
    unresolved = read_csv("UNRESOLVED_DEFERRED_QUEUE_SUMMARY_v1.0.0.csv")

    if manifest.get("source_release_sha256") != EXPECTED_SOURCE_SHA256:
        fail("source release SHA-256 differs from audited Batch 8E release")
    if manifest.get("repository_promotion_collection_sha256") != EXPECTED_ZIP_SHA256:
        fail("promotion manifest ZIP SHA-256 differs from governed value")
    if manifest.get("production_deployment_authorized") is not False:
        fail("repository promotion must not imply production deployment authority")
    if manifest.get("public_canon_completeness_claimed") is not False:
        fail("repository promotion must not claim Public Canon completeness")
    if int(manifest.get("r1_deferred_candidates", -1)) != 1671:
        fail("R1 deferred-candidate boundary changed")
    if manifest.get("r1_owner_decision") != "OPEN":
        fail("R1 owner-decision state must remain OPEN")

    if metrics.get("status") != "PORTABLE_RELEASE_CANDIDATE_ASSEMBLED_AND_VALIDATED":
        fail("unexpected Batch 8E portable release status")
    if int(metrics.get("validation_gates", -1)) != 22 or int(metrics.get("validation_failures", -1)) != 0:
        fail("Batch 8E metrics do not record 22 PASS gates / 0 failures")
    if metrics.get("repository_ingestion_claimed") is not False:
        fail("source release incorrectly claims repository ingestion")
    if metrics.get("public_canon_completeness_claimed") is not False:
        fail("source release incorrectly claims Public Canon completeness")

    if len(validation) != 22:
        fail(f"expected 22 validation rows; found {len(validation)}")
    bad = [r for r in validation if r.get("Result") != "PASS" or r.get("Severity") != "BLOCKING"]
    if bad:
        fail(f"Batch 8E validation contains non-PASS/non-BLOCKING gates: {bad[:3]}")
    expected_gates = {f"8E-G{i:02d}" for i in range(1, 23)}
    actual_gates = {r.get("Gate_ID") for r in validation}
    if actual_gates != expected_gates:
        fail("Batch 8E gate IDs are incomplete or unexpected")

    r1 = [r for r in unresolved if r.get("Queue") == "Canonical R1 formally deferred source candidates"]
    if len(r1) != 1 or r1[0].get("Count") != "1671" or r1[0].get("State") != "OWNER_DEFERRED_OPEN_DECISION":
        fail("unresolved queue does not preserve 1,671 R1 owner-deferred candidates")

    handoff = RELEASE / "BATCH8E_GOVERNED_REPOSITORY_PROMOTION_HANDOFF.md"
    closure = RELEASE / "BATCH8E_CROSS_DOMAIN_CONTENT_CLOSURE_REPORT_v1.6.0.md"
    for required in (handoff, closure):
        if not required.is_file():
            fail(f"missing required evidence file: {required.relative_to(ROOT)}")

    zip_path = RELEASE / ZIP_NAME
    if not zip_path.is_file():
        fail(
            f"exact promotion ZIP is not committed at {zip_path.relative_to(ROOT)}; "
            "handoff evidence alone is not completed repository promotion"
        )
    actual_zip_sha = sha256(zip_path)
    if actual_zip_sha != EXPECTED_ZIP_SHA256:
        fail(f"promotion ZIP SHA-256 mismatch: expected {EXPECTED_ZIP_SHA256}, got {actual_zip_sha}")

    print("PASS: Content v2 Batch 8E governed repository promotion")
    print(f"  promotion ZIP: {ZIP_NAME}")
    print(f"  SHA-256: {actual_zip_sha}")
    print("  portable gates: 22/22 PASS")
    print("  R1 deferred candidates: 1671 (owner decision OPEN)")
    print("  production deployment authorized: false")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as exc:
        print(f"FAIL: unexpected validator error: {exc}", file=sys.stderr)
        raise SystemExit(1)
