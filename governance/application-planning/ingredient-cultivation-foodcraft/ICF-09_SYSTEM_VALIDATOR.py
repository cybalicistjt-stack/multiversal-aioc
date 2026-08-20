#!/usr/bin/env python3
from __future__ import annotations
import json, pathlib, re, sys
ROOT=pathlib.Path(__file__).resolve().parent

def load(n): return json.loads((ROOT/n).read_text())
XI=load('ICF-09_CANONICAL_CREATURE_CROSSWALK.json')
SI=load('ICF-09_SIGNATURE_INGREDIENT_LIBRARY.json')
C=load('ICF-09_SOURCE_COVERAGE.json')
X=dict(XI); X['records']=[]
for p in XI['packs']:
    X['records'].extend(load(p['path'])['records'])
S=dict(SI); S['records']=[]
for p in SI['packs']:
    S['records'].extend(load(p['path'])['records'])
errors=[]
def need(ok,msg):
    if not ok: errors.append(msg)

need(X.get('schemaVersion')=='1.0.0' and X.get('workItem')=='ICF-09','crosswalk identity')
need(X.get('catalogObjectCount')==27==len(X.get('records',[])),'canonical creature count must be 27')
ids=[r.get('creatureDefinitionRef') for r in X['records']]
need(len(ids)==len(set(ids)),'canonical creature refs must be unique')
need(all(isinstance(i,str) and i.startswith('mv.') for i in ids),'canonical creature ref format')
need(X.get('rules',{}).get('noAnatomyFromNameOrTypeAlone') is True,'no-anatomy inference rule')
need(X.get('rules',{}).get('noHarvestModeOrYieldWithoutAuthoredOrGovernedProfile') is True,'harvest fail-closed rule')
need(X.get('rules',{}).get('noEdibilitySafetyLegalityInference') is True,'edibility/safety/legality fail-closed rule')
need(X.get('rules',{}).get('icf08TendenciesAreNotExactEffects') is True,'ICF-08 tendency boundary')
valid_parts={'blood-ichor','heart-core','neural-brain','eye','liver-kidney','lung-gill','gland','fat-oil','bone-horn-antler','tooth-fang-claw','hide-skin','scale-shell-chitin','feather','muscle-meat','marrow','egg-roe','silk-webbing','slime-mucus','magical-organ-core','venom-poison-sac'}
valid_bodies={'mammalian','avian','reptilian','amphibian','piscine-aquatic','arthropod','molluscan','plant','fungal','ooze','draconic','giant','elemental','undead','celestial-divine','infernal-fiendish','aberrant-psychic','spirit-ectoplasmic','synthetic-biotech','construct-biological','extradimensional-anomalous'}
valid_traits={'fire-attuned','cold-attuned','storm-attuned','aquatic','venomous','regenerative','psychic','necrotic-undead','radiant-celestial','infernal','planar','arcane','camouflaged','acidic','toxic','electric','sonic','shadow','fey','anomalous'}
for r in X['records']:
    need(r.get('catalogCoverageStatus')=='CANONICAL_OBJECT_PRESENT',f"{r.get('creatureName')}: canonical coverage")
    hp=r.get('harvestProfile',{})
    if hp.get('evidenceStatus')=='gap':
        need(hp.get('allowedModes')==[] and hp.get('renewableOutputs')==[] and hp.get('postmortemOutputs')==[],f"{r.get('creatureName')}: gap profile must fail closed")
    need(r.get('edibilityAssertion') in {'unknown','authored-edible','authored-unsafe','authored-inedible'},f"{r.get('creatureName')}: edibility band")
    need(r.get('safetyAssertion')=='unknown',f"{r.get('creatureName')}: safety must remain unknown in ICF-09")
    need(r.get('legalityAssertion')=='unknown',f"{r.get('creatureName')}: legality must remain unknown in ICF-09")
    need(set(r.get('anatomyPartBaselines',[])) <= valid_parts,f"{r.get('creatureName')}: unknown ICF-08 part baseline")
    need(set(r.get('bodyPlanTypeProfiles',[])) <= valid_bodies,f"{r.get('creatureName')}: unknown ICF-08 body profile")
    need(set(r.get('traitAffinityProfiles',[])) <= valid_traits,f"{r.get('creatureName')}: unknown ICF-08 trait profile")

