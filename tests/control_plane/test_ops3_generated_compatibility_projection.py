from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GENERATOR_PATH = ROOT / "scripts/sync_ops3_compatibility_projections.py"
MANIFEST_PATH = ROOT / "operations/GENERATED_COMPATIBILITY_PROJECTIONS.json"

_SPEC = importlib.util.spec_from_file_location("ops3_projection_generator", GENERATOR_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise RuntimeError("unable to load OPS3 compatibility projection generator")
_GENERATOR = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_GENERATOR)


class OperationsV3GeneratedCompatibilityProjectionTests(unittest.TestCase):
    def _json(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_manifest_declares_only_the_two_generated_compatibility_outputs(self) -> None:
        manifest = self._json(MANIFEST_PATH)
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

    def test_checked_in_compatibility_files_equal_canonical_generator_output(self) -> None:
        rendered = _GENERATOR.render_projections(ROOT)
        self.assertEqual(set(rendered), set(_GENERATOR.ALLOWED_OUTPUTS))
        for relative, expected in rendered.items():
            with self.subTest(path=str(relative)):
                self.assertEqual(self._json(ROOT / relative), expected)
        self.assertEqual(_GENERATOR.check(ROOT), [])

    def test_generator_follows_current_and_referenced_checkpoint_without_using_legacy_inputs(self) -> None:
        current = self._json(ROOT / "operations/CURRENT.json")
        product = current["lanes"]["product-development"]
        checkpoint_path = Path(product["checkpoint_path"])
        checkpoint = self._json(ROOT / checkpoint_path)

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

    def test_write_is_bounded_to_declared_outputs(self) -> None:
        self.assertEqual(
            _GENERATOR.ALLOWED_OUTPUTS,
            (
                Path("governance/ai/runtime/CURRENT_WORK_POINTER.json"),
                Path("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json"),
            ),
        )


if __name__ == "__main__":
    unittest.main()
