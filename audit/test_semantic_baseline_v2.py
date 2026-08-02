#!/usr/bin/env python3
"""Regression tests for Semantic Baseline v2.

These fixtures encode failure modes observed in prior production runs. They are
not a substitute for a manually annotated corpus, but they stop known defects
from silently returning.
"""
from __future__ import annotations

import unittest
from collections import Counter

from build_semantic_baseline_v2 import classify


def candidate(name: str, family: str, summary: str, path: str, block_type: str = "prose", **spec):
    base_spec = {"summary": summary, **spec}
    templates = {
        "ability": {"prerequisites": [], "effects": [], "scaling": []},
        "adventure": {"scenes": [], "encounters": [], "clues": [], "objectives": []},
        "creature": {"attacks": [], "traits": [], "ecology": None, "variants": []},
        "environment": {"hazards": [], "weather": [], "adaptations": [], "travelRules": []},
        "faction": {"goals": [], "members": [], "relationships": []},
        "item": {"itemCategory": None, "weight": None, "properties": [], "crafting": None},
        "npc": {"role": None, "speciesId": None, "affiliations": [], "abilities": []},
        "rule": {"procedure": [], "exceptions": [], "optional": False},
        "species": {"appearance": None, "culture": None, "traits": [], "adaptations": [], "progression": []},
        "vehicle": {"vehicleClass": None, "crew": None, "components": [], "upgrades": []},
        "world": {"locations": [], "cultures": [], "factions": [], "rules": []},
    }
    base_spec.update(templates[family])
    return {
        "candidateId": f"fixture.{family}.{name}",
        "objectType": family,
        "name": name,
        "sourceBlockType": block_type,
        "provenance": [{"sourcePath": path, "locator": "page:1;chunk:1", "page": 1, "findingId": "fixture"}],
        "spec": base_spec,
        "missingFields": [],
        "relationships": [],
    }


GOOD = [
    candidate(
        "Fortified Constitution", "ability",
        "Fortified Constitution is an ability perk. Once per rest, the character reduces required rest time and recovers additional HP. This ability has a defined effect and applies during recovery.",
        "/Part 1/Creation/Abilities/Health XP Buy.PDF", block_type="mechanic-block",
    ),
    candidate(
        "Arborae", "species",
        "Arborae are a species with bark-like appearance, seasonal culture, inherited traits, environmental adaptations, and a species progression that develops over time.",
        "/Part 1/Species/Arborae.PDF",
    ),
    candidate(
        "Void Skimmer", "vehicle",
        "The Void Skimmer is a vehicle and starship with a two-person crew, an engine frame, travel speed, vehicle components, and upgrade slots used during multiversal travel.",
        "/Part 1/Vehicles/Void Skimmer.PDF", block_type="stat-block",
    ),
    candidate(
        "Mental Strain", "rule",
        "Mental Strain is a rule triggered when a character perceives an aberration. The character must make a DC 16 save; failure applies confusion for one round. The procedure defines trigger, check, and result.",
        "/Creatures/Aberrations Rules.PDF", block_type="mechanic-block",
    ),
    candidate(
        "The Glass Covenant", "faction",
        "The Glass Covenant is a faction and religious organization. Its members pursue specific goals, maintain allies and enemies, and operate through cells across several cities.",
        "/Part 3/Worlds/Factions/Glass Covenant.PDF",
    ),
]

BAD = [
    candidate(
        "A familiar's role may include", "ability",
        "A familiar may provide tactical assistance, relay magic, extend perception, and contribute to storytelling. The following list describes several possible uses rather than one named ability.",
        "/Part 2/Magic/Familiars and pets.PDF", block_type="mechanic-block",
    ),
    candidate(
        "1.3 Security Modules", "ability",
        "Security modules are computer components used as equipment. Components include firewall modules, encryption modules, intrusion alarms, and access controls for a computer item.",
        "/Part 1/Items/Computers.PDF",
    ),
    candidate(
        "2 200 XP1st 3 4", "ability",
        "2 200 XP 1st 3 4 3 300 XP 2nd 3 1 5 4 400 XP 2nd 3 2 6 5 500 XP 3rd 4 2 1 7 progression table values.",
        "/Part 2/Magic/Magic Rules.PDF", block_type="table",
    ),
    candidate(
        "Choosing Starting Facilities", "ability",
        "Choosing starting facilities is a procedure in the homestead rules. Players choose food production, livestock, energy, and support facilities based on available land plots.",
        "/Part 1/Downtime/Homesteading Rules.PDF",
    ),
    candidate(
        "+1 to AC, even when unarmored", "ability",
        "A bullet in a larger durability upgrade grants plus one AC while unarmored and is followed by several unrelated upgrade examples and reference tables.",
        "/Part 1/Creation/Health XP Buy.PDF",
    ),
]


class SemanticBaselineV2Tests(unittest.TestCase):
    def test_good_fixtures_are_not_rejected(self):
        for row in GOOD:
            with self.subTest(row=row["name"]):
                result = classify(row, Counter())
                self.assertIn(result["baselineV2"]["tier"], {"ready", "needs-review"})
                self.assertNotIn("known-regression", result["baselineV2"]["reasons"])

    def test_known_bad_fixtures_are_rejected(self):
        for row in BAD:
            with self.subTest(row=row["name"]):
                result = classify(row, Counter())
                self.assertEqual(result["baselineV2"]["tier"], "rejected")
                self.assertTrue(result["baselineV2"]["reasons"])

    def test_graph_contract_uses_current_field_names(self):
        row = GOOD[0].copy()
        degree = Counter({row["candidateId"]: 2})
        result = classify(row, degree)
        self.assertEqual(result["baselineV2"]["semanticGraphDegree"], 2)

    def test_family_conflict_is_detected(self):
        row = candidate(
            "Quantum CPU", "ability",
            "Quantum CPU is an item component for a computer. This equipment component changes processing power, energy cost, weight, and item upgrade capacity.",
            "/Part 1/Items/Computers.PDF",
        )
        result = classify(row, Counter())
        self.assertEqual(result["baselineV2"]["tier"], "rejected")
        self.assertIn("family-conflict", result["baselineV2"]["reasons"])


if __name__ == "__main__":
    unittest.main()
