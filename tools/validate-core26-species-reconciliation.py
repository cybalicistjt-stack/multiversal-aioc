#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/species-reconciliation"
AUTH = BASE / "CORE_26_SPECIES_AUTHORITY_v0.1.0.json"
AUDIT = BASE / "CORE_26_DOWNSTREAM_AUDIT_v0.1.0.json"
CURRENT_AUTH = BASE / "CORE_26_SPECIES_AUTHORITY_v1.0.0.json"
STANDARD = ROOT / "governance/application-planning/player-species/CORE_26_GAME_READY_STANDARD_v1.0.0.json"
BASELINE = ROOT / "governance/application-planning/player-species/CORE_26_PRODUCTION_BASELINE_v0.1.0.json"
CURRENT = ROOT / "operations/CURRENT.json"


def req(cond, msg):
    if not cond:
        raise SystemExit(f"CORE26 invariant failure: {msg}")


a = json.loads(AUTH.read_text(encoding="utf-8"))
d = json.loads(AUDIT.read_text(encoding="utf-8"))
ca = json.loads(CURRENT_AUTH.read_text(encoding="utf-8"))
std = json.loads(STANDARD.read_text(encoding="utf-8"))
base = json.loads(BASELINE.read_text(encoding="utf-8"))
cur = json.loads(CURRENT.read_text(encoding="utf-8"))

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
expected = ["Human","Elf","Dwarf","Goblin","Orc","Giantkin","Stygian","Sharr","Gray","The Free","Ratman","Furashin","Rog","Rohai","Moravi","Vespin","Rakuuta","Traiga","Kola-Ha","Toba-Madra","Arborae","Mythragara","Suula","Morganthyr","ManyToms","Akwi"]
req(ca["authority_id"] == "CORE26-CURRENT-01" and ca["status"] == "CURRENT_CANON", "current authority identity")
req(ca["current_core_26"]["species"] == expected and ca["current_core_26"]["count"] == 26, "current authority exact Core 26")
req("Nekron" not in ca["current_core_26"]["species"] and ca["identity_migrations"]["Nekron"]["current"] == "Morganthyr", "current Morganthyr identity")
req(ca["akwi"]["status"] == "core_playable_species", "current Akwi core status")
req(len(ca["ratman"]["subordinate_lineages"]) == 9, "current Ratman subordinate lineages")
pointer = cur.get("domain_authorities", {}).get("player_species", {})
req(pointer.get("path") == "governance/application-planning/species-reconciliation/CORE_26_SPECIES_AUTHORITY_v1.0.0.json", "CURRENT player-species authority pointer")
req(pointer.get("authority_id") == "CORE26-CURRENT-01" and pointer.get("roster_count") == 26, "CURRENT player-species authority metadata")
req(std["standard_id"] == "CORE26.GAME_READY.v1" and std["applies_to"] == expected, "equal game-ready standard roster")
req(len(std["dimensions"]) >= 19, "game-ready standard dimension count")
req([x["name"] for x in base["species"]] == expected and len(base["species"]) == 26, "production baseline exact roster")
req(all(x["standard_id"] == "CORE26.GAME_READY.v1" and x["overall_status"] != "game_ready_certified" for x in base["species"]), "baseline must not overclaim certification")
by_name = {x["name"]: x for x in base["species"]}
req(by_name["Morganthyr"]["canonical_object_state"] == "legacy_nekron_object_requires_current_identity_migration", "Morganthyr baseline")
req(by_name["Rog"]["canonical_object_state"] == "missing_current_content_db_object", "Rog baseline")
req(by_name["Suula"]["canonical_object_state"] == "missing_current_content_db_object", "Suula baseline")
req(by_name["Akwi"]["canonical_object_state"] == "governed_supplemental_runtime_requires_catalog_convergence", "Akwi baseline")
print("CORE26 validation PASS: legacy=25 current=26 current_authority=CORE26-CURRENT-01 equal_standard=19+ baseline=26 historical_evidence=preserved")
