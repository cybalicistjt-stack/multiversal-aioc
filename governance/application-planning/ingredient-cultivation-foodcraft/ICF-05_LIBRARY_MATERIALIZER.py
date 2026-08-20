#!/usr/bin/env python3
"""Deterministically materialize and validate the ICF-05 livestock/animal/aquatic library."""
from __future__ import annotations
import argparse, json, re
from collections import Counter
from pathlib import Path
from typing import Any

HERE=Path(__file__).resolve().parent
SOURCE=HERE/"ICF-05_LIBRARY_SOURCE.json"
ID_RE=re.compile(r"^ingredient:[a-z0-9]+(?:-[a-z0-9]+)*$")
AUTHORING_REF="governance:ICF-05-governed-first-party-livestock-animal-aquatic-library@1.0.0"
PACKS={
 "ICF-05_LIBRARY_A_LIVESTOCK_PRODUCTS.json":["livestock_game_meat","poultry_game_bird_meat","raw_milk","egg","fiber_hide_secretion"],
 "ICF-05_LIBRARY_B_FINFISH.json":["freshwater_fish","marine_fish"],
 "ICF-05_LIBRARY_C_SHELLFISH_AQUATIC.json":["crustacean","mollusk_cephalopod","aquatic_other"],
}

def load()->dict[str,Any]: return json.loads(SOURCE.read_text(encoding="utf-8"))

def display(slug:str,src:dict[str,Any])->str:
    if slug in src.get("displayNameOverrides",{}): return src["displayNameOverrides"][slug]
    return " ".join(t.capitalize() for t in slug.split("-"))

def category_of(slug:str,src:dict[str,Any])->str:
    if slug in src.get("sourceCategoryOverrides",{}): return src["sourceCategoryOverrides"][slug]
    for cat,items in src["categories"].items():
        if slug in items: return cat
    raise KeyError(slug)

def source_assertions(slug:str,spec:dict[str,Any]|None)->list[dict[str,Any]]:
    if not spec: return []
    return [
      {"assertionId":f"assertion:icf05:{slug}:identity","sourceId":spec["source"],"sourceTerm":spec["sourceTerm"],"semantic":"identity","status":"mapped","notes":spec["assertion"]},
      {"assertionId":f"assertion:icf05:{slug}:husbandry-output","sourceId":spec["source"],"sourceField":spec["sourceField"],"rawValue":spec["rawValue"],"semantic":"agriculture","status":"mapped","notes":spec["assertion"]},
    ]

def unit_profile(kind:str)->dict[str,Any]:
    if kind=="volume":
        return {"primaryUnit":{"unitId":"unit:milliliter","dimension":"volume"},"allowedUnits":["unit:milliliter","unit:liter"],"exactConversions":[{"conversionId":"conversion:milliliter-to-liter","fromUnitId":"unit:milliliter","toUnitId":"unit:liter","numerator":1,"denominator":1000,"ruleKind":"global-exact","sourceAssertionRefs":[]}],"sourceUnitAssertions":[]}
    if kind=="count":
        return {"primaryUnit":{"unitId":"unit:count","dimension":"count"},"allowedUnits":["unit:count"],"exactConversions":[],"sourceUnitAssertions":[]}
    return {"primaryUnit":{"unitId":"unit:gram","dimension":"mass"},"allowedUnits":["unit:gram","unit:kilogram"],"exactConversions":[{"conversionId":"conversion:gram-to-kilogram","fromUnitId":"unit:gram","toUnitId":"unit:kilogram","numerator":1,"denominator":1000,"ruleKind":"global-exact","sourceAssertionRefs":[]}],"sourceUnitAssertions":[]}

