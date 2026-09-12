import json,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class ReadinessTests(unittest.TestCase):
 def test_index_is_derived_and_complete(self):
  p=subprocess.run([sys.executable,"scripts/build_tranche_readiness.py","--root",str(ROOT),"--check"],cwd=ROOT,text=True,capture_output=True);self.assertEqual(p.returncode,0,p.stdout+p.stderr);idx=json.loads((ROOT/"governance/ai/runtime/TRANCHE_READINESS_INDEX.json").read_text());ids=[wid for row in idx["programs"].values() for wid in row["work_items"]];self.assertEqual(idx["total_tranches"],281);self.assertEqual(len(ids),281);self.assertEqual(len(set(ids)),281)
 def test_readiness_never_grants_authority_or_branch(self):idx=json.loads((ROOT/"governance/ai/runtime/TRANCHE_READINESS_INDEX.json").read_text());self.assertFalse(idx["branch_policy"]["created_before_governed_start"]);self.assertFalse(idx["authority_policy"]["implementation_authority"]);self.assertTrue(idx["authority_policy"]["readiness_never_grants_authority"])
 def test_near_term_hot_ready(self):idx=json.loads((ROOT/"governance/ai/runtime/TRANCHE_READINESS_INDEX.json").read_text());hot={x for row in idx["programs"].values() for x in row["hot_ready_overrides"]};self.assertEqual(hot,{"ARI-18","ARI-19","ARI-20","ARI-21","ARI-22A","ARI-22B","ARI-22C","MIB-16","MIB-17","MIB-18"})
if __name__=="__main__":unittest.main()
