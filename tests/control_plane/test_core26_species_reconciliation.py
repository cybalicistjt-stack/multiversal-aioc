import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class Core26SpeciesReconciliationTests(unittest.TestCase):
    def test_core26_validator_passes(self):
        process = subprocess.run(
            [sys.executable, str(ROOT / "tools/validate-core26-species-reconciliation.py")],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        self.assertEqual(process.returncode, 0, process.stdout)
        self.assertIn("CORE26 validation PASS", process.stdout)


if __name__ == "__main__":
    unittest.main()
