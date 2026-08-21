from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'governance/source-material/recovered-legacy/now-this-2026-08-21'
RSR01 = BASE / 'RSR-01_DISPOSITION_REGISTRY.json'
REG = BASE / 'RSR-02_MIB11_RECONCILIATION_REGISTRY.json'
QUEUE = BASE / 'RSR-02_CHRONOLOGY_AND_CONFLICT_QUEUE.json'
ROUTES = BASE / 'RSR-02_DOWNSTREAM_ROUTING.json'
REPORT = BASE / 'RSR-02_COMPLETION_REPORT.md'


def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def main() -> int:
    errors=[]
    for p in [RSR01,REG,QUEUE,ROUTES,REPORT]:
        if not p.is_file(): errors.append(f'missing required RSR-02 artifact: {p}')
    if errors:
        print('RSR-02 validation: BLOCK'); [print('-',e) for e in errors]; return 1
    r1=load(RSR01); reg=load(REG); queue=load(QUEUE); routes=load(ROUTES)
    expected={s['source_id'] for s in r1['sources'] if 'RSR-02' in s.get('routes',[])}
    records=reg.get('records',[]); actual={r.get('source_id') for r in records}
    if expected != actual:
        errors.append(f'RSR-02 source coverage mismatch: expected {len(expected)}, got {len(actual)}')
    if reg.get('rsr02_source_count') != len(expected) or len(expected) != 21:
        errors.append('RSR-02 must reconcile exactly the 21 RSR-01 sources routed to RSR-02')
    for row in records:
        if not row.get('outcome'): errors.append(f"missing outcome: {row.get('source_id')}")
        if row.get('automatic_canon_promotion') is not False: errors.append(f"automatic canon promotion not false: {row.get('source_id')}")
        if not row.get('routes'): errors.append(f"missing downstream routing: {row.get('source_id')}")
        for cid in row.get('candidate_ids',[]):
            if not str(cid).startswith('rsr02:'): errors.append(f"candidate is not RSR bookkeeping ID: {cid}")
    by={r['source_id']:r for r in records}
    def stable(source, sid):
        return sid in by[source].get('stable_ids',[])
    if not stable('rsr01:black-vegas-manual-review','world:black-vegas'): errors.append('Black Vegas must reuse world:black-vegas')
    if not stable('rsr01:black-vegas-manual-review','branch:chronica'): errors.append('Black Vegas must retain branch:chronica link')
    if not stable('rsr01:vertigon-information-breakdown','setting:vertigon'): errors.append('Vertigon must reuse setting:vertigon')
    if not stable('rsr01:vertigon-information-breakdown','world:havalaea'): errors.append('Vertigon must retain world:havalaea parent')
    if not stable('rsr01:goblin-empire-policies-and-role','setting:vertigon'): errors.append('Goblin Empire source must reuse setting:vertigon')
    if not stable('rsr01:empire-of-species-setting','world:antiquaria'): errors.append('Antiquaria source must reuse world:antiquaria')
    if 'rsr02:reality:carnival' not in by['rsr01:carnival-world'].get('candidate_ids',[]): errors.append('Carnival Reality candidate missing')
    qby={x['source_id']:x for x in queue.get('items',[])}
    city=' '.join(qby['rsr01:city-of-millennial'].get('chronology_constraints',[])).lower()
    if 'sapphire' not in city or 'pre-new-tokyo' not in city: errors.append('City of Millennial Sapphire chronology correction missing')
    winds=' '.join(qby['rsr01:consortium-and-30-winds'].get('chronology_constraints',[])).lower()
    if 'age of orilaun' not in winds or 'new tokyo' not in winds: errors.append('30 Winds chronology guardrail missing')
    pen=' '.join(qby['rsr01:pencrona-world'].get('chronology_constraints',[])).lower()
    if 'iteration' not in pen: errors.append('Pencrona iteration chronology guardrail missing')
    if queue.get('queue_count') != len(queue.get('items',[])) or queue.get('queue_count',0) < 3: errors.append('chronology/conflict queue incomplete')
    routed=set()
    for ids in routes.get('routes',{}).values(): routed.update(ids)
    if routed != expected: errors.append('downstream routing does not cover every RSR-02 source')
    if reg.get('assistant_generated_material_policy') != 'proposal-only-unless-independently-supported-or-later-owner-approved': errors.append('assistant-generated material policy drift')
    if reg.get('candidate_authority') != 'noncanonical-reconciliation-bookkeeping-only': errors.append('candidate authority drift')
    auth=reg.get('mib11_authority',{})
    if auth.get('sole_world_runtime_authority') != 'D18/A10': errors.append('D18/A10 authority boundary missing')
    if auth.get('application_merge_sha') != 'b04ce8f2ddb04ab27ea38902041023e761e30eaa': errors.append('MIB-11 completion merge drift')
    text=REPORT.read_text(encoding='utf-8')
    for phrase in ['21 RSR-01 sources','world:black-vegas','setting:vertigon','world:antiquaria','D18/A10']:
        if phrase not in text: errors.append(f'completion report missing {phrase}')
    if errors:
        print('RSR-02 validation: BLOCK'); [print('-',e) for e in errors]; return 1
    print('RSR-02 validation: PASS')
    print('- all 21 RSR-01 world/reality/timeline routes have an explicit reconciliation result')
    print('- Black Vegas, Vertigon/Havalaea, and Antiquaria reuse existing MIB-11 stable identities')
    print('- all RSR-02 candidate IDs remain noncanonical reconciliation bookkeeping')
    print('- owner chronology/corrections remain explicit; assistant-generated material remains proposal-only')
    print('- every source has downstream routing and D18/A10 remains sole World runtime authority')
    return 0

if __name__=='__main__': raise SystemExit(main())
