from __future__ import annotations

import importlib.util
import json
import tempfile
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

_GENERATOR_PATH = ROOT / "scripts/sync_ops3_compatibility_projections.py"
_GENERATOR_SPEC = importlib.util.spec_from_file_location("ops3_projection_generator", _GENERATOR_PATH)
if _GENERATOR_SPEC is None or _GENERATOR_SPEC.loader is None:
    raise RuntimeError("unable to load OPS3 compatibility projection generator")
_GENERATOR = importlib.util.module_from_spec(_GENERATOR_SPEC)
_GENERATOR_SPEC.loader.exec_module(_GENERATOR)


class OperationsV3SingleDoorTests(unittest.TestCase):
    def _json(self, path: str | Path) -> dict:
        relative = Path(path)
        return json.loads((ROOT / relative).read_text(encoding="utf-8"))

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
        self.assertIn(product["state"], {"selected_not_started", "in_progress", "completed_verified"})
        self.assertTrue(product["selected_work_item"])
        self.assertTrue(product["attempt_id"])
        self.assertTrue(product.get("checkpoint_path") or product.get("legacy_checkpoint_path"))
        if product["state"] == "selected_not_started":
            self.assertIsNone(product["implementation_branch"])
            self.assertFalse(product["implementation_authority"])
        elif product["state"] == "in_progress":
            self.assertTrue(product["implementation_branch"])
            self.assertTrue(product["implementation_authority"])
        else:
            self.assertFalse(product["implementation_authority"])

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

    def test_selected_not_started_product_lane_is_valid_without_branch_or_authority(self) -> None:
        current = {
            "lanes": {
                "product-development": {
                    "state": "selected_not_started",
                    "selected_work_item": "MIB-18",
                    "attempt_id": "MIB-18-attempt-001",
                    "implementation_branch": None,
                    "implementation_authority": False,
                }
            }
        }
        pointer = {
            "active_attempt": {
                "work_item_id": "MIB-18",
                "attempt_id": "MIB-18-attempt-001",
                "status": "selected_not_started",
                "implementation_branch": None,
                "implementation_authority": False,
            }
        }
        authority = {
            "preserved_product_selection": {
                "work_item": "MIB-18",
                "attempt_id": "MIB-18-attempt-001",
                "state": "selected_not_started",
                "implementation_branch": None,
                "implementation_authority": False,
            }
        }
        checkpoint = {
            "work_item_id": "MIB-18",
            "attempt_id": "MIB-18-attempt-001",
            "status": "selected_not_started",
            "implementation_branch": None,
            "implementation_authority": False,
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

    def test_generated_compatibility_manifest_declares_only_two_outputs(self) -> None:
        manifest = self._json("operations/GENERATED_COMPATIBILITY_PROJECTIONS.json")
        self.assertEqual(manifest["canonical_source"], "operations/CURRENT.json")
        self.assertEqual(manifest["generator"], "scripts/sync_ops3_compatibility_projections.py")
        self.assertEqual(
            manifest["outputs"],
            [
                "governance/ai/runtime/CURRENT_WORK_POINTER.json",
                "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json",
            ],
        )
        self.assertIn("NO OPERATIONAL AUTHORITY", manifest["authority_banner"])

    def test_checked_in_generated_compatibility_equals_generator_output(self) -> None:
        rendered = _GENERATOR.render_projections(ROOT)
        self.assertEqual(set(rendered), set(_GENERATOR.ALLOWED_OUTPUTS))
        for relative, expected in rendered.items():
            with self.subTest(path=str(relative)):
                self.assertEqual(self._json(relative), expected)
        self.assertEqual(_GENERATOR.check(ROOT), [])

    def test_generator_reads_current_and_current_referenced_checkpoint_only(self) -> None:
        current = self._json("operations/CURRENT.json")
        product = current["lanes"]["product-development"]
        checkpoint_path = Path(product["checkpoint_path"])
        checkpoint = self._json(checkpoint_path)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "operations").mkdir(parents=True)
            (root / checkpoint_path).parent.mkdir(parents=True)
            (root / "operations/CURRENT.json").write_text(json.dumps(current), encoding="utf-8")
            (root / checkpoint_path).write_text(json.dumps(checkpoint), encoding="utf-8")
            rendered = _GENERATOR.render_projections(root)
            pointer = rendered[_GENERATOR.POINTER]
            authority = rendered[_GENERATOR.AUTHORITY]
            self.assertEqual(pointer["active_attempt"]["work_item_id"], product["selected_work_item"])
            self.assertEqual(pointer["active_attempt"]["status"], product["state"])
            self.assertEqual(pointer["active_attempt"]["implementation_authority"], product["implementation_authority"])
            self.assertEqual(authority["preserved_product_selection"]["work_item"], product["selected_work_item"])
            self.assertEqual(authority["preserved_product_selection"]["state"], product["state"])
            self.assertEqual(authority["preserved_product_selection"]["implementation_authority"], product["implementation_authority"])

    def test_generator_write_set_is_bounded_to_declared_outputs(self) -> None:
        self.assertEqual(
            _GENERATOR.ALLOWED_OUTPUTS,
            (
                Path("governance/ai/runtime/CURRENT_WORK_POINTER.json"),
                Path("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json"),
            ),
        )


if __name__ == "__main__":
    unittest.main()
