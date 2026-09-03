#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/species-reconciliation"
AUTH = BASE / "CORE_26_SPECIES_AUTHORITY_v0.1.0.json"
AUDIT = BASE / "CORE_26_DOWNSTREAM_AUDIT_v0.1.0.json"


def req(cond, msg):
    if not cond:
        raise SystemExit(f"CORE26 invariant failure: {msg}")


a = json.loads(AUTH.read_text(encoding="utf-8"))
d = json.loads(AUDIT.read_text(encoding="utf-8"))

legacy = a["legacy_25"]["species"]
current = a["current_core_26"]["species"]
req(a["legacy_25"]["count"] == 25 and len(legacy) == 25 and len(set(legacy)) == 25, "legacy 25 roster")
req(a["current_core_26"]["count"] == 26 and len(current) == 26 and len(set(current)) == 26, "current 26 roster")
for name in ["Ratman", "Giantkin", "Mythragara", "Suula", "ManyToms", "Akwi", "Morganthyr"]:
    req(name in current, f"{name} missing from Core 26")
req("Nekron" in legacy and "Nekron" not in current and "Nekrons" not in current, "legacy/current Morganthyr migration")
mig = next((x for x in a["identity_migrations"] if x.get("current") == "Morganthyr"), None)
req(mig and set(mig["legacy"]) == {"Nekron", "Nekrons"} and mig["singular_if_needed"] == "Morganth", "Morganthyr migration contract")
req(a["akwi"]["current_status"] == "core_playable_species" and a["akwi"]["stable_id"] == "species.akwi" and a["akwi"]["governed_integration"] == "AKWI-01", "Akwi authority")
rat = a["ratman"]
names = [x["name"] for x in rat["lineages"]]
req(rat["lineage_count"] == 9 and len(names) == 9 and len(set(names)) == 9, "Ratman lineage count")
req(names == ["Rattori", "Nybra", "Rattakar", "Ratborn", "Chitta", "Taipanua", "Ska", "Muridian", "Raughtt"], "Ratman lineage order/content")
raughtt = next(x for x in rat["lineages"] if x["name"] == "Raughtt")
req(raughtt.get("established_facts") == ["proper", "aristocratic", "Dominix"], "Raughtt bounded facts")
req(any("sealed PPIA-05" in x for x in a["preservation_rules"]), "historical preservation rule")
req(d["status"] == "reconciled", "downstream audit state")
immutable = {x["path"] for x in d["legacy_completion_artifacts"] if x["disposition"].startswith("preserve")}
for path in [
    "governance/application-planning/parallel-preimplementation/PPIA-05_COMPLETION_REPORT.md",
    "governance/application-planning/parallel-preimplementation/PPIA-06_COMPLETION_REPORT.md",
    "governance/application-planning/character-appearance-production/CAPP-01_COMPLETION_REPORT.md",
]:
    req(path in immutable and (ROOT / path).exists(), f"historical artifact missing: {path}")
p6 = (ROOT / "governance/application-planning/parallel-preimplementation/PPIA-06_COMPLETION_REPORT.md").read_text(encoding="utf-8")
req("All 25 governed Species are explicit" in p6, "PPIA-06 historical evidence unexpectedly rewritten")
capp = (ROOT / "governance/application-planning/character-appearance-production/CAPP-01_COMPLETION_REPORT.md").read_text(encoding="utf-8")
req("25-Species Appearance Choice Registry" in capp, "CAPP-01 historical evidence unexpectedly rewritten")
print("CORE26 validation PASS: legacy=25 current=26 ratman_lineages=9 akwi=core morganthyr=current historical_evidence=preserved")
