#!/usr/bin/env python3
"""Build a hierarchical, section-aware evidence model from forensic findings.

The output preserves parent/child structure and prevents generic child labels such
as Actions, Traits, and Effects from becoming independent object identities.
Outputs are evidence only and never modify canon.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

NUMBERED_HEADING = re.compile(r"^\s*(?P<num>\d+(?:\.\d+){0,5})[.)]?\s+(?P<title>\S.*)$")
ALL_CAPS = re.compile(r"^[A-Z][A-Z0-9 &'’:/\-]{3,}$")
BULLET = re.compile(r"^\s*(?:[-•*◦▪‣]|\d+[.)]|[A-Z][.)])\s+")
MECHANIC = re.compile(r"\b(?:\d+d\d+|DC\s*\d+|once per|bonus action|reaction|rounds?|turns?|feet|ft\.?|miles?|hours?|minutes?|HP|AC|damage|save|check)\b", re.I)
STAT = re.compile(r"\b(?:HP|AC|DR|EP|MP|SP|Speed|Attack|Damage|Range|Duration|Cost|Level|Tier)\s*[:=]", re.I)
CONTAINER = re.compile(r"^(?:actions?|reactions?|traits?|features?|effects?|statistics?|stats?|objectives?|encounters?|equipment|inventory|abilities|attacks?|defenses?|ecology|variants?|notes?|description|appearance|culture|society|history|background|prerequisites?|requirements?|scaling|upgrades?|components?|tables?|examples?)$", re.I)
CLAUSE = re.compile(r"\b(?:may include|can include|includes the following|are as follows|can be|allows you to|used to|consists of|such as)$", re.I)
OBJECT_HINT = re.compile(r"\b(?:creature|species|item|weapon|armor|vehicle|world|realm|faction|guild|adventure|quest|ability|spell|power|rule|procedure|hazard|environment|NPC)\b", re.I)


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def stable(*parts: object) -> str:
    raw = "\n".join(str(p or "") for p in parts)
    return hashlib.sha256(raw.encode("utf-8", "ignore")).hexdigest()[:20]


def page_of(locator: object) -> int | None:
    match = re.search(r"page:(\d+)", str(locator or ""))
    return int(match.group(1)) if match else None


def clean(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def strip_marker(line: str) -> str:
    return re.sub(r"^[^\w\d]+", "", clean(line)).strip(" :-")


def heading_level(line: str) -> tuple[int, str] | None:
    text = strip_marker(line)
    if not text or len(text) > 100 or len(text.split()) > 14:
        return None
    numbered = NUMBERED_HEADING.match(text)
    if numbered:
        title = clean(numbered.group("title")).strip(" :-")
        if not title or title.endswith(('.', '?', '!')) or CLAUSE.search(title):
            return None
        return min(6, numbered.group("num").count(".") + 1), title
    if ALL_CAPS.match(text):
        return 1, text.title()
    if text.endswith(('.', '?', '!')) or CLAUSE.search(text):
        return None
    words = text.split()
    title_like = sum(w[:1].isupper() or w.lower() in {"of", "and", "or", "the", "to", "for", "in", "with"} for w in words)
    if 1 <= len(words) <= 10 and title_like / len(words) >= 0.72:
        return 2, text
    return None


def block_type(lines: list[str], text: str) -> str:
    nonempty = [line for line in lines if clean(line)]
    list_ratio = sum(bool(BULLET.match(line)) for line in nonempty) / max(1, len(nonempty))
    table_ratio = sum(
        line.count("|") >= 2 or len(re.split(r"\s{2,}", line.strip())) >= 3
        for line in nonempty
    ) / max(1, len(nonempty))
    if table_ratio >= 0.45:
        return "table"
    if STAT.search(text) and sum(bool(STAT.search(line)) for line in nonempty) >= 2:
        return "stat-block"
    if list_ratio >= 0.45:
        return "list"
    if MECHANIC.search(text):
        return "mechanic-block"
    return "prose"


def role_for(title: str | None, body: str, kind: str) -> str:
    title = clean(title)
    if title and CONTAINER.match(strip_marker(title)):
        return "container"
    if kind == "table":
        return "table"
    if kind == "stat-block":
        return "object-detail"
    if title and OBJECT_HINT.search(title):
        return "object-section"
    if MECHANIC.search(body):
        return "mechanic-section"
    return "narrative-section"


def source_relative(path: str) -> str:
    normalized = path.replace("\\", "/")
    marker = "/audit-work/corpus/"
    return normalized.split(marker, 1)[1] if marker in normalized else normalized


def emit_node(nodes: list[dict], source: str, page: int | None, item: dict, order: int,
              title: str | None, level: int, parent_id: str | None, ancestors: list[dict],
              body_lines: list[str]) -> dict | None:
    body = "\n".join(body_lines).strip()
    if not title and not body:
        return None
    kind = block_type(body_lines, body)
    role = role_for(title, body, kind)
    title_text = clean(title) or None
    node_id = "section-" + stable(source, page, item.get("finding_id"), order, title_text, body[:300])
    ancestor_path = [entry["title"] for entry in ancestors if entry.get("title")]
    parent_object = next((entry["title"] for entry in reversed(ancestors) if entry.get("role") == "object-section"), None)
    node = {
        "nodeId": node_id,
        "parentId": parent_id,
        "sourcePath": source,
        "sourceRelativePath": source_relative(source),
        "pageStart": page,
        "pageEnd": page,
        "locator": item.get("locator"),
        "findingId": item.get("finding_id"),
        "readingOrder": order,
        "level": level,
        "title": title_text,
        "headingPath": ancestor_path + ([title_text] if title_text else []),
        "parentObjectTitle": parent_object,
        "sectionRole": role,
        "blockType": kind,
        "text": body,
        "lineCount": len(body_lines),
        "mechanicSignals": item.get("mechanic_signals") or [],
        "familyScores": item.get("family_scores") or {},
        "tableShape": item.get("table_shape"),
        "provenanceComplete": bool(source and source != "unknown" and item.get("locator")),
    }
    node["contentHash"] = hashlib.sha256(
        json.dumps({k: node[k] for k in ("sourceRelativePath", "pageStart", "title", "text")}, sort_keys=True).encode("utf-8")
    ).hexdigest()
    nodes.append(node)
    return node


def parse_finding(source: str, page: int | None, item: dict, start_order: int) -> tuple[list[dict], int]:
    lines = (item.get("text") or "").splitlines()
    nodes: list[dict] = []
    stack: list[dict] = []
    current_title: str | None = None
    current_level = 0
    current_parent: str | None = None
    current_ancestors: list[dict] = []
    body: list[str] = []
    order = start_order

    def flush() -> None:
        nonlocal body, order
        node = emit_node(nodes, source, page, item, order, current_title, current_level,
                         current_parent, current_ancestors, body)
        if node:
            order += 1
        body = []

    for raw in lines:
        line = raw.strip()
        if not line:
            if body and len("\n".join(body)) > 900:
                flush()
            continue
        parsed = heading_level(line)
        if parsed:
            flush()
            level, title = parsed
            while stack and stack[-1]["level"] >= level:
                stack.pop()
            current_parent = stack[-1]["nodeId"] if stack else None
            current_ancestors = list(stack)
            current_title = title
            current_level = level
            # Provisional stack node. It is replaced with the emitted node on the next flush.
            provisional = {
                "nodeId": "pending-" + stable(source, page, item.get("finding_id"), order, title),
                "title": title,
                "level": level,
                "role": "container" if CONTAINER.match(strip_marker(title)) else ("object-section" if OBJECT_HINT.search(title) else "section"),
            }
            stack.append(provisional)
        else:
            body.append(raw)
    flush()

    # Repair provisional ancestry using nearest emitted title at each level.
    last_by_level: dict[int, dict] = {}
    for node in nodes:
        level = node["level"]
        last_by_level = {k: v for k, v in last_by_level.items() if k < level}
        parent = last_by_level.get(level - 1)
        if parent:
            node["parentId"] = parent["nodeId"]
            node["headingPath"] = parent["headingPath"] + ([node["title"]] if node.get("title") else [])
            node["parentObjectTitle"] = parent.get("parentObjectTitle") or (parent.get("title") if parent.get("sectionRole") == "object-section" else None)
        last_by_level[level] = node
    return nodes, order


def build_chunks(nodes: list[dict]) -> list[dict]:
    children: dict[str, list[dict]] = defaultdict(list)
    by_id = {node["nodeId"]: node for node in nodes}
    for node in nodes:
        if node.get("parentId"):
            children[node["parentId"]].append(node)
    chunks: list[dict] = []
    for node in nodes:
        title = node.get("title")
        role = node.get("sectionRole")
        parent = by_id.get(node.get("parentId"))
        effective_title = title
        if role == "container" and parent:
            effective_title = parent.get("title")
        context_titles = [x for x in node.get("headingPath", []) if x]
        context_prefix = " > ".join(context_titles[-4:])
        child_labels = [child.get("title") for child in children.get(node["nodeId"], []) if child.get("sectionRole") == "container"]
        searchable = "\n".join(part for part in [context_prefix, node.get("text", "")] if part).strip()
        if len(searchable) < 40 and parent:
            searchable = "\n".join(part for part in [" > ".join(parent.get("headingPath", [])[-4:]), parent.get("text", ""), searchable] if part).strip()
        chunk = {
            "chunkId": "chunk-" + stable(node["nodeId"], searchable[:500]),
            "nodeId": node["nodeId"],
            "parentId": node.get("parentId"),
            "sourcePath": node["sourcePath"],
            "sourceRelativePath": node["sourceRelativePath"],
            "pageStart": node["pageStart"],
            "pageEnd": node["pageEnd"],
            "locator": node.get("locator"),
            "findingId": node.get("findingId"),
            "title": effective_title,
            "localTitle": title,
            "headingPath": node.get("headingPath", []),
            "parentObjectTitle": node.get("parentObjectTitle"),
            "sectionRole": role,
            "blockType": node.get("blockType"),
            "text": node.get("text", ""),
            "searchableText": searchable,
            "childContainerLabels": [x for x in child_labels if x],
            "mechanicSignals": node.get("mechanicSignals", []),
            "familyScores": node.get("familyScores", {}),
            "provenanceComplete": node.get("provenanceComplete", False),
            "contentHash": node["contentHash"],
            "identityEligible": bool(effective_title and role not in {"container", "table"} and not CONTAINER.match(strip_marker(effective_title))),
        }
        chunks.append(chunk)
    return chunks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    rows = load_jsonl(args.input / "findings.jsonl") + load_jsonl(args.input / "csv-findings.jsonl")
    grouped: dict[tuple[str, int | None], list[dict]] = defaultdict(list)
    for row in rows:
        grouped[(row.get("source_path") or "unknown", page_of(row.get("locator")))].append(row)

    nodes: list[dict] = []
    order_by_source: dict[str, int] = defaultdict(int)
    for (source, page), items in sorted(grouped.items(), key=lambda pair: (pair[0][0], pair[0][1] or 0)):
        for item in items:
            parsed, next_order = parse_finding(source, page, item, order_by_source[source])
            nodes.extend(parsed)
            order_by_source[source] = next_order

    chunks = build_chunks(nodes)
    role_counts = Counter(node["sectionRole"] for node in nodes)
    type_counts = Counter(node["blockType"] for node in nodes)
    summary = {
        "format": "multiversal-hierarchical-document-index",
        "version": "2.0.0",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceCount": len({node["sourcePath"] for node in nodes}),
        "nodeCount": len(nodes),
        "chunkCount": len(chunks),
        "sectionRoleCounts": dict(role_counts),
        "blockTypeCounts": dict(type_counts),
        "identityEligibleChunkCount": sum(chunk["identityEligible"] for chunk in chunks),
        "containerChunkCount": sum(chunk["sectionRole"] == "container" for chunk in chunks),
        "provenanceCompleteCount": sum(chunk["provenanceComplete"] for chunk in chunks),
        "publishedNodeSample": nodes[:200],
        "publishedChunkSample": chunks[:200],
        "authorityNote": "Hierarchical nodes and chunks are source evidence, not canonical objects.",
    }
    (args.out / "hierarchical-document-index.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    with (args.out / "hierarchical-nodes.jsonl").open("w", encoding="utf-8") as handle:
        for node in nodes:
            handle.write(json.dumps(node, ensure_ascii=False) + "\n")
    with (args.out / "section-aware-chunks.jsonl").open("w", encoding="utf-8") as handle:
        for chunk in chunks:
            handle.write(json.dumps(chunk, ensure_ascii=False) + "\n")
    print(json.dumps({k: summary[k] for k in ("sourceCount", "nodeCount", "chunkCount", "sectionRoleCounts", "identityEligibleChunkCount")}, indent=2))


if __name__ == "__main__":
    main()
