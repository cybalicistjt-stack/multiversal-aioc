#!/usr/bin/env python3
"""Retired Operations V2 execution-integrity gate."""
import sys
MESSAGE = "The V2 execution-integrity gate is retired. Bootstrap through operations/BOOTSTRAP.md and use current OPS3 validation."
if __name__ == "__main__":
    print(MESSAGE, file=sys.stderr)
    raise SystemExit(2)
