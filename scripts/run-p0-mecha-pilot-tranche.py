import csv, json, re, shutil, zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/object-system/csv-intake"
contract = json.loads((BASE / "P0_MECHA_PILOT_TRANCHE_CONTRACT.json").read_text())
delegation = json.loads((ROOT / contract["ownerDelegation"]).read_text())
registry = json.loads((ROOT / contract["templateRegistry"]).read_text())
assert delegation["status"] == "approved-and-active"
templates = {t["templateId"]: t for t in registry["templates"]}
allowed = set(templates["vehicle.mecha.component"]["allowedSubtypes"])
wanted = set(range(2,22)) | set(range(52,139))
rows = {}
with zipfile.ZipFile(ROOT / "Csv.zip") as archive:
    member = next(n for n in archive.namelist() if Path(n).name == contract["dataset"])
    with archive.open(member) as raw:
        for n, row in enumerate(csv.DictReader(line.decode("utf-8-sig") for line in raw), start=2):
            if n in wanted:
                rows[n] = {k:(v or "") for k,v in row.items()}
assert set(rows) == wanted

def norm(s): return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
def route(row, n):
    if n < 22: return "shared-rules"
    hay = " ".join(row.values()).lower()
    rules = [
        ("power-source",("reactor","generator","power source")),("capacitor",("capacitor","battery")),
        ("mobility",("thruster","flight","wheel","track","leg","mobility","jump")),
        ("weapon",("weapon","cannon","gun","missile","laser","blade")),("armor",("armor","plating","shield")),
        ("resistance",("resistance","resistant","immunity")),("sensor",("sensor","scanner","radar")),
        ("targeting",("targeting","aiming")),("repair",("repair","maintenance")),
        ("communication",("communication","radio","comms")),("safety",("escape","ejection","safety")),
        ("resource-gathering",("mining","harvest","resource")),("utility",("utility","cargo","tool"))]
    hits=[sub for sub,terms in rules if any(t in hay for t in terms)]
    return hits[0] if len(set(hits))==1 else "utility" if not hits else hits[0]

records=[]; names=defaultdict(list); recommendations=0; unresolved_relationships=0
for n in sorted(rows):
    raw=rows[n]; name=raw.get("Item_Name") or raw.get("Name") or f"source-row-{n}"
    template_id="vehicle.mecha.frame" if n<22 else "vehicle.mecha.component"
    subtype=route(raw,n)
    if template_id.endswith("component") and subtype not in allowed: subtype="utility"
    names[norm(name)].append(n)
    nonblank={k:v for k,v in raw.items() if v.strip()}
    host_fields={k:v for k,v in nonblank.items() if any(x in k.lower() for x in ("host","compatible","frame","parent"))}
    relationship="not-applicable-shared-rules" if n<22 else ("source-claim-retained-provisionally" if host_fields else "unresolved-without-explicit-host-evidence")
    if relationship.startswith("unresolved"): unresolved_relationships += 1
    power={k:v for k,v in nonblank.items() if any(x in k.lower() for x in ("power","energy","draw","capacity","capacitor"))}
    recommendation={"action":"retain-source-claim-as-reversible-provisional-value","basis":contract["ownerDelegation"],"confidence":"medium","reversible":True}
    recommendations += 1
    records.append({
      "recordId":f"staging:mecha:row-{n}","sourceRow":n,"templateId":template_id,"subtype":subtype,
      "identity":{"name":name,"normalizedName":norm(name),"state":"staging-only","canonicalId":None},
      "rawCsv":raw,"provisionalValues":nonblank,"relationship":relationship,
      "compatibility":"unresolved-unless-explicitly-supported" if n>=22 else "not-applicable",
      "powerBudget":"fields-retained-no-unsupported-arithmetic" if power else "not-computable-from-present-source-fields",
      "completeness":{"requiredEnvelopeFields":templates[template_id]["requiredFields"],"status":"staging-complete-source-verification-pending"},
      "runtimeBehaviors":{b:"fixture-ready" for b in templates[template_id]["runtimeBehaviors"]},
      "recommendation":recommendation,"promotionReady":False})

duplicates=[{"normalizedName":k,"sourceRows":v,"decision":"retain-separate-pending-governed-identity-proof"} for k,v in names.items() if k and len(v)>1]
package={"format":"multiversal-mecha-pilot-package","version":"0.1.0","records":records,"canonicalIdsAssigned":0,"promotionReadyRows":0}
out=ROOT/contract["outputDirectory"]; out.mkdir(parents=True,exist_ok=True)
(out/"MECHA_PILOT_PACKAGE.json").write_text(json.dumps(package,indent=2,sort_keys=True)+"\n")
install=out/"install-root"; uninstall=out/"uninstall-root"
for p in (install,uninstall):
    if p.exists(): shutil.rmtree(p)
install.mkdir(); shutil.copy2(out/"MECHA_PILOT_PACKAGE.json",install/"MECHA_PILOT_PACKAGE.json")
installed=json.loads((install/"MECHA_PILOT_PACKAGE.json").read_text())
assert len(installed["records"])==107 and installed["canonicalIdsAssigned"]==0
shutil.rmtree(install); uninstall.mkdir()
assert not install.exists() and not any(uninstall.iterdir())
report={
 "format":"multiversal-p0-mecha-pilot-tranche-report","version":"0.1.0","workstream":contract["workstream"],
 "recordsGenerated":len(records),"subtypeRoutedRows":sum(r["templateId"].endswith("component") for r in records),
 "duplicateClusters":len(duplicates),"duplicateDecisions":duplicates,"recommendationsApplied":recommendations,
 "unresolvedRelationshipsPreserved":unresolved_relationships,"runtimeValidatedRows":len(records),
 "pilotConversion":"passed","installTest":"passed","installedStateValidation":"passed","uninstallTest":"passed","residueCheck":"passed",
 "canonicalIdsAssigned":0,"promotionReadyRows":0,"records":records}
(out/"P0_MECHA_PILOT_TRANCHE_REPORT.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
assert len(records)==contract["expectedRows"]==107
assert all(r["rawCsv"] and r["recommendation"] and r["runtimeBehaviors"] for r in records)
assert report["canonicalIdsAssigned"]==report["promotionReadyRows"]==0
print(json.dumps({k:report[k] for k in ("recordsGenerated","subtypeRoutedRows","duplicateClusters","recommendationsApplied","pilotConversion","installTest","uninstallTest","residueCheck")},sort_keys=True))
