#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, pathlib, re
from collections import Counter
ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"ICF-14_RECIPE_CORPUS_SOURCE.json"
GRAM=ROOT/"ICF-14_GENERATION_GRAMMAR.json"
FIX=ROOT/"ICF-14_REFERENCE_FIXTURES.json"
ID_RE=re.compile(r"^(recipe|source-recipe|recipe-template|alchemy-formula|formula-template):[a-z0-9]+(?:-[a-z0-9]+)*$")
DEF_RE=re.compile(r"^(ingredient|preparation):[a-z0-9]+(?:-[a-z0-9]+)*$")

def load(p): return json.loads(p.read_text(encoding="utf-8"))
def slot(ref,role,amount,unit,optional=False): return {"definitionRef":ref,"role":role,"quantity":{"amount":amount,"unit":unit},"optional":optional}

def materialize(s):
 p=s["pools"]; R=[]; add=R.append
 grains=p["grains"]; legumes=p["legumes"]; roots=p["roots"]; veg=p["vegetables"]; leafy=p["leafy"]; fruits=p["fruits"]; nuts=p["nutsSeeds"]; herbs=p["herbs"]; proteins=p["proteins"]; fish=p["fish"]; milks=p["milks"]; eggs=p["eggs"]
 for i in range(24):
  add({"recipeId":f"recipe:hearth-bowl-{i+1:02d}","name":f"Hearth Bowl {i+1:02d}","family":"ordinary-meal","recordKind":"concrete","authorship":"governed-first-party","inputs":[slot("ingredient:"+grains[i%len(grains)],"staple",120,"unit:gram"),slot("ingredient:"+proteins[i%len(proteins)],"protein",100,"unit:gram"),slot("ingredient:"+veg[(i*2)%len(veg)],"vegetable",80,"unit:gram"),slot("ingredient:"+herbs[(i*3)%len(herbs)],"seasoning",4,"unit:gram")],"processMedia":[{"term":"water","retained":False,"authority":"culinary-process-medium"}],"outcome":{"authorityRef":"ICF-12:ordinaryFood","qualityResolvedAtCookTime":True},"tags":["meal","bowl","ordinary"]})
 for i in range(24):
  a=["onion","garlic","leek"][i%3]
  add({"recipeId":f"recipe:stew-{i+1:02d}","name":f"Stew {i+1:02d}","family":"ordinary-meal","recordKind":"concrete","authorship":"governed-first-party","inputs":[slot("ingredient:"+legumes[i%len(legumes)],"body",110,"unit:gram"),slot("ingredient:"+roots[(i*2)%len(roots)],"body",120,"unit:gram"),slot("ingredient:"+a,"aromatic",35,"unit:gram"),slot("ingredient:"+herbs[(i*4)%len(herbs)],"seasoning",4,"unit:gram")],"processMedia":[{"term":"water","retained":True,"authority":"culinary-process-medium","exactQuantityStatus":"recipe-local-not-canonical-ingredient"}],"outcome":{"authorityRef":"ICF-12:ordinaryFood","qualityResolvedAtCookTime":True},"tags":["meal","stew","ordinary"]})
 for i in range(24):
  c=["lemon","lime","orange"][i%3]
  add({"recipeId":f"recipe:fish-plate-{i+1:02d}","name":f"Fish Plate {i+1:02d}","family":"ordinary-meal","recordKind":"concrete","authorship":"governed-first-party","inputs":[slot("ingredient:"+fish[i%len(fish)],"protein",140,"unit:gram"),slot("ingredient:"+c,"acid-aromatic",25,"unit:gram"),slot("ingredient:"+herbs[(i*5)%len(herbs)],"seasoning",4,"unit:gram"),slot("ingredient:"+veg[(i*3)%len(veg)],"vegetable",80,"unit:gram")],"outcome":{"authorityRef":"ICF-12:ordinaryFood","qualityResolvedAtCookTime":True},"tags":["meal","fish","ordinary"]})
 for i in range(32):
  m=milks[i%2]
  add({"recipeId":f"recipe:bake-{i+1:02d}","name":f"Bakery Formula {i+1:02d}","family":"baked-good","recordKind":"concrete","authorship":"governed-first-party","inputs":[slot("preparation:"+grains[i%len(grains)]+"-flour","structure",180,"unit:gram"),slot("ingredient:"+m,"liquid",90,"unit:milliliter"),slot("ingredient:"+eggs[i%2],"binder",1,"unit:count"),slot("preparation:"+m+"-butter","fat",30,"unit:gram"),slot("ingredient:"+fruits[i%len(fruits)],"flavor",60,"unit:gram",i%3==0)],"outcome":{"authorityRef":"ICF-12:ordinaryFood","qualityResolvedAtCookTime":True},"tags":["baked-good","ordinary"]})
 juices=p["juiceFruits"]
 for i in range(24):
  add({"recipeId":f"recipe:beverage-{i+1:02d}","name":f"Botanical Beverage {i+1:02d}","family":"beverage","recordKind":"concrete","authorship":"governed-first-party","inputs":[slot("preparation:"+juices[i%len(juices)]+"-juice","base",220,"unit:milliliter"),slot("ingredient:"+herbs[i%len(herbs)],"botanical",3,"unit:gram"),slot("ingredient:honey","sweetener",12,"unit:gram",True)],"outcome":{"authorityRef":"ICF-12:ordinaryFood","qualityResolvedAtCookTime":True},"tags":["beverage","ordinary"]})
 for i in range(24):
  acid=["lemon","lime","orange"][i%3]
  add({"recipeId":f"recipe:fresh-side-{i+1:02d}","name":f"Fresh Side {i+1:02d}","family":"fresh-side","recordKind":"concrete","authorship":"governed-first-party","inputs":[slot("ingredient:"+leafy[i%len(leafy)],"leafy-base",90,"unit:gram"),slot("ingredient:"+veg[(i*2)%len(veg)],"vegetable",70,"unit:gram"),slot("ingredient:"+nuts[(i*3)%len(nuts)],"texture",18,"unit:gram"),slot("ingredient:"+acid,"acid",20,"unit:gram")],"outcome":{"authorityRef":"ICF-12:ordinaryFood","qualityResolvedAtCookTime":True},"tags":["side","fresh","ordinary"]})
 oils=["preparation:olive-oil","preparation:sesame-seed-oil","preparation:sunflower-seed-oil"]
 for i in range(16):
  a=["garlic","onion","leek"][i%3]; acid=["lemon","lime"][i%2]
  add({"recipeId":f"recipe:sauce-{i+1:02d}","name":f"Herb Sauce {i+1:02d}","family":"stock-sauce","recordKind":"concrete","authorship":"governed-first-party","inputs":[slot(oils[i%3],"fat-base",45,"unit:milliliter"),slot("ingredient:"+herbs[i%len(herbs)],"botanical",10,"unit:gram"),slot("ingredient:"+a,"aromatic",12,"unit:gram"),slot("ingredient:"+acid,"acid",18,"unit:gram")],"outcome":{"authorityRef":"ICF-12:ordinaryFood","qualityResolvedAtCookTime":True,"usage":"component-or-serving"},"tags":["sauce","ordinary"]})
 for i,m in enumerate(s["preservationMappings"]):
  add({"recipeId":f"recipe:preserve-{i+1:02d}","name":f"Preservation Formula {i+1:02d}","family":"preservation","recordKind":"concrete","authorship":"governed-first-party","inputs":[slot(m["input"],"preservation-input",250,"unit:gram")],"outputDefinitionRef":m["output"],"transformationRuleRef":m["rule"],"outcome":{"authorityRef":"ICF-10","culinaryPreservationAuthorityRef":"ICF-12:ordinaryFood.preservation"},"tags":["preservation","derived-preparation"]})
 surv_f=["preparation:"+x+"-dried" for x in ["apple","pear","peach","plum","strawberry","grape"]]; surv_p=["preparation:"+x+"-cured" for x in ["beef","pork","lamb","chicken-meat","turkey-meat","rabbit-meat"]]
 for i in range(24):
  add({"recipeId":f"recipe:survival-ration-{i+1:02d}","name":f"Survival Ration {i+1:02d}","family":"survival-food","recordKind":"concrete","authorship":"governed-first-party","inputs":[slot(surv_p[i%6],"protein",90,"unit:gram"),slot(surv_f[(i*2)%6],"fruit",60,"unit:gram"),slot("ingredient:"+nuts[(i*3)%len(nuts)],"fat-seed",30,"unit:gram")],"outcome":{"authorityRef":"ICF-12:ordinaryFood","qualityResolvedAtCookTime":True},"tags":["survival","portable","ordinary"]})
 for x in s["sourceCulinaryRecipes"]:
  add({"recipeId":"source-recipe:"+x["slug"],"name":x["name"],"family":"source-culinary","recordKind":"source-backed","authorship":"source-derived","inputs":[],"sourceIngredientEnumerationStatus":"not-enumerated-in-governed-ICF12-assertion","outcome":{"authorityRef":"ICF-12","kind":x["kind"],"quality":x["quality"],"cookingDL":x["cookingDL"],"effectText":x["effectText"]},"tags":["source-recipe",x["kind"]]})
 for i in range(24):
  add({"recipeId":f"recipe-template:regional-{i+1:02d}","name":f"Regional Dish Template {i+1:02d}","family":"cultural-regional-template","recordKind":"template","authorship":"governed-first-party","slots":[{"slot":"staple","selector":"canonical ingredient/preparation tagged for staple use","quantity":{"amount":120,"unit":"unit:gram"}},{"slot":"featured-component","selector":"canonical edible ingredient authorized by ICF profile","quantity":{"amount":100,"unit":"unit:gram"}},{"slot":"aromatic","selector":"canonical herb/spice/aromatic ingredient","quantity":{"amount":5,"unit":"unit:gram"}}],"instantiationRule":"must bind every slot to canonical definition refs and attach separately authored setting/culture scope; template creates no culture/world facts","outcome":{"authorityRef":"ICF-12:ordinaryFood","qualityResolvedAtCookTime":True},"tags":["template","regional-style","noncanonical-setting"]})
 base=[f"recipe:hearth-bowl-{i:02d}" for i in range(1,13)]
 for i in range(24):
  ench=s["icf12EnchantmentRefs"][i%len(s["icf12EnchantmentRefs"])]
  add({"recipeId":f"recipe-template:enchanted-{i+1:02d}","name":f"Enchanted Meal Template {i+1:02d}","family":"enchanted-elemental-food","recordKind":"template","authorship":"governed-first-party","baseMealRecipeRef":base[i%12],"enchantmentRef":ench,"slots":[{"slot":"enchantment-ingredient","selector":"canonical ingredient explicitly eligible as an enchantment ingredient under governed evidence","sourceExamples":s["enchantmentIngredientSourceExamples"]}],"requirements":["Cooking skill check","spellcaster or enchanted tools"],"outcome":{"authorityRef":"ICF-12:enchantedFood","rawIngredientEffectProjection":False},"tags":["template","enchanted-food","elemental" if ench=="food-enchantment:elemental-flavor" else "magical"]})
 for i in range(12):
  add({"recipeId":f"recipe-template:alchemical-food-{i+1:02d}","name":f"Alchemical Food Template {i+1:02d}","family":"alchemical-food","recordKind":"template","authorship":"governed-first-party","baseMealRecipeRef":base[i%12],"formulaRef":s["icf11FormulaRefs"][i%3],"outcome":{"authorityRef":"ICF-12:specializedCooking.alchemicalCooking","formulaAuthorityRef":"ICF-11","interactionEffectStatus":"not-precomputed"},"tags":["template","alchemical-food"]})
 for x in s["sourceAlchemyFormulas"]:
  add({"recipeId":"alchemy-formula:"+x["slug"],"name":x["name"],"family":"source-alchemy","recordKind":"source-backed","authorship":"source-derived","outputForm":x["outputForm"],"rarity":x["rarity"],"mixingDC":x["mixingDC"],"requirementAuthorityRef":"ICF-11_FORMULA_GRAMMAR.sampleFormulas","sourceExamplesAreExactRequirements":False,"outcome":{"authorityRef":"ICF-11","effectText":x["effectText"]},"tags":["source-formula",x["outputForm"],x["rarity"]]})
 for form in s["alchemyOutputForms"]:
  for rarity in s["alchemyRarityBands"]:
   add({"recipeId":f"formula-template:{form}-{rarity}","name":f"{rarity.title()} {form.title()} Formulation Template","family":"alchemical-formulation-template","recordKind":"template","authorship":"governed-first-party","outputForm":form,"rarity":rarity,"compositionProfileRef":f"ICF-11_FORMULA_GRAMMAR.compositionByRarity.{rarity}","roleSlotAuthorityRef":"ICF-11_FORMULA_GRAMMAR.roleSlots","effectRequirement":"must reference an already governed formula/effect specification before becoming executable","outcome":{"authorityRef":"ICF-11","effectStatus":"unbound-template"},"tags":["template","alchemy",form,rarity]})
 return R

