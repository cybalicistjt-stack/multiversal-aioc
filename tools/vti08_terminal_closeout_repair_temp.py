import json
import textwrap
from pathlib import Path

root = Path('.')
registry_path = root / 'governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json'
original_registry = json.loads(registry_path.read_text(encoding='utf-8'))
original_history = list(original_registry['recently_completed_implementation_work'])

helper = (root / '.github/workflows/vti08-terminal-closeout-projection.yml').read_text(encoding='utf-8')
start_marker = "          python3 - <<'PY'\n"
end_marker = "\n          PY\n"
body = helper.split(start_marker, 1)[1].split(end_marker, 1)[0]
code = textwrap.dedent(body)
exec(compile(code, 'vti08-terminal-closeout-projection.py', 'exec'), {})

projected_registry = json.loads(registry_path.read_text(encoding='utf-8'))
vti08_completion = projected_registry['recently_completed_implementation_work'][0]
projected_registry['recently_completed_implementation_work'] = [vti08_completion] + [
    row for row in original_history if row.get('work_item_id') != 'VTI-08'
]
registry_path.write_text(json.dumps(projected_registry, separators=(',', ':')) + '\n', encoding='utf-8')

path = root / 'tests/control_plane/test_vti06_scene_map_token_mai_bridge_registration.py'
source = path.read_text(encoding='utf-8')
old = '''        if successor["status"] == "completed_verified":
            self.assertEqual(backlog["completed_through"], "VTI-07")
            self.assertEqual(backlog["current_item"], "VTI-08")
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-08")
            self.assertEqual(index["current"]["work_item_id"], "VTI-08")
            self.assertEqual(runtime["active_work"]["work_item"], "VTI-08")
            self.assertEqual(runtime["application_repository"]["canonical_main"], successor["application_merge_sha"])
        else:
'''
new = '''        if successor["status"] == "completed_verified":
            vti08 = load_json("governance/ai/work-state/VTI-08-attempt-001.json")
            if vti08["status"] == "completed_verified":
                self.assertEqual(backlog["completed_through"], "VTI-08")
                self.assertEqual(backlog["current_item"], "VTI-09")
                self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-09")
                self.assertEqual(index["current"]["work_item_id"], "VTI-09")
                self.assertEqual(runtime["active_work"]["work_item"], "VTI-09")
                self.assertEqual(runtime["application_repository"]["canonical_main"], vti08["application_merge_sha"])
            else:
                self.assertEqual(backlog["completed_through"], "VTI-07")
                self.assertEqual(backlog["current_item"], "VTI-08")
                self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-08")
                self.assertEqual(index["current"]["work_item_id"], "VTI-08")
                self.assertEqual(runtime["active_work"]["work_item"], "VTI-08")
                self.assertEqual(runtime["application_repository"]["canonical_main"], successor["application_merge_sha"])
        else:
'''
if old not in source:
    raise SystemExit('VTI-06 lifecycle replacement marker missing')
path.write_text(source.replace(old, new), encoding='utf-8')

path = root / 'tests/control_plane/test_vti07_red_unlock.py'
source = path.read_text(encoding='utf-8')
old = '''            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-08")
            self.assertEqual(index["current"]["work_item_id"], "VTI-08")
            self.assertEqual(runtime["active_work"]["work_item"], "VTI-08")
            self.assertEqual(backlog["active_contract"]["work_item"], "VTI-08")
            if successor["status"] in {"in_progress", "ready_for_review"} and successor["validation"]["acceptance_red"] is not None:
                self.assertTrue(pointer["bounded_authority"]["production_mutation_authorized"])
                self.assertTrue(index["current"]["production_mutation_authorized"])
                self.assertTrue(runtime["active_work"]["production_mutation_authorized"])
                self.assertTrue(backlog["active_contract"]["production_mutation_authorized"])
            else:
                self.assertFalse(pointer["bounded_authority"]["production_mutation_authorized"])
                self.assertFalse(index["current"]["production_mutation_authorized"])
                self.assertFalse(runtime["active_work"]["production_mutation_authorized"])
                self.assertFalse(backlog["active_contract"]["production_mutation_authorized"])
'''
new = '''            if successor["status"] == "completed_verified":
                self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-09")
                self.assertEqual(index["current"]["work_item_id"], "VTI-09")
                self.assertEqual(runtime["active_work"]["work_item"], "VTI-09")
                self.assertEqual(backlog["active_contract"]["work_item"], "VTI-09")
                self.assertFalse(pointer["bounded_authority"]["production_mutation_authorized"])
                self.assertFalse(index["current"]["production_mutation_authorized"])
                self.assertFalse(runtime["active_work"]["production_mutation_authorized"])
                self.assertFalse(backlog["active_contract"]["production_mutation_authorized"])
            else:
                self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-08")
                self.assertEqual(index["current"]["work_item_id"], "VTI-08")
                self.assertEqual(runtime["active_work"]["work_item"], "VTI-08")
                self.assertEqual(backlog["active_contract"]["work_item"], "VTI-08")
                if successor["status"] in {"in_progress", "ready_for_review"} and successor["validation"]["acceptance_red"] is not None:
                    self.assertTrue(pointer["bounded_authority"]["production_mutation_authorized"])
                    self.assertTrue(index["current"]["production_mutation_authorized"])
                    self.assertTrue(runtime["active_work"]["production_mutation_authorized"])
                    self.assertTrue(backlog["active_contract"]["production_mutation_authorized"])
                else:
                    self.assertFalse(pointer["bounded_authority"]["production_mutation_authorized"])
                    self.assertFalse(index["current"]["production_mutation_authorized"])
                    self.assertFalse(runtime["active_work"]["production_mutation_authorized"])
                    self.assertFalse(backlog["active_contract"]["production_mutation_authorized"])
'''
if old not in source:
    raise SystemExit('VTI-07 RED lifecycle replacement marker missing')
path.write_text(source.replace(old, new), encoding='utf-8')

path = root / 'tests/control_plane/test_vti07_terminal_closeout.py'
source = path.read_text(encoding='utf-8')
old = '''        self.assertEqual(backlog["completed_through"],"VTI-07")
        if nxt["status"] != "completed_verified":
            self.assertEqual(backlog["current_item"],"VTI-08")
            self.assertEqual(pointer["active_attempt"]["work_item_id"],"VTI-08")
            self.assertEqual(index["current"]["work_item_id"],"VTI-08")
            self.assertEqual(runtime["active_work"]["work_item"],"VTI-08")
        else:
            self.assertIn(pointer["active_attempt"]["work_item_id"],{"VTI-08","VTI-09"})
'''
new = '''        if nxt["status"] != "completed_verified":
            self.assertEqual(backlog["completed_through"],"VTI-07")
            self.assertEqual(backlog["current_item"],"VTI-08")
            self.assertEqual(pointer["active_attempt"]["work_item_id"],"VTI-08")
            self.assertEqual(index["current"]["work_item_id"],"VTI-08")
            self.assertEqual(runtime["active_work"]["work_item"],"VTI-08")
        else:
            self.assertEqual(backlog["completed_through"],"VTI-08")
            self.assertEqual(backlog["current_item"],"VTI-09")
            self.assertEqual(pointer["active_attempt"]["work_item_id"],"VTI-09")
            self.assertEqual(index["current"]["work_item_id"],"VTI-09")
            self.assertEqual(runtime["active_work"]["work_item"],"VTI-09")
'''
if old not in source:
    raise SystemExit('VTI-07 terminal lifecycle replacement marker missing')
path.write_text(source.replace(old, new), encoding='utf-8')
