#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"
OLD_SCRIPT = ROOT / "assemble_ia_d03_001.py"
SELF = Path(__file__)
V2_WORKFLOW = ROOT.parents[2] / ".github" / "workflows" / "assemble-ia-d03-001-v2.yml"

actual = """## Current next design action

**IA-D03-001 — Design MV-IA-F004, Character Creation and Advancement.**

The Character packet must consume the IA-D02-006 shared-foundation contract matrix rather than creating private identity, permission, picker, save, recovery, diagnostic, or support behavior."""
expected_by_assembler = """## Current next design action

**IA-D03-001 — Design MV-IA-F004, Character Creation and Advancement.**

F004 must consume the IA-D02-006 contract matrix rather than redefining identity, roles, selected context, authorization, stable-ID selection, idempotency, reconnect, diagnostics, support access, accessibility, or provider boundaries."""

text = README.read_text(encoding="utf-8")
if actual not in text:
    raise SystemExit("WRAPPER FAIL: current README next-action block was not found")
README.write_text(text.replace(actual, expected_by_assembler, 1), encoding="utf-8")

subprocess.run([sys.executable, str(OLD_SCRIPT)], check=True)

if V2_WORKFLOW.exists():
    V2_WORKFLOW.unlink()
if SELF.exists():
    SELF.unlink()

print("IA-D03-001 WRAPPED ASSEMBLY: PASS")
