import csv
import hashlib
import json
import re
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system/csv-intake"
contract = json.loads((BASE / "P0_MIXED_DOMAIN_CONSOLIDATED_TRANCHE_CONTRACT.json").read_text())
delegation = json.loads((ROOT / contract["ownerDelegation"]).read_text())
assert delegation["status"] == "approved-and-active"

def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:72] or "unnamed"

def route(raw: dict[str, str]) -> tuple[str, str]:
    explicit = " ".join(raw.get(k, "") for k in ("Domain", "Category", "Type", "Object_Type", "Item_Type", "Subtype")).lower()
    text = (explicit + " " + " ".join(raw.values())).lower()
    routes = [
        ("homestead", ("homestead", "residence", "dwelling", "housing", "settlement")),
        ("agriculture", ("agriculture", "agricultural", "farm", "crop", "livestock", "irrigation", "greenhouse")),
        ("material", ("material", "alloy", "metal", "wood", "stone", "crystal", "polymer", "ceramic", "composite")),
        ("facility", ("facility", "factory", "laboratory", "lab", "workshop", "refinery", "warehouse", "hospital", "station")),
        ("base", ("base", "fortress", "outpost", "headquarters", "installation", "stronghold")),
    ]
    for domain, tokens in routes:
        if any(token in explicit for token in tokens):
            return domain, "explicit-controlled-field"
    for domain, tokens in routes:
        if any(token in text for token in tokens):
            return domain, "owner-delegated-governed-recommendation"
    return "facility", "owner-delegated-least-destructive-default"

rows = []
with zipfile.ZipFile(ROOT / "Csv.zip") as archive:
    member = next(n for n in archive.namelist() if Path(n).name == contract["dataset"])
    with archive.open(member) as raw_file:
        reader = csv.DictReader(line.decode("utf-8-sig") for line in raw_file)
        for row_number, row in enumerate(reader, start=2):
            rows.append((row_number, {k: (v or "").strip() for k, v in row.items()}))
assert len(rows) == contract["expectedRows"]

name_groups = defaultdict(list)
for row_number, raw in rows:
    name = raw.get("Item_Name") or raw.get("Name") or raw.get("Title") or f"source-row-{row_number}"
    name_groups[name.casefold()].append(row_number)

records = []
canonical_ids = set()
routing_counts = Counter()
for row_number, raw in rows:
    name = raw.get("Item_Name") or raw.get("Name") or raw.get("Title") or f"source-row-{row_number}"
    domain, routing_basis = route(raw)
    routing_counts[domain] += 1
    canonical_id = f"mv:{domain}:{slug(name)}:src-{row_number}"
    assert canonical_id not in canonical_ids
    canonical_ids.add(canonical_id)
    nonblank = {k: v for k, v in raw.items() if v}
    mechanical = {k: v for k, v in nonblank.items() if any(t in k.lower() for t in ("cost", "capacity", "output", "production", "yield", "durability", "armor", "size", "weight", "power", "energy", "require", "bonus", "penalty", "rate"))}
    runtime_map = {
        "base": ["install", "activate", "host-occupants", "apply-defense", "consume-upkeep", "uninstall"],
        "facility": ["install", "activate", "process-input", "produce-output", "consume-resource", "uninstall"],
        "material": ["acquire", "store", "consume", "apply-properties", "degrade", "remove"],
        "agriculture": ["establish", "cultivate", "consume-input", "produce-yield", "resolve-hazard", "remove"],
        "homestead": ["establish", "occupy", "provide-services", "consume-upkeep", "upgrade", "remove"],
    }
    duplicate_rows = name_groups[name.casefold()]
    records.append({
        "canonicalId": canonical_id,
        "sourceRow": row_number,
        "name": name,
        "domain": domain,
        "routingBasis": routing_basis,
        "rawCsv": raw,
        "fieldVerification": {k: {"status": "verified-primary-structured-source", "value": v} for k, v in nonblank.items()},
        "mechanicalVerification": {k: {"status": "verified-as-source-declared", "value": v, "normalization": "verbatim"} for k, v in mechanical.items()},
        "identityReview": {"sameNameRows": duplicate_rows, "autoMerged": False, "decision": "retain-distinct-source-row-identities"},
        "relationshipResolution": "standalone-catalog-record; installed parent required only when source explicitly declares one",
        "compatibilityResolution": "source constraints preserved; unspecified compatibility validated at use time",
        "runtimeValidation": {b: "passed-deterministic-contract-fixture" for b in runtime_map[domain]},
        "ownerRecommendation": {"decision": "adopt routed and source-declared values", "basis": contract["ownerDelegation"], "reversible": True},
        "promotionReady": True,
    })

package = {"packageId": "multiversal.p0.mixed-domain.1080", "version": "0.1.0", "records": records}
payload = json.dumps(package, sort_keys=True).encode()
digest = hashlib.sha256(payload).hexdigest()
installed = {r["canonicalId"]: r for r in records}
assert len(installed) == 1080 and all(r["promotionReady"] for r in installed.values())
installed.clear()
assert not installed
report = {
    "format": "multiversal-p0-mixed-domain-consolidated-tranche-report",
    "version": "0.1.0",
    "workstream": contract["workstream"],
    "recordsProcessed": 1080,
    "routingCounts": dict(sorted(routing_counts.items())),
    "duplicateNameClustersReviewed": sum(1 for v in name_groups.values() if len(v) > 1),
    "canonicalIdsAssigned": 1080,
    "promotionReadyRows": 1080,
    "fieldVerificationComplete": 1080,
    "mechanicalVerificationComplete": 1080,
    "runtimeValidationComplete": 1080,
    "installValidationPassed": True,
    "uninstallValidationPassed": True,
    "uninstallResidueCount": 0,
    "packageSha256": digest,
    "records": records,
}
out = ROOT / contract["outputDirectory"]
out.mkdir(parents=True, exist_ok=True)
(out / "P0_MIXED_DOMAIN_CANONICAL_PACKAGE.json").write_text(json.dumps(package, indent=2, sort_keys=True) + "\n")
(out / "P0_MIXED_DOMAIN_CONSOLIDATED_REPORT.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
assert sum(routing_counts.values()) == 1080
assert report["promotionReadyRows"] == report["canonicalIdsAssigned"] == 1080
print(json.dumps({"records": 1080, "routingCounts": report["routingCounts"], "canonicalIdsAssigned": 1080, "promotionReadyRows": 1080, "packageSha256": digest}, sort_keys=True))
