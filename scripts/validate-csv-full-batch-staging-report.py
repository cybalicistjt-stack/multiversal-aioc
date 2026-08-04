import json
from pathlib import Path

path = Path('governance/object-system/csv-intake/CSV_FULL_BATCH_STAGING_VALIDATION_REPORT.json')
report = json.loads(path.read_text(encoding='utf-8'))
summary = report['summary']
assert report['workstream'] == '8E-009L19'
assert report['status'] == 'validated-staging-only'
assert summary['datasetsExpected'] == summary['datasetsValidated'] == 20
assert summary['rowsExpected'] == summary['rowsValidated'] == 19199
assert summary['rawRowsPreserved'] == 19199
assert summary['unresolvedManifestsPresent'] == 19199
assert summary['stagingIdsUnique'] is True
assert summary['quarantinedRows'] == 2482
assert summary['canonicalIdsAssigned'] == 0
assert summary['promotionReadyRows'] == 0
assert report['domainState']['mappedDatasets'] == 7
assert report['domainState']['datasetsStillRequiringDomainMappingOrReconciliation'] == 13
assert report['domainState']['promotionAuthorized'] is False
assert report['workflow']['artifact']['sha256'] == '3dccc05cc9c343916aa56b0110ecb924c67827a169469d89ec74d412314fbd90'
print('CSV full batch staging report validated: 20 datasets, 19199 rows, 2482 quarantined, 0 canonical IDs.')
