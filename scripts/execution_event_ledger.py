#!/usr/bin/env python3
"""Hash-chained execution-event ledger and derived execution metrics.

Execution System v2 treats observed events as the source of truth for owner
interaction and latency facts. Checkpoints may project these values but may not
independently author them.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence


SCHEMA_VERSION = "1.0.0"


class EventLedgerError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise EventLedgerError(message)


def _parse_timestamp(value: Any) -> datetime:
    _require(isinstance(value, str) and bool(value.strip()), "timestamp must be a non-empty ISO-8601 string")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as exc:
        raise EventLedgerError(f"invalid ISO-8601 timestamp: {value!r}") from exc
    _require(parsed.tzinfo is not None and parsed.utcoffset() is not None, "timestamp must be offset-aware")
    return parsed


def _canonical_digest(event: Mapping[str, Any]) -> str:
    material = {key: value for key, value in event.items() if key != "event_digest"}
    payload = json.dumps(
        material,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _valid_digest(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(ch in "0123456789abcdef" for ch in value)
    )


def build_event(
    *,
    run_id: str,
    sequence: int,
    event_type: str,
    timestamp: str,
    source: str,
    payload: Mapping[str, Any] | None = None,
    previous_digest: str | None = None,
) -> dict[str, Any]:
    """Build one immutable execution event with a canonical SHA-256 digest."""
    _require(isinstance(run_id, str) and bool(run_id.strip()), "run_id must be non-empty")
    _require(isinstance(sequence, int) and not isinstance(sequence, bool) and sequence >= 1, "sequence must be a positive integer")
    _require(isinstance(event_type, str) and bool(event_type.strip()), "event_type must be non-empty")
    _require(isinstance(source, str) and bool(source.strip()), "source must be non-empty")
    _parse_timestamp(timestamp)
    _require(payload is None or isinstance(payload, Mapping), "payload must be an object")
    if sequence == 1:
        _require(previous_digest is None, "first event may not have previous_digest")
    else:
        _require(_valid_digest(previous_digest), "non-first event requires a valid previous_digest")

    event: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "event_id": f"{run_id}:{sequence:06d}",
        "run_id": run_id,
        "sequence": sequence,
        "timestamp": timestamp,
        "event_type": event_type,
        "source": source,
        "payload": dict(payload or {}),
        "previous_digest": previous_digest,
    }
    event["event_digest"] = _canonical_digest(event)
    return event


def validate_chain(events: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Validate identity, chronology, linkage and digest integrity for a run."""
    _require(isinstance(events, Sequence) and not isinstance(events, (str, bytes)), "events must be an array")
    _require(len(events) > 0, "events must not be empty")

    run_id: str | None = None
    prior_digest: str | None = None
    prior_time: datetime | None = None
    seen_ids: set[str] = set()

    for index, raw in enumerate(events, start=1):
        _require(isinstance(raw, Mapping), f"event {index} must be an object")
        event = dict(raw)
        current_run = event.get("run_id")
        _require(isinstance(current_run, str) and bool(current_run.strip()), f"event {index}: invalid run_id")
        if run_id is None:
            run_id = current_run
        _require(current_run == run_id, f"event {index}: run_id changed within ledger")
        _require(event.get("schema_version") == SCHEMA_VERSION, f"event {index}: schema_version mismatch")
        _require(event.get("sequence") == index, f"event {index}: non-contiguous sequence")
        expected_id = f"{run_id}:{index:06d}"
        _require(event.get("event_id") == expected_id, f"event {index}: event_id mismatch")
        _require(expected_id not in seen_ids, f"event {index}: duplicate event_id")
        seen_ids.add(expected_id)
        _require(isinstance(event.get("event_type"), str) and bool(str(event.get("event_type")).strip()), f"event {index}: invalid event_type")
        _require(isinstance(event.get("source"), str) and bool(str(event.get("source")).strip()), f"event {index}: invalid source")
        _require(isinstance(event.get("payload"), Mapping), f"event {index}: payload must be an object")

        observed_time = _parse_timestamp(event.get("timestamp"))
        if prior_time is not None:
            _require(observed_time >= prior_time, f"event {index}: timestamp moved backwards")
        prior_time = observed_time

        if index == 1:
            _require(event.get("previous_digest") is None, "first event must not link to a previous digest")
        else:
            _require(event.get("previous_digest") == prior_digest, f"event {index}: previous_digest mismatch")

        observed_digest = event.get("event_digest")
        _require(_valid_digest(observed_digest), f"event {index}: invalid event_digest")
        expected_digest = _canonical_digest(event)
        _require(observed_digest == expected_digest, f"event {index}: event digest mismatch")
        prior_digest = observed_digest

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "PASS",
        "run_id": run_id,
        "event_count": len(events),
        "head_digest": prior_digest,
    }


