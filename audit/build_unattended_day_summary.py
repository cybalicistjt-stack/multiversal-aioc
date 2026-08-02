#!/usr/bin/env python3
"""Consolidate the unattended workday into one owner-facing readiness report."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

def read(path: Path):
    try: return json.loads(path.read_text(encoding='utf-8'))
    except Exception: return None

def main() -> None:
    root=Path('v2/audit-data'); out=Path('unattended-day-summary'); out.mkdir(parents=True,exist_ok=True)
    sources={
      'v4Assembly':root/'semantic-recovery-v4/object-assembly-v4-index.json',
      'v4Candidates':root/'semantic-recovery-v4/canonical-candidate-v4-index.json',
      'gptPackets':root/'semantic-recovery-v4/gpt-review-packets-v4-index.json',
      'regressionMining':root/'semantic-recovery-v4/regression-mining-v4-index.json',
      'longform':root/'unattended-longform/unattended-longform-index.json',
      'duplicates':root/'unattended-longform/duplicate-clusters.json',
      'schemaGaps':root/'unattended-longform/schema-gap-report.json',
      'relationships':root/'unattended-longform/relationship-diagnostics.json',
    }
    loaded={k:read(v) for k,v in sources.items()}; available=[k for k,v in loaded.items() if v is not None]
    missing=[k for k,v in loaded.items() if v is None]
    cand=loaded.get('v4Candidates') or {}; asm=loaded.get('v4Assembly') or {}; packets=loaded.get('gptPackets') or {}; reg=loaded.get('regressionMining') or {}; longform=loaded.get('longform') or {}
    actions=[]
    if int(cand.get('expertSampleCount',0))>0: actions.append('Review the strict GPT packet first.')
    if int(packets.get('diagnosticCount',0))>0: actions.append('Send the diagnostic GPT packet to a dedicated analysis conversation.')
    if int(reg.get('boundaryChallengeCount',0))>0: actions.append('Convert confirmed boundary challenges into permanent regression tests.')
    if not longform: actions.append('Inspect the long-form workflow because its compact index did not publish.')
    summary={
      'format':'multiversal-unattended-workday-summary','version':'1.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),
      'availableOutputs':available,'missingOutputs':missing,
      'metrics':{
        'assembledObjects':asm.get('assembledObjectCount'), 'candidateCount':cand.get('candidateCount'), 'familyCounts':cand.get('familyCounts'),
        'expertSampleCount':cand.get('expertSampleCount'), 'humanReviewCount':cand.get('humanReviewCount'), 'evidenceOnlyCount':cand.get('evidenceOnlyCount'),
        'resolvedRelationships':cand.get('resolvedRelationshipCount'), 'unresolvedRelationships':cand.get('unresolvedRelationshipCount'),
        'strictGptPacketCount':packets.get('strictCount'), 'diagnosticGptPacketCount':packets.get('diagnosticCount'),
        'regressionPositiveCount':reg.get('probablePositiveCount'), 'regressionChallengeCount':reg.get('boundaryChallengeCount'),
        'longformFamilyPacketCount':longform.get('familyPacketCount')
      },
      'recommendedNextActions':actions,
      'authority':'Summary and diagnostics only. No canonical approval, merge, or owner certification occurred.'
    }
    (out/'unattended-workday-summary.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
    lines=['# Multiversal Unattended Workday Summary','',f"Generated: {summary['generatedAt']}",'',f"Available outputs: {', '.join(available) or 'none'}",f"Missing outputs: {', '.join(missing) or 'none'}",'','## Key metrics']
    for k,v in summary['metrics'].items(): lines.append(f'- **{k}:** {v}')
    lines+=['','## Recommended next actions']+[f'- {x}' for x in actions]+['','No canonical content was changed.']
    (out/'README.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
