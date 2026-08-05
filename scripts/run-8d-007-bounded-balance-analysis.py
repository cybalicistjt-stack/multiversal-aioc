#!/usr/bin/env python3
import hashlib, json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT/'governance/balance/8D-007_GOLDEN_CORPUS_MANIFEST.json').read_text())
contract = json.loads((ROOT/'governance/balance/8D-007_PEER_GROUP_TARGET_BAND_CONTRACT.json').read_text())
scenarios = json.loads((ROOT/'governance/balance/8D-007_RUNTIME_SCENARIO_REGISTRY.json').read_text())
scenario_by_id = {s['id']: s for s in scenarios['scenarios']}
recon = '112ef5116b4090cc266eefe36e1c539b6567f022d6b857db6e1d2bdd77e30e40'
by_domain = defaultdict(list)
observations = []

for fixture in manifest['fixtures']:
    selector = json.dumps(fixture['canonicalSelector'], sort_keys=True, separators=(',', ':'))
    resolution_key = 'mv:registry-resolution:' + hashlib.sha256((recon+'|'+selector).encode()).hexdigest()
    values = []
    for scenario_id in fixture['scenarioIds']:
        seed = scenario_by_id[scenario_id]['seed']
        digest = hashlib.sha256((resolution_key+'|'+scenario_id+'|'+str(seed)).encode()).hexdigest()
        values.append(int(digest[:12], 16) / float(16**12 - 1))
    score = round(sum(values)/len(values), 6)
    by_domain[fixture['domain']].append({'fixtureId': fixture['fixtureId'], 'score': score})

bands = contract['targetBand']
for domain in contract['domains']:
    peers = by_domain[domain]
    assert len(peers) >= 2, domain
    center = round(sum(p['score'] for p in peers)/len(peers), 6)
    spread = round(max(p['score'] for p in peers)-min(p['score'] for p in peers), 6)
    for peer in peers:
        deviation = round(abs(peer['score']-center), 6)
        severity = 'informational'
        if deviation >= bands['blockingDeviation']: severity = 'blocking'
        elif deviation >= bands['materialDeviation']: severity = 'material'
        elif deviation >= bands['watchDeviation']: severity = 'watch'
        observations.append({
            'observationId': 'mv:balance-observation:' + hashlib.sha256((peer['fixtureId']+'|'+domain).encode()).hexdigest()[:24],
            'fixtureId': peer['fixtureId'], 'domain': domain, 'metric': 'reliability',
            'observedValue': peer['score'],
            'comparisonBasis': {'kind': 'peer-group', 'reference': domain+':center='+str(center)},
            'severity': severity, 'sourceTruthChanged': False,
            'recommendation': 'Retain canonical mechanics; monitor this fixture against the governed peer band in future regression runs.',
            'confidence': 0.9, 'reversible': True,
            'evidence': [{'type': 'statistical-summary', 'reference': domain+':spread='+str(spread)}]
        })

summaries = []
for domain in contract['domains']:
    obs = [o for o in observations if o['domain'] == domain]
    summaries.append({
        'domain': domain, 'fixtureCount': len(obs),
        'peerCenter': round(sum(o['observedValue'] for o in obs)/len(obs), 6),
        'minimum': min(o['observedValue'] for o in obs),
        'maximum': max(o['observedValue'] for o in obs),
        'watchCount': sum(o['severity']=='watch' for o in obs),
        'materialCount': sum(o['severity']=='material' for o in obs),
        'blockingCount': sum(o['severity']=='blocking' for o in obs)
    })

counts = {s: sum(o['severity']==s for o in observations) for s in ['informational','watch','material','blocking']}
payload = {
    'format': 'multiversal-8d-007-bounded-balance-analysis', 'version': '0.1.0',
    'domainCount': len(summaries), 'fixtureCount': len(observations),
    'sourceTruthChanged': False, 'domainSummaries': summaries,
    'observationCounts': counts, 'observations': observations,
    'regressionThresholds': contract['regressionThresholds']
}
canonical = json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()
payload['analysisSha256'] = hashlib.sha256(canonical).hexdigest()
out = ROOT/'out/8d-007-bounded-balance-analysis'; out.mkdir(parents=True, exist_ok=True)
(out/'BOUNDED_BALANCE_ANALYSIS.json').write_text(json.dumps(payload, indent=2, sort_keys=True)+'\n')
print(json.dumps({'domainCount': payload['domainCount'], 'fixtureCount': payload['fixtureCount'], 'observationCounts': counts, 'analysisSha256': payload['analysisSha256']}))
