#!/usr/bin/env python3
"""Governed Multiversal owner-correction to regression-case intake."""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
from correction_regression_lib.common import CorrectionError
from correction_regression_lib.state import capture,promote,review,validate_repository

def main()->int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",default=".")
    sub=parser.add_subparsers(dest="command",required=True)
    sub.add_parser("validate")
    cap=sub.add_parser("capture"); cap.add_argument("--input",required=True)
    rev=sub.add_parser("review"); rev.add_argument("--candidate-id",required=True); rev.add_argument("--decision",choices=("approved","rejected"),required=True); rev.add_argument("--reviewer",required=True); rev.add_argument("--evidence",action="append",required=True); rev.add_argument("--decided-at")
    pro=sub.add_parser("promote"); pro.add_argument("--candidate-id",required=True); pro.add_argument("--case-id",required=True); pro.add_argument("--evidence",action="append",required=True); pro.add_argument("--promoted-at")
    args=parser.parse_args(); root=Path(args.root).resolve()
    try:
        if args.command=="validate":
            validate_repository(root); print("Correction-to-regression validation: PASS")
        elif args.command=="capture":
            correction_id,candidate_id,created=capture(root,Path(args.input).resolve())
            print(f"{'created' if created else 'existing'} correction={correction_id} candidate={candidate_id}")
        elif args.command=="review":
            review(root,args.candidate_id,args.decision,args.reviewer,args.evidence,args.decided_at)
            print(f"reviewed candidate={args.candidate_id} decision={args.decision}")
        else:
            promote(root,args.candidate_id,args.case_id,args.evidence,args.promoted_at)
            print(f"promoted candidate={args.candidate_id} case={args.case_id}")
    except (CorrectionError,OSError) as exc:
        print(f"Correction-to-regression error: {exc}",file=sys.stderr); return 1
    return 0

if __name__=="__main__": raise SystemExit(main())
