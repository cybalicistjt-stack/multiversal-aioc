"""Summarize audit evidence and prepare reference-only human target triage."""
import csv
import hashlib
import html
import json
import shutil
import zipfile
from pathlib import Path
import librosa
import numpy as np
import soundfile as sf
from scipy.spatial.distance import pdist, squareform

BASE=Path('/home/antiquaria/multiversal/dwc-tts')
OUT=BASE/'runs/perceptual_recovery_20260910'
CORPUS=BASE/'corpora/DWC_Synthetic_Bootstrap_Corpus_v0.2.1'
GOV=BASE/'governance/multiversal-aioc/governance/application-planning/dwc-speech'
DOWNLOADS=Path('/mnt/c/Users/Antiquaria/Downloads')

def sha(p):
    with Path(p).open('rb') as f: return hashlib.file_digest(f,'sha256').hexdigest()

def save(path,data):
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')

rows=json.loads((OUT/'TINY_SELECTION.json').read_text())
ref=[{'id':r['corpus_row_id'],'ids':[int(v) for v in r['phoneme_id_sequence'].split()], 'audio':str(CORPUS/r['audio_path'])} for r in rows]
neg=[{**r,'audio':str(OUT/'R2C_final799'/(r['id']+'.wav'))} for r in ref]
save(OUT/'reference_manifest.json',ref); save(OUT/'rejected_manifest.json',neg)
save(OUT/'contrast_pairs.json',[[0,1],[2,3],[4,5],[6,7]])

manifest=list(csv.DictReader((CORPUS/'SYNTHETIC_BOOTSTRAP_MANIFEST.tsv').open(),delimiter='\t'))
lookup={r['corpus_row_id']:r for r in manifest}
save(OUT/'full_reference_manifest.json',[{'id':r['corpus_row_id'],'ids':[int(v) for v in r['phoneme_id_sequence'].split()], 'audio':str(CORPUS/r['audio_path'])} for r in manifest])
positions={r['corpus_row_id']:i for i,r in enumerate(manifest)}
save(OUT/'full_contrast_pairs.json',[[positions[rows[i]['corpus_row_id']],positions[rows[j]['corpus_row_id']]] for i,j in [(0,1),(2,3),(4,5),(6,7)]])
audit=json.loads((OUT/'TARGET_AUDIT.json').read_text())
summary={'duplicate_audio_groups':len(audit['exact_duplicate_audio_groups']),
 'duplicate_excess_rows':sum(len(g)-1 for g in audit['exact_duplicate_audio_groups']),
 'different_id_duplicate_groups':[g for g in audit['exact_duplicate_audio_groups'] if len({lookup[i]['phoneme_id_sequence'] for i in g})>1],
 'mapping_collisions':audit['mapping_collision_groups'],
 'human_target_quality':'UNKNOWN_PENDING_12_REFERENCE_CLIPS',
 'training_authorized':False}
save(OUT/'TARGET_SUMMARY.json',summary)

# Measure preserved early R1 probes without repeating training or inference.
def feat(path):
    y,sr=sf.read(path,dtype='float32')
    mel=librosa.power_to_db(librosa.feature.melspectrogram(y=y,sr=sr,n_fft=1024,hop_length=256,n_mels=40),ref=np.max,top_db=70)
    c=librosa.feature.mfcc(S=mel,n_mfcc=16)[1:]
    return np.array([np.interp(np.linspace(0,len(v)-1,32),np.arange(len(v)),v) for v in c]).flatten()
early=[]
for folder in sorted((BASE/'runs/repair_retrain_20260910_110122/probes').iterdir()):
    paths=sorted(folder.glob('*.wav')); f=np.array([feat(p) for p in paths])
    d=squareform(pdist(f))/np.sqrt(f.shape[1]); np.fill_diagonal(d,np.inf)
    early.append({'label':folder.name,'rows':len(paths),'median_nearest_distance':float(np.median(d.min(axis=1))),
                  'minimum_pair_distance':float(d.min()),'limitation':'Preserved probe inputs differ in content and length; cannot date human failure to an exact batch.'})
