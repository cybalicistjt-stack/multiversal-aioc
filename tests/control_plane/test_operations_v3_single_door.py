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
        operations = current["lanes"]["operations"]
        freeze = current["product_start_freeze"]
        self.assertFalse(freeze["implementation_authority"])
        if current["active_operations_work_item"] is None:
            self.assertIsNone(current["active_operations_work_item_path"])
            self.assertFalse(freeze["active"])
            self.assertEqual(operations["state"], "completed_verified")
            self.assertFalse(operations["implementation_authority"])
        else:
            self.assertEqual(operations["work_item_id"], current["active_operations_work_item"])
            self.assertEqual(operations["work_item_path"], current["active_operations_work_item_path"])
            self.assertEqual(operations["state"], "in_progress")
            self.assertTrue(operations["implementation_authority"])
            self.assertTrue(freeze["active"])
            self.assertEqual(freeze["preserved_selected_work_item"], current["lanes"]["msas"]["selected_work_item"])
            self.assertEqual(freeze["preserved_attempt_id"], current["lanes"]["msas"]["attempt_id"])

        product = current["lanes"]["msas"]
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
                "msas": {
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
                "msas": {
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


    def test_msas_mrcs_and_mvps_lanes_keep_independent_authority(self) -> None:
        current = self._json("operations/CURRENT.json")
        for lane_id in ("msas", "mrcs", "mvps"):
            lane = current["lanes"][lane_id]
            self.assertIn(lane["state"], {"selected_not_started", "in_progress", "completed_verified"})
            checkpoint = self._json(lane["checkpoint_path"])
            self.assertEqual(checkpoint["work_item_id"], lane["selected_work_item"])
            self.assertEqual(checkpoint["attempt_id"], lane["attempt_id"])
            self.assertEqual(checkpoint["status"], lane["state"])
            self.assertEqual(checkpoint["implementation_branch"], lane["implementation_branch"])
            self.assertEqual(checkpoint["implementation_authority"], lane["implementation_authority"])
            if lane["state"] == "selected_not_started":
                self.assertFalse(lane["implementation_authority"])
                self.assertIsNone(lane["implementation_branch"])
            if lane["state"] == "in_progress":
                self.assertTrue(lane["implementation_authority"])
                self.assertTrue(lane["implementation_branch"])

        attempts = {current["lanes"][lane_id]["attempt_id"] for lane_id in ("msas", "mrcs", "mvps")}
        self.assertEqual(len(attempts), 3)
        branches = [
            current["lanes"][lane_id]["implementation_branch"]
            for lane_id in ("msas", "mrcs", "mvps")
            if current["lanes"][lane_id]["implementation_branch"]
        ]
        self.assertEqual(len(branches), len(set(branches)))

        uisr = current["completed_programs"]["UISR"]
        self.assertEqual(uisr["state"], "completed_verified")
        self.assertFalse(uisr["implementation_authority"])

        bootstrap = self._text("operations/BOOTSTRAP.md")
        contract = self._text("operations/OPERATING_CONTRACT.md")
        for lane_id in ("msas", "mrcs", "mvps"):
            self.assertIn(lane_id, bootstrap)
            self.assertIn(lane_id, contract)
        self.assertIn("does **not** pause, revoke, or rewrite another lane", bootstrap)
        self.assertIn("does not implicitly pause, revoke, reorder, or rewrite another active lane", contract)

    def test_mvps_lane_lifecycle_is_independent_and_checkpointed(self) -> None:
        current = self._json("operations/CURRENT.json")
        mvps = current["lanes"]["mvps"]
        self.assertTrue(mvps["selected_work_item"].startswith("MVPS-"))
        self.assertTrue(mvps["attempt_id"].startswith(mvps["selected_work_item"] + "-attempt-"))
        self.assertIn(mvps["state"], {"selected_not_started", "in_progress", "completed_verified"})

        checkpoint = self._json(mvps["checkpoint_path"])
        self.assertEqual(checkpoint["work_item_id"], mvps["selected_work_item"])
        self.assertEqual(checkpoint["attempt_id"], mvps["attempt_id"])
        self.assertEqual(checkpoint["status"], mvps["state"])
        self.assertEqual(checkpoint["implementation_branch"], mvps["implementation_branch"])
        self.assertEqual(checkpoint["implementation_authority"], mvps["implementation_authority"])

        if mvps["state"] == "selected_not_started":
            self.assertIsNone(mvps["implementation_branch"])
            self.assertFalse(mvps["implementation_authority"])
        elif mvps["state"] == "in_progress":
            self.assertTrue(mvps["implementation_branch"])
            self.assertTrue(mvps["implementation_authority"])
        else:
            self.assertFalse(mvps["implementation_authority"])

        msas = current["lanes"]["msas"]
        mrcs = current["lanes"]["mrcs"]
        self.assertNotEqual(mvps["attempt_id"], msas["attempt_id"])
        self.assertNotEqual(mvps["attempt_id"], mrcs["attempt_id"])
        if mvps.get("implementation_branch") and msas.get("implementation_branch"):
            self.assertNotEqual(mvps["implementation_branch"], msas["implementation_branch"])
        if mvps.get("implementation_branch") and mrcs.get("implementation_branch"):
            self.assertNotEqual(mvps["implementation_branch"], mrcs["implementation_branch"])

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
        for required in {"msas", "mrcs", "mvps", "operations", "content-design", "dwc-speech", "research-evaluation", "source-provenance"}:
            self.assertIn(required, lane_ids)

    def test_legacy_projections_follow_canonical_product_state_without_selecting_work(self) -> None:
        current = self._json("operations/CURRENT.json")
        product = current["lanes"]["msas"]
        pointer = self._json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        self.assertTrue(pointer["projection_only"])
        self.assertEqual(pointer["active_attempt"]["work_item_id"], product["selected_work_item"])
        self.assertEqual(pointer["active_attempt"]["attempt_id"], product["attempt_id"])
        self.assertEqual(pointer["active_attempt"]["status"], product["state"])
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], product["implementation_branch"])
        self.assertEqual(pointer["active_attempt"]["implementation_authority"], product["implementation_authority"])
        operations = current["lanes"]["operations"]
        blocked = bool(current["product_start_freeze"]["active"])
        self.assertEqual(pointer["exclusive_control_plane_maintenance"]["work_item_id"], operations["work_item_id"])
        self.assertEqual(pointer["exclusive_control_plane_maintenance"]["status"], operations["state"])
        self.assertEqual(pointer["exclusive_control_plane_maintenance"]["feature_starts_blocked"], blocked)

        authority = self._json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        self.assertTrue(authority["projection_only"])
        self.assertEqual(authority["active_operations_work"]["work_item"], operations["work_item_id"])
        self.assertEqual(authority["active_operations_work"]["state"], operations["state"])
        self.assertEqual(authority["active_operations_work"]["implementation_authority"], operations["implementation_authority"])
        projection = authority["preserved_product_selection"]
        self.assertEqual(projection["work_item"], product["selected_work_item"])
        self.assertEqual(projection["attempt_id"], product["attempt_id"])
        self.assertEqual(projection["state"], product["state"])
        self.assertEqual(projection["implementation_branch"], product["implementation_branch"])
        self.assertEqual(projection["implementation_authority"], product["implementation_authority"])
        self.assertEqual(projection["feature_starts_blocked"], blocked)

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
        product = current["lanes"]["msas"]
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

    def test_three_persistent_implementation_lanes_are_never_collapsed(self) -> None:
        lanes = self._json("operations/LANES.json")
        self.assertEqual(lanes["persistent_implementation_lanes"], ["msas","mrcs","mvps"])
        current = self._json("operations/CURRENT.json")
        for lane_id in lanes["persistent_implementation_lanes"]:
            self.assertIn(lane_id, current["lanes"])

    def test_repository_health_workflow_never_pushes_generated_content_directly_to_main(self) -> None:
        workflow = self._text(".github/workflows/validate-repository-health.yml")
        self.assertNotIn("git push origin HEAD:main", workflow)
        self.assertIn("OPS3 forbids CI/bot direct pushes to protected main", workflow)


if __name__ == "__main__":
    unittest.main()
