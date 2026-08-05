import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system"
registry = json.loads((BASE / "vehicle-templates/MECHA_TEMPLATE_REGISTRY.json").read_text())
fixtures = json.loads((BASE / "csv-intake/P0_MECHA_REPRESENTATIVE_FIXTURES.json").read_text())
coverage = json.loads((BASE / "csv-intake/P0_MECHA_VERIFICATION_CONSOLIDATION.json").read_text())
delegation = json.loads((BASE / "csv-intake/OWNER_RECOMMENDATION_DELEGATION.json").read_text())

assert registry["format"] == "multiversal-mecha-template-registry"
assert registry["workstream"] == "8E-009L46"
assert {t["templateId"] for t in registry["templates"]} == {"vehicle.mecha.frame", "vehicle.mecha.component"}
for template in registry["templates"]:
    assert template["requiredFields"]
    assert template["runtimeBehaviors"]
    assert template["validationRules"]

assert delegation["status"] == "approved-and-active"
assert coverage["rows"] == fixtures["coveredRows"] == 107
assert len(fixtures["fixtures"]) == 3
rows = []
for fixture in fixtures["fixtures"]:
    rows.extend(fixture["sourceRows"])
    assert fixture["templateId"] in {"vehicle.mecha.frame", "vehicle.mecha.component"}
    assert fixture["identityState"] == "staging-only"
    assert fixture["canonicalId"] is None
    assert fixture["promotionReady"] is False
assert len(rows) == len(set(rows)) == 107
assert set(rows) == set(range(2, 22)) | set(range(52, 139))
assert registry["canonicalIdsAssigned"] == fixtures["canonicalIdsAssigned"] == 0
assert registry["promotionReadyRows"] == fixtures["promotionReadyRows"] == 0

out = ROOT / "build/csv-p0-mecha-template-representatives-l46"
out.mkdir(parents=True, exist_ok=True)
(out / "MECHA_TEMPLATE_REGISTRY.json").write_text(json.dumps(registry, indent=2) + "\n")
(out / "P0_MECHA_REPRESENTATIVE_FIXTURES.json").write_text(json.dumps(fixtures, indent=2) + "\n")
print(json.dumps({"templates": 2, "fixtures": 3, "coveredRows": 107, "canonicalIdsAssigned": 0, "promotionReadyRows": 0}, sort_keys=True))
