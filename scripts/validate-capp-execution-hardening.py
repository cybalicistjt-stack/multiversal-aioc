#!/usr/bin/env python3
from __future__ import annotations
import subprocess, sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]

def req(x,m):
    if not x: raise SystemExit('CAPP execution hardening FAILED: '+m)
def read(rel): return (R/rel).read_text(encoding='utf-8')
def run(*args):
    p=subprocess.run([sys.executable,*args],cwd=R,text=True,capture_output=True)
    req(p.returncode==0,(p.stdout+p.stderr).strip())
    return p.stdout

def main():
    for rel in ('scripts/validate-capp01-final-state-structured.py','scripts/validate-capp02-final-state-structured.py'):
        text=read(rel)
        req('historically batched/pending and is now complete' not in text,rel+' contains prose-sensitive pointer assertion')
        req("--format=%B" not in text,rel+' parses merge-message prose')
        req('selection_reason' not in text,rel+' treats explanatory selection prose as completion truth')
    req('validate-capp01-final-state-structured.py' in read('scripts/validate-capp01-completion.py'),'CAPP-01 dispatcher not hardened')
    req('validate-capp02-final-state-structured.py' in read('scripts/validate-capp02-completion.py'),'CAPP-02 dispatcher not hardened')
    transition=read('tools/capp_transition.py')
    req('mode") in {"start", "advance"}' in transition,'transition engine lacks start/advance modes')
    req('json.dumps(value, indent=2' in transition,'transition output is not stable pretty JSON')
    req('all(value is False for value in boundaries.values())' in transition,'transition engine lacks boundary guard')
    workflow=read('.github/workflows/capp-transition.yml')
    req('transition-requests/*.json' in workflow,'connector-safe request trigger missing')
    req("github.actor != 'github-actions[bot]'" in workflow,'transition bot recursion guard missing')
    run('tools/capp_transition.py','self-test')
    run('tools/capp_ci_scope.py','check')
    policy=read('governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md')
    req('No standalone completion-loop rule' in policy,'controlling no-standalone-completion policy missing')
    req('Workflow isolation' in policy,'controlling workflow-isolation policy missing')
    print('CAPP execution hardening: PASS')
    print('controls=structured_completion_evidence,atomic_transition_request,stable_pretty_json,legacy_ppia_scope_isolation,single_completion_transition')

if __name__=='__main__': main()
