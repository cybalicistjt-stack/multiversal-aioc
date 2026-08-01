#!/usr/bin/env python3
"""Run the complete Multiversal forensic audit across the four ZIP archives.

Pipeline:
1. Safely extract and inventory Part 1, Part 2, Part 3, and Creatures.
2. Suppress exact duplicate source members by SHA-256 while preserving provenance.
3. Build deterministic per-document page batches.
4. Run the page/CSV forensic extractor for every unique source.
5. Merge outputs into one corpus-wide ledger.
6. Run duplicate, schema, and canonical reconciliation.
7. Emit a resumable corpus status receipt.

Automatic output remains candidate evidence and is never canonical approval.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from pypdf import PdfReader
except ImportError as exc:
    raise SystemExit("Install dependencies with: pip install pypdf") from exc


def run(command: list[str], cwd: Path) -> None:
    result = subprocess.run(command, cwd=cwd, text=True)
    if result.returncode:
        raise SystemExit(result.returncode)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def slug(value: str) -> str:
    out = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")[:120] or "source"


def make_batches(pdf_path: Path, batch_size: int) -> list[dict[str, Any]]:
    page_count = len(PdfReader(str(pdf_path)).pages)
    batches = []
    for start in range(1, page_count + 1, batch_size):
        end = min(start + batch_size - 1, page_count)
        batches.append({"startPage": start, "endPage": end, "pageCount": end - start + 1})
    return batches


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--canonical", type=Path, default=Path("content-source/phase-1-8-canonical-objects.json"))
    parser.add_argument("--batch-size", type=int, default=50)
    parser.add_argument("--reset", action="store_true", help="Delete previous generated audit work and output")
    args = parser.parse_args()

    repo = args.repo_root.resolve()
    work = repo / "audit-work"
    corpus_root = work / "corpus"
    document_root = work / "documents"
    output = repo / "audit-output"
    inventory_path = output / "archive-inventory.json"
    manifest_path = repo / "audit/archive-corpus-manifest.json"

    if args.reset:
        shutil.rmtree(work, ignore_errors=True)
        shutil.rmtree(output, ignore_errors=True)
    work.mkdir(parents=True, exist_ok=True)
    document_root.mkdir(parents=True, exist_ok=True)
    output.mkdir(parents=True, exist_ok=True)

    run([
        sys.executable,
        "audit/extract_archive_corpus.py",
        "--repo-root", str(repo),
        "--manifest", str(manifest_path),
        "--out", str(corpus_root),
        "--inventory", str(inventory_path),
    ], repo)

    inventory = read_json(inventory_path)
    if not inventory.get("readyForCompleteAudit"):
        raise SystemExit(f"Corpus incomplete: {inventory.get('missingRequiredArchives', [])}")

    members = inventory.get("members", [])
    unique_by_hash: dict[str, dict[str, Any]] = {}
    provenance_by_hash: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for member in members:
        provenance_by_hash[member["sha256"]].append(member)
        unique_by_hash.setdefault(member["sha256"], member)

    schedule: list[dict[str, Any]] = []
    all_findings: list[dict[str, Any]] = []
    all_csv_findings: list[dict[str, Any]] = []
    all_pages: list[dict[str, Any]] = []
    canonical = args.canonical if args.canonical.is_absolute() else repo / args.canonical

    for source_hash, member in sorted(unique_by_hash.items(), key=lambda item: (item[1]["group"], item[1]["member"].lower())):
        source_path = repo / member["extractedPath"]
        doc_id = f"{member['group']}--{slug(member['member'])}--{source_hash[:10]}"
        doc_out = document_root / doc_id
        doc_out.mkdir(parents=True, exist_ok=True)
        provenance = provenance_by_hash[source_hash]

        if member["type"] == "pdf":
            batches = make_batches(source_path, args.batch_size)
            schedule.append({
                "documentId": doc_id,
                "type": "pdf",
                "group": member["group"],
                "member": member["member"],
                "sha256": source_hash,
                "provenance": provenance,
                "pageCount": sum(b["pageCount"] for b in batches),
                "batches": batches,
            })
            for batch in batches:
                command = [
                    sys.executable, "audit/forensic_audit.py",
                    "--pdf", str(source_path),
                    "--canonical", str(canonical),
                    "--out", str(doc_out),
                    "--start-page", str(batch["startPage"]),
                    "--end-page", str(batch["endPage"]),
                ]
                run(command, repo)
            for row in read_jsonl(doc_out / "findings.jsonl"):
                row["documentId"] = doc_id
                row["archiveProvenance"] = provenance
                all_findings.append(row)
            for row in read_jsonl(doc_out / "page-ledger.jsonl"):
                row["documentId"] = doc_id
                row["sourceHash"] = source_hash
                row["archiveProvenance"] = provenance
                all_pages.append(row)
        elif member["type"] == "csv":
            schedule.append({
                "documentId": doc_id,
                "type": "csv",
                "group": member["group"],
                "member": member["member"],
                "sha256": source_hash,
                "provenance": provenance,
            })
            command = [
                sys.executable, "audit/forensic_audit.py",
                "--pdf", str(next((repo / m["extractedPath"] for m in members if m["type"] == "pdf"), source_path)),
                "--csv-root", str(source_path.parent),
                "--canonical", str(canonical),
                "--out", str(doc_out),
                "--start-page", "1",
                "--end-page", "0",
            ]
            # forensic_audit currently requires --pdf; end-page 0 prevents PDF scanning.
            run(command, repo)
            for row in read_jsonl(doc_out / "csv-findings.jsonl"):
                if Path(row.get("source_path", "")).resolve() != source_path.resolve():
                    continue
                row["documentId"] = doc_id
                row["archiveProvenance"] = provenance
                all_csv_findings.append(row)

    write_jsonl(output / "findings.jsonl", all_findings)
    write_jsonl(output / "csv-findings.jsonl", all_csv_findings)
    write_jsonl(output / "page-ledger.jsonl", all_pages)
    (output / "document-batch-schedule.json").write_text(
        json.dumps({
            "format": "multiversal-document-batch-schedule",
            "version": "1.0.0",
            "batchSize": args.batch_size,
            "documents": schedule,
        }, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    run([
        sys.executable, "audit/reconcile_audit.py",
        "--audit-output", str(output),
        "--canonical", str(canonical),
    ], repo)

    families = Counter()
    matches = Counter()
    for finding in all_findings + all_csv_findings:
        families.update(finding.get("family_scores", {}).keys())
        matches[finding.get("match_state", "unmatched")] += 1

    total_pages = sum(int(row.get("pageCount", 0)) for row in schedule if row["type"] == "pdf")
    completed_pages = len({(row["documentId"], row["page"]) for row in all_pages if row.get("status") == "complete"})
    status = {
        "format": "multiversal-forensic-corpus-status",
        "version": "1.0.0",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "corpusComplete": True,
        "archiveCount": inventory["presentArchiveCount"],
        "requiredArchiveCount": 4,
        "uniqueSourceCount": len(unique_by_hash),
        "duplicateSourceGroups": len(inventory.get("duplicateMemberGroups", [])),
        "pdfCount": sum(1 for m in unique_by_hash.values() if m["type"] == "pdf"),
        "csvCount": sum(1 for m in unique_by_hash.values() if m["type"] == "csv"),
        "totalPages": total_pages,
        "completedPages": completed_pages,
        "pageCoveragePercent": round((completed_pages / total_pages * 100), 2) if total_pages else 0,
        "findingCount": len(all_findings),
        "csvFindingCount": len(all_csv_findings),
        "familyCounts": dict(families),
        "matchStates": dict(matches),
        "automaticAuditComplete": completed_pages == total_pages,
        "humanReviewComplete": False,
        "canonicalPromotionComplete": False,
        "authorityNote": "Machine extraction completion does not equal human verification or canonical approval."
    }
    (output / "corpus-status.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(status, indent=2))


if __name__ == "__main__":
    main()
