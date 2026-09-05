import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ts = "2026-09-05T18:08:05-05:00"
red_head = "5ff92aaebc311933a3fa814b22badcb8ee694f76"
red_run = 33997794873
red_receipt = "d234d207d409056383670a853e29d6d2748ea5bc59db3892f3c7d9a0133bff7b"
linux_job = 101391267473
windows_job = 101391267534
selector_job = 101391250792
compare_job = 101391325205
branch = "integration/vti-05-character-sheet-item-compendium-projection"

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def save(path, data):
    (ROOT / path).write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")

acceptance_red = {
    "head_sha": red_head,
    "run_id": red_run,
    "repository_health_job": selector_job,
    "linux_job": linux_job,
    "windows_job": windows_job,
    "deterministic_compare_job": compare_job,
    "deterministic_receipt_sha256": red_receipt,
    "matching_red_observed": True,
    "linux_failure_step": "vti05-invariants",
    "windows_failure_step": "vti05-invariants",
    "expected_failure": "VTI-05 production contract intentionally absent",
    "historical_profile_fanout": 0,
}

p = "governance/ai/work-state/VTI-05-attempt-001.json"
d = load(p)
d["schema_version"] = "0.3.0"
d["production_mutation_authorized"] = True
d["validation"]["acceptance_red"] = acceptance_red
d["next_action"] = "Validate and merge the exact VTI-05 RED-unlock AIOC head, then implement only packages/contracts/src/virtual-tabletop-interoperability/character-sheet-item-compendium-projection-contract.ts on application PR #420 and prove exact-head repository health, Linux GREEN, Windows GREEN and deterministic comparison before merge."
save(p, d)

p = "governance/ai/runtime/CURRENT_WORK_POINTER.json"
d = load(p)
d["schema_version"] = "15.79.0"
d["updated_at"] = ts
b = d["bounded_authority"]
b.update(production_mutation_authorized=True, matching_red_observed=True, matching_red_head=red_head, matching_red_run=red_run, matching_red_receipt_sha256=red_receipt)
b["vti_scope"] = "VTI-05 matching RED sealed: bounded provider-neutral Character/NPC/creature sheet, equipment/power/condition item and RuleReference/roll-table/vehicle compendium production contract is authorized. Provider-specific schemas, credentials/accounts, adapters, live external/canonical mutation, persistence/migration and VTI-06+ scope remain closed."
d["selection_invariants"] = [
    "ALP-01 through ALP-08 and VTI-01 through VTI-04 remain completed_verified and frozen with implementation authority retired.",
    f"VTI-05 is in_progress on {branch}; genuine matching acceptance RED is sealed from application head {red_head} / run {red_run} with deterministic receipt {red_receipt}.",
    "Only the bounded provider-neutral VTI-05 production projection contract is unlocked; Multiversal remains canonical rules/campaign authority.",
    "VTI-05 may implement Character, NPC, creature, equipment, power, condition, RuleReference, roll-table and vehicle projection with explicit present/redacted/unsupported fidelity.",
    "Visibility, ownership, consent, hidden-information filtering and GM authority remain preserved constraints.",
    "Platform selection remains evidence-driven and deferred to VTI-09; no vendor is selected or ranked.",
    "No provider-specific schema, credential use, external account mutation, adapter implementation, live external/canonical mutation, durable VTI persistence, new migration, provider activation, tester distribution, release or deployment is authorized.",
    "VTI-06+ and SGC-01+ remain unauthorized.",
]
d["exact_next_action"] = "Validate and merge exact VTI-05 RED-unlock AIOC head, then implement only packages/contracts/src/virtual-tabletop-interoperability/character-sheet-item-compendium-projection-contract.ts on application PR #420 and prove exact-head repository health, Linux GREEN, Windows GREEN and deterministic comparison before merge."
save(p, d)

p = "governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json"
d = load(p)
d["schema_version"] = "0.15.0"
d["active_contract"].update(production_mutation_authorized=True, matching_red_observed=True, matching_red_head=red_head, matching_red_run=red_run, matching_red_receipt_sha256=red_receipt)
d["active_contract"]["rule"] = "VTI-05 genuine matching RED is sealed. Only the bounded provider-neutral character-sheet/item/compendium production contract is unlocked; provider-specific/live mutation/persistence/VTI-06+ scope remains closed."
save(p, d)

p = "governance/ai/runtime/ROADMAP_INDEX.json"
d = load(p)
d["schema_version"] = "15.47.0"
d["updated_at"] = ts
d["current"].update(production_mutation_authorized=True, matching_red_observed=True, matching_red_head=red_head, matching_red_run=red_run, matching_red_receipt_sha256=red_receipt)
d["rule"] = "DPL, MAI, AAI, ISE, SSA, WCI, KFR, ODL, SCL, MAL, ECI, ALP-01 through ALP-08 and VTI-01 through VTI-04 are completed_verified. VTI-05 is in_progress with genuine matching RED sealed and only its bounded provider-neutral production projection contract unlocked."
save(p, d)

