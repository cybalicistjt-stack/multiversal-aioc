#!/usr/bin/env python3
"""Post-process forensic audit findings into reviewable reconciliation sets."""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def clean(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def normalized_name(value: str) -> str:
    value = clean(value).lower()
    value = re.sub(r"^[\d\W_]+", "", value)
    value = re.sub(r"\([^)]*\)", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return clean(value)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            rows.append({"parseError": True, "raw": line})
    return rows


def load_canonical(path: Path | None) -> tuple[dict[str, dict[str, Any]], dict[str, list[str]]]:
    if not path or not path.exists():
        return {}, {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload.get("records", payload if isinstance(payload, list) else [])
    by_id: dict[str, dict[str, Any]] = {}
    by_name: dict[str, list[str]] = defaultdict(list)
    for record in records:
        rid = clean(record.get("id") or record.get("stableId"))
        name = normalized_name(record.get("name") or record.get("title"))
        if rid:
            by_id[rid] = record
        if rid and name:
            by_name[name].append(rid)
    return by_id, dict(by_name)


def similarity(a: str, b: str) -> float:
    aa, bb = set(normalized_name(a).split()), set(normalized_name(b).split())
    if not aa or not bb:
        return 0.0
    return len(aa & bb) / len(aa | bb)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--audit-output", type=Path, default=Path("audit-output"))
    p.add_argument("--canonical", type=Path)
    args = p.parse_args()
    out = args.audit_output
    findings = load_jsonl(out / "findings.jsonl") + load_jsonl(out / "csv-findings.jsonl")
    canonical, canonical_names = load_canonical(args.canonical)

    name_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for finding in findings:
        key = normalized_name(finding.get("title_candidate", ""))
        if key:
            name_groups[key].append(finding)

    duplicate_groups = []
    for name, group in sorted(name_groups.items()):
        if len(group) < 2:
            continue
        duplicate_groups.append({
            "normalizedName": name,
            "count": len(group),
            "sources": sorted({f.get("source_path", "") for f in group}),
            "locators": [f.get("locator") for f in group],
            "findingIds": [f.get("finding_id") for f in group],
            "reviewState": "needs-review"
        })

    candidate_matches = []
    for finding in findings:
        if finding.get("canonical_match"):
            continue
        title = clean(finding.get("title_candidate"))
        scored = []
        for cname, ids in canonical_names.items():
            score = similarity(title, cname)
            if score >= 0.6:
                scored.append((score, cname, ids))
        scored.sort(reverse=True)
        if scored:
            candidate_matches.append({
                "findingId": finding.get("finding_id"),
                "title": title,
                "candidates": [
                    {"score": round(score, 3), "normalizedName": cname, "canonicalIds": ids}
                    for score, cname, ids in scored[:5]
                ],
                "decision": "unreviewed"
            })

    csv_schemas: dict[str, dict[str, Any]] = {}
    for finding in findings:
        if finding.get("source_kind") != "csv":
            continue
        shape = finding.get("table_shape") or {}
        cols = tuple(clean(x).lower() for x in shape.get("columns", []) if clean(x))
        key = "|".join(cols)
        rec = csv_schemas.setdefault(key, {"columns": list(cols), "rowCount": 0, "files": set(), "families": Counter()})
        rec["rowCount"] += 1
        rec["files"].add(finding.get("source_path", ""))
        rec["families"].update((finding.get("family_scores") or {}).keys())
    schema_rows = []
    for key, rec in csv_schemas.items():
        schema_rows.append({
            "schemaKey": key,
            "columns": rec["columns"],
            "rowCount": rec["rowCount"],
            "files": sorted(rec["files"]),
            "familySignals": dict(rec["families"]),
            "reviewState": "unclassified"
        })

    page_density: dict[int, int] = Counter()
    for finding in findings:
        loc = clean(finding.get("locator"))
        m = re.search(r"page:(\d+)", loc)
        if m:
            page_density[int(m.group(1))] += 1

    report = {
        "format": "multiversal-forensic-reconciliation-report",
        "version": "1.0.0",
        "findingCount": len(findings),
        "canonicalRecordCount": len(canonical),
        "duplicateGroupCount": len(duplicate_groups),
        "candidateMatchCount": len(candidate_matches),
        "csvSchemaCount": len(schema_rows),
        "pagesWithFindings": len(page_density),
        "topFindingPages": [{"page": p, "findings": n} for p, n in page_density.most_common(100)]
    }

    out.mkdir(parents=True, exist_ok=True)
    (out / "duplicate-groups.json").write_text(json.dumps(duplicate_groups, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "candidate-matches.json").write_text(json.dumps(candidate_matches, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "csv-schema-registry.json").write_text(json.dumps(schema_rows, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "reconciliation-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