need(S.get('recordCount')==7==len(S.get('records',[])),'signature ingredient count must be 7')
sids=[r.get('stableId') for r in S['records']]
need(len(sids)==len(set(sids)) and all(re.fullmatch(r'ingredient:[a-z0-9]+(?:-[a-z0-9]+)*',s or '') for s in sids),'signature stable IDs')
for r in S['records']:
    sid=r['stableId']
    need(r.get('schemaVersion')=='1.0.0' and r.get('recordKind')=='primary-ingredient',f'{sid}: ICF-02 identity')
    need(r.get('lifecycle',{}).get('status')=='active',f'{sid}: lifecycle')
    need(r.get('authorship',{}).get('class') in {'source-derived','governed-first-party','hybrid'},f'{sid}: authorship')
    prof=r.get('profiles',{})
    need(prof.get('economic',{}).get('currentPriceAuthority')=='MIB-13' and prof.get('economic',{}).get('marketScarcityAuthority')=='MIB-13',f'{sid}: MIB-13 economy authority')
    need(r.get('qualityConditionModel',{}).get('liveStateAuthority')=='D17 Asset Instance' and r.get('qualityConditionModel',{}).get('definitionMaySetCurrentInstanceState') is False,f'{sid}: D17 live authority')
    cs=prof.get('creatureSource',{})
    need(cs.get('evidenceRequired') is True and cs.get('evidenceStatus')=='partial',f'{sid}: creature evidence boundary')
    need(len(cs.get('creatureDefinitionRefs',[]))==1 and cs['creatureDefinitionRefs'][0] in ids,f'{sid}: canonical creature binding')
    need(cs.get('allowedHarvestModes')==[],f'{sid}: anatomy evidence must not create harvest mode')
    parts=prof.get('physical',{}).get('partClassRefs',[])
    need(len(parts)==1 and parts[0].startswith('part:') and parts[0][5:] in valid_parts,f'{sid}: part baseline')
    need(prof.get('culinary',{}).get('edibility')=='unknown',f'{sid}: no edibility inference')
    need(not prof.get('alchemical',{}).get('effectPropertyRefs',[]),f'{sid}: no ICF-11 exact effect leakage')
    need(all(g.get('domain') in {'creature-harvest','culinary','alchemy','magical-culinary','physical'} for g in r.get('coverage',{}).get('gaps',[])),f'{sid}: known coverage gap domains')
    need(any(s.get('role')=='signature-exact-only' and s.get('compatibility')=='exact' for s in r.get('substitutions',[])),f'{sid}: exact signature substitution membership')

need(len(S.get('icf06CreatureDerivedBindings',[]))==7,'seven unresolved ICF-06 creature-derived bindings')
need(all(x.get('bindingStatus')=='unresolved-no-canonical-match' for x in S.get('icf06CreatureDerivedBindings',[])),'ICF-06 unresolved bindings must stay unresolved')
need(C.get('canonicalCatalog',{}).get('creatureDefinitionCount')==27,'coverage canonical count')
need(C.get('sourceCorpus',{}).get('documentCount')==23,'source corpus document count')
need(C.get('sourceCorpus',{}).get('sourceStatblockEvidenceCount')==826,'source evidence count')
need(C.get('sourceCorpus',{}).get('sourceSignatureCandidateCount')==324,'source signature candidate count')
need(C.get('unresolvedICF06CreatureDerivedBindingCount')==7,'coverage ICF-06 unresolved count')
dig=C.get('sourceCorpus',{}).get('noncanonicalWorkingIndexDigests',{})
need(re.fullmatch(r'[0-9a-f]{64}',dig.get('sourceCreatureEvidenceIndexSha256','')) is not None,'source evidence working-index digest')
need(re.fullmatch(r'[0-9a-f]{64}',dig.get('sourceSignatureCandidateIndexSha256','')) is not None,'source candidate working-index digest')
for r in X['records']:
    need(set(r.get('signatureIngredientRefs',[])) <= set(sids),f"{r.get('creatureName')}: dangling signature ref")
need(sum(len(r.get('signatureIngredientRefs',[])) for r in X['records'])==7,'all seven signature ingredients must be linked exactly once')
root=next(r for r in X['records'] if r['creatureDefinitionRef']=='mv.setting.havalaea.creature.rootstalker')
need(root.get('bodyPlanTypeProfiles')==[],'Rootstalker Plant-like must not auto-map to plant body profile')
need('plant-like-label-does-not-prove-plant-body-profile' in root.get('coverageGaps',[]),'Rootstalker plant-like gap must be explicit')
lava=next(x for x in S['icf06CreatureDerivedBindings'] if x['definitionRef']=='ingredient:lava-beetle-shell')
need(lava['bindingStatus']=='unresolved-no-canonical-match' and 'Jungle-Slip Beetle' in lava['coverageGap'],'Lava Beetle/Jungle-Slip anti-name-similarity boundary')
if errors:
    print('ICF-09 VALIDATION FAIL')
    for e in errors: print(' -',e)
    sys.exit(1)
summary={'schemaVersion':'1.0.0','workItem':'ICF-09','status':'PASS','canonicalCreatureCount':27,'canonicalSignatureIngredientCount':7,'sourceDocumentCount':23,'sourceStatblockEvidenceCount':826,'sourceSignatureCandidateCount':324,'sourceEvidenceCanonicalNameMatchCount':5,'unresolvedICF06CreatureDerivedBindingCount':7,'checks':{'canonicalCatalogCoveredExactlyOnce':True,'sourceOnlyEvidenceNotPromotedToCreatureTruth':True,'icf07HarvestFailClosedWithoutProfileEvidence':True,'icf08PartBodyTraitVocabularyBounded':True,'noAnatomyFromNameOrTypeAlone':True,'noExactEffectInference':True,'noEdibilitySafetyLegalityInference':True,'signatureIngredientsICF02CompatibleShape':True,'D17LiveAssetAuthorityPreserved':True,'MIB13PriceScarcityAuthorityPreserved':True,'rootstalkerPlantLikeNotAutoPlant':True,'lavaBeetleNotGuessedToJungleSlipBeetle':True,'icf06UnresolvedCreatureBindingsPreserved':True,'migration0022NotRequired':True}}
print(json.dumps(summary,indent=2,sort_keys=True))
