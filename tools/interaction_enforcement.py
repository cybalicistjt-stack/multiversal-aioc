#!/usr/bin/env python3
"""Validate Multiversal interaction policy coverage and typed control receipts."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PATTERN_RE = re.compile(r"^MV-(FRIC|SUCC)-[A-Z]+-[0-9]{3}$")
CASE_RE = re.compile(r"^MV-EVAL-[0-9]{3}$")
RECEIPT_RE = re.compile(r"^MV-ICR-[0-9]{3}$")
CONTROL_TYPES = {
    "deliverable", "capability", "source_coverage", "ui_verification",
    "notification", "request_alignment", "owner_report",
}
COVERAGE_STATES = {"enforced", "enforced_elsewhere", "partial", "target_enforced"}
CONTROL_STATES = {
    "enforced", "enforced_elsewhere", "partially_enforced",
    "policy_and_repository_enforced", "implemented_in_mv_cont_003",
}
PROJECT_BIBLE_ALIASES = {
    "MULTIVERSAL_PROJECT_BIBLE_v2.0.md": "MULTIVERSAL_PROJECT_BIBLE_v2.0_CANONICAL_RELEASE.md"
}


class EnforcementError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise EnforcementError(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise EnforcementError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise EnforcementError(f"invalid JSON in {path}: {exc}") from exc


def artifact_exists(root: Path, path: str) -> bool:
    actual = PROJECT_BIBLE_ALIASES.get(path, path)
    return (root / actual).is_file()


def validate_receipt(receipt: dict) -> None:
    required = {
        "schema_version", "receipt_id", "control_type", "work_item_id",
        "created_at", "status", "details", "evidence",
    }
    require(required <= set(receipt), f"receipt missing fields: {sorted(required - set(receipt))}")
    require(receipt["schema_version"] == "1.0.0", "receipt schema version mismatch")
    require(RECEIPT_RE.fullmatch(receipt["receipt_id"]) is not None, "invalid receipt ID")
    require(receipt["control_type"] in CONTROL_TYPES, "invalid control type")
    require(receipt["status"] in {"pass", "fail", "send", "suppress"}, "invalid receipt status")
    require(isinstance(receipt["details"], dict), "receipt details must be an object")
    require(isinstance(receipt["evidence"], list), "receipt evidence must be an array")

    details = receipt["details"]
    control_type = receipt["control_type"]
    status = receipt["status"]

    if control_type == "deliverable":
        for key in ("artifact_id", "locator", "locator_kind", "exists_verified", "user_accessible_verified", "bytes_verified"):
            require(key in details, f"deliverable receipt missing {key}")
        if status == "pass":
            require(details["exists_verified"] is True, "deliverable existence not verified")
            require(details["user_accessible_verified"] is True, "deliverable is not owner-accessible")
            require(details["bytes_verified"] is True, "deliverable bytes not verified")
            require(bool(details.get("checksum") or details.get("immutable_identity")), "deliverable immutable identity missing")
            require(receipt["evidence"], "deliverable evidence missing")

    elif control_type == "capability":
        for key in (
            "owner_authorized", "actor_identity_verified", "contributor_authority",
            "connector_available", "repository_permission_verified",
            "operation_attempted", "operation_succeeded",
        ):
            require(key in details, f"capability receipt missing {key}")
        if status == "pass":
            require(details["owner_authorized"] is True, "owner authorization not verified")
            require(details["actor_identity_verified"] is True, "actor identity not verified")
            require(details["connector_available"] is True, "connector unavailable")
            require(details["repository_permission_verified"] is True, "repository permission not verified")
            require(details["operation_attempted"] is True and details["operation_succeeded"] is True, "operation success not verified")
            require(receipt["evidence"], "capability evidence missing")
        if details["operation_succeeded"]:
            require(details["operation_attempted"], "successful operation was not attempted")
            require(details["connector_available"], "successful operation lacks connector availability")

    elif control_type == "source_coverage":
        for key in (
            "required_sources", "evaluated_sources", "missing_sources",
            "deferred_sources", "completion_allowed",
        ):
            require(key in details, f"source coverage receipt missing {key}")
        required_sources = set(details["required_sources"])
        evaluated_sources = set(details["evaluated_sources"])
        missing_sources = set(details["missing_sources"])
        deferred_sources = set(details["deferred_sources"])
        require(missing_sources == required_sources - evaluated_sources - deferred_sources, "source coverage sets are inconsistent")
        if status == "pass" and details["completion_allowed"]:
            require(not missing_sources and not deferred_sources, "completion allowed with missing or deferred sources")
            require(required_sources <= evaluated_sources, "required sources were not evaluated")
            require(receipt["evidence"], "source coverage evidence missing")

    elif control_type == "ui_verification":
        for key in (
            "guidance_subject", "verification_method", "observed_current_ui",
            "official_source_current", "verified_label_allowed",
        ):
            require(key in details, f"UI verification receipt missing {key}")
        verified = details["observed_current_ui"] or details["official_source_current"]
        if status == "pass":
            require(verified, "UI guidance has no current verification")
            require(details["verified_label_allowed"] is True, "verified UI label is not allowed")
            require(receipt["evidence"], "UI verification evidence missing")
        if details["verified_label_allowed"]:
            require(verified, "UI guidance labeled verified without current evidence")

    elif control_type == "notification":
        for key in (
            "dedupe_key", "evidence_fingerprint", "previous_evidence_fingerprint",
            "material_change", "decision",
        ):
            require(key in details, f"notification receipt missing {key}")
        same = details["evidence_fingerprint"] == details["previous_evidence_fingerprint"]
        if same and not details["material_change"]:
            require(status == "suppress" and details["decision"] == "suppress", "unchanged notification was not suppressed")
        if status == "send":
            require(details["material_change"] or not same, "notification sent without fresh evidence")
            require(details["decision"] == "send", "notification send decision mismatch")

    elif control_type == "request_alignment":
        for key in (
            "primary_request_mode", "secondary_request_modes", "immediate_question",
            "direct_answer_status", "related_execution_status",
        ):
            require(key in details, f"request alignment receipt missing {key}")
        if status == "pass" and details["primary_request_mode"] in {
            "decision_support", "comparison", "estimate", "verification", "status"
        }:
            require(details["immediate_question"], "immediate question missing")
            require(details["direct_answer_status"] == "provided", "immediate question was not answered")

    elif control_type == "owner_report":
        for key in ("completed", "evidence_summary", "remaining", "owner_decision", "next_action"):
            require(key in details and isinstance(details[key], str) and details[key].strip(), f"owner report missing {key}")
        if status == "pass":
            require(receipt["evidence"], "owner report evidence missing")


def validate(root: Path) -> None:
    base = root / "governance/ai/interaction-system"
    enforcement = base / "enforcement"
    friction = load_json(base / "analysis/FAILURE_FRICTION_TAXONOMY.json")
    success = load_json(base / "analysis/SUCCESS_PATTERN_CATALOG.json")
    evaluations = load_json(base / "evaluation/EVALUATION_CASES.json")
    matrix = load_json(enforcement / "CONTROL_COVERAGE_MATRIX.json")
    gaps = load_json(enforcement / "CONTROL_GAP_REGISTER.json")
    evaluation_map = load_json(enforcement / "EVALUATION_CONTROL_MAP.json")
    examples = load_json(enforcement / "CONTROL_RECEIPT.examples.json")

    require(matrix.get("schema_version") == "1.0.0", "coverage matrix schema mismatch")
    require(matrix.get("work_item_id") == "MV-CONT-003", "coverage matrix work item mismatch")
    authorities = matrix.get("authority_catalog", {})
    controls = matrix.get("control_catalog", {})
    coverage = matrix.get("pattern_coverage", [])
    require(authorities, "authority catalog is empty")
    require(controls, "control catalog is empty")

    for authority_id, authority in authorities.items():
        require(authority.get("document") and authority.get("section"), f"authority incomplete: {authority_id}")
        require(artifact_exists(root, authority["document"]), f"authority document missing: {authority['document']}")

    for control_id, control in controls.items():
        require(control.get("status") in CONTROL_STATES, f"invalid control state: {control_id}")
        artifacts = control.get("artifacts", [])
        require(artifacts, f"control artifacts missing: {control_id}")
        for artifact in artifacts:
            require(artifact_exists(root, artifact), f"control artifact missing: {control_id} -> {artifact}")

    taxonomy_patterns = friction.get("patterns", []) + success.get("patterns", [])
    pattern_ids = {item["pattern_id"] for item in taxonomy_patterns}
    coverage_ids = [item.get("pattern_id") for item in coverage]
    require(len(pattern_ids) == 22, "unexpected taxonomy pattern count")
    require(len(coverage_ids) == len(set(coverage_ids)), "duplicate pattern coverage")
    require(set(coverage_ids) == pattern_ids, f"pattern coverage mismatch: {sorted(pattern_ids ^ set(coverage_ids))}")

    for item in coverage:
        pattern_id = item["pattern_id"]
        require(PATTERN_RE.fullmatch(pattern_id) is not None, f"invalid pattern ID: {pattern_id}")
        require(item.get("coverage_status") in COVERAGE_STATES, f"invalid coverage state: {pattern_id}")
        require(item.get("priority") in {"P0", "P1", "P2", "P3"}, f"invalid priority: {pattern_id}")
        require(item.get("authority_ids"), f"authority missing: {pattern_id}")
        for authority_id in item["authority_ids"]:
            require(authority_id in authorities, f"unknown authority: {pattern_id} -> {authority_id}")
        referenced_controls = item.get("existing_control_ids", []) + item.get("target_control_ids", [])
        require(referenced_controls, f"control coverage missing: {pattern_id}")
        for control_id in referenced_controls:
            require(control_id in controls, f"unknown control: {pattern_id} -> {control_id}")
        if item["coverage_status"] == "target_enforced":
            require(item.get("target_control_ids"), f"target control missing: {pattern_id}")
            for control_id in item["target_control_ids"]:
                require(controls[control_id]["status"] == "implemented_in_mv_cont_003", f"target control not implemented: {control_id}")

    gap_items = gaps.get("gaps", [])
    gap_ids = [item.get("gap_id") for item in gap_items]
    require(len(gap_ids) == len(set(gap_ids)), "duplicate gap ID")
    require(gaps.get("summary", {}).get("gap_count") == len(gap_items), "gap count mismatch")
    implemented_count = 0
    deferred_count = 0
    for gap in gap_items:
        require(gap.get("priority") in {"P0", "P1", "P2", "P3"}, f"invalid gap priority: {gap.get('gap_id')}")
        for pattern_id in gap.get("pattern_ids", []):
            require(pattern_id in pattern_ids, f"gap references unknown pattern: {pattern_id}")
        control_id = gap.get("implemented_control_id")
        if control_id is None:
            deferred_count += 1
        else:
            implemented_count += 1
            require(control_id in controls, f"gap references unknown control: {control_id}")
            require(controls[control_id]["status"] == "implemented_in_mv_cont_003", f"gap control not implemented: {control_id}")
        require(gap.get("residual_risk") and gap.get("next_hardening"), f"gap risk or hardening missing: {gap.get('gap_id')}")
    require(gaps["summary"].get("implemented_in_mv_cont_003") == implemented_count, "implemented gap count mismatch")
    require(gaps["summary"].get("deferred") == deferred_count, "deferred gap count mismatch")

    evaluation_ids = {item["case_id"] for item in evaluations.get("cases", [])}
    mapped = evaluation_map.get("cases", [])
    mapped_ids = [item.get("case_id") for item in mapped]
    require(len(evaluation_ids) == 15, "unexpected evaluation case count")
    require(len(mapped_ids) == len(set(mapped_ids)), "duplicate evaluation control mapping")
    require(set(mapped_ids) == evaluation_ids, f"evaluation mapping mismatch: {sorted(evaluation_ids ^ set(mapped_ids))}")
    for item in mapped:
        require(CASE_RE.fullmatch(item["case_id"]) is not None, f"invalid evaluation case ID: {item['case_id']}")
        require(item.get("control_ids"), f"evaluation controls missing: {item['case_id']}")
        for control_id in item["control_ids"]:
            require(control_id in controls, f"evaluation references unknown control: {item['case_id']} -> {control_id}")

    receipts = examples.get("receipts", [])
    receipt_ids = [item.get("receipt_id") for item in receipts]
    require(len(receipt_ids) == len(set(receipt_ids)), "duplicate receipt ID")
    require({item.get("control_type") for item in receipts} == CONTROL_TYPES, "receipt examples do not cover every control type")
    for receipt in receipts:
        validate_receipt(receipt)

    for required_path in (
        enforcement / "README.md",
        enforcement / "PROJECT_BIBLE_TRACEABILITY.md",
        enforcement / "CONTROL_RECEIPT.schema.json",
    ):
        require(required_path.is_file(), f"required enforcement file missing: {required_path}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("validate", "validate-receipt"))
    parser.add_argument("path", nargs="?")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    try:
        if args.command == "validate":
            validate(Path(args.root).resolve())
            print("Interaction enforcement validation: PASS")
        else:
            require(args.path is not None, "validate-receipt requires a JSON path")
            validate_receipt(load_json(Path(args.path)))
            print("Interaction control receipt validation: PASS")
    except (EnforcementError, OSError) as exc:
        print(f"Interaction enforcement validation error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
