import csv,json,re,zipfile
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
contract=json.loads((ROOT/'governance/object-system/csv-intake/CSV_CROSS_FILE_IDENTITY_CONFLICT_RECONCILIATION_CONTRACT.json').read_text())
registry=json.loads((ROOT/'governance/object-system/csv-intake/CSV_FULL_DOMAIN_IDENTITY_RECONCILIATION.json').read_text())
out=ROOT/contract['outputDirectory']; out.mkdir(parents=True,exist_ok=True)

def norm(v): return re.sub(r'[^a-z0-9]+',' ',(v or '').lower()).strip()
def first(row,names):
    for n in names:
        if n in row and (row.get(n) or '').strip(): return (row.get(n) or '').strip(),n
rows=[]; groups={}
for g in registry['identityGroups']:
    for f in g['datasets']: groups[f]=g['groupId']
with zipfile.ZipFile(ROOT/'Csv.zip') as zf:
    members={Path(n).name:n for n in zf.namelist() if not n.endswith('/')}
    for filename,group in groups.items():
        member=members.get(filename)
        if not member: raise SystemExit(f'missing {filename}')
        with zf.open(member) as raw:
            reader=csv.DictReader(line.decode('utf-8-sig') for line in raw)
            for rn,row in enumerate(reader,start=2):
                sid,sidcol=first(row,['Catalog_ID','Record_ID','Spell_ID','Vehicle_ID','Item_ID','Weapon_ID','ID','Id']) or (None,None)
                name,namecol=first(row,['Item_Name','Ability_Name','Spell_Name','Item','Weapon','Name','Vehicle_Name','Display_Name']) or (None,None)
                rows.append({'group':group,'dataset':filename,'rowNumber':rn,'sourceId':sid,'sourceIdColumn':sidcol,'name':name,'nameColumn':namecol,'normalizedName':norm(name),'canonicalId':None,'promotionReady':False})
if len(rows)!=contract['expectedRows']: raise SystemExit(f'rows {len(rows)} != {contract["expectedRows"]}')
by_name=defaultdict(list); by_id=defaultdict(list)
for r in rows:
    if r['normalizedName']: by_name[(r['group'],r['normalizedName'])].append(r)
    if r['sourceId']: by_id[(r['dataset'],r['sourceId'])].append(r)
clusters=[]
for (group,name),members_ in sorted(by_name.items()):
    datasets={m['dataset'] for m in members_}
    if len(members_)>1 and len(datasets)>1:
        clusters.append({'clusterId':f'{group}:{name}','identityGroup':group,'normalizedName':name,'members':members_,'decisionState':'unresolved','automaticMerge':False,'verificationNeeded':['source-document-page-verification','mechanical-signature-comparison','variant-and-homonym-review'],'canonicalId':None,'promotionReady':False})
source_id_conflicts=[]
for (dataset,sid),members_ in sorted(by_id.items()):
    if len(members_)>1: source_id_conflicts.append({'dataset':dataset,'sourceId':sid,'members':members_,'decisionState':'conflict','automaticMerge':False})
with (out/'REVIEW_CLUSTERS.jsonl').open('w',encoding='utf-8') as f:
    for c in clusters:f.write(json.dumps(c,ensure_ascii=False,sort_keys=True)+'\n')
with (out/'SOURCE_ID_CONFLICTS.jsonl').open('w',encoding='utf-8') as f:
    for c in source_id_conflicts:f.write(json.dumps(c,ensure_ascii=False,sort_keys=True)+'\n')
summary={'format':'multiversal-csv-cross-file-identity-conflict-reconciliation-report','workstream':'8E-009L29','datasets':len(groups),'rows':len(rows),'reviewClusters':len(clusters),'clusteredRows':sum(len(c['members']) for c in clusters),'sourceIdConflictGroups':len(source_id_conflicts),'canonicalIdsAssigned':0,'promotionReadyRows':0,'automaticMerges':0}
(out/'SUMMARY.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))
