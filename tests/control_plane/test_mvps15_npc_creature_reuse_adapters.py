from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "governance/application-planning/player-species/contracts"
REUSE = D / "MVPS-15_ENTITY_REUSE_CONTRACT.json"
ADAPTERS = D / "MVPS-15_CROSS_SYSTEM_ADAPTER_CONTRACT.json"
HANDOFF = D / "MVPS-15_RUNTIME_HANDOFF_CONTRACT.json"
FIXTURES = D / "MVPS-15_REUSE_ADAPTER_FIXTURES.json"
INVARIANTS = D / "MVPS-15_INVARIANTS.json"


class MVPS15NpcCreatureReuseAdapterTests(unittest.TestCase):
    def _j(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_artifacts_exist(self):
        for path in (REUSE, ADAPTERS, HANDOFF, FIXTURES, INVARIANTS):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_species_canon_is_shared_without_collapsing_entity_layers(self):
        c = self._j(REUSE)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesEntityReuse")
        self.assertEqual(
            c["identity_layers"],
            ["species_definition", "npc_or_creature_definition", "archetype_or_template", "live_instance"],
        )
        self.assertTrue(c["canonical_species_policy"]["single_shared_species_canon"])
        self.assertFalse(c["canonical_species_policy"]["duplicate_npc_species_canon_allowed"])
        self.assertTrue(c["reference_policy"]["exact_version_species_ref_required"])
        self.assertTrue(c["reference_policy"]["provenance_preserved"])
        self.assertFalse(c["reference_policy"]["species_mechanics_copied_into_npc_record"])

    def test_mncs_species_form_composition_remains_owner_authoritative(self):
        c = self._j(REUSE)
        m = c["mncs_handoff"]
        self.assertEqual(m["composition_owner"], "MNCS-14")
        self.assertEqual(m["species_form_authority"], "Species/Form-owner-domains")
        self.assertTrue(m["authoritative_refs_only"])
        self.assertTrue(m["unresolved_composition_preserved"])
        self.assertFalse(m["duplicate_biology_ledger_created"])
        self.assertFalse(m["canonical_npc_or_creature_mutation_owned_by_mvps15"])

    def test_cross_system_adapters_preserve_owner_refs_and_do_not_create_engines(self):
        c = self._j(ADAPTERS)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesCrossSystemAdapters")
        required = {"campaign", "combat", "social", "exploration", "crafting"}
        self.assertTrue(required <= set(c["adapter_domains"]))
        for name in required:
            with self.subTest(domain=name):
                a = c["adapter_domains"][name]
                self.assertTrue(a["source_owner_refs_preserved"])
                self.assertTrue(a["projection_or_mapping_only"])
                self.assertFalse(a["canonical_owner_mutation_performed"])
                self.assertFalse(a["domain_engine_reimplemented"])
        combat = c["adapter_domains"]["combat"]
        self.assertEqual(combat["owner_contract"], "A7 CombatParticipantPort")
        self.assertTrue(combat["participant_source_reference_preserved"])

    def test_runtime_handoff_never_mints_or_infers_unresolved_owner_state(self):
        c = self._j(HANDOFF)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesRuntimeHandoff")
        self.assertEqual(c["mncs_runtime_owner"], "MNCS-22")
        self.assertTrue(c["mapping_proposal_only"])
        self.assertFalse(c["canonical_entity_minted"])
        self.assertFalse(c["live_instance_minted"])
        self.assertFalse(c["cast_membership_mutated"])
        self.assertFalse(c["session_state_mutated"])
        self.assertFalse(c["unresolved_mappings_invented"])
        self.assertTrue(c["late_bound_owner_dependency_remains_explicit"])

    def test_player_only_creation_or_presentation_is_not_an_npc_requirement(self):
        c = self._j(REUSE)
        p = c["player_only_separation"]
        self.assertFalse(p["character_species_selection_required_for_npc"])
        self.assertFalse(p["player_builder_state_required_for_npc"])
        self.assertFalse(p["player_presentation_assets_required_for_npc"])
        self.assertTrue(p["shared_species_definition_reused"])
        self.assertTrue(p["shared_species_runtime_contribution_refs_may_be_consumed_when_owner_compatible"])

    def test_fixtures_cover_reuse_and_all_cross_system_boundaries(self):
        cases = self._j(FIXTURES)["cases"]
        required = {
            "npc_shared_species_reference",
            "creature_form_composition",
            "combat_participant_adapter",
            "campaign_cast_adapter",
            "social_adapter",
            "exploration_adapter",
            "crafting_adapter",
            "unresolved_late_bound_owner",
        }
        self.assertTrue(required <= set(cases))
        self.assertFalse(cases["npc_shared_species_reference"]["expected"]["duplicate_species_record_created"])
        self.assertTrue(cases["creature_form_composition"]["expected"]["species_owner_ref_preserved"])
        self.assertTrue(cases["combat_participant_adapter"]["expected"]["a7_source_reference_preserved"])
        self.assertFalse(cases["campaign_cast_adapter"]["expected"]["cast_membership_mutated"])
        self.assertFalse(cases["unresolved_late_bound_owner"]["expected"]["mapping_invented"])

    def test_invariants_lock_mvps15_scope(self):
        ids = {x["id"] for x in self._j(INVARIANTS)["invariants"]}
        self.assertTrue({
            "MVPS15-I01-single-species-canon",
            "MVPS15-I02-entity-layers-remain-distinct",
            "MVPS15-I03-exact-version-provenance-preserved",
            "MVPS15-I04-mncs-owner-authority-preserved",
            "MVPS15-I05-adapters-not-domain-engines",
            "MVPS15-I06-runtime-handoff-proposal-only",
            "MVPS15-I07-player-only-state-not-npc-required",
            "MVPS15-I08-unresolved-owner-state-not-invented",
        } <= ids)


if __name__ == "__main__":
    unittest.main()
