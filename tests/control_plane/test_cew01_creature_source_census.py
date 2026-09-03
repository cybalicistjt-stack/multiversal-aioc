import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW_DIR = ROOT / "governance/application-planning/creature-ecology-wildlife"
CENSUS = CEW_DIR / "CEW-01_CREATURE_SOURCE_CENSUS_v1.0.0.json"
LEDGER = CEW_DIR / "CEW-01_IDENTITY_LEDGER_v1.0.0.json"
CONTRACT = CEW_DIR / "CEW-01_IDENTITY_LEDGER_CONTRACT.md"
REPORT = CEW_DIR / "CEW-01_COMPLETION_REPORT.md"
BACKLOG = CEW_DIR / "CEW_PROGRAM_BACKLOG.json"


class Cew01CreatureSourceCensusTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_retained_creature_source_census_matches_governed_evidence(self):
        census = self.load_json(CENSUS)
        corpus = census["retained_creature_pdf_corpus"]
        self.assertEqual(census["census_id"], "CEW-SC-1.0")
        self.assertEqual(corpus["document_count"], 23)
        self.assertEqual(corpus["candidate_start_count"], 878)
        self.assertEqual(corpus["source_statblock_evidence_count"], 826)
        self.assertEqual(corpus["source_signature_candidate_count"], 324)
        self.assertEqual(len(corpus["documents"]), 23)
        self.assertEqual(len({row["sha256"] for row in corpus["documents"]}), 23)
        statuses = {row["source_document"]: row["coverage_status"] for row in corpus["documents"]}
        self.assertEqual(statuses["Creature types.PDF"], "source-family-gap-no-safe-statblock-records")
        self.assertEqual(statuses["animals 11-16-24.PDF"], "source-family-gap-no-safe-statblock-records")
        self.assertEqual(statuses["Vampirism&Lycanthropy.PDF"], "source-family-gap-no-safe-statblock-records")

    def test_player_creatures_and_related_sources_do_not_collapse_identity(self):
        census = self.load_json(CENSUS)
        conversion = census["creation_and_conversion_sources"][0]
        self.assertEqual(conversion["source_document"], "Player Creatures.PDF")
        self.assertIn("does not create identity equivalence", conversion["identity_role"])
        related = {row["source_document"]: row for row in census["related_supporting_sources"]}
        self.assertIn("Havalaea.PDF", related)
        self.assertIn("Animal training.PDF", related)
        self.assertIn("not base creature identity authority", related["Animal training.PDF"]["role"])

    def test_current_canonical_creature_definition_set_is_explicit_and_unique(self):
        census = self.load_json(CENSUS)
        current = census["governed_current_catalog"]
        ids = current["canonical_ids"]
        self.assertEqual(current["creature_definition_count"], 27)
        self.assertEqual(len(ids), 27)
        self.assertEqual(len(set(ids)), 27)
        self.assertIn("mv.setting.havalaea.creature.rootstalker", ids)
        self.assertIn("mv.adventure.lost-key.creature.rift-touched-animal", ids)
        self.assertFalse(current["legacy_sparse_objects_are_complete_source_truth"])

    def test_r1_formal_deferral_is_preserved_without_auto_binding(self):
        census = self.load_json(CENSUS)
        r1 = census["formal_r1_recovery"]
        self.assertEqual(r1["formally_deferred_creature_candidates"], 93)
        self.assertEqual(r1["content_state"], "formally_deferred_source_candidate")
        self.assertFalse(r1["canonical_promotion"])
        self.assertFalse(r1["automatic_binding_authorized"])
        self.assertTrue(r1["row_ledger"].endswith("PPIA-02_R1_DEFERRED_CREATURE_CANDIDATES.csv"))

    def test_semantic_gpt_and_evernote_evidence_fail_closed(self):
        census = self.load_json(CENSUS)
        recovery = census["semantic_and_gpt_recovery"]
        self.assertEqual(recovery["direct_review_creature_candidates"], 18)
        self.assertEqual(recovery["semantic_validation_pending_creature_candidates"], 9)
        self.assertEqual(recovery["gpt_diagnostic_creature_packet_count"], 3)
        self.assertEqual(recovery["default_identity_state"], "unresolved_recovery_candidate")
        self.assertFalse(census["evernote_recovery"]["independent_creature_identity_set_found_in_current_canonical_repository"])

    def test_identity_ledger_states_and_near_name_watch_are_conservative(self):
        ledger = self.load_json(LEDGER)
        self.assertEqual(ledger["ledger_id"], "CEW-ID-1.0")
        required = {
            "canonical_definition",
            "recoverable_source_record",
            "formally_deferred_source_candidate",
            "unresolved_recovery_candidate",
            "rejected_identity_authority",
        }
        self.assertEqual(set(ledger["identity_states"]), required)
        watch = ledger["identity_overlap_watch"]
        self.assertEqual(len(watch), 1)
        self.assertEqual(watch[0]["source_heading"], "3. Rift-Touched Animals (Optional)")
        self.assertEqual(watch[0]["possible_canonical_target"], "mv.adventure.lost-key.creature.rift-touched-animal")
        self.assertEqual(watch[0]["resolution"], "unresolved_near_name_no_supported_alias")
        self.assertFalse(watch[0]["auto_merge"])
        duplicate = ledger["duplicate_alias_resolution"]
        self.assertEqual(duplicate["confirmed_duplicate_merges"], 0)
        self.assertEqual(duplicate["confirmed_alias_bindings"], 0)
        self.assertFalse(duplicate["name_only_merges_authorized"])

    def test_unsuccessful_487_object_parse_database_is_rejected_as_identity_authority(self):
        census = self.load_json(CENSUS)
        rejected = census["rejected_identity_authorities"]
        self.assertEqual(len(rejected), 1)
        self.assertEqual(rejected[0]["authority_id"], "unsuccessful-487-object-semantic-parse-database")
        self.assertEqual(rejected[0]["disposition"], "rejected_identity_authority")
        self.assertFalse(rejected[0]["may_seed_canonical_identity"])

    def test_contract_locks_no_silent_promotion_or_name_merge(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "The census is an accountability layer, not a mass-promotion step.",
            "Formal deferral is neither canonical promotion nor exclusion.",
            "Name similarity",
            "zero confirmed duplicate merges and zero confirmed alias bindings",
            "review packet",
            "does not expose an independent Evernote creature identity ledger",
            "no application implementation authority",
        ]:
            self.assertIn(phrase, text)

    def test_closeout_completes_cew01_and_selects_cew02(self):
        backlog = self.load_json(BACKLOG)
        status = {row["id"]: row["status"] for row in backlog["tranches"]}
        self.assertEqual(backlog["completed_through"], "CEW-01")
        self.assertEqual(backlog["current_item"], "CEW-02")
        self.assertEqual(backlog["current_item_state"], "selected_not_started")
        self.assertEqual(status["CEW-01"], "completed_verified")
        self.assertEqual(status["CEW-02"], "selected_not_started")
        self.assertEqual(status["CEW-03"], "planned")
        decisions = backlog["cew01_decisions"]
        self.assertEqual(decisions["canonical_creature_definition_count"], 27)
        self.assertEqual(decisions["formally_deferred_creature_candidate_count"], 93)
        self.assertEqual(decisions["confirmed_duplicate_merges"], 0)
        self.assertEqual(decisions["confirmed_alias_bindings"], 0)
        self.assertFalse(decisions["source_only_auto_promotion_authorized"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertFalse(backlog["application_implementation_authority"])
        self.assertIn("CEW-02", REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
