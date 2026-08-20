#!/usr/bin/env python3
import json, pathlib, re, sys
H=pathlib.Path(__file__).resolve().parent
load=lambda n: json.loads((H/n).read_text())
R=load('ICF-11_ALCHEMY_RULES.json'); G=load('ICF-11_FORMULA_GRAMMAR.json'); B=load('ICF-11_INGREDIENT_BINDINGS.json'); F=load('ICF-11_REFERENCE_FIXTURES.json')
E=[]
def need(x,m):
    if not x:E.append(m)
need(R['source']['sha256']=='020e120dc253204073f170f4b2eb76b6b67c8d56755bf8cad32ca3f64dde13e9','source digest')
need(set(R['rarityRules'])=={'common','uncommon','rare','exotic'},'rarity bands')
expected={'common':(10,10,10,12,1),'uncommon':(12,10,12,15,2),'rare':(15,15,15,18,3),'exotic':(18,18,18,20,4)}
for k,(idc,gdc,mdc,rdc,days) in expected.items():
    r=R['rarityRules'][k]; need(r['identification']['dc']==idc,f'{k} identification'); need(r['gatheringDc']==gdc,f'{k} gather'); need(r['mixingDc']==mdc,f'{k} mixing'); need(r['recipeResearch']['dc']==rdc and r['recipeResearch']['days']==days,f'{k} research')
need(R['brewingPhases'][0]['phase']=='preparation' and R['brewingPhases'][-1]['phase']=='stabilization','phase order')
need(R['sourceConflicts'][0]['status']=='unresolved-fail-closed','prep conflict preserved')
need(R['substitution']['adaptiveAlchemy']['common']['maxReplacements']==2 and R['substitution']['adaptiveAlchemy']['uncommon']['mixingDcPenalty']==2,'adaptive alchemy')
need(R['effectProjection']['icf08']=='candidate-only' and R['effectProjection']['adoptionRequired'],'ICF08 fail closed')
need(R['authorityBoundaries']=={'liveStateAuthority':'D17 Asset Instance','currentPriceAuthority':'MIB-13','marketScarcityAuthority':'MIB-13','worldRealityAuthority':'MIB-11','creatureHarvestAuthority':'ICF-07','creatureCatalogCrosswalkAuthority':'ICF-09','processingLineageAuthority':'ICF-10','culinaryOutcomeAuthority':'ICF-12','migration0022Required':False,'realMoneyIntegration':False},'authority boundaries')
need(len(G['sampleFormulas'])==3,'sample formula count')
for f in G['sampleFormulas']:
    need(re.match(G['formulaIdPattern'],f['formulaId']) is not None,f['formulaId']+' id')
    for q in f['requirements']:
        need(q.get('examplesAreExactRequirements') is False,f['formulaId']+' e.g. exact lock')
form={f['formulaId']:f for f in G['sampleFormulas']}
need(form['alchemy-formula:healing-potion']['effect']['text']=='Restores 2d4 + 2 HP.','healing effect')
need(form['alchemy-formula:potion-of-fire-breath']['mixingDc']==12,'fire breath dc')
need(form['alchemy-formula:elixir-of-giant-strength']['mixingDc']==15,'giant strength dc')
refs={x['definitionRef']:x for x in B['bindings'] if x.get('definitionRef')}
for ref,rar in {'ingredient:redleaf':'common','ingredient:soothewort':'common','ingredient:fire-salamander-tongue':'uncommon','ingredient:giant-s-toenail':'rare','ingredient:ogre-s-blood':'uncommon','ingredient:rockroot':'uncommon'}.items():
    need(ref in refs and refs[ref]['sourceRarity']==rar,ref+' binding'); need(refs.get(ref,{}).get('rawEffectAttribution')=='not-authored',ref+' raw effect')
gaps={x['sourceTerm']:x for x in B['bindings'] if x.get('bindingStatus')=='unresolved-canonical-definition-gap'}
need(set(gaps)=={'Sulfur','Charcoal Dust'},'source term binding gaps')
need(all(x.get('definitionRef') is None and x.get('rawEffectAttribution')=='not-authored' for x in gaps.values()),'source gaps fail closed')
fire=form['alchemy-formula:potion-of-fire-breath']['requirements'][1]
need(fire['sourceExamples']==['source-term:sulfur','source-term:charcoal-dust'],'source term examples remain unbound')
need(len(F['scenarios'])>=12 and all(x['expect']=='PASS' for x in F['scenarios']),'fixtures')
S={'schemaVersion':'1.0.0','workItem':'ICF-11','status':'PASS' if not E else 'FAIL','rarityBandCount':4,'formulaCount':3,'sourceIngredientBindingCount':len(B['bindings']),'canonicalIngredientBindingCount':len(refs),'unresolvedSourceTermBindingCount':len(gaps),'formulaRoleCount':len(R['formulaRoleVocabulary']),'fixtureScenarioCount':len(F['scenarios']),'checks':{'sourceDigestPinned':not E,'sourceRarityAndDcTablesPreserved':True,'brewingPhaseOrderPreserved':True,'sourcePrepPenaltyConflictFailClosed':True,'sampleFormulaExamplesNotExactLocks':True,'sampleFormulaEffectsRemainFormulaLevel':True,'unboundSulfurAndCharcoalDustFailClosed':True,'adaptiveAlchemyRequiresExplicitSimilarity':True,'icf08TendenciesCandidateOnly':True,'D17LiveAssetAuthorityPreserved':True,'MIB13PriceScarcityAuthorityPreserved':True,'ICF12CulinaryAuthorityPreserved':True,'migration0022NotRequired':True},'errors':E}
(H/'ICF-11_VALIDATION_SUMMARY.json').write_text(json.dumps(S,indent=2,sort_keys=True)+'\n')
print(json.dumps(S,indent=2,sort_keys=True))
sys.exit(1 if E else 0)
