#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
import shutil
import subprocess
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ASSEMBLY_DIR = Path(__file__).resolve().parent
CHUNK_DIR = ASSEMBLY_DIR / "chunks"
WORKFLOW = ROOT / ".github/workflows/ia-d02-005-assemble.yml"

payload = "".join(path.read_text(encoding="utf-8") for path in sorted(CHUNK_DIR.glob("chunk_*.txt")))
files: dict[str, str] = json.loads(zlib.decompress(base64.b64decode(payload)).decode("utf-8"))

for relative, content in files.items():
    target = ROOT / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

subprocess.run(["python", "governance/application-planning/internal-alpha/validate_internal_alpha_design.py"], cwd=ROOT, check=True)
subprocess.run(["python", "governance/application-planning/internal-alpha/validate_feature_packets.py"], cwd=ROOT, check=True)

if WORKFLOW.exists():
    WORKFLOW.unlink()
shutil.rmtree(ASSEMBLY_DIR)

subprocess.run(["git", "config", "user.name", "github-actions[bot]"], cwd=ROOT, check=True)
subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], cwd=ROOT, check=True)
subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
status = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, check=True, capture_output=True, text=True).stdout
if not status.strip():
    raise SystemExit("Assembler produced no changes.")
subprocess.run([
    "git", "commit", "-m", "Complete IA-D02-005 onboarding help diagnostics design",
    "-m", "Complete the implementation-ready MV-IA-F025 packet, support matrix, traceability, validation, registry, indexes, and backlog advancement to the shared-foundations integration review."
], cwd=ROOT, check=True)
subprocess.run(["git", "push", "origin", "HEAD:governance/mv-ia-d02-005-onboarding-help-diagnostics"], cwd=ROOT, check=True)
