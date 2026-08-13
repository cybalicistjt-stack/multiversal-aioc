#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
CP=R/'governance/ai/work-state/CAPP-01-attempt-001.json'
CANDIDATE=R/'scripts/validate-capp01-completion-candidate.py'
FINAL=R/'scripts/validate-capp01-final-state-structured.py'

def main():
    cp=json.loads(CP.read_text(encoding='utf-8'))
    target=FINAL if cp.get('status')=='completed_verified' else CANDIDATE
    return subprocess.call([sys.executable,str(target)],cwd=R)

if __name__=='__main__': raise SystemExit(main())
