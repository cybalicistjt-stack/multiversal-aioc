import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
MODEL = ENV_DIR / "ENV-14_ABILITY_CREATOR_RECONCILIATION_v1.0.0.json"
CROSSWALK = ENV_DIR / "ENV-14_SOURCE_COLLECTION_CROSSWALK_v1.0.0.csv"
CONTRACT = ENV_DIR / "ENV-14_CREATOR_COMPOSITION_CONTRACT.md"
REPORT = ENV_DIR / "ENV-14_FULL_LIBRARY_RECONCILIATION_REPORT.md"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"


class Env14AbilityCreatorReconciliationTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def load_csv(self, path):
        with path.open(encoding="utf-8", newline="") as fh:
            return list(csv.DictReader(fh))

    def test_source_corpus_counts_and_receipts_are_locked(self):
        model = self.load_json(MODEL)
        counts = model["source_corpus_counts"]
        self.assertEqual(counts["prestige_env_ability_rows"], 296)
        self.assertEqual(counts["source_collections"], 38)
        self.assertEqual(counts["collection_records"], 38)
        self.assertEqual(counts["member_records"], 258)
        self.assertEqual(counts["environment_specific_collections"], 36)
        self.assertEqual(counts["environment_specific_member_records"], 245)
        self.assertEqual(counts["multi_environment_member_records"], 5)
        self.assertEqual(counts["chaos_foam_member_records"], 8)
        self.assertEqual(counts["canonical_environment_ability_links"], 68)
        self.assertEqual(counts["canonical_linked_profiles"], 17)
        self.assertEqual(counts["promoted_profiles_without_canonical_links"], 23)
        self.assertEqual(counts["source_supported_environment_specific_members_not_canonically_promoted"], 177)
        receipts = model["source_receipts"]
        self.assertEqual(receipts["prestige_env_abilities_sha256"], "052897f355daa1719d7e44ad04642f3cdb5ccff208b2302f24c81711f8a205d4")
        self.assertEqual(receipts["environment_ability_links_sha256"], "fd07619688d5aa92f9315c7ac88eb12ab6d55a38f4d7acc8d3055c3724c22f68")
        self.assertEqual(receipts["canonical_link_identity_digest"], "d566367cdbeac7c9201665c1716dbdbc7b19623c84cfa97f84a92e07dd5eb04a")
        self.assertTrue(receipts["all_68_governed_source_keys_resolved"])
        self.assertEqual(receipts["unique_canonical_ability_ids"], 68)

    def test_collection_crosswalk_preserves_three_authority_states(self):
        rows = self.load_csv(CROSSWALK)
        self.assertEqual(len(rows), 38)
        by_state = {}
        for row in rows:
            by_state.setdefault(row["Reconciliation_State"], []).append(row)
        self.assertEqual(len(by_state["canonical_links_preserved"]), 17)
        self.assertEqual(len(by_state["source_collection_present_not_canonically_promoted"]), 19)
        self.assertEqual(len(by_state["multi_environment_source_collection_not_preset_specific"]), 1)
        self.assertEqual(len(by_state["source_backed_overlay_context_seam"]), 1)
        exact = [r for r in rows if r["Preset_ID"]]
        self.assertEqual(len(exact), 36)
        self.assertEqual(len({r["Preset_ID"] for r in exact}), 36)
        self.assertTrue(all(r["Inference_Authorized"] == "NO" for r in rows))
        chaos = next(r for r in rows if r["Source_Collection"] == "Chaos and Foam Environment Perk Tree")
        self.assertEqual(chaos["Overlay_ID"], "OVL-SUP-CHAOS-FOAM")
        self.assertEqual(chaos["Canonical_Link_Count"], "0")

    def test_missing_and_expanded_presets_do_not_receive_inferred_links(self):
        model = self.load_json(MODEL)
        self.assertEqual(set(model["source_profiles_without_environment_ability_collection"]), {
            "Industrial Zones", "Floating Megacity", "Wormhole Convergence", "Nebula"
        })
        policy = model["inference_policy"]
        self.assertFalse(policy["archetype_similarity_creates_ability_links"])
        self.assertFalse(policy["overlay_similarity_creates_ability_links"])
        self.assertFalse(policy["habitat_or_property_similarity_creates_canonical_links"])
        self.assertFalse(policy["new_env06_through_env10_presets_inherit_source_tree_links"])
        self.assertFalse(policy["unpromoted_source_members_become_canonical_by_reconciliation"])
        self.assertEqual(model["full_library_counts"]["preset_count"], 76)
        self.assertEqual(model["full_library_counts"]["archetype_count"], 19)
        self.assertEqual(model["full_library_counts"]["overlay_count"], 47)
        self.assertEqual(model["full_library_counts"]["post_env05_expansion_presets"], 36)

    def test_creator_contract_is_explainable_and_never_auto_grants(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "exact source relationship outranks environmental similarity",
            "source-supported but not canonically promoted",
            "must never auto-grant an ability",
            "must never manufacture a canonical link from archetype, overlay, Habitat Signature, or property similarity",
            "Chaos/Foam Influence is a context seam, not an ability bundle",
            "Special Perks (Applicable to Multiple Environments) remain ability-system-owned",
            "source provenance must be visible in every ability suggestion",
            "custom environment creator",
            "Resolved Environment remains derived and read-only",
        ]:
            self.assertIn(phrase, text)

    def test_full_library_report_preserves_boundaries(self):
        text = REPORT.read_text(encoding="utf-8")
        for phrase in [
            "68 canonical Environment->Ability links remain unchanged",
            "177 environment-specific source member records remain source-supported but not canonically promoted",
            "No new ability link was inferred for the 36 post-ENV-05 presets",
            "No ability is granted by selecting a preset, archetype, overlay, or local environment",
            "ENV-15 owns Habitat Signature vocabulary",
            "CEW owns creature ecology and distribution",
            "application implementation authority remains false",
        ]:
            self.assertIn(phrase, text)

    def test_candidate_keeps_env14_selected_until_closeout(self):
        backlog = self.load_json(BACKLOG)
        statuses = {item["id"]: item["status"] for item in backlog["tranches"]}
        self.assertEqual(backlog["completed_through"], "ENV-13")
        self.assertEqual(backlog["current_item"], "ENV-14")
        self.assertEqual(statuses["ENV-14"], "selected_not_started")
        self.assertFalse(backlog["application_implementation_authority"])


if __name__ == "__main__":
    unittest.main()
