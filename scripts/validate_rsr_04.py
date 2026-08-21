#!/usr/bin/env python3
"""Validate RSR-04 CEL/economy/life-loop reconciliation invariants."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'governance/source-material/recovered-legacy/now-this-2026-08-21'

def load(name):
    return json.loads((BASE/name).read_text(encoding='utf-8'))

def main():
    reg=load('RSR-04_CEL_RECONCILIATION_REGISTRY.json')
    q=load('RSR-04_CANDIDATE_AND_BOUNDARY_QUEUE.json')
    tax=load('RSR-04_POST_SCARCITY_PROPOSAL_TAXONOMY.json')
    routing=load('RSR-04_DOWNSTREAM_ROUTING.json')
    assert reg['work_item']=='RSR-04' and reg['source_count']==24
    assert len(reg['records'])==24
    assert len({r['source_id'] for r in reg['records']})==24
    assert len({r['filename'] for r in reg['records']})==24
    assert all(r['automatic_canon_promotion'] is False for r in reg['records'])
    assert all(r['canonical_mutation'] is False for r in reg['records'])
    assert reg['canonical_cel_or_economy_mutation'] is False
    counts=reg['counts']
    assert counts=={'material_cel_signal_count':16,'no_material_cel_signal_count':8,'original_rsr01_rsr04_route_count':4,'supplemental_cel_signal_count':12}
    assert sum(1 for r in reg['records'] if r['explicit_rsr04_route'])==4
    assert any(r['source_id']=='rsr01:vertigon-information-breakdown' and r['relevance']=='owner-grounded-context' for r in reg['records'])
    assert any(r['source_id']=='rsr01:pencrona-world' and 'CEL-04' in r['cel_surfaces'] for r in reg['records'])
    assert any(r['source_id']=='rsr01:consortium-s-manipulation-revealed' and r['result']=='world-context-only' for r in reg['records'])
    assert q['candidate_count']==13 and len(q['candidates'])==13
    assert q['boundary_count']==12 and len(q['boundaries'])==12
    assert all(c['canonical'] is False for c in q['candidates'])
    assert q['canonical_cel_or_economy_mutation'] is False
    assert tax['model_count']==79 and len(tax['models'])==79
    assert tax['canonical'] is False and tax['automatic_canon_promotion'] is False
    assert [m['ordinal'] for m in tax['models']]==list(range(1,80))
    assert routing['implementation_authority_granted'] is False
    routes={x['destination']:x for x in routing['routes']}
    assert {'RSR-05','RSR-07','DPL','WCI','SGC'} <= set(routes)
    assert len(routes['SGC']['source_ids'])==24
    authority=reg['authority']
    assert authority['cozy_life_loop']=='completed CEL-01..06'
    assert authority['markets_prices_currencies_trade']=='MIB-13'
    assert authority['downtime_projects']=='APW'
    assert authority['cozy_delegation_automation']=='APM'
    assert authority['wall_clock_progress'] is False
    print('RSR-04 reconciliation integrity: PASS')
    print(json.dumps({'sources':24,'material':16,'supplemental':12,'candidates':13,'boundaries':12,'post_scarcity_models':79,'canonical_mutations':0},sort_keys=True))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
