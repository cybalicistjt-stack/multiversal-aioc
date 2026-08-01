#!/usr/bin/env python3
"""Refine raw forensic findings into document-qualified reconciliation queues.

This stage does not approve or modify canon. It reduces extraction noise,
repairs provenance aggregation, and produces ranked review candidates.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable

GENERIC_TITLES = {
    "contents", "table of contents", "introduction", "overview", "notes",
    "chapter", "section", "example", "examples", "rules", "abilities",
    "items", "creatures", "vehicles", "worlds", "adventures", "untitled finding",
}
STOPWORDS = {
    "the", "a", "an", "of", "to", "and", "or", "in", "on", "for", "with",
    "from", "by", "at", "as", "is", "are", "this", "that", "their", "your",
}


def clean(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def normalized(value: Any) -> str:
    text = clean(value).lower()
    text = re.sub(r"\([^)]*\)", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return clean(text)


def tokens(value: Any) -> set[str]:
    return {x for x in normalized(value).split() if len(x) > 1 and x not in STOPWORDS}


def jsonl(path: Path) -> Iterable[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def load_canonical(path: Path | None) -> list[dict[str, Any]]:
    if not path or not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload.get("records", payload if isinstance(payload, list) else [])
    return records if isinstance(records, list) else []


def canonical_names(record: dict[str, Any]) -> list[str]:
    values: list[str] = []
    for key in ("name", "title", "displayName", "shortName"):
        if record.get(key):
            values.append(clean(record[key]))
    for key in ("aliases", "alternateNames", "legacyNames"):
        value = record.get(key)
        if isinstance(value, list):
            values.extend(clean(x) for x in value if clean(x))
    spec = record.get("spec")
    if isinstance(spec, dict):
        for key in ("name", "title", "displayName", "aliases"):
            value = spec.get(key)
            if isinstance(value, str) and clean(value):
                values.append(clean(value))
            elif isinstance(value, list):
                values.extend(clean(x) for x in value if clean(x))
    return list(dict.fromkeys(values))


def source_identity(row: dict[str, Any]) -> tuple[str, int | None, int | None]:
    path = clean(row.get("source_path") or row.get("sourcePath") or "unknown")
    locator = clean(row.get("locator"))
    page_match = re.search(r"page:(\d+)", locator)
    chunk_match = re.search(r"chunk:(\d+)", locator)
    return path, int(page_match.group(1)) if page_match else None, int(chunk_match.group(1)) if chunk_match else None


def title_quality(title: str) -> int:
    n = normalized(title)
    if not n or n in GENERIC_TITLES:
        return 0
    words = n.split()
    score = 1
    if 1 <= len(words) <= 10:
        score += 2
    if len(title) <= 90:
        score += 1
    if not re.match(r"^(page|chapter|section|table|figure)\s+\d+", n):
        score += 1
    if any(ch.isalpha() for ch in title):
        score += 1
    return score


def signal_score(row: dict[str, Any]) -> int:
    score = 0
    families = row.get("family_scores") or {}
    mechanics = row.get("mechanic_signals") or []
    text = clean(row.get("text"))
    score += min(5, len(families))
    score += min(5, len(mechanics) * 2)
    score += title_quality(clean(row.get("title_candidate")))
    if row.get("table_shape"):
        score += 4
    if 80 <= len(text) <= 5000:
        score += 2
    if re.search(r"\b(?:tier|level|cost|damage|range|duration|prerequisite|effect|trait|action|reaction)\b", text, re.I):
        score += 2
    return score


def similarity(a: str, b: str) -> float:
    na, nb = normalized(a), normalized(b)
    if not na or not nb:
        return 0.0
    ta, tb = tokens(na), tokens(nb)
    jaccard = len(ta & tb) / len(ta | tb) if ta and tb else 0.0
    sequence = SequenceMatcher(None, na, nb).ratio()
    containment = 1.0 if na in nb or nb in na else 0.0
    return max(jaccard, sequence * 0.9, containment * 0.86)


def build_index(records: list[dict[str, Any]]) -> tuple[dict[str, list[str]], list[tuple[str, str]]]:
    exact: dict[str, list[str]] = defaultdict(list)
    names: list[tuple[str, str]] = []
    for record in records:
        rid = clean(record.get("id") or record.get("stableId"))
        if not rid:
            continue
        for name in canonical_names(record):
            key = normalized(name)
            if key:
                exact[key].append(rid)
                names.append((name, rid))
    return dict(exact), names


def match(title: str, exact: dict[str, list[str]], names: list[tuple[str, str]]) -> dict[str, Any]:
    key = normalized(title)
    hits = exact.get(key, [])
    if len(hits) == 1:
        return {"state": "exact-or-alias", "canonicalId": hits[0], "score": 1.0}
    if len(hits) > 1:
        return {"state": "ambiguous-exact", "canonicalIds": hits, "score": 1.0}
    ranked = sorted(((similarity(title, name), name, rid) for name, rid in names), reverse=True)[:5]
    if not ranked or ranked[0][0] < 0.58:
        return {"state": "unmatched", "score": ranked[0][0] if ranked else 0.0, "candidates": []}
    best = ranked[0]
    state = "probable-existing" if best[0] >= 0.82 else "possible-existing"
    return {
        "state": state,
        "canonicalId": best[2] if state == "probable-existing" else None,
        "score": round(best[0], 4),
        "candidates": [{"score": round(s, 4), "name": n, "canonicalId": rid} for s, n, rid in ranked],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("audit-output"))
    parser.add_argument("--canonical", type=Path)
    parser.add_argument("--out", type=Path, default=Path("audit-output/refined"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    raw = list(jsonl(args.input / "findings.jsonl")) + list(jsonl(args.input / "csv-findings.jsonl"))
    canonical = load_canonical(args.canonical)
    exact, names = build_index(canonical)

    seen: set[tuple[str, int | None, str]] = set()
    refined: list[dict[str, Any]] = []
    suppressed: list[dict[str, Any]] = []
    document_pages: dict[str, set[int]] = defaultdict(set)
    document_findings: Counter[str] = Counter()

    for row in raw:
        source, page, chunk = source_identity(row)
        title = clean(row.get("title_candidate"))
        text = clean(row.get("text"))
        fingerprint = (source, page, normalized(title + " " + text[:500]))
        if fingerprint in seen:
            continue
        seen.add(fingerprint)
        score = signal_score(row)
        entry = dict(row)
        entry.update({
            "documentId": source,
            "page": page,
            "chunk": chunk,
            "documentPageId": f"{source}#page={page}" if page is not None else source,
            "signalScore": score,
            "titleQuality": title_quality(title),
            "canonicalMatchV2": match(title, exact, names),
        })
        if page is not None:
            document_pages[source].add(page)
        if score < 5 or title_quality(title) == 0:
            entry["refinementState"] = "suppressed-low-information"
            suppressed.append(entry)
            continue
        entry["refinementState"] = "review-candidate"
        refined.append(entry)
        document_findings[source] += 1

    queues = {
        "likely-existing": [],
        "possible-existing": [],
        "likely-new": [],
        "ambiguous": [],
    }
    for row in refined:
        state = row["canonicalMatchV2"]["state"]
        if state in {"exact-or-alias", "probable-existing"}:
            queues["likely-existing"].append(row)
        elif state == "possible-existing":
            queues["possible-existing"].append(row)
        elif state.startswith("ambiguous"):
            queues["ambiguous"].append(row)
        else:
            queues["likely-new"].append(row)

    for name, rows in queues.items():
        rows.sort(key=lambda r: (-r["signalScore"], r["documentId"], r.get("page") or 0))
        (args.out / f"{name}.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")

    coverage = [
        {"documentId": doc, "pagesWithRawFindings": len(document_pages[doc]), "reviewCandidateCount": document_findings[doc]}
        for doc in sorted(document_pages)
    ]
    summary = {
        "format": "multiversal-refined-forensic-reconciliation",
        "version": "2.0.0",
        "rawFindingCount": len(raw),
        "uniqueFindingCount": len(refined) + len(suppressed),
        "reviewCandidateCount": len(refined),
        "suppressedCount": len(suppressed),
        "canonicalRecordCount": len(canonical),
        "queueCounts": {key: len(value) for key, value in queues.items()},
        "documentCount": len(document_pages),
        "documentCoverage": coverage,
        "authorityNote": "Refinement and matching are triage aids only; no canonical approval is implied.",
    }
    (args.out / "refinement-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (args.out / "suppressed-low-information.json").write_text(json.dumps(suppressed, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
