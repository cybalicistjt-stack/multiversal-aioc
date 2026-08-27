#!/usr/bin/env python3
"""Validate only the current Multiversal authority and execution surface."""
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
from typing import Any

class HealthError(RuntimeError): pass

def require(ok:bool,msg:str)->None:
    if not ok: raise HealthError(msg)

def load(root:Path,rel:str)->dict[str,Any]:
    path=root/rel
    require(path.is_file(),f'missing current file: {rel}')
    try: data=json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc: raise HealthError(f'invalid JSON {rel}: {exc}') from exc
    require(isinstance(data,dict),f'expected object JSON: {rel}')
    return data

def current_paths(authority:dict[str,Any])->set[str]:
    rows=authority.get('current',[]); require(isinstance(rows,list),'authority current must be an array')
    paths=[row.get('path') for row in rows if isinstance(row,dict) and row.get('lifecycle') in {'CURRENT','CURRENT_COMPATIBLE'}]
    require(len(paths)==len(set(paths)),'duplicate authority paths')
    return {p for p in paths if isinstance(p,str)}

def git_head(root:Path)->str:
    p=subprocess.run(['git','rev-parse','HEAD'],cwd=root,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,check=False)
    require(p.returncode==0,f'git head unavailable: {p.stdout.strip()}')
    return p.stdout.strip()

