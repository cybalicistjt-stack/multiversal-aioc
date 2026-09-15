#!/usr/bin/env python3
"""Retired Operations V2 Stage-A validator."""
import sys
MESSAGE = "This Stage-A-era validator is historical and retired. Bootstrap through operations/BOOTSTRAP.md."
if __name__ == "__main__":
    print(MESSAGE, file=sys.stderr)
    raise SystemExit(2)
