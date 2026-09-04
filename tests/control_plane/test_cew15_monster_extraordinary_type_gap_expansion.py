import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / 'governance/application-planning/creature-ecology-wildlife'


def load(name):
    return json.loads((CEW / name).read_text(encoding='utf-8'))


class Cew15MonsterExtraordinaryTypeGapExpansionTests(unittest.TestCase):
    def test_cew15_monster_extraordinary_type_gap_expansion_contract(self):
        model = load('CEW-15_EXTRAORDINARY_TYPE_GAP_MODEL_v1.0.0.json')
        expansion = load('CEW-15_MONSTER_EXTRAORDINARY_EXPANSION_v1.0.0.json')
        backlog = load('CEW_PROGRAM_BACKLOG.json')
        contract = (CEW / 'CEW-15_MONSTER_EXTRAORDINARY_CREATURE_TYPE_CONTRACT.md').read_text(encoding='utf-8')
        report = (CEW / 'CEW-15_COMPLETION_REPORT.md').read_text(encoding='utf-8')

        self.assertEqual(model['contract_id'], 'CEW-MON-EXTRA-1.0')
        self.assertEqual(model['extraordinary_source_corpus']['document_count'], 19)
        self.assertEqual(model['extraordinary_source_corpus']['safe_statblock_record_count'], 741)
        self.assertEqual(len(model['extraordinary_source_corpus']['documents']), 19)

        gaps = {row['gap_id']: row for row in model['type_gap_resolutions']}
        self.assertEqual(gaps['CEW08-GAP-001']['subject'], 'Beast')
        self.assertEqual(gaps['CEW08-GAP-001']['resolution_state'], 'resolved_bounded_source_usage_contract')
        self.assertFalse(gaps['CEW08-GAP-001']['animal_equivalence_created'])
        self.assertEqual(gaps['CEW08-GAP-002']['subject'], 'Illusion')
        self.assertEqual(gaps['CEW08-GAP-002']['resolution_state'], 'resolved_explicit_source_type_usage')
        self.assertEqual(gaps['CEW08-GAP-002']['explicit_type_usage_count'], 4)
        self.assertEqual(gaps['CEW08-GAP-003']['subject'], 'Dragon')
        self.assertEqual(gaps['CEW08-GAP-003']['resolution_state'], 'resolved_category_and_family_specific_stage_contract')
        self.assertEqual(gaps['CEW08-GAP-003']['category_count'], 5)
        self.assertFalse(gaps['CEW08-GAP-003']['universal_stage_ladder_created'])
        self.assertEqual(gaps['CEW08-GAP-004']['resolution_state'], 'preserved_unknown_requires_explicit_binding_authority')
        self.assertEqual(gaps['CEW08-GAP-004']['unknown_stable_id_type_binding_count'], 27)

        self.assertEqual(model['extraordinary_environment_handoff']['preset_count'], 3)
        self.assertEqual({x['preset_name'] for x in model['extraordinary_environment_handoff']['presets']}, {
            'Volcano', 'Post-Apocalyptic Radioactive Zone', 'Ashland'
        })
        self.assertEqual(expansion['profile_count'], 6)
        self.assertEqual(len(expansion['profiles']), 6)
        self.assertEqual({p['environment_context'] for p in expansion['profiles']}, {
            'Volcano', 'Post-Apocalyptic Radioactive Zone', 'Ashland'
        })
        self.assertTrue(all(p['canonical_definition_binding'] is None for p in expansion['profiles']))
        self.assertTrue(all(p['canonical_distribution_binding'] is None for p in expansion['profiles']))
        self.assertTrue(all(p['statblock_authored'] is False for p in expansion['profiles']))
        self.assertTrue(all(p['personhood_state'] == 'unknown' for p in expansion['profiles']))

        self.assertFalse(model['policy']['species_or_monster_quota_authorized'])
        self.assertFalse(model['policy']['name_or_mechanics_identity_binding_authorized'])
        self.assertFalse(model['policy']['environment_fit_creates_distribution'])
        self.assertFalse(model['policy']['canonical_creature_definition_creation_authorized'])
        self.assertFalse(model['policy']['application_runtime_mutation_authorized'])
        self.assertFalse(expansion['policy']['environment_selection_creates_encounter_placement'])

        strict_order = backlog['strict_order']
        states = {x['id']: x['status'] for x in backlog['tranches']}
        self.assertEqual(states['CEW-15'], 'completed_verified')
        self.assertGreaterEqual(strict_order.index(backlog['completed_through']), strict_order.index('CEW-15'))
        self.assertEqual(backlog['current_item'], 'CEW-16')
        self.assertIn(backlog['current_item_state'], {'selected_not_started', 'completed_verified'})
        if backlog['current_item_state'] == 'selected_not_started':
            self.assertEqual(backlog['completed_through'], 'CEW-15')
            self.assertEqual(states['CEW-16'], 'selected_not_started')
        else:
            self.assertEqual(backlog['completed_through'], 'CEW-16')
            self.assertEqual(states['CEW-16'], 'completed_verified')
        self.assertEqual(backlog['cew15_decisions']['contract_id'], 'CEW-MON-EXTRA-1.0')
        self.assertEqual(backlog['cew15_decisions']['canonical_type_bindings_created'], 0)
        self.assertEqual(backlog['cew15_decisions']['canonical_creature_definitions_created'], 0)
        self.assertFalse(backlog['cew15_decisions']['application_runtime_mutation_authorized'])

        for phrase in (
            'Beast does not become synonymous with Animal',
            'Illusion is source-supported as a Type value',
            'no universal dragon stage ladder',
            'canonical stable-ID type bindings remain unknown',
            'environment suitability does not create canonical distribution',
            'CEW-16',
        ):
            self.assertTrue(phrase in contract or phrase in report, phrase)


if __name__ == '__main__':
    unittest.main()
