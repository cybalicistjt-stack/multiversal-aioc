#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEAD = "1e29fc706a17c39be622b1a1bb450bd5667f3d77"
RUN = 34144077082
REPO_HEALTH = 101812172039
LINUX = 101812200863
WINDOWS = 101812200823
COMPARATOR = 101812291853
RECEIPT = "8c321ae5c93d220ff5fe4ff4171afc140cad82d2e9e6365225a3f89503392dd8"
RECORDED = "2026-09-07T11:38:00-05:00"

red = {
    "head_sha": HEAD,
    "run_id": RUN,
    "repository_health_job": REPO_HEALTH,
    "linux_job": LINUX,
    "windows_job": WINDOWS,
    "deterministic_compare_job": COMPARATOR,
    "deterministic_receipt_sha256": RECEIPT,
    "historical_profile_fanout": 0,
    "failure_stage": "vti09-invariants",
    "failure_reason": "VTI-09 production contract intentionally absent: packages/contracts/src/virtual-tabletop-interoperability/foundry-vtt-first-full-platform-integration-contract.ts",
    "linux_artifact": {"id":10026982756,"digest":"sha256:0b356c460e1be00f69195ad023d54c7e61d982189f03cfe5171bdbc5c5dde0fb"},
    "windows_artifact": {"id":10026987775,"digest":"sha256:9704d1dfbe4d3cc246d348f1980fff46e623e2c556c87546648cd65d739392ed"},
    "comparison_artifact": {"id":10026993548,"digest":"sha256:3bfe1514b7d53c4e7f99dbafcca9777d769f52fd616c81c537b1e144e45abd3e"},
    "recorded_at": RECORDED
}

