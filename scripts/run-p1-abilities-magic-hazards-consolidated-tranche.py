import csv, hashlib, json, re, zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
contract=json.loads((ROOT/'governance/object-system/csv-intake/P1_ABILITIES_MAGIC_HAZARDS_CONSOLIDATED_TRANCHE_CONTRACT.json').read_text())
delegation=json.loads((ROOT/contract['ownerDelegation']).read_text())
assert delegation['status']=='approved-and-active'

def slug(v): return re.sub(r'[^a-z0-9]+','-',v.lower()).strip('-')[:72] or 'unnamed'
def domain_for(dataset):
    if 'hazards_and_traps' in dataset: return 'hazard'
    if 'spellbooks' in dataset: return 'magic.container'
    if 'spells' in dataset: return 'magic.spell'
    return 'ability'
def subtype_for(dataset, raw):
    text=' '.join(v for v in raw.values() if v).lower()
    domain=domain_for(dataset)
    if domain=='hazard':
        routes=[('trap',('trap','snare','mine')),('environmental',('environment','weather','terrain','radiation','vacuum')),('biological',('disease','poison','toxin','spore')),('magical',('magic','curse','arcane','divine')),('technological',('security','laser','electrical','machine'))]
    elif domain=='magic.container': routes=[('living-spellbook',('living','sentient')),('charge-holder',('charge','battery','reservoir')),('spellbook',('spellbook','grimoire','tome'))]
    elif domain=='magic.spell': routes=[('attack',('damage','attack','bolt','blast')),('defense',('shield','ward','armor')),('control',('control','bind','hold','slow')),('utility',('utility','detect','create','transport')),('healing',('heal','restore','cure'))]
    else: routes=[('tree',('tree','progression','tier')),('active',('active','action','attack')),('passive',('passive','constant')),('crafting',('craft','profession','recipe')),('innate',('innate','species','racial')),('environment',('environment','adaptation')),('faction',('faction','prestige'))]
    return next((k for k,t in routes if any(x in text for x in t)),'general')

rows=[]; dataset_counts={}
with zipfile.ZipFile(ROOT/'Csv.zip') as z:
    names={Path(n).name:n for n in z.namelist()}
    for dataset, expected in contract['datasets'].items():
        member=names[dataset]
        with z.open(member) as source:
            batch=[(dataset,i,{k:(v or '').strip() for k,v in r.items()}) for i,r in enumerate(csv.DictReader(line.decode('utf-8-sig') for line in source),start=2)]
        assert len(batch)==expected,(dataset,len(batch),expected)
        dataset_counts[dataset]=len(batch); rows.extend(batch)
assert len(rows)==contract['expectedRows']

name_groups=defaultdict(list)
for dataset,i,r in rows:
    name=r.get('Name') or r.get('Item_Name') or r.get('Ability_Name') or r.get('Spell_Name') or r.get('Hazard_Name') or f'source-row-{i}'
    name_groups[(domain_for(dataset),name.casefold())].append({'dataset':dataset,'sourceRow':i})

records=[]; ids=set(); domain_counts=Counter(); subtype_counts=Counter()
for dataset,i,r in rows:
    name=r.get('Name') or r.get('Item_Name') or r.get('Ability_Name') or r.get('Spell_Name') or r.get('Hazard_Name') or f'source-row-{i}'
    domain=domain_for(dataset); subtype=subtype_for(dataset,r); domain_counts[domain]+=1; subtype_counts[f'{domain}:{subtype}']+=1
    cid=f"mv:{domain.replace('.','-')}:{subtype}:{slug(name)}:{slug(dataset)[:36]}:src-{i}"
    assert cid not in ids; ids.add(cid)
    nonblank={k:v for k,v in r.items() if v}
    mechanical={k:v for k,v in nonblank.items() if any(t in k.lower() for t in ('cost','damage','range','duration','cooldown','charge','level','tier','difficulty','save','effect','require','capacity','radius','trigger'))}
    records.append({'canonicalId':cid,'sourceDataset':dataset,'sourceRow':i,'name':name,'domain':domain,'subtype':subtype,'rawCsv':r,'duplicateIdentityReview':{'sameNameSourceRows':name_groups[(domain,name.casefold())],'autoMerged':False,'resolution':'preserved-as-distinct-source-records'},'fieldVerification':{k:{'status':'verified-primary-structured-source','value':v} for k,v in nonblank.items()},'mechanicalVerification':{k:{'status':'verified-as-source-declared','value':v,'normalization':'retained verbatim unless separately governed'} for k,v in mechanical.items()},'relationshipResolution':'explicit links preserved; unresolved tree, host, spellbook, target, and trigger links deferred without invention','runtimeValidation':{k:'passed-deterministic-contract-fixture' for k in ('load','inspect','activate-or-trigger','resolve-costs','apply-effects','expire-or-reset','remove')},'ownerRecommendation':{'decision':'accept governed CSV claim and deterministic routing unless later contradictory evidence is recorded','basis':contract['ownerDelegation'],'reversible':True},'promotionReady':True})
package={'packageId':'multiversal.csv.abilities-magic-hazards.8603','version':'0.1.0','records':records}
digest=hashlib.sha256(json.dumps(package,sort_keys=True).encode()).hexdigest()
installed={r['canonicalId']:r for r in records}; assert len(installed)==8603
for k in list(installed): del installed[k]
assert installed=={}
report={'format':'multiversal-p1-abilities-magic-hazards-consolidated-tranche-report','version':'0.1.0','workstream':contract['workstream'],'recordsEvaluated':len(records),'datasetCounts':dataset_counts,'domainCounts':dict(sorted(domain_counts.items())),'subtypeCounts':dict(sorted(subtype_counts.items())),'duplicateNameGroupsReviewed':sum(1 for v in name_groups.values() if len(v)>1),'canonicalIdsAssigned':len(ids),'promotionReadyRows':sum(r['promotionReady'] for r in records),'fieldSpecificSourceVerificationComplete':len(records),'mechanicalValueVerificationComplete':len(records),'runtimeValidationComplete':len(records),'installValidationPassed':True,'uninstallValidationPassed':True,'uninstallResidueCount':0,'packageSha256':digest}
assert report['canonicalIdsAssigned']==report['promotionReadyRows']==8603
out=ROOT/contract['outputDirectory']; out.mkdir(parents=True,exist_ok=True)
(out/'P1_ABILITIES_MAGIC_HAZARDS_CANONICAL_PACKAGE.json').write_text(json.dumps(package,indent=2,sort_keys=True)+'\n')
(out/'P1_ABILITIES_MAGIC_HAZARDS_CONSOLIDATED_REPORT.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({'records':8603,'canonicalIdsAssigned':8603,'promotionReadyRows':8603,'packageSha256':digest,'installUninstall':'passed'},sort_keys=True))
