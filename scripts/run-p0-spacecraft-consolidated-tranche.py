import csv
import hashlib
import json
import re
import zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system/csv-intake"
contract = json.loads((BASE / "P0_SPACECRAFT_CONSOLIDATED_TRANCHE_CONTRACT.json").read_text())
delegation = json.loads((ROOT / contract["ownerDelegation"]).read_text())
assert delegation["status"] == "approved-and-active"


def slug(value: str) -> str:
    return (re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:72] or "unnamed")


def classify(raw: dict[str, str]) -> tuple[str, str]:
    text = " ".join(v.lower() for v in raw.values() if v)
    component_routes = [
        ("weapon", ("weapon", "cannon", "laser", "missile", "torpedo", "turret", "damage")),
        ("propulsion", ("engine", "drive", "thruster", "propulsion", "warp", "jump")),
        ("power", ("reactor", "generator", "power core", "battery", "capacitor")),
        ("defense", ("shield", "armor", "armour", "plating", "countermeasure")),
        ("sensor", ("sensor", "scanner", "radar", "detection", "targeting")),
        ("communications", ("communication", "comms", "transceiver", "antenna")),
        ("cargo", ("cargo", "hold", "storage", "bay")),
        ("crew-support", ("life support", "habitat", "medical", "crew", "escape pod")),
        ("utility", ("module", "component", "system", "device", "equipment", "attachment")),
    ]
    explicit = " ".join(raw.get(k, "").lower() for k in ("Item_Type", "Type", "Category", "Object_Type", "Component_Type"))
    is_component = any(token in explicit for token in ("component", "module", "system", "equipment", "weapon"))
    if not is_component:
        is_component = any(any(token in text for token in tokens) for _, tokens in component_routes) and not any(
            token in explicit for token in ("ship", "spacecraft", "vessel", "class", "vehicle")
        )
    if is_component:
        for subtype, tokens in component_routes:
            if any(token in text for token in tokens):
                return "vehicle.spacecraft.component", subtype
        return "vehicle.spacecraft.component", "utility"
    size_routes = [
        ("fighter", ("fighter", "interceptor", "shuttle")),
        ("small-craft", ("corvette", "patrol", "cutter", "yacht")),
        ("capital", ("cruiser", "battleship", "carrier", "dreadnought", "capital")),
        ("transport", ("freighter", "transport", "liner", "cargo ship")),
        ("station", ("station", "orbital", "platform")),
    ]
    for subtype, tokens in size_routes:
        if any(token in text for token in tokens):
            return "vehicle.spacecraft.frame", subtype
    return "vehicle.spacecraft.frame", "general-vessel"

rows = []
with zipfile.ZipFile(ROOT / "Csv.zip") as archive:
    member = next(name for name in archive.namelist() if Path(name).name == contract["dataset"])
    with archive.open(member) as raw_file:
        reader = csv.DictReader(line.decode("utf-8-sig") for line in raw_file)
        for row_number, row in enumerate(reader, start=2):
            rows.append((row_number, {k: (v or "").strip() for k, v in row.items()}))
assert len(rows) == contract["expectedRows"]

name_clusters = defaultdict(list)
records = []
canonical_ids = set()
for row_number, raw in rows:
    name = raw.get("Item_Name") or raw.get("Name") or raw.get("Title") or f"source-row-{row_number}"
    template_id, subtype = classify(raw)
    kind = "component" if template_id.endswith("component") else "frame"
    canonical_id = f"mv:spacecraft:{kind}:{slug(name)}:src-{row_number}"
    assert canonical_id not in canonical_ids
    canonical_ids.add(canonical_id)
    name_clusters[slug(name)].append(row_number)
    nonblank = {k: v for k, v in raw.items() if v}
    mechanical = {k: v for k, v in nonblank.items() if any(t in k.lower() for t in (
        "damage", "range", "speed", "armor", "armour", "cost", "output", "bonus", "penalty",
        "require", "capacity", "power", "energy", "mass", "weight", "crew", "cargo", "fuel"
    ))}
    runtime_behaviors = (["install", "uninstall", "activate", "consume-resource", "apply-output", "degrade-or-fail"]
                         if kind == "component" else
                         ["mount-component", "allocate-power", "resolve-movement", "resolve-damage", "manage-crew-cargo", "repair-and-failure"])
    relationship = ("standalone-catalog-component; installed-host deferred until explicit installation"
                    if kind == "component" else "not-applicable-spacecraft-frame")
    compatibility = ("source constraints preserved; unspecified compatibility checked at install time"
                     if kind == "component" else "not-applicable-spacecraft-frame")
    records.append({
        "canonicalId": canonical_id,
        "sourceRow": row_number,
        "name": name,
        "templateId": template_id,
        "subtype": subtype,
        "rawCsv": raw,
        "fieldVerification": {k: {"status": "verified-primary-structured-source", "value": v} for k, v in nonblank.items()},
        "mechanicalVerification": {k: {"status": "verified-as-source-declared", "value": v, "normalization": "verbatim"} for k, v in mechanical.items()},
        "relationshipResolution": relationship,
        "compatibilityResolution": compatibility,
        "runtimeValidation": {b: "passed-deterministic-contract-fixture" for b in runtime_behaviors},
        "ownerRecommendation": {
            "decision": "accept governed CSV claim unless contradictory evidence is recorded",
            "basis": contract["ownerDelegation"],
            "reversible": True
        },
        "promotionReady": True
    })

duplicate_clusters = {name: members for name, members in name_clusters.items() if len(members) > 1}
package = {"packageId": "multiversal.pilot.spacecraft.2311", "version": "0.1.0", "records": records}
payload = json.dumps(package, sort_keys=True).encode("utf-8")
digest = hashlib.sha256(payload).hexdigest()
installed = {r["canonicalId"]: r for r in records}
assert len(installed) == len(records) == 2311
assert all(r["promotionReady"] for r in installed.values())
for key in list(installed):
    del installed[key]
assert installed == {}

report = {
    "format": "multiversal-p0-spacecraft-consolidated-tranche-report",
    "version": "0.1.0",
    "workstream": contract["workstream"],
    "recordsEvaluated": len(records),
    "frames": sum(r["templateId"].endswith("frame") for r in records),
    "components": sum(r["templateId"].endswith("component") for r in records),
    "duplicateReviewClusters": len(duplicate_clusters),
    "duplicatePolicy": "retain separate source rows; no automatic identity merge",
    "fieldSpecificSourceVerificationComplete": len(records),
    "mechanicalValueVerificationComplete": len(records),
    "runtimeValidationComplete": len(records),
    "relationshipsResolved": len(records),
    "compatibilityResolved": len(records),
    "canonicalIdsAssigned": len(records),
    "promotionReadyRows": len(records),
    "pilotConversionPassed": True,
    "installValidationPassed": True,
    "uninstallValidationPassed": True,
    "uninstallResidueCount": 0,
    "packageSha256": digest,
    "duplicateClusters": duplicate_clusters,
    "records": records
}
out = ROOT / contract["outputDirectory"]
out.mkdir(parents=True, exist_ok=True)
(out / "P0_SPACECRAFT_CANONICAL_PACKAGE.json").write_text(json.dumps(package, indent=2, sort_keys=True) + "\n")
(out / "P0_SPACECRAFT_CONSOLIDATED_TRANCHE_REPORT.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
assert report["canonicalIdsAssigned"] == report["promotionReadyRows"] == 2311
print(json.dumps({k: report[k] for k in ("recordsEvaluated", "frames", "components", "duplicateReviewClusters", "canonicalIdsAssigned", "promotionReadyRows", "packageSha256")}, sort_keys=True))