p = "governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json"
d = load(p)
d["schema_version"] = "12.60.0"
d["updated_at"] = ts
d["canonical_selector"]["rule"] = "This is the only current-work selector. ALP-01 through ALP-08 and VTI-01 through VTI-04 are completed_verified and retired; VTI-05 is in_progress with matching RED sealed and bounded production-contract authority open."
d["application_repository"]["active_validation_family_state"] = "VTI01_VTI02_VTI03_VTI04_completed_VTI05_in_progress_matching_red_production_contract_only"
d["active_work"].update(role="bounded_production_contract_authority", production_mutation_authorized=True, matching_red_observed=True, matching_red_head=red_head, matching_red_run=red_run, matching_red_receipt_sha256=red_receipt, execution_rule="Implement only the bounded VTI-05 provider-neutral projection contract on the registered application branch, then prove exact-head Linux/Windows/comparator GREEN before merge.")
d["boundaries"] = [
    "ALP-01 through ALP-08 and VTI-01 through VTI-04 remain completed_verified with retired implementation authority.",
    f"VTI-05 is in_progress on {branch}; matching RED is sealed from {red_head} / run {red_run} and bounded production-contract authority is open.",
    "Multiversal remains canonical rules/campaign authority; external VTTs are derivative presentation clients only.",
    "VTI-05 may implement provider-neutral Character, NPC, creature, equipment, power, condition, RuleReference, roll-table and vehicle projection with explicit present/redacted/unsupported fidelity.",
    "Visibility, ownership, consent, hidden-information filtering and GM-authority constraints remain preserved.",
    "No provider-specific schema, credential use, external account mutation, adapter implementation, live external/canonical mutation, durable VTI persistence, new migration, provider activation, tester distribution, release or deployment is authorized.",
    "VTI-06+ and SGC-01+ remain unauthorized.",
]
save(p, d)

p = "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json"
d = load(p)
d["schema_version"] = "15.65.0"
d["updated_at"] = ts
d["active_planning_work"]["implementation_scope"] = "VTI-05 matching RED sealed: only the bounded provider-neutral Character/NPC/creature sheet, equipment/power/condition item and RuleReference/roll-table/vehicle compendium production contract is authorized. Provider-specific schemas, credentials/accounts, adapters, live external/canonical mutation, persistence/migration and VTI-06+ remain unauthorized."
d["rule"] = "Only registered CURRENT or CURRENT_COMPATIBLE surfaces may govern. ALP-01 through ALP-08 and VTI-01 through VTI-04 are completed_verified and retired; VTI-05 is in_progress with matching RED sealed and bounded production-contract authority open."
a = d["vti_05_authority"]
a.update(production_mutation_authorized=True, character_sheet_projection_authorized=True, item_projection_authorized=True, compendium_projection_authorized=True, matching_red_observed=True, matching_red_head=red_head, matching_red_run=red_run, matching_red_receipt_sha256=red_receipt)
save(p, d)

p = ROOT / "tests/control_plane/test_vti05_character_sheet_item_compendium_projection_registration.py"
s = p.read_text(encoding="utf-8")
s = s.replace('self.assertFalse(checkpoint["production_mutation_authorized"])\n        self.assertIsNone(checkpoint["validation"]["acceptance_red"])', 'self.assertTrue(checkpoint["production_mutation_authorized"])\n        red = checkpoint["validation"]["acceptance_red"]\n        self.assertEqual(red["head_sha"], "' + red_head + '")\n        self.assertEqual(red["run_id"], ' + str(red_run) + ')\n        self.assertEqual(red["deterministic_receipt_sha256"], "' + red_receipt + '")\n        self.assertTrue(red["matching_red_observed"])')
s = s.replace('self.assertFalse(backlog["active_contract"]["production_mutation_authorized"])', 'self.assertTrue(backlog["active_contract"]["production_mutation_authorized"])')
s = s.replace('self.assertFalse(pointer["bounded_authority"]["production_mutation_authorized"])', 'self.assertTrue(pointer["bounded_authority"]["production_mutation_authorized"])')
s = s.replace('self.assertFalse(authority["production_mutation_authorized"])\n        for key in ("character_sheet_projection_authorized","item_projection_authorized","compendium_projection_authorized"):\n            self.assertFalse(authority[key])', 'self.assertTrue(authority["production_mutation_authorized"])\n        self.assertTrue(authority["matching_red_observed"])\n        for key in ("character_sheet_projection_authorized","item_projection_authorized","compendium_projection_authorized"):\n            self.assertTrue(authority[key])')
s = s.replace('self.assertFalse(index["current"]["production_mutation_authorized"])', 'self.assertTrue(index["current"]["production_mutation_authorized"])')
s = s.replace('self.assertFalse(runtime["active_work"]["production_mutation_authorized"])', 'self.assertTrue(runtime["active_work"]["production_mutation_authorized"])')
p.write_text(s, encoding="utf-8")

p = ROOT / "tests/control_plane/test_vti04_rules_action_roll_bridge_registration.py"
s = p.read_text(encoding="utf-8")
s = s.replace('self.assertFalse(successor["production_mutation_authorized"])\n\n        self.assertEqual(pointer', 'self.assertEqual(successor["production_mutation_authorized"], successor["validation"]["acceptance_red"] is not None)\n\n        self.assertEqual(pointer')
s = s.replace('self.assertFalse(vti05_authority["production_mutation_authorized"])', 'self.assertEqual(vti05_authority["production_mutation_authorized"], successor["validation"]["acceptance_red"] is not None)')
p.write_text(s, encoding="utf-8")
