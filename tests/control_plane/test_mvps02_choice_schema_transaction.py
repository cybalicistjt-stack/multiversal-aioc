from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACT_DIR = ROOT / "governance/application-planning/player-species/contracts"
CHOICE = CONTRACT_DIR / "MVPS-02_CHOICE_SCHEMA_CONTRACT.json"
TX = CONTRACT_DIR / "MVPS-02_CHARACTER_CREATION_TRANSACTION.json"
VALIDATION = CONTRACT_DIR / "MVPS-02_CHOICE_VALIDATION_CONTRACT.json"
FIXTURES = CONTRACT_DIR / "MVPS-02_CHOICE_FIXTURES.json"


class MVPS02ChoiceSchemaTransactionTests(unittest.TestCase):
    def _json(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_contract_artifacts_exist(self) -> None:
        for path in (CHOICE, TX, VALIDATION, FIXTURES):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_choice_schema_enumerates_required_choice_kinds(self) -> None:
        choice = self._json(CHOICE)
        self.assertEqual(choice["contract_id"], "MVPS.SpeciesChoiceSchema")
        self.assertEqual(choice["record_type"], "SpeciesChoiceSchema")
        self.assertEqual(choice["execution_policy"], "declarative_choice_constraints_only")
        kinds = set(choice["choice_group_kinds"])
        self.assertTrue({
            "selected_trait", "optional_alternative", "lineage",
            "form", "adaptation", "substitution"
        } <= kinds)
        gate_kinds = set(choice["gate_kinds"])
        self.assertTrue({
            "prerequisite", "mutual_exclusion", "budget",
            "source_availability", "campaign", "setting", "entitlement"
        } <= gate_kinds)
        self.assertEqual(choice["fixed_grants_policy"], "not_selectable_but_receipted")
        self.assertTrue(choice["required_choice_enumeration"]["deterministic"])

    def test_creation_transaction_preserves_incomplete_draft_without_playable_state(self) -> None:
        tx = self._json(TX)
        self.assertEqual(tx["contract_id"], "MVPS.CharacterCreationSpeciesTransaction")
        self.assertEqual(tx["transaction_model"], "staged")
        self.assertIn("draft_incomplete", tx["states"])
        self.assertIn("ready_for_validation", tx["states"])
        self.assertIn("valid_playable", tx["states"])
        self.assertTrue(tx["draft_policy"]["save_incomplete"])
        self.assertFalse(tx["draft_policy"]["incomplete_may_be_playable"])
        self.assertEqual(tx["commit_policy"]["required_terminal_state"], "valid_playable")

    def test_validation_results_are_sourced_and_explain_legality(self) -> None:
        validation = self._json(VALIDATION)
        self.assertEqual(validation["contract_id"], "MVPS.SpeciesChoiceValidationResult")
        self.assertTrue(validation["issue_contract"]["rule_source_required"])
        self.assertTrue(validation["choice_result_contract"]["choice_source_required"])
        self.assertTrue(validation["choice_result_contract"]["explanation_required"])
        self.assertEqual(validation["severity_order"], ["blocking", "advisory", "info"])
        checks = set(validation["required_checks"])
        self.assertTrue({
            "required_choices", "budgets", "prerequisites", "mutual_exclusions",
            "source_availability", "campaign_restrictions", "setting_restrictions",
            "entitlement_constraints"
        } <= checks)

    def test_fixture_enumerates_pending_choices_and_blocks_invalid_publish(self) -> None:
        fixtures = self._json(FIXTURES)
        draft = fixtures["incomplete_draft"]
        self.assertEqual(draft["transaction_state"], "draft_incomplete")
        self.assertGreater(len(draft["pending_required_choices"]), 0)
        self.assertFalse(draft["playable"])
        self.assertFalse(draft["publish_allowed"])

        invalid = fixtures["invalid_combination"]
        self.assertFalse(invalid["validation"]["valid_playable"])
        blocking = invalid["validation"]["issues"]
        self.assertTrue(any(issue["severity"] == "blocking" for issue in blocking))
        for issue in blocking:
            self.assertTrue(issue["rule_source_ref"])
            self.assertTrue(issue["explanation"])

        valid = fixtures["valid_selection"]
        self.assertEqual(valid["transaction_state"], "valid_playable")
        self.assertTrue(valid["playable"])
        self.assertTrue(valid["publish_allowed"])
        self.assertEqual(valid["pending_required_choices"], [])


if __name__ == "__main__":
    unittest.main()
