from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "governance/application-planning/player-species/contracts"
SOCIAL = D / "MVPS-11_SOCIAL_IDENTITY_HOOK_CONTRACT.json"
LANGUAGE = D / "MVPS-11_LANGUAGE_COMMUNICATION_HOOK_CONTRACT.json"
KNOWLEDGE = D / "MVPS-11_KNOWLEDGE_VISIBILITY_HOOK_CONTRACT.json"
FIXTURES = D / "MVPS-11_SOCIAL_LANGUAGE_KNOWLEDGE_FIXTURES.json"
INVARIANTS = D / "MVPS-11_INVARIANTS.json"


class MVPS11SocialLanguageKnowledgeTests(unittest.TestCase):
    def _j(self, p: Path) -> dict:
        return json.loads(p.read_text(encoding="utf-8"))

    def test_required_artifacts_exist(self):
        for p in (SOCIAL, LANGUAGE, KNOWLEDGE, FIXTURES, INVARIANTS):
            with self.subTest(path=p):
                self.assertTrue(p.is_file(), p)

    def test_culture_and_behavior_are_not_biology(self):
        c = self._j(SOCIAL)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesSocialIdentityHook")
        self.assertFalse(c["culture_is_biology"])
        self.assertFalse(c["species_identity_implies_behavior"])
        self.assertFalse(c["species_identity_auto_creates_relationship"])
        self.assertFalse(c["species_identity_auto_creates_reputation"])
        self.assertFalse(c["species_identity_auto_assigns_faction_membership"])
        self.assertFalse(c["species_identity_auto_grants_legal_status"])
        self.assertEqual(c["culture_context_policy"], "reference_only_never_immutable_biology")

    def test_social_domains_remain_shared_owner_truth(self):
        c = self._j(SOCIAL)
        owners = c["owner_domain_handoffs"]
        self.assertEqual(owners["personal_relationship"], "MV-IA-F009 / Relationship owner")
        self.assertEqual(owners["faction_standing_reputation"], "MV-IA-F016 / Faction-Reputation owner")
        self.assertEqual(owners["membership_rank_office"], "Organization/Faction owner")
        self.assertEqual(owners["law_legal_status"], "Law/World/Campaign owning domain")
        self.assertFalse(c["social_state_mutation_owned_by_mvps11"])
        self.assertEqual(c["unknown_or_conflict_policy"], "surface_unresolved_not_guess")

    def test_biological_communication_and_learned_language_are_distinct(self):
        c = self._j(LANGUAGE)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesLanguageCommunicationHook")
        self.assertTrue(c["biological_communication_distinct_from_learned_language"])
        self.assertFalse(c["biological_communication_implies_language_proficiency"])
        self.assertFalse(c["learned_language_is_immutable_biology"])
        self.assertFalse(c["species_local_language_engine_created"])
        self.assertEqual(c["learned_language_policy"], "shared_language_knowledge_progression_owner_handoff")
        self.assertTrue(c["exact_source_and_provenance_refs_required"])

    def test_observer_knowledge_never_rewrites_canonical_identity(self):
        c = self._j(KNOWLEDGE)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesIdentityKnowledgeHook")
        self.assertTrue(c["canonical_identity_distinct_from_observer_knowledge"])
        self.assertTrue(c["observer_misidentification_allowed_as_belief_only"])
        self.assertFalse(c["observer_belief_can_rewrite_canonical_identity"])
        self.assertTrue(c["permission_filter_before_projection_and_derivatives"])
        self.assertFalse(c["hidden_identity_leaks_through_counts_search_diagnostics_or_ai"])
        self.assertEqual(c["unknown_or_hidden_policy"], "preserve_unknown_hidden_or_misidentified_without_truth_inference")

    def test_fixtures_cover_acceptance_and_owner_boundaries(self):
        f = self._j(FIXTURES)["cases"]
        self.assertTrue({
            "culture_adjacent_not_biology",
            "biological_signal_not_learned_language",
            "learned_language_owner_handoff",
            "relationship_reputation_owner_deferred",
            "observer_hidden_identity",
            "observer_misidentification_without_truth_mutation",
            "unknown_social_identity_fact_unresolved",
        } <= set(f))
        self.assertEqual(f["culture_adjacent_not_biology"]["expected"]["classification"], "culture_context")
        self.assertFalse(f["biological_signal_not_learned_language"]["expected"]["language_proficiency_granted"])
        self.assertEqual(f["learned_language_owner_handoff"]["expected"]["status"], "owner_deferred")
        self.assertEqual(f["relationship_reputation_owner_deferred"]["expected"]["status"], "owner_deferred")
        self.assertEqual(f["observer_hidden_identity"]["expected"]["visible_identity"], "hidden")
        self.assertTrue(f["observer_misidentification_without_truth_mutation"]["expected"]["canonical_identity_unchanged"])
        self.assertEqual(f["unknown_social_identity_fact_unresolved"]["expected"]["status"], "unresolved")

    def test_invariants_cover_acceptance_and_boundaries(self):
        ids = {x["id"] for x in self._j(INVARIANTS)["invariants"]}
        self.assertTrue({
            "MVPS11-I01-culture-separate-from-biology",
            "MVPS11-I02-no-species-behavior-stereotype-inference",
            "MVPS11-I03-biological-communication-not-learned-language",
            "MVPS11-I04-social-owner-delegation",
            "MVPS11-I05-canonical-identity-separate-from-observer-knowledge",
            "MVPS11-I06-hidden-truth-filter-before-derivatives",
            "MVPS11-I07-unknowns-not-fabricated",
            "MVPS11-I08-no-social-language-knowledge-runtime-engine",
        } <= ids)


if __name__ == "__main__":
    unittest.main()
