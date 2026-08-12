#!/usr/bin/env python3
from __future__ import annotations

import runpy
from pathlib import Path

validator = Path(__file__).with_name("validate-ppia15-foundation.py")
namespace = runpy.run_path(str(validator), run_name="ppia15_foundation_validator")
try:
    namespace["main"]()
except SystemExit as exc:
    message = str(exc).replace("\n", "%0A").replace("\r", "%0D")
    print(f"::error title=PPIA-15 Foundation Validator::{message}")
    raise
