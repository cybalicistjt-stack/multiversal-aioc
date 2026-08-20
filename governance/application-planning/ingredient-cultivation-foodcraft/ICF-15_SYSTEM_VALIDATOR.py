#!/usr/bin/env python3
"""Validate ICF-15 pack/search/workbench contracts and their owner boundaries."""
from __future__ import annotations
import argparse, json, pathlib, subprocess, sys
from typing import Any

HERE = pathlib.Path(__file__).resolve().parent

def load(name: str) -> Any:
    return json.loads((HERE/name).read_text(encoding="utf-8"))

def fail(errors: list[str], ok: bool, message: str) -> None:
    if not ok:
        errors.append(message)

def static_validate() -> dict[str, Any]:
    reg = load("ICF-15_CONTENT_PACK_REGISTRY.json")
    facets = load("ICF-15_SEARCH_FACET_REGISTRY.json")
    insp = load("ICF-15_INSPECTOR_WORKBENCH_PROJECTIONS.json")
    harvest = load("ICF-15_HARVEST_COVERAGE_REPORT.json")
    fixtures = load("ICF-15_REFERENCE_FIXTURES.json")
    expected = load("ICF-15_VALIDATION_SUMMARY.json")
    e: list[str] = []

    fail(e, reg["workItem"]=="ICF-15" and reg["packVersion"]=="1.0.0", "registry identity/version")
    fail(e, len(reg["recordSets"])==8, "record-set count")
    fail(e, sum(x["recordCount"] for x in reg["recordSets"])==1717, "record-set total")
    fail(e, reg["compiledTotals"]=={
        "primaryIngredientDefinitions":971,
        "derivedPreparationDefinitions":400,
        "recipeAndTemplateRecords":319,
        "creatureHarvestCrosswalkRecords":27,
        "searchableProjectionRecords":1717}, "compiled totals")
    fail(e, len(reg["ruleSets"])==6, "rule-set count")
    b=reg["boundaries"]
    fail(e, b["authorizationBeforeSearchCountsFacets"] is True, "authorization-before-facets")
    fail(e, b["liveStateAuthority"]=="D17 Asset Instance", "D17 authority")
    fail(e, b["currentPriceAuthority"]=="MIB-13" and b["marketScarcityAuthority"]=="MIB-13", "MIB13 authority")
    fail(e, b["cozyAutomationAuthority"].startswith("APM/CEL"), "cozy authority")
    fail(e, b["migration0022Required"] is False and b["realMoneyBehavior"] is False, "migration/real-money boundary")

    fail(e, facets["queryContract"]["stableIdentityOnly"] is True, "stable identity search")
    fail(e, facets["queryContract"]["hiddenCountLeakageForbidden"] is True, "hidden count leakage")
    fail(e, facets["queryContract"]["providerNeutral"] is True, "provider neutral search")
    counts={k:len(v) for k,v in facets["facets"].items()}
    fail(e, counts=={"ingredient":13,"preparation":4,"recipe":7,"creature-harvest":8}, f"facet counts {counts}")

    fail(e, set(insp["projections"])=={"ingredient","recipe","creature-harvest"}, "inspector projections")
    fail(e, insp["workbench"]["mode"].startswith("derived read-only"), "workbench read-only")
    fail(e, insp["workbench"]["cozyEligibility"]["metadataOnly"] is True, "cozy metadata only")
    forbidden=" ".join(insp["workbench"]["cozyEligibility"]["doesNotMean"])
    fail(e, "wall-clock progress" in forbidden and "automatic spending" in forbidden, "cozy denied semantics")

    c=harvest["catalogCoverage"]
    fail(e, c["canonicalCreatureCount"]==27 and c["executableHarvestProfileCount"]==0 and c["evidenceGapProfileCount"]==27, "harvest executable-gap counts")
    fail(e, c["canonicalSignatureIngredientCount"]==7 and c["creaturesWithSignatureIngredientRefs"]==6, "signature coverage")
    fail(e, all(v==27 for v in harvest["universalGapCounts"].values()), "universal harvest gap preservation")

    fail(e, fixtures["fixtureCount"]==24==len(fixtures["fixtures"]), "fixture count")
    fail(e, len({x["id"] for x in fixtures["fixtures"]})==24, "fixture IDs unique")
    fail(e, all(x["expected"]=="pass" for x in fixtures["fixtures"]), "fixture expectations")
    fail(e, expected["status"]=="PASS" and expected["compiledProjectionRecordCount"]==1717, "expected summary")
    fail(e, expected["fixtureScenarioCount"]==24, "expected fixture count")
    return {
      "schemaVersion":"1.0.0","workItem":"ICF-15",
      "status":"FAIL" if e else "PASS",
      "staticChecks":{
        "recordSetCount":8,"ruleSetCount":6,"compiledProjectionRecordCount":1717,
        "facetCounts":counts,"inspectorProjectionCount":3,"fixtureScenarioCount":24,
        "harvestCatalogCreatureCount":27,"harvestExecutableProfileCount":0,
      },
      "errors":e,
    }

