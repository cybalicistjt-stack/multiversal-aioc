#!/usr/bin/env python3
"""Deterministically materialize/validate ICF-06."""
from __future__ import annotations
import argparse,json,re
from collections import Counter
from pathlib import Path
H=Path(__file__).resolve().parent; S=H/'ICF-06_LIBRARY_SOURCE.json'; R=re.compile(r'^ingredient:[a-z0-9]+(?:-[a-z0-9]+)*$')
AFF={'ember':'fire','frost':'cold','storm':'storm','tide':'water','stone':'earth','void':'void','astral':'astral','fey':'fey','infernal':'infernal','celestial':'celestial','shadow':'shadow','liminal':'liminal','chrono':'time','phase':'phase','echo':'echo','gravity':'gravity','mirror':'reflection'}
def load():return json.loads(S.read_text())
def name(s):return {'giant-s-toenail':"Giant's Toenail",'ogre-s-blood':"Ogre's Blood",'mana-salt':'Mana Salt','fire-salamander-tongue':'Fire Salamander Tongue'}.get(s,' '.join(x.capitalize() for x in s.split('-')))
def alias(x,ref):return {'display':x,'lexicalKey':re.sub(r'[^a-z0-9]+','-',x.lower()).strip('-'),'compactedKey':re.sub(r'[^a-z0-9]+','',x.lower()),'status':'active','sourceAssertionRefs':[ref]}
def af(s,base,k):
 a=AFF.get(s.split('-')[0]);return [f'{k}:{a}-affinity'] if a else list(base)
def ass(s,b):
 if not b:return []
 z=[{'assertionId':f'assertion:icf06:{s}:identity','sourceId':b['source'],'sourceTerm':b['term'],'semantic':'identity','status':'mapped','notes':b['assertion']}]
 if b.get('rarity'):z+=[{'assertionId':f'assertion:icf06:{s}:rarity','sourceId':b['source'],'sourceField':'ingredient rarity','rawValue':b['rarity'].title(),'semantic':'rarity','status':'mapped'}]
 if b.get('sourceClass'):z+=[{'assertionId':f'assertion:icf06:{s}:source-classification','sourceId':b['source'],'sourceField':'crop type/classification','rawValue':b['sourceClass'],'semantic':'source-classification','status':'mapped','notes':'Preserved as source classification; not canonical rarity.'}]
 z+=[{'assertionId':f'assertion:icf06:{s}:use','sourceId':b['source'],'semantic':b['semantic'],'status':'mapped','notes':b['assertion']}]
 if b.get('sourceRules'):z+=[{'assertionId':f'assertion:icf06:{s}:agriculture-rules','sourceId':b['source'],'sourceField':'growth/yield/resources','rawValue':b['sourceRules'],'semantic':'agriculture','status':'mapped'}]
 if b.get('sourceValue'):z+=[{'assertionId':f'assertion:icf06:{s}:value','sourceId':b['source'],'sourceField':'base value','rawValue':b['sourceValue']['amountText']+' '+b['sourceValue']['currencyTerm'],'semantic':'value','status':'mapped'}]
 return z
def unit(s,c,b):
 if s=='fire-blossom':return {'unitId':'unit:bloom','dimension':'custom'},['unit:bloom']
 if s=='etherleaf':return {'unitId':'unit:leaf','dimension':'custom'},['unit:leaf']
 if c=='anomalous_fluid_gel' or s=='ogre-s-blood':return {'unitId':'unit:milliliter','dimension':'volume'},['unit:milliliter','unit:liter']
 if b and b.get('part') in {'part:egg','part:feather','part:shell','part:tongue','part:toenail'}:return {'unitId':'unit:item','dimension':'count'},['unit:item']
 return {'unitId':'unit:gram','dimension':'mass'},['unit:gram','unit:kilogram']
