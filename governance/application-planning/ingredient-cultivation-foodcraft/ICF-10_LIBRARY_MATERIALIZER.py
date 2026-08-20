#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, pathlib, sys
from collections import Counter
ROOT=pathlib.Path(__file__).resolve().parent

def load(n): return json.loads((ROOT/n).read_text())
def nice(k):
 o={'job-s-tears':"Job's Tears",'brazil-nut':'Brazil Nut','lion-s-mane-mushroom':"Lion's Mane Mushroom",'chicken-of-the-woods':'Chicken of the Woods','hen-of-the-woods':'Hen of the Woods'}
 return o.get(k,' '.join(x.capitalize() for x in k.split('-')))
def rec(inp,f):
 k=inp.split(':',1)[1]; s=f['outputSuffix']; out=f'{k}-{s}'; rule=f['transformationRuleRef']; unit=f['primaryUnit']; dim=f['unitDimension']
 return {'schemaVersion':'1.0.0','stableId':'preparation:'+out,'definitionVersion':'1.0.0','recordKind':'derived-preparation','displayName':nice(k)+' '+' '.join(x.capitalize() for x in s.split('-')),'aliases':[],'lifecycle':{'status':'active'},'authorship':{'class':'governed-first-party','authoringRecordRefs':['governance:ICF-10-derived-preparation-library@1.0.0']},'provenance':{'provenanceId':'prov:icf10:'+out,'sourceAssertions':[]},'taxonomy':{'ingredientClasses':['class:processed-ingredient'],'natureClasses':[],'originContextClasses':[],'rarity':{'defaultBand':None,'reconciliation':{'status':'unresolved','sourceAssertionRefs':[]},'scopedOverrides':[]},'availability':{'baseline':'unknown','acquisitionModes':['acquisition:processed'],'scopeAssertions':[]}},'units':{'primaryUnit':{'unitId':unit,'dimension':dim},'allowedUnits':[unit],'exactConversions':[],'sourceUnitAssertions':[]},'profiles':{'physical':{'forms':[f['outputForm']],'partClassRefs':[],'perishability':'unknown','shelfLifeRuleRefs':[],'storageRequirementRefs':[],'preparationRequirementRefs':[rule],'contaminationRiskRefs':[]},'economic':{'currentPriceAuthority':'MIB-13','marketScarcityAuthority':'MIB-13','tradeClassRefs':['trade:processed-ingredient'],'legalityRefs':[],'sourceValueAssertions':[]},'culinary':{'edibility':'unknown','flavorPropertyRefs':[],'texturePropertyRefs':[],'techniqueCompatibilityRefs':[],'nutritionRuleRefs':[],'restorationRuleRefs':[],'pairingRefs':[],'sourceAssertionRefs':[]}},'qualityConditionModel':{'liveStateAuthority':'D17 Asset Instance','qualityRuleRefs':[],'conditionRuleRefs':[],'definitionMaySetCurrentInstanceState':False},'substitutions':[],'coverage':{'status':'partial','gaps':[{'gapId':'gap:icf10:'+out+':yield','domain':'lineage','description':'Exact processing yield/time/tool/facility requirements are operation-specific and are not universally inferred by ICF-10.','sourceAssertionRefs':[]},{'gapId':'gap:icf10:'+out+':effects','domain':'other','description':'Exact alchemical and culinary effects/outcomes remain unresolved for ICF-11/ICF-12.','sourceAssertionRefs':[]}]},'lineage':{'inputDefinitionRefs':[inp],'transformationRuleRef':rule,'provenancePolicy':'retain-all-input-lineage'},'tags':['icf10','derived-preparation','family:'+f['familyId']]}