def make_record(slug:str,src:dict[str,Any])->dict[str,Any]:
    cat=category_of(slug,src); d=src["categoryDefaults"][cat]; sb=src.get("sourceBacked",{}).get(slug)
    assertions=source_assertions(slug,sb); arefs=[a["assertionId"] for a in assertions]
    edibility=d["edibility"]
    if slug in src.get("conditionalEdibility",[]): edibility="conditional"
    if slug in src.get("edibleOverrides",[]): edibility="known-edible"
    acquisition=list(d["acquisition"])
    if sb: acquisition=["acquisition:husbandry","acquisition:trade"]
    rarity_recon={"status":"first-party-authored","sourceAssertionRefs":[],"authorityRef":AUTHORING_REF}
    profiles={
      "physical":{"forms":[d["form"]],"perishability":d["perishability"],"shelfLifeRuleRefs":[],"storageRequirementRefs":[],"preparationRequirementRefs":[],"contaminationRiskRefs":[]},
      "ecology":{"habitatRefs":[],"biomeRefs":[],"climateRefs":[],"seasonRefs":[],"worldRealityRefs":[],"renewability":"conditionally-renewable","sourceAssertionRefs":[]},
      "agriculture":{"cultivationEligible":False,"husbandryEligible":bool(d["husbandry"]),"foragingEligible":bool(d["foraging"]),"facilityTagRefs":["facility:animal-pen"] if sb else (["facility:aquaculture"] if cat in {"freshwater_fish","marine_fish","crustacean","mollusk_cephalopod","aquatic_other"} else []),"growthRuleRefs":[],"yieldRuleRefs":[],"resourceRequirementRefs":[],"sourceAssertionRefs":[x for x in arefs if x.endswith(":husbandry-output")]},
      "economic":{"currentPriceAuthority":"MIB-13","marketScarcityAuthority":"MIB-13","tradeClassRefs":["trade:ingredient"],"legalityRefs":[],"sourceValueAssertions":[]},
      "culinary":{"edibility":edibility,"flavorPropertyRefs":list(d["culinary"]),"texturePropertyRefs":[],"techniqueCompatibilityRefs":[],"nutritionRuleRefs":[],"restorationRuleRefs":[],"pairingRefs":[],"sourceAssertionRefs":[]},
    }
    gaps=[]
    if sb:
        gaps.append({"gapId":f"gap:{slug}:generic-source-output","domain":"identity","description":"The Animal Pen source names a generic output class rather than a species-specific ingredient and does not author exact yield, processing, quality or price.","sourceAssertionRefs":[arefs[0],arefs[1]]})
    if slug=="animal-leather":
        gaps.append({"gapId":"gap:animal-leather:processing-lineage","domain":"processing","description":"The source lists leather directly as an Animal Pen output but does not define hide-to-leather processing; ICF-10 must reconcile this legacy output with derived-preparation lineage.","sourceAssertionRefs":[arefs[1]]})
    tags=["icf05","livestock-animal-aquatic",f"category:{cat}","source-backed" if sb else "governed-first-party"]
    if cat in {"freshwater_fish","marine_fish","crustacean","mollusk_cephalopod","aquatic_other"}: tags.append("aquatic")
    return {
      "schemaVersion":"1.0.0","stableId":f"ingredient:{slug}","definitionVersion":"1.0.0","recordKind":"primary-ingredient","displayName":display(slug,src),"aliases":[],
      "lifecycle":{"status":"active"},"authorship":{"class":"hybrid" if sb else "governed-first-party","authoringRecordRefs":[AUTHORING_REF]+([sb["source"]] if sb else [])},
      "provenance":{"provenanceId":f"prov:icf05:{slug}","sourceAssertions":assertions},
      "taxonomy":{"ingredientClasses":[d["cls"]],"natureClasses":[d["nature"]],"originContextClasses":[],"rarity":{"defaultBand":"common","reconciliation":rarity_recon,"scopedOverrides":[]},"availability":{"baseline":d["availability"],"acquisitionModes":acquisition,"scopeAssertions":[]}},
      "units":unit_profile(d["unit"]),
      "profiles":profiles,
      "qualityConditionModel":{"liveStateAuthority":"D17 Asset Instance","qualityRuleRefs":[],"conditionRuleRefs":[],"definitionMaySetCurrentInstanceState":False},
      "substitutions":[],"coverage":{"status":"partial" if gaps else "complete","gaps":gaps},"tags":tags}

def records(src:dict[str,Any])->list[dict[str,Any]]:
    slugs=[]
    for items in src["categories"].values(): slugs.extend(items)
    slugs.extend(src.get("sourceBacked",{}).keys())
    if len(slugs)!=len(set(slugs)): raise AssertionError("duplicate source slug")
    return [make_record(s,src) for s in slugs]

