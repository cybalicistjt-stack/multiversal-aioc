"""Target, tiny-overfit and output diversity gates with explicit calibration.

Manifest: JSON array of {id, ids: [integer], audio: absolute path}. Corresponding
reference/output/rejected rows must have identical IDs and phone sequences.
This tool never grants human acceptance. No universal MFCC threshold is assumed.
"""
import argparse
import hashlib
import json
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf
from scipy.spatial.distance import cdist, pdist


def fingerprint(path):
    with Path(path).open('rb') as f: return hashlib.file_digest(f,'sha256').hexdigest()


def load(path):
    rows=json.loads(Path(path).read_text()); values=[]; hashes=[]; issues=[]
    if len({r['id'] for r in rows})!=len(rows): issues.append('duplicate row identity')
    if len({r['audio'] for r in rows})!=len(rows): issues.append('colliding audio paths')
    for row in rows:
        if not row['ids'] or any(type(i) is not int or not 0<=i<58 for i in row['ids']): issues.append('invalid exact IDs')
        y,sr=sf.read(row['audio'],dtype='float32')
        if sr!=22050 or y.ndim!=1: raise ValueError('Expected 22050-Hz mono audio')
        rms=20*np.log10(max(float(np.sqrt(np.mean(y*y))),1e-12))
        if len(y)/sr<.08 or rms < -55 or np.max(np.abs(y))>10**(-.05/20): issues.append('waveform fail: '+row['id'])
        mel=librosa.power_to_db(librosa.feature.melspectrogram(y=y,sr=sr,n_fft=1024,hop_length=256,n_mels=40),ref=np.max,top_db=70)
        mfcc=librosa.feature.mfcc(S=mel,n_mfcc=16)[1:]
        f=np.array([np.interp(np.linspace(0,len(v)-1,32),np.arange(len(v)),v) for v in mfcc]).flatten()
        values.append(f); hashes.append(fingerprint(row['audio']))
    for i in range(len(rows)):
        for j in range(i):
            if hashes[i]==hashes[j] and rows[i]['ids']!=rows[j]['ids']: issues.append('different inputs share exact waveform')
    return rows,np.array(values),issues


def measures(reference, outputs, pairs):
    d=cdist(outputs,reference)/np.sqrt(reference.shape[1])
    own=np.diag(d)
    other=d.copy(); np.fill_diagonal(other,np.inf)
    pair_dist=pdist(outputs)/np.sqrt(reference.shape[1])
    contrast=[np.linalg.norm(outputs[i]-outputs[j])/max(np.linalg.norm(reference[i]-reference[j]),1e-9) for i,j in pairs]
    return {'own_target_top1_fraction':float(np.mean(own<other.min(axis=1))),
            'own_target_margin':float(np.min(other.min(axis=1)-own)),
            'contrast_ratio_min':float(min(contrast)),
            'median_pair_distance':float(np.median(pair_dist))}


def decide(positive, negative, candidate):
    # Three independent requirements: correct target identity, target margin,
    # and survival of the deliberately chosen contrasts. Diversity alone fails.
    keys=('own_target_top1_fraction','own_target_margin','contrast_ratio_min')
    if any(positive[k]<=negative[k] for k in keys):
        return {'status':'UNCALIBRATED_BLOCK','reason':'controls do not separate on every required metric'}
    thresholds={k:(positive[k]+negative[k])/2 for k in keys}
    # A tiny overfit must retrieve EVERY own target with a positive margin.
    thresholds['own_target_top1_fraction']=1.0
    thresholds['own_target_margin']=max(0.0,thresholds['own_target_margin'])
    failed=[k for k in keys if (candidate[k]<thresholds[k] if k=='own_target_top1_fraction' else candidate[k]<=thresholds[k])]
    return {'status':'OUTPUT_MACHINE_FAIL' if failed else 'OUTPUT_MACHINE_PASS',
            'thresholds':thresholds,'failed_metrics':failed,
            'calibration_scope':'This exact panel and controls only; positive control is reference self-retrieval, not evidence of naturalness.'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--reference',required=True); ap.add_argument('--candidate',required=True)
    ap.add_argument('--rejected',required=True); ap.add_argument('--pairs',required=True); ap.add_argument('--output',required=True)
    args=ap.parse_args()
    rows,ref,issues=load(args.reference); cr,cand,ci=load(args.candidate); nr,neg,ni=load(args.rejected)
    assert [(r['id'],r['ids']) for r in rows]==[(r['id'],r['ids']) for r in cr]==[(r['id'],r['ids']) for r in nr]
    pairs=json.loads(Path(args.pairs).read_text())
    if not 8<=len(rows)<=16 or not pairs: raise ValueError('8-16 rows and explicit contrasts required')
    positive=measures(ref,ref,pairs); negative=measures(ref,neg,pairs); candidate=measures(ref,cand,pairs)
    result=decide(positive,negative,candidate)
    if issues or ci: result['status']='OUTPUT_MACHINE_FAIL'
    result.update(reference_issues=issues,candidate_issues=ci,positive=positive,negative=negative,candidate=candidate,
                  human_perceptual_gate='NOT_RUN',training_authorized=False,
                  inputs={k:fingerprint(getattr(args,k)) for k in ('reference','candidate','rejected','pairs')},
                  audio_hashes={group:[{'id':r['id'],'sha256':fingerprint(r['audio'])} for r in records]
                                for group,records in [('reference',rows),('candidate',cr),('rejected',nr)]})
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='audio_hashes'},indent=2))
    raise SystemExit(0 if result['status']=='OUTPUT_MACHINE_PASS' else 2)


if __name__=='__main__': main()
