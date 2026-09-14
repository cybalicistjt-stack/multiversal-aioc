#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Mapping

import execution_transaction_preflight as preflight

HEX40 = re.compile(r"^[0-9a-f]{40}$")


class MergeAuthorizationError(RuntimeError):
    pass


def _canonical_digest(payload: Mapping[str, Any]) -> str:
    material = {key: value for key, value in payload.items() if key != "authorization_digest"}
    raw = json.dumps(material, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def authorize_merge_effect(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    repository = str(snapshot.get("repository") or "").strip()
    head_sha = str(snapshot.get("head_sha") or "").strip().lower()
    if "/" not in repository:
        raise preflight.TransactionPreflightError("repository must be owner/name")
    if not HEX40.fullmatch(head_sha):
        raise preflight.TransactionPreflightError("head_sha must be an exact 40-character lowercase hexadecimal SHA")

    selected = preflight.select_merge_method(snapshot, snapshot.get("requested_method"))
    if selected["decision"] != "USE_MERGE_METHOD":
        return {
            **selected,
            "repository": repository,
            "expected_head_sha": head_sha,
            "authorization_digest": None,
        }

    receipt: dict[str, Any] = {
        "schema_version": "1.0.0",
        "decision": "MERGE_AUTHORIZED",
        "repository": repository,
        "expected_head_sha": head_sha,
        "merge_method": selected["merge_method"],
        "supported_methods": selected["supported_methods"],
    }
    receipt["authorization_digest"] = _canonical_digest(receipt)
    return receipt


def validate_merge_invocation(receipt: Mapping[str, Any], invocation: Mapping[str, Any]) -> dict[str, Any]:
    if receipt.get("decision") != "MERGE_AUTHORIZED":
        raise MergeAuthorizationError("receipt does not authorize a merge")
    digest = str(receipt.get("authorization_digest") or "")
    if len(digest) != 64 or digest != _canonical_digest(receipt):
        raise MergeAuthorizationError("merge authorization digest mismatch")
    expected = {
        "repository": receipt.get("repository"),
        "expected_head_sha": receipt.get("expected_head_sha"),
        "merge_method": receipt.get("merge_method"),
    }
    observed = {
        "repository": invocation.get("repository"),
        "expected_head_sha": invocation.get("expected_head_sha"),
        "merge_method": invocation.get("merge_method"),
    }
    if observed != expected:
        raise MergeAuthorizationError(f"merge invocation drift: expected {expected!r}, observed {observed!r}")
    return {"status": "PASS", **expected}


def main() -> int:
    parser = argparse.ArgumentParser(description="Bind a PR merge to fresh repository capabilities and one exact head")
    parser.add_argument("snapshot")
    args = parser.parse_args()
    data = json.loads(Path(args.snapshot).read_text(encoding="utf-8"))
    result = authorize_merge_effect(data)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "MERGE_AUTHORIZED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
