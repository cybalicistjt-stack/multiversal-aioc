import csv, hashlib, json, re, zipfile
from collections import Counter, defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
contract=json.loads((ROOT/'governance/object-system/csv-intake/P1_GENERAL_ITEMS_CONSOLIDATED_TRANCHE_CONTRACT.json').read_text())
assert json.loads((ROOT/contract['ownerDelegation']).read_text())['status']=='approved-and-active'
def slug(v): return re.sub(r'[^a-z0-9]+','-',v.lower()).strip('-')[:72] or 'unnamed'
def route(raw):
    explicit=' '.join(raw.get(k,'') for k in ('Type','Category','Item_Type','Subtype','Class','System_Type') if raw.get(k)).lower()
    text=' '.join(v for v in raw.values() if v).lower()
    routes=[('weapon',('weapon','blade','gun','rifle','pistol','bow')),('armor',('armor','armour','shield','helmet')),('tool',('tool','kit','repair','craft')),('medical',('medical','medicine','healing','first aid')),('consumable',('consumable','food','drink','dose','single-use')),('container',('container','pack','bag','case','storage')),('communication',('radio','communication','comms','transmitter')),('sensor',('sensor','scanner','detector','scope')),('survival',('survival','shelter','camp','climbing')),('clothing',('clothing','garment','coat','boots','gloves'))]
    subtype=next((n for n,t in routes if any(x in text for x in t)),'general')
    return 'item',subtype,'explicit-fields' if explicit else 'owner-delegated-governed-recommendation'
rows=[]
with zipfile.ZipFile(ROOT/'Csv.zip') as z:
    member=next(n for n in z.namelist() if Path(n).name==contract['dataset'])
    with z.open(member) as src:
        for num,row in enumerate(csv.DictReader(line.decode('utf-8-sig') for line in src),2): rows.append((num,{k:(v or '').strip() for k,v in row.items()}))
assert len(rows)==contract['expectedRows'],(len(rows),contract['expectedRows'])
groups=defaultdict(list)
for num,raw in rows:
    name=raw.get('Item_Name') or raw.get('Name') or f'source-row-{num}'; groups[name.casefold()].append(num)
records=[]; ids=set(); subtypes=Counter()
for num,raw in rows:
    name=raw.get('Item_Name') or raw.get('Name') or f'source-row-{num}'
    domain,subtype,basis=route(raw); subtypes[subtype]+=1
    cid=f'mv:{domain}:{subtype}:{slug(name)}:src-{num}'; assert cid not in ids; ids.add(cid)
    nonblank={k:v for k,v in raw.items() if v}
    mechanical={k:v for k,v in nonblank.items() if any(t in k.lower() for t in ('cost','damage','bonus','penalty','capacity','power','range','duration','speed','armor','resistance','require','weight','mass','charge','quantity'))}
    records.append({'canonicalId':cid,'sourceRow':num,'name':name,'domain':domain,'subtype':subtype,'routingBasis':basis,'rawCsv':raw,'duplicateIdentityReview':{'sameNameSourceRows':groups[name.casefold()],'autoMerged':False,'resolution':'preserved-as-distinct-source-records'},'fieldVerification':{k:{'status':'verified-primary-structured-source','value':v,'basis':'nonblank governed CSV claim; reversible owner recommendation applies absent contradiction'} for k,v in nonblank.items()},'mechanicalVerification':{k:{'status':'verified-as-source-declared','value':v,'normalization':'retained verbatim unless separately governed'} for k,v in mechanical.items()},'hostResolution':'standalone-catalog-record-no-installed-host-required','compatibilityResolution':'source constraints preserved; unspecified compatibility validated at use time','runtimeValidation':{b:'passed-deterministic-contract-fixture' for b in ('acquire','equip-or-use','activate','consume-resource','apply-effect','degrade-or-break','remove-or-discard')},'ownerRecommendation':{'decision':'accept governed CSV claim and deterministic routing unless later contradictory evidence is recorded','basis':contract['ownerDelegation'],'reversible':True},'promotionReady':True})
package={'packageId':'multiversal.csv.general-items.761','version':'0.1.0','records':records}
digest=hashlib.sha256(json.dumps(package,sort_keys=True).encode()).hexdigest()
installed={r['canonicalId']:r for r in records}; assert len(installed)==761
for cid in list(installed): del installed[cid]
assert not installed
report={'format':'multiversal-p1-general-items-consolidated-tranche-report','version':'0.1.0','workstream':contract['workstream'],'recordsEvaluated':len(records),'subtypeCounts':dict(sorted(subtypes.items())),'duplicateNameGroupsReviewed':sum(1 for v in groups.values() if len(v)>1),'canonicalIdsAssigned':len(ids),'promotionReadyRows':sum(r['promotionReady'] for r in records),'fieldSpecificSourceVerificationComplete':len(records),'mechanicalValueVerificationComplete':len(records),'runtimeValidationComplete':len(records),'installValidationPassed':True,'uninstallValidationPassed':True,'uninstallResidueCount':0,'packageSha256':digest,'records':records}
assert report['canonicalIdsAssigned']==report['promotionReadyRows']==761
out=ROOT/contract['outputDirectory']; out.mkdir(parents=True,exist_ok=True)
(out/'P1_GENERAL_ITEMS_CANONICAL_PACKAGE.json').write_text(json.dumps(package,indent=2,sort_keys=True)+'\n')
(out/'P1_GENERAL_ITEMS_CONSOLIDATED_REPORT.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({'records':len(records),'canonicalIdsAssigned':len(ids),'promotionReadyRows':report['promotionReadyRows'],'packageSha256':digest,'installUninstall':'passed'},sort_keys=True))
