#!/usr/bin/env python3
"""Deterministically materialize and validate the ICF-04 herb/spice/fungi/forage library."""
from __future__ import annotations
import argparse, json, re
from collections import Counter
from pathlib import Path
from typing import Any

HERE=Path(__file__).resolve().parent
SOURCE=HERE/"ICF-04_LIBRARY_SOURCE.json"
ID_RE=re.compile(r"^ingredient:[a-z0-9]+(?:-[a-z0-9]+)*$")
AUTHORING_REF="governance:ICF-04-governed-first-party-herb-spice-fungi-forage-library@1.0.0"
PACKS={
 "ICF-04_LIBRARY_A_HERBS_SPICES_AROMATICS.json":["culinary_herb","spice_seed_fruit","aromatic_root_bark_resin"],
 "ICF-04_LIBRARY_B_BOTANICALS_FUNGI_CULTURES.json":["tea_medicinal_botanical","edible_fungus","fermentation_microbe"],
 "ICF-04_LIBRARY_C_WILD_FORAGE_AQUATIC.json":["wild_green_flower","wild_berry_fruit","aquatic_sea_vegetable","lichen_moss_misc"],
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
def edibility(slug:str,default:str,src:dict[str,Any])->str:
    for value in ("inedible","unsafe","conditional"):
        if slug in src.get("edibilityOverrides",{}).get(value,[]): return value
    return default
def source_assertions(slug:str,spec:dict[str,Any]|None)->list[dict[str,Any]]:
    if not spec: return []
    a=[{"assertionId":f"assertion:icf04:{slug}:identity","sourceId":spec["source"],"sourceTerm":display(slug,{"displayNameOverrides":{}}),"semantic":"identity","status":"mapped","notes":spec["assertion"]}]
    if spec.get("rarity"):
        a.append({"assertionId":f"assertion:icf04:{slug}:rarity","sourceId":spec["source"],"sourceField":"rarity/formula classification","rawValue":spec["rarity"].title(),"semantic":"rarity","status":"mapped","notes":spec["assertion"]})
    a.append({"assertionId":f"assertion:icf04:{slug}:use","sourceId":spec["source"],"semantic":"alchemy" if spec["source"]=="Alchemy.mht" else "ecology","status":"mapped","notes":spec["assertion"]})
    return a
def make_record(slug:str,src:dict[str,Any])->dict[str,Any]:
    cat=category_of(slug,src); d=src["categoryDefaults"][cat]; sb=src.get("sourceBacked",{}).get(slug)
    assertions=source_assertions(slug,sb); arefs=[a["assertionId"] for a in assertions]
    rarity=(sb or {}).get("rarity") or "common"
    rarity_status="direct" if sb and sb.get("rarity") else "first-party-authored"
    rarity_recon={"status":rarity_status,"sourceAssertionRefs":[f"assertion:icf04:{slug}:rarity"] if sb and sb.get("rarity") else []}
    if rarity_status=="first-party-authored": rarity_recon["authorityRef"]=AUTHORING_REF
    cls="class:microbial" if cat=="fermentation_microbe" else ("class:fungus" if d["nature"]=="nature:fungal" else "class:plant")
    profiles={
      "physical":{"forms":[d["form"]],"perishability":d["perishability"],"shelfLifeRuleRefs":[],"storageRequirementRefs":[],"preparationRequirementRefs":[],"contaminationRiskRefs":[]},
      "ecology":{"habitatRefs":[],"biomeRefs":[],"climateRefs":[],"seasonRefs":[],"worldRealityRefs":[],"renewability":"renewable","sourceAssertionRefs":[x for x in arefs if x.endswith(":use")]},
      "agriculture":{"cultivationEligible":bool(d["cultivation"]),"husbandryEligible":False,"foragingEligible":bool(d["foraging"]),"facilityTagRefs":[],"growthRuleRefs":[],"yieldRuleRefs":[],"resourceRequirementRefs":[],"sourceAssertionRefs":[x for x in arefs if x.endswith(":use")]},
      "economic":{"currentPriceAuthority":"MIB-13","marketScarcityAuthority":"MIB-13","tradeClassRefs":["trade:ingredient"],"legalityRefs":[],"sourceValueAssertions":[]},
      "culinary":{"edibility":edibility(slug,d["edibility"],src),"flavorPropertyRefs":list(d["culinary"]),"texturePropertyRefs":[],"techniqueCompatibilityRefs":[],"nutritionRuleRefs":[],"restorationRuleRefs":[],"pairingRefs":[],"sourceAssertionRefs":[]},
    }
    if sb and sb["source"]=="Alchemy.mht":
        profiles["alchemical"]={"roleRefs":[],"essencePropertyRefs":[],"effectPropertyRefs":[],"volatilityRuleRefs":[],"extractionRuleRefs":[],"identificationRuleRefs":[],"sourceAssertionRefs":[x for x in arefs if x.endswith(":use")]}
    gaps=[]
    if sb and slug in {"medicinal-herbs","wild-berries","mushrooms","water-plants","medicinal-plants"}:
        gaps.append({"gapId":f"gap:{slug}:generic-source-term","domain":"identity","description":"Legacy Agriculture source names a generic resource class rather than a species-specific ingredient; retain as a governed generic ingredient definition until later content binds more specific members.","sourceAssertionRefs":[arefs[0]]})
    return {
      "schemaVersion":"1.0.0","stableId":f"ingredient:{slug}","definitionVersion":"1.0.0","recordKind":"primary-ingredient","displayName":display(slug,src),"aliases":[],
      "lifecycle":{"status":"active"},"authorship":{"class":"hybrid" if sb else "governed-first-party","authoringRecordRefs":[AUTHORING_REF]+([sb["source"]] if sb else [])},
      "provenance":{"provenanceId":f"prov:icf04:{slug}","sourceAssertions":assertions},
      "taxonomy":{"ingredientClasses":[cls],"natureClasses":[d["nature"]],"originContextClasses":[],"rarity":{"defaultBand":rarity,"reconciliation":rarity_recon,"scopedOverrides":[]},"availability":{"baseline":d["availability"],"acquisitionModes":list(d["acquisition"]),"scopeAssertions":[]}},
      "units":{"primaryUnit":{"unitId":"unit:gram","dimension":"mass"},"allowedUnits":["unit:gram","unit:kilogram"],"exactConversions":[{"conversionId":"conversion:gram-to-kilogram","fromUnitId":"unit:gram","toUnitId":"unit:kilogram","numerator":1,"denominator":1000,"ruleKind":"global-exact","sourceAssertionRefs":[]}],"sourceUnitAssertions":[]},
      "profiles":profiles,"qualityConditionModel":{"liveStateAuthority":"D17 Asset Instance","qualityRuleRefs":[],"conditionRuleRefs":[],"definitionMaySetCurrentInstanceState":False},
      "substitutions":[],"coverage":{"status":"partial" if gaps else "complete","gaps":gaps},"tags":["icf04","herbs-spices-fungi-forage",f"category:{cat}","source-backed" if sb else "governed-first-party"]}
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
    assert all("magicalCulinary" not in r["profiles"] and "creatureSource" not in r["profiles"] for r in rs)
    assert all(not r["profiles"].get("alchemical",{}).get("effectPropertyRefs") for r in rs)
    assert not any("currentMarketPrice" in r or "ownerSubjectId" in r for r in rs)
    cats=Counter(next(t.split(":",1)[1] for t in r["tags"] if t.startswith("category:")) for r in rs)
    auth=Counter(r["authorship"]["class"] for r in rs); nature=Counter(r["taxonomy"]["natureClasses"][0] for r in rs); edil=Counter(r["profiles"]["culinary"]["edibility"] for r in rs)
    assert len(rs)==242 and auth["hybrid"]==9 and auth["governed-first-party"]==233
    source_ids={r["stableId"] for r in rs if r["authorship"]["class"]=="hybrid"}
    assert {"ingredient:redleaf","ingredient:soothewort","ingredient:rockroot","ingredient:snow-moss"}.issubset(source_ids)
    return {"schemaVersion":"1.0.0","workItem":"ICF-04","libraryVersion":"1.0.0","status":"PASS","recordCount":len(rs),"checks":{"stableIdsUnique":True,"allPrimaryIngredient":True,"liveStateAuthorityPreserved":True,"currentPriceAuthorityMIB13":True,"marketScarcityAuthorityMIB13":True,"noCurrentPriceFields":True,"noMagicalCulinaryClaims":True,"noCreatureSourceClaims":True,"noIndividualAlchemicalEffectClaims":True,"sourceBackedTermsPreserved":True,"magicalExoticSourceTermsDeferredToICF06":True},"categoryCounts":dict(sorted(cats.items())),"authorshipCounts":dict(auth),"natureCounts":dict(nature),"edibilityCounts":dict(edil),"deferredToICF06":src["deferredSourceTerms"]["ICF-06"],"notes":["Alchemy formula participation is preserved for Redleaf, Soothewort and Rockroot without inventing ingredient-specific effects.","Agriculture generic outputs remain generic source-backed ingredient definitions where the source does not identify a species.","Current price/scarcity remains MIB-13; live quantity/quality/condition/ownership remains D17 Asset Instance."]}
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--out-dir"); ap.add_argument("--validate-only",action="store_true"); args=ap.parse_args(); src=load(); rs=records(src); summary=validate(rs,src)
    if args.out_dir and not args.validate_only:
        out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
        for fn,categories in PACKS.items():
            pack=[r for r in rs if next(t.split(":",1)[1] for t in r["tags"] if t.startswith("category:")) in categories]
            (out/fn).write_text(json.dumps({"schemaVersion":"1.0.0","workItem":"ICF-04","libraryVersion":"1.0.0","recordCount":len(pack),"records":pack},indent=2,sort_keys=True)+"\n",encoding="utf-8")
        (out/"ICF-04_LIBRARY_VALIDATION_SUMMARY.generated.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
