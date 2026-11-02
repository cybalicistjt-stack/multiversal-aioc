"""XTRA-04 source-linked fixture assertions; never asserts actual gameplay occurred."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

MANIFEST_PATH = "governance/application-planning/xtra-pre-pcv-readiness/XTRA-04_BEACON_DEBT_GOLDEN_CAMPAIGN_FIXTURE_v1.0.0.json"
RUNTIME_PATH = "evidence/content-pipeline/beacon-debt-runtime-instantiated.json"
CANDIDATE_PATH = "evidence/content-pipeline/beacon-debt-runtime-fixture-candidate.json"
MECHANICS_PATH = "content-source/beacon-debt-golden-test-mechanics-v1.0.0.json"

class Xtra04GoldenFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = load(MANIFEST_PATH)
        cls.r = load(RUNTIME_PATH)
        cls.c = load(CANDIDATE_PATH)
        cls.rules = load(MECHANICS_PATH)

    def test_source_provenance_and_no_runtime_claim(self):
        m, r = self.m, self.r
        self.assertEqual(m["status"], "SOURCE_GROUNDED_ACCEPTANCE_SPEC_ONLY")
        self.assertEqual([x["path"] for x in m["source_pin"]["sources"]],
                         [RUNTIME_PATH, CANDIDATE_PATH, MECHANICS_PATH])
        self.assertEqual(m["campaign"]["id"], r["campaign"]["campaignId"])
        self.assertEqual(m["campaign"]["pack_lock_digest"], r["campaign"]["packLockId"])
        self.assertEqual(m["campaign"]["fixture_snapshot_ref"], r["launchSnapshot"]["snapshotId"])
        self.assertEqual(m["campaign"]["character_bindings_present"], 0)
        self.assertEqual(len(r["launchSnapshot"]["participantBindings"]), 1)
        self.assertEqual(r["launchSnapshot"]["participantBindings"][0]["role"], "gm")
        self.assertFalse(r["playSequenceExecuted"])
        self.assertFalse(r["productionPersistentRuntimeStateCreated"])
        self.assertFalse(m["campaign"]["real_persistence_executed"])
        self.assertFalse(m["campaign"]["live_actions_executed"])
        self.assertFalse(m["proof_limits"]["actual_two_human_play"])
        self.assertFalse(m["proof_limits"]["actual_combat"])

    def test_five_scenes_are_existing_gridless_source_graph(self):
        scenes = self.m["scenes"]
        self.assertEqual(len(scenes), 5)
        self.assertEqual([s["scene_id"] for s in scenes], [s["sceneId"] for s in self.r["scenes"]])
        self.assertEqual([s["scene_id"] for s in scenes], [s["sceneId"] for s in self.c["sceneDrafts"]])
        for source_scene, prepared in zip(self.r["scenes"], scenes):
            self.assertEqual(prepared["next"], source_scene["branchTargetSceneIds"])
            self.assertTrue(prepared["map_binding"]["gridless"])
            map_entry = next(x for x in self.r["maps"] if x["sceneId"] == source_scene["sceneId"])
            self.assertEqual(prepared["map_binding"]["semantic_alternative"], map_entry["nonvisualAlternative"])
            self.assertFalse(prepared["actual_executed"])
        self.assertIn("social_encounter_noncombat", [s["acceptance_class"] for s in scenes])
        self.assertIn("exploration_transition", [s["acceptance_class"] for s in scenes])

    def test_actions_and_effects_are_only_packet_local_predictions(self):
        actions = {a["action_ref"]: a for a in self.m["actions"]}
        source = [x for x in self.rules["records"] if x["objectType"] == "mv.object.action-definition"]
        self.assertEqual(len(actions), len(source))
        inputs = self.c["deterministicInputContract"]["defaultGoldenPathInputs"]
        for definition in source:
            ref = definition["id"] + "@" + definition["contentVersion"]
            a = actions[ref]
            self.assertEqual(a["target"], definition["target"])
            self.assertEqual(a["fixture_input_total"], inputs[ref])
            self.assertEqual(a["predicted_outcome"], "success")
            self.assertEqual(a["success_effect_refs"],
                [x["objectId"] + "@" + x["objectVersion"] for x in definition["successEffectRefs"]])
            self.assertEqual(a["failure_effect_refs"],
                [x["objectId"] + "@" + x["objectVersion"] for x in definition["failureEffectRefs"]])
            self.assertEqual(a["gameplay_execution_status"], "NOT_RUN")
        effects = {e["ref"] for e in self.m["effect_registry"]}
        for a in actions.values():
            self.assertTrue(set(a["success_effect_refs"] + a["failure_effect_refs"]) <= effects)
        self.assertEqual({x["ref"] for x in self.m["effect_registry"]},
            {x["id"] + "@" + x["contentVersion"] for x in self.rules["records"]
                if x["objectType"] == "mv.object.effect-definition"})

    def test_hidden_state_resources_and_release_gates_remain_closed(self):
        self.assertEqual(self.m["initial_state"], self.r["initialCampaignLocalState"])
        self.assertEqual(self.m["hidden_information"]["hidden_clue_ids"],
                         self.c["visibilityPolicyCandidate"]["initiallyHiddenClueIds"])
        self.assertEqual(self.m["hidden_information"]["initial_player_knowledge_created"], False)
        self.assertEqual(len(self.m["negative_cases"]), 6)
        self.assertTrue(all(x["status"] == "NOT_RUN" for x in self.m["negative_cases"]))
        self.assertTrue(all(x["status"] == "BLOCKED" for x in self.m["future_pcv_integration"]))
        self.assertEqual(self.m["rights"]["commercial_clearance"], "UNVERIFIED_REQUIRES_XTRA05")
        self.assertEqual(self.m["rights"]["asset_catalog_clearance"], "PENDING_XTRA05")
        self.assertTrue(all(x["step"] == i + 1 for i, x in enumerate(self.m["scenes"])))

if __name__ == "__main__":
    unittest.main()
