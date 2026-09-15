#!/usr/bin/env python3
"""Retired Operations V2-era program validator."""
import sys
MESSAGE = "This pre-OPS3 validator is historical and retired from live execution. Bootstrap through operations/BOOTSTRAP.md."
if __name__ == "__main__":
    print(MESSAGE, file=sys.stderr)
    raise SystemExit(2)
