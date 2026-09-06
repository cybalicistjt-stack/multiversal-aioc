import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Vti06SceneMapTokenMaiBridgeRegistrationTests(unittest.TestCase):
    def test_vti06_governed_start_is_consistent_across_current_control_plane(self):
        baseline = "e9ddbf9c763faca74689cb3776ad21501c341ba5"
        branch = "integration/vti-06-scene-map-token-mai-bridge"
        checkpoint = load_json("governance/ai/work-state/VTI-06-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")

        self.assertEqual(checkpoint["status"], "in_progress")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertEqual(checkpoint["implementation_branch"], branch)
        self.assertTrue(checkpoint["implementation_authority"])
        self.assertTrue(checkpoint["branch_creation_authorized"])
        self.assertTrue(checkpoint["acceptance_package_authorized"])
        self.assertFalse(checkpoint["production_mutation_authorized"])
        self.assertIsNone(checkpoint["validation"]["acceptance_red"])

        reconciliation = checkpoint["baseline_reconciliation"]
        self.assertEqual(reconciliation["previous_authorized_sha"], "4bd061a87852f4bb4b17f5d500ae6ab85081c72b")
        self.assertEqual(reconciliation["current_main_sha"], baseline)
        self.assertEqual(reconciliation["previous_tree_sha"], "8e9942b47cb5231816d4584397d460eaec522846")
        self.assertEqual(reconciliation["current_tree_sha"], reconciliation["previous_tree_sha"])
        self.assertEqual(reconciliation["intermediate_placeholder_commit"], "973490e8358fe0a48dad43933ac3675acd188303")
        self.assertFalse(reconciliation["net_semantic_change"])

        vti06 = next(item for item in backlog["tranches"] if item["id"] == "VTI-06")
        self.assertEqual(vti06["status"], "in_progress")
        self.assertEqual(vti06["application_baseline_sha"], baseline)
        self.assertEqual(vti06["implementation_branch"], branch)
        self.assertTrue(vti06["implementation_authority"])
        self.assertEqual(backlog["active_contract"]["work_item"], "VTI-06")
        self.assertTrue(backlog["active_contract"]["acceptance_package_authorized"])
        self.assertFalse(backlog["active_contract"]["production_mutation_authorized"])

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-06")
        self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
        self.assertEqual(pointer["active_attempt"]["application_baseline_sha"], baseline)
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
        self.assertTrue(pointer["bounded_authority"]["acceptance_package_authorized"])
        self.assertFalse(pointer["bounded_authority"]["production_mutation_authorized"])

        authority = registry["vti_06_authority"]
        self.assertFalse(authority["selected_not_started"])
        self.assertTrue(authority["implementation_authority"])
        self.assertEqual(authority["application_baseline_sha"], baseline)
        self.assertEqual(authority["implementation_branch"], branch)
        self.assertTrue(authority["branch_creation_authorized"])
        self.assertTrue(authority["acceptance_package_authorized"])
        self.assertFalse(authority["production_mutation_authorized"])
        self.assertFalse(authority["scene_map_token_mai_bridge_authorized"])

        self.assertEqual(index["current"]["work_item_id"], "VTI-06")
        self.assertEqual(index["current"]["status"], "in_progress")
        self.assertEqual(index["current"]["application_baseline_sha"], baseline)
        self.assertEqual(index["current"]["implementation_branch"], branch)
        self.assertFalse(index["current"]["production_mutation_authorized"])
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-06")
        self.assertEqual(runtime["active_work"]["state"], "in_progress")
        self.assertEqual(runtime["active_work"]["implementation_branch"], branch)
        self.assertFalse(runtime["active_work"]["production_mutation_authorized"])
        self.assertEqual(runtime["application_repository"]["canonical_main"], baseline)

    def test_vti06_scope_reuses_native_scene_spatial_and_mai_authorities(self):
        checkpoint = load_json("governance/ai/work-state/VTI-06-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        for item in (
            "provider-neutral projection of canonical Scene, map-version and placement semantics into external scene/map/token presentation envelopes",
            "provider-neutral projection of walls, doors, lighting, grid or gridless geometry, elevation, notes and GM-only material only where native canonical semantics and target capability support them",
            "MAI/ISE/SSA asset-reference and semantic-construction-role bridging without making the external VTT an asset, spatial or rules authority",
            "deterministic normalization plus visibility, ownership, consent, hidden-information filtering and GM-authority preservation across scene/map/token projection",
        ):
            self.assertIn(item, scope["authorized"])
        for item in (
            "new canonical spatial, scene, map, token, wall, door, lighting, grid, elevation or asset semantics that duplicate or replace existing native authorities",
            "provider-specific schemas, vendor selection/ranking or VTI-09 platform commitment",
            "credentials, external account mutation, adapter implementation, live external synchronization mutation or canonical game-state mutation",
            "durable VTI persistence or a new migration before separately authorized persistence work",
            "VTI-07 permissions-engine behavior or any VTI-07+ implementation",
        ):
            self.assertIn(item, scope["not_authorized"])


if __name__ == "__main__":
    unittest.main()
