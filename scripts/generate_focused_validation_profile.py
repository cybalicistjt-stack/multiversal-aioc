#!/usr/bin/env python3
from __future__ import annotations

from typing import Any, Mapping


def build_profile(spec: Mapping[str, Any]) -> dict[str, Any]:
    work_item = str(spec["work_item"])
    compact = work_item.lower().replace("-", "")
    test_path = str(spec["test_path"])
    artifact_prefix = str(spec["artifact_prefix"])
    description = str(spec.get("description") or f"{work_item} focused validation.")
    boundary = str(spec.get("boundary") or f"{work_item} only.")
    linux_test = [
        "corepack", "pnpm", "--filter", "@multiversal/app-client-ui", "exec", "vitest", "run",
        test_path, "--maxWorkers=1", "--minWorkers=1",
    ]
    windows_test = [
        "cmd.exe", "/d", "/s", "/c",
        f"pnpm --filter @multiversal/app-client-ui exec vitest run {test_path} --maxWorkers=1 --minWorkers=1",
    ]
    return {
        "schema_version": "1.0.0",
        "profile_id": work_item,
        "work_item": work_item,
        "description": description,
        "preflight_required": True,
        "preflight_only": False,
        "artifact_prefix": artifact_prefix,
        "raw_evidence_required": True,
        "migrated_from": [],
        "steps": [
            {
                "id": "workspace-install",
                "timeout_seconds": 600,
                "commands": {
                    "linux": ["corepack", "pnpm", "install", "--no-frozen-lockfile", "--prefer-offline"],
                    "windows": ["cmd.exe", "/d", "/s", "/c", "pnpm install --no-frozen-lockfile --prefer-offline"],
                },
            },
            {
                "id": "client-typecheck",
                "timeout_seconds": 600,
                "commands": {
                    "linux": ["corepack", "pnpm", "--filter", "@multiversal/app-client-ui", "typecheck"],
                    "windows": ["cmd.exe", "/d", "/s", "/c", "pnpm --filter @multiversal/app-client-ui typecheck"],
                },
            },
            {
                "id": f"{compact}-focused-regression",
                "timeout_seconds": 900,
                "commands": {"linux": linux_test, "windows": windows_test},
            },
        ],
        "boundaries": [boundary],
    }
