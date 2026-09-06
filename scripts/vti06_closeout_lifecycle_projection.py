from pathlib import Path

PROGRAM = Path("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")
TEST = Path("tests/control_plane/test_vti06_scene_map_token_mai_bridge_registration.py")

text = PROGRAM.read_text(encoding="utf-8")
text = text.replace(
    "**Status:** OWNER-APPROVED — VTI-01 THROUGH VTI-05 COMPLETED_VERIFIED; VTI-06 IN_PROGRESS / ACCEPTANCE-ONLY UNTIL MATCHING RED  ",
    "**Status:** OWNER-APPROVED — VTI-01 THROUGH VTI-06 COMPLETED_VERIFIED; VTI-07 SELECTED_NOT_STARTED  ",
)
old_current = "VTI-06 — Scene, Map, Token & MAI Bridge — is `in_progress` as `VTI-06-attempt-001` from exact current application main `e9ddbf9c763faca74689cb3776ad21501c341ba5` on `integration/vti-06-scene-map-token-mai-bridge`. Branch creation, bounded implementation authority and acceptance-package authority are open. Production scene/map/token/MAI bridge mutation remains locked until genuine matching self-hosted Linux/Windows RED is sealed."
new_current = "VTI-06 — Scene, Map, Token & MAI Bridge — is `completed_verified` and retired. Genuine matching acceptance RED was sealed from exact application head `bf00d1d17befb35560c3ee5c18899d25df209d83` in run `34058733989` with deterministic receipt `456ec49cfaf07080c948cfa8b0024330179433b88f7aabedbc220e486e49103d`. Final exact-head repository health, self-hosted Linux, self-hosted Windows and deterministic comparison all passed at `80cd22e0e28304c0a59aa5954d35d504b55c4ea0` in run `34059463389` with receipt `636c05c378b4c081ae51b3f8b5feb4f5e446471073f0ce0e6a6153c70c5754a1`. Application PR #435 was merged as `1e325045b2fc65d067a5e587f8cde78dcba9f766`. VTI-07 — Permissions, Hidden Information & GM Authority — is the strict successor and is `selected_not_started` from that exact application main with no branch, acceptance-package, implementation or production authority."
if old_current not in text:
    raise SystemExit("expected VTI-06 current-state paragraph not found")
text = text.replace(old_current, new_current)
old_tranches = "6. **VTI-06 — Scene, Map, Token & MAI Bridge** — **IN_PROGRESS — ACCEPTANCE-ONLY UNTIL MATCHING RED**.  \n   Translate existing canonical Multiversal Scene + MAI/ISE/SSA projections to provider-neutral maps, tokens, walls, doors, lighting, grid/elevation/notes and GM-only presentation where supported. Acceptance authority is open; production bridge mutation remains locked pending matching RED.\n\n7. **VTI-07 — Permissions, Hidden Information & GM Authority**  \n   Preserve ownership, consent, GM adjudication and hidden-information filtering across external clients; prevent hidden counts/content leakage."
new_tranches = "6. **VTI-06 — Scene, Map, Token & MAI Bridge** — **COMPLETED_VERIFIED**.  \n   Projects existing canonical Multiversal Scene, map-version, placement and MAI/ISE/SSA semantics to provider-neutral scene/map/token envelopes with deterministic normalization, explicit `present`/`redacted`/`unsupported` fidelity, native wall/door/grid semantics only, fail-closed hidden presentation, and preserved visibility, ownership, consent and GM authority. No provider-specific adapter, live external mutation, durable persistence or VTI-07 permission-engine behavior was introduced.\n\n7. **VTI-07 — Permissions, Hidden Information & GM Authority** — **SELECTED_NOT_STARTED**.  \n   Preserve ownership, consent, GM adjudication and hidden-information filtering across external clients; prevent hidden counts/content leakage. Selection alone grants no branch, acceptance-package, implementation or production authority."
if old_tranches not in text:
    raise SystemExit("expected VTI-06/VTI-07 tranche block not found")
