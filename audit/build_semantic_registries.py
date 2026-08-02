#!/usr/bin/env python3
"""Build cumulative semantic-engineering registries from repository diagnostics.

Produces schema, labeling-function, regression, provenance, and experiment
registries. Diagnostics only; never writes canonical game content.
"""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('.')
OUT = Path('semantic-registries')


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return None


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    now=datetime.now(timezone.utc).isoformat()

    schema_records=[]
    for p in sorted(ROOT.glob('schemas/**/*')):
        if p.is_file():
            schema_records.append({'path':str(p),'sha256':sha256(p),'size':p.stat().st_size,'status':'active'})

    label_records=[]
    foundry=read_json(ROOT/'v2/audit-data/semantic-foundry-foundations/semantic-foundry-foundation-index.json') or {}
    for name,count in sorted((foundry.get('labelingFunctionCounts') or foundry.get('negativeSemanticCounts') or {}).items()):
        label_records.append({'id':name,'coverageCount':count,'source':'semantic-foundry-foundations','status':'observed'})

    regression_records=[]
    for p in sorted(ROOT.glob('v2/audit-data/**/*regression*.json')):
        data=read_json(p)
        if data is not None:
            regression_records.append({'path':str(p),'sha256':sha256(p),'summary':{k:data.get(k) for k in ('candidateCount','familyCount','probablePositiveCount','boundaryChallengeCount','anomalyCounts') if isinstance(data,dict)}})

    provenance_records=[]
    for p in sorted(ROOT.glob('v2/audit-data/**/*provenance*.json')):
        data=read_json(p)
        if data is not None:
            provenance_records.append({'path':str(p),'sha256':sha256(p),'inputSha256':data.get('inputSha256') if isinstance(data,dict) else None,'recordCount':data.get('recordCount') if isinstance(data,dict) else None})

    experiment_records=[]
    for p in sorted(ROOT.glob('v2/audit-data/**/*index.json')):
        data=read_json(p)
        if isinstance(data,dict):
            experiment_records.append({
                'id':str(p),
                'generatedAt':data.get('generatedAt'),
                'format':data.get('format'),
                'version':data.get('version'),
                'candidateCount':data.get('candidateCount'),
                'familyCounts':data.get('familyCounts'),
                'sha256':sha256(p),
            })

    registries={
        'schema-registry.json':{'format':'multiversal-schema-registry','version':'1.0.0','generatedAt':now,'records':schema_records},
        'label-registry.json':{'format':'multiversal-label-registry','version':'1.0.0','generatedAt':now,'records':label_records},
        'regression-registry.json':{'format':'multiversal-regression-registry','version':'1.0.0','generatedAt':now,'records':regression_records},
        'provenance-registry.json':{'format':'multiversal-provenance-registry','version':'1.0.0','generatedAt':now,'records':provenance_records},
        'experiment-registry.json':{'format':'multiversal-experiment-registry','version':'1.0.0','generatedAt':now,'records':experiment_records},
    }
    for name,data in registries.items():
        (OUT/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    index={
        'format':'multiversal-semantic-registry-index','version':'1.0.0','generatedAt':now,
        'schemaCount':len(schema_records),'labelCount':len(label_records),'regressionArtifactCount':len(regression_records),
        'provenanceArtifactCount':len(provenance_records),'experimentCount':len(experiment_records),
        'authority':'Diagnostics and registry metadata only; no canonical content modified.'
    }
    (OUT/'semantic-registry-index.json').write_text(json.dumps(index,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(index,indent=2))

if __name__=='__main__':
    main()
