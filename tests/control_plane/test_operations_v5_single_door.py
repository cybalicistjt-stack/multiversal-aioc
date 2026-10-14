"""OPS5 source/version and authority tests without rewriting historical OPS4 tests."""
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def load(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
class Ops5ActivationTests(unittest.TestCase):
    def setUp(self):
        self.state=load("operations/CURRENT.json")
        self.lanes=load("operations/LANES.json")
        self.registry=load("operations/CONTROL_SURFACE_REGISTRY.json")
        self.record=load("operations/work-items/OPS5-01.json")
    def test_exact_current_version_and_single_selector(self):
        self.assertEqual(self.state["system"],"OPS5")
        self.assertEqual(self.state["schema_version"],"5.0.0")
        self.assertIsInstance(self.state["state_revision"],int)
        self.assertGreaterEqual(self.state["state_revision"],614)
        self.assertEqual(self.state["canonical_door"],"operations/BOOTSTRAP.md")
        self.assertEqual(self.state["operating_contract"],"operations/OPERATING_CONTRACT.md")
        self.assertEqual(self.state["lane_registry"],"operations/LANES.json")
        self.assertEqual(self.lanes["schema_version"],"5.0.0")
        self.assertEqual(self.registry["schema_version"],"5.0.0")
        self.assertEqual(self.state["active_operations_work_item"],None)
        self.assertEqual(self.state["lanes"]["operations"]["work_item_id"],"OPS5-01")
        self.assertFalse(self.state["product_start_freeze"]["active"])
        selectors={(x["system"],x["path"]) for x in self.registry["surfaces"] if x.get("can_select_work")}
        self.assertEqual(selectors,{("AIOC","operations/BOOTSTRAP.md"),("AIOC","operations/CURRENT.json")})
    def test_completed_upgrade_record_and_resource_source(self):
        self.assertEqual(self.record["status"],"completed_verified")
        self.assertFalse(self.record["implementation_authority"])
        resource=self.state["research_resource"]
        self.assertEqual(resource["repository"],"cybalicistjt-stack/NCG")
        self.assertEqual(resource["source_commit"],self.record["resource_commit"])
        self.assertEqual(resource["entry"],"docs/ncg-brain/ops5/current/README.md")
        self.assertEqual(resource["engine"],"ncg_brain/current_corpus.py")
        self.assertEqual(resource["canonical_work_selector"],"operations/CURRENT.json")
        self.assertFalse(resource["executionAllowed"])
        self.assertFalse(resource["productAcceptanceCertified"])
        self.assertFalse(resource["mandatory_for_trivial_tasks"])
        self.assertEqual(resource["host_skill_installed"],"UNVERIFIED_OPTIONAL")
        self.assertEqual(resource["owner_utility_measurement"],"NOT_RUN")
    def test_product_lanes_remain_persistently_isolated(self):
        current=self.state["lanes"]
        persistent=["gpr","cwks","mtlc"]
        self.assertEqual(self.lanes["persistent_implementation_lanes"],persistent)
        for k in persistent:
            with self.subTest(lane=k):
                lane=current[k]
                self.assertIn(lane["state"],{"selected_not_started","in_progress","completed_verified"})
                self.assertTrue(lane["attempt_id"].startswith(lane["selected_work_item"]+"-attempt-"))
                checkpoint=load(lane["checkpoint_path"])
                for selected,record in (("selected_work_item","work_item_id"),("attempt_id","attempt_id"),("state","status"),("implementation_branch","implementation_branch"),("implementation_authority","implementation_authority")):
                    self.assertEqual(lane[selected],checkpoint[record])
                if lane["state"]=="in_progress":
                    self.assertTrue(lane["implementation_authority"])
                    self.assertTrue(lane["implementation_branch"])
                else:
                    self.assertFalse(lane["implementation_authority"])
                    self.assertIsNone(lane["implementation_branch"])
        self.assertEqual(len({current[k]["attempt_id"] for k in persistent}),len(persistent))
        branches=[current[k]["implementation_branch"] for k in persistent if current[k]["implementation_branch"]]
        self.assertEqual(len(branches),len(set(branches)))
    def test_current_source_is_not_empirical_certification(self):
        resource=self.state["research_resource"]
        self.assertEqual(resource["empirical_research_proofs"],"CASE_SPECIFIC_ONLY")
        self.assertIn("GitHub",resource["fallback"])
        door=(ROOT/"operations/BOOTSTRAP.md").read_text()
        contract=(ROOT/"operations/OPERATING_CONTRACT.md").read_text()
        self.assertIn("Operations V5",door)
        self.assertIn("Operations V5",contract)
        self.assertIn("CI is an **acceptance system, not a remote REPL**",door+contract)
        self.assertIn("blocked",door+contract)
        self.assertIn("research",door+contract)
        self.assertIn("not a new scheduler",contract)
    def test_inherited_guard_scripts_and_single_workflow(self):
        workflow=(ROOT/".github/workflows/validate-repository-health.yml").read_text()
        for p in ("scripts/validate_operations_v5.py","scripts/validate_ops5_semantic_surfaces.py",
                  "tests/control_plane/test_ops4_ci_guard.py"):
            with self.subTest(p=p):
                self.assertIn(p,workflow)
                self.assertTrue((ROOT/p).is_file())
        for p in ("scripts/ops4_execution_guard.py","scripts/ops4_ci_guard.py"):
            self.assertTrue((ROOT/p).is_file())
        self.assertIn("expected-head",workflow)
        self.assertIn("pull_request",workflow)
        self.assertNotIn("git push origin main",workflow)
if __name__=="__main__":
    unittest.main()

