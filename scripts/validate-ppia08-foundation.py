#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'governance/application-planning/parallel-preimplementation'
INV=BASE/'PPIA-08_SOURCE_AND_DESIGN_INVENTORY.md'
SRC=BASE/'PPIA-08_SOURCE_MANIFEST_v0.1.0.json'
TAX=BASE/'PPIA-08_CAMPAIGN_SCENE_SESSION_TAXONOMY_v0.1.0.json'
MAP=BASE/'PPIA-08_MAP_GRID_DUNGEON_AUTHORING_CONTRACT_v0.1.0.json'
AUTH=BASE/'PPIA-08_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json'
CAND=BASE/'PPIA-08_FOUNDATION_CANDIDATE.md'
CP=ROOT/'governance/ai/work-state/PPIA-08-attempt-001.json'
PTR=ROOT/'governance/ai/runtime/CURRENT_WORK_POINTER.json'
STATUS=ROOT/'governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json'
BACKLOG=BASE/'PPIA_PROGRAM_BACKLOG.json'
TRANSITION='ccdad24fc26ca853b92411ad1066eb6b7ec1f0f5'

def req(c,m):
    if not c: raise SystemExit('PPIA-08 FOUNDATION: FAIL — '+m)
def load(p): req(p.exists(),f'missing {p.relative_to(ROOT)}'); return json.loads(p.read_text(encoding='utf-8'))

