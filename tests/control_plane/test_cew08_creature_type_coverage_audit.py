import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
AUDIT = CEW / "CEW-08_CREATURE_TYPE_COVERAGE_AUDIT_v1.0.0.json"
MATRIX = CEW / "CEW-08_TYPE_FAMILY_COVERAGE_MATRIX_v1.0.0.json"
CONTRACT = CEW / "CEW-08_CREATURE_TYPE_COVERAGE_CONTRACT.md"
REPORT = CEW / "CEW-08_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"


class Cew08CreatureTypeCoverageAuditTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_contract_and_authority_boundaries(self):
        audit = self.load(AUDIT)
        self.assertEqual(audit["contract_id"], "CEW-TYPE-COV-1.0")
        self.assertEqual(audit["work_item"], "CEW-08")
        self.assertEqual(audit["identity_authority"], "CEW-ID-1.0")
        self.assertEqual(audit["taxonomy_authority"], "CEW-TAX-1.0")
        self.assertEqual(audit["coverage_authority"], "CEW-COV-1.0")
        self.assertFalse(audit["application_implementation_authority"])
        self.assertFalse(audit["canonical_type_binding_authorized"])
        self.assertFalse(audit["type_gap_expansion_authorized"])
        self.assertFalse(audit["name_or_mechanics_type_inference_authorized"])
        self.assertEqual(audit["strict_successor"], "CEW-09")

    def test_type_family_matrix_covers_recovered_base_usages_exactly(self):
        matrix = self.load(MATRIX)
        rows = {row["term"]: row for row in matrix["type_family_rows"]}
        self.assertEqual(
            set(rows),
            {
                "Aberration", "Chaos", "Construct", "Demonic", "Digital", "Divine",
                "Elemental", "Fell", "Fey", "Toon", "Undead", "Dragon", "Beast", "Illusion",
            },
        )
        self.assertEqual(matrix["audited_type_usage_count"], 14)
        explicit = {"Aberration", "Chaos", "Construct", "Demonic", "Divine", "Elemental", "Fey", "Toon", "Undead"}
        strong = {"Digital", "Fell", "Dragon"}
        for term in explicit:
            self.assertEqual(rows[term]["taxonomy_strength"], "source_explicit_base_type")
        for term in strong:
            self.assertEqual(rows[term]["taxonomy_strength"], "source_strong_base_type_usage")
        self.assertEqual(rows["Beast"]["taxonomy_strength"], "statblock_base_type_usage_without_family_contract")
        self.assertEqual(rows["Illusion"]["taxonomy_strength"], "orphan_type_usage_unresolved")

    def test_source_collection_evidence_is_quantified_without_overclaiming(self):
        matrix = self.load(MATRIX)
        rows = {row["term"]: row for row in matrix["type_family_rows"]}
        expected = {
            "Aberration": 25,
            "Chaos": 30,
            "Construct": 49,
            "Demonic": 44,
            "Digital": 22,
            "Divine": 23,
            "Elemental": 39,
            "Fell": 17,
            "Fey": 29,
            "Toon": 43,
            "Undead": 40,
            "Dragon": 123,
            "Beast": 199,
        }
        self.assertEqual(matrix["quantified_type_collection_safe_statblock_count"], 683)
        for term, count in expected.items():
            self.assertEqual(rows[term]["quantified_safe_statblock_count"], count)
            self.assertTrue(rows[term]["quantification_is_source_collection_scoped"])
            self.assertFalse(rows[term]["quantified_count_is_canonical_definition_count"])
        self.assertIsNone(rows["Illusion"]["quantified_safe_statblock_count"])
        self.assertEqual(rows["Illusion"]["quantification_state"], "unknown_mixed_source_usage_not_safely_counted")

    def test_family_semantic_coverage_distinguishes_gaps(self):
        audit = self.load(AUDIT)
        summary = audit["type_family_semantic_coverage"]
        self.assertEqual(summary["recovered_family_semantics_count"], 11)
        self.assertEqual(set(summary["recovered_family_semantics"]), {
            "Aberration", "Chaos", "Construct", "Demonic", "Digital", "Divine", "Elemental", "Fell", "Fey", "Toon", "Undead"
        })
        self.assertEqual(summary["partial_normalization_count"], 1)
        self.assertEqual(summary["partial_normalization"], ["Dragon"])
        self.assertEqual(summary["usage_without_family_contract_count"], 1)
        self.assertEqual(summary["usage_without_family_contract"], ["Beast"])
        self.assertEqual(summary["orphan_usage_count"], 1)
        self.assertEqual(summary["orphan_usage"], ["Illusion"])

    def test_canonical_stable_id_type_binding_gap_remains_unknown(self):
        audit = self.load(AUDIT)
        cov = audit["canonical_stable_id_type_coverage"]
        self.assertEqual(cov["canonical_creature_definition_count"], 27)
        self.assertEqual(cov["explicit_type_binding_count"], 0)
        self.assertEqual(cov["unknown_type_binding_count"], 27)
        self.assertEqual(cov["coverage_state"], "unknown_no_explicit_stable_id_type_bindings")
        self.assertFalse(cov["source_label_overlap_used_as_binding"])
        self.assertFalse(cov["namespace_used_as_type_binding"])
        self.assertFalse(cov["mechanics_used_as_type_binding"])

    def test_non_base_systems_are_not_miscounted_as_missing_base_types(self):
        audit = self.load(AUDIT)
        exclusions = set(audit["non_base_type_systems_not_counted_as_base_type_gaps"])
        self.assertTrue({
            "Plant biological tag and movement categories",
            "Incorporeal manifestation axis",
            "Zombie conversion templates",
            "Ghost and spirit conversion templates",
            "Vampirism and lycanthropy transformations",
            "Animal biological/ecological identity",
            "Fire/Cold/Shadow/Chaos/Mechanical animal modifiers",
        }.issubset(exclusions))

    def test_gap_queue_and_unresolved_conflicts_are_preserved(self):
        audit = self.load(AUDIT)
        gaps = {row["gap_id"]: row for row in audit["type_coverage_gap_queue"]}
        self.assertEqual(set(gaps), {"CEW08-GAP-001", "CEW08-GAP-002", "CEW08-GAP-003", "CEW08-GAP-004"})
        self.assertEqual(gaps["CEW08-GAP-001"]["subject"], "Beast")
        self.assertEqual(gaps["CEW08-GAP-002"]["subject"], "Illusion")
        self.assertEqual(gaps["CEW08-GAP-003"]["subject"], "Dragon")
        self.assertEqual(gaps["CEW08-GAP-004"]["subject"], "canonical stable-ID type bindings")
        for row in gaps.values():
            self.assertFalse(row["auto_resolve"])
            self.assertFalse(row["creates_new_creature"])
        self.assertEqual(audit["preserved_cew02_taxonomy_conflict_count"], 7)
        self.assertFalse(audit["cew02_taxonomy_conflicts_auto_resolved"])

    def test_future_owner_boundaries_are_preserved(self):
        audit = self.load(AUDIT)
        owners = audit["future_owner_boundaries"]
        self.assertEqual(owners["next_tranche"], "CEW-09")
        self.assertEqual(owners["intelligence_personhood_domestication_partnership"], "CEW-09")
        self.assertEqual(owners["havalaea_native_lineage"], "CEW-10")
        self.assertEqual(owners["relationship_pathways"], "CEW-11")
        self.assertEqual(owners["earthlike_animal_wildlife_baseline"], "CEW-12")
        self.assertEqual(owners["type_gap_expansion"], "CEW-15")

    def test_contract_text_states_non_inference_and_no_expansion(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "Type coverage is not creature identity coverage.",
            "Source-family coverage does not create canonical stable-ID type bindings.",
            "A missing family contract is an audit gap, not permission to invent one.",
            "Cross-cutting systems are not base-type gaps merely because they use the word type.",
            "CEW-09 is the strict successor.",
            "no application implementation authority",
        ]:
            self.assertIn(phrase, text)

    def test_closeout_is_monotonic_and_selects_cew09(self):
        backlog = self.load(BACKLOG)
        strict_order = backlog["strict_order"]
        status = {row["id"]: row["status"] for row in backlog["tranches"]}
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-08"))
        self.assertEqual(status["CEW-08"], "completed_verified")
        if backlog["completed_through"] == "CEW-08":
            self.assertEqual(backlog["current_item"], "CEW-09")
            self.assertEqual(backlog["current_item_state"], "selected_not_started")
            self.assertEqual(status["CEW-09"], "selected_not_started")
        else:
            self.assertGreater(strict_order.index(backlog["current_item"]), strict_order.index("CEW-08"))
        decisions = backlog["cew08_decisions"]
        self.assertEqual(decisions["contract_id"], "CEW-TYPE-COV-1.0")
        self.assertEqual(decisions["audited_type_usage_count"], 14)
        self.assertEqual(decisions["quantified_type_collection_safe_statblock_count"], 683)
        self.assertEqual(decisions["canonical_creature_definition_count"], 27)
        self.assertEqual(decisions["explicit_stable_id_type_binding_count"], 0)
        self.assertEqual(decisions["type_coverage_gap_count"], 4)
        self.assertFalse(decisions["type_gap_expansion_authorized"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertIn("CEW-09", REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
