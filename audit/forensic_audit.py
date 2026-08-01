#!/usr/bin/env python3
"""Resumable forensic audit runner for Multiversal legacy sources.

Primary source: fullmv062926.pdf
Supplemental source: CSV/table files exported from the aaaa source.

The runner deliberately scans every page and every table. It does not assume
that object families are confined to chapter headings.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    from pypdf import PdfReader
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Install dependencies with: pip install pypdf") from exc

FAMILIES: dict[str, tuple[str, ...]] = {
    "rule": ("rule", "check", "save", "dc ", "advantage", "disadvantage", "round", "turn", "action", "reaction"),
    "ability": ("ability", "power", "technique", "feat", "talent", "spell", "ritual", "maneuver"),
    "creature": ("creature", "monster", "beast", "construct", "undead", "dragon", "demon", "animal"),
    "npc": ("npc", "merchant", "soldier", "warden", "medic", "scout", "engineer", "trader"),
    "item": ("item", "weapon", "armor", "tool", "potion", "artifact", "relic", "wand", "staff", "ring"),
    "vehicle": ("vehicle", "ship", "starship", "mecha", "mount", "drone", "walker"),
    "species": ("species", "race", "subspecies", "ancestry", "heritage"),
    "world": ("world", "reality", "plane", "realm", "dimension", "region", "city", "location"),
    "environment": ("environment", "terrain", "hazard", "weather", "biome", "underwater", "desert", "arctic"),
    "adventure": ("adventure", "quest", "hook", "encounter", "objective", "clue", "investigation"),
    "economy": ("business", "trade", "currency", "resource", "craft", "mining", "salvage", "yield"),
    "faction": ("faction", "organization", "corporation", "guild", "religion", "culture", "empire"),
}

MECHANIC_PATTERNS = [
    re.compile(r"\b\d+d\d+(?:\s*[+\-]\s*\d+)?\b", re.I),
    re.compile(r"\bDC\s*\d+\b", re.I),
    re.compile(r"\b(?:HP|AC|DR|EP|MP|SP)\s*[:=]?\s*\d+\b", re.I),
    re.compile(r"\b\d+\s*(?:ft|feet|mile|miles|rounds?|turns?|hours?|minutes?)\b", re.I),
    re.compile(r"\b(?:bonus action|free action|reaction|once per|per encounter|per scene|per rest)\b", re.I),
]

CSV_HEADER_HINTS = {
    "name", "npc", "ability", "item", "creature", "hp", "ac", "speed", "attack",
    "damage", "effect", "description", "cost", "range", "duration", "traits", "type",
}

@dataclass
class Finding:
    finding_id: str
    source_kind: str
    source_path: str
    locator: str
    family_scores: dict[str, int]
    title_candidate: str
    text: str
    mechanic_signals: list[str]
    table_shape: dict[str, Any] | None
    canonical_match: str | None = None
    match_state: str = "unmatched"
    review_state: str = "needs-review"


def stable_id(*parts: str) -> str:
    return hashlib.sha256("\n".join(parts).encode("utf-8", "ignore")).hexdigest()[:20]


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def family_scores(text: str) -> dict[str, int]:
    lower = text.lower()
    scores = {family: sum(lower.count(term) for term in terms) for family, terms in FAMILIES.items()}
    return {k: v for k, v in scores.items() if v}


def mechanic_signals(text: str) -> list[str]:
    signals: list[str] = []
    for pattern in MECHANIC_PATTERNS:
        signals.extend(m.group(0) for m in pattern.finditer(text))
    return list(dict.fromkeys(signals))[:40]


def title_candidate(text: str) -> str:
    lines = [clean(x) for x in text.splitlines() if clean(x)]
    for line in lines[:8]:
        if 2 <= len(line.split()) <= 14 and len(line) <= 120:
            if not re.fullmatch(r"[\d\W]+", line):
                return line.strip("•-: ")
    return lines[0][:120] if lines else "Untitled finding"


def chunks(text: str, max_chars: int = 2200) -> Iterable[str]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    buffer = ""
    for paragraph in paragraphs:
        if len(buffer) + len(paragraph) + 2 > max_chars and buffer:
            yield buffer
            buffer = paragraph
        else:
            buffer = f"{buffer}\n\n{paragraph}".strip()
    if buffer:
        yield buffer


def detect_inline_csv(text: str) -> list[dict[str, Any]]:
    lines = [line.strip() for line in text.splitlines()]
    tables: list[dict[str, Any]] = []
    for idx, line in enumerate(lines):
        if line.count(",") < 2:
            continue
        try:
            header = next(csv.reader([line]))
        except csv.Error:
            continue
        normalized = {clean(x).lower() for x in header}
        if len(normalized & CSV_HEADER_HINTS) < 2:
            continue
        rows = []
        for candidate in lines[idx + 1: idx + 51]:
            if candidate.count(",") < 1:
                break
            try:
                row = next(csv.reader([candidate]))
            except csv.Error:
                break
            if len(row) < 2:
                break
            rows.append(row)
        tables.append({"header": header, "rows": rows, "start_line": idx + 1})
    return tables


def load_canonical(path: Path | None) -> tuple[dict[str, Any], dict[str, list[str]]]:
    if not path or not path.exists():
        return {}, {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload.get("records", payload if isinstance(payload, list) else [])
    by_id: dict[str, Any] = {}
    by_name: dict[str, list[str]] = defaultdict(list)
    for record in records:
        rid = str(record.get("id") or record.get("stableId") or "")
        name = clean(str(record.get("name") or record.get("title") or "")).lower()
        if rid:
            by_id[rid] = record
        if name and rid:
            by_name[name].append(rid)
    return by_id, dict(by_name)


def match_finding(finding: Finding, by_name: dict[str, list[str]]) -> None:
    candidate = clean(finding.title_candidate).lower()
    exact = by_name.get(candidate, [])
    if len(exact) == 1:
        finding.canonical_match = exact[0]
        finding.match_state = "exact-name"
    elif len(exact) > 1:
        finding.match_state = "ambiguous-name"


def audit_pdf(pdf_path: Path, out: Path, by_name: dict[str, list[str]], start_page: int = 1, end_page: int | None = None) -> list[Finding]:
    reader = PdfReader(str(pdf_path))
    final_page = min(end_page or len(reader.pages), len(reader.pages))
    findings: list[Finding] = []
    ledger_path = out / "page-ledger.jsonl"
    findings_path = out / "findings.jsonl"
    completed = set()
    if ledger_path.exists():
        for line in ledger_path.read_text(encoding="utf-8").splitlines():
            try:
                row = json.loads(line)
                if row.get("status") == "complete":
                    completed.add(int(row["page"]))
            except Exception:
                pass
    with ledger_path.open("a", encoding="utf-8") as ledger, findings_path.open("a", encoding="utf-8") as sink:
        for page_no in range(max(1, start_page), final_page + 1):
            if page_no in completed:
                continue
            raw = reader.pages[page_no - 1].extract_text() or ""
            page_findings = 0
            for index, block in enumerate(chunks(raw)):
                scores = family_scores(block)
                signals = mechanic_signals(block)
                inline_tables = detect_inline_csv(block)
                if not scores and not signals and not inline_tables:
                    continue
                finding = Finding(
                    finding_id=stable_id(str(pdf_path), str(page_no), str(index), block[:500]),
                    source_kind="pdf",
                    source_path=str(pdf_path),
                    locator=f"page:{page_no};chunk:{index + 1}",
                    family_scores=scores,
                    title_candidate=title_candidate(block),
                    text=block,
                    mechanic_signals=signals,
                    table_shape={"tables": inline_tables} if inline_tables else None,
                )
                match_finding(finding, by_name)
                sink.write(json.dumps(asdict(finding), ensure_ascii=False) + "\n")
                findings.append(finding)
                page_findings += 1
            ledger.write(json.dumps({"page": page_no, "status": "complete", "characters": len(raw), "findings": page_findings}) + "\n")
            ledger.flush(); sink.flush()
    return findings


def audit_csvs(csv_root: Path, out: Path, by_name: dict[str, list[str]]) -> list[Finding]:
    results: list[Finding] = []
    sink_path = out / "csv-findings.jsonl"
    with sink_path.open("w", encoding="utf-8") as sink:
        for path in sorted(csv_root.rglob("*.csv")):
            text = path.read_text(encoding="utf-8-sig", errors="replace")
            try:
                dialect = csv.Sniffer().sniff(text[:8192])
            except csv.Error:
                dialect = csv.excel
            rows = list(csv.DictReader(text.splitlines(), dialect=dialect))
            for row_index, row in enumerate(rows, start=2):
                row_text = " | ".join(f"{k}: {v}" for k, v in row.items() if v not in (None, ""))
                finding = Finding(
                    finding_id=stable_id(str(path), str(row_index), row_text),
                    source_kind="csv",
                    source_path=str(path),
                    locator=f"row:{row_index}",
                    family_scores=family_scores(row_text),
                    title_candidate=clean(str(next((v for k, v in row.items() if k and k.lower() in {"name", "npc", "ability", "item", "creature", "title"} and v), ""))) or title_candidate(row_text),
                    text=row_text,
                    mechanic_signals=mechanic_signals(row_text),
                    table_shape={"columns": list(row.keys()), "row": row},
                )
                match_finding(finding, by_name)
                sink.write(json.dumps(asdict(finding), ensure_ascii=False) + "\n")
                results.append(finding)
    return results


def summarize(out: Path) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    for name in ("findings.jsonl", "csv-findings.jsonl"):
        path = out / name
        if path.exists():
            findings.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
    families = Counter()
    sources = Counter()
    matches = Counter()
    for finding in findings:
        families.update(finding.get("family_scores", {}).keys())
        sources[finding.get("source_kind", "unknown")] += 1
        matches[finding.get("match_state", "unmatched")] += 1
    unresolved = [f for f in findings if f.get("match_state") != "exact-name"]
    summary = {
        "format": "multiversal-forensic-audit-summary",
        "findingCount": len(findings),
        "bySourceKind": dict(sources),
        "byFamily": dict(families),
        "byMatchState": dict(matches),
        "unresolvedCount": len(unresolved),
    }
    (out / "audit-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (out / "unresolved-review-queue.json").write_text(json.dumps(unresolved, indent=2, ensure_ascii=False), encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--csv-root", type=Path)
    parser.add_argument("--canonical", type=Path)
    parser.add_argument("--out", type=Path, default=Path("audit-output"))
    parser.add_argument("--start-page", type=int, default=1)
    parser.add_argument("--end-page", type=int)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    _, by_name = load_canonical(args.canonical)
    audit_pdf(args.pdf, args.out, by_name, args.start_page, args.end_page)
    if args.csv_root and args.csv_root.exists():
        audit_csvs(args.csv_root, args.out, by_name)
    print(json.dumps(summarize(args.out), indent=2))

if __name__ == "__main__":
    main()
