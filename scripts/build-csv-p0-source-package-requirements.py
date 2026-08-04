import csv
import json
import os
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_P0_SOURCE_PACKAGE_REQUIREMENTS_CONTRACT.json').read_text())
batch = json.loads((ROOT / contract['sourceBatchContract']).read_text())
out = ROOT / contract['outputDirectory']
out.mkdir(parents=True, exist_ok=True)

present_files = defaultdict(list)
for dirpath, dirnames, filenames in os.walk(ROOT):
    rel_dir = Path(dirpath).relative_to(ROOT)
    if rel_dir.parts and rel_dir.parts[0] in {'.git', 'build'}:
        dirnames[:] = []
        continue
    for filename in filenames:
        present_files[filename.casefold()].append(str((rel_dir / filename).as_posix()))

exact_claims = Counter()
alias_claims = Counter()
claim_datasets = defaultdict(set)
rows = 0
source_column_names = {'source_pdf', 'source pdf'}

with zipfile.ZipFile(ROOT / 'Csv.zip') as zf:
    members = {Path(name).name: name for name in zf.namelist() if not name.endswith('/')}
    for spec in batch['datasets']:
        filename = spec['file']
        member = members.get(filename)
        if not member:
            raise SystemExit(f'missing dataset {filename}')
        with zf.open(member) as raw:
            reader = csv.DictReader(line.decode('utf-8-sig') for line in raw)
            fields = reader.fieldnames or []
            source_fields = [field for field in fields if field.strip().lower() in source_column_names]
            if not source_fields:
                raise SystemExit(f'{filename}: no source claim column')
            for row in reader:
                rows += 1
                claims = {(row.get(field) or '').strip() for field in source_fields if (row.get(field) or '').strip()}
                for claim in claims:
                    for part in (segment.strip() for segment in claim.split(';')):
                        if not part:
                            continue
                        lower = part.casefold()
                        is_exact_pdf = lower.endswith('.pdf') and not lower.startswith('original expansion derived') and 'relevant class pdfs' not in lower
                        target = exact_claims if is_exact_pdf else alias_claims
                        target[part] += 1
                        claim_datasets[part].add(filename)

if rows != contract['expectedRows']:
    raise SystemExit(f'row count {rows} != {contract["expectedRows"]}')

requirements = []
for claim, count in sorted(exact_claims.items(), key=lambda item: (-item[1], item[0].casefold())):
    matches = present_files.get(claim.casefold(), [])
    requirements.append({
        'claimedFilename': claim,
        'rowsReferencing': count,
        'datasets': sorted(claim_datasets[claim]),
        'repositoryMatches': matches,
        'status': 'present' if matches else 'missing'
    })

aliases = []
for claim, count in sorted(alias_claims.items(), key=lambda item: (-item[1], item[0].casefold())):
    aliases.append({
        'claim': claim,
        'rowsReferencing': count,
        'datasets': sorted(claim_datasets[claim]),
        'status': 'requires-claim-resolution'
    })

summary = {
    'format': 'multiversal-csv-p0-source-package-requirements',
    'workstream': contract['workstream'],
    'rowsAudited': rows,
    'exactSourceFilenames': len(requirements),
    'presentExactSourceFilenames': sum(item['status'] == 'present' for item in requirements),
    'missingExactSourceFilenames': sum(item['status'] == 'missing' for item in requirements),
    'narrativeOrAliasClaims': len(aliases),
    'pageLevelVerificationReady': all(item['status'] == 'present' for item in requirements) and not aliases,
    'canonicalIdsAssigned': 0,
    'promotionReadyRows': 0
}

(out / 'REQUIRED_SOURCE_FILES.json').write_text(json.dumps(requirements, indent=2, sort_keys=True) + '\n')
(out / 'SOURCE_CLAIM_ALIASES.json').write_text(json.dumps(aliases, indent=2, sort_keys=True) + '\n')
(out / 'SUMMARY.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
print(json.dumps(summary, sort_keys=True))
