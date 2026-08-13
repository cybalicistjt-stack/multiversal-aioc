#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INDEX=ROOT/'governance/ai/runtime/ROADMAP_INDEX.json'
BACKLOG=ROOT/'governance/application-planning/character-appearance-production/CAPP_PROGRAM_BACKLOG.json'
PROGRAM='governance/application-planning/character-appearance-production/CAPP_CHARACTER_APPEARANCE_PRODUCTION_PREPARATION_PROGRAM.md'
BACKLOG_PATH='governance/application-planning/character-appearance-production/CAPP_PROGRAM_BACKLOG.json'
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def desired():
 b=load(BACKLOG); out=[]
 for item in b['work_items']:
  out.append({'work_item_id':item['id'],'track':'character-appearance-production','governing_document':BACKLOG_PATH,'roadmap_document':PROGRAM,'roadmap_section':f"{item['id']} — {item['title']}",'dependencies':item['dependencies'],'completion_gate':item['completion_gate']})
 return out
def synced():
 data=load(INDEX); keep=[x for x in data['entries'] if not x.get('work_item_id','').startswith('CAPP-')]; data['entries']=keep+desired(); return data
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); a=ap.parse_args(); want=json.dumps(synced(),indent=2,ensure_ascii=False)+'\n'
 if a.check:
  if INDEX.read_text(encoding='utf-8')!=want:
   print('CAPP roadmap index sync: STALE'); return 1
  print('CAPP roadmap index sync: PASS; entries=12'); return 0
 INDEX.write_text(want,encoding='utf-8'); print('CAPP roadmap index sync: WROTE 12 CAPP entries'); return 0
if __name__=='__main__': raise SystemExit(main())
