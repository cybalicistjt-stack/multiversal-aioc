#!/usr/bin/env python3
"""CAPP-10 deterministic nonvisual appearance description formatter."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ORDER = [
    "topology",
    "surface",
    "coloration",
    "distinguishing_features",
    "wardrobe",
    "equipment_projection",
    "renderer_support",
]
LABELS = {
    "topology": "Body topology",
    "surface": "Surface and covering",
    "coloration": "Coloration",
    "distinguishing_features": "Distinguishing features",
    "wardrobe": "Presentation wardrobe",
    "equipment_projection": "Equipment projection",
    "renderer_support": "Renderer support",
}


def allowed(item: dict[str, Any], permissions: set[str]) -> bool:
    return set(item.get("permission_tags", [])).issubset(permissions)


def normalize_items(raw: Any, permissions: set[str]) -> list[str]:
    if raw is None:
        return []
    if not isinstance(raw, list):
        raw = [raw]
    values: list[str] = []
    for item in raw:
        if isinstance(item, str):
            values.append(item)
        elif isinstance(item, dict) and allowed(item, permissions):
            text = item.get("text")
            if isinstance(text, str) and text.strip():
                values.append(text.strip())
    return sorted(set(values), key=lambda x: x.casefold())


def describe(payload: dict[str, Any]) -> dict[str, Any]:
    permissions = set(payload.get("permission_projection", []))
    sections = payload.get("sections", {})
    rendered_sections: list[dict[str, Any]] = []
    for key in ORDER:
        values = normalize_items(sections.get(key), permissions)
        if values:
            rendered_sections.append({"section": key, "label": LABELS[key], "items": values})

    changes = []
    for change in payload.get("changes", []):
        if isinstance(change, dict) and allowed(change, permissions):
            field = change.get("field")
            before = change.get("before")
            after = change.get("after")
            if field and before != after:
                changes.append({"field": field, "before": before, "after": after})
    changes.sort(key=lambda x: str(x["field"]))

    text_parts = []
    for section in rendered_sections:
        text_parts.append(f"{section['label']}: " + "; ".join(section["items"]) + ".")
    if changes:
        text_parts.append("Changes: " + "; ".join(
            f"{c['field']}: {c['before']} to {c['after']}" for c in changes
        ) + ".")
    if not text_parts:
        text_parts.append("No authorized appearance description is available.")

    return {
        "schema_version": "0.1.0",
        "work_item_id": "CAPP-10",
        "description_sections": rendered_sections,
        "change_announcements": changes,
        "text": " ".join(text_parts),
        "permission_filtered": True,
        "character_truth_changed": False,
    }


def self_test() -> None:
    payload = {
        "permission_projection": [],
        "sections": {
            "topology": ["four arms and two legs"],
            "coloration": ["blue", {"text": "secret red marking", "permission_tags": ["gm_only"]}],
            "renderer_support": ["partial: secondary armwear asset missing"],
        },
        "changes": [
            {"field": "hair", "before": "short", "after": "long"},
            {"field": "secret", "before": "a", "after": "b", "permission_tags": ["gm_only"]},
        ],
    }
    one = describe(payload)
    two = describe(payload)
    assert one == two
    assert "secret" not in one["text"]
    assert "four arms and two legs" in one["text"]
    assert len(one["change_announcements"]) == 1
    assert one["character_truth_changed"] is False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("CAPP-10 self-test: PASS")
        return 0
    if not args.input:
        parser.error("--input is required unless --self-test is used")
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = describe(payload)
    text = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
