"""Verify recovery guards and collect durable diagnostics without training."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

BASE=Path('/home/antiquaria/multiversal/dwc-tts')
GOV=BASE/'governance/multiversal-aioc'
HERE=Path(__file__).parent
OUT=BASE/'runs/perceptual_recovery_20260910'

def run(args, expected=0):
    p=subprocess.run(args,cwd=HERE,text=True,capture_output=True)
    return {'command':[str(x) for x in args],'exit_code':p.returncode,
            'passed':p.returncode==expected,'stdout':p.stdout,'stderr':p.stderr}

results=[run([sys.executable,'-m','unittest','test_dwc_recovery_gates','-v'])]
for file in ('DWC_Protected_R2_v0.1.0.py','DWC_Protected_R2B_v0.1.0.py','DWC_Protected_R2C_v0.1.0.py'):
    r=run([sys.executable,str(HERE/file)],expected=1)
    r['passed']=r['passed'] and 'DWC TRAINING BLOCKED' in r['stderr'];results.append(r)
r=run(['bash','/home/antiquaria/multiversal/bootstrap/DWC_Local_Workstation_Bootstrap_v0.1.0/scripts/run_repaired_retrain.sh'],expected=2)
r['passed']=r['passed'] and 'DWC TRAINING BLOCKED' in r['stderr'];results.append(r)
r=run([sys.executable,str(BASE/'harness/DWC_Piper_RepairedCorpus_Retrain_v0.1.0/dwc_retrain_repaired.py')],expected=1)
r['passed']=r['passed'] and 'DWC TRAINING BLOCKED' in r['stderr'];results.append(r)
common=[sys.executable,str(HERE/'dwc_audio_gate.py'),'--reference',str(OUT/'reference_manifest.json'),
        '--rejected',str(OUT/'rejected_manifest.json'),'--pairs',str(OUT/'contrast_pairs.json')]
results.append(run(common+['--candidate',str(OUT/'rejected_manifest.json'),'--output',str(OUT/'REJECTED_CONTROL_GATE.json')],2))
results.append(run(common+['--candidate',str(OUT/'reference_manifest.json'),'--output',str(OUT/'POSITIVE_SELF_CONTROL_GATE.json')],0))
results.append(run([sys.executable,str(HERE/'dwc_target_gate.py'),'--manifest',str(OUT/'reference_manifest.json'),
 '--pairs',str(OUT/'contrast_pairs.json'),'--corpus-artifact',str(OUT/'reference_manifest.json'),'--output',str(OUT/'TINY_TARGET_GATE.json')],0))
results.append(run([sys.executable,'-m','compileall','-q',str(HERE)]))
report={'status':'PASS' if all(r['passed'] for r in results) else 'FAIL','checks':results,'training_performed':False}
(OUT/'VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'checks':len(results)},indent=2))
if report['status']!='PASS':
    print(json.dumps(results,indent=2));raise SystemExit(1)

# Record local blocker patches without importing source archives into Git.
original='set -euo pipefail\n'
patches={'bootstrap_launcher':'run_repaired_retrain.sh now exits 2 before CUDA or output allocation',
         'local_harness':'dwc_retrain_repaired.py main refuses non-preflight use',
         'bootstrap_sha256':hashlib.sha256(Path('/home/antiquaria/multiversal/bootstrap/DWC_Local_Workstation_Bootstrap_v0.1.0/scripts/run_repaired_retrain.sh').read_bytes()).hexdigest(),
         'harness_sha256':hashlib.sha256((BASE/'harness/DWC_Piper_RepairedCorpus_Retrain_v0.1.0/dwc_retrain_repaired.py').read_bytes()).hexdigest()}
(OUT/'LOCAL_GUARD_PATCHES.json').write_text(json.dumps(patches,indent=2)+'\n')
evidence=GOV/'governance/application-planning/dwc-speech/recovery-evidence-20260910'
evidence.mkdir(exist_ok=True)
for name in ('TARGET_AUDIT.json','TARGET_SUMMARY.json','TARGET_CONTRASTS.json','LINEAGE_CONDITIONING_AUDIT.json','EARLY_PROBES.json',
             'HUMAN_REVIEW_IDENTITY.json','TINY_SELECTION.json','REFERENCE_REVIEW_PACKAGE.json',
             'FULL_TARGET_GATE.json','TINY_TARGET_GATE.json','REJECTED_CONTROL_GATE.json','POSITIVE_SELF_CONTROL_GATE.json','VALIDATION.json','LOCAL_GUARD_PATCHES.json'):
    (evidence/name).write_bytes((OUT/name).read_bytes())
hashes=[]
for p in sorted(OUT.rglob('*')):
    if p.is_file() and p.name!='SHA256SUMS.txt': hashes.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(OUT)))
(OUT/'SHA256SUMS.txt').write_text('\n'.join(hashes)+'\n')
(evidence/'SHA256SUMS.txt').write_text('\n'.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name for p in sorted(evidence.glob('*.json')))+'\n')
state={'command_mode':'execution','work_item_status':'Recovery diagnostics and guard repairs validated; target human smoke pending',
 'successor_selection_required':False,'successor_selected':False,'requested_boundary_completed':False,
 'active_async_operations':0,'pending_authorized_steps':['Owner target-smoke judgment before tiny training; tiny model and independent calibration cannot pass in advance'],
 'genuine_blocker':{'class':'owner_only','evidence':['DWC_HUMAN_CATASTROPHIC_FAILURE_2026-09-10.json',
 'Downloads/DWC_TARGET_SMOKE_12_20260910/TARGET_HUMAN_RECEIPT.json has NOT_RUN; no target human PASS exists',
 'Recovery contract requires human target smoke before adaptation; all independent inference, guard implementation and verification completed'],
 'recovery_attempted':True,'blocks_all_authorized_progress':True}}
Path('/tmp/dwc_recovery_termination_state.json').write_text(json.dumps(state))
p=run([sys.executable,str(GOV/'scripts/execution_termination_preflight.py'),'--state','/tmp/dwc_recovery_termination_state.json'])
print(p['stdout']);print(p['stderr'])
if not p['passed'] or 'ALLOW_FINAL_RESPONSE' not in p['stdout']:raise SystemExit(1)
