#!/usr/bin/env python3
"""Retired Operations V2 IA-D09 validator."""
import sys
MESSAGE = "This IA-D09-era validator is historical and retired. Bootstrap through operations/BOOTSTRAP.md."
if __name__ == "__main__":
    print(MESSAGE, file=sys.stderr)
    raise SystemExit(2)
