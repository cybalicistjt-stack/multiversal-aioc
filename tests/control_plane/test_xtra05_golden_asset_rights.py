"""XTRA-05 source and rights evidence consistency; no commercial-license conclusions."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
AUDIT = "governance/application-planning/xtra-pre-pcv-readiness/XTRA-05_BEACON_ASSET_RIGHTS_COVERAGE_v1.0.0.json"
RUNTIME = "evidence/content-pipeline/beacon-debt-runtime-instantiated.json"
FIXTURE = "governance/application-planning/xtra-pre-pcv-readiness/XTRA-04_BEACON_DEBT_GOLDEN_CAMPAIGN_FIXTURE_v1.0.0.json"
OCS = "governance/application-planning/resource-source-catalog/OPEN_CONTENT_SOURCE_CATALOG.json"
OARC = "governance/application-planning/operational-asset-readiness-closure/OARC-07_COVERAGE_GAP_CERTIFICATION_CONTRACT_v1.0.0.json"
CAPABILITIES = {"private-use", "transform", "campaign-use", "export", "redistribution", "commercial-use"}

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Xtra05GoldenAssetRightsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = load(AUDIT)
        cls.r = load(RUNTIME)
        cls.f = load(FIXTURE)
        cls.ocs = load(OCS)
        cls.oarc = load(OARC)

    def test_all_five_scenes_have_exact_source_and_explicit_nonvisual_alternative(self):
        scenes = self.a["scenes"]
        self.assertEqual(len(scenes), len(self.r["scenes"]))
        self.assertEqual([s["scene_id"] for s in scenes], [s["sceneId"] for s in self.r["scenes"]])
        for source, row in zip(self.r["scenes"], scenes):
            source_map = next(m for m in self.r["maps"] if m["sceneId"] == source["sceneId"])
            self.assertEqual(row["scene_type"], source["sceneType"])
            self.assertEqual(row["placement_count"], sum(p["sceneId"] == source["sceneId"] for p in self.r["placements"]))
            presentation = row["media_presentation"]
            self.assertEqual(presentation["fixture_coordinate_mode"], "gridless")
            self.assertEqual(presentation["semantic_nonvisual_alternative"], source_map["nonvisualAlternative"])
            self.assertTrue(presentation["semantic_nonvisual_alternative"])
            self.assertEqual(presentation["fixture_media_reference_count"], 0)
            self.assertFalse(presentation["native_android_windows_projection"] == "VERIFIED")
        self.assertEqual(len(self.f["scenes"]), len(scenes))

    def test_all_34_governed_placement_references_are_identical_to_source(self):
        rows = self.a["placements"]
        self.assertEqual(len(rows), len(self.r["placements"]))
        self.assertEqual(len(rows), 34)
        self.assertEqual({x["placement_id"] for x in rows}, {x["placementId"] for x in self.r["placements"]})
        source_by_id = {x["placementId"]: x for x in self.r["placements"]}
        for row in rows:
            src = source_by_id[row["placement_id"]]
            self.assertEqual(row["scene_id"], src["sceneId"])
            self.assertEqual(row["placement_kind"], src["placementKind"])
            self.assertEqual(row["definition_owner"], src["sourceDefinition"]["ownerDomain"])
            self.assertEqual(row["object_id"], src["sourceDefinition"]["objectId"])
            self.assertEqual(row["object_version"], src["sourceDefinition"]["objectVersion"])
            self.assertIsNone(row["resource_byte_sha256"])
            self.assertIsNone(row["per_asset_license_evidence"])
            self.assertEqual(set(row["rights_capabilities"]), CAPABILITIES)
            self.assertTrue(all(v == "unknown" for v in row["rights_capabilities"].values()))
            self.assertEqual(row["rights_decision"], "NOT_CLEARED_FOR_MEDIA_EXPORT_OR_COMMERCIAL_DISTRIBUTION")
            self.assertEqual(row["runtime_rendering_proof"], "NOT_RUN")

    def test_cross_cutting_asset_demands_are_unresolved_not_absent_claims(self):
        names = {x["need_id"] for x in self.a["additional_product_demands"]}
        self.assertEqual(names, {f"PCV10-A{i:02d}" for i in range(1, 10)})
        for demand in self.a["additional_product_demands"]:
            self.assertFalse(demand["source_binding_proven"])
            self.assertFalse(demand["rights_capabilities_verified"])
            self.assertFalse(demand["asset_delivery_proven"])
            self.assertEqual(demand["required_or_optional"], "PCV_OWNED_DEMAND_DETERMINATION_PENDING")
            self.assertIn("UNRESOLVED", demand["golden_path_blocker_state"])
        self.assertEqual(self.a["coverage"]["source_npc_placements"], 3)
        self.assertEqual(self.a["coverage"]["source_item_placements"], 3)
        self.assertEqual(self.a["coverage"]["source_media_bindings"], 0)
        self.assertEqual(self.a["coverage"]["nonvisual_scene_alternatives"], 5)

    def test_rights_authority_and_oarc_gaps_are_preserved(self):
        a = self.a
        self.assertEqual(set(a["rights_rules"]["capabilities"]), CAPABILITIES)
        self.assertEqual(a["rights_rules"]["default_for_unobserved_rights"], "unknown")
        self.assertEqual(a["rights_rules"]["catalog_sources"], len(self.ocs["sources"]))
        self.assertEqual(a["coverage"]["oarc_game_ready_rows"], self.oarc["coverage"]["counts"]["game_ready"])
        self.assertEqual(a["coverage"]["oarc_governed_rows"], 6708)
        self.assertEqual(a["rights_rules"]["commercial_pack_export"], "NOT_CLEARED")
        self.assertEqual(a["cross_domain_gaps"]["runtime_two_human"], "NOT_RUN")
        self.assertEqual(a["cross_domain_gaps"]["asset_rights_distribution"], "NOT_CLEARED")
        self.assertEqual(a["cross_domain_gaps"]["actual_combat"], "NOT_PRESENT_IN_BEACON_FIXTURE")

if __name__ == "__main__":
    unittest.main()
