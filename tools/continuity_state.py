#!/usr/bin/env python3
"""Retired Operations V2 compatibility tool."""
from __future__ import annotations

import sys

MESSAGE = (
    "This Operations V2 tool is retired from live execution. "
    "Bootstrap through operations/BOOTSTRAP.md and use the current lane/work item instead."
)

if __name__ == "__main__":
    print(MESSAGE, file=sys.stderr)
    raise SystemExit(2)