def full_repo_validate() -> dict[str, Any]:
    errors=[]
    required_summaries = {
      "ICF-03_LIBRARY_VALIDATION_SUMMARY.json":176,
      "ICF-04_LIBRARY_VALIDATION_SUMMARY.json":242,
      "ICF-05_LIBRARY_VALIDATION_SUMMARY.json":234,
      "ICF-06_LIBRARY_VALIDATION_SUMMARY.json":312,
      "ICF-10_VALIDATION_SUMMARY.json":400,
      "ICF-14_VALIDATION_SUMMARY.json":319,
    }
    for name,count in required_summaries.items():
        path=HERE/name
        if not path.exists():
            errors.append(f"missing upstream summary {name}")
            continue
        payload=json.loads(path.read_text(encoding="utf-8"))
        if payload.get("status")!="PASS":
            errors.append(f"upstream summary not PASS {name}")
        actual = payload.get("recordCount", payload.get("recipeCount"))
        if actual != count:
            errors.append(f"{name}: expected {count}, got {actual}")
    h9=HERE/"ICF-09_VALIDATION_SUMMARY.json"
    if not h9.exists():
        errors.append("missing ICF-09_VALIDATION_SUMMARY.json")
    else:
        z=json.loads(h9.read_text(encoding="utf-8"))
        if not (z.get("status")=="PASS" and z.get("canonicalCreatureCount")==27 and z.get("canonicalSignatureIngredientCount")==7):
            errors.append("ICF-09 summary mismatch")
    p13=HERE/"ICF-13_PRODUCTION_RULES.json"
    if not p13.exists():
        errors.append("missing ICF-13_PRODUCTION_RULES.json")
    else:
        z=json.loads(p13.read_text(encoding="utf-8"))
        b=z["authorityBoundaries"]
        if b["liveStateAuthority"]!="D17 Asset Instance" or b["currentPriceAuthority"]!="MIB-13" or not b["cozyAutomationAuthority"].startswith("APM/CEL"):
            errors.append("ICF-13 authority boundary mismatch")
        if "wall-clock elapsed time" not in z["timeModel"]["runtimeRule"]:
            errors.append("ICF-13 wall-clock guardrail missing")

    creature_records=[]
    for n in range(1,5):
        path=HERE/f"ICF-09_CANONICAL_CREATURE_CROSSWALK_PACK_{n:02d}.json"
        if not path.exists():
            errors.append(f"missing {path.name}")
            continue
        creature_records += json.loads(path.read_text(encoding="utf-8"))["records"]
    if creature_records:
        if len(creature_records)!=27: errors.append("creature crosswalk count")
        if any(r.get("harvestProfile",{}).get("evidenceStatus")!="gap" for r in creature_records):
            errors.append("unexpected executable creature harvest profile")
        if sum(bool(r.get("signatureIngredientRefs")) for r in creature_records)!=6:
            errors.append("signature-bearing creature count")
        if sum(len(r.get("signatureIngredientRefs",[])) for r in creature_records)!=7:
            errors.append("signature ingredient ref count")

    return {"status":"FAIL" if errors else "PASS","errors":errors}

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--full-repo", action="store_true")
    ap.add_argument("--compile-out")
    args=ap.parse_args()
    result=static_validate()
    if result["status"]=="PASS" and args.full_repo:
        result["fullRepo"]=full_repo_validate()
        if result["fullRepo"]["status"]!="PASS":
            result["status"]="FAIL"
    if result["status"]=="PASS" and args.compile_out:
        proc=subprocess.run([sys.executable,str(HERE/"ICF-15_CONTENT_PACK_COMPILER.py"),"--out-dir",args.compile_out],
                            text=True,capture_output=True)
        result["compiler"]={"returncode":proc.returncode,"stdout":proc.stdout,"stderr":proc.stderr}
        if proc.returncode:
            result["status"]="FAIL"
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0 if result["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