def _events_of_type(events: Sequence[Mapping[str, Any]], event_type: str) -> list[Mapping[str, Any]]:
    return [event for event in events if event.get("event_type") == event_type]


def derive_metrics(events: Sequence[Mapping[str, Any]], *, latency_slo_minutes: float = 24.0) -> dict[str, Any]:
    """Derive interaction and owner-visible latency facts from the event chain."""
    chain = validate_chain(events)
    _require(
        isinstance(latency_slo_minutes, (int, float))
        and not isinstance(latency_slo_minutes, bool)
        and float(latency_slo_minutes) > 0,
        "latency_slo_minutes must be a positive number",
    )
    starts = _events_of_type(events, "run_started")
    completions = _events_of_type(events, "run_completed")
    _require(len(starts) == 1, "completed-run metrics require exactly one run_started event")
    _require(len(completions) == 1, "completed-run metrics require exactly one run_completed event")

    started_at = _parse_timestamp(starts[0].get("timestamp"))
    completed_at = _parse_timestamp(completions[0].get("timestamp"))
    _require(completed_at >= started_at, "run_completed precedes run_started")

    owner_continue_count = len(_events_of_type(events, "owner_continue"))
    owner_stall_nudge_count = len(_events_of_type(events, "owner_stall_nudge"))
    execution_incident_count = len(_events_of_type(events, "execution_incident"))
    wall_minutes = (completed_at - started_at).total_seconds() / 60.0
    slo = float(latency_slo_minutes)
    overrun = max(wall_minutes - slo, 0.0)

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "PASS",
        "run_id": chain["run_id"],
        "ledger_head_digest": chain["head_digest"],
        "owner_continue_count": owner_continue_count,
        "owner_stall_nudge_count": owner_stall_nudge_count,
        "execution_incident_count": execution_incident_count,
        "single_continue_achieved": (
            owner_continue_count == 1
            and owner_stall_nudge_count == 0
            and execution_incident_count == 0
        ),
        "owner_visible_wall_minutes": wall_minutes,
        "latency_slo_minutes": slo,
        "latency_slo_status": "within_slo" if wall_minutes <= slo else "missed",
        "latency_slo_overrun_minutes": overrun,
    }


def _load_events(path: Path) -> list[dict[str, Any]]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise EventLedgerError(f"unable to load ledger {path}: {exc}") from exc
    if isinstance(value, dict):
        value = value.get("events")
    _require(isinstance(value, list), "ledger JSON must be an event array or object containing events")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Multiversal execution event ledger")
    parser.add_argument("ledger")
    parser.add_argument("--derive-metrics", action="store_true")
    parser.add_argument("--latency-slo-minutes", type=float, default=24.0)
    args = parser.parse_args()
    try:
        events = _load_events(Path(args.ledger))
        result = (
            derive_metrics(events, latency_slo_minutes=args.latency_slo_minutes)
            if args.derive_metrics
            else validate_chain(events)
        )
    except EventLedgerError as exc:
        result = {"schema_version": SCHEMA_VERSION, "status": "FAIL", "error": str(exc)}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
