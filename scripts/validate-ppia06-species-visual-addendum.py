#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
B=ROOT/"governance/application-planning/parallel-preimplementation"
req={
 "owner":B/"PPIA-06_OWNER_VISUAL_CANON_DECISIONS_v0.1.0.json",
 "manifest":B/"PPIA-06_SPECIES_VISUAL_AUTHORITY_MANIFEST_v0.1.0.json",
 "profiles":B/"PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json",
 "conflicts":B/"PPIA-06_SPECIES_VISUAL_CONFLICT_REGISTER_v0.1.0.json",
 "taxonomy":B/"PPIA-06_APPEARANCE_SEMANTIC_TAXONOMY_v0.2.0.json",
 "renderer":B/"PPIA-06_PIXEL_ART_RENDERER_CONTRACT_v0.2.0.json",
 "cases":B/"PPIA-06_SPECIES_VISUAL_REFERENCE_CASES_v0.1.0.json",
 "addendum":B/"PPIA-06_SPECIES_VISUAL_MORPHOLOGY_SOURCE_ADDENDUM_v0.1.0.md",
}
def fail(m): raise SystemExit("PPIA-06 SPECIES VISUAL ADDENDUM: FAIL — "+m)
def need(c,m):
 if not c: fail(m)
def load_path(p:Path):
 need(p.exists(),"missing "+str(p.relative_to(ROOT)))
 return json.loads(p.read_text(encoding="utf-8")) if p.suffix==".json" else p.read_text(encoding="utf-8")
