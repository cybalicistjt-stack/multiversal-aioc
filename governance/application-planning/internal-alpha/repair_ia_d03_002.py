#!/usr/bin/env python3
"""Repair the F005 packet readiness sentence before final assembly."""

from pathlib import Path

packet = Path(__file__).resolve().parent / "feature-packets" / "MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md"
text = packet.read_text(encoding="utf-8")
old = "**Final design status:** implementation-ready; application implementation not started and dependency-gated."
new = "**Final design status:** implementation-ready; application implementation remains dependency-gated and has not started."
if old in text:
    text = text.replace(old, new, 1)
elif "implementation remains dependency-gated" not in text.lower():
    raise SystemExit("REPAIR FAIL: expected F005 readiness sentence not found")
packet.write_text(text, encoding="utf-8")
print("IA-D03-002 PACKET REPAIR: PASS")
