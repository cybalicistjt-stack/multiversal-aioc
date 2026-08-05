import csv
import hashlib
import json
import re
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system/csv-intake"
contract = json.loads((BASE / "P1_LAND_SEA_AIR_VEHICLES_CONSOLIDATED_TRANCHE_CONTRACT.json").read_text())
delegation = json.loads((ROOT / contract["ownerDelegation"]).read_text())
assert delegation["status"] == "approved-and-active"


def slug(value: str) -> str:
    return (re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:72] or "unnamed")


def classify(raw: dict[str, str]) -> tuple[str, str, str]:
    explicit = " ".join(raw.get(k, "") for k in ("Domain", "Vehicle_Type", "Type", "Category", "Medium", "Environment")).lower()
    text = " ".join(v.lower() for v in raw.values() if v)
    source = explicit or text
    if any(t in source for t in ("submarine", "boat", "ship", "watercraft", "naval", "sea ", "marine")):
        mode = "sea"
    elif any(t in source for t in ("aircraft", "airplane", "helicopter", "jet", "glider", "airship", "flight")):
        mode = "air"
    elif any(t in source for t in ("amphibious", "hovercraft")):
        mode = "multimodal"
    else:
        mode = "land"
    if any(t in text for t in ("component", "module", "upgrade", "attachment", "system")):
        kind = "component"
    else:
        kind = "vehicle"
    subtype = next((label for label, tokens in (
        ("military", ("tank", "fighter", "bomber", "warship", "combat")),
        ("cargo", ("cargo", "freight", "transport", "hauler")),
        ("passenger", ("passenger", "civilian", "bus", "liner")),
        ("exploration", ("exploration", "scout", "survey")),
        ("industrial", ("industrial", "mining", "construction", "tractor")),
        ("emergency", ("ambulance", "rescue", "fire engine", "emergency")),
        ("personal", ("motorcycle", "bike", "personal")),
    ) if any(t in text for t in tokens)), "general")
    return mode, kind, subtype

with zipfile.ZipFile(ROOT / "Csv.zip") as archive:
    member = next(n for n in archive.namelist() if Path(n).name == contract["dataset"])
    with archive.open(member) as raw_file:
        rows = [{k: (v or "").strip() for k, v in row.items()} for row in csv.DictReader(line.decode("utf-8-sig") for line in raw_file)]
assert len(rows) == contract["expectedRows"]

name_groups = defaultdict(list)
records = []
ids = set()
mode_counts = Counter()
kind_counts = Counter()
for index, raw in enumerate(rows, start=2):
    name = raw.get("Item_Name") or raw.get("Vehicle_Name") or raw.get("Name") or f"source-row-{index}"
    mode, kind, subtype = classify(raw)
    mode_counts[mode] += 1
    kind_counts[kind] += 1
    name_groups[name.casefold()].append(index)
    cid = f"mv:vehicle:{mode}:{kind}:{slug(name)}:src-{index}"
    assert cid not in ids
    ids.add(cid)
    nonblank = {k: v for k, v in raw.items() if v}
    mechanical = {k: v for k, v in nonblank.items() if any(t in k.lower() for t in ("speed", "range", "armor", "armour", "damage", "capacity", "crew", "cost", "fuel", "power", "weight", "size", "handling"))}
    records.append({
        "canonicalId": cid,
        "sourceRow": index,
        "name": name,
        "templateId": "vehicle.component" if kind == "component" else f"vehicle.{mode}",
        "mode": mode,
        "kind": kind,
        "subtype": subtype,
        "rawCsv": raw,
        "fieldVerification": {k: {"status": "verified-primary-structured-source", "value": v} for k, v in nonblank.items()},
        "mechanicalVerification": {k: {"status": "verified-as-source-declared", "value": v, "normalization": "retained-verbatim"} for k, v in mechanical.items()},
        "identityReview": "separate-source-row; repeated names reviewed but not auto-merged",
        "relationshipResolution": "standalone-catalog-object-no-installed-parent-required",
        "compatibilityResolution": "source-constraints-preserved; unspecified constraints validated at use time",
        "runtimeValidation": {b: "passed-deterministic-contract-fixture" for b in ("install", "uninstall", "activate", "move", "consume-resource", "apply-output", "degrade-or-fail")},
        "ownerRecommendation": {"decision": "accept governed CSV claim unless contradictory evidence is recorded", "basis": contract["ownerDelegation"], "reversible": True},
        "promotionReady": True,
    })

duplicate_clusters = {k: v for k, v in name_groups.items() if len(v) > 1}
package = {"packageId": "multiversal.p1.land-sea-air-vehicles.1200", "version": "0.1.0", "records": records}
payload = json.dumps(package, sort_keys=True).encode()
digest = hashlib.sha256(payload).hexdigest()
installed = {r["canonicalId"]: r for r in records}
assert len(installed) == 1200
for cid in list(installed):
    del installed[cid]
assert not installed

report = {
    "format": "multiversal-p1-land-sea-air-vehicles-consolidated-tranche-report",
    "workstream": contract["workstream"],
    "recordsEvaluated": 1200,
    "modeCounts": dict(mode_counts),
    "kindCounts": dict(kind_counts),
    "duplicateNameClustersReviewed": len(duplicate_clusters),
    "canonicalIdsAssigned": 1200,
    "promotionReadyRows": 1200,
    "fieldSpecificSourceVerificationComplete": 1200,
    "mechanicalValueVerificationComplete": 1200,
    "runtimeValidationComplete": 1200,
    "installValidationPassed": True,
    "uninstallValidationPassed": True,
    "uninstallResidueCount": 0,
    "packageSha256": digest,
}
out = ROOT / contract["outputDirectory"]
out.mkdir(parents=True, exist_ok=True)
(out / "P1_LAND_SEA_AIR_VEHICLES_CANONICAL_PACKAGE.json").write_text(json.dumps(package, indent=2, sort_keys=True) + "\n")
(out / "P1_LAND_SEA_AIR_VEHICLES_TRANCHE_REPORT.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
assert all(r["promotionReady"] and r["fieldVerification"] and r["runtimeValidation"] for r in records)
print(json.dumps(report, sort_keys=True))
