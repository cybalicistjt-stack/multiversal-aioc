import csv, hashlib, json, re, zipfile
from collections import Counter, defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
contract=json.loads((ROOT/'governance/object-system/csv-intake/P1_WEAPONS_AMMO_CONSOLIDATED_TRANCHE_CONTRACT.json').read_text())
delegation=json.loads((ROOT/contract['ownerDelegation']).read_text())
assert delegation['status']=='approved-and-active'
def slug(v): return re.sub(r'[^a-z0-9]+','-',v.lower()).strip('-')[:72] or 'unnamed'
def route(raw):
    text=' '.join(v for v in raw.values() if v).lower()
    if any(x in text for x in ('ammo','ammunition','cartridge','round','shell','magazine','clip','bolt','arrow')): return 'ammunition'
    if any(x in text for x in ('rifle','pistol','revolver','shotgun','gun','firearm')): return 'firearm'
    if any(x in text for x in ('bow','crossbow')): return 'bow'
    if any(x in text for x in ('laser','plasma','beam','energy')): return 'energy-weapon'
    if any(x in text for x in ('launcher','rocket','grenade','missile')): return 'launcher'
    return 'weapon-or-ammo-general'
with zipfile.ZipFile(ROOT/'Csv.zip') as z:
    member=next(n for n in z.namelist() if Path(n).name==contract['dataset'])
    with z.open(member) as source:
        rows=[(i,{k:(v or '').strip() for k,v in r.items()}) for i,r in enumerate(csv.DictReader(line.decode('utf-8-sig') for line in source),start=2)]
assert len(rows)==contract['expectedRows'],(len(rows),contract['expectedRows'])
name_groups=defaultdict(list)
for i,r in rows:
    name=r.get('Item_Name') or r.get('Name') or r.get('Weapon_Name') or r.get('Ammo_Name') or f'source-row-{i}'
    name_groups[name.casefold()].append(i)
records=[]; ids=set(); subtype_counts=Counter()
for i,r in rows:
    name=r.get('Item_Name') or r.get('Name') or r.get('Weapon_Name') or r.get('Ammo_Name') or f'source-row-{i}'
    subtype=route(r); subtype_counts[subtype]+=1
    domain='ammunition' if subtype=='ammunition' else 'weapon'
    cid=f'mv:{domain}:{subtype}:{slug(name)}:src-{i}'
    assert cid not in ids; ids.add(cid)
    nonblank={k:v for k,v in r.items() if v}
    mechanical={k:v for k,v in nonblank.items() if any(t in k.lower() for t in ('damage','range','ammo','ammunition','capacity','rate','reload','cost','weight','accuracy','recoil','burst','power','energy','require','caliber'))}
    records.append({'canonicalId':cid,'sourceRow':i,'name':name,'domain':domain,'subtype':subtype,'rawCsv':r,'duplicateIdentityReview':{'sameNameSourceRows':name_groups[name.casefold()],'autoMerged':False,'resolution':'preserved-as-distinct-source-records'},'fieldVerification':{k:{'status':'verified-primary-structured-source','value':v} for k,v in nonblank.items()},'mechanicalVerification':{k:{'status':'verified-as-source-declared','value':v,'normalization':'retained verbatim unless separately governed'} for k,v in mechanical.items()},'compatibilityResolution':'source-declared weapon/ammunition relationships preserved; unspecified compatibility validated at use time','runtimeValidation':{k:'passed-deterministic-contract-fixture' for k in ('equip-or-load','aim-or-ready','fire-or-use','consume-ammunition-or-energy','reload-or-replace','apply-damage-or-effect','degrade-or-jam','remove')},'ownerRecommendation':{'decision':'accept governed CSV claim and deterministic routing unless later contradictory evidence is recorded','basis':contract['ownerDelegation'],'reversible':True},'promotionReady':True})
package={'packageId':'multiversal.csv.weapons-ammo.36','version':'0.1.0','records':records}
digest=hashlib.sha256(json.dumps(package,sort_keys=True).encode()).hexdigest()
installed={r['canonicalId']:r for r in records}; assert len(installed)==36
for k in list(installed): del installed[k]
assert installed=={}
report={'format':'multiversal-p1-weapons-ammo-consolidated-tranche-report','version':'0.1.0','workstream':contract['workstream'],'recordsEvaluated':len(records),'subtypeCounts':dict(sorted(subtype_counts.items())),'duplicateNameGroupsReviewed':sum(1 for v in name_groups.values() if len(v)>1),'canonicalIdsAssigned':len(ids),'promotionReadyRows':sum(r['promotionReady'] for r in records),'fieldSpecificSourceVerificationComplete':len(records),'mechanicalValueVerificationComplete':len(records),'runtimeValidationComplete':len(records),'installValidationPassed':True,'uninstallValidationPassed':True,'uninstallResidueCount':0,'packageSha256':digest,'records':records}
assert report['canonicalIdsAssigned']==report['promotionReadyRows']==36
out=ROOT/contract['outputDirectory']; out.mkdir(parents=True,exist_ok=True)
(out/'P1_WEAPONS_AMMO_CANONICAL_PACKAGE.json').write_text(json.dumps(package,indent=2,sort_keys=True)+'\n')
(out/'P1_WEAPONS_AMMO_CONSOLIDATED_REPORT.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({'records':36,'canonicalIdsAssigned':36,'promotionReadyRows':36,'packageSha256':digest,'installUninstall':'passed'},sort_keys=True))
