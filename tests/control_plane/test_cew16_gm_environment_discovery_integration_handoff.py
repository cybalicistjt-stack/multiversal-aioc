import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
HANDOFF = CEW / "CEW-16_GM_ENVIRONMENT_DISCOVERY_HANDOFF_v1.0.0.json"
MATRIX = CEW / "CEW-16_DISCOVERY_FACET_BINDING_MATRIX_v1.0.0.json"
CONTRACT = CEW / "CEW-16_GM_DISCOVERY_INTEGRATION_CONTRACT.md"
REPORT = CEW / "CEW-16_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"
PROGRAM = CEW / "CEW_CREATURE_ECOLOGY_WILDLIFE_PROGRAM.md"


class Cew16GmEnvironmentDiscoveryIntegrationHandoffTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_cew16_terminal_handoff_contract(self):
        for path in (HANDOFF, MATRIX, CONTRACT, REPORT):
            self.assertTrue(path.exists(), f"missing CEW-16 artifact: {path.name}")

        handoff = self.load(HANDOFF)
        matrix = self.load(MATRIX)
        backlog = self.load(BACKLOG)
        contract = CONTRACT.read_text(encoding="utf-8")
        report = REPORT.read_text(encoding="utf-8")
        program = PROGRAM.read_text(encoding="utf-8")

        self.assertEqual(handoff["contract_id"], "CEW-GM-DISC-1.0")
        self.assertEqual(handoff["work_item"], "CEW-16")
        self.assertEqual(handoff["environment_projection_authority"], "ENV-CD-1.0")
        self.assertEqual(handoff["habitat_signature_authority"], "ENV-HS-1.0")
        self.assertFalse(handoff["application_implementation_authority"])
        self.assertTrue(handoff["projection_is_read_only"])
        self.assertFalse(handoff["projection_creates_encounter_placement"])
        self.assertFalse(handoff["projection_creates_relationship_state"])

        self.assertEqual(handoff["gate_order"], [
            "identity_and_authority_gate",
            "campaign_visibility_gate",
            "canonical_distribution_gate",
            "ecological_fit_gate",
            "overlay_condition_gate",
            "season_activity_gate",
            "projection_facet_derivation",
            "stable_grouping_and_trace",
        ])
        self.assertEqual(set(handoff["query_modes"]), {
            "normal_discovery", "include_blocked", "include_unresolved"
        })
        self.assertFalse(handoff["semantics"]["can_occur_here_equals_normally_occurs_here"])
        self.assertFalse(handoff["semantics"]["habitat_fit_creates_presence"])
        self.assertFalse(handoff["semantics"]["ecological_role_creates_encounter_placement"])
        self.assertFalse(handoff["semantics"]["relationship_eligibility_creates_bond"])
        self.assertTrue(handoff["semantics"]["material_unknowns_fail_closed"])

        authority_ids = {row["contract_id"] for row in handoff["authority_bindings"]}
        for required in {
            "CEW-ID-1.0", "CEW-TAX-1.0", "CEW-CLASS-1.0", "CEW-HAB-1.0",
            "CEW-DIST-1.0", "CEW-ECO-1.0", "CEW-COG-PART-1.0",
            "CEW-HAV-LIN-1.0", "CEW-REL-PATH-1.0", "CEW-EARTHLIKE-BASE-1.0",
            "CEW-ENV-GAP-1.0", "CEW-ALIEN-WILD-1.0", "CEW-MON-EXTRA-1.0",
        }:
            self.assertIn(required, authority_ids)

        readiness = {row["corpus_id"]: row for row in handoff["candidate_universe_partitions"]}
        self.assertEqual(readiness["canonical-creature-definitions"]["record_count"], 27)
        self.assertEqual(readiness["cew12-earthlike-baseline"]["record_count"], 100)
        self.assertEqual(readiness["cew13-environment-gap-profiles"]["record_count"], 29)
        self.assertEqual(readiness["cew14-alien-wildlife-profiles"]["record_count"], 10)
        self.assertEqual(readiness["cew15-extraordinary-profiles"]["record_count"], 6)
        for corpus_id in (
            "cew12-earthlike-baseline",
            "cew13-environment-gap-profiles",
            "cew14-alien-wildlife-profiles",
            "cew15-extraordinary-profiles",
        ):
            self.assertFalse(readiness[corpus_id]["canonical_distribution_prepopulated"])
            self.assertEqual(readiness[corpus_id]["default_presence_without_distribution_authority"], "unresolved")

        facet_ids = {row["facet_id"] for row in matrix["gm_discovery_facets"]}
        for required in {
            "native_common", "possible_tolerated", "migratory_seasonal",
            "introduced_invasive", "predator", "prey_grazer_herd",
            "small_fauna_invertebrate", "aerial_aquatic_subterranean",
            "dangerous_wildlife", "extraordinary_creature", "sapient_native_fauna",
            "npc_capable", "pet_companion_candidate", "mount_pack_work_service_candidate",
            "familiar_compatible", "overlay_enabled", "canonical_presence_conflict",
            "excluded_or_blocked", "unresolved",
        }:
            self.assertIn(required, facet_ids)

        for row in matrix["gm_discovery_facets"]:
            self.assertTrue(row["authority_contracts"])
            self.assertFalse(row["creates_canonical_distribution"])
            self.assertFalse(row["creates_encounter_placement"])
            self.assertFalse(row["creates_relationship_state"])

        cases = {row["case_id"]: row for row in handoff["reference_cases"]}
        self.assertEqual(cases["compatible-but-distribution-unknown"]["outcome"], "unresolved")
        self.assertEqual(cases["canonical-presence-ecology-conflict"]["outcome"], "discoverable_with_warning")
        self.assertIn("canonical_presence_conflict", cases["canonical-presence-ecology-conflict"]["facets"])
        self.assertEqual(cases["sapient-voluntary-partnership"]["relationship_effect"], "eligibility_only_no_bond")

        self.assertEqual(backlog["status"], "completed_parallel_content_authoring")
        self.assertEqual(backlog["completed_through"], "CEW-16")
        self.assertEqual(backlog["current_item"], "CEW-16")
        states = {row["id"]: row["status"] for row in backlog["tranches"]}
        self.assertEqual(states["CEW-16"], "completed_verified")
        self.assertIsNone(backlog["strict_successor_item"])
        self.assertEqual(backlog["application_integration_handoff_state"], "ready_for_separately_governed_software_selection")
        self.assertFalse(backlog["application_integration_authorized"])
        self.assertEqual(backlog["cew16_decisions"]["contract_id"], "CEW-GM-DISC-1.0")

        self.assertIn("Status:** completed_parallel_content_authoring", program)
        self.assertIn("Current:** CEW-16", program)
        self.assertIn("CEW-16 — GM Environment Discovery, Encounter Ecology & Full Integration Handoff** — `completed_verified`", program)
        self.assertIn("can occur here", contract)
        self.assertIn("normally occurs here", contract)
        self.assertIn("application implementation remains deferred", contract.lower())
        self.assertIn("CEW program is complete", report)


if __name__ == "__main__":
    unittest.main()
