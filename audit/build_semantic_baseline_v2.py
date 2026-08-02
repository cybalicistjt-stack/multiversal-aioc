#!/usr/bin/env python3
"""Compile a precision-first semantic baseline from parser and graph outputs.

This is deliberately conservative. It records every downgrade/rejection reason,
uses independent family evidence channels, deduplicates source fragments, and
never writes canonical content.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

FAMILIES = (
    "ability", "adventure", "creature", "environment", "faction", "item",
    "npc", "rule", "species", "vehicle", "world",
)

FAMILY_TERMS = {
    "ability": ("ability", "spell", "power", "feat", "technique", "maneuver", "ritual", "perk", "activation", "duration", "range"),
    "adventure": ("adventure", "quest", "encounter", "scene", "clue", "objective", "investigation", "hook"),
    "creature": ("creature", "monster", "beast", "aberration", "construct", "undead", "dragon", "demon", "habitat", "attack"),
    "environment": ("environment", "terrain", "hazard", "weather", "biome", "climate", "travel", "zone"),
    "faction": ("faction", "organization", "guild", "corporation", "religion", "empire", "members", "allies", "enemies"),
    "item": ("item", "weapon", "armor", "artifact", "relic", "tool", "potion", "equipment", "component", "weight"),
    "npc": ("npc", "merchant", "warden", "soldier", "medic", "scout", "engineer", "trader", "affiliation", "role"),
    "rule": ("rule", "check", "save", "action", "reaction", "round", "turn", "procedure", "must", "may", "dc "),
    "species": ("species", "subspecies", "ancestry", "heritage", "racial", "appearance", "culture", "adaptation", "trait"),
    "vehicle": ("vehicle", "ship", "starship", "mecha", "mount", "drone", "walker", "crew", "frame", "engine"),
    "world": ("world", "realm", "dimension", "region", "city", "location", "setting", "history", "culture"),
}

PATH_TERMS = {
    "ability": ("ability", "abilities", "magic", "spell", "power", "feat"),
    "adventure": ("adventure", "quest", "module", "investigation"),
    "creature": ("creature", "monster", "bestiary", "aberration"),
    "environment": ("environment", "terrain", "hazard", "biome"),
    "faction": ("faction", "organization", "guild", "religion"),
    "item": ("item", "equipment", "weapon", "armor", "computer"),
    "npc": ("npc", "character"),
    "rule": ("rule", "system", "combat", "creation", "downtime"),
    "species": ("species", "ancestry", "heritage", "race"),
    "vehicle": ("vehicle", "ship", "racing", "mount"),
    "world": ("world", "setting", "lore", "location"),
}

GENERIC = re.compile(
    r"^(?:introduction|overview|description|background|history|notes?|table|"
    r"results?|effects?|chapter|section|tier|level|attributes?|statistics?|"
    r"contents?|appendix|examples?|summary|conclusion|mechanics?|rules?)$", re.I
)
CLAUSE = re.compile(
    r"\b(?:may include|can include|may be|can be|allows? (?:a|the|you)|"
    r"used to|in order to|how to|the following|as follows|is when|are when)$", re.I
)
SECTIONISH = re.compile(
    r"\b(?:guidelines?|procedures?|reference tables?|starting facilities|"
    r"choosing|limits? by|production rate|types? (?:and|&) traits?|"
    r"modules?|components?|categories|overview|introduction)$", re.I
)
NUMBER_PREFIX = re.compile(r"^\s*\d+(?:\.\d+)*[.)]?\s+")
NUMERIC_NOISE = re.compile(r"^(?:\d+[\s,;:/-]*){3,}|\bXP\d|\d+(?:st|nd|rd|th)\s+\d", re.I)
ROLLISH = re.compile(r"\b(?:1d\d+|d100|random table|roll result|roll effect)\b", re.I)
SENTENCE_END = re.compile(r"[.!?]$")

KNOWN_BAD_PATTERNS = (
    re.compile(r"a familiar.s role may include", re.I),
    re.compile(r"security modules", re.I),
    re.compile(r"choosing starting facilities", re.I),
    re.compile(r"limits by cr or frame size", re.I),
    re.compile(r"production rate by facility", re.I),
    re.compile(r"^[+\-=*/]"),
)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def norm(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def normalize_name(value: Any) -> str:
    text = " ".join(str(value or "").split()).strip(" •:-")
    text = NUMBER_PREFIX.sub("", text).strip(" •:-")
    return text


def evidence_hash(row: dict[str, Any]) -> str:
    provenance = row.get("provenance") or []
    payload = json.dumps(
        {
            "candidateId": row.get("candidateId"),
            "name": row.get("name"),
            "objectType": row.get("objectType"),
            "provenance": provenance,
            "summary": (row.get("spec") or {}).get("summary"),
        },
        sort_keys=True,
        ensure_ascii=False,
    )
    return hashlib.sha256(payload.encode("utf-8", "ignore")).hexdigest()


def usable_provenance(row: dict[str, Any]) -> bool:
    for item in row.get("provenance") or []:
        source = str(item.get("sourcePath") or "").strip()
        if source and (item.get("locator") or item.get("page") or item.get("findingId")):
            return True
    return False


def title_reasons(name: str) -> list[str]:
    reasons: list[str] = []
    if not 3 <= len(name) <= 78:
        reasons.append("generic-title")
    if GENERIC.fullmatch(name):
        reasons.append("generic-title")
    if CLAUSE.search(name):
        reasons.append("clause-heading")
    if SECTIONISH.search(name):
        reasons.append("section-heading")
    if SENTENCE_END.search(name):
        reasons.append("clause-heading")
    if NUMERIC_NOISE.search(name):
        reasons.append("numeric-noise")
    if ROLLISH.search(name):
        reasons.append("table-fragment")
    if len(name.split()) > 10 or name[:1].islower():
        reasons.append("clause-heading")
    if sum(ch.isalpha() for ch in name) < max(3, len(name) // 3):
        reasons.append("numeric-noise")
    if any(pattern.search(name) for pattern in KNOWN_BAD_PATTERNS):
        reasons.append("known-regression")
    return sorted(set(reasons))


def substantive_reasons(row: dict[str, Any]) -> list[str]:
    summary = " ".join(str((row.get("spec") or {}).get("summary") or "").split())
    reasons: list[str] = []
    if len(summary) < 100 or len(re.findall(r"[A-Za-z]{3,}", summary)) < 16:
        reasons.append("non-substantive")
    if row.get("sourceBlockType") == "table" and not (row.get("spec") or {}).get("mechanicSignals"):
        reasons.append("table-fragment")
    return reasons


def family_channel_scores(row: dict[str, Any], name: str) -> tuple[dict[str, int], dict[str, list[str]]]:
    summary = str((row.get("spec") or {}).get("summary") or "")
    path = str(((row.get("provenance") or [{}])[0]).get("sourcePath") or "").lower().replace("\\", "/")
    title_text = name.lower()
    body_text = summary.lower()
    fields = row.get("spec") or {}
    scores: dict[str, int] = {}
    channels: dict[str, list[str]] = defaultdict(list)
    for family in FAMILIES:
        score = 0
        for term in FAMILY_TERMS[family]:
            if term in title_text:
                score += 4
                channels[family].append("title")
            if term in body_text:
                score += 1
                channels[family].append("body")
        if any(term in path for term in PATH_TERMS[family]):
            score += 4
            channels[family].append("path")
        family_fields = {
            "ability": ("activation", "duration", "range", "prerequisites", "effects", "scaling"),
            "creature": ("hp", "ac", "speed", "attacks", "ecology", "variants"),
            "item": ("itemCategory", "weight", "properties", "crafting"),
            "species": ("appearance", "culture", "traits", "adaptations", "progression"),
            "npc": ("role", "speciesId", "affiliations", "abilities"),
            "vehicle": ("vehicleClass", "crew", "components", "upgrades"),
            "environment": ("hazards", "weather", "adaptations", "travelRules"),
            "world": ("locations", "cultures", "factions"),
            "faction": ("goals", "members", "relationships"),
            "adventure": ("scenes", "encounters", "clues", "objectives"),
            "rule": ("procedure", "exceptions", "optional"),
        }[family]
        if any(key in fields for key in family_fields):
            score += 3
            channels[family].append("fields")
        scores[family] = score
        channels[family] = sorted(set(channels[family]))
    return scores, dict(channels)


def graph_degree(graph: dict[str, Any]) -> Counter:
    degree: Counter = Counter()
    for edge in graph.get("edges") or []:
        if edge.get("relationshipType") == "supportedBy":
            continue
        source = edge.get("sourceId")
        target = edge.get("targetId")
        if source:
            degree[source] += 1
        if target:
            degree[target] += 1
    return degree


def classify(row: dict[str, Any], degree: Counter) -> dict[str, Any]:
    name = normalize_name(row.get("name"))
    reasons: list[str] = []
    if not usable_provenance(row):
        reasons.append("missing-provenance")
    reasons.extend(title_reasons(name))
    reasons.extend(substantive_reasons(row))

    scores, channels = family_channel_scores(row, name)
    ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
    proposed = str(row.get("objectType") or "")
    winner, winner_score = ranked[0]
    runner_score = ranked[1][1] if len(ranked) > 1 else 0
    margin = winner_score - runner_score
    proposed_channels = channels.get(proposed, [])

    if winner != proposed and winner_score >= scores.get(proposed, 0) + 3:
        reasons.append("family-conflict")
    if margin < 3 or len(proposed_channels) < 2:
        reasons.append("family-ambiguous")

    semantic_edges = degree.get(row.get("candidateId"), 0)
    missing_count = len(row.get("missingFields") or [])
    identity_points = 0
    summary = str((row.get("spec") or {}).get("summary") or "")
    if norm(name) and norm(name) in norm(summary[:350]):
        identity_points += 2
    if row.get("sourceBlockType") in {"stat-block", "mechanic-block"}:
        identity_points += 1
    if len(name.split()) <= 6:
        identity_points += 1
    if semantic_edges:
        identity_points += 1

    confidence = 45
    confidence += min(20, scores.get(proposed, 0) * 2)
    confidence += min(10, margin * 2)
    confidence += identity_points * 4
    confidence += min(6, semantic_edges * 2)
    confidence -= min(18, missing_count * 3)
    confidence -= 25 * len(set(reasons) & {
        "missing-provenance", "clause-heading", "section-heading", "table-fragment",
        "numeric-noise", "generic-title", "non-substantive", "family-conflict",
        "known-regression",
    })
    confidence -= 10 if "family-ambiguous" in reasons else 0
    confidence = max(0, min(100, confidence))

    hard = {
        "missing-provenance", "clause-heading", "section-heading", "table-fragment",
        "numeric-noise", "generic-title", "non-substantive", "family-conflict",
        "known-regression",
    }
    if set(reasons) & hard or confidence < 70:
        tier = "rejected"
    elif confidence >= 85 and margin >= 3 and len(proposed_channels) >= 2:
        tier = "ready"
    else:
        tier = "needs-review"

    return {
        **row,
        "name": name,
        "evidenceHash": evidence_hash(row),
        "baselineV2": {
            "tier": tier,
            "confidence": round(confidence, 2),
            "reasons": sorted(set(reasons)),
            "familyScores": scores,
            "familyChannels": channels,
            "winningFamily": winner,
            "familyMargin": margin,
            "identityPoints": identity_points,
            "semanticGraphDegree": semantic_edges,
        },
        "authority": "Semantic Baseline v2 candidate only; no canonical write is authorized.",
    }


def deduplicate(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    kept: list[dict[str, Any]] = []
    duplicates: list[dict[str, Any]] = []
    seen: dict[tuple[str, str, str], dict[str, Any]] = {}
    for row in sorted(rows, key=lambda x: (-x["baselineV2"]["confidence"], x.get("candidateId", ""))):
        source = str(((row.get("provenance") or [{}])[0]).get("sourcePath") or "")
        key = (row.get("objectType", ""), norm(row.get("name")), source.lower())
        if key in seen:
            row["baselineV2"]["tier"] = "rejected"
            row["baselineV2"]["reasons"] = sorted(set(row["baselineV2"]["reasons"] + ["duplicate-fragment"]))
            duplicates.append(row)
        else:
            seen[key] = row
            kept.append(row)
    return kept, duplicates


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parsed", type=Path, required=True)
    parser.add_argument("--graph", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--ready-limit", type=int, default=500)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    candidates = read_jsonl(args.parsed / "family-parser-candidates.jsonl")
    graph = read_json(args.graph / "canonical-knowledge-graph.json")
    degree = graph_degree(graph)
    classified = [classify(row, degree) for row in candidates]
    classified, duplicates = deduplicate(classified)
    classified.extend(duplicates)

    ready = [row for row in classified if row["baselineV2"]["tier"] == "ready"]
    needs = [row for row in classified if row["baselineV2"]["tier"] == "needs-review"]
    rejected = [row for row in classified if row["baselineV2"]["tier"] == "rejected"]
    ready.sort(key=lambda x: (-x["baselineV2"]["confidence"], x["objectType"], x["name"].lower()))
    needs.sort(key=lambda x: (-x["baselineV2"]["confidence"], x["objectType"], x["name"].lower()))

    ready = ready[: args.ready_limit]
    reason_counts = Counter(reason for row in rejected + needs for reason in row["baselineV2"]["reasons"])
    family_counts = Counter(row["objectType"] for row in ready)
    connected = sum(row["baselineV2"]["semanticGraphDegree"] > 0 for row in ready)
    duplicate_rate = len(duplicates) / max(1, len(classified))

    known_bad_ready = [
        row["candidateId"] for row in ready
        if any(pattern.search(row["name"]) for pattern in KNOWN_BAD_PATTERNS)
    ]
    gates = {
        "readyCandidatesExist": len(ready) > 0,
        "readyProvenanceComplete": all(usable_provenance(row) for row in ready),
        "familyMarginsValid": all(row["baselineV2"]["familyMargin"] >= 3 for row in ready),
        "familyChannelsValid": all(len(row["baselineV2"]["familyChannels"].get(row["objectType"], [])) >= 2 for row in ready),
        "knownRegressionsAbsent": not known_bad_ready,
        "duplicateRateBelowTwoPercent": duplicate_rate < 0.02,
        "graphFieldContractVerified": all("sourceId" in edge and "targetId" in edge and "relationshipType" in edge for edge in graph.get("edges", [])[:100]),
    }

    summary = {
        "format": "multiversal-semantic-baseline-v2-index",
        "version": "2.0.0",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "inputCandidateCount": len(candidates),
        "readyCount": len(ready),
        "needsReviewCount": len(needs),
        "rejectedCount": len(rejected),
        "duplicateCount": len(duplicates),
        "duplicateRate": round(duplicate_rate, 5),
        "readyFamilyCounts": dict(family_counts),
        "connectedReadyCount": connected,
        "rejectionReasonCounts": dict(reason_counts),
        "knownBadReady": known_bad_ready,
        "gates": gates,
        "engineeringBaselinePassed": all(gates.values()),
        "publishedReadySample": ready[:250],
        "publishedNeedsReviewSample": needs[:100],
        "authorityNote": "Engineering baseline only. Final acceptance requires stratified expert/owner review.",
    }

    write_jsonl(args.out / "semantic-baseline-v2-ready.jsonl", ready)
    write_jsonl(args.out / "semantic-baseline-v2-needs-review.jsonl", needs)
    write_jsonl(args.out / "semantic-baseline-v2-rejected.jsonl", rejected)
    write_json(args.out / "semantic-baseline-v2-error-report.json", {
        "format": "multiversal-semantic-baseline-v2-error-report",
        "reasonCounts": dict(reason_counts),
        "duplicateCount": len(duplicates),
        "knownBadReady": known_bad_ready,
        "rejectedSample": rejected[:250],
    })
    write_json(args.out / "semantic-baseline-v2-index.json", summary)
    print(json.dumps({key: summary[key] for key in (
        "inputCandidateCount", "readyCount", "needsReviewCount", "rejectedCount",
        "readyFamilyCounts", "connectedReadyCount", "gates", "engineeringBaselinePassed"
    )}, indent=2))


if __name__ == "__main__":
    main()