def load(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8"))
def dump(path,obj):
    (ROOT/path).write_text(json.dumps(obj,separators=(",",":"),ensure_ascii=False)+"\n",encoding="utf-8")

p="governance/ai/work-state/VTI-09-attempt-001.json"; x=load(p)
x["validation"]["acceptance_red"] = red
x["production_mutation_authorized"] = True
x["matching_red_observed"] = True
x["application_pr"] = 438
x["red_unlock_recorded_at"] = RECORDED
x["next_action"] = "Implement only packages/contracts/src/virtual-tabletop-interoperability/foundry-vtt-first-full-platform-integration-contract.ts on application PR #438, then obtain exact-head VTI-09 GREEN on repository health, self-hosted Linux, self-hosted Windows and deterministic comparison before merge."
x["governed_start_boundaries"] = [row for row in x.get("governed_start_boundaries",[]) if "Production Foundry adapter behavior remains locked" not in row]
x["governed_start_boundaries"].append("Genuine matching VTI-09 RED is sealed at exact application head "+HEAD+"; bounded provider-specific production mutation is now authorized only for the registered Foundry adapter contract.")
dump(p,x)

p="governance/ai/runtime/CURRENT_WORK_POINTER.json"; x=load(p)
x["updated_at"] = RECORDED
x["selection_reason"] = "VTI-09 Foundry acceptance RED is sealed from exact app head "+HEAD+" with matching Linux/Windows vti09-invariants failure and deterministic comparator PASS; bounded production mutation is unlocked."
x["bounded_authority"]["production_mutation_authorized"] = True
x["bounded_authority"]["matching_red_observed"] = True
x["bounded_authority"]["vti_scope"] = "VTI-09 Foundry VTT production mutation is unlocked only for the bounded provider-specific adapter contract after sealed matching RED; credentials/network/live mutation/persistence/activation/publication/release remain closed."
x["exact_next_action"] = "Implement only the bounded VTI-09 Foundry adapter contract on application PR #438, then exact-head GREEN and merge before terminal AIOC closeout."
dump(p,x)

p="governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json"; x=load(p)
v=next(row for row in x["tranches"] if row["id"]=="VTI-09")
v["production_mutation_authorized"] = True; v["matching_red_observed"] = True; v["application_pr"] = 438; v["acceptance_red"] = red
x["active_contract"]["production_mutation_authorized"] = True; x["active_contract"]["matching_red_observed"] = True
x["active_contract"]["rule"] = "Foundry VTT is selected; matching VTI-09 RED is sealed and only the bounded provider-specific production contract is unlocked. All credential/network/live-mutation/persistence/activation/publication/release authority remains closed."
dump(p,x)

p="governance/ai/runtime/ROADMAP_INDEX.json"; x=load(p)
x["updated_at"] = RECORDED; x["rule"] = "VTI-09 is in_progress with Foundry VTT selected and matching RED sealed; bounded production mutation is unlocked only for the registered adapter contract."
x["current"]["production_mutation_authorized"] = True; x["current"]["matching_red_observed"] = True; x["current"]["application_pr"] = 438
x["selected_vti"]["matching_red_observed"] = True; x["selected_vti"]["production_mutation_authorized"] = True
dump(p,x)

p="governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json"; x=load(p)
x["updated_at"] = RECORDED
x["active_work"]["production_mutation_authorized"] = True; x["active_work"]["matching_red_observed"] = True; x["active_work"]["application_pr"] = 438
x["active_work"]["execution_rule"] = "Matching VTI-09 RED is sealed. Implement only the registered bounded Foundry adapter contract, then exact-head current-family GREEN and merge."
x["selected_vti"]["matching_red_observed"] = True; x["selected_vti"]["production_mutation_authorized"] = True
dump(p,x)

p="governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json"; x=load(p)
x["updated_at"] = RECORDED
x["active_planning_work"]["implementation_scope"] = "Foundry VTT selected; matching RED sealed; bounded provider-specific production adapter contract unlocked. Credentials/network/live mutation/persistence/activation/publication/release remain closed."
a=x["vti_09_authority"]
a["production_mutation_authorized"] = True; a["matching_red_observed"] = True; a["application_pr"] = 438; a["acceptance_red"] = red
a["provider_specific_schema_authorized_after_red"] = True
for key in ["credential_use_authorized","external_account_use_authorized","provider_network_access_authorized","live_external_mutation_authorized","canonical_mutation_authorized","durable_persistence_authorized","new_migration_authorized","provider_activation_authorized","tester_distribution_authorized","package_publication_authorized","release_or_deployment_authorized","vti10_plus_authorized","sgc01_plus_authorized"]:
    a[key] = False
dump(p,x)

p="tests/control_plane/test_vti09_red_unlock.py"
(ROOT/p).write_text('''import json\nimport unittest\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[2]\ndef load_json(path): return json.loads((ROOT/path).read_text(encoding="utf-8"))\nclass Vti09RedUnlockTests(unittest.TestCase):\n    def test_matching_red_seals_only_bounded_production_authority(self):\n        cp=load_json("governance/ai/work-state/VTI-09-attempt-001.json")\n        pointer=load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")\n        backlog=load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")\n        registry=load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")\n        red=cp["validation"]["acceptance_red"]\n        self.assertEqual(red["head_sha"],"1e29fc706a17c39be622b1a1bb450bd5667f3d77")\n        self.assertEqual(red["run_id"],34144077082)\n        self.assertEqual(red["repository_health_job"],101812172039)\n        self.assertEqual(red["linux_job"],101812200863)\n        self.assertEqual(red["windows_job"],101812200823)\n        self.assertEqual(red["deterministic_compare_job"],101812291853)\n        self.assertEqual(red["deterministic_receipt_sha256"],"8c321ae5c93d220ff5fe4ff4171afc140cad82d2e9e6365225a3f89503392dd8")\n        self.assertEqual(red["historical_profile_fanout"],0)\n        self.assertEqual(red["failure_stage"],"vti09-invariants")\n        self.assertIn("production contract intentionally absent",red["failure_reason"])\n        self.assertTrue(cp["matching_red_observed"]); self.assertTrue(cp["production_mutation_authorized"]); self.assertEqual(cp["application_pr"],438)\n        self.assertTrue(pointer["bounded_authority"]["matching_red_observed"]); self.assertTrue(pointer["bounded_authority"]["production_mutation_authorized"])\n        self.assertTrue(backlog["active_contract"]["matching_red_observed"]); self.assertTrue(backlog["active_contract"]["production_mutation_authorized"])\n        auth=registry["vti_09_authority"]; self.assertTrue(auth["matching_red_observed"]); self.assertTrue(auth["production_mutation_authorized"])\n        for key in ("credential_use_authorized","external_account_use_authorized","provider_network_access_authorized","live_external_mutation_authorized","canonical_mutation_authorized","durable_persistence_authorized","new_migration_authorized","provider_activation_authorized","tester_distribution_authorized","package_publication_authorized","release_or_deployment_authorized","vti10_plus_authorized","sgc01_plus_authorized"):\n            self.assertFalse(auth[key],key)\nif __name__=="__main__": unittest.main()\n''',encoding="utf-8")
print("VTI-09 RED unlock projection complete")
