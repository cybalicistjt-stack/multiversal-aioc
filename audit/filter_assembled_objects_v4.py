#!/usr/bin/env python3
"""Apply hard object-boundary regression rules to Semantic Recovery v4 assemblies.

This stage is intentionally separate from object assembly so its effects are
measurable. It never writes canon.
"""
from __future__ import annotations
import argparse, json, re
from collections import Counter
from pathlib import Path

STAT_FIELD = re.compile(
    r"^(?:AC|HP|DR|EP|MP|SP|CR|DC|Speed|Initiative|Proficiency|"
    r"STR|DEX|CON|INT|WIS|CHA|Armor Class|Hit Points|Saving Throws?|Skills?|"
    r"Damage Resistances?|Damage Immunities?|Damage Vulnerabilities?|"
    r"Condition Immunities?|Senses?|Languages?|Passive Perception|Challenge)\s*[:=]",
    re.I,
)
TABLE_HEADING = re.compile(r"\b(?:frequency|weighted|roll|result|table|chart|cost by|progression|limits by)\b", re.I)
CONTEXTUAL = {
    "campaign use", "investigation hooks", "philosophical arcs", "distorted dungeons",
    "encounter frequency", "encounter frequency weighted", "design notes", "gm notes",
    "using this material", "adventure use", "story use", "common uses",
}
FRAGMENT = re.compile(r"(?:[,;:]$|^(?:ac|hp|speed|str|dex|con|int|wis|cha)\s*:|\b(?:and|or|of|to|with|inside)$)", re.I)
CREATURE_CHILD_ACTION = re.compile(
    r"(?:\((?:\d+\s*/\s*)?round|\breaction\b|\brecharge\s*\d|\bbonus action\b|"
    r"\blegendary action\b|\blair action\b|\bmelee weapon attack\b|\branged weapon attack\b)",
    re.I,
)
CREATURE_SOURCE = re.compile(r"(?:^|/)(?:creatures?|npcs?)(?:/|$)", re.I)


def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def key(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def source_path(row: dict) -> str:
    prov = row.get("provenance") or []
    if prov and isinstance(prov[0], dict):
        return str(prov[0].get("sourcePath") or "")
    return str(row.get("sourcePath") or "")


def reason(row: dict) -> str | None:
    name = str(row.get("name") or "").strip()
    summary = str((row.get("specification") or {}).get("summary") or "").strip()
    family = row.get("objectType")
    path = source_path(row)
    if STAT_FIELD.search(name):
        return "stat-field-identity"
    if key(name) in CONTEXTUAL:
        return "contextual-heading"
    if FRAGMENT.search(name):
        return "fragment-identity"
    if TABLE_HEADING.search(name) and len((row.get("childNodeIds") or [])) == 0:
        return "unreconstructed-table-heading"
    # Named attacks/actions inside creature or NPC source documents are child mechanics,
    # not standalone rule roots. Preserve them as evidence for their owning object.
    if family == "rule" and CREATURE_SOURCE.search(path) and CREATURE_CHILD_ACTION.search(f"{name} {summary}"):
        return "creature-child-action-as-rule"
    # Adventures require multiple adventure-bearing signals, not one contextual word.
    if family == "adventure":
        signals = len(re.findall(r"\b(?:adventure|quest|hook|objective|scene|encounter|clue|reward|module)\b", f"{name} {summary}", re.I))
        if signals < 2:
            return "weak-adventure-boundary"
    # Creature identities must be named objects, not raw stat fields or generic type labels.
    if family == "creature" and re.search(r"\b(?:type|category|immunities|traits|statistics)\b", name, re.I):
        if not re.search(r"\b(?:HP|AC|CR|challenge rating|multiattack|attack)\b", summary, re.I):
            return "weak-creature-boundary"
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--assembly", type=Path, required=True)
    args = ap.parse_args()
    data_path = args.assembly / "assembled-objects.jsonl"
    index_path = args.assembly / "object-assembly-v4-index.json"
    rows = load(data_path)
    kept: list[dict] = []
    rejected = Counter()
    for row in rows:
        why = reason(row)
        if why:
            rejected[why] += 1
        else:
            kept.append(row)
    with data_path.open("w", encoding="utf-8") as handle:
        for row in kept:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    index = json.loads(index_path.read_text(encoding="utf-8"))
    previous = int(index.get("assembledObjectCount", len(rows)))
    merged = Counter(index.get("rejectedCounts") or {})
    merged.update(rejected)
    families = Counter(row.get("objectType") for row in kept)
    index.update({
        "version": "4.3.2",
        "preBoundaryFilterCount": previous,
        "assembledObjectCount": len(kept),
        "familyCounts": dict(families),
        "boundaryFilterRejectedCounts": dict(rejected),
        "rejectedCounts": dict(merged),
        "survivalGates": {
            "rootsExist": int(index.get("rootCandidateCount", 0)) > 0,
            "objectsExist": len(kept) > 0,
            "multipleFamilies": len(families) >= 3,
        },
        "publishedSample": kept[:200],
    })
    index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"before": previous, "after": len(kept), "rejected": dict(rejected), "families": dict(families)}, indent=2))


if __name__ == "__main__":
    main()
