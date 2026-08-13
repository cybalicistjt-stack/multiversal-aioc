#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ALLOWED_ROOTS=(
 'governance/application-planning/',
 'governance/ai/',
 'scripts/',
 'tools/',
 '.github/workflows/',
 'tests/',
)
REGISTERED={
 'capp-transition':['python','tools/capp_transition.py','apply'],
 'capp-transition-self-test':['python','tools/capp_transition.py','self-test'],
 'capp-ci-scope':['python','tools/capp_ci_scope.py','check'],
}

def fail(msg): raise SystemExit('WRITE BRIDGE: FAIL — '+msg)
def rel(path):
 p=Path(path)
 if p.is_absolute() or '..' in p.parts: fail('unsafe path')
 s=p.as_posix()
 if not any(s.startswith(root) for root in ALLOWED_ROOTS): fail('path outside allowlist: '+s)
 return ROOT/p

def load(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def write_json(path,value):
 path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def pointer_parts(ptr):
 if ptr in ('','/'): return []
 if not ptr.startswith('/'): fail('JSON pointer must start with /')
 return [x.replace('~1','/').replace('~0','~') for x in ptr[1:].split('/')]
def set_pointer(doc,ptr,value):
 parts=pointer_parts(ptr)
 if not parts: fail('root replacement not permitted; use json_create')
 cur=doc
 for key in parts[:-1]:
  if isinstance(cur,list): cur=cur[int(key)]
  else:
   if key not in cur: cur[key]={}
   cur=cur[key]
 key=parts[-1]
 if isinstance(cur,list): cur[int(key)]=value
 else: cur[key]=value

def op_json_create(op):
 p=rel(op['path'])
 if p.exists(): fail('json_create target exists: '+op['path'])
 if not isinstance(op.get('document'),(dict,list)): fail('json_create document')
 write_json(p,op['document'])
def op_json_set(op):
 p=rel(op['path'])
 if not p.exists(): fail('json_set target missing: '+op['path'])
 doc=load(p)
 changes=op.get('set',{})
 if not isinstance(changes,dict) or not changes: fail('json_set requires set object')
 for ptr,value in changes.items(): set_pointer(doc,ptr,value)
 write_json(p,doc)
def op_text_replace(op):
 p=rel(op['path'])
 if not p.exists(): fail('text_replace target missing: '+op['path'])
 text=p.read_text(encoding='utf-8')
 reps=op.get('replacements',[])
 if not reps or len(reps)>20: fail('text_replace replacement count')
 for r in reps:
  old,new=r.get('old'),r.get('new')
  if not isinstance(old,str) or not old or not isinstance(new,str): fail('text_replace payload')
  if len(old)>4000 or len(new)>4000: fail('text_replace entry too large')
  count=text.count(old)
  if count!=1: fail(f'text_replace expected one match, got {count}')
  text=text.replace(old,new,1)
 p.write_text(text,encoding='utf-8',newline='\n')
def op_run_registered(op):
 name=op.get('name')
 if name not in REGISTERED: fail('unregistered command')
 argv=list(REGISTERED[name])
 args=op.get('args',[])
 if not isinstance(args,list) or any(not isinstance(x,str) or len(x)>512 for x in args): fail('registered args')
 subprocess.run(argv+args,cwd=ROOT,check=True)

def apply(req):
 if req.get('schema_version')!='1.0.0': fail('schema_version')
 ops=req.get('operations')
 if not isinstance(ops,list) or not 1<=len(ops)<=25: fail('operations')
 handlers={'json_create':op_json_create,'json_set':op_json_set,'text_replace':op_text_replace,'run_registered':op_run_registered}
 for op in ops:
  kind=op.get('op')
  if kind not in handlers: fail('unsupported operation: '+str(kind))
  handlers[kind](op)
 print(f"WRITE BRIDGE: PASS operations={len(ops)}")
def self_test():
 for root in ALLOWED_ROOTS: assert root.endswith('/')
 assert 'capp-transition' in REGISTERED
 print('WRITE BRIDGE SELF-TEST: PASS')
def main():
 ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
 a=sub.add_parser('apply'); a.add_argument('--request',required=True)
 sub.add_parser('self-test'); args=ap.parse_args()
 if args.cmd=='self-test': self_test()
 else: apply(load(args.request))
if __name__=='__main__': main()
