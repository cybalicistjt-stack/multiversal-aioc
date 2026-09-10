#!/usr/bin/env python3
"""Inference-only module rollback diagnosis for protected DWC R2 batch-64 abort.

Compares the exact batch-64 abort checkpoint with the promoted R1+warm-flow source
checkpoint. R2's model_g.flow is already frozen and is never changed here.

The diagnostic selectively restores from the promoted source checkpoint the three
inference-side modules that R2 was allowed to update:
  model_g.dp.     stochastic duration predictor
  model_g.enc_p.  DWC text/prior encoder
  model_g.dec.    decoder

All eight rollback combinations are evaluated on the corrected 125-row acceptance
set across the same five deterministic seed schedules. This script NEVER trains,
updates optimizer state, authorizes R2 continuation, or performs human acceptance.
"""
from __future__ import annotations

import argparse, csv, hashlib, json, math, sys, types
from pathlib import Path
import numpy as np
import torch

NUM_SYMBOLS=58
SR=22050
RMS_FLOOR_DBFS=-55.0
CLIP_FLOOR_DBFS=-0.05
DEFAULT_SEED=20260908
PREFIXES={"dp":"model_g.dp.","enc_p":"model_g.enc_p.","dec":"model_g.dec.","flow":"model_g.flow.","enc_q":"model_g.enc_q."}

def sha256_file(path:Path,chunk:int=16*1024*1024)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(chunk),b''): h.update(b)
    return h.hexdigest()

def dbfs(v:float)->float: return 20.0*math.log10(max(float(v),1e-12))

def stats(audio:np.ndarray)->dict:
    x=np.asarray(audio,dtype=np.float32).reshape(-1)
    peak=float(np.max(np.abs(x))) if x.size else 0.0
    rms=float(np.sqrt(np.mean(np.square(x)))) if x.size else 0.0
    return {"duration_s":float(len(x)/SR),"peak_dbfs":dbfs(peak),"rms_dbfs":dbfs(rms)}

def status(st:dict)->tuple[str,str]:
    notes=[]
    if st['duration_s']<0.08: notes.append('duration')
    if st['peak_dbfs']>CLIP_FLOOR_DBFS: notes.append('clipping')
    if st['rms_dbfs']<RMS_FLOOR_DBFS: notes.append('low_level')
    return ('PASS' if not notes else 'FAIL',';'.join(notes))

def install_stubs()->None:
    if 'pysilero_vad' not in sys.modules:
        m=types.ModuleType('pysilero_vad')
        class DummyVAD: pass
        m.SileroVoiceActivityDetector=DummyVAD
        sys.modules['pysilero_vad']=m
    if 'pathvalidate' not in sys.modules:
        m=types.ModuleType('pathvalidate'); m.sanitize_filename=lambda s,*a,**k:s; sys.modules['pathvalidate']=m

def load_acceptance(path:Path)->list[dict]:
    rows=list(csv.DictReader(path.open(encoding='utf-8'),delimiter='\t'))
    req={'acceptance_row_id','source_utterance_id','tier','dwc_text','ipa','phoneme_id_sequence','audio_filename'}
    if len(rows)!=125 or not rows or not req.issubset(rows[0]): raise SystemExit('invalid corrected 125-row acceptance table')
    if len({r['acceptance_row_id'] for r in rows})!=125 or len({r['audio_filename'] for r in rows})!=125: raise SystemExit('acceptance identity collision')
    for r in rows:
        ids=[int(x) for x in r['phoneme_id_sequence'].split()]
        if not ids or min(ids)<0 or max(ids)>=NUM_SYMBOLS: raise SystemExit(f"bad IDs: {r['acceptance_row_id']}")
        r['phoneme_ids']=ids
    return rows

def prefix_hash(state:dict,prefix:str)->str:
    h=hashlib.sha256()
    for k in sorted(k for k in state if k.startswith(prefix)):
        t=state[k].detach().cpu().contiguous(); h.update(k.encode()); h.update(str(tuple(t.shape)).encode()); h.update(str(t.dtype).encode()); h.update(t.numpy().tobytes())
    return h.hexdigest()

