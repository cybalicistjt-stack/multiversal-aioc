#!/usr/bin/env python3
"""Build bounded GPT review packets from Semantic Recovery v4 candidates.

Creates a strict expert packet and a stratified diagnostic packet. These packets
support deeper analysis in a separate GPT conversation but never authorize canon.
"""
from __future__ import annotations
import argparse, json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

FAMILY_ORDER=("ability","creature","item","species","npc","vehicle","environment","world","faction","adventure","rule")

def load(path:Path)->list[dict]:
 return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]

def compact(row:dict)->dict:
 p=(row.get('provenance') or [{}])[0]
 r=row.get('recovery') or {}
 return {
  'candidateId':row.get('id'),'proposedType':row.get('type'),'proposedName':row.get('name'),
  'reviewRoute':row.get('reviewRoute'),'summary':(row.get('specification') or {}).get('summary'),
  'sections':(row.get('specification') or {}).get('sections'),
  'mechanicSignals':(row.get('specification') or {}).get('mechanicSignals'),
  'relationships':row.get('relationships') or [],
  'source':{'path':p.get('sourcePath'),'pageStart':p.get('pageStart'),'pageEnd':p.get('pageEnd'),'locator':p.get('locator'),'findingId':p.get('findingId')},
  'quality':{'identityConfidence':r.get('identityConfidence'),'completenessScore':r.get('completenessScore'),'familyMargin':r.get('familyMargin'),'boundaryEvidenceCount':r.get('boundaryEvidenceCount'),'sectionCount':r.get('sectionCount'),'missingFields':r.get('missingFields')},
  'requiredDecision':{'shouldExtract':None,'correctType':None,'correctName':None,'boundaryAssessment':None,'fieldCorrections':{},'relationshipCorrections':[],'confidence':None,'reasoningSummary':None}
 }

def prompt(packet_name:str)->str:
 return f"""You are reviewing Multiversal legacy-content recovery candidates as a senior tabletop-RPG data architect, rules editor, and information-extraction verifier.

Review packet: {packet_name}

For every candidate:
1. Decide whether it represents a distinct game object that should be extracted.
2. Correct the object family and name when necessary.
3. Identify whether the boundary is complete, merged, fragmented, a child section, table row, stat field, taxonomy heading, example, procedure, or contextual heading.
4. Correct structured fields only when supported by the supplied evidence.
5. Remove invalid relationships and suggest relationships only when the target is explicitly supported.
6. Never add lore or mechanics from general knowledge.
7. Preserve exact source provenance.

Return JSON only, with one decision object per candidate using this schema:
{{
  \"candidateId\": \"...\",
  \"shouldExtract\": true,
  \"correctType\": \"ability|creature|item|species|npc|vehicle|environment|world|faction|adventure|rule|null\",
  \"correctName\": \"... or null\",
  \"boundaryAssessment\": \"complete|needs-parent|needs-children|merged-objects|fragment|table-row|stat-field|taxonomy|example|procedure|contextual-heading|duplicate|other\",
  \"fieldCorrections\": {{}},
  \"relationshipCorrections\": [],
  \"confidence\": 0,
  \"reasoningSummary\": \"brief evidence-based explanation\"
}}

This is evaluation evidence only. Do not approve canonical import or claim owner approval."""

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--candidates',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--diagnostic-limit',type=int,default=40);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 rows=load(a.candidates/'canonical-candidates-v4.jsonl')
 strict=[x for x in rows if x.get('reviewRoute')=='expert-sample']
 by=defaultdict(list)
 for x in rows:
  if x.get('reviewRoute')!='expert-sample': by[x.get('type')].append(x)
 diagnostic=[]
 per=max(2,a.diagnostic_limit//max(1,len([f for f in FAMILY_ORDER if by.get(f)])))
 for family in FAMILY_ORDER:
  pool=sorted(by.get(family,[]),key=lambda x:(-(x.get('recovery') or {}).get('identityConfidence',0),-(x.get('recovery') or {}).get('familyMargin',0),-(x.get('recovery') or {}).get('completenessScore',0),x.get('name','')))
  diagnostic.extend(pool[:per])
 diagnostic=diagnostic[:a.diagnostic_limit]
 meta={'format':'multiversal-gpt-review-packets-v4-index','version':'4.4.0','generatedAt':datetime.now(timezone.utc).isoformat(),'strictCount':len(strict),'diagnosticCount':len(diagnostic),'strictFamilyCounts':dict(Counter(x.get('type') for x in strict)),'diagnosticFamilyCounts':dict(Counter(x.get('type') for x in diagnostic)),'authorityNote':'Review packets are non-canonical evaluation evidence.'}
 strict_payload={**meta,'packetType':'strict-expert','prompt':prompt('strict-expert'),'candidates':[compact(x) for x in strict]}
 diagnostic_payload={**meta,'packetType':'diagnostic-stratified','prompt':prompt('diagnostic-stratified'),'candidates':[compact(x) for x in diagnostic]}
 (a.out/'gpt-review-packets-v4-index.json').write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')
 (a.out/'gpt-strict-expert-review-packet.json').write_text(json.dumps(strict_payload,indent=2,ensure_ascii=False)+'\n')
 (a.out/'gpt-diagnostic-review-packet.json').write_text(json.dumps(diagnostic_payload,indent=2,ensure_ascii=False)+'\n')
 (a.out/'GPT-REVIEW-INSTRUCTIONS.txt').write_text(prompt('selected-packet')+'\n',encoding='utf-8')
 print(json.dumps(meta,indent=2))
if __name__=='__main__':main()
