import csv, json, re, zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
contract=json.loads((ROOT/'governance/object-system/csv-intake/CSV_MIXED_HAZARD_DOMAIN_BATCH_CONTRACT.json').read_text())
out=ROOT/contract['outputDirectory']; out.mkdir(parents=True,exist_ok=True)
def slug(v): return re.sub(r'[^a-z0-9]+','-',(v or '').lower()).strip('-') or 'unnamed'
def route(filename,row):
    if filename.startswith('expanded_bases'):
        value=(row.get('Record Type') or '').lower()
        if 'material' in value: return 'items','item.material.crafting-resource'
        if 'homestead' in value: return 'homestead','homestead'
        if 'base' in value: return 'base','base'
        return 'facility','facility'
    value=(row.get('Record_Type') or '').lower()
    if 'trap' in value: return 'items','item.trap'
    if 'deploy' in value: return 'items','item.deployable'
    return 'hazards','hazard'
summary={'format':'multiversal-csv-domain-batch-summary','workstream':contract['workstream'],'datasets':[],'totalRows':0,'canonicalIdsAssigned':0,'promotionReadyRows':0}
with zipfile.ZipFile(ROOT/'Csv.zip') as zf:
    members={Path(n).name:n for n in zf.namelist() if not n.endswith('/')}
    for spec in contract['datasets']:
        fn=spec['file']; member=members.get(fn)
        if not member: raise SystemExit(f'missing {fn}')
        path=out/f'{Path(fn).stem}.jsonl'; count=0; routes={}
        with zf.open(member) as raw, path.open('w',encoding='utf-8') as target:
            reader=csv.DictReader(line.decode('utf-8-sig') for line in raw); fields=reader.fieldnames or []
            if spec['identityColumn'] not in fields: raise SystemExit(f'{fn} missing {spec["identityColumn"]}')
            for row_number,row in enumerate(reader,start=2):
                count+=1; identity=(row.get(spec['identityColumn']) or '').strip(); domain,routing=route(fn,row); routes[routing]=routes.get(routing,0)+1
                record={'stagingId':f'mvstg:{slug(Path(fn).stem)}:{row_number}:{slug(identity)}','dataset':fn,'rowNumber':row_number,'domain':domain,'templateRouting':routing,'routingEvidence':'inferred-classification','identity':{'sourceIdentity':identity or None,'canonicalId':None},'rawSource':row,'unmappedColumns':fields,'provenance':{'archive':'Csv.zip','dataset':fn,'rowNumber':row_number},'unresolvedManifest':['source-document-page-verification','field-level-provenance','identity-reconciliation','domain-template-validation','owner-promotion-approval'],'validationState':'domain-staged-unverified','promotionReady':False}
                target.write(json.dumps(record,ensure_ascii=False,sort_keys=True)+'\n')
        if count!=spec['rows']: raise SystemExit(f'{fn}: {count} != {spec["rows"]}')
        summary['datasets'].append({'file':fn,'rows':count,'routes':routes,'output':str(path.relative_to(ROOT))}); summary['totalRows']+=count
if summary['totalRows']!=contract['expectedRows']: raise SystemExit('row total mismatch')
(out/'SUMMARY.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))