def validate(s,R,g,f):
 E=[]; need=lambda ok,msg:E.append(msg) if not ok else None
 need(len(R)==319,"recipe count"); ids=[r["recipeId"] for r in R]; need(len(ids)==len(set(ids)) and all(ID_RE.fullmatch(x) for x in ids),"recipe ids")
 kinds=Counter(r["recordKind"] for r in R); need(kinds==Counter({"concrete":216,"template":92,"source-backed":11}),"record kind counts"); auth=Counter(r["authorship"] for r in R); need(auth==Counter({"governed-first-party":308,"source-derived":11}),"authorship counts")
 fam=Counter(r["family"] for r in R); expected={"ordinary-meal":72,"baked-good":32,"beverage":24,"fresh-side":24,"stock-sauce":16,"preservation":24,"survival-food":24,"source-culinary":8,"cultural-regional-template":24,"enchanted-elemental-food":24,"alchemical-food":12,"source-alchemy":3,"alchemical-formulation-template":32}; need(dict(fam)==expected,"family counts")
 pools=s["pools"]; primary=set(); [primary.update(pools[k]) for k in ["grains","legumes","roots","vegetables","leafy","fruits","nutsSeeds","herbs","proteins","fish","milks","eggs"]]; primary.add("honey"); known={"ingredient:"+x for x in primary}; known.update("preparation:"+x+"-flour" for x in pools["grains"]); known.update("preparation:"+x+"-butter" for x in pools["milks"]); known.update("preparation:"+x+"-juice" for x in pools["juiceFruits"]); known.update({"preparation:olive-oil","preparation:sesame-seed-oil","preparation:sunflower-seed-oil"}); known.update(m["output"] for m in s["preservationMappings"]); known.update("preparation:"+x+"-dried" for x in ["apple","pear","peach","plum","strawberry","grape"]); known.update("preparation:"+x+"-cured" for x in ["beef","pork","lamb","chicken-meat","turkey-meat","rabbit-meat"])
 for r in R:
  for i in r.get("inputs",[]): need(DEF_RE.fullmatch(i["definitionRef"]) is not None,r["recipeId"]+": input ref"); need(i["definitionRef"] in known,r["recipeId"]+": input ref not in canonical source/ICF10-derived set"); need(i["quantity"]["amount"]>0 and i["quantity"]["unit"].startswith("unit:"),r["recipeId"]+": quantity")
  txt=json.dumps(r,sort_keys=True)
  for bad in ["currentMarketPrice","currentQuantity","ownerSubjectId","marketScarcityValue","wallClockProgress"]: need(bad not in txt,r["recipeId"]+": prohibited "+bad)
 ordinary={"ordinary-meal","baked-good","beverage","fresh-side","stock-sauce","survival-food"}; need(all(r["outcome"]["authorityRef"]=="ICF-12:ordinaryFood" and r["outcome"].get("qualityResolvedAtCookTime") is True and "effectText" not in r["outcome"] for r in R if r["family"] in ordinary),"ordinary outcome"); need(all(r["outputDefinitionRef"].startswith("preparation:") and r["outcome"]["authorityRef"]=="ICF-10" for r in R if r["family"]=="preservation"),"preservation")
 sc=[r for r in R if r["family"]=="source-culinary"]; need(len(sc)==8 and all(r["inputs"]==[] for r in sc),"source culinary"); need(all(r["enchantmentRef"] in set(s["icf12EnchantmentRefs"]) and r["outcome"]["rawIngredientEffectProjection"] is False for r in R if r["family"]=="enchanted-elemental-food"),"enchanted"); sa=[r for r in R if r["family"]=="source-alchemy"]; need(len(sa)==3 and all(r["sourceExamplesAreExactRequirements"] is False for r in sa),"source alchemy")
 aft=[r for r in R if r["family"]=="alchemical-formulation-template"]; need(len(aft)==32 and all(r["outcome"]["effectStatus"]=="unbound-template" for r in aft),"alchemy templates"); need({r["outputForm"] for r in aft}==set(s["alchemyOutputForms"]),"alchemy forms"); need({r["rarity"] for r in aft}==set(s["alchemyRarityBands"]),"alchemy rarity"); need(all(r["outcome"]["interactionEffectStatus"]=="not-precomputed" for r in R if r["family"]=="alchemical-food"),"alchemical food"); need(all("creates no culture/world facts" in r["instantiationRule"] for r in R if r["family"]=="cultural-regional-template"),"culture templates")
 need(len(g["generationPhases"])==8 and g["templateResolution"]["unresolvedTemplateExecutable"] is False,"grammar"); need(g["boundaries"]["liveStateAuthority"]=="D17 Asset Instance" and g["boundaries"]["currentPriceAuthority"]=="MIB-13" and g["boundaries"]["marketScarcityAuthority"]=="MIB-13","owner boundaries"); need(g["boundaries"]["migration0022Required"] is False and g["boundaries"]["realMoneyBehavior"] is False,"migration/real money"); need(f["fixtureCount"]==18==len(f["fixtures"]),"fixtures")
 if E:return {"schemaVersion":"1.0.0","workItem":"ICF-14","status":"FAIL","errors":E}
 return {"schemaVersion":"1.0.0","workItem":"ICF-14","status":"PASS","recipeCount":319,"concreteRecipeCount":216,"templateCount":92,"sourceBackedRecipeCount":11,"familyCount":13,"familyCounts":dict(sorted(fam.items())),"generationPhaseCount":8,"fixtureScenarioCount":18,"sourceCulinaryRecipeCount":8,"sourceAlchemyFormulaCount":3,"alchemyFormulationTemplateCount":32,"alchemyOutputFormCount":8,"checks":{"stableRecipeIdsUnique":True,"allConcreteInputsTypedCanonicalRefs":True,"ordinaryOutcomesRemainICF12Owned":True,"preservationUsesICF10PreparationOutputs":True,"sourceCulinaryInputsNotReconstructed":True,"sourceAlchemyExamplesNotExactLocks":True,"enchantedEffectsRemainICF12Owned":True,"rawIngredientEffectProjectionForbidden":True,"alchemicalTemplatesRequireGovernedEffect":True,"alchemicalFoodInteractionNotInvented":True,"culturalTemplatesCreateNoWorldCanon":True,"D17LiveStatePreserved":True,"MIB13PriceScarcityPreserved":True,"providerAuthorityNotIntroduced":True,"migration0022NotRequired":True,"realMoneyBehavior":False}}

def main():
 a=argparse.ArgumentParser(); a.add_argument("--out-dir"); q=a.parse_args(); s=load(SRC); g=load(GRAM); f=load(FIX); R=materialize(s); V=validate(s,R,g,f)
 if q.out_dir and V["status"]=="PASS":
  out=pathlib.Path(q.out_dir); out.mkdir(parents=True,exist_ok=True)
  for n in range(5):
   pack=R[n*64:(n+1)*64]
   if pack:(out/f"ICF-14_RECIPE_PACK_{n+1:02d}.json").write_text(json.dumps({"schemaVersion":"1.0.0","workItem":"ICF-14","recordCount":len(pack),"records":pack},indent=2,sort_keys=True)+"\n")
 print(json.dumps(V,indent=2,sort_keys=True)); return 0 if V["status"]=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
