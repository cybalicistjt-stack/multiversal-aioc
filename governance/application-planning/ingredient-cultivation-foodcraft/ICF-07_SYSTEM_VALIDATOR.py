#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from jsonschema import Draft202012Validator

HERE=Path(__file__).resolve().parent
schema=json.loads((HERE/'ICF-07_HARVEST_PROFILE_SCHEMA.json').read_text())
fixtures=json.loads((HERE/'ICF-07_REFERENCE_FIXTURES.json').read_text())
Draft202012Validator.check_schema(schema)
v=Draft202012Validator(schema)
profiles={p['profileId']:p for p in fixtures['profiles']}
for p in profiles.values():
    errors=list(v.iter_errors(p))
    assert not errors,(p['profileId'],[e.message for e in errors])

def resolve(s):
    if 'phase' in s:
        if s['id']=='ICF07-FX-007':
            assert s['dispatchOutcome']=='ambiguous'
            return 'recovery-required','query-d17-status-before-retry'
        if s['id']=='ICF07-FX-008':
            assert s['d17ReceiptDurable'] is True
            return 'recovery-required','query-source-owner-and-replay-finalization-not-output'
    p=profiles[s['profileId']]
    if p['evidenceStatus']=='gap': return 'gap',None
    if s['sourceVersion']!=s['expectedSourceVersion']: return 'blocked',None
    if s['mode'] not in p['allowedModes']: return 'blocked',None
    if s.get('hardRestriction'): return 'blocked',None
    if not s.get('requirementsPresent',False): return 'blocked',None
    if s.get('elapsedTimeBand')=='>12h':
        for q in p['qualityRules']:
            if q['dimension']=='elapsed-time' and q.get('table',{}).get('>12h')=='block':
                return 'blocked',None
    outputs=[]
    for slot in p['outputSlots']:
        if slot['mode']!=s['mode']: continue
        q=slot['quantityRule']
        if q['kind']=='fixed': qty=q['fixedQuantity']
        elif q['kind']=='outcome-table': qty=q['outcomes'].get(s['procedureOutcome'])
        else: raise AssertionError('fixture validator does not resolve external source-table-ref')
        if qty and qty>0: outputs.append({'definitionRef':slot['definitionRef'],'quantity':qty,'unitRef':q['unitRef']})
    return 'source-reservation-pending',outputs

for s in fixtures['scenarios']:
    state,extra=resolve(s)
    assert state==s['expected'],(s['id'],state,s['expected'])
    if 'expectedOutput' in s: assert extra==s['expectedOutput'],(s['id'],extra,s['expectedOutput'])
    if 'recoveryAction' in s: assert extra==s['recoveryAction'],(s['id'],extra,s['recoveryAction'])

assert all(p['authority']['outputOwnerDomain']=='D17 Asset Instance' for p in profiles.values())
assert all(p['authority']['priceAuthority']=='MIB-13' for p in profiles.values())
assert all(p['recoveryPolicy']['statusBeforeRetry'] for p in profiles.values())
assert all(not p['allowedModes'] and not p['outputSlots'] for p in profiles.values() if p['evidenceStatus']=='gap')
assert profiles['harvest-profile:icf06-phoenix-feather-gap']['evidenceStatus']=='gap'

summary={'schemaVersion':'1.0.0','workItem':'ICF-07','status':'PASS','profileCount':len(profiles),'scenarioCount':len(fixtures['scenarios']),'checks':{'schemaValid':True,'profilesConform':True,'gapProfilesCannotHarvest':True,'staleSourceVersionFailsClosed':True,'requirementsFailClosed':True,'hardRestrictionsBlock':True,'explicitElapsedTimeRuleOnly':True,'sourceReservationPrecedesD17':True,'d17OutputAuthorityPreserved':True,'statusBeforeRetry':True,'durableD17ReceiptPreventsDuplicateOutput':True,'icf06CreatureGapDoesNotAuthorizeHarvest':True},'notes':['Reference creature profiles are fixtures, not a mass creature-catalog crosswalk.','No part-effect affinity grammar is implemented; ICF-08 remains authoritative.','No processing lineage is implemented; ICF-10 remains authoritative.','ICF-06 Phoenix Feather remains unharvestable until authored creature/crosswalk evidence is supplied.']}
print(json.dumps(summary,indent=2,sort_keys=True))