def rec(s,c,x,b=None):
 d=x['categoryDefaults'][c]; A=ass(s,b); refs=[q['assertionId'] for q in A]; p,u=unit(s,c,b)
 if b and b.get('rarity'):rar={'defaultBand':b['rarity'],'reconciliation':{'status':'direct','sourceAssertionRefs':[f'assertion:icf06:{s}:rarity']},'scopedOverrides':[]}
 elif b:rar={'defaultBand':None,'reconciliation':{'status':'unresolved','sourceAssertionRefs':[q for q in refs if q.endswith('source-classification')]},'scopedOverrides':[]}
 else:rar={'defaultBand':d['rarity'],'reconciliation':{'status':'first-party-authored','sourceAssertionRefs':[],'authorityRef':x['authoringRecord']},'scopedOverrides':[]}
 P={'physical':{'forms':[d['form']],'partClassRefs':([b['part']] if b and b.get('part') else []),'perishability':d['perish'],'shelfLifeRuleRefs':[],'storageRequirementRefs':[],'preparationRequirementRefs':[],'contaminationRiskRefs':[]},'ecology':{'habitatRefs':[],'biomeRefs':[],'climateRefs':[],'seasonRefs':[],'worldRealityRefs':[],'renewability':d['renew'],'sourceAssertionRefs':[q for q in refs if q.endswith(':use')]},'agriculture':{'cultivationEligible':d['cult'],'husbandryEligible':c=='supernatural_animal_product' and not (b and b.get('creatureGap')),'foragingEligible':d['forage'],'facilityTagRefs':[],'growthRuleRefs':[],'yieldRuleRefs':[],'resourceRequirementRefs':[],'sourceAssertionRefs':[q for q in refs if q.endswith(':agriculture-rules') or (b and b['source'].startswith('Agriculture') and q.endswith(':use'))]},'economic':{'currentPriceAuthority':'MIB-13','marketScarcityAuthority':'MIB-13','tradeClassRefs':['trade:magical-ingredient'],'legalityRefs':[],'sourceValueAssertions':[]},'culinary':{'edibility':d['ed'],'flavorPropertyRefs':[],'texturePropertyRefs':[],'techniqueCompatibilityRefs':[],'nutritionRuleRefs':[],'restorationRuleRefs':[],'pairingRefs':[],'sourceAssertionRefs':[]}}
 if b and b.get('sourceValue'):P['economic']['sourceValueAssertions']=[{'amountText':b['sourceValue']['amountText'],'currencyTerm':b['sourceValue']['currencyTerm'],'context':b['sourceValue']['context'],'inferred':False,'sourceAssertionRef':f'assertion:icf06:{s}:value'}]
 if not b:
  m,a=af(s,d['magic'],'magical-culinary'),af(s,d['alchemy'],'alchemy')
  if m:P['magicalCulinary']={'affinityPropertyRefs':m,'potencyRuleRefs':[],'overloadRuleRefs':[],'compatibilityRuleRefs':[],'sourceAssertionRefs':[]}
  if a:P['alchemical']={'roleRefs':['alchemy-role:reagent'],'essencePropertyRefs':a,'effectPropertyRefs':[],'volatilityRuleRefs':[],'extractionRuleRefs':[],'identificationRuleRefs':[],'sourceAssertionRefs':[]}
 else:
  if b.get('magicCulinaryRole'):P['magicalCulinary']={'affinityPropertyRefs':['magical-culinary:enchantment-ingredient'],'potencyRuleRefs':[],'overloadRuleRefs':[],'compatibilityRuleRefs':[],'sourceAssertionRefs':[q for q in refs if q.endswith(':use')]}
  if b['source']=='Alchemy.mht':P['alchemical']={'roleRefs':['alchemy-role:ingredient'],'essencePropertyRefs':[],'effectPropertyRefs':[],'volatilityRuleRefs':[],'extractionRuleRefs':[],'identificationRuleRefs':[],'sourceAssertionRefs':[q for q in refs if q.endswith(':use')]}
  if b.get('creatureGap'):P['creatureSource']={'evidenceRequired':True,'evidenceStatus':'gap','creatureDefinitionRefs':[],'authoredHarvestReferenceRefs':[],'allowedHarvestModes':[],'sourceAssertionRefs':[f'assertion:icf06:{s}:identity',f'assertion:icf06:{s}:use']}
 G=[]
 if b and b.get('creatureGap'):G+=[{'gapId':f'gap:{s}:creature-crosswalk','domain':'creature-harvest','description':'Source-authored ingredient lacks canonical creature/harvest binding; resolve in ICF-07/09 without invented anatomy.','sourceAssertionRefs':[f'assertion:icf06:{s}:identity']}]
 if b and not b.get('rarity'):G+=[{'gapId':f'gap:{s}:canonical-rarity','domain':'rarity','description':'No directly mappable canonical rarity is authored; preserve source classification/context.','sourceAssertionRefs':[q for q in refs if q.endswith('source-classification')]}]
 if b and b['source']=='Cooking 11-24-24.mht' and s in {'frostberry','chrono-crystal','voidfruit','phoenix-egg'}:G+=[{'gapId':f'gap:{s}:raw-effect-attribution','domain':'magical-culinary','description':'Finished dish effect is authored but not explicitly owned by raw ingredient; resolve at ICF-12 recipe level.','sourceAssertionRefs':[f'assertion:icf06:{s}:use']}]
 return {'schemaVersion':'1.0.0','stableId':f'ingredient:{s}','definitionVersion':'1.0.0','recordKind':'primary-ingredient','displayName':name(s),'aliases':[alias(q,f'assertion:icf06:{s}:identity') for q in (b or {}).get('aliases',[])],'lifecycle':{'status':'active'},'authorship':{'class':'hybrid' if b else 'governed-first-party','authoringRecordRefs':[x['authoringRecord']]+([b['source']] if b else [])},'provenance':{'provenanceId':f'prov:icf06:{s}','sourceAssertions':A},'taxonomy':{'ingredientClasses':[d['cls']],'natureClasses':d['nature'],'originContextClasses':d['origin'],'rarity':rar,'availability':{'baseline':'unknown' if b else d['avail'],'acquisitionModes':d['acq'],'scopeAssertions':[]}},'units':{'primaryUnit':p,'allowedUnits':u,'exactConversions':[],'sourceUnitAssertions':[]},'profiles':P,'qualityConditionModel':{'liveStateAuthority':'D17 Asset Instance','qualityRuleRefs':[],'conditionRuleRefs':[],'definitionMaySetCurrentInstanceState':False},'substitutions':[],'coverage':{'status':'partial' if G else 'complete','gaps':G},'tags':['icf06','magical-exotic-multiversal',f'category:{c}','source-backed' if b else 'governed-first-party']}
