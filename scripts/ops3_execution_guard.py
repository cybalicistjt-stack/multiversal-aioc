#!/usr/bin/env python3
"""Operations V3 execution response and conformance guard.

This module validates execution evidence only. It never selects work, grants
implementation authority, or replaces operations/CURRENT.json.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

NONTERMINAL = "OPS3.NONTERMINAL_RESPONSE"
MULTI_CONTINUE = "OPS3.MULTI_CONTINUE_UNRECORDED"
STALL_NUDGE = "OPS3.STALL_NUDGE_UNRECORDED"
INVALID_BLOCKER = "OPS3.INVALID_BLOCKER"

_ALLOWED_BLOCKERS = {"owner_only", "external_blocker"}
_ALLOWED_TERMINAL_REASONS = {"completed", *_ALLOWED_BLOCKERS}


def _guard(checkpoint: dict[str, Any]) -> dict[str, Any]:
    value = checkpoint.get("execution_guard", {})
    return value if isinstance(value, dict) else {}


def _conformance(checkpoint: dict[str, Any]) -> dict[str, Any]:
    value = checkpoint.get("execution_conformance", {})
    return value if isinstance(value, dict) else {}


def _violations(checkpoint: dict[str, Any]) -> set[str]:
    raw = _conformance(checkpoint).get("policy_violations", [])
    return {str(value) for value in raw} if isinstance(raw, list) else set()


def _valid_stop_reason(value: Any) -> bool:
    if not isinstance(value, dict):
        return False
    kind = value.get("kind")
    evidence = value.get("evidence")
    return kind in _ALLOWED_TERMINAL_REASONS and isinstance(evidence, str) and bool(evidence.strip())


def validate_terminal_response(checkpoint: dict[str, Any]) -> list[str]:
    """Return violations for a proposed terminal assistant response."""
    errors: list[str] = []
    status = checkpoint.get("status")
    guard = _guard(checkpoint)
    allowed = guard.get("terminal_response_allowed") is True
    stop_reason = guard.get("stop_reason")

    if status == "in_progress":
        if not allowed:
            errors.append(NONTERMINAL)
        elif not _valid_stop_reason(stop_reason) or stop_reason.get("kind") not in _ALLOWED_BLOCKERS:
            errors.append(INVALID_BLOCKER)
    elif status == "completed_verified":
        if not allowed or not _valid_stop_reason(stop_reason) or stop_reason.get("kind") != "completed":
            errors.append(NONTERMINAL)
    elif status == "selected_not_started":
        # A selection-only state may be reported, but it is not a terminal result of an
        # already-started bounded Continue.
        if guard.get("continue_turns", 0):
            errors.append(NONTERMINAL)
    else:
        errors.append(NONTERMINAL)
    return errors


def validate_execution_conformance(checkpoint: dict[str, Any]) -> list[str]:
    """Prevent owner-interaction evidence from being certified as clean when it is not."""
    errors: list[str] = []
    guard = _guard(checkpoint)
    violations = _violations(checkpoint)
    conformance_status = _conformance(checkpoint).get("status")
    continue_turns = guard.get("continue_turns", 0)
    stall_nudges = guard.get("stall_nudges", 0)

    if not isinstance(continue_turns, int) or continue_turns < 0:
        errors.append(MULTI_CONTINUE)
    elif continue_turns > 1 and MULTI_CONTINUE not in violations and conformance_status in {"completed_verified", "conforming"}:
        errors.append(MULTI_CONTINUE)

    if not isinstance(stall_nudges, int) or stall_nudges < 0:
        errors.append(STALL_NUDGE)
    elif stall_nudges > 0 and STALL_NUDGE not in violations and conformance_status in {"completed_verified", "conforming"}:
        errors.append(STALL_NUDGE)

    return errors


def validate_checkpoint(checkpoint: dict[str, Any], *, terminal_response: bool = False) -> list[str]:
    errors = validate_execution_conformance(checkpoint)
    if terminal_response:
        errors.extend(validate_terminal_response(checkpoint))
    return sorted(set(errors))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("checkpoint")
    parser.add_argument("--terminal-response", action="store_true")
    args = parser.parse_args()
    checkpoint = json.loads(Path(args.checkpoint).read_text(encoding="utf-8"))
    errors = validate_checkpoint(checkpoint, terminal_response=args.terminal_response)
    print(json.dumps({"status": "FAIL" if errors else "PASS", "errors": errors}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
