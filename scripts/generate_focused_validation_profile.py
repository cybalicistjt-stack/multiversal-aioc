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
                "failure": {
                    "layer": "TOOLCHAIN",
                    "reason_code": "TOOLCHAIN.DEPENDENCY_INSTALL_FAILURE",
                    "feature_blame": "no",
                    "responsibility": "toolchain",
                    "blame_rationale": f"Dependency installation prepares the runner for bounded {work_item} validation.",
                    "remediation": f"Repair runner/toolchain only; do not weaken {work_item} acceptance.",
                },
            },
            {
                "id": "client-typecheck",
                "timeout_seconds": 600,
                "commands": {
                    "linux": ["corepack", "pnpm", "--filter", "@multiversal/app-client-ui", "typecheck"],
                    "windows": ["cmd.exe", "/d", "/s", "/c", "pnpm --filter @multiversal/app-client-ui typecheck"],
                },
                "failure": {
                    "layer": "BUILD",
                    "reason_code": "BUILD.COMPILE_FAILURE",
                    "feature_blame": "yes",
                    "responsibility": "feature",
                    "blame_rationale": f"The bounded {work_item} contract and focused regression must compile before successor work begins.",
                    "remediation": f"Repair bounded {work_item} typing only.",
                },
            },
            {
                "id": f"{compact}-focused-regression",
                "timeout_seconds": 900,
                "commands": {"linux": linux_test, "windows": windows_test},
                "failure": {
                    "layer": "TEST_UNIT",
                    "reason_code": "TEST_UNIT.ASSERTION_FAILURE",
                    "feature_blame": "undetermined",
                    "responsibility": "undetermined",
                    "blame_rationale": f"The focused {work_item} behavior contract must pass on the exact candidate head.",
                    "remediation": f"Repair {work_item} only; do not begin successor work.",
                },
            },
        ],
        "boundaries": [boundary],
    }
