from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


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
        self.assertEqual(current["active_operations_work_item"], "OPS3-01")
        self.assertTrue(current["product_start_freeze"]["active"])
        self.assertEqual(current["product_start_freeze"]["preserved_selected_work_item"], "MIB-17")

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
        by_path = {row["path"]: row for row in registry["surfaces"]}
        expected_non_authoritative = [
            "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md",
            "governance/ai/runtime/CURRENT_WORK_POINTER.json",
            "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json",
            "governance/ai/runtime/EXECUTION_PROFILE.json",
            "governance/ai/interaction-system/OWNER_AI_INTERACTION_CONTRACT.md",
            "governance/ai/interaction-system/EXECUTION_TERMINATION_CONTRACT.json",
        ]
        for path in expected_non_authoritative:
            with self.subTest(path=path):
                self.assertIn(path, by_path)
                self.assertNotEqual(by_path[path]["disposition"], "CANONICAL")

    def test_lane_registry_uses_one_contract_for_every_lane(self) -> None:
        lanes = self._json("operations/LANES.json")
        self.assertEqual(lanes["operating_contract"], "operations/OPERATING_CONTRACT.md")
        self.assertEqual(lanes["selection_rule"], "User intent selects a lane; lane state never changes the global operating contract.")
        lane_ids = {row["id"] for row in lanes["lanes"]}
        for required in {"product-development", "operations", "content-design", "dwc-speech", "research-evaluation", "source-provenance"}:
            self.assertIn(required, lane_ids)


if __name__ == "__main__":
    unittest.main()