def drift(state_a:dict,state_b:dict,prefix:str)->dict:
    keys=sorted(k for k in state_a if k.startswith(prefix))
    if not keys: return {'tensors':0,'relative_l2':None,'changed_tensors':0}
    num=den=0.0; changed=0
    for k in keys:
        if k not in state_b or tuple(state_a[k].shape)!=tuple(state_b[k].shape): raise SystemExit(f'checkpoint mismatch at {k}')
        a=state_a[k].detach().cpu().float(); b=state_b[k].detach().cpu().float(); d=a-b
        num+=float(torch.sum(d*d)); den+=float(torch.sum(b*b))
        if not torch.equal(state_a[k].detach().cpu(),state_b[k].detach().cpu()): changed+=1
    return {'tensors':len(keys),'changed_tensors':changed,'relative_l2':math.sqrt(num/max(den,1e-30))}

def write_tsv(path:Path,rows:list[dict])->None:
    if not rows: return
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys()),delimiter='\t',lineterminator='\n'); w.writeheader(); w.writerows(rows)

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--piper-src',required=True); ap.add_argument('--abort-checkpoint',required=True); ap.add_argument('--promoted-checkpoint',required=True)
    ap.add_argument('--acceptance-tsv',required=True); ap.add_argument('--output-dir',required=True); ap.add_argument('--device',default='cuda'); ap.add_argument('--seed',type=int,default=DEFAULT_SEED)
    args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    abort_path=Path(args.abort_checkpoint); promo_path=Path(args.promoted_checkpoint); acc_path=Path(args.acceptance_tsv)
    for p in (abort_path,promo_path,acc_path):
        if not p.exists(): raise SystemExit(f'missing input: {p}')
    acc=load_acceptance(acc_path); device=torch.device(args.device)
    if device.type=='cuda' and not torch.cuda.is_available(): raise SystemExit('CUDA requested but unavailable')
    sys.path.insert(0,str(Path(args.piper_src)/'src')); install_stubs(); from piper.train.vits.lightning import VitsModel
    abort=torch.load(abort_path,map_location='cpu',weights_only=False); promo=torch.load(promo_path,map_location='cpu',weights_only=False)
    for label,p in [('abort',abort),('promoted',promo)]:
        if int(p.get('num_symbols',-1))!=NUM_SYMBOLS or int(p.get('sample_rate',-1))!=SR: raise SystemExit(f'{label} checkpoint metadata mismatch')
    astate=abort['model_state_dict']; pstate=promo['model_state_dict']
    if set(astate)!=set(pstate): raise SystemExit('checkpoint key sets differ')
    if prefix_hash(astate,PREFIXES['flow'])!=prefix_hash(pstate,PREFIXES['flow']): raise SystemExit('flow differs between abort and promoted source; protected-R2 invariant violated')
    module_drift={name:drift(astate,pstate,prefix) for name,prefix in PREFIXES.items()}
    variants=[
        ('abort64_as_is',()),
        ('restore_dp',('dp',)),
        ('restore_enc_p',('enc_p',)),
        ('restore_dec',('dec',)),
        ('restore_dp_enc_p',('dp','enc_p')),
        ('restore_dp_dec',('dp','dec')),
        ('restore_enc_p_dec',('enc_p','dec')),
        ('restore_dp_enc_p_dec',('dp','enc_p','dec')),
    ]
    seed_bases=[args.seed+3000+1000*k for k in range(5)]
    all_results=[]; summaries=[]; sensitive=[]
    model=VitsModel(num_symbols=NUM_SYMBOLS,num_speakers=1,batch_size=1,mos_metric='none').to(device)
    @torch.inference_mode()
    def infer(ids:list[int],seed:int)->np.ndarray:
        model.eval(); torch.manual_seed(seed)
        if device.type=='cuda': torch.cuda.manual_seed_all(seed)
        x=torch.tensor([ids],dtype=torch.long,device=device); xl=torch.tensor([len(ids)],dtype=torch.long,device=device)
        return model.model_g.infer(x,xl,noise_scale=0.667,length_scale=1.0,noise_scale_w=0.8)[0][0,0].detach().float().cpu().numpy()
    for vname,restore in variants:
        state={k:v.clone() for k,v in astate.items()}
        for mod in restore:
            pref=PREFIXES[mod]
            for k in [x for x in state if x.startswith(pref)]: state[k]=pstate[k].clone()
        missing,unexpected=model.load_state_dict(state,strict=False)
        if missing or unexpected: raise SystemExit(f'{vname} state mismatch: missing={missing[:10]} unexpected={unexpected[:10]}')
        per_row={r['acceptance_row_id']:[] for r in acc}; seed_s=[]
        for sj,sb in enumerate(seed_bases,1):
            rows=[]
            for i,r in enumerate(acc):
                st=stats(infer(r['phoneme_ids'],sb+i)); s,n=status(st)
                rec={'variant':vname,'seed_index':sj,'seed_base':sb,'acceptance_row_id':r['acceptance_row_id'],'source_utterance_id':r['source_utterance_id'],'dwc_text':r['dwc_text'],**st,'status':s,'notes':n}
                rows.append(rec); all_results.append(rec); per_row[r['acceptance_row_id']].append(rec)
            vals=[x['rms_dbfs'] for x in rows]; ps=sum(x['status']=='PASS' for x in rows)
            seed_s.append({'seed_index':sj,'seed_base':sb,'pass':ps,'fail':125-ps,'median_dbfs':float(np.median(vals)),'min_dbfs':float(min(vals))})
        always=sum(all(x['status']=='PASS' for x in rs) for rs in per_row.values())
        anyfail=125-always
        summaries.append({'variant':vname,'restored_modules':','.join(restore) if restore else 'none','pass_counts':'/'.join(str(x['pass']) for x in seed_s),'always_pass_5_of_5':always,'rows_failing_any_seed':anyfail,'worst_rms_dbfs':min(x['min_dbfs'] for x in seed_s),'median_dbfs_seed1':seed_s[0]['median_dbfs']})
        for r in acc:
            rs=per_row[r['acceptance_row_id']]; passes=sum(x['status']=='PASS' for x in rs)
            if passes<5:
                sensitive.append({'variant':vname,'acceptance_row_id':r['acceptance_row_id'],'source_utterance_id':r['source_utterance_id'],'dwc_text':r['dwc_text'],'passes_of_5':passes,'failure_notes':'|'.join(x['notes'] for x in rs if x['status']!='PASS'),'rms_dbfs_min':min(x['rms_dbfs'] for x in rs),'duration_s_min':min(x['duration_s'] for x in rs)})
    write_tsv(out/'variant_summary.tsv',summaries); write_tsv(out/'variant_sensitive_rows.tsv',sensitive); write_tsv(out/'all_variant_seed_rows.tsv',all_results)
    best=max(summaries,key=lambda x:(x['always_pass_5_of_5'],min(int(q) for q in x['pass_counts'].split('/')),x['median_dbfs_seed1']))
    report={'schema_version':'0.1.0','status':'MODULE_ROLLBACK_DIAGNOSTIC_COMPLETE','training_performed':False,'r2_continuation_authorized_by_this_script':False,'human_gate_authorized_by_this_script':False,
      'abort_checkpoint':{'file':abort_path.name,'bytes':abort_path.stat().st_size,'sha256':sha256_file(abort_path)},'promoted_checkpoint':{'file':promo_path.name,'bytes':promo_path.stat().st_size,'sha256':sha256_file(promo_path)},
      'acceptance':{'file':acc_path.name,'sha256':sha256_file(acc_path),'rows':125},'flow_hash':prefix_hash(astate,PREFIXES['flow']),'module_drift_relative_to_promoted':module_drift,'seed_bases':seed_bases,'variants':summaries,'best_by_machine_robustness':best,
      'interpretation_boundary':'Diagnostic only. Review module rollback results before changing the protected R2 training contract.'}
    (out/'R2_ABORT64_MODULE_ROLLBACK_REPORT.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    hashes=[]
    for p in sorted(out.iterdir()):
        if p.is_file() and p.name!='SHA256SUMS.txt': hashes.append(f'{sha256_file(p)}  {p.name}')
    (out/'SHA256SUMS.txt').write_text('\n'.join(hashes)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