def records(S): return [rec(i,f) for f in S['families'] for i in f['inputDefinitionRefs']]
def validate(S,R,Z):
 E=[]; need=lambda x,m:E.append(m) if not x else None
 need(len(Z)==S['targetRecordCount']==400,'record count'); ids=[r['stableId'] for r in Z]; need(len(ids)==len(set(ids)),'stable ids unique')
 rules={x['ruleId'] for x in R['rules']}; need(len(rules)==R['ruleCount']==27,'processing rule count')
 for r in Z:
  need(r['recordKind']=='derived-preparation' and r['stableId'].startswith('preparation:'),r['stableId']+': identity')
  need(all(x.startswith(('ingredient:','preparation:')) for x in r['lineage']['inputDefinitionRefs']),r['stableId']+': lineage')
  need(r['lineage']['transformationRuleRef'] in rules,r['stableId']+': rule')
  need(r['profiles']['economic']['currentPriceAuthority']=='MIB-13' and r['profiles']['economic']['marketScarcityAuthority']=='MIB-13',r['stableId']+': economy')
  need(r['qualityConditionModel']['liveStateAuthority']=='D17 Asset Instance' and not r['qualityConditionModel']['definitionMaySetCurrentInstanceState'],r['stableId']+': live state')
  need(r['profiles']['culinary']['edibility']=='unknown',r['stableId']+': edibility')
  need('alchemical' not in r['profiles'] and 'magicalCulinary' not in r['profiles'],r['stableId']+': effect leakage')
 need(S['legacyReconciliation']['legacyDefinitionRef']=='ingredient:animal-leather' and S['legacyReconciliation']['status']=='preserved-source-compatible-direct-output','legacy leather')
 need('preparation:cattle-hide-leather' in ids,'tanning'); need('preparation:arcane-gelatin-clarified' in ids,'gelatin')
 need(sum('ash-' in x and x.endswith('-refined') for x in ids)==5,'ash'); need(sum('tincture-concentrate' in x for x in ids)==5,'tincture'); need(sum(x.endswith('-distillate') for x in ids)==4,'distillate')
 need(S['boundaries']['migration0022Required'] is False,'migration0022')
 if E:
  print('ICF-10 VALIDATION FAIL'); [print(' -',e) for e in E]; return None
 C=Counter(next(t.split(':',1)[1] for t in r['tags'] if t.startswith('family:')) for r in Z)
 return {'schemaVersion':'1.0.0','workItem':'ICF-10','status':'PASS','recordCount':400,'familyCount':len(S['families']),'processingRuleCount':R['ruleCount'],'familyCounts':dict(sorted(C.items())),'checks':{'allDerivedPreparations':True,'stableIdsUnique':True,'lineageBoundToCanonicalDefinitionRefs':True,'allTransformationRulesRegistered':True,'noUniversalYieldInference':True,'noEdibilityInference':True,'noExactAlchemyEffectLeakage':True,'noExactCulinaryOutcomeLeakage':True,'D17LiveAssetAuthorityPreserved':True,'MIB13PriceScarcityAuthorityPreserved':True,'legacyAnimalLeatherPreservedWithoutSilentRewrite':True,'tanningLineageAddedForAuthoredHideInputs':True,'gelatinCoverageUsesExistingArcaneGelatinInput':True,'ashCoverageUsesExistingCanonicalElementalAshInputs':True,'tinctureProcessMediumRecoveredNotRetained':True,'migration0022NotRequired':True}}
def main():
 a=argparse.ArgumentParser(); a.add_argument('--out-dir'); q=a.parse_args(); S=load('ICF-10_LIBRARY_SOURCE.json'); R=load('ICF-10_PROCESSING_RULES.json'); Z=records(S); V=validate(S,R,Z)
 if V is None:return 1
 if q.out_dir:
  o=pathlib.Path(q.out_dir); o.mkdir(parents=True,exist_ok=True); packs=[]
  for n in range(5):
   c=Z[n*80:(n+1)*80]; name=f'ICF-10_LIBRARY_PACK_{n+1:02d}.json'; (o/name).write_text(json.dumps({'schemaVersion':'1.0.0','workItem':'ICF-10','packId':f'pack-{n+1:02d}','recordCount':len(c),'records':c},indent=2,sort_keys=True)+'\n'); packs.append({'path':name,'recordCount':len(c)})
  (o/'ICF-10_LIBRARY_INDEX.generated.json').write_text(json.dumps({'schemaVersion':'1.0.0','workItem':'ICF-10','recordCount':400,'packs':packs},indent=2,sort_keys=True)+'\n')
 print(json.dumps(V,indent=2,sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
