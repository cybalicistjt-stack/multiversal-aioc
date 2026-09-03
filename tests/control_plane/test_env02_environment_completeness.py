import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
PACKAGE = ENV_DIR / "ENV-02_COMPLETION_PACKAGE_v1.0.0.md"
MATRIX = ENV_DIR / "ENV-02_EFFECTIVE_COMPLETENESS_MATRIX_v1.0.0.csv"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"


class Env02EnvironmentCompletenessTests(unittest.TestCase):
    def test_effective_matrix_has_exactly_40_complete_profiles(self):
        with MATRIX.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 40)
        required = [
            "Has_Overview",
            "Has_Environmental_Features",
            "Has_Movement_Or_Navigation",
            "Has_Hazards",
            "Has_Encounters_Or_Challenges",
            "Has_Rest_Or_Shelter",
            "Has_Random_Encounter_Table",
        ]
        for row in rows:
            self.assertEqual(row["Minimum_Profile_Complete"], "YES", row["Environment_Name"])
            for field in required:
                self.assertEqual(row[field], "YES", f"{row['Environment_Name']}:{field}")

    def test_source_flags_are_preserved_alongside_effective_repairs(self):
        with MATRIX.open(encoding="utf-8", newline="") as handle:
            rows = {row["Environment_Name"]: row for row in csv.DictReader(handle)}
        self.assertEqual(rows["Nomadic Camp"]["Has_Random_Encounter_Table_Source_Matrix"], "NO")
        self.assertEqual(rows["Nomadic Camp"]["Has_Random_Encounter_Table"], "YES")
        self.assertEqual(rows["Bustling Metropolis"]["Has_Encounters_Or_Challenges_Source_Matrix"], "NO")
        self.assertEqual(rows["Bustling Metropolis"]["Has_Encounters_Or_Challenges"], "YES")
        self.assertEqual(rows["Swamps"]["Has_Rest_Or_Shelter_Source_Matrix"], "YES")
        self.assertEqual(rows["Swamps"]["Has_Rest_Or_Shelter"], "YES")
        self.assertIn("Resting heading was empty", rows["Swamps"]["ENV02_Repair_Note"])

    def test_authored_completions_and_provenance_boundary_are_explicit(self):
        text = PACKAGE.read_text(encoding="utf-8")
        self.assertIn("not recovered PDF text", text)
        self.assertIn("No environment-ability links are added", text)
        self.assertIn("all **40/40** promoted environment profiles", text)
        for name in [
            "Swamps",
            "Temperate Forest",
            "Rainforest or Jungle",
            "Post-Apocalyptic Overgrown City",
            "Bustling Metropolis",
            "Port City",
            "Small Town or Hamlet",
        ]:
            self.assertIn(f"## {name} - Random Encounter Table (d12)", text)
        self.assertIn("### Swamps - Rest and Shelter", text)
        self.assertIn("### Post-Apocalyptic Overgrown City - Rest and Shelter", text)
        self.assertIn("Nomadic Camp", text)
        self.assertIn("Metropolitan Encounters", text)

    def test_env02_remains_completed_as_program_progresses(self):
        backlog = json.loads(BACKLOG.read_text(encoding="utf-8"))
        strict_order = backlog["strict_order"]
        status = {item["id"]: item["status"] for item in backlog["tranches"]}
        self.assertEqual(status["ENV-01"], "completed_verified")
        self.assertEqual(status["ENV-02"], "completed_verified")
        self.assertIn(backlog["current_item"], strict_order)
        self.assertGreater(strict_order.index(backlog["current_item"]), strict_order.index("ENV-02"))
        self.assertIn(backlog["completed_through"], strict_order)
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("ENV-02"))
        self.assertFalse(backlog["application_implementation_authority"])


if __name__ == "__main__":
    unittest.main()
