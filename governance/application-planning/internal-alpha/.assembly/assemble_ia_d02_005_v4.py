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
CHUNK_EXPECTED = {
    "chunk_000.txt": (5000, "4472a912a70d17375830f44fa8c8a4b203eb916ff793ac9f2994360b27606b91"),
    "chunk_001.txt": (5000, "8ab91f82c2666b404a03cd1f9e5e669944d31d1c4bdaf841d83e3d781b7e8d1b"),
    "chunk_002.txt": (5000, "c6bcde632e797f3e3f2d7e581e6cb63a8f0ee8b0191e062d4ba790985081db99"),
    "chunk_003.txt": (5000, "0faed9fdace61d06f1ff4bbf1584a7793f3396a54cf24931d286287f155b46f1"),
    "chunk_004.txt": (5000, "1b531c97a5178a6af5f615514ba669bcd2c7d7b7257aca7393d05b4a0b3ca658"),
    "chunk_005.txt": (5000, "b8ffb41a788fb4030fe2fed9a0a6095d0f5cb3ba8fffda1eef934926d14311eb"),
    "chunk_006.txt": (5000, "fb56ef81d588d8d2f1fde16155478ad9ce0dca72b0404ee1229e21a09ee811f0"),
    "chunk_007.txt": (4144, "7ec57f8aaadbc0f73242a4fce97df22cc5f76d3b44bb1e4256eb2933830a3cdc"),
}
OUTER_PART_EXPECTED = {
    0: "2929fe5c222b4bfe08cf4ce03386516f45050953a9245d87ab3ccc28c2918956",
    2: "7b486b525a029be1878f0897377e377d74c018ebbf5ccb9f6666cebaa2c086d3",
    3: "40b13369652775919f0974c31fc370eb4648377588f66d2d90b5587ab75618c7",
    4: "959c112c79ca76228e80e757058f1bc8e399e8ea00e544708be3d08db0ec68cb",
}
SUBPART_EXPECTED = [
    "089bdbdf662b246b78a7e4b1ac4bdf254fa76aef9c7d3f97f5c32ace0fa27ad9",
    "a545669575e644c617885c40b8d631684e8a1f9c096ba96aec6957829fcd7182",
    "e4a4ba68d140db30b50eaede96c8bcd2f8cbddf0da7f422edfb621940caec4fa",
    "52b3928486f8572f5fa207c176d1601403509f063c033c2c2b404d982cfa7c79",
    "e15cebf71c7bef0125efcb6e31bf2a16e7dfc2445effd221867210778f387b44",
    "8ca133062c764006d0d5805fb4a83abdcc670e8026ec790b5578185cf2a65c04",
    "ce3e758425e32647b8d220020f5b2345b168391632cb61b1cf21657fb68e560e",
    "ddb41e7db9fda71f9626dcdffb3614f8c72fec69b2a3ff3a215aac655eba9040",
    "1080bdc09149ec3e5bf14737e78dfdf0d821a5642de6989bad750717252b2e54",
    "d9b11f7c0ed7f115b8a8a418acdfeff2e6d609d45fe22e17e6a2260b9dfb0b79",
]

def verified_text(path: Path, length: int, digest: str) -> str:
    data = path.read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    print(f"{path.name}: length={len(data)} sha256={actual}")
    if len(data) != length or actual != digest:
        raise SystemExit(f"{path.name} mismatch: expected length={length} sha256={digest}; got length={len(data)} sha256={actual}")
    return data.decode("utf-8")

outer: dict[int, str] = {}
for index, digest in OUTER_PART_EXPECTED.items():
    outer[index] = verified_text(CHUNK_DIR / f"chunk_000_part_{index}.txt", 1000, digest)
subparts = [verified_text(CHUNK_DIR / f"chunk_000_part_1_{index:02d}.txt", 100, digest) for index, digest in enumerate(SUBPART_EXPECTED)]
outer[1] = "".join(subparts)
if len(outer[1]) != 1000 or hashlib.sha256(outer[1].encode()).hexdigest() != "309cbe894983b463d2b8d20857491e37a7fa9e5b060a484fc13bfdd143c5e270":
    raise SystemExit("reconstructed chunk_000 part 1 mismatch")

chunks = ["".join(outer[index] for index in range(5))]
for index in range(1, 8):
    chunks.append((CHUNK_DIR / f"chunk_{index:03d}.txt").read_text(encoding="utf-8"))
for index, text in enumerate(chunks):
    name = f"chunk_{index:03d}.txt"
    length, digest = CHUNK_EXPECTED[name]
    actual = hashlib.sha256(text.encode()).hexdigest()
    print(f"{name}: length={len(text)} sha256={actual}")
    if len(text) != length or actual != digest:
        raise SystemExit(f"{name} mismatch")

payload = "".join(chunks)
compressed = base64.b64decode(payload, validate=True)
files: dict[str, str] = json.loads(zlib.decompress(compressed).decode("utf-8"))
print(f"decoded file count={len(files)}")
for relative, content in files.items():
    target = ROOT / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

subprocess.run(["python", "governance/application-planning/internal-alpha/validate_internal_alpha_design.py"], cwd=ROOT, check=True)
subprocess.run(["python", "governance/application-planning/internal-alpha/validate_feature_packets.py"], cwd=ROOT, check=True)

for workflow_name in ("ia-d02-005-assemble.yml", "ia-d02-005-assemble-pr.yml", "ia-d02-005-assemble-v2.yml", "ia-d02-005-assemble-v3.yml", "ia-d02-005-assemble-v4.yml"):
    workflow = ROOT / ".github/workflows" / workflow_name
    if workflow.exists():
        workflow.unlink()
shutil.rmtree(ASSEMBLY_DIR)
subprocess.run(["git", "config", "user.name", "github-actions[bot]"], cwd=ROOT, check=True)
subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], cwd=ROOT, check=True)
subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
subprocess.run(["git", "commit", "-m", "Complete IA-D02-005 onboarding help diagnostics design", "-m", "Complete the implementation-ready MV-IA-F025 packet, support matrix, traceability, validation, registry, indexes, and backlog advancement to the shared-foundations integration review."], cwd=ROOT, check=True)
subprocess.run(["git", "push", "origin", "HEAD:governance/mv-ia-d02-005-onboarding-help-diagnostics"], cwd=ROOT, check=True)
