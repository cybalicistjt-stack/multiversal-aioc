#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKET = ROOT / "feature-packets" / "MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md"
WRAPPER = ROOT / "assemble_ia_d03_001_wrapper.py"
SELF = Path(__file__)
V3_WORKFLOW = ROOT.parents[2] / ".github" / "workflows" / "assemble-ia-d03-001-v3.yml"

text = PACKET.read_text(encoding="utf-8")
next_item = "**Next design item:** IA-D03-002 — Design MV-IA-F005, Campaign, Scene, and Session Builder."
if next_item not in text:
    PACKET.write_text(text.rstrip() + "\n\n" + next_item + "\n", encoding="utf-8")

subprocess.run([sys.executable, str(WRAPPER)], check=True)

if V3_WORKFLOW.exists():
    V3_WORKFLOW.unlink()
if SELF.exists():
    SELF.unlink()

print("IA-D03-001 REPAIR AND ASSEMBLY: PASS")
