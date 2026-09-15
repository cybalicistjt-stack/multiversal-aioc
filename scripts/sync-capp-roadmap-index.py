#!/usr/bin/env python3
"""Retired Operations V2 roadmap-index synchronizer."""
import sys
MESSAGE = "The legacy roadmap-index synchronizer is retired. Live state is operations/CURRENT.json; bootstrap through operations/BOOTSTRAP.md."
if __name__ == "__main__":
    print(MESSAGE, file=sys.stderr)
    raise SystemExit(2)