text = text.replace(old_tranches, new_tranches)
start = text.index("## VTI-06 governed-start boundary")
end = text.index("## Invariants", start)
replacement = """## VTI-06 completed contract

VTI-06 established:
- provider-neutral `scene`, `map` and `token` projection envelopes while Multiversal remains canonical authority;
- direct reuse of canonical `SceneRecord`, `SceneMapVersion` and `ScenePlacementRecord` semantics rather than parallel spatial models;
- wall and door projection only from native semantic dungeon primitives, and grid presentation only from canonical coordinate/calibration state;
- lighting and elevation as unsupported unless an owning native Multiversal semantic source exists;
- MAI/ISE/SSA asset/version references and semantic-construction roles as derivative presentation inputs without transferring asset or spatial authority;
- deterministic source, placement, primitive and related-asset normalization;
- explicit `present`, `redacted` and `unsupported` fidelity with redacted/unsupported values removed rather than inferred or manufactured;
- fail-closed hidden-information and GM-only presentation while preserving ownership, consent, visibility-policy and GM-authority metadata;
- explicit proof that provider-specific schemas, credentials/accounts, adapters, live external/canonical mutation, durable VTI persistence, new migration, provider activation, tester distribution, release/deployment and VTI-07+ implementation were not introduced.

Sealed completion evidence:
- acceptance RED head `bf00d1d17befb35560c3ee5c18899d25df209d83`, run `34058733989`, repository-health job `101555305842`, Linux job `101555324339`, Windows job `101555324315`, comparator job `101555372459`, receipt `456ec49cfaf07080c948cfa8b0024330179433b88f7aabedbc220e486e49103d`;
- final GREEN head `80cd22e0e28304c0a59aa5954d35d504b55c4ea0`, run `34059463389`, repository-health job `101557264698`, Linux job `101557279052`, Windows job `101557279039`, comparator job `101557349207`, receipt `636c05c378b4c081ae51b3f8b5feb4f5e446471073f0ce0e6a6153c70c5754a1`;
- application PR #435 merge `1e325045b2fc65d067a5e587f8cde78dcba9f766`;
- historical profile fanout `0`, application-feature repair cycles `0`, and one final validation-contract wording repair on changed evidence only.

## VTI-07 selection boundary

VTI-07 — Permissions, Hidden Information & GM Authority — is `selected_not_started` as `VTI-07-attempt-001` from exact application main `1e325045b2fc65d067a5e587f8cde78dcba9f766`. Selection records strict order only. No VTI-07 application branch, acceptance package, permission behavior, production mutation or permission-engine implementation is authorized until a separate governed start validates and merges.

A future governed start may bound provider-neutral preservation of canonical Multiversal ownership, consent, visibility, hidden-information and GM-authority decisions across derivative external-VTT clients. External VTTs may not become authoritative for permissions, adjudication or hidden state. Hidden counts/content, redacted identities and GM-only material remain fail-closed with no inference channel. Provider-specific schemas, credentials/accounts, adapter implementation, live external/canonical mutation, durable persistence/new migration, provider activation, tester distribution, release/deployment, VTI-08+ and SGC-01+ remain unauthorized.

"""
text = text[:start] + replacement + text[end:]
text = text.replace(
    "- VTI-01 through VTI-05 are frozen completed_verified with implementation authority retired.",
    "- VTI-01 through VTI-06 are frozen completed_verified with implementation authority retired.",
)
old_invariants = "- VTI-06 is in_progress on its registered branch with acceptance-package authority; production scene/map/token/MAI bridge mutation remains locked pending genuine matching RED.\n- VTI-06 must reuse existing native spatial, Scene, map, placement, visibility and MAI/ISE/SSA semantic authorities rather than duplicate them.\n- VTI-07+ and SGC-01+ remain unauthorized until their own governed selections and starts."
new_invariants = "- VTI-06 completed by reusing existing native spatial, Scene, map, placement, visibility and MAI/ISE/SSA semantic authorities rather than duplicating them.\n- VTI-07 is selected_not_started from exact application main `1e325045b2fc65d067a5e587f8cde78dcba9f766`; selection grants no branch, acceptance-package, implementation or production authority.\n- VTI-08+ and SGC-01+ remain unauthorized until their own governed selections and starts."
if old_invariants not in text:
    raise SystemExit("expected VTI-06 invariant block not found")
