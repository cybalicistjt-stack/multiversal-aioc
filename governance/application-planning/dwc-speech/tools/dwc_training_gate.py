"""Fail-closed authorization for bounded experiments and training.

No waveform score can supply a human receipt. Human decisions bind to exact
audio-manifest hashes. Calibration must separate positive and rejected controls.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path


def digest(path):
    with Path(path).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def human_pass(receipt, manifest):
    accepted = (receipt.get('status') == 'PERCEPTUAL_SMOKE_PASS'
            and receipt.get('reviewer') == 'John Brandon Turner'
            and receipt.get('audio_manifest_sha256') == digest(manifest)
            and bool(receipt.get('owner_evidence')))
    if not accepted: return False
    try:
        records=json.loads(Path(manifest).read_text())
        return bool(records) and all(digest(Path(manifest).parent/r['audio'])==r['sha256'] for r in records)
    except (OSError,KeyError,TypeError,ValueError):
        return False


def authorize(request, target, target_receipt, target_manifest, tiny=None,
              output_receipt=None, output_manifest=None):
    errors=[]
    if target.get('status') != 'TARGET_MACHINE_PASS': errors.append('target audit incomplete or failed')
    if not human_pass(target_receipt,target_manifest): errors.append('target human smoke missing, failed or stale')
    if request.get('corpus_sha256') != target.get('corpus_sha256'): errors.append('corpus identity mismatch')
    if request.get('kind') not in ('tiny_overfit','small_tranche','larger_tranche'): errors.append('unknown training stage')
    if any(not isinstance(request.get(k), (int,float)) or not math.isfinite(request[k]) or request[k]<=0 for k in ('max_steps','max_seconds')): errors.append('finite positive budget required')
    if request.get('kind')=='tiny_overfit':
        if not 8<=request.get('rows',0)<=16: errors.append('tiny set must contain 8-16 rows')
        if request.get('max_steps',0)>200 or request.get('max_seconds',0)>300: errors.append('tiny budget exceeds 200 steps/300 seconds')
    else:
        tiny=tiny or {}
        if tiny.get('status') != 'TINY_OVERFIT_MACHINE_PASS': errors.append('tiny overfit has not passed')
        for field in ('all_own_targets_retrieved','contrasts_survive','fixed_seed_conditioning_pass','loss_reduction_verified','independent_calibration_pass'):
            if tiny.get(field) is not True: errors.append('tiny requirement missing: '+field)
        if tiny.get('corpus_sha256')!=request.get('corpus_sha256'): errors.append('tiny corpus identity mismatch')
        if tiny.get('checkpoint_sha256')!=request.get('source_checkpoint_sha256'): errors.append('source checkpoint not validated')
        if not output_manifest or not human_pass(output_receipt or {},output_manifest): errors.append('output human smoke missing, failed or stale')
        if not request.get('owner_tranche_authorization'): errors.append('explicit bounded tranche authorization required')
    return {'authorized':not errors,'errors':errors}


def reject_legacy_training():
    raise SystemExit('DWC TRAINING BLOCKED: catastrophic human failure. Legacy waveform-only training is retired. Use a bounded recovery experiment with target audit, exact-artifact human smoke and tiny-overfit authorization.')


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--reject-legacy',action='store_true')
    ap.add_argument('--request',type=Path)
    args=ap.parse_args()
    if args.reject_legacy: reject_legacy_training()
    if not args.request: ap.error('--request required')
    bundle=json.loads(args.request.read_text())
    result=authorize(**bundle)
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if result['authorized'] else 2)
