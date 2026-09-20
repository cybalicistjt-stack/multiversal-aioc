#!/usr/bin/env python3
"""Regenerate/check MVPS-21 current Core-26 presentation projections.

The committed outputs are current-authority overlays. Historical PPIA-06/CAPP
25-profile artifacts are inputs only and remain immutable.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"governance/application-planning/player-species"
FILES=[
 "MVPS-21_CURRENT_APPEARANCE_PROFILE_OVERLAY_v1.0.0.json",
 "MVPS-21_CURRENT_CORE26_PRESENTATION_CATALOG_v1.0.0.json",
 "MVPS-21_AUTHORING_SEARCH_INSPECTION_INDEX_v1.0.0.json",
 "MVPS-21_PRESENTATION_REGENERATION_RECEIPT_v1.0.0.json",
]
def load(name): return json.loads((BASE/name).read_text(encoding="utf-8"))
def check():
 o,p,i,r=[load(x) for x in FILES]
 assert o["profile_count"]==26
 assert p["roster_count"]==26
 assert i["entry_count"]==26
 assert r["current_roster_count"]==26
 assert [x["species"] for x in o["profiles"]]==[x["display_name"] for x in p["entries"]]
 assert [x["display_name"] for x in i["entries"]]==[x["display_name"] for x in p["entries"]]
 assert all(x["mechanics_authority"] is False for x in o["profiles"])
 assert all(x["mechanics_authority"] is False for x in p["entries"])
 assert "Nekron" not in [x["display_name"] for x in p["entries"]]
 assert "Akwi" in [x["display_name"] for x in p["entries"]]
 print("MVPS-21 current Core-26 presentation projections: OK")
if __name__=="__main__":
 ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); args=ap.parse_args()
 check()
