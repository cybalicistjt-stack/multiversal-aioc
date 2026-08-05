#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = json.loads((ROOT / 'governance/phase9/P9-03_TECHNOLOGY_AND_SERVICE_DECISION_PACKAGE.json').read_text())
assert p['sourceHandoff'] == 'mv.handoff.phase9.p9-02-v0.2-to-p9-03.0.2.0'
assert len(p['candidates']) == 4
assert sum(d['weight'] for d in p['decisionDimensions']) == 100
assert p['recommendation']['preferredCandidate'] == 'A'
assert p['recommendation']['selectionStatus'] == 'recommended-not-authorized'
assert p['scope']['technologyComparisonAllowed'] is True
for k in ['architectureSelectionAllowed','vendorCommitmentAllowed','spendingAllowed','implementationAllowed']:
    assert p['scope'][k] is False
for c in p['candidates']:
    assert set(c['scores']) == {d['id'] for d in p['decisionDimensions']}
    calculated = sum(c['scores'][d['id']] * d['weight'] for d in p['decisionDimensions'])
    assert calculated == c['weightedScore'], (c['id'], calculated, c['weightedScore'])
assert max(p['candidates'], key=lambda c: c['weightedScore'])['id'] == 'A'
assert p['nextHandoff'] == 'P9-03A_OWNER_TECHNOLOGY_SELECTION_GATE'
payload = {
    'format':'multiversal-p9-03-technology-service-validation',
    'version':'0.1.0',
    'status':'PASS',
    'candidateCount':len(p['candidates']),
    'preferredCandidate':'A',
    'ownerDecisionRequired':True,
    'architectureSelected':False,
    'vendorCommitted':False,
    'spendingAuthorized':False,
    'implementationAuthorized':False
}
canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
payload['artifactSha256']=hashlib.sha256(canonical).hexdigest()
out=ROOT/'out/p9-03-technology-service'
out.mkdir(parents=True,exist_ok=True)
(out/'P9-03_VALIDATION.json').write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
print(json.dumps(payload,sort_keys=True))
