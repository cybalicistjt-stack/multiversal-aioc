#!/usr/bin/env python3
"""Compile deterministic ICF content packs and a provider-neutral search projection.

This is a derived compiler. Canonical authority remains in ICF-02..14 source,
rule, crosswalk and materializer artifacts. Emitted files never become live
Asset, economy, Campaign, Project, recipe-rule or creature-harvest authority.
"""
from __future__ import annotations
import argparse, hashlib, json, pathlib, shutil, subprocess, sys
from typing import Any

HERE = pathlib.Path(__file__).resolve().parent
REGISTRY = HERE / "ICF-15_CONTENT_PACK_REGISTRY.json"
FACETS = HERE / "ICF-15_SEARCH_FACET_REGISTRY.json"

def load(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def dump(path: pathlib.Path, payload: Any) -> str:
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def run_materializer(script: pathlib.Path, args: list[str]) -> None:
    proc = subprocess.run([sys.executable, str(script), *args], cwd=str(HERE), text=True, capture_output=True)
    if proc.returncode:
        raise RuntimeError(f"{script.name} failed:\n{proc.stdout}\n{proc.stderr}")

def copy_referenced_packs(source_path: pathlib.Path, destination: pathlib.Path) -> list[pathlib.Path]:
    source = load(source_path); copied = []
    for item in source.get("packs", []):
        src = HERE / item["path"]
        if not src.exists(): raise FileNotFoundError(src)
        dst = destination / src.name; dst.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(src, dst); copied.append(dst)
    return copied

def name_of(record: dict[str, Any], kind: str) -> str:
    return (record.get("displayName") or record.get("name") or record.get("creatureName") or record.get("stableId") or record.get("recipeId") or record.get("creatureDefinitionRef") or "")

def identity_of(record: dict[str, Any], kind: str) -> str:
    if kind == "recipe-or-template": return record["recipeId"]
    if kind == "creature-harvest-projection": return record["creatureDefinitionRef"]
    return record["stableId"]

def aliases_of(record: dict[str, Any]) -> list[str]:
    result=[]
    for alias in record.get("aliases", []):
        if isinstance(alias,str): result.append(alias)
        elif isinstance(alias,dict) and alias.get("display"): result.append(alias["display"])
    return result

def search_doc(record: dict[str, Any], record_set: dict[str, Any]) -> dict[str, Any]:
    kind=record_set["kind"]
    doc={"stableIdentity":identity_of(record,kind),"objectKind":kind,"displayName":name_of(record,kind),"aliases":aliases_of(record),"recordSetId":record_set["id"],"workItem":record_set["workItem"],"tags":sorted(set(record.get("tags",[]))),"coverageStatus":record.get("coverage",{}).get("status"),"provenancePresent":bool(record.get("provenance") or record.get("sourceEvidence"))}
    if kind in {"primary-ingredient","derived-preparation"}:
        tax=record.get("taxonomy",{}); ag=record.get("profiles",{}).get("agriculture",{})
        doc["facets"]={"ingredientClasses":tax.get("ingredientClasses",[]),"natureClasses":tax.get("natureClasses",[]),"originContextClasses":tax.get("originContextClasses",[]),"rarity":tax.get("rarity",{}).get("defaultBand"),"availability":tax.get("availability",{}).get("baseline"),"acquisitionModes":tax.get("availability",{}).get("acquisitionModes",[]),"edibility":record.get("profiles",{}).get("culinary",{}).get("edibility"),"perishability":record.get("profiles",{}).get("physical",{}).get("perishability"),"cultivationEligible":ag.get("cultivationEligible"),"foragingEligible":ag.get("foragingEligible"),"husbandryEligible":ag.get("husbandryEligible")}
        if kind=="derived-preparation": doc["facets"]["transformationRuleRef"]=record.get("lineage",{}).get("transformationRuleRef")
    elif kind=="recipe-or-template":
        outcome=record.get("outcome",{})
        doc["facets"]={"family":record.get("family"),"recordKind":record.get("recordKind"),"authorship":record.get("authorship"),"outputForm":record.get("outputForm"),"rarity":record.get("rarity"),"outcomeAuthority":outcome.get("authorityRef"),"executableState":"blocked-unbound-template" if outcome.get("effectStatus")=="unbound-template" else "governed"}
    elif kind=="creature-harvest-projection":
        hp=record.get("harvestProfile",{})
        doc["facets"]={"evidenceStatus":hp.get("evidenceStatus"),"bodyPlanTypeProfiles":record.get("bodyPlanTypeProfiles",[]),"traitAffinityProfiles":record.get("traitAffinityProfiles",[]),"signatureIngredient":bool(record.get("signatureIngredientRefs")),"edibility":record.get("edibilityAssertion"),"safety":record.get("safetyAssertion"),"legality":record.get("legalityAssertion"),"coverageGaps":record.get("coverageGaps",[])}
    return doc

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--out-dir",required=True); args=ap.parse_args(); out=pathlib.Path(args.out_dir).resolve()
    if out==HERE or HERE in out.parents: raise SystemExit("--out-dir must be a separate generated-output directory")
    out.mkdir(parents=True,exist_ok=True); registry=load(REGISTRY); emitted=[]
    for rs in registry["recordSets"]:
        if rs.get("materializerPath"):
            script=HERE/rs["materializerPath"]
            if not script.exists(): raise FileNotFoundError(script)
            run_materializer(script,[a.replace("{out}",str(out)) for a in rs["compileArgs"]]); emitted.extend((rs,p) for p in sorted(out.glob(rs["outputGlob"])))
        elif rs.get("copyReferencedPacks"):
            dest=out/("harvest/signature" if rs["id"].startswith("signature") else "harvest/crosswalk")
            emitted.extend((rs,p) for p in copy_referenced_packs(HERE/rs["sourcePath"],dest))
    docs=[]; identities_by_kind={}; manifest=[]
    for rs,path in emitted:
        payload=load(path); count=len(payload.get("records",[]))
        if count!=payload.get("recordCount",count): raise AssertionError(f"recordCount mismatch: {path}")
        ids=identities_by_kind.setdefault(rs["kind"],set())
        for rec in payload.get("records",[]):
            sid=identity_of(rec,rs["kind"])
            if sid in ids: raise AssertionError(f"duplicate {rs['kind']} identity: {sid}")
            ids.add(sid); docs.append(search_doc(rec,rs))
        manifest.append({"recordSetId":rs["id"],"path":path.relative_to(out).as_posix(),"recordCount":count,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    for rs in registry["recordSets"]:
        actual=sum(x["recordCount"] for x in manifest if x["recordSetId"]==rs["id"])
        if actual!=rs["recordCount"]: raise AssertionError(f"{rs['id']}: expected {rs['recordCount']} records, compiled {actual}")
    docs.sort(key=lambda x:(x["objectKind"],x["stableIdentity"]))
    if len(docs)!=registry["compiledTotals"]["searchableProjectionRecords"]: raise AssertionError("global searchable projection count mismatch")
    index_digest=dump(out/"ICF-15_SEARCH_INDEX.json",{"schemaVersion":"1.0.0","workItem":"ICF-15","authority":"derived-projection-only","authorizationRule":"authorization and field filtering must occur before counts, facets, suggestions, relationships or provenance are computed","recordCount":len(docs),"records":docs})
    manifest_digest=dump(out/"ICF-15_COMPILED_PACK_MANIFEST.json",{"schemaVersion":"1.0.0","workItem":"ICF-15","packCount":len(manifest),"recordsBySet":{rs["id"]:rs["recordCount"] for rs in registry["recordSets"]},"packs":sorted(manifest,key=lambda x:x["path"]),"searchIndex":{"path":"ICF-15_SEARCH_INDEX.json","recordCount":len(docs),"sha256":index_digest}})
    print(json.dumps({"status":"PASS","workItem":"ICF-15","searchableProjectionRecords":len(docs),"emittedPhysicalPacks":len(manifest),"manifestSha256":manifest_digest,"searchIndexSha256":index_digest},indent=2,sort_keys=True)); return 0

if __name__=="__main__": raise SystemExit(main())
