import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "governance/object-system/csv-intake/OWNER_RECOMMENDATION_DELEGATION.json"
record = json.loads(path.read_text())

assert record["format"] == "multiversal-owner-recommendation-delegation"
assert record["workstream"] == "8E-009L44"
assert record["authority"]["role"] == "project owner and final decision authority"
assert record["scope"]["ownerReviewNotRequired"] is True
assert record["status"] == "approved-and-active"
assert len(record["decisionRules"]) >= 8
assert all(record["requiredRecord"].values())
assert any("Never fabricate" in rule for rule in record["decisionRules"])
assert any("canonical identity" in rule for rule in record["decisionRules"])
print(json.dumps({"validated": True, "status": record["status"], "decisionRules": len(record["decisionRules"])}, sort_keys=True))
