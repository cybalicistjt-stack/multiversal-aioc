"""Bounded inference-only audit; never trains or grants perceptual acceptance."""
import csv
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf
import torch
from scipy.spatial.distance import pdist, squareform, cdist
from scipy.stats import spearmanr

BASE = Path('/home/antiquaria/multiversal/dwc-tts')
OUT = BASE / 'runs/perceptual_recovery_20260910'
CORPUS = BASE / 'corpora/DWC_Synthetic_Bootstrap_Corpus_v0.2.1'
OUT.mkdir(exist_ok=True)
torch.set_num_threads(4)


def sha(p):
    with Path(p).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def save(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')


def feature(y):
    # Level-independent spectral trajectory; retain duration/level separately.
    y = np.asarray(y, dtype=np.float32)
    power = librosa.feature.melspectrogram(y=y, sr=22050, n_fft=1024, hop_length=256, n_mels=40)
    mel = librosa.power_to_db(power, ref=np.max, top_db=70)
    mfcc = librosa.feature.mfcc(S=mel, n_mfcc=16)[1:]
    positions = np.linspace(0, mfcc.shape[1]-1, 32)
    trajectory = np.array([np.interp(positions, np.arange(len(v)), v) for v in mfcc])
    return trajectory.flatten(), mel


def audio(p):
    y, sr = sf.read(p, dtype='float32')
    assert sr == 22050 and y.ndim == 1
    return y


def diversity(features):
    distances = squareform(pdist(np.array(features), metric='euclidean')) / np.sqrt(len(features[0]))
    np.fill_diagonal(distances, np.inf)
    return {'median_pair_distance': float(np.median(distances[np.isfinite(distances)])),
            'median_nearest_distance': float(np.median(distances.min(axis=1))),
            'min_pair_distance': float(distances.min())}


rows = list(csv.DictReader((CORPUS/'SYNTHETIC_BOOTSTRAP_MANIFEST.tsv').open(), delimiter='\t'))
features, durations, hashes, levels = [], [], defaultdict(list), []
for row in rows:
    p = CORPUS / row['audio_path']
    y = audio(p)
    features.append(feature(y)[0])
    durations.append(len(y)/22050)
    levels.append(20*np.log10(max(float(np.sqrt(np.mean(y*y))), 1e-12)))
    hashes[sha(p)].append(row['corpus_row_id'])
features = np.array(features)
d = squareform(pdist(features)) / np.sqrt(features.shape[1])
np.fill_diagonal(d, np.inf)
nearest = np.argsort(d.min(axis=1))[:30]
codes = defaultdict(list)
for r in rows:
    codes[r['bootstrap_espeak_code']].append(r)
mapping_collisions = [[{'id':r['corpus_row_id'], 'ids':r['phoneme_id_sequence'], 'text':r['dwc_text']} for r in group]
                      for group in codes.values() if len({r['phoneme_id_sequence'] for r in group})>1]
audit = {'rows':len(rows), 'duration_quantiles_s':np.quantile(durations,[0,.1,.5,.9,1]).tolist(),
         'phone_length_duration_spearman':float(spearmanr([len(r['phoneme_id_sequence'].split()) for r in rows],durations).statistic),
         'rms_min_dbfs':min(levels), 'exact_duplicate_audio_groups':[v for v in hashes.values() if len(v)>1],
         'mapping_collision_groups':mapping_collisions, 'diversity':diversity(features),
         'nearest_pairs':[{'a':rows[i]['corpus_row_id'],'b':rows[int(d[i].argmin())]['corpus_row_id'],
                           'distance':float(d[i].min()),'same_ids':rows[i]['phoneme_id_sequence']==rows[int(d[i].argmin())]['phoneme_id_sequence']} for i in nearest],
         'human_target_smoke':'NOT_RUN', 'training_authorized':False,
         'metric_limit':'MFCC time-normalized distance diagnoses spectral dependence; it does not prove human speech or CNS correctness.'}
save('TARGET_AUDIT.json',audit)
print('TARGET_AUDIT complete', flush=True)

# Four exact one-phone contrasts, plus four short ordinary utterances.
contrasts=[]
for i,r in enumerate(rows):
    ids=r['phoneme_id_sequence'].split()
    if not r['source_utterance_id'].startswith('CONTRAST'): continue
    for j in range(i+1,len(rows)):
        other=rows[j]['phoneme_id_sequence'].split()
        changes=[(a,b) for a,b in zip(ids,other) if a!=b]
        if len(ids)==len(other) and len(changes)==1 and all(int(v)>=13 for v in changes[0]):
            if not any(i in p or j in p for p in contrasts): contrasts.append((i,j))
            break
    if len(contrasts)==4: break
selected=[i for pair in contrasts for i in pair]
selected += [i for i,r in enumerate(rows[:100]) if 7<=len(r['phoneme_id_sequence'].split())<=16 and i not in selected][:4]
selected=selected[:12]
save('TINY_SELECTION.json',[rows[i] for i in selected])
save('TARGET_CONTRASTS.json',[{'a':rows[i]['corpus_row_id'],'b':rows[j]['corpus_row_id'],'ids_a':rows[i]['phoneme_id_sequence'],'ids_b':rows[j]['phoneme_id_sequence'],'distance':float(d[i,j])} for i,j in contrasts])
sys.path.insert(0,str(BASE/'src/piper1-gpl/src'))
from piper.train.vits.lightning import VitsModel
from piper.train.vits.mel_processing import spectrogram_torch
checkpoints={
 'warmstart':None,
 'R1':BASE/'runs/repair_retrain_20260910_110122/R1_phone_balanced_weights_batch0128.pt',
 'R1_flow_restored':BASE/'runs/r1_flow_restore_promotion_20260910_125137/R1_flow_restored_candidate.pt',
 'R2_64':BASE/'runs/r2_protected_20260910_130011/ABORT_R2_PROTECTED_batch0064.pt',
 'R2B_128':BASE/'runs/r2b_protected_20260910_145428/R2B_PROTECTED_weights_batch0128.pt',
 'R2B_256':BASE/'runs/r2b_protected_20260910_145428/R2B_PROTECTED_weights_batch0256.pt',
 'R2C_source384':BASE/'runs/r2c_protected_20260910_195045/R2C_source_rep2_abort384_encp_restored.pt',
 'R2C_final799':BASE/'runs/r2c_protected_20260910_195045/R2C_PROTECTED_weights_batch0799.pt'}
reports={}
target_features=features[selected]
for label,path in checkpoints.items():
    torch.manual_seed(20260908)
    model=VitsModel(num_symbols=58,num_speakers=1,batch_size=1,mos_metric='none')
    if path:
        payload=torch.load(path,map_location='cpu',weights_only=False)
        model.load_state_dict(payload['model_state_dict'],strict=True)
        del payload
    else: model._warmstart_vocoder_from_ckpt(str(BASE/'artifacts/verified/lj-med_1000.ckpt'))
    model=model.cuda().eval()
    g=model.model_g
    def infer(ids, ns=.667, fixed_duration=False):
        torch.manual_seed(91473)
        x=torch.tensor([ids],device='cuda'); lengths=torch.tensor([len(ids)],device='cuda')
        with torch.inference_mode():
            enc,mu,logs,mask=g.enc_p(x,lengths)
            if fixed_duration:
                zprior=mu.repeat_interleave(8,dim=2)
                z=g.flow(zprior,torch.ones_like(zprior[:,:1]),reverse=True)
                wav=g.dec(z)[0,0]
            else:
                output=g.infer(x,lengths,noise_scale=ns,noise_scale_w=0.8,max_len=1000)
                wav=output[0][0,0]; z=output[3][0]
            vals={ 'encoder':enc.cpu().numpy().reshape(-1), 'prior_mean':mu.cpu().numpy().reshape(-1),
                   'decoder_input':torch.nn.functional.adaptive_avg_pool1d(z,32).cpu().numpy().reshape(-1)}
            return wav.cpu().numpy(),vals
    generated=[]
    for i in selected:
        y,_=infer([int(v) for v in rows[i]['phoneme_id_sequence'].split()])
        p=OUT/label/(rows[i]['corpus_row_id']+'.wav'); p.parent.mkdir(exist_ok=True)
        sf.write(p,y,22050,subtype='PCM_16')
        generated.append(feature(y)[0])
    distances=cdist(generated,target_features)/np.sqrt(target_features.shape[1])
    ranks=[int(np.sum(distances[i]<distances[i,i]))+1 for i in range(len(selected))]
    # Equal-length content perturbations with fixed seed and a duration-clamped, zero-noise control.
    ids=[int(v) for v in rows[selected[-1]]['phoneme_id_sequence'].split()]
    content=[i for i,v in enumerate(ids) if v>=13]
    perm=ids.copy(); rev=[ids[i] for i in content][::-1]
    for i,v in zip(content,rev): perm[i]=v
    single=ids.copy(); single[content[0]]=21 if ids[content[0]]!=21 else 37
    repeated=[13 if v>=13 else v for v in ids]
    substituted=[37 if v>=13 else v for v in ids]
    conditions={'original':ids,'single_phone':single,'permuted':perm,'repeated_a':repeated,'substituted_u':substituted}
    causal={}
    for control in (False,True):
        reference,refvals=infer(ids,fixed_duration=control)
        ref_feature=feature(reference)[0]
        measures={}
        for name,seq in conditions.items():
            y,vals=infer(seq,fixed_duration=control)
            measures[name]={'ids':seq,'duration_s':len(y)/22050,
              'mfcc_distance':float(np.sqrt(np.mean((feature(y)[0]-ref_feature)**2))),
              'relative_tensor_deltas':{k:float(np.linalg.norm(v-refvals[k])/max(np.linalg.norm(refvals[k]),1e-9)) for k,v in vals.items()}}
        causal['duration_clamped_zero_noise' if control else 'fixed_seed_default']=measures
    # Posterior reconstruction is an oracle diagnostic, not text-to-speech.
    posterior=[]
    for i in selected[:4]:
        y=audio(CORPUS/rows[i]['audio_path'])
        with torch.inference_mode():
            t=torch.tensor(y,device='cuda').unsqueeze(0)
            spec=spectrogram_torch(t,1024,22050,256,1024,center=False)
            torch.manual_seed(91473)
            z,mu,logs,mask=g.enc_q(spec,torch.tensor([spec.shape[-1]],device='cuda'))
            recon=g.dec(mu*mask)[0,0].cpu().numpy()
        sf.write(OUT/label/(rows[i]['corpus_row_id']+'_posterior_oracle.wav'),recon,22050,subtype='PCM_16')
        posterior.append(float(np.sqrt(np.mean((feature(recon)[0]-features[i])**2))))
    reports[label]={'checkpoint':str(path) if path else 'fresh58 + vocoder-only warm-start',
       'sha256':sha(path) if path else None, 'diversity':diversity(generated),
       'target_retrieval_top1':sum(r==1 for r in ranks),'target_retrieval_count':len(ranks),
       'target_ranks':ranks,'median_own_target_distance':float(np.median(np.diag(distances))),
       'posterior_oracle_target_distances':posterior,'causal':causal}
    save('LINEAGE_CONDITIONING_AUDIT.json',reports)
    print(label, reports[label]['diversity'], 'retrieval',reports[label]['target_retrieval_top1'],flush=True)
    del model,g
    torch.cuda.empty_cache()
save('AUDIT_COMPLETION.json',{'training_performed':False,'checkpoints':len(reports),'selected_rows':len(selected),'human_recovered_candidate_pass':False})