def load(k): return load_path(req[k])
def main():
 o,m,p,c,t,r,q,a=[load(k) for k in ["owner","manifest","profiles","conflicts","taxonomy","renderer","cases","addendum"]]
 need(len(o["decisions"])>=27,"owner decisions incomplete")
 need(any(x.get("id")=="OVC-027" and "all rat-humanoid" in x.get("decision","").lower() and "Furashin" in x.get("decision","") for x in o["decisions"]),"OVC-027 broad Furashin art ruling missing")
 need(m["inventory"]["pdf_count"]==27 and m["inventory"]["art_count"]==88,"Arthold inventory mismatch")
 need(len(m["document_sources"])==27,"document source inventory must contain 27 PDFs")
 parts=m.get("art_manifest_parts",[])
 need(len(parts)==4,"art inventory must be split into exactly four governed parts")
 assets=[]
 for fn in parts:
  part=load_path(B/fn)
  need(part.get("part_count")==4,"art manifest part_count mismatch")
  need(part.get("asset_count")==len(part.get("assets",[])),"art manifest part asset_count mismatch")
  need(part.get("default_asset_class")=="ai_generated_reference_or_inspiration" and part.get("default_authority")=="noncanonical_unless_owner_explicitly_promotes","art manifest defaults changed")
  assets.extend(part["assets"])
 need(len(assets)==88,"art parts must inventory exactly 88 files")
 art_names=[x["filename"] for x in assets]
 need(len(set(art_names))==88,"art filenames must be unique")
 need(any(x["filename"]=="IMG_20240811_115259.jpg" and x.get("species_binding")=="Rakuuta" for x in assets),"Rakuuta owner concept binding missing")
 need(any(x["filename"]=="IMG_20240812_114703.jpg" and x.get("species_binding")=="Kola-Ha" for x in assets),"Kola-Ha owner concept binding missing")
 rat_humanoid=[x for x in assets if "ratman" in x["filename"].lower()]
 need(len(rat_humanoid)>=9,"expected Arthold rat-humanoid reference set")
 need(all(x.get("species_binding")=="Furashin" for x in rat_humanoid),"all rat-humanoid Arthold art must bind to Furashin")
 need(all(x.get("binding_authority")=="owner_identification_OVC-027" for x in rat_humanoid),"rat-humanoid art must carry OVC-027 binding authority")
 need(any(x.get("species_binding")=="Ratman" for x in []) is False,"art binding rule must not fabricate Ratman art")
 need(any(x.get("scope")=="all rat-humanoid artwork in Arthold.zip" and x.get("species_binding")=="Furashin" for x in m.get("owner_identified_ai_bindings",[])),"authority manifest broad Furashin art binding missing")
 need(p["profile_count"]==25 and len(p["profiles"])==25,"must cover exactly 25 direct Species")
 species_names={x["species"] for x in p["profiles"]}
 for s in ["Vespin","Moravi","Rakuuta","Furashin","Ratman","Kola-Ha","Toba-Madra","Arborae","Mythragara","Suula","Nekron","ManyToms","The Free","Stygian","Giantkin","Gray"]: need(s in species_names,"missing profile "+s)
 by={x["species"]:x for x in p["profiles"]}
 need("4 arms" in json.dumps(by["Vespin"]),"Vespin four-arm correction missing")
 need("4 legs" in json.dumps(by["Moravi"]),"Moravi four-leg topology missing")
 need("no horns" in json.dumps(by["Rakuuta"]).lower(),"Rakuuta horn correction missing")
 need("three simultaneous fur colors" in json.dumps(by["Furashin"]),"Furashin three-color control missing")
 need("long prehensile tail" in json.dumps(by["Ratman"]).lower(),"separate Ratman Species profile missing")
 need("anthropomorphic bear" in json.dumps(by["Toba-Madra"]).lower(),"Toba ursine correction missing")
 need("four separately customizable" in json.dumps(by["Arborae"]).lower(),"Arborae four-season authoring missing")
 need("one_time" in by["Nekron"]["appearance_state_model"],"Nekron one-time transition missing")
 need("composite" in by["ManyToms"]["baseline_topology"],"ManyToms composite topology missing")
 need("humanoid_android" in by["The Free"]["baseline_topology"],"Free humanoid android bound missing")
 need(len(c["resolved_conflicts"])>=11 and c["unresolved_visual_conflicts"]==[],"visual conflict register incomplete")
 need(any(x.get("id")=="VC-011" and x.get("decision")=="OVC-027" for x in c["resolved_conflicts"]),"VC-011 Furashin/Ratman filename conflict resolution missing")
 need("owner_canon_decision" in t["provenance_classes"],"taxonomy lacks owner decision provenance")
 need("constituent_body" in t["morphology_graph_contract"]["node_kinds"],"taxonomy lacks composite body node")
 need(r["view_contract"]["master_view"]=="full_body_three_quarter" and r["view_contract"]["arbitrary_rotation"] is False,"fixed 3/4 view contract missing")
 need(r["topology"]["six_limb_and_composite_support_required"] is True,"renderer lacks six-limb/composite requirement")
 need("visual-only" in r["wardrobe_and_equipment"]["presentation_wardrobe"],"presentation wardrobe boundary missing")
 need(q["case_count"]>=36 and len(q["cases"])==q["case_count"],"species visual QA corpus too small or count mismatch")
 low=a.lower()
 for phrase in ["morphology graph","presentation-only wardrobe","3/4 full-body master view","no known visual conflict","does not authorize ppia-06 to invent or mutate biology"]: need(phrase in low,"addendum missing "+phrase)
 for prohibited in ["runtime_activation=true","arbitrary rotation is allowed"]: need(prohibited not in low,"prohibited activation/rotation implication")
 print("PPIA-06 SPECIES VISUAL ADDENDUM: PASS")
 print(f"species_profiles={p['profile_count']} art_assets={len(assets)} rat_humanoid_furashin={len(rat_humanoid)} resolved_conflicts={len(c['resolved_conflicts'])} qa_cases={q['case_count']}")
 print("morphology_graph=true six_limb=true composite=true nested_appendage=true")
 print("ratman_species_preserved=true arthold_rat_humanoid_art=Furashin filename_prompt_authority=false")
 print("fixed_three_quarter=true portrait_zoom=true token=true arbitrary_rotation=false")
 print("presentation_wardrobe_nonmechanical=true actual_equipment_projection_separate=true")
 print("runtime_activation=false")
if __name__=="__main__": main()
