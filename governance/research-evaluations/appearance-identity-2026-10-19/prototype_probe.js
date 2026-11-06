"use strict";
// APPEARANCE RESEARCH PROBE ONLY. Not a game runtime, owner resolver, or canonical validator.
const contexts=["neutral","daylight","low_light","interior_warm","high_contrast_magic"];
const methods=["no-roll","fixed-dc","opposed-check","degree-of-success","extended-challenge","gm-determined"];
const owned={character:"Character-Actors",form:"Species/Form",outfit:"FDE-04",appearance:"CAPP/PPIA"};
const allowedRecipe=["schemaVersion","character","form","outfit","appearance","presentation","abilities","equipment","requiredCapabilities"];
const allowedReference=["ref","version"];
const allowedForm=["ref","version","topology","visibility"];
const allowedOutfit=["ref","version","checksum"];
const allowedPresentation=["context","view","effectVisible"];
const views=["cas_sd_full_body","cas_sd_portrait","cas_sd_token"];
const obj=x=>x!==null&&typeof x==="object"&&!Array.isArray(x);
const keys=(x,allow)=>obj(x)&&Object.keys(x).every(k=>allow.includes(k));
const id=x=>typeof x==="string"&&x.trim().length>0&&x.length<=256;
function hash(x){
 const v=JSON.stringify(x);let n=2166136261;
 for(let i=0;i<v.length;i++){n^=v.charCodeAt(i);n=Math.imul(n,16777619);}
 return (n>>>0).toString(16).padStart(8,"0");
}
function inspect(recipe,catalog,scopes=[]){
 const deny=reason=>({status:"rejected",reason,requiresReview:true,actions:[]});
 if(!keys(recipe,allowedRecipe)||recipe.schemaVersion!=="APPEARANCE-STUDY-1"||!obj(catalog))return deny("unrecognized-schema");
 if(!keys(recipe.character,allowedReference)||!keys(recipe.form,allowedForm)||!keys(recipe.outfit,allowedOutfit)||!keys(recipe.appearance,allowedReference)||!keys(recipe.presentation,allowedPresentation))return deny("unapproved-fields");
 if(!id(recipe.character.ref)||!id(recipe.character.version)||!id(recipe.form.ref)||!id(recipe.form.version)||!id(recipe.form.topology)||!id(recipe.outfit.ref)||!id(recipe.outfit.version)||!id(recipe.outfit.checksum)||!id(recipe.appearance.ref)||!id(recipe.appearance.version))return deny("missing-owner-reference");
 if(!contexts.includes(recipe.presentation.context)||!views.includes(recipe.presentation.view)||typeof recipe.presentation.effectVisible!=="boolean")return deny("unapproved-presentation");
 if(!Array.isArray(recipe.abilities)||!Array.isArray(recipe.equipment)||!Array.isArray(recipe.requiredCapabilities)||recipe.abilities.length>16||recipe.equipment.length>16)return deny("invalid-references");
 if(![...recipe.abilities,...recipe.equipment].every(x=>keys(x,allowedReference)&&id(x.ref)&&id(x.version)))return deny("owner-mutation-field");
 if(!recipe.requiredCapabilities.every(id))return deny("invalid-capability");
 const refs=[
 ["character",recipe.character],["form",recipe.form],["outfit",recipe.outfit],["appearance",recipe.appearance],
 ...recipe.abilities.map(x=>["ability",x]),...recipe.equipment.map(x=>["equipment",x])
 ];
 // Visibility is checked BEFORE any field-specific diagnostics are generated.
 for(const [kind,ref] of refs){
   const value=catalog[ref.ref];
   if(value&&value.visibility&&value.visibility!=="public"&&!scopes.includes(value.visibility))return {status:"forbidden",reason:"reference-not-available",actions:[],requiresReview:true};
 }
 const problems=[];let status="compatible";
 const priority={compatible:0,partial:1,unresolved:2,incompatible:3,forbidden:4};
 function degrade(s,why){if(priority[s]>priority[status])status=s;if(!problems.includes(why))problems.push(why);}
 for(const [kind,ref] of refs){
  const entry=catalog[ref.ref];
  if(!entry){degrade("unresolved","owner-reference-unresolved");continue;}
  if(entry.kind!==kind){degrade("incompatible","owner-kind-incompatible");continue;}
  if(entry.version!==ref.version){degrade("unresolved","owner-version-stale");continue;}
  if(entry.rights==="forbidden"||entry.availability==="revoked"){degrade("forbidden","resource-unavailable");continue;}
  if(entry.availability==="missing"){degrade("partial","visual-resource-missing");continue;}
  if(entry.availability==="unknown"){degrade("unresolved","resource-state-unknown");}
 }
 const form=catalog[recipe.form.ref],outfit=catalog[recipe.outfit.ref];
 if(form&&form.kind==="form"){
   if(form.topology!==recipe.form.topology)degrade("unresolved","topology-unresolved");
   if(!Array.isArray(form.capabilities)&&recipe.requiredCapabilities.length)degrade("unresolved","topology-capabilities-unknown");
   else if(Array.isArray(form.capabilities)&&recipe.requiredCapabilities.some(x=>!form.capabilities.includes(x)))degrade("incompatible","topology-incompatible");
 }
 if(outfit&&outfit.kind==="outfit"){
   if(outfit.checksum!==recipe.outfit.checksum)degrade("unresolved","outfit-checksum-stale");
   if(outfit.fit==="incompatible")degrade("incompatible","FGA-fit-incompatible");
   else if(outfit.fit==="unresolved"||outfit.fit===undefined)degrade("unresolved","FGA-fit-unresolved");
   else if(outfit.fit==="partial")degrade("partial","FGA-coverage-partial");
 }
 const semanticHash=hash({character:recipe.character,form:recipe.form,outfit:recipe.outfit,appearance:recipe.appearance,abilities:recipe.abilities,equipment:recipe.equipment});
 return {status,problems:problems.sort(),semanticHash,previewHash:hash([semanticHash,recipe.presentation]),actions:[],requiresReview:true,anatomyChanged:false,mechanicsChanged:false,equipmentChanged:false};
}
function draftModification(input){
 const allowed=["kind","bodyLocation","interfaceReference","sourceEventId","sourceOwnerVersion","transition"];
 if(!keys(input,allowed)||!["graft","implant","symbiote","prosthetic"].includes(input.kind)||![input.bodyLocation,input.interfaceReference,input.sourceEventId].every(id)||!Number.isInteger(input.sourceOwnerVersion)||input.sourceOwnerVersion<1||!["grant","remove","retain","reverse"].includes(input.transition))return {status:"rejected",actions:[]};
 return {status:"owner-resolution-required",routes:["DPL-13","MSWI-07","Character-Actors","D17-Asset","Condition","DPL-05","MIB-12"],actions:[],installed:false,anatomyChanged:false};
}
function socialEvidence(input,role){
 if(!obj(input)||input.mode!=="structured-challenge"||!methods.includes(input.method)||!Array.isArray(input.visible)||!Array.isArray(input.hidden)||!Array.isArray(input.tags))return {status:"rejected",actions:[]};
 return {status:"proposal",method:input.method,visible:input.visible,tags:input.tags,...(role==="gm"?{hidden:input.hidden}:{}),automaticScore:null,automaticModifier:null,actions:[]};
}
const sample=()=>({
 schemaVersion:"APPEARANCE-STUDY-1",
 character:{ref:"character:sample",version:"1"},form:{ref:"form:vespin",version:"2",topology:"top:vespin"},
 outfit:{ref:"outfit:four-arms",version:"3",checksum:"ga:123"},appearance:{ref:"appearance:sample",version:"2"},
 presentation:{context:"neutral",view:"cas_sd_full_body",effectVisible:true},
 abilities:[],equipment:[],requiredCapabilities:["four-arm","wing-clearance"]
});
const sampleCatalog=()=>({
 "character:sample":{kind:"character",version:"1",visibility:"public"},
 "form:vespin":{kind:"form",version:"2",topology:"top:vespin",capabilities:["four-arm","wing-clearance"],visibility:"public"},
 "outfit:four-arms":{kind:"outfit",version:"3",checksum:"ga:123",fit:"compatible",visibility:"public"},
 "appearance:sample":{kind:"appearance",version:"2",visibility:"public"}
});
function runTests(){
 let passed=0;function ok(name,condition){if(!condition)throw Error("FAILED:"+name);passed++;}
 const base=sample(),cat=sampleCatalog(),normal=inspect(base,cat);
 ok("positive",normal.status==="compatible");
 ok("no-mutation",normal.actions.length===0&&!normal.anatomyChanged&&!normal.mechanicsChanged&&!normal.equipmentChanged);
 const lit=sample();lit.presentation.context="low_light";
 ok("context-hash-invariant",inspect(lit,cat).semanticHash===normal.semanticHash);
 ok("context-preview-differs",inspect(lit,cat).previewHash!==normal.previewHash);
 const effect=sample();effect.presentation.effectVisible=false;
 ok("effect-mechanics-invariant",inspect(effect,cat).semanticHash===normal.semanticHash);
 const bad=sample();bad.damage=999;ok("forbidden-root",inspect(bad,cat).status==="rejected");
 const badBody=sample();badBody.form.wingsGranted=true;ok("no-form-grant",inspect(badBody,cat).status==="rejected");
 const badItem=sample();badItem.equipment=[{ref:"x",version:"1",equipped:true}];ok("no-equipment-grant",inspect(badItem,cat).status==="rejected");
 const hidden=sampleCatalog();hidden["appearance:sample"].visibility="gm";const filtered=inspect(sample(),hidden);
 ok("visibility-first",filtered.status==="forbidden"&&!JSON.stringify(filtered).includes("appearance:sample"));
 ok("gm-scope",inspect(sample(),hidden,["gm"]).status==="compatible");
 const stale=sample();stale.character.version="old";ok("owner-version",inspect(stale,cat).status==="unresolved");
 const unknown=sampleCatalog();delete unknown["form:vespin"].capabilities;ok("unknown-anatomy",inspect(sample(),unknown).status==="unresolved");
 const badFit=sampleCatalog();badFit["outfit:four-arms"].fit="incompatible";ok("fit",inspect(sample(),badFit).status==="incompatible");
 const absent=sampleCatalog();delete absent["appearance:sample"];ok("missing-ref",inspect(sample(),absent).status==="unresolved");
 const missingAsset=sampleCatalog();missingAsset["outfit:four-arms"].availability="missing";ok("partial",inspect(sample(),missingAsset).status==="partial");
 const noFit=sampleCatalog();delete noFit["outfit:four-arms"].fit;ok("unknown-fit",inspect(sample(),noFit).status==="unresolved");
 const unknownContext=sample();unknownContext.presentation.context="live-world-weather";ok("world-truth-block",inspect(unknownContext,cat).status==="rejected");
 const augment={kind:"prosthetic",bodyLocation:"left-arm",interfaceReference:"interface:approved",sourceEventId:"event:test",sourceOwnerVersion:1,transition:"grant"};
 ok("modification-proposal",draftModification(augment).status==="owner-resolution-required"&&!draftModification(augment).installed);
 ok("modification-grant-block",draftModification({...augment,bonusStrength:10}).status==="rejected");
 const social={mode:"structured-challenge",method:"gm-determined",visible:["formal"],hidden:["masked judge"],tags:["court-style"]};
 ok("social-private-player",!("hidden" in socialEvidence(social,"player")));
 ok("social-private-gm",socialEvidence(social,"gm").hidden[0]==="masked judge");
 ok("social-no-autoscore",socialEvidence(social,"player").automaticScore===null);
 ok("social-unknown-method",socialEvidence({...social,method:"fashion-bonus"},"gm").status==="rejected");
 return {passed,status:"exploratory-prototype-only",program:"appearance-research"};
}
if(typeof module!=="undefined"&&module.exports)module.exports={inspect,draftModification,socialEvidence,runTests};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(runTests())+"\n");
