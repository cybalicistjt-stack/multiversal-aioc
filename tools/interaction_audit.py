#!/usr/bin/env python3
"""Validate public, redacted Multiversal interaction-audit artifacts."""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

SOURCE_HASH = "eba9af96055c7a2d7f1bda3823440bc2a7c623ea34a77a6bc5b536d7e3d996a6"
FORBIDDEN_KEYS = {
    "text", "raw_text", "verbatim_text", "quote", "source_file",
    "conversation_title", "attachment_content", "credential", "token",
}
FORBIDDEN_STRINGS = ("Conversation/", ".mht", "sk-proj-", "ghp_", "github_pat_")
EPISODE_RE = re.compile(r"^MV-EP-\d{3}$")
PATTERN_RE = re.compile(r"^MV-(FRIC|SUCC)-[A-Z]+-\d{3}$")
CASE_RE = re.compile(r"^MV-EVAL-\d{3}$")


class AuditError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuditError(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise AuditError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise AuditError(f"invalid JSON in {path}: {exc}") from exc


def load_jsonl(path: Path) -> list[dict]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError as exc:
        raise AuditError(f"missing file: {path}") from exc
    records = []
    for line_number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise AuditError(f"invalid JSONL in {path}:{line_number}: {exc}") from exc
    return records


def walk(value, path="root"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield path, key, child
            yield from walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


def validate_privacy(name: str, value) -> None:
    serialized = json.dumps(value, ensure_ascii=False)
    for path, key, _ in walk(value):
        require(key not in FORBIDDEN_KEYS, f"{name}: forbidden key {key!r} at {path}")
    for forbidden in FORBIDDEN_STRINGS:
        require(forbidden not in serialized, f"{name}: forbidden string {forbidden!r}")


def validate(root: Path) -> None:
    analysis = root / "governance/ai/interaction-system/analysis"
    evaluation = root / "governance/ai/interaction-system/evaluation"

    source = load_json(analysis / "SOURCE_CORPUS_REFERENCE.json")
    friction = load_json(analysis / "FAILURE_FRICTION_TAXONOMY.json")
    success = load_json(analysis / "SUCCESS_PATTERN_CATALOG.json")
    privacy = load_json(analysis / "PRIVACY_REVIEW.json")
    episodes = load_jsonl(analysis / "REDACTED_EPISODE_INDEX.jsonl")
    cases_doc = load_json(evaluation / "EVALUATION_CASES.json")
    cases = cases_doc.get("cases", [])

    for name, value in {
        "source": source, "friction": friction, "success": success,
        "privacy": privacy, "episodes": episodes, "evaluation": cases_doc,
    }.items():
        validate_privacy(name, value)

    require(source.get("source_package_sha256") == SOURCE_HASH, "source package hash mismatch")
    require(source.get("conversation_count") == 9, "unexpected conversation count")
    require(source.get("message_count") == 114, "unexpected message count")
    conversation_counts = {
        item["conversation_id"]: item["message_count"]
        for item in source.get("conversations", [])
    }
    require(len(conversation_counts) == source["conversation_count"], "conversation reference count mismatch")
    require(sum(conversation_counts.values()) == source["message_count"], "message reference count mismatch")

    all_patterns = friction.get("patterns", []) + success.get("patterns", [])
    pattern_ids = [item.get("pattern_id") for item in all_patterns]
    require(len(pattern_ids) == len(set(pattern_ids)), "duplicate pattern ID")
    require(all(PATTERN_RE.fullmatch(item or "") for item in pattern_ids), "invalid pattern ID")
    require(len(friction.get("patterns", [])) == 12, "unexpected friction taxonomy size")
    require(len(success.get("patterns", [])) == 10, "unexpected success catalog size")

    episode_ids = [item.get("episode_id") for item in episodes]
    require(len(episodes) == 27, "unexpected episode count")
    require(len(episode_ids) == len(set(episode_ids)), "duplicate episode ID")
    require(all(EPISODE_RE.fullmatch(item or "") for item in episode_ids), "invalid episode ID")
    occurrence_counts = Counter()
    for episode in episodes:
        require(episode.get("source_package_sha256") == SOURCE_HASH, f"{episode.get('episode_id')}: source hash mismatch")
        require(episode.get("verbatim_content_included") is False, f"{episode.get('episode_id')}: verbatim flag must be false")
        conversation_id = episode.get("conversation_id")
        require(conversation_id in conversation_counts, f"{episode.get('episode_id')}: unknown conversation")
        message_range = episode.get("message_range", {})
        start, end = message_range.get("start"), message_range.get("end")
        require(isinstance(start, int) and isinstance(end, int) and 1 <= start <= end <= conversation_counts[conversation_id], f"{episode.get('episode_id')}: invalid message range")
        require(episode.get("severity") in {"low", "medium", "high", "critical"}, f"{episode.get('episode_id')}: invalid severity")
        require(isinstance(episode.get("owner_intervention_required"), bool), f"{episode.get('episode_id')}: intervention flag invalid")
        require(0 < len(episode.get("trigger_summary", "")) <= 500, f"{episode.get('episode_id')}: trigger summary length")
        require(0 < len(episode.get("assistant_behavior_summary", "")) <= 500, f"{episode.get('episode_id')}: behavior summary length")
        refs = episode.get("pattern_ids", [])
        require(refs and len(refs) == len(set(refs)), f"{episode.get('episode_id')}: pattern references invalid")
        for pattern_id in refs:
            require(pattern_id in pattern_ids, f"{episode.get('episode_id')}: unknown pattern {pattern_id}")
            occurrence_counts[pattern_id] += 1

    for pattern in all_patterns:
        require(pattern.get("episode_count") == occurrence_counts[pattern["pattern_id"]], f"{pattern['pattern_id']}: episode count mismatch")
        basis = pattern.get("evidence_basis")
        require(basis in {"archive_episodes", "owner_approved_control"}, f"{pattern['pattern_id']}: invalid evidence basis")
        if pattern.get("episode_count", 0) == 0:
            require(basis == "owner_approved_control", f"{pattern['pattern_id']}: unsupported pattern")
        else:
            require(basis == "archive_episodes", f"{pattern['pattern_id']}: archive evidence basis required")

    case_ids = [item.get("case_id") for item in cases]
    require(len(cases) == 15, "unexpected evaluation case count")
    require(len(case_ids) == len(set(case_ids)), "duplicate evaluation case ID")
    require(all(CASE_RE.fullmatch(item or "") for item in case_ids), "invalid evaluation case ID")
    covered_patterns = set()
    for case in cases:
        refs = case.get("source_patterns", [])
        require(refs and len(refs) == len(set(refs)), f"{case.get('case_id')}: source patterns invalid")
        for pattern_id in refs:
            require(pattern_id in pattern_ids, f"{case.get('case_id')}: unknown pattern {pattern_id}")
            covered_patterns.add(pattern_id)
        require(case.get("expected_actions"), f"{case.get('case_id')}: expected actions missing")
        require(case.get("prohibited_actions"), f"{case.get('case_id')}: prohibited actions missing")
        require(case.get("pass_condition"), f"{case.get('case_id')}: pass condition missing")
    require(set(pattern_ids) <= covered_patterns, f"evaluation coverage missing: {sorted(set(pattern_ids) - covered_patterns)}")

    require(privacy.get("source_package_sha256") == SOURCE_HASH, "privacy source hash mismatch")
    require(privacy.get("review_result") == "pass", "privacy review did not pass")
    checks = privacy.get("checks", {})
    require(checks.get("raw_message_fields_present") is False, "raw fields reported present")
    require(checks.get("source_filenames_present") is False, "source filenames reported present")
    require(checks.get("conversation_titles_present") is False, "conversation titles reported present")
    overlap = checks.get("exact_contiguous_token_overlap", {})
    require(overlap.get("minimum_sequence_length_reviewed") == 8, "privacy overlap threshold changed")
    require(overlap.get("matches_found") == 0, "privacy overlap matches found")

    require((analysis / "REDACTION_AND_MINIMIZATION_CONTRACT.md").is_file(), "redaction contract missing")
    require((analysis / "INTERACTION_AUDIT_SUMMARY.md").is_file(), "audit summary missing")
    require((analysis / "REDACTED_EPISODE.schema.json").is_file(), "episode schema missing")
    require((evaluation / "EVALUATION_CASE.schema.json").is_file(), "evaluation schema missing")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("validate",))
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    try:
        validate(Path(args.root).resolve())
    except (AuditError, OSError) as exc:
        print(f"Interaction audit validation error: {exc}", file=sys.stderr)
        return 1
    print("Interaction audit validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
