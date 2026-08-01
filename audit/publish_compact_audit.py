#!/usr/bin/env python3
"""Publish compact forensic-audit results for the static AIOC dashboard.

Copies bounded summaries from audit-output into v2/audit-data. Full findings stay
in workflow artifacts so the repository does not grow without limit.
"""
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

COMPACT_FILES = (
    "corpus-status.json",
    "archive-inventory.json",
    "document-batch-schedule.json",
    "reconciliation-report.json",
    "csv-schema-registry.json",
    "duplicate-groups.json",
    "candidate-matches.json",
    "audit-summary.json",
)


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--source", type=Path, default=Path("audit-output"))
    p.add_argument("--destination", type=Path, default=Path("v2/audit-data"))
    p.add_argument("--source-sha", default="")
    args = p.parse_args()

    args.destination.mkdir(parents=True, exist_ok=True)
    published = []
    for name in COMPACT_FILES:
        src = args.source / name
        if src.exists():
            shutil.copy2(src, args.destination / name)
            published.append(name)

    status = read_json(args.source / "corpus-status.json") or {}
    reconciliation = read_json(args.source / "reconciliation-report.json") or {}
    inventory = read_json(args.source / "archive-inventory.json") or {}
    manifest = {
        "format": "multiversal-static-audit-publication",
        "version": "1.0.0",
        "publishedAt": datetime.now(timezone.utc).isoformat(),
        "sourceCommit": args.source_sha,
        "publishedFiles": published,
        "summary": {
            "archiveCount": status.get("archiveCount", inventory.get("archiveCount", 0)),
            "pdfCount": status.get("pdfCount", inventory.get("pdfCount", 0)),
            "csvCount": status.get("csvCount", inventory.get("csvCount", 0)),
            "totalPages": status.get("totalPages", 0),
            "completedPages": status.get("completedPages", 0),
            "findingCount": status.get("findingCount", reconciliation.get("findingCount", 0)),
            "unresolvedCount": status.get("unresolvedCount", reconciliation.get("unresolvedCount", 0)),
            "machineScanComplete": bool(status.get("machineScanComplete")),
            "humanReviewComplete": bool(status.get("humanReviewComplete")),
            "canonicalPromotionComplete": bool(status.get("canonicalPromotionComplete")),
        },
    }
    (args.destination / "publication-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