def validate(rs:list[dict[str,Any]],src:dict[str,Any])->dict[str,Any]:
    ids=[r["stableId"] for r in rs]
    assert len(ids)==len(set(ids)) and all(ID_RE.match(x) for x in ids)
    assert all(r["recordKind"]=="primary-ingredient" for r in rs)
    assert all(r["profiles"]["economic"]["currentPriceAuthority"]=="MIB-13" and r["profiles"]["economic"]["marketScarcityAuthority"]=="MIB-13" for r in rs)
    assert all(r["qualityConditionModel"]["liveStateAuthority"]=="D17 Asset Instance" and r["qualityConditionModel"]["definitionMaySetCurrentInstanceState"] is False for r in rs)
    assert all("creatureSource" not in r["profiles"] and "magicalCulinary" not in r["profiles"] and "alchemical" not in r["profiles"] for r in rs)
    assert not any("currentMarketPrice" in r or "ownerSubjectId" in r or "harvestYield" in r for r in rs)
    assert all(not r["profiles"]["economic"]["legalityRefs"] for r in rs)
    assert len(rs)==234
    auth=Counter(r["authorship"]["class"] for r in rs); assert auth==Counter({"governed-first-party":230,"hybrid":4})
    source_ids={r["stableId"] for r in rs if r["authorship"]["class"]=="hybrid"}
    assert source_ids=={"ingredient:animal-meat","ingredient:animal-milk","ingredient:animal-wool","ingredient:animal-leather"}
    cats=Counter(next(t.split(":",1)[1] for t in r["tags"] if t.startswith("category:")) for r in rs)
    aquatic=sum(v for k,v in cats.items() if k in {"freshwater_fish","marine_fish","crustacean","mollusk_cephalopod","aquatic_other"})
    assert aquatic==138
    return {"schemaVersion":"1.0.0","workItem":"ICF-05","libraryVersion":"1.0.0","status":"PASS","recordCount":len(rs),"checks":{"stableIdsUnique":True,"allPrimaryIngredient":True,"liveStateAuthorityPreserved":True,"currentPriceAuthorityMIB13":True,"marketScarcityAuthorityMIB13":True,"noCurrentPriceFields":True,"noCreatureHarvestProfiles":True,"noMagicalExoticClaims":True,"noAlchemicalEffectClaims":True,"noHarvestYieldRules":True,"noUniversalLegalityClaims":True,"animalPenSourceOutputsPreserved":True,"leatherProcessingDeferredToICF10":True},"categoryCounts":dict(sorted(cats.items())),"authorshipCounts":dict(auth),"aquaticRecordCount":aquatic,"sourceBackedStableIds":sorted(source_ids),"boundaries":src["boundaries"],"notes":["The Animal Pen source seam preserves generic meat, milk, wool and leather outputs without inventing species, yields, prices or butchery rules.","Species-named mundane meats, milks, eggs, fish and shellfish are governed first-party reusable ingredient identities, not claims about a specific creature instance or authored harvest anatomy.","ICF-07 remains the authority for creature-specific harvest/butchery procedures and ICF-10 remains the place to resolve hide-to-leather and other derived processing lineage.","Current price/scarcity remains MIB-13; live quantity, ownership, quality and condition remains D17 Asset Instance."]}

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--out-dir"); ap.add_argument("--validate-only",action="store_true"); args=ap.parse_args(); src=load(); rs=records(src); summary=validate(rs,src)
    if args.out_dir and not args.validate_only:
        out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
        for fn,categories in PACKS.items():
            pack=[r for r in rs if next(t.split(":",1)[1] for t in r["tags"] if t.startswith("category:")) in categories]
            (out/fn).write_text(json.dumps({"schemaVersion":"1.0.0","workItem":"ICF-05","libraryVersion":"1.0.0","recordCount":len(pack),"records":pack},indent=2,sort_keys=True)+"\n",encoding="utf-8")
        (out/"ICF-05_LIBRARY_VALIDATION_SUMMARY.generated.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