def main():
    for p in (INV,SRC,TAX,MAP,AUTH,CAND): req(p.exists(),f'missing {p.relative_to(ROOT)}')
    inv=INV.read_text(encoding='utf-8'); src=load(SRC); tax=load(TAX); mapc=load(MAP); auth=load(AUTH); cand=CAND.read_text(encoding='utf-8'); cp=load(CP); ptr=load(PTR); status=load(STATUS); backlog=load(BACKLOG)
    req(src['work_item_id']=='PPIA-08' and src['transition_merge']==TRANSITION,'source manifest identity/transition mismatch')
    req(len(src['canonical_repository_sources'])==9,'expected nine canonical repository source entries')
    req(len(src['retained_supporting_design_sources'])==3,'expected three retained design-bible source groups')
    req(src['owner_directed_extension']['blocking'] is True,'owner map extension must be blocking')
    ext=' '.join(src['owner_directed_extension']['requirements']).lower()
    for x in ['map image upload','square-grid','pan','cell/area','dungeon-map']:
        req(x in ext,f'owner extension missing {x}')

    layers=tax['identity_state_layers']; ids=[x['id'] for x in layers]
    req(len(layers)==16 and len(ids)==len(set(ids)),'expected sixteen unique semantic layers')
    for x in ['map-media-asset-reference','grid-calibration-and-coordinate-transform','cell-area-zone-addressing','map-content-placement-and-layering','dungeon-geometry-and-construction','preparation-launch-snapshot-and-session-binding','permission-provenance-recovery-accessibility']:
        req(x in ids,f'taxonomy missing {x}')
    req(len(tax['presentation_profiles'])==12,'expected twelve presentation profiles')
    req(set(tax['map_coordinate_invariants']) and all(v is False for v in tax['foundation_non_assumptions'].values()),'taxonomy non-assumptions/invariants invalid')

    req(mapc['owner_requirement_blocking'] is True,'map contract owner requirement must be blocking')
    req(mapc['map_asset_contract']['asset_is_separate_from_calibration'] is True,'map asset/calibration must be separate')
    req(mapc['map_asset_contract']['destructive_rewrite_for_grid_alignment'] is False,'grid alignment may not rewrite image')
    req(mapc['coordinate_modes']==['square','gridless'],'initial coordinate modes must be square + gridless')
    cal=mapc['square_grid_calibration']; required=set(cal['required_fields'])
    for x in ['cellSizePx','originOffsetXPx','originOffsetYPx','expected_version']:
        req(x in required,f'calibration missing {x}')
    req(cal['camera_view_state_is_not_calibration_state'] is True,'camera pan and grid alignment must stay separate')
    req(cal['automatic_scale_inference_required'] is False and cal['rotation_required'] is False,'foundation may not require scale inference or rotation')
    placement=mapc['placement_record']; kinds=set(placement['placement_kinds'])
    for x in ['item','hazard','encounter','creature-npc','vehicle','objective','trigger','note']:
        req(x in kinds,f'placement kind missing {x}')
    req(placement['copies_source_definition'] is False,'placements may not copy source definitions')
    req(mapc['launch_snapshot']['post_launch_recalibration_silently_moves_active_session'] is False,'recalibration may not silently move live session')
    dungeon=mapc['dungeon_construction_kit']; req(len(dungeon['primitive_families'])==7,'expected seven dungeon primitive families')
    for x in ['room-floor-region','corridor-path-region','wall-segment','door-opening','terrain-feature-region','stairs-portal-transition-marker','reusable-tile-stamp']:
        req(x in dungeon['primitive_families'],f'dungeon primitive missing {x}')
    req(dungeon['procedural_generator_required'] is False and dungeon['automatic_collision_cover_los_rules'] is False,'dungeon scope overreached')
    req(mapc['recovery']['authoritative_mutations_require_expected_version'] is True and mapc['recovery']['authoritative_mutations_require_operation_id'] is True,'map mutations need recovery protocol')
    req(mapc['accessibility']['map_is_only_authoritative_representation'] is False and mapc['accessibility']['cell_and_zone_semantic_list_required'] is True,'nonvisual map equivalence missing')

    req(len(auth['authority_levels'])==4 and len(auth['domain_handoffs'])==10,'authority matrix cardinality mismatch')
    guard=' '.join(auth['blocking_guardrails']).lower()
    for x in ['destructively','camera','source definition','hidden','launch snapshots','gridless','nonvisual']:
        req(x in guard,f'guardrail missing {x}')

    for x in ['SD-302','SD-1003','MV-IA-F005','square grid','panned/translated','basic dungeon map construction kit','Gridless','nonvisual']:
        req(x.lower() in inv.lower(),f'inventory missing {x}')
    for x in ['FOUNDATION CANDIDATE — NOT PPIA-08 COMPLETE','cellSizePx','originOffsetXPx','originOffsetYPx','rooms/floors','launch snapshots','PPIA-08 remains `started`']:
        req(x.lower() in cand.lower(),f'candidate missing {x}')

    tr={x['work_item_id']:x for x in backlog['tranches']}; req(backlog['current_work_item_id']=='PPIA-08' and tr['PPIA-08']['status'] in {'started','in_progress'},'backlog must select active PPIA-08')
    gate=tr['PPIA-08']['completion_gate'].lower()
    for x in ['map-image upload','grid','calibration','cell-addressable','dungeon-map construction kit']:
        req(x in gate,f'backlog gate lost {x}')
    req(cp['work_item_id']=='PPIA-08' and cp['attempt_id']=='PPIA-08-attempt-001' and cp['status'] in {'started','in_progress'},'PPIA-08 checkpoint identity/state mismatch')
    req(cp['base_commit']=='ac1628227d34df7fc1585b21c21988fb2fd7080a','PPIA-08 checkpoint original base mismatch')
    req(not cp['unresolved_failures'] and cp['owner_decision_required'] is False,'PPIA-08 checkpoint unresolved state')
    selected=[x for x in ptr['active_attempts'] if x.get('owner_selected')]; req(len(selected)==1 and selected[0]['work_item_id']=='PPIA-08','pointer must select PPIA-08')
    req(ptr['primary_attempt_id']=='PPIA-08-attempt-001','primary PPIA attempt mismatch')
    primary=status['primary']; req(primary['work_item_id']=='PPIA-08' and primary['attempt_id']=='PPIA-08-attempt-001' and primary['status']==cp['status'],'compact status mismatch')
    req(primary['active_substep']==cp['active_substep'] and primary['next_action']==cp['next_action'],'compact checkpoint work mismatch')

    print('PPIA-08 FOUNDATION: PASS')
    print('semantic_layers=16')
    print('presentation_profiles=12')
    print('domain_handoffs=10')
    print('coordinate_modes=square,gridless')
    print('dungeon_primitive_families=7')
    print('map_image_rewrite_for_calibration=false')
    print('map_grid_dungeon_owner_requirement=blocking')
    print('runtime_activation=false')
if __name__=='__main__': main()
