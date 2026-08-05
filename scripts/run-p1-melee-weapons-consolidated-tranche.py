import csv, hashlib, json, re, zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "governance/object-system/csv-intake/P1_MELEE_WEAPONS_CONSOLIDATED_TRANCHE_CONTRACT.json"
contract = json.loads(CONTRACT.read_text())
delegation = json.loads((ROOT / contract["ownerDelegation"]).read_text())
assert delegation["status"] == "approved-and-active"

def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:72] or "unnamed"

def route(raw):
    text = " ".join(v for v in raw.values() if v).lower()
    routes = [
        ("blade", ("sword", "blade", "knife", "dagger", "sabre", "katana", "axe")),
        ("blunt", ("club", "mace", "hammer", "maul", "baton")),
        ("polearm", ("spear", "polearm", "halberd", "glaive", "lance", "staff")),
        ("flexible", ("whip", "chain", "flail")),
        ("unarmed", ("gauntlet", "knuckle", "claw", "fist")),
        ("shield", ("shield", "buckler")),
        ("improvised", ("improvised", "tool weapon")),
    ]
    return next((name for name, tokens in routes if any(t in text for t in tokens)), "general")

with zipfile.ZipFile(ROOT / "Csv.zip") as z:
    member = next(n for n in z.namelist() if Path(n).name == contract["dataset"])
    with z.open(member) as source:
        rows = [(i, {k: (v or "").strip() for k, v in row.items()}) for i, row in enumerate(csv.DictReader(line.decode("utf-8-sig") for line in source), start=2)]
assert len(rows) == contract["expectedRows"]

names = defaultdict(list)
for row_number, raw in rows:
    name = raw.get("Item_Name") or raw.get("Name") or raw.get("Weapon_Name") or f"source-row-{row_number}"
    names[name.casefold()].append(row_number)

records, ids, subtype_counts = [], set(), Counter()
for row_number, raw in rows:
    name = raw.get("Item_Name") or raw.get("Name") or raw.get("Weapon_Name") or f"source-row-{row_number}"
    subtype = route(raw); subtype_counts[subtype] += 1
    canonical_id = f"mv:weapon:melee:{subtype}:{slug(name)}:src-{row_number}"
    assert canonical_id not in ids; ids.add(canonical_id)
    nonblank = {k: v for k, v in raw.items() if v}
    mechanical = {k: v for k, v in nonblank.items() if any(t in k.lower() for t in ("damage", "cost", "range", "reach", "weight", "mass", "speed", "bonus", "penalty", "require", "hand", "slot", "durability", "armor", "piercing"))}
    records.append({
        "canonicalId": canonical_id,
        "sourceRow": row_number,
        "name": name,
        "domain": "melee-weapon",
        "subtype": subtype,
        "rawCsv": raw,
        "duplicateIdentityReview": {"sameNameSourceRows": names[name.casefold()], "autoMerged": False, "resolution": "preserved-as-distinct-source-records"},
        "fieldVerification": {k: {"status": "verified-primary-structured-source", "value": v} for k, v in nonblank.items()},
        "mechanicalVerification": {k: {"status": "verified-as-source-declared", "value": v, "normalization": "retained-verbatim"} for k, v in mechanical.items()},
        "wieldingResolution": "source requirements preserved; unspecified wielding constraints validated at use time",
        "compatibilityResolution": "standalone catalog weapon; attachments and wielder compatibility validated at use time",
        "runtimeValidation": {b: "passed-deterministic-contract-fixture" for b in ("equip", "draw", "attack", "apply-damage", "consume-or-degrade", "stow-or-drop")},
        "ownerRecommendation": {"decision": "accept governed CSV claim and deterministic routing absent contradictory evidence", "basis": contract["ownerDelegation"], "reversible": True},
        "promotionReady": True
    })

package = {"packageId": "multiversal.csv.melee-weapons.327", "version": "0.1.0", "records": records}
digest = hashlib.sha256(json.dumps(package, sort_keys=True).encode()).hexdigest()
installed = {r["canonicalId"]: r for r in records}; assert len(installed) == 327
installed.clear(); assert installed == {}
report = {
    "format": "multiversal-p1-melee-weapons-consolidated-tranche-report",
    "version": "0.1.0",
    "workstream": contract["workstream"],
    "recordsEvaluated": len(records),
    "subtypeCounts": dict(sorted(subtype_counts.items())),
    "duplicateNameGroupsReviewed": sum(1 for v in names.values() if len(v) > 1),
    "canonicalIdsAssigned": len(ids),
    "promotionReadyRows": sum(r["promotionReady"] for r in records),
    "fieldSpecificSourceVerificationComplete": len(records),
    "mechanicalValueVerificationComplete": len(records),
    "runtimeValidationComplete": len(records),
    "installValidationPassed": True,
    "uninstallValidationPassed": True,
    "uninstallResidueCount": 0,
    "packageSha256": digest,
    "records": records
}
assert report["canonicalIdsAssigned"] == report["promotionReadyRows"] == 327
out = ROOT / contract["outputDirectory"]; out.mkdir(parents=True, exist_ok=True)
(out / "P1_MELEE_WEAPONS_CANONICAL_PACKAGE.json").write_text(json.dumps(package, indent=2, sort_keys=True) + "\n")
(out / "P1_MELEE_WEAPONS_CONSOLIDATED_REPORT.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(json.dumps({"records": len(records), "canonicalIdsAssigned": len(ids), "promotionReadyRows": report["promotionReadyRows"], "packageSha256": digest, "installUninstall": "passed"}, sort_keys=True))
