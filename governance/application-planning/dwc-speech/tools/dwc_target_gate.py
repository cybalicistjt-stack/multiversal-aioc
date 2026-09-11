"""Corpus gate: integrity plus calibrated contrast/near-duplicate checks.

Human smoke remains a separate required authorization receipt.
"""
import argparse
import json
from pathlib import Path
import librosa
import numpy as np
import soundfile as sf
from scipy.spatial.distance import cdist
from dwc_audio_gate import load, fingerprint


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--manifest',required=True);ap.add_argument('--pairs',required=True)
    ap.add_argument('--corpus-artifact',required=True);ap.add_argument('--output',required=True)
    a=ap.parse_args();rows,f,issues=load(a.manifest)
    pairs=json.loads(Path(a.pairs).read_text());control=[]
    for r,original in zip(rows,f):
        y,sr=sf.read(r['audio'],dtype='float32')
        rng=np.random.default_rng(91473)
        # Fixed 16-bit quantization-scale perturbation, not a naturalness proxy.
        y=y+rng.uniform(-1/32768,1/32768,len(y)).astype(np.float32)
        mel=librosa.power_to_db(librosa.feature.melspectrogram(y=y,sr=sr,n_fft=1024,hop_length=256,n_mels=40),ref=np.max,top_db=70)
        c=librosa.feature.mfcc(S=mel,n_mfcc=16)[1:]
        v=np.array([np.interp(np.linspace(0,len(x)-1,32),np.arange(len(x)),x) for x in c]).flatten()
        control.append(float(np.sqrt(np.mean((v-original)**2))))
    floor=max(control);d=cdist(f,f)/np.sqrt(f.shape[1]);suspect=[]
    for i in range(len(rows)):
        for j in range(i):
            if rows[i]['ids']!=rows[j]['ids'] and d[i,j]<=floor:
                suspect.append({'a':rows[i]['id'],'b':rows[j]['id'],'distance':float(d[i,j])})
    contrasts=[{'a':rows[i]['id'],'b':rows[j]['id'],'distance':float(d[i,j]),'pass':bool(d[i,j]>floor)} for i,j in pairs]
    if not pairs:issues.append('no deliberate contrast pairs')
    if suspect:issues.append('unexplained distinct-input near duplicates')
    if any(not r['pass'] for r in contrasts):issues.append('contrast below quantization-control separation')
    result={'status':'TARGET_MACHINE_REVIEW' if issues else 'TARGET_MACHINE_PASS',
      'corpus_sha256':fingerprint(a.corpus_artifact),'rows':len(rows),'issues':issues,
      'quantization_control_max_mfcc_distance':floor,'contrasts':contrasts,'suspect_pairs':suspect,
      'human_perceptual_gate':'NOT_RUN','training_authorized':False,
      'meaning':'Machine-distinguishable references; human speech quality remains untested.',
      'audio_hashes':[{'id':r['id'],'sha256':fingerprint(r['audio'])} for r in rows]}
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='audio_hashes'},indent=2))
    raise SystemExit(2 if issues else 0)


if __name__=='__main__':main()
