import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
AUDIT = CEW / "CEW-07_EXISTING_CREATURE_COVERAGE_AUDIT_v1.0.0.json"
LEDGER = CEW / "CEW-07_CANONICAL_CREATURE_COVERAGE_LEDGER_v1.0.0.json"
CONTRACT = CEW / "CEW-07_COVERAGE_AUDIT_CONTRACT.md"
REPORT = CEW / "CEW-07_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"


class Cew07ExistingCreatureCoverageAuditTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_audit_contract_and_population_boundaries(self):
        audit = self.load(AUDIT)
        self.assertEqual(audit["contract_id"], "CEW-COV-1.0")
        self.assertEqual(audit["work_item"], "CEW-07")
        self.assertEqual(audit["identity_authority"], "CEW-ID-1.0")
        self.assertEqual(audit["taxonomy_authority"], "CEW-TAX-1.0")
        self.assertEqual(audit["classification_authority"], "CEW-CLASS-1.0")
        self.assertEqual(audit["habitat_authority"], "CEW-HAB-1.0")
        self.assertEqual(audit["distribution_authority"], "CEW-DIST-1.0")
        self.assertEqual(audit["ecological_role_authority"], "CEW-ECO-1.0")
        self.assertFalse(audit["application_implementation_authority"])
        self.assertFalse(audit["missing_fact_backfill_authorized"])
        self.assertFalse(audit["name_only_source_binding_authorized"])
        self.assertEqual(audit["strict_successor"], "CEW-08")

    def test_source_recovery_accounting_is_exact_and_nonpromoting(self):
        source = self.load(AUDIT)["source_recovery_coverage"]
        self.assertEqual(source["dedicated_source_document_count"], 23)
        self.assertEqual(source["candidate_start_count"], 878)
        self.assertEqual(source["safe_statblock_record_count"], 826)
        self.assertEqual(source["unresolved_candidate_start_count"], 52)
        self.assertEqual(source["fully_accounted_document_count"], 14)
        self.assertEqual(source["partially_accounted_document_count"], 6)
        self.assertEqual(source["no_safe_statblock_document_count"], 3)
        self.assertEqual(
            set(source["no_safe_statblock_documents"]),
            {"Creature types.PDF", "Vampirism&Lycanthropy.PDF", "animals 11-16-24.PDF"},
        )
        self.assertEqual(source["source_signature_candidate_count"], 324)
        self.assertEqual(source["formally_deferred_source_candidate_count"], 93)
        self.assertEqual(source["unresolved_review_candidate_count"], 30)
        self.assertFalse(source["source_record_is_canonical_definition"])
        self.assertFalse(source["audit_promotes_source_records"])

    def test_canonical_ledger_covers_exact_current_definition_set(self):
        ledger = self.load(LEDGER)
        rows = ledger["canonical_creatures"]
        self.assertEqual(ledger["canonical_creature_definition_count"], 27)
        self.assertEqual(len(rows), 27)
        ids = [row["stable_id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(sum(i.startswith("mv.playtest.creature.reference.") for i in ids), 15)
        self.assertEqual(sum(i.startswith("mv.setting.havalaea.creature.") for i in ids), 5)
        self.assertEqual(sum(i.startswith("mv.adventure.lost-key.creature.") for i in ids), 7)
        for row in rows:
            self.assertEqual(row["identity_coverage"], "covered_stable_id")
            self.assertFalse(row["source_binding_inferred_from_name"])

    def test_stable_id_fact_coverage_does_not_overclaim_source_label_overlap(self):
        audit = self.load(AUDIT)
        cov = audit["canonical_stable_id_fact_coverage"]
        self.assertEqual(cov["identity"]["covered_count"], 27)
        self.assertEqual(cov["game_type_or_taxonomy"]["covered_count"], 0)
        self.assertEqual(cov["habitat_ecology"]["covered_count"], 0)
        self.assertEqual(cov["distribution_scope"]["covered_count"], 5)
        self.assertEqual(cov["ecological_role_or_encounter_use"]["covered_count"], 0)
        self.assertEqual(
            set(cov["distribution_scope"]["covered_stable_ids"]),
            {
                "mv.setting.havalaea.creature.rootstalker",
                "mv.setting.havalaea.creature.hisscap-frog",
                "mv.setting.havalaea.creature.mossling-glider",
                "mv.setting.havalaea.creature.sapcrawl-varnet",
                "mv.setting.havalaea.creature.jungle-slip-beetle",
            },
        )
        self.assertEqual(cov["distribution_scope"]["native_status_for_covered_ids"], "unknown")

    def test_source_label_overlap_queue_is_unresolved_not_auto_bound(self):
        audit = self.load(AUDIT)
        rows = {row["source_subject_label"]: row for row in audit["source_label_overlap_queue"]}
        self.assertEqual(set(rows), {"Jungle-Slip Beetle", "Rootstalker", "Sapcrawl Varnet", "3. Rift-Touched Animals (Optional)"})
        for row in rows.values():
            self.assertFalse(row["canonical_binding_created"])
            self.assertFalse(row["name_similarity_sufficient"])
            self.assertIn(row["state"], {"unresolved_exact_name_overlap", "unresolved_near_name_no_supported_alias"})
        self.assertEqual(rows["Rootstalker"]["source_fact_owner"], "CEW-06")
        self.assertEqual(rows["Sapcrawl Varnet"]["source_fact_owner"], "CEW-06")
        self.assertEqual(rows["Jungle-Slip Beetle"]["source_fact_owner"], "CEW-04")
        self.assertEqual(rows["3. Rift-Touched Animals (Optional)"]["source_fact_owner"], "CEW-01")

    def test_audit_preserves_future_owner_boundaries(self):
        audit = self.load(AUDIT)
        owners = audit["deferred_population_owners"]
        self.assertEqual(owners["creature_type_coverage"], "CEW-08")
        self.assertEqual(owners["intelligence_personhood_domestication_partnership"], "CEW-09")
        self.assertEqual(owners["havalaea_native_lineage"], "CEW-10")
        self.assertEqual(owners["mount_pet_familiar_companion_crosswalk"], "CEW-11")
        self.assertEqual(owners["earthlike_wildlife_baseline"], "CEW-12")
        self.assertFalse(audit["gap_expansion_authorized"])

    def test_contract_states_coverage_is_not_truth_and_not_identity_binding(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "Coverage is evidence accounting, not a substitute for creature truth.",
            "Canonical object presence does not mean source recovery is complete.",
            "A source-label match does not create a canonical identity binding.",
            "Unknown remains a valid audited result.",
            "CEW-08 owns the Creature-Type Coverage Audit.",
            "no application implementation authority",
        ]:
            self.assertIn(phrase, text)

    def test_closeout_is_monotonic_and_selects_cew08(self):
        backlog = self.load(BACKLOG)
        strict_order = backlog["strict_order"]
        status = {row["id"]: row["status"] for row in backlog["tranches"]}
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-07"))
        self.assertEqual(status["CEW-07"], "completed_verified")
        if backlog["completed_through"] == "CEW-07":
            self.assertEqual(backlog["current_item"], "CEW-08")
            self.assertEqual(backlog["current_item_state"], "selected_not_started")
            self.assertEqual(status["CEW-08"], "selected_not_started")
        else:
            self.assertGreater(strict_order.index(backlog["current_item"]), strict_order.index("CEW-07"))
        decisions = backlog["cew07_decisions"]
        self.assertEqual(decisions["contract_id"], "CEW-COV-1.0")
        self.assertEqual(decisions["canonical_creature_definition_count"], 27)
        self.assertEqual(decisions["safe_statblock_record_count"], 826)
        self.assertEqual(decisions["unresolved_candidate_start_count"], 52)
        self.assertFalse(decisions["name_only_source_binding_authorized"])
        self.assertFalse(decisions["gap_expansion_authorized"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertIn("CEW-08", REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
