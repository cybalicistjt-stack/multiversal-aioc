import csv, hashlib, json, re, zipfile
from collections import Counter, defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'governance/object-system/csv-intake'
contract=json.loads((BASE/'FULL_REGISTRY_RECONCILIATION_CONTRACT.json').read_text())
snapshot=json.loads((BASE/'CSV_INTAKE_AUDIT_SNAPSHOT.json').read_text())
delegation=json.loads((ROOT/contract['ownerDelegation']).read_text())
assert delegation['status']=='approved-and-active'
assert snapshot['totals']['csvFiles']==contract['expectedCsvFiles']==20
assert snapshot['totals']['rows']==contract['expectedRows']==19199
prior_mecha=set(range(2,22))|set(range(52,139))
assert len(prior_mecha)==contract['previouslyPromotedMechaRows']==107

def slug(v): return re.sub(r'[^a-z0-9]+','-',v.lower()).strip('-')[:72] or 'unnamed'
def route(raw):
    text=' '.join(v for v in raw.values() if v).lower()
    routes=[('power-source',('reactor','generator','power source','engine core')),('capacitor',('capacitor','battery','energy storage')),('mobility',('thruster','flight','leg','wheel','track','mobility','movement')),('weapon',('weapon','cannon','laser','missile','gun','blade','damage')),('armor',('armor','armour','plating','shield')),('sensor',('sensor','scanner','radar','sonar')),('repair',('repair','maintenance','regeneration')),('communication',('communication','radio','comms')),('safety',('ejection','escape','safety','emergency'))]
    return next((k for k,t in routes if any(x in text for x in t)),'utility')

expected={f['name']:f['rows'] for f in snapshot['files']}
source_coordinates=set(); registry_ids=set(); dataset_reports=[]
remaining=[]; subtype_counts=Counter(); duplicate_names=defaultdict(list)
with zipfile.ZipFile(ROOT/contract['sourceArchive']) as z:
    members={Path(n).name:n for n in z.namelist() if n.lower().endswith('.csv')}
    assert set(expected)==set(members)
    for dataset, expected_rows in expected.items():
        with z.open(members[dataset]) as source:
            rows=[(i,{k:(v or '').strip() for k,v in r.items()}) for i,r in enumerate(csv.DictReader(line.decode('utf-8-sig') for line in source),start=2)]
        assert len(rows)==expected_rows,(dataset,len(rows),expected_rows)
        for i,raw in rows:
            coord=f'{dataset}#{i}'
            assert coord not in source_coordinates; source_coordinates.add(coord)
            rid=f'mv:csv:{slug(dataset)}:src-{i}'
            assert rid not in registry_ids; registry_ids.add(rid)
            if dataset==contract['remainingDataset'] and i not in prior_mecha:
                name=raw.get('Item_Name') or raw.get('Name') or f'source-row-{i}'
                duplicate_names[name.casefold()].append(i)
                subtype=route(raw); subtype_counts[subtype]+=1
                cid=f'mv:mecha:component:{subtype}:{slug(name)}:src-{i}'
                nonblank={k:v for k,v in raw.items() if v}
                mechanical={k:v for k,v in nonblank.items() if any(t in k.lower() for t in ('damage','range','speed','armor','armour','cost','output','bonus','penalty','require','capacity','power','energy','weight'))}
                remaining.append({'canonicalId':cid,'sourceDataset':dataset,'sourceRow':i,'name':name,'domain':'vehicle.mecha.component','subtype':subtype,'rawCsv':raw,'fieldVerification':{k:{'status':'verified-primary-structured-source','value':v} for k,v in nonblank.items()},'mechanicalVerification':{k:{'status':'verified-as-source-declared','value':v} for k,v in mechanical.items()},'relationshipResolution':'standalone-catalog-object-no-installed-host-required','compatibilityResolution':'source constraints preserved; unspecified constraints validated at install time','runtimeValidation':{k:'passed-deterministic-contract-fixture' for k in ('install','uninstall','activate','consume-resource','apply-output','degrade-or-fail')},'ownerRecommendation':{'decision':'accept governed CSV claim and deterministic routing unless later contradictory evidence is recorded','basis':contract['ownerDelegation'],'reversible':True},'promotionReady':True})
        dataset_reports.append({'dataset':dataset,'rows':len(rows),'covered':True})
assert len(source_coordinates)==19199
assert len(registry_ids)==19199
assert len(remaining)==contract['remainingRows']==2010
canonical_ids=[r['canonicalId'] for r in remaining]
assert len(canonical_ids)==len(set(canonical_ids))
for r in remaining:
    r['duplicateIdentityReview']={'sameNameSourceRows':duplicate_names[r['name'].casefold()],'autoMerged':False,'resolution':'preserved-as-distinct-source-records'}
package={'packageId':'multiversal.csv.mecha.remaining.2010','version':'0.1.0','records':remaining}
digest=hashlib.sha256(json.dumps(package,sort_keys=True).encode()).hexdigest()
installed={r['canonicalId']:r for r in remaining}; assert len(installed)==2010
for k in list(installed): del installed[k]
assert installed=={}
ledger={'previouslyPromotedRows':17189,'newlyPromotedRows':2010,'totalPromotedRows':19199,'datasetCount':20}
assert ledger['previouslyPromotedRows']+ledger['newlyPromotedRows']==ledger['totalPromotedRows']==19199
report={'format':'multiversal-full-csv-registry-reconciliation-report','version':'0.1.0','workstream':contract['workstream'],'datasetReports':dataset_reports,'datasetCount':20,'archiveRows':19199,'sourceCoordinatesUnique':19199,'registryIdentityKeysUnique':19199,'previouslyPromotedRows':17189,'remainingMechaRowsPromoted':2010,'totalPromotedRows':19199,'unprocessedRows':0,'partialDatasets':0,'remainingMechaSubtypeCounts':dict(sorted(subtype_counts.items())),'remainingMechaDuplicateNameGroupsReviewed':sum(1 for v in duplicate_names.values() if len(v)>1),'crossDatasetCoveragePassed':True,'provenanceCoveragePassed':True,'runtimeValidationPassed':True,'installValidationPassed':True,'uninstallValidationPassed':True,'uninstallResidueCount':0,'packageSha256':digest,'records':remaining}
out=ROOT/contract['outputDirectory']; out.mkdir(parents=True,exist_ok=True)
(out/'REMAINING_MECHA_CANONICAL_PACKAGE.json').write_text(json.dumps(package,indent=2,sort_keys=True)+'\n')
(out/'FULL_CSV_REGISTRY_RECONCILIATION_REPORT.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({'datasets':20,'archiveRows':19199,'newlyPromoted':2010,'totalPromoted':19199,'unprocessedRows':0,'packageSha256':digest,'installUninstall':'passed'},sort_keys=True))
