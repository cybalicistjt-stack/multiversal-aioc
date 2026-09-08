import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")

class AriSaaP3dRoadmapRegistrationTests(unittest.TestCase):
    def test_ari_is_registered_between_sgc_and_mib16(self):
        ari = load_json("governance/application-planning/asset-resource-ingestion-reuse/ARI_PROGRAM_BACKLOG.json")
        sgc = load_json("governance/application-planning/source-gameplay-coverage-closure/SGC_PROGRAM_BACKLOG.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        amendment = load_text("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_ARI_SAA_P3D_AMENDMENT_2026-09-07.md")
        mib_amendment = load_text("governance/application-planning/multiversal-implementation-backbone/MIB_ARI_INTERSTITIAL_INTEGRATION_AMENDMENT_2026-09-07.md")
        self.assertEqual(ari["program_id"], "ARI")
        self.assertEqual(ari["activation_after"], "SGC-08")
        self.assertEqual(ari["successor"], "MIB-16")
        self.assertFalse(ari["implementation_authority"])
        self.assertEqual(ari["tranche_execution_target_minutes"], 24)
        self.assertEqual(len(ari["strict_order"]), 22)
        self.assertEqual(sgc["successor"], "ARI-01")
        self.assertIn("SGC-01..08 → ARI-01..22 → MIB-16", index["effective_forward_order"])
        self.assertIn("SGC-01..08 → ARI-01..22 → MIB-16", amendment)
        self.assertIn("SGC-08 → ARI-01..22 → MIB-16", mib_amendment)
        names = {row["id"]: row["name"] for row in ari["tranches"]}
        self.assertEqual(names["ARI-08"], "Syrinscape Soundset XML Adapter")
        self.assertEqual(names["ARI-09"], "Map, Tileset & Variant-Family Recognition")
        self.assertEqual(names["ARI-15"], "Large-Library Query, Pagination & Lazy Retrieval")
        self.assertEqual(names["ARI-18"], "PAPT, CAPP & Native Asset Registration Bridge")
        self.assertEqual(names["ARI-22"], "Golden Bulk-Ingestion, Cross-System & Scale Proof")

    def test_saa_is_registered_between_smb09_and_smb10(self):
        saa = load_json("governance/application-planning/sequential-art-authoring/SAA_PROGRAM_BACKLOG.json")
        smb = load_text("governance/application-planning/system-maturation-buildout/SMB_SYSTEM_MATURATION_AND_BUILDOUT_PROGRAM.md")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        self.assertEqual(saa["program_id"], "SAA")
        self.assertEqual(saa["activation_after"], "SMB-09")
        self.assertEqual(saa["successor"], "SMB-10")
        self.assertFalse(saa["implementation_authority"])
        self.assertEqual(saa["tranche_execution_target_minutes"], 24)
        self.assertEqual(len(saa["strict_order"]), 20)
        self.assertIn("SMB-01..09 → SAA-01..20 → SMB-10", index["effective_forward_order"])
        self.assertIn("SMB-09 → SAA-01..20 → SMB-10", smb)
        self.assertIn("SAA-18 comic-project packaging/dependency contracts", smb)
        names = {row["id"]: row["name"] for row in saa["tranches"]}
        self.assertEqual(names["SAA-04"], "ARI Asset Palette & Capability Filtering")
        self.assertEqual(names["SAA-05"], "Character Actor Projection")
        self.assertEqual(names["SAA-07"], "Maps, Tilesets & Scene Background Projection")
        self.assertEqual(names["SAA-16"], "Optional Digital-Comic Audio Cue Lane")
        self.assertEqual(names["SAA-20"], "Integrated Desktop/Mobile Golden Comic Proof")

    def test_p3d_is_durable_but_deferred_and_noncritical(self):
        future = load_json("governance/application-planning/future-projects/DEFERRED_FUTURE_PROJECTS_REGISTRY.json")
        p3d = load_text("governance/application-planning/future-projects/P3D_PHYSICAL_3D_MINIATURE_PIPELINE.md")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        project = next(row for row in future["projects"] if row["program_id"] == "P3D")
        self.assertEqual(project["status"], "owner_approved_deferred_future")
        self.assertFalse(project["critical_path"])
        self.assertFalse(project["implementation_authority"])
        self.assertFalse(project["automatic_activation"])
        self.assertIn("physical-pixel-v1", project["future_renderers"])
        self.assertIn("physical-detailed-v1", project["future_renderers"])
        indexed = next(row for row in index["deferred_future_projects"] if row["program_id"] == "P3D")
        self.assertFalse(indexed["critical_path"])
        self.assertFalse(indexed["automatic_activation"])
        self.assertNotIn("P3D", index["effective_forward_order"])
        for phrase in ("renderer-neutral appearance snapshot","physical-pixel-v1","physical-detailed-v1","composable atomic parts plus parametric morphing","must not silently place P3D on the critical path"):
            self.assertIn(phrase, p3d)

    def test_papt_and_sgc_cross_system_routes_are_preserved(self):
        papt = load_text("governance/application-planning/pixel-asset-production-toolkit/PAPT_ARI_INTEGRATION_AMENDMENT_2026-09-07.md")
        sgc = load_text("governance/application-planning/source-gameplay-coverage-closure/SGC_SOURCE_GAMEPLAY_COVERAGE_CLOSURE_PROGRAM.md")
        amendment = load_text("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_ARI_SAA_P3D_AMENDMENT_2026-09-07.md")
        for phrase in ("PAPT remains the pixel production/generation/tooling authority","ARI becomes the reusable resource-library/ingestion/catalog/derivative authority","PAPT-03","PAPT-16"):
            self.assertIn(phrase, papt)
        self.assertIn("bulk resource-pack intake/universal asset reuse to ARI-01..22", sgc)
        self.assertIn("sequential-art/comic authoring", sgc)
        self.assertIn("renderer-neutral future miniature/physicalization requirements to deferred P3D", sgc)
        self.assertIn("No later roadmap edit may silently drop ARI, SAA or the P3D deferred-future record", amendment)

    def test_current_vti_selector_is_not_replaced_by_planning(self):
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        checkpoint = load_json("governance/ai/work-state/VTI-10-attempt-001.json")
        vti11 = load_json("governance/ai/work-state/VTI-11-attempt-001.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        self.assertIn(checkpoint["status"], {"in_progress", "completed_verified"})
        if checkpoint["status"] == "completed_verified":
            if vti11["status"] in {"selected_not_started", "in_progress"}:
                self.assertEqual(index["current"]["work_item_id"], "VTI-11")
                self.assertEqual(index["current"]["status"], vti11["status"])
                self.assertEqual(index["current"]["implementation_authority"], vti11["implementation_authority"])
                self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-11")
                self.assertEqual(pointer["active_attempt"]["status"], vti11["status"])
                self.assertEqual(backlog["current_item"], "VTI-11")
                self.assertEqual(runtime["active_work"]["work_item"], "VTI-11")
            else:
                self.assertEqual(vti11["status"], "completed_verified")
                self.assertEqual(index["current"]["work_item_id"], "VTI-12")
            self.assertTrue(authority["vti_10_authority"]["retired"])
            self.assertFalse(authority["vti_10_authority"]["production_mutation_authorized"])
        else:
            self.assertEqual(index["current"]["work_item_id"], "VTI-10")
            self.assertEqual(index["current"]["status"], "in_progress")
            self.assertTrue(index["current"]["implementation_authority"])
            red = checkpoint["validation"]["acceptance_red"]
            matching_red = bool(red and red.get("matching_red_observed"))
            expected_production = matching_red and checkpoint["production_mutation_authorized"]
            self.assertEqual(index["current"]["matching_red_observed"], matching_red)
            self.assertEqual(index["current"]["production_mutation_authorized"], expected_production)
            self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], expected_production)
            self.assertEqual(backlog["active_contract"]["production_mutation_authorized"], expected_production)
            self.assertEqual(runtime["active_work"]["production_mutation_authorized"], expected_production)
            self.assertEqual(authority["vti_10_authority"]["production_mutation_authorized"], expected_production)
        self.assertEqual(index["planned_programs"][0]["program_id"], "ARI")
        self.assertEqual(index["planned_programs"][1]["program_id"], "SAA")
        self.assertFalse(index["planned_programs"][0]["implementation_authority"])
        self.assertFalse(index["planned_programs"][1]["implementation_authority"])
        for project in index["deferred_future_projects"]:
            self.assertFalse(project["implementation_authority"])
            self.assertFalse(project["automatic_activation"])

if __name__ == "__main__":
    unittest.main()
