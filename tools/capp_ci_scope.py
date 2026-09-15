#!/usr/bin/env python3
"""Retired Operations V2 CAPP CI-scope tool."""
import sys
MESSAGE = "CAPP's V2 CI-scope tool is historical and retired. Bootstrap through operations/BOOTSTRAP.md."
if __name__ == "__main__":
    print(MESSAGE, file=sys.stderr)
    raise SystemExit(2)
