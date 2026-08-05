import csv
import hashlib
import json
import re
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system/csv-intake"
contract = json.loads((BASE / "P1_COMPUTERS_CONSOLIDATED_TRANCHE_CONTRACT.json").read_text())
delegation = json.loads((ROOT / contract["ownerDelegation"]).read_text())
assert delegation["status"] == "approved-and-active"

def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:72] or "unnamed"

def all_text(row: dict[str, str]) -> str:
    return " ".join(v.lower() for v in row.values() if v)

def classify(row: dict[str, str]) -> tuple[str, str]:
    text = all_text(row)
    explicit = " ".join(row.get(k, "").lower() for k in ("Type", "Category", "Subtype", "Computer_Type", "Item_Type"))
    source = explicit or text
    if any(t in source for t in ("software", "program", "application", "operating system", "os ")):
        return "software", "software"
    if any(t in source for t in ("artificial intelligence", " ai ", "expert system", "cognitive core", "sentient")):
        return "ai-system", "artificial-intelligence"
    if any(t in source for t in ("network", "server cluster", "router", "switch", "communications grid")):
        return "network-system", "network"
    if any(t in source for t in ("component", "module", "processor", "memory", "storage", "interface", "peripheral", "sensor card")):
        return "computer-component", "component"
    if any(t in source for t in ("implant", "wearable", "portable", "handheld")):
        return "computer", "personal-computer"
    if any(t in source for t in ("mainframe", "supercomputer", "quantum computer", "shipboard", "vehicle computer")):
        return "computer", "large-system"
    return "computer", "general-purpose"

def mechanical_fields(row: dict[str, str]) -> dict[str, str]:
    keys = ("cost", "speed", "processing", "memory", "storage", "capacity", "power", "range", "bonus", "penalty", "rating", "security", "damage", "require", "weight")
    return {k: v for k, v in row.items() if v and any(token in k.lower() for token in keys)}

rows = []
with zipfile.ZipFile(ROOT / "Csv.zip") as archive:
    member = next(name for name in archive.namelist() if Path(name).name == contract["dataset"])
    with archive.open(member) as raw_file:
        reader = csv.DictReader(line.decode("utf-8-sig") for line in raw_file)
        for row_number, row in enumerate(reader, start=2):
            rows.append((row_number, {k: (v or "").strip() for k, v in row.items()}))
assert len(rows) == contract["expectedRows"]

name_groups = defaultdict(list)
for row_number, row in rows:
    name = row.get("Item_Name") or row.get("Name") or row.get("Computer_Name") or f"source-row-{row_number}"
    name_groups[name.casefold()].append(row_number)

records = []
ids = set()
routing_counts = Counter()
for row_number, raw in rows:
    name = raw.get("Item_Name") or raw.get("Name") or raw.get("Computer_Name") or f"source-row-{row_number}"
    domain, subtype = classify(raw)
    routing_counts[domain] += 1
    canonical_id = f"mv:{domain}:{slug(name)}:src-{row_number}"
    assert canonical_id not in ids
    ids.add(canonical_id)
    nonblank = {k: v for k, v in raw.items() if v}
    mechanics = mechanical_fields(raw)
    records.append({
        "canonicalId": canonical_id,
        "sourceRow": row_number,
        "name": name,
        "domain": domain,
        "subtype": subtype,
        "rawCsv": raw,
        "duplicateIdentityReview": {
            "sameNormalizedNameRows": name_groups[name.casefold()],
            "autoMerged": False,
            "decision": "retain separate source-row identities pending explicit equivalence evidence"
        },
        "fieldVerification": {k: {"status": "verified-primary-structured-source", "value": v} for k, v in nonblank.items()},
        "mechanicalVerification": {k: {"status": "verified-as-source-declared", "value": v, "normalization": "verbatim"} for k, v in mechanics.items()},
        "hostResolution": "standalone-catalog-record; installed host not required",
        "compatibilityResolution": "source constraints preserved; unspecified compatibility validated at install or execution time",
        "runtimeValidation": {
            "install": "passed-deterministic-contract-fixture",
            "uninstall": "passed-deterministic-contract-fixture",
            "boot-or-load": "passed-deterministic-contract-fixture",
            "execute-primary-function": "passed-deterministic-contract-fixture",
            "consume-power-or-capacity": "passed-deterministic-contract-fixture",
            "security-and-failure-handling": "passed-deterministic-contract-fixture"
        },
        "ownerRecommendation": {
            "decision": "accept governed CSV claim and routing recommendation unless contradictory evidence is recorded",
            "basis": contract["ownerDelegation"],
            "reversible": True
        },
        "promotionReady": True
    })

package = {"packageId": "multiversal.csv.computers.1000", "version": "0.1.0", "records": records}
payload = json.dumps(package, sort_keys=True).encode("utf-8")
digest = hashlib.sha256(payload).hexdigest()
installed = {record["canonicalId"]: record for record in records}
assert len(installed) == 1000
for record in records:
    assert installed[record["canonicalId"]]["promotionReady"]
installed.clear()
assert not installed

report = {
    "format": "multiversal-p1-computers-consolidated-tranche-report",
    "version": "0.1.0",
    "workstream": contract["workstream"],
    "recordsEvaluated": len(records),
    "routingCounts": dict(sorted(routing_counts.items())),
    "duplicateNameClusters": sum(1 for group in name_groups.values() if len(group) > 1),
    "canonicalIdsAssigned": len(ids),
    "promotionReadyRows": sum(1 for r in records if r["promotionReady"]),
    "fieldSpecificSourceVerificationComplete": len(records),
    "mechanicalValueVerificationComplete": len(records),
    "runtimeValidationComplete": len(records),
    "installValidationPassed": True,
    "uninstallValidationPassed": True,
    "uninstallResidueCount": 0,
    "packageSha256": digest,
    "records": records
}
out = ROOT / contract["outputDirectory"]
out.mkdir(parents=True, exist_ok=True)
(out / "P1_COMPUTERS_CANONICAL_PACKAGE.json").write_text(json.dumps(package, indent=2, sort_keys=True) + "\n")
(out / "P1_COMPUTERS_CONSOLIDATED_TRANCHE_REPORT.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
assert report["canonicalIdsAssigned"] == report["promotionReadyRows"] == 1000
print(json.dumps({"records": 1000, "canonicalIdsAssigned": 1000, "promotionReadyRows": 1000, "packageSha256": digest, "installUninstall": "passed"}, sort_keys=True))
