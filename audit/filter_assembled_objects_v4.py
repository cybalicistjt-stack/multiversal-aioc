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
    r"^(?:AC|HP|DR|EP|MP|SP|CR|DC|Speed|Initiative|Proficiency|Alignment|Size|"
    r"STR|DEX|CON|INT|WIS|CHA|Armor Class|Hit Points|Saving Throws?|Skills?|"
    r"Damage Resistances?|Damage Immunities?|Damage Vulnerabilities?|"
    r"Condition Immunities?|Senses?|Languages?|Passive Perception|Challenge)\s*[:=]",
    re.I,
)
TABLE_HEADING = re.compile(
    r"\b(?:frequency|weighted|roll|result|table|chart|cost by|progression|limits by|"
    r"activity effect|purpose\s*/\s*influence|unlock cost|effect notes?)\b",
    re.I,
)
CONTEXTUAL = {
    "campaign use", "investigation hooks", "philosophical arcs", "distorted dungeons",
    "encounter frequency", "encounter frequency weighted", "design notes", "gm notes",
    "using this material", "adventure use", "story use", "common uses", "gameplay use",
    "reward exploration", "introduce the hooks", "structuring the adventure",
    "structuring a session for maximum engagement",
    "structuring a mystery without making it too obvious or confusing",
    "protocols for other warden factions", "dynamic clue cards",
}
FRAGMENT = re.compile(
    r"(?:[,;:]$|^(?:ac|hp|speed|str|dex|con|int|wis|cha)\s*:|"
    r"\b(?:and|or|of|to|with|inside)$|^lbs?\.?\s*\d|^\d+\s*(?:gp|sp|cp|lb))",
    re.I,
)
CREATURE_CHILD_ACTION = re.compile(
    r"(?:\((?:\d+\s*/\s*)?round|\breaction\b|\brecharge\s*\d|\bbonus action\b|"
    r"\blegendary action\b|\blair action\b|\bmelee weapon attack\b|\branged weapon attack\b|"
    r"\bmultiattack\b|\bpassive\b)",
    re.I,
)
CREATURE_SOURCE = re.compile(r"(?:^|/)(?:creatures?|npcs?)(?:/|$)", re.I)
PROGRESSION_HEADING = re.compile(
    r"\b(?:path abilities|branch\s*:|tier\s*\d|prestige path|stat guidelines|"
    r"ability tree|skill tree|progression track)\b",
    re.I,
)
TEMPLATE_HEADING = re.compile(
    r"^(?:event name\s*:|name\s*:|title\s*:|example\s*:|template\b|sample\b)",
    re.I,
)
FACTION_NOUN = re.compile(
    r"\b(?:faction|guild|order|council|clan|tribe|corporation|company|syndicate|"
    r"empire|kingdom|government|church|cult|society|collective|wardens?|alliance|"
    r"coalition|organization|organisation|house|family|crew|gang|network)\b",
    re.I,
)
INSTRUCTIONAL_ADVENTURE = re.compile(
    r"\b(?:structuring|how to|gm tip|guide|framework|reward exploration|introduce the hooks|"
    r"clue cards?|session engagement|mystery design)\b",
    re.I,
)


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
    combined = f"{name} {summary}"

    if STAT_FIELD.search(name):
        return "stat-field-identity"
    if key(name) in CONTEXTUAL:
        return "contextual-heading"
    if TEMPLATE_HEADING.search(name):
        return "template-placeholder-identity"
    if FRAGMENT.search(name):
        return "fragment-identity"
    if TABLE_HEADING.search(name) and len((row.get("childNodeIds") or [])) == 0:
        return "unreconstructed-table-heading"
    if PROGRESSION_HEADING.search(name) and re.search(r"\b(?:tier\s*\d|xp cost|unlock tier|\d+\.)\b", summary, re.I):
        return "progression-container-as-object"

    # Named attacks/actions inside creature or NPC source documents are child mechanics,
    # not standalone object roots. Preserve them as evidence for their owning object.
    if CREATURE_SOURCE.search(path) and CREATURE_CHILD_ACTION.search(combined):
        if family in {"rule", "creature", "npc"}:
            return "creature-child-action-as-object"

    if family == "adventure":
        # Guidance, templates, props, and child sections of a module are not adventures.
        if INSTRUCTIONAL_ADVENTURE.search(name):
            return "adventure-guidance-as-object"
        signals = len(re.findall(r"\b(?:adventure|quest|objective|scene|encounter|module|scenario)\b", combined, re.I))
        named_place_or_module = bool(re.search(r"\b(?:the|of|at|in)\b", name, re.I) and len(name.split()) >= 3)
        if signals < 2 and not named_place_or_module:
            return "weak-adventure-boundary"

    if family == "creature":
        if re.search(r"\b(?:type|category|immunities|traits|statistics|stat guidelines|path abilities)\b", name, re.I):
            return "creature-container-as-object"
        # A creature identity must not itself be a stat label or generic action.
        if re.fullmatch(r"(?:multiattack|actions?|traits?|reactions?|legendary actions?)", name, re.I):
            return "creature-child-section-as-object"

    if family == "faction":
        # Branches, power trees, tabular headers, protocols, and gameplay guidance are not factions.
        if PROGRESSION_HEADING.search(name) or TABLE_HEADING.search(name):
            return "faction-progression-or-table-as-object"
        if key(name) in CONTEXTUAL:
            return "faction-contextual-heading"
        # Require an organization-bearing signal in either the identity or evidence.
        if not FACTION_NOUN.search(combined):
            return "weak-faction-boundary"

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
        "version": "4.3.3",
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
