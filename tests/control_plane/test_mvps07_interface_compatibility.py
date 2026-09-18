from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "governance/application-planning/player-species/contracts"
COMP = D / "MVPS-07_INTERFACE_COMPATIBILITY_CONTRACT.json"
RESULT = D / "MVPS-07_COMPATIBILITY_RESULT_CONTRACT.json"
FIX = D / "MVPS-07_COMPATIBILITY_FIXTURES.json"
INV = D / "MVPS-07_INVARIANTS.json"


class MVPS07CompatibilityTests(unittest.TestCase):
    def _j(self, p: Path) -> dict:
        return json.loads(p.read_text(encoding="utf-8"))

    def test_required_artifacts_exist(self):
        for p in (COMP, RESULT, FIX, INV):
            with self.subTest(path=p):
                self.assertTrue(p.is_file(), p)

    def test_common_interface_is_species_agnostic_and_not_size_only(self):
        c = self._j(COMP)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesInterfaceCompatibility")
        self.assertFalse(c["species_name_input_allowed"])
        self.assertFalse(c["size_only_compatibility_allowed"])
        self.assertTrue({"clothing","armor","weapon","tool","implant","suit","seat","vehicle_occupant","mount_rider"} <= set(c["interface_kinds"]))
        self.assertEqual(c["evaluation_policy"], "side_effect_free_policy_evaluation")
        self.assertFalse(c["authoritative_assignment_mutation_allowed"])

    def test_requirements_compose_structure_scale_capability_and_external_owner_refs(self):
        c = self._j(COMP)
        kinds = set(c["requirement_kinds"])
        self.assertTrue({"structural","scale_profile","capability","attachment","worn_region","manipulator","host_interface","relationship_authority"} <= kinds)
        req = set(c["requirement_contract"]["required"])
        self.assertTrue({"requirement_id","kind","predicate_ref","source_ref","owner_domain"} <= req)
        self.assertFalse(c["requirement_contract"]["inline_owner_mechanics_allowed"])
        self.assertFalse(c["mount_role_eligibility_inferred_from_fit"])
        self.assertFalse(c["vehicle_station_authority_inferred_from_fit"])

    def test_result_has_explicit_reason_and_unresolved_state(self):
        r = self._j(RESULT)
        self.assertEqual(set(r["statuses"]), {"compatible","compatible_with_adapter","incompatible","unresolved"})
        required = set(r["result_contract"]["required"])
        self.assertTrue({"status","reason","evidence_refs","matched_requirements","unmet_requirements","owner_route"} <= required)
        self.assertTrue(r["reason_required"])
        self.assertTrue(r["unresolved_when_required_fact_unknown"])
        self.assertFalse(r["automatic_adapter_synthesis_allowed"])

    def test_fixtures_cover_diverse_body_plans_and_explicit_rejection(self):
        f = self._j(FIX)
        cases = f["cases"]
        self.assertTrue({"humanoid_armor","centaur_like_trousers","radial_tool","nonhumanoid_vehicle_seat","mount_interface"} <= set(cases))
        self.assertEqual(cases["humanoid_armor"]["expected"]["status"], "compatible")
        self.assertEqual(cases["centaur_like_trousers"]["expected"]["status"], "incompatible")
        self.assertTrue(cases["centaur_like_trousers"]["expected"]["reason"])
        self.assertEqual(cases["radial_tool"]["expected"]["status"], "compatible")
        self.assertEqual(cases["nonhumanoid_vehicle_seat"]["expected"]["status"], "compatible_with_adapter")
        self.assertEqual(cases["mount_interface"]["expected"]["status"], "unresolved")
        for case in cases.values():
            self.assertNotIn("species_name", case)
            self.assertFalse(case["mutates_assignment"])
            self.assertFalse(case["mutates_ownership_or_relationship"])

    def test_invariants_preserve_owner_boundaries(self):
        i = self._j(INV)
        ids = {x["id"] for x in i["invariants"]}
        self.assertTrue({
            "MVPS07-I01-no-species-name-dispatch",
            "MVPS07-I02-no-size-only-fit",
            "MVPS07-I03-explicit-reason-for-rejection",
            "MVPS07-I04-unknown-remains-unresolved",
            "MVPS07-I05-adapters-are-explicit",
            "MVPS07-I06-compatibility-does-not-mutate-assignment",
            "MVPS07-I07-mount-fit-does-not-create-role-or-bond",
            "MVPS07-I08-vehicle-fit-does-not-create-station-authority"
        } <= ids)
        self.assertFalse(i["runtime_equipment_engine_created"])
        self.assertFalse(i["runtime_vehicle_or_mount_engine_created"])


if __name__ == "__main__":
    unittest.main()
