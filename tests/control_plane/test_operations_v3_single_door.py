from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_VALIDATOR_PATH = ROOT / "scripts/validate_operations_v3.py"
_SPEC = importlib.util.spec_from_file_location("ops3_validator", _VALIDATOR_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise RuntimeError("unable to load Operations V3 validator")
_VALIDATOR = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_VALIDATOR)
_validate_product_lane_projection = getattr(_VALIDATOR, "_validate_product_lane_projection")


class OperationsV3SingleDoorTests(unittest.TestCase):
    def _json(self, path: str) -> dict:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))

    def _text(self, path: str) -> str:
        return (ROOT / path).read_text(encoding="utf-8")

    def test_single_door_files_exist_and_define_one_authority_chain(self) -> None:
        required = [
            "operations/BOOTSTRAP.md",
            "operations/OPERATING_CONTRACT.md",
            "operations/CURRENT.json",
            "operations/LANES.json",
            "operations/CONTROL_SURFACE_REGISTRY.json",
            "operations/work-items/OPS3-01.json",
        ]
        for relative in required:
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)

        current = self._json("operations/CURRENT.json")
        self.assertEqual(current["schema_version"], "3.0.0")
        self.assertEqual(current["canonical_door"], "operations/BOOTSTRAP.md")
        self.assertEqual(current["operating_contract"], "operations/OPERATING_CONTRACT.md")
        self.assertEqual(current["lane_registry"], "operations/LANES.json")
        self.assertEqual(current["status"], "completed_verified")
        self.assertIsNone(current["active_operations_work_item"])
        self.assertFalse(current["product_start_freeze"]["active"])
        self.assertEqual(current["product_start_freeze"]["preserved_selected_work_item"], "MIB-17")
        self.assertFalse(current["product_start_freeze"]["implementation_authority"])
        self.assertEqual(current["lanes"]["operations"]["state"], "completed_verified")
        self.assertFalse(current["lanes"]["operations"]["implementation_authority"])
        product = current["lanes"]["product-development"]
        self.assertEqual(product["state"], "in_progress")
        self.assertEqual(product["selected_work_item"], "MIB-17")
        self.assertEqual(product["attempt_id"], "MIB-17-attempt-001")
        self.assertEqual(product["implementation_branch"], "work/mib-17-family-safety")
        self.assertTrue(product["implementation_authority"])

        work_item = self._json("operations/work-items/OPS3-01.json")
        self.assertEqual(work_item["status"], "completed_verified")
        self.assertFalse(work_item["implementation_authority"])

    def test_product_lane_transition_validation_is_dynamic(self) -> None:
        current = {
            "lanes": {
                "product-development": {
                    "state": "in_progress",
                    "selected_work_item": "MIB-17",
                    "attempt_id": "MIB-17-attempt-001",
                    "implementation_branch": "work/mib-17-family-safety",
                    "implementation_authority": True,
                }
            }
        }
        pointer = {
            "active_attempt": {
                "work_item_id": "MIB-17",
                "attempt_id": "MIB-17-attempt-001",
                "status": "in_progress",
                "implementation_branch": "work/mib-17-family-safety",
                "implementation_authority": True,
            }
        }
        authority = {
            "preserved_product_selection": {
                "work_item": "MIB-17",
                "attempt_id": "MIB-17-attempt-001",
                "state": "in_progress",
                "implementation_branch": "work/mib-17-family-safety",
                "implementation_authority": True,
            }
        }
        checkpoint = {
            "work_item_id": "MIB-17",
            "attempt_id": "MIB-17-attempt-001",
            "status": "in_progress",
            "implementation_branch": "work/mib-17-family-safety",
            "implementation_authority": True,
        }
        errors: list[str] = []
        _validate_product_lane_projection(current, pointer, authority, checkpoint, errors)
        self.assertEqual(errors, [])

    def test_repository_entrypoint_has_no_independent_current_state(self) -> None:
        agents = self._text("AGENTS.md")
        self.assertIn("operations/BOOTSTRAP.md", agents)
        self.assertNotIn("CURRENT_WORK_POINTER", agents)
        self.assertNotIn("STAGE-A-A2", agents)
        self.assertNotIn("MIB-17", agents)
        self.assertNotIn("exact next", agents.lower())

    def test_legacy_bootstrap_is_only_a_redirect(self) -> None:
        legacy = self._text("governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md")
        self.assertIn("HISTORICAL_INERT", legacy)
        self.assertIn("operations/BOOTSTRAP.md", legacy)
        self.assertNotIn("CURRENT_WORK_POINTER.json", legacy)
        self.assertNotIn("execution_termination_preflight.py", legacy)

    def test_control_surface_registry_retires_known_duplicate_selectors(self) -> None:
        registry = self._json("operations/CONTROL_SURFACE_REGISTRY.json")
        self.assertEqual(registry["canonical_door"], "operations/BOOTSTRAP.md")
        by_key = {(row["system"], row["path"]): row for row in registry["surfaces"]}
        expected_non_authoritative = [
            ("AIOC", "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md"),
            ("AIOC", "governance/ai/runtime/CURRENT_WORK_POINTER.json"),
            ("AIOC", "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json"),
            ("AIOC", "governance/ai/runtime/EXECUTION_PROFILE.json"),
            ("AIOC", "governance/ai/interaction-system/OWNER_AI_INTERACTION_CONTRACT.md"),
            ("AIOC", "governance/ai/interaction-system/EXECUTION_TERMINATION_CONTRACT.json"),
        ]
        for key in expected_non_authoritative:
            with self.subTest(key=key):
                self.assertIn(key, by_key)
                self.assertFalse(by_key[key]["can_select_work"])

    def test_lane_registry_uses_one_contract_for_every_lane(self) -> None:
        lanes = self._json("operations/LANES.json")
        self.assertEqual(lanes["operating_contract"], "operations/OPERATING_CONTRACT.md")
        self.assertEqual(lanes["selection_rule"], "User intent selects a lane; lane state never changes the global operating contract.")
        lane_ids = {row["id"] for row in lanes["lanes"]}
        for required in {"product-development", "operations", "content-design", "dwc-speech", "research-evaluation", "source-provenance"}:
            self.assertIn(required, lane_ids)

    def test_legacy_projections_follow_canonical_product_state_without_selecting_work(self) -> None:
        current = self._json("operations/CURRENT.json")
        product = current["lanes"]["product-development"]
        pointer = self._json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        self.assertTrue(pointer["projection_only"])
        self.assertEqual(pointer["active_attempt"]["work_item_id"], product["selected_work_item"])
        self.assertEqual(pointer["active_attempt"]["attempt_id"], product["attempt_id"])
        self.assertEqual(pointer["active_attempt"]["status"], product["state"])
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], product["implementation_branch"])
        self.assertEqual(pointer["active_attempt"]["implementation_authority"], product["implementation_authority"])
        self.assertEqual(pointer["exclusive_control_plane_maintenance"]["status"], "completed_verified")
        self.assertFalse(pointer["exclusive_control_plane_maintenance"]["feature_starts_blocked"])

        authority = self._json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        self.assertTrue(authority["projection_only"])
        self.assertEqual(authority["active_operations_work"]["state"], "completed_verified")
        self.assertFalse(authority["active_operations_work"]["implementation_authority"])
        projection = authority["preserved_product_selection"]
        self.assertEqual(projection["work_item"], product["selected_work_item"])
        self.assertEqual(projection["attempt_id"], product["attempt_id"])
        self.assertEqual(projection["state"], product["state"])
        self.assertEqual(projection["implementation_branch"], product["implementation_branch"])
        self.assertEqual(projection["implementation_authority"], product["implementation_authority"])
        self.assertFalse(projection["feature_starts_blocked"])


if __name__ == "__main__":
    unittest.main()