text = text.replace(old_invariants, new_invariants)
PROGRAM.write_text(text, encoding="utf-8")

TEST.write_text('''import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Vti06SceneMapTokenMaiBridgeRegistrationTests(unittest.TestCase):
    def test_vti06_completed_lifecycle_and_vti07_successor_are_consistent(self):
        merge = "1e325045b2fc65d067a5e587f8cde78dcba9f766"
        red_head = "bf00d1d17befb35560c3ee5c18899d25df209d83"
        red_receipt = "456ec49cfaf07080c948cfa8b0024330179433b88f7aabedbc220e486e49103d"
        green_head = "80cd22e0e28304c0a59aa5954d35d504b55c4ea0"
        green_receipt = "636c05c378b4c081ae51b3f8b5feb4f5e446471073f0ce0e6a6153c70c5754a1"
        checkpoint = load_json("governance/ai/work-state/VTI-06-attempt-001.json")
        successor = load_json("governance/ai/work-state/VTI-07-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md")

        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertEqual(checkpoint["application_pr"], 435)
        self.assertEqual(checkpoint["application_merge_sha"], merge)
        self.assertTrue(checkpoint["authority_retired"])
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertFalse(checkpoint["branch_creation_authorized"])
        self.assertFalse(checkpoint["acceptance_package_authorized"])
        self.assertFalse(checkpoint["production_mutation_authorized"])
        self.assertTrue(checkpoint["completed"])

        red = checkpoint["validation"]["acceptance_red"]
        green = checkpoint["validation"]["final_green"]
        self.assertEqual(red["head_sha"], red_head)
        self.assertEqual(red["run_id"], 34058733989)
        self.assertEqual(red["deterministic_receipt_sha256"], red_receipt)
        self.assertTrue(red["matching_red_observed"])
        self.assertEqual(green["head_sha"], green_head)
        self.assertEqual(green["run_id"], 34059463389)
        self.assertEqual(green["repository_health_job"], 101557264698)
        self.assertEqual(green["linux_job"], 101557279052)
        self.assertEqual(green["windows_job"], 101557279039)
        self.assertEqual(green["deterministic_compare_job"], 101557349207)
        self.assertEqual(green["deterministic_receipt_sha256"], green_receipt)
        self.assertEqual(green["historical_profile_fanout"], 0)

        vti06 = next(item for item in backlog["tranches"] if item["id"] == "VTI-06")
        self.assertEqual(vti06["status"], "completed_verified")
        self.assertEqual(vti06["application_merge_sha"], merge)
        self.assertFalse(vti06["implementation_authority"])

        authority = registry["vti_06_authority"]
        self.assertTrue(authority["retired"])
        self.assertFalse(authority["implementation_authority"])
        self.assertEqual(authority["application_merge_sha"], merge)
        self.assertTrue(authority["matching_red_observed"])
        self.assertEqual(authority["validated_head"], green_head)
        self.assertEqual(authority["validation_run"], 34059463389)
        self.assertEqual(authority["deterministic_receipt_sha256"], green_receipt)
        for key in ("branch_creation_authorized", "acceptance_package_authorized", "production_mutation_authorized", "scene_map_token_mai_bridge_authorized"):
            self.assertFalse(authority[key])

        self.assertEqual(successor["status"], "selected_not_started")
        self.assertEqual(successor["application_baseline_sha"], merge)
        self.assertIsNone(successor["implementation_branch"])
        self.assertFalse(successor["implementation_authority"])
        self.assertFalse(successor["branch_creation_authorized"])
        self.assertFalse(successor["acceptance_package_authorized"])
        self.assertFalse(successor["production_mutation_authorized"])

        successor_authority = registry["vti_07_authority"]
        self.assertTrue(successor_authority["selected_not_started"])
        self.assertFalse(successor_authority["retired"])
        self.assertFalse(successor_authority["implementation_authority"])
        self.assertEqual(successor_authority["application_baseline_sha"], merge)
        self.assertIsNone(successor_authority["implementation_branch"])
        self.assertFalse(successor_authority["branch_creation_authorized"])
        self.assertFalse(successor_authority["acceptance_package_authorized"])
        self.assertFalse(successor_authority["production_mutation_authorized"])
        self.assertFalse(successor_authority["permissions_hidden_information_gm_authority_authorized"])

        self.assertEqual(backlog["completed_through"], "VTI-06")
        self.assertEqual(backlog["current_item"], "VTI-07")
        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-07")
        self.assertEqual(pointer["active_attempt"]["status"], "selected_not_started")
        self.assertEqual(index["current"]["work_item_id"], "VTI-07")
        self.assertEqual(index["current"]["status"], "selected_not_started")
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-07")
        self.assertEqual(runtime["active_work"]["state"], "selected_not_started")
        self.assertEqual(runtime["application_repository"]["canonical_main"], merge)

        for phrase in ("VTI-06 — Scene, Map, Token & MAI Bridge", "COMPLETED_VERIFIED", "VTI-07 — Permissions, Hidden Information & GM Authority", "SELECTED_NOT_STARTED", "Platform selection remains evidence-driven"):
            self.assertIn(phrase, program)

    def test_vti06_completed_scope_preserves_native_authority_boundaries(self):
        checkpoint = load_json("governance/ai/work-state/VTI-06-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        contract = checkpoint["completed_contract"]
        for item in (
            "provider-neutral projection of canonical Scene, map-version and placement semantics into external scene/map/token presentation envelopes",
            "provider-neutral projection of walls, doors, lighting, grid or gridless geometry, elevation, notes and GM-only material only where native canonical semantics and target capability support them",
            "MAI/ISE/SSA asset-reference and semantic-construction-role bridging without making the external VTT an asset, spatial or rules authority",
            "deterministic normalization plus visibility, ownership, consent, hidden-information filtering and GM-authority preservation across scene/map/token projection",
        ):
            self.assertIn(item, scope["authorized"])
        for item in (
            "new canonical spatial, scene, map, token, wall, door, lighting, grid, elevation or asset semantics that duplicate or replace existing native authorities",
            "provider-specific schemas, vendor selection/ranking or VTI-09 platform commitment",
            "credentials, external account mutation, adapter implementation, live external synchronization mutation or canonical game-state mutation",
            "durable VTI persistence or a new migration before separately authorized persistence work",
            "VTI-07 permissions-engine behavior or any VTI-07+ implementation",
        ):
            self.assertIn(item, scope["not_authorized"])
        self.assertTrue(contract["native_scene_record_reused"])
        self.assertTrue(contract["native_scene_map_version_reused"])
        self.assertTrue(contract["native_scene_placement_record_reused"])
        self.assertTrue(contract["native_wall_and_door_semantics_only"])
        self.assertTrue(contract["native_grid_calibration_only"])
        self.assertTrue(contract["lighting_and_elevation_require_native_semantics"])
        self.assertTrue(contract["hidden_safe_presentation"])
        self.assertFalse(contract["provider_specific_integration_performed"])
        self.assertFalse(contract["durable_persistence_added"])
        self.assertFalse(contract["vti07_plus_implemented"])


if __name__ == "__main__":
    unittest.main()
''', encoding="utf-8")