save(OUT/'EARLY_PROBES.json',early)

# Verify owner-reviewed audio is byte-identical to persisted final machine set.
review=DOWNLOADS/'DWC_R2C_HUMAN_REVIEW_20260910_201801'
final=BASE/'runs/r2c_protected_20260910_195045'
review_files=list((review/'audio').glob('*.wav'))
final_files={p.name:p for p in (final/'wav/R2C_final').glob('*.wav')}
comparisons=[{'file':p.name,'sha256':sha(p),'persisted_match':p.name in final_files and sha(p)==sha(final_files[p.name])} for p in review_files]
checkpoint=final/'R2C_PROTECTED_weights_batch0799.pt'
identity={'checkpoint_sha256':sha(checkpoint),'checkpoint_bytes':checkpoint.stat().st_size,
 'review_zip_sha256':sha(DOWNLOADS/'DWC_R2C_HUMAN_REVIEW_20260910_201801.zip'),
 'review_rows':len(comparisons),'exact_matches':sum(r['persisted_match'] for r in comparisons),'rows':comparisons}
assert identity['checkpoint_sha256']=='c26ecb279ed5759a4c251ad54c80ebaa38e055194f6698681922b33e64269a3e'
assert identity['review_rows']==identity['exact_matches']==125
save(OUT/'HUMAN_REVIEW_IDENTITY.json',identity)

# References only: no recovered candidate has earned a listening release.
package=DOWNLOADS/'DWC_TARGET_SMOKE_12_20260910'
package.mkdir(exist_ok=True); (package/'audio').mkdir(exist_ok=True)
items=[]
for n,r in enumerate(rows,1):
    name=f'{n:02d}_{r["corpus_row_id"]}.wav'; dest=package/'audio'/name
    shutil.copy2(CORPUS/r['audio_path'],dest)
    items.append({'id':r['corpus_row_id'],'text':r['dwc_text'],'ipa':r['ipa'],
                  'ids':r['phoneme_id_sequence'],'audio':'audio/'+name,'sha256':sha(dest)})
save(package/'AUDIO_MANIFEST.json',items)
save(package/'TARGET_HUMAN_RECEIPT.json',{'status':'NOT_RUN','reviewer':'John Brandon Turner',
 'audio_manifest_sha256':sha(package/'AUDIO_MANIFEST.json'),'owner_evidence':'',
 'question':'Do these reference clips sound like distinguishable speech, with the paired sounds different? These are synthetic targets, not a new trained candidate.'})
cards='\n'.join('<li><h2>'+html.escape(r['id']+' '+r['text'])+'</h2><p>'+html.escape(r['ipa'])+'</p><audio controls preload="none" src="'+r['audio']+'"></audio><details><summary>Exact IDs</summary>'+r['ids']+'</details></li>' for r in items)
(package/'review.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DWC target audio review</title><style>body{font:18px system-ui;max-width:720px;margin:auto;padding:20px;color:#202020;background:#fff}li{border-bottom:1px solid #ccc;padding:16px 0}h2{font-size:19px}audio{width:100%}ol{padding-left:24px}</style><h1>DWC target audio review</h1><p>12 existing synthetic reference clips. No recovered model candidate is being presented.</p><p>Are these distinguishable speech? Are the first four pairs audibly different? A brief pass/fail and any clip numbers are enough.</p><ol>'+cards+'</ol></html>')
with zipfile.ZipFile(str(package)+'.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in package.rglob('*'):
        if p.is_file(): z.write(p,p.relative_to(package))
save(OUT/'REFERENCE_REVIEW_PACKAGE.json',{'path':str(package)+'.zip','sha256':sha(str(package)+'.zip'),'kind':'TARGET_REFERENCE_TRIAGE_ONLY','recovered_candidate_produced':False})
print(json.dumps(summary,indent=2)); print('Reference review',str(package)+'.zip')
