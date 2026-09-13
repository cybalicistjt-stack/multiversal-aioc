#!/usr/bin/env python3
from __future__ import annotations

from typing import Any, Mapping


def authorize_context_access(
    manifest: Mapping[str, Any], *, path: str | None, operation: str
) -> dict[str, Any]:
    allowed_paths = {str(value) for value in manifest.get("allowed_paths", [])}
    diagnostic_mode = manifest.get("diagnostic_mode") is True
    failure_signature = str(manifest.get("failure_signature") or "").strip()

    if operation == "read" and path in allowed_paths:
        return {"decision": "ALLOW_DECLARED_INPUT", "path": path}
    if diagnostic_mode and failure_signature and operation in {"read", "repository_search"}:
        return {
            "decision": "ALLOW_DIAGNOSTIC_EXPANSION",
            "path": path,
            "failure_signature": failure_signature,
        }
    return {
        "decision": "DENY_UNDECLARED_INPUT",
        "path": path,
        "operation": operation,
    }
