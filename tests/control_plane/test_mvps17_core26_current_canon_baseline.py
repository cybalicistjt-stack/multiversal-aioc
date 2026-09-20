from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUTH = ROOT / "governance/application-planning/species-reconciliation/CORE_26_SPECIES_AUTHORITY_v1.0.0.json"
STANDARD = ROOT / "governance/application-planning/player-species/CORE_26_GAME_READY_STANDARD_v1.0.0.json"
BASELINE = ROOT / "governance/application-planning/player-species/CORE_26_PRODUCTION_BASELINE_v0.1.0.json"
CURRENT = ROOT / "operations/CURRENT.json"
BOOTSTRAP = ROOT / "operations/BOOTSTRAP.md"
CONTRACT = ROOT / "operations/OPERATING_CONTRACT.md"
REGISTRY = ROOT / "operations/CONTROL_SURFACE_REGISTRY.json"

EXPECTED = [
    "Human","Elf","Dwarf","Goblin","Orc","Giantkin","Stygian","Sharr","Gray","The Free",
    "Ratman","Furashin","Rog","Rohai","Moravi","Vespin","Rakuuta","Traiga","Kola-Ha",
    "Toba-Madra","Arborae","Mythragara","Suula","Morganthyr","ManyToms","Akwi"
]

class MVPS17Core26CanonBaselineTests(unittest.TestCase):
    def _j(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_current_authority_and_production_artifacts_exist(self):
        for path in (AUTH, STANDARD, BASELINE):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_current_selector_points_to_core26_authority(self):
        current = self._j(CURRENT)
        p = current["domain_authorities"]["player_species"]
        self.assertEqual(p["path"], "governance/application-planning/species-reconciliation/CORE_26_SPECIES_AUTHORITY_v1.0.0.json")
        self.assertEqual(p["authority_id"], "CORE26-CURRENT-01")
        self.assertEqual(p["status"], "current_canon")
        self.assertEqual(p["roster_count"], 26)

    def test_authority_is_exact_core26_and_legacy_nekron_is_not_current(self):
        a = self._j(AUTH)
        self.assertEqual(a["authority_id"], "CORE26-CURRENT-01")
        self.assertEqual(a["status"], "CURRENT_CANON")
        self.assertEqual(a["current_core_26"]["count"], 26)
        self.assertEqual(a["current_core_26"]["species"], EXPECTED)
        self.assertNotIn("Nekron", a["current_core_26"]["species"])
        self.assertEqual(a["identity_migrations"]["Nekron"]["current"], "Morganthyr")
        self.assertEqual(a["akwi"]["status"], "core_playable_species")
        self.assertEqual(a["ratman"]["core_species"], "Ratman")
        self.assertEqual(len(a["ratman"]["subordinate_lineages"]), 9)

    def test_startup_and_operating_contract_load_current_domain_authority(self):
        bootstrap = BOOTSTRAP.read_text(encoding="utf-8")
        contract = CONTRACT.read_text(encoding="utf-8")
        self.assertIn("CURRENT-referenced domain authority", bootstrap)
        self.assertIn("CURRENT-referenced domain authority", contract)
        self.assertIn("historical domain material cannot override", contract)

    def test_control_surface_registry_marks_current_species_authority(self):
        r = self._j(REGISTRY)
        self.assertIn("CURRENT_REFERENCED_DOMAIN_AUTHORITY", r["dispositions"])
        rows = [x for x in r["surfaces"] if x.get("path") == "governance/application-planning/species-reconciliation/CORE_26_SPECIES_AUTHORITY_v1.0.0.json"]
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["disposition"], "CURRENT_REFERENCED_DOMAIN_AUTHORITY")
        self.assertFalse(rows[0]["can_select_work"])

    def test_equal_standard_applies_same_required_dimensions_to_all_26(self):
        s = self._j(STANDARD)
        self.assertEqual(s["standard_id"], "CORE26.GAME_READY.v1")
        self.assertEqual(s["applies_to"], EXPECTED)
        self.assertGreaterEqual(len(s["dimensions"]), 19)
        required = [x["id"] for x in s["dimensions"] if x["requirement"] == "required"]
        self.assertIn("canonical_species_definition", required)
        self.assertIn("balance_testing_certification", required)
        optional = {x["id"] for x in s["dimensions"] if x["requirement"] == "required_or_explicit_not_applicable"}
        self.assertTrue({"lineage_subspecies","forms_transformation","progression_maturation"} <= optional)

    def test_baseline_has_exactly_26_rows_and_does_not_overclaim_certification(self):
        b = self._j(BASELINE)
        rows = b["species"]
        self.assertEqual([x["name"] for x in rows], EXPECTED)
        self.assertEqual(len(rows), 26)
        for row in rows:
            with self.subTest(species=row["name"]):
                self.assertEqual(row["standard_id"], "CORE26.GAME_READY.v1")
                self.assertNotEqual(row["overall_status"], "game_ready_certified")
                self.assertIn("canonical_object_state", row)
                self.assertIn("current_authority_evidence", row)
        by_name={x["name"]:x for x in rows}
        self.assertEqual(by_name["Morganthyr"]["canonical_object_state"], "legacy_nekron_object_requires_current_identity_migration")
        self.assertEqual(by_name["Rog"]["canonical_object_state"], "missing_current_content_db_object")
        self.assertEqual(by_name["Suula"]["canonical_object_state"], "missing_current_content_db_object")
        self.assertEqual(by_name["Akwi"]["canonical_object_state"], "governed_supplemental_runtime_requires_catalog_convergence")

if __name__ == "__main__":
    unittest.main()