def check(root:Path,expected_head:str|None)->dict[str,Any]:
    if expected_head is not None:
        require(len(expected_head)==40 and all(c in '0123456789abcdef' for c in expected_head),'expected head must be a full lowercase Git SHA')
        require(git_head(root)==expected_head,'AIOC checkout does not match declared exact head')

    pointer=load(root,'governance/ai/runtime/CURRENT_WORK_POINTER.json')
    authority=load(root,'governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json')
    runtime=load(root,'governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json')
    workflows=load(root,'governance/repository-health/WORKFLOW_LIFECYCLE_REGISTRY.json')
    validators=load(root,'governance/repository-health/VALIDATOR_LIFECYCLE_REGISTRY.json')

    active=pointer.get('active_attempt',{}); require(isinstance(active,dict),'pointer active_attempt missing')
    checkpoint_rel=active.get('checkpoint_path'); require(isinstance(checkpoint_rel,str),'pointer checkpoint_path missing')
    checkpoint=load(root,checkpoint_rel)
    require(pointer.get('primary_attempt_id')==checkpoint.get('attempt_id'),'pointer primary attempt/checkpoint mismatch')
    require(active.get('attempt_id')==checkpoint.get('attempt_id'),'pointer active attempt/checkpoint mismatch')
    require(active.get('work_item_id')==checkpoint.get('work_item_id'),'pointer work item/checkpoint mismatch')
    require(active.get('status')==checkpoint.get('status'),'pointer/checkpoint status mismatch')
    if checkpoint.get('status')=='selected_not_started':
        require(checkpoint.get('implementation_authority') is False,'selected_not_started cannot have implementation authority')
        require(checkpoint.get('implementation_branch') is None,'selected_not_started cannot have implementation branch')
    if checkpoint.get('status')=='in_progress':
        require(checkpoint.get('implementation_authority') is True,'in_progress implementation checkpoint must have authority')
        require(bool(checkpoint.get('implementation_branch')),'in_progress implementation checkpoint requires branch')

    paths=current_paths(authority)
    required_authority={
        'governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md',
        'governance/ai/runtime/CURRENT_WORK_POINTER.json',
        checkpoint_rel,
        'governance/ai/MULTIVERSAL_EXECUTION_CONVERGENCE_POLICY.md',
        'governance/ai/MULTIVERSAL_FAMILY_SCOPED_VALIDATION_POLICY.md',
        'governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json',
    }
    require(required_authority<=paths,f'authority missing current paths: {sorted(required_authority-paths)}')
    planning=authority.get('active_planning_work',{}); require(isinstance(planning,dict),'authority active_planning_work missing')
    require(planning.get('work_item')==active.get('work_item_id'),'authority/pointer work item mismatch')
    require(planning.get('attempt_id')==active.get('attempt_id'),'authority/pointer attempt mismatch')
    require(planning.get('state')==active.get('status'),'authority/pointer state mismatch')

    lease=pointer.get('exclusive_control_plane_maintenance')
    if lease is not None:
        require(isinstance(lease,dict),'maintenance lease must be an object')
        require(lease.get('feature_starts_blocked') is True,'exclusive maintenance must block feature starts')
        lease_rel=lease.get('checkpoint_path'); require(isinstance(lease_rel,str),'maintenance checkpoint missing')
        lease_checkpoint=load(root,lease_rel)
        require(lease_checkpoint.get('attempt_id')==lease.get('attempt_id'),'maintenance pointer/checkpoint mismatch')
        require(lease_checkpoint.get('status')=='in_progress','exclusive maintenance checkpoint must be in_progress')
        require(lease_checkpoint.get('exclusive_control_plane_maintenance') is True,'maintenance checkpoint must declare exclusive control')
        require(checkpoint.get('implementation_authority') is False,'feature implementation authority forbidden during exclusive maintenance')
        remediation=authority.get('active_repository_health_remediation',{})
        require(remediation.get('attempt_id')==lease.get('attempt_id'),'authority missing active maintenance lease')
        require(remediation.get('feature_starts_blocked') is True,'authority maintenance must block feature starts')

    work_state=runtime.get('work_state',{}); require(work_state.get('selected_checkpoint')==checkpoint_rel,'runtime selected checkpoint drift')
    ractive=runtime.get('active_work',{}); require(ractive.get('attempt_id')==active.get('attempt_id'),'runtime/pointer attempt drift')
    require(ractive.get('state')==active.get('status'),'runtime/pointer state drift')
    require(ractive.get('implementation_authority')==checkpoint.get('implementation_authority'),'runtime/checkpoint authority drift')

    program=pointer.get('active_program',{}); require(isinstance(program,dict),'pointer active_program missing')
    backlog_rel=program.get('backlog_path'); require(isinstance(backlog_rel,str),'active program backlog missing')
    backlog=load(root,backlog_rel)
    require(backlog.get('program_id')==program.get('program_id'),'program/backlog id mismatch')
    require(backlog.get('completed_through')==program.get('completed_through'),'program/backlog completed_through mismatch')
    require(backlog.get('current_item')==program.get('current'),'program/backlog current item mismatch')

    aioc_live=workflows.get('repositories',{}).get('cybalicistjt-stack/multiversal-aioc',{}).get('live_workflows',[])
    require([x.get('path') for x in aioc_live]==['.github/workflows/validate-repository-health.yml'],'AIOC live workflow namespace must contain exactly one current workflow')
    app_live=workflows.get('repositories',{}).get('cybalicistjt-stack/Multiversal-app',{}).get('live_workflows',[])
    app_paths={x.get('path') for x in app_live}
    require(app_paths=={'.github/workflows/_validation-core-profile.yml','.github/workflows/validate-current-family.yml'},f'application workflow registry drift: {sorted(app_paths)}')
    auto=[x for x in app_live if x.get('automatic_repository_event_trigger') is True]
    require(len(auto)==1 and auto[0].get('path')=='.github/workflows/validate-current-family.yml','application must have exactly one automatic project workflow')
    app_main=workflows.get('repositories',{}).get('cybalicistjt-stack/Multiversal-app',{}).get('current_main')
    require(runtime.get('application_repository',{}).get('canonical_main')==app_main,'runtime/workflow-registry application main drift')

    aioc_validators=validators.get('repositories',{}).get('cybalicistjt-stack/multiversal-aioc',{}).get('current_validators',[])
    require(len(aioc_validators)==1 and aioc_validators[0].get('path')=='scripts/validate_repository_health.py','AIOC must have one flat current validator')
    require(aioc_validators[0].get('implementation')=='flat_current_state','AIOC validator must be registered flat_current_state')
    app_core=validators.get('repositories',{}).get('cybalicistjt-stack/Multiversal-app',{}).get('current_validation_core',[])
    app_core_paths={x.get('path') for x in app_core}
    require('tools/validation_core/validate_family_contract.py' in app_core_paths,'family contract validator not registered')
    require('tools/validation_core/validate_repository_health_app.py' in app_core_paths,'application health validator not registered')
    require(validators.get('repositories',{}).get('cybalicistjt-stack/Multiversal-app',{}).get('current_compatible_manual_checks')==[],'stale manual validation caller remains registered')

    wf_text=(root/'.github/workflows/validate-repository-health.yml').read_text(encoding='utf-8')
    require('validate_rsr_' not in wf_text,'historical RSR validator still auto-executes')
    require('_validate_repository_health_v' not in wf_text,'version-chain validator marker returned to live workflow')
    self_text=(root/'scripts/validate_repository_health.py').read_text(encoding='utf-8')
    require('importlib.util' not in self_text,'flat validator must not dynamically import historical validator chain')
    require('_validate_repository_health_v1_' not in self_text,'flat validator must not reference historical validator chain')

    return {
        'schema_version':'2.0.0',
        'validator':'scripts/validate_repository_health.py',
        'status':'PASS',
        'active_attempt':active.get('attempt_id'),
        'active_status':active.get('status'),
        'exclusive_control_plane_maintenance':lease.get('attempt_id') if isinstance(lease,dict) else None,
        'aioc_automatic_workflows':1,
        'application_automatic_project_workflows':1,
        'historical_rsr_auto_calls':0,
        'validator_runtime_inheritance_depth':0,
        'application_main_registered':app_main,
    }

def main()->int:
    p=argparse.ArgumentParser(); p.add_argument('--root',default='.'); p.add_argument('--expected-head'); p.add_argument('--output'); p.add_argument('--app-root'); a=p.parse_args(); root=Path(a.root).resolve()
    try: result=check(root,a.expected_head)
    except (HealthError,OSError,KeyError,TypeError) as exc: result={'schema_version':'2.0.0','validator':'scripts/validate_repository_health.py','status':'FAIL','error':str(exc)}
    payload=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if a.output: Path(a.output).write_text(payload,encoding='utf-8')
    print(payload,end=''); return 0 if result['status']=='PASS' else 1
if __name__=='__main__': raise SystemExit(main())
