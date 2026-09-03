import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
MODEL = ENV_DIR / "ENV-01_COMPOSITION_MODEL_v1.0.0.json"
CONTRACT = ENV_DIR / "ENV-01_ENVIRONMENT_MODEL_COMPOSITION_CONTRACT_v1.0.0.md"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"


class Env01CompositionContractTests(unittest.TestCase):
    def test_model_has_four_durable_layers_and_derived_resolved_view(self):
        model = json.loads(MODEL.read_text(encoding="utf-8"))
        ids = [item["id"] for item in model["durable_object_types"]]
        self.assertEqual(
            ids,
            [
                "environment_archetype",
                "environment_preset",
                "environment_overlay",
                "local_environment_instance",
            ],
        )
        self.assertEqual(model["derived_projection"]["id"], "resolved_environment")
        self.assertFalse(model["derived_projection"]["durable"])
        self.assertFalse(model["derived_projection"]["write_back"])

    def test_composition_order_and_external_boundaries_are_locked(self):
        model = json.loads(MODEL.read_text(encoding="utf-8"))
        self.assertEqual(
            model["composition_order"],
            [
                "archetype_baselines",
                "preset_parameterization",
                "local_instance_configuration",
                "active_overlays",
                "current_runtime_scene_state",
                "participant_evaluation",
            ],
        )
        self.assertEqual(model["external_owner_boundaries"]["creature_ecology"], "CEW")
        self.assertIn("World/Reality", model["external_owner_boundaries"]["creature_distribution"])
        self.assertFalse(model["application_implementation_authority"])
        self.assertEqual(model["overlay_detail_owner"], "ENV-04")
        self.assertEqual(model["habitat_vocabulary_owner"], "ENV-15")

    def test_compound_presets_and_visible_conflicts_are_preserved(self):
        model = json.loads(MODEL.read_text(encoding="utf-8"))
        self.assertTrue(model["compound_preset_model"]["primary_archetype_required"])
        self.assertTrue(model["compound_preset_model"]["secondary_archetypes_allowed"])
        self.assertIn("unresolved_conflict", model["validation_states"])
        self.assertIn("provenance_gap", model["validation_states"])
        self.assertIn("set", model["explicit_delta_operations"]["initial_contract"])
        self.assertIn("constrain", model["explicit_delta_operations"]["initial_contract"])

    def test_contract_preserves_source_profiles_and_noninterference(self):
        text = CONTRACT.read_text(encoding="utf-8")
        required = [
            "Resolved Environment",
            "does not mutate",
            "existing forty promoted environment profiles",
            "participant adaptations/equipment/vehicles/powers remain external",
            "no `Multiversal-app` mutation",
            "ENV-04",
            "ENV-15",
        ]
        for phrase in required:
            self.assertIn(phrase, text)

    def test_backlog_advances_only_after_env01(self):
        backlog = json.loads(BACKLOG.read_text(encoding="utf-8"))
        self.assertEqual(backlog["completed_through"], "ENV-01")
        self.assertEqual(backlog["current_item"], "ENV-02")
        status = {item["id"]: item["status"] for item in backlog["tranches"]}
        self.assertEqual(status["ENV-01"], "completed_verified")
        self.assertEqual(status["ENV-02"], "selected_not_started")
        self.assertFalse(backlog["application_implementation_authority"])


if __name__ == "__main__":
    unittest.main()
