#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import json
import shutil
import subprocess
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ASSEMBLY_DIR = Path(__file__).resolve().parent
CHUNK_DIR = ASSEMBLY_DIR / "chunks"
EXPECTED = {
    "chunk_000.txt": (5000, "4472a912a70d17375830f44fa8c8a4b203eb916ff793ac9f2994360b27606b91"),
    "chunk_001.txt": (5000, "8ab91f82c2666b404a03cd1f9e5e669944d31d1c4bdaf841d83e3d781b7e8d1b"),
    "chunk_002.txt": (5000, "c6bcde632e797f3e3f2d7e581e6cb63a8f0ee8b0191e062d4ba790985081db99"),
    "chunk_003.txt": (5000, "0faed9fdace61d06f1ff4bbf1584a7793f3396a54cf24931d286287f155b46f1"),
    "chunk_004.txt": (5000, "1b531c97a5178a6af5f615514ba669bcd2c7d7b7257aca7393d05b4a0b3ca658"),
    "chunk_005.txt": (5000, "b8ffb41a788fb4030fe2fed9a0a6095d0f5cb3ba8fffda1eef934926d14311eb"),
    "chunk_006.txt": (5000, "fb56ef81d588d8d2f1fde16155478ad9ce0dca72b0404ee1229e21a09ee811f0"),
    "chunk_007.txt": (4144, "7ec57f8aaadbc0f73242a4fce97df22cc5f76d3b44bb1e4256eb2933830a3cdc"),
}

selected: list[Path] = []
errors: list[str] = []
for name, (expected_length, expected_digest) in EXPECTED.items():
    correction = CHUNK_DIR / f"corrected_{name}"
    path = correction if correction.exists() else CHUNK_DIR / name
    if not path.exists():
        errors.append(f"missing {name}")
        continue
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    print(f"{name}: source={path.name} length={len(data)} sha256={digest}")
    if len(data) != expected_length or digest != expected_digest:
        errors.append(
            f"{name}: expected length={expected_length} sha256={expected_digest}; "
            f"got length={len(data)} sha256={digest}"
        )
    selected.append(path)

if errors:
    raise SystemExit("IA-D02-005 PAYLOAD DIAGNOSTIC: FAIL\n" + "\n".join(errors))

payload = "".join(path.read_text(encoding="utf-8") for path in selected)
print(f"payload length={len(payload)} remainder={len(payload) % 4}")
compressed = base64.b64decode(payload, validate=True)
files: dict[str, str] = json.loads(zlib.decompress(compressed).decode("utf-8"))
print(f"decoded file count={len(files)}")

for relative, content in files.items():
    target = ROOT / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

subprocess.run(["python", "governance/application-planning/internal-alpha/validate_internal_alpha_design.py"], cwd=ROOT, check=True)
subprocess.run(["python", "governance/application-planning/internal-alpha/validate_feature_packets.py"], cwd=ROOT, check=True)

for workflow_name in (
    "ia-d02-005-assemble.yml",
    "ia-d02-005-assemble-pr.yml",
    "ia-d02-005-assemble-v2.yml",
):
    workflow = ROOT / ".github/workflows" / workflow_name
    if workflow.exists():
        workflow.unlink()
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
