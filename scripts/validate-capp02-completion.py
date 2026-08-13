#!/usr/bin/env python3
from __future__ import annotations
import subprocess, sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
FINAL=R/'scripts/validate-capp02-final-state-structured.py'
if __name__=='__main__': raise SystemExit(subprocess.call([sys.executable,str(FINAL)],cwd=R))