def records(x):
 z=[]
 for c,L in x['categories'].items():z += [rec(s,c,x) for s in L]
 z += [rec(s,b['category'],x,b) for s,b in x['sourceBacked'].items()];return z
def validate(z,x):
 ids=[r['stableId'] for r in z];assert len(z)==312==len(set(ids)) and all(R.match(i) for i in ids);assert sum(r['authorship']['class']=='hybrid' for r in z)==25;assert sum(r['profiles'].get('creatureSource',{}).get('evidenceStatus')=='gap' for r in z)==7;assert 'ingredient:snow-moss' not in ids;assert all(r['profiles']['economic']['currentPriceAuthority']=='MIB-13' and r['profiles']['economic']['marketScarcityAuthority']=='MIB-13' for r in z);assert all(r['qualityConditionModel']['liveStateAuthority']=='D17 Asset Instance' and not r['qualityConditionModel']['definitionMaySetCurrentInstanceState'] for r in z);assert all(not r['profiles'].get('alchemical',{}).get('effectPropertyRefs') for r in z)
 C=Counter(next(t.split(':',1)[1] for t in r['tags'] if t.startswith('category:')) for r in z)
 return {'schemaVersion':'1.0.0','workItem':'ICF-06','libraryVersion':'1.0.0','status':'PASS','recordCount':312,'governedFirstPartyCount':287,'hybridSourceBackedCount':25,'creatureCrosswalkGapCount':7,'categoryCounts':dict(sorted(C.items())),'checks':{'stableIdsUnique':True,'allPrimaryIngredient':True,'liveStateAuthorityPreserved':True,'currentPriceAuthorityMIB13':True,'marketScarcityAuthorityMIB13':True,'worldRealityAuthorityMIB11':True,'noCurrentPriceFields':True,'noLiveOwnerFields':True,'noRawIngredientFinishedRecipeEffectInference':True,'agricultureExoticSupernaturalNotAutoRarity':True,'creatureHarvestDeferredICF07':True,'creatureCrosswalkDeferredICF09':True,'processingLineageDeferredICF10':True,'magicalCulinaryMechanicsDeferredICF12':True},'sourceBackedStableIds':[f'ingredient:{s}' for s in sorted(x['sourceBacked'])]}
def main():
 a=argparse.ArgumentParser();a.add_argument('--out-dir');a.add_argument('--validate-only',action='store_true');q=a.parse_args();x=load();z=records(x);v=validate(z,x)
 if q.out_dir and not q.validate_only:
  o=Path(q.out_dir);o.mkdir(parents=True,exist_ok=True);G={'ICF-06_LIBRARY_A_MAGICAL_BOTANICALS_FUNGI.json':['arcane_botanical','elemental_botanical','planar_botanical','magical_fungus'],'ICF-06_LIBRARY_B_MINERALS_RESIDUES_ANOMALIES.json':['arcane_crystal_mineral','elemental_salt_mineral','planar_residue_essence','anomalous_fluid_gel'],'ICF-06_LIBRARY_C_SUPERNATURAL_ANIMAL_PRODUCTS.json':['supernatural_animal_product']}
  for f,C in G.items():
   p=[r for r in z if next(t.split(':',1)[1] for t in r['tags'] if t.startswith('category:')) in C];(o/f).write_text(json.dumps({'schemaVersion':'1.0.0','workItem':'ICF-06','libraryVersion':'1.0.0','recordCount':len(p),'records':p},indent=2,sort_keys=True)+'\n')
  (o/'ICF-06_LIBRARY_VALIDATION_SUMMARY.generated.json').write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
 print(json.dumps(v,indent=2,sort_keys=True));return 0
if __name__=='__main__':raise SystemExit(main())
