#!/usr/bin/env python3
"""Keep closed PPIA feature workflows from firing on generic live-state projection changes."""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
KEEP_RUNTIME = {"validate-ppia-program.yml"}
GENERIC_RUNTIME_PATHS = {
    "governance/ai/runtime/CURRENT_WORK_POINTER.json",
    "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json",
}


def ppi_feature_workflows() -> list[Path]:
    return sorted(
        path
        for path in WORKFLOWS.glob("validate-ppia-*.yml")
        if path.name not in KEEP_RUNTIME
    )


def forbidden_lines(text: str) -> list[str]:
    hits = []
    for line in text.splitlines():
        stripped = line.strip().strip("'").strip('"')
        if stripped.startswith("- "):
            stripped = stripped[2:].strip().strip("'").strip('"')
        if stripped in GENERIC_RUNTIME_PATHS:
            hits.append(line)
    return hits


def apply() -> int:
    changed = 0
    for path in ppi_feature_workflows():
        text = path.read_text(encoding="utf-8")
        lines = []
        removed = 0
        for line in text.splitlines(keepends=True):
            stripped = line.strip().strip("'").strip('"')
            if stripped.startswith("- "):
                stripped = stripped[2:].strip().strip("'").strip('"')
            if stripped in GENERIC_RUNTIME_PATHS:
                removed += 1
                continue
            lines.append(line)
        if removed:
            path.write_text("".join(lines), encoding="utf-8", newline="\n")
            changed += 1
    print(f"CAPP CI scope apply: changed_workflows={changed}")
    return 0


def check() -> int:
    failures: list[str] = []
    for path in ppi_feature_workflows():
        hits = forbidden_lines(path.read_text(encoding="utf-8"))
        if hits:
            failures.append(f"{path.relative_to(ROOT)} still watches generic runtime projection")
    if failures:
        print("CAPP CI scope check: FAILED")
        for item in failures:
            print(f"- {item}")
        return 1
    print(f"CAPP CI scope check: PASS workflows={len(ppi_feature_workflows())}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("check", "apply"))
    args = parser.parse_args()
    return apply() if args.mode == "apply" else check()


if __name__ == "__main__":
    raise SystemExit(main())
