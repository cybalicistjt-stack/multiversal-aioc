#!/usr/bin/env python3
"""Protected DWC R2C continuation after cross-replicate batch-384 rollback diagnosis.

Source:
- replicate-2 ABORT_R2B_PROTECTED_batch0384.pt
- restore ONLY model_g.enc_p.* from that replicate's proven batch-256 checkpoint
- verify five-seed 625/625 before any training

Protection:
- freeze/hash-protect model_g.flow, model_g.dp, model_g.enc_p
- train only remaining generator parameters plus discriminator
- reconstruct original deterministic 799-row schedule and train rows 385..799 (415 rows)
- preserve/restore torch RNG around inference guards so validation cannot perturb training RNG
- fixed probes every 8 global batches
- primary 125-row gate every 32 global batches
- five-seed strengthened gate every 64 global batches
- keep one rolling exact-resume checkpoint with optimizer/RNG state at strengthened boundaries

This script never performs or claims human CNS perceptual acceptance.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math, random, sys, time, types, wave
from pathlib import Path
import numpy as np
import torch
NUM_SYMBOLS=58; SR=22050; RMS_FLOOR_DBFS=-55.0; CLIP_FLOOR_DBFS=-0.05; DEFAULT_SEED=20260908
EXPECTED_ABORT384_SHA256="5a53ce2dde13df389fada834cc027283ef14dc2be44a102fc9fedd249716fd1b"
EXPECTED_CK256_SHA256="88afedca8530f95eaa276568c15aa8612570e51f7aad2a04c6c51b49464e8ff6"
EXPECTED_SOURCE_CANDIDATE_SHA256="e0d78cf89a4fd50a79e064837993d8bc11556e03ad2399d64b8cc53ee93c146b"
PREFIX_FLOW="model_g.flow."; PREFIX_DP="model_g.dp."; PREFIX_ENCP="model_g.enc_p."
FIRST_COMPLETED=384; TOTAL_ROWS=799
class GuardAbort(RuntimeError): pass

def sha256_file(path:Path,chunk:int=16*1024*1024)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(chunk),b""): h.update(b)
    return h.hexdigest()

def dbfs(v:float)->float: return 20.0*math.log10(max(float(v),1e-12))

def stats_from_audio(audio:np.ndarray)->dict:
    x=np.asarray(audio,dtype=np.float32).reshape(-1); peak=float(np.max(np.abs(x))) if x.size else 0.0; rms=float(np.sqrt(np.mean(np.square(x)))) if x.size else 0.0
    return {"duration_s":float(len(x)/SR),"peak_dbfs":dbfs(peak),"rms_dbfs":dbfs(rms)}

def wav_stats(path:Path)->dict:
    with wave.open(str(path),"rb") as w: ch,sw,sr,n=w.getnchannels(),w.getsampwidth(),w.getframerate(),w.getnframes(); raw=w.readframes(n)
    if not (ch==1 and sw==2 and sr==SR): raise ValueError(f"bad WAV format {path.name}: ch={ch} sw={sw} sr={sr}")
    return stats_from_audio(np.frombuffer(raw,dtype="<i2").astype(np.float32)/32768.0)

def write_wav(path:Path,audio:np.ndarray)->dict:
    path.parent.mkdir(parents=True,exist_ok=True); x=np.asarray(audio,dtype=np.float32).reshape(-1); pcm=(np.clip(x,-1.0,1.0)*32767.0).astype("<i2")
    with wave.open(str(path),"wb") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    return wav_stats(path)

def machine_status(st:dict)->tuple[str,str]:
    notes=[]
    if st["duration_s"]<0.08: notes.append("duration")
    if st["peak_dbfs"]>CLIP_FLOOR_DBFS: notes.append("clipping")
    if st["rms_dbfs"]<RMS_FLOOR_DBFS: notes.append("low_level")
    return ("PASS" if not notes else "FAIL",";".join(notes))

def install_stubs()->None:
    if "pysilero_vad" not in sys.modules:
        m=types.ModuleType("pysilero_vad")
        class DummyVAD: pass
        m.SileroVoiceActivityDetector=DummyVAD; sys.modules["pysilero_vad"]=m
    if "pathvalidate" not in sys.modules:
        m=types.ModuleType("pathvalidate"); m.sanitize_filename=lambda s,*a,**k:s; sys.modules["pathvalidate"]=m

def load_corpus(root:Path)->list[dict]:
    manifest=list(csv.DictReader((root/"SYNTHETIC_BOOTSTRAP_MANIFEST.tsv").open(encoding="utf-8"),delimiter="\t")); lines=(root/"piper_synthetic_bootstrap_custom_ids.csv").read_text(encoding="utf-8").splitlines()
    if len(manifest)!=TOTAL_ROWS or len(lines)!=TOTAL_ROWS: raise SystemExit(f"expected {TOTAL_ROWS} repaired corpus rows")
    by_filename={r["piper_audio_filename"]:r for r in manifest}
    if len(by_filename)!=TOTAL_ROWS or len({r["corpus_row_id"] for r in manifest})!=TOTAL_ROWS: raise SystemExit("repaired corpus identity collision")
    rows=[]
    for i,line in enumerate(lines,1):
        parts=line.split("|")
        if len(parts)!=3: raise SystemExit(f"bad corpus csv row {i}")
        fn,text,ids_s=parts; ids=[int(x) for x in ids_s.split()]
        if not ids or min(ids)<0 or max(ids)>=NUM_SYMBOLS: raise SystemExit(f"bad IDs at corpus row {i}")
        m=by_filename.get(fn)
        if m is None: raise SystemExit(f"corpus filename missing from manifest: {fn}")
        wav=root/"audio_22050"/fn
        if not wav.exists(): raise SystemExit(f"missing corpus WAV: {wav}")
        st=wav_stats(wav); status,notes=machine_status(st)
        if status!="PASS": raise SystemExit(f"corpus target gate failed: {fn}: {notes}: {st}")
        rows.append({"file":fn,"text":text,"ids":ids,"corpus_row_id":m["corpus_row_id"],"source_utterance_id":m["source_utterance_id"]})
    return rows

def load_acceptance(path:Path)->list[dict]:
    rows=list(csv.DictReader(path.open(encoding="utf-8"),delimiter="\t")); required={"acceptance_row_id","source_utterance_id","tier","dwc_text","ipa","phoneme_id_sequence","audio_filename"}
    if len(rows)!=125 or not rows or not required.issubset(rows[0]): raise SystemExit("invalid corrected 125-row acceptance table")
    if len({r["acceptance_row_id"] for r in rows})!=125 or len({r["audio_filename"] for r in rows})!=125: raise SystemExit("acceptance identity collision")
    for r in rows:
        ids=[int(x) for x in r["phoneme_id_sequence"].split()]
        if not ids or min(ids)<0 or max(ids)>=NUM_SYMBOLS: raise SystemExit(f"bad exact IDs: {r['acceptance_row_id']}")
        r["phoneme_ids"]=ids
    return rows

def state_prefix_sha256(state:dict,prefix:str)->str:
    h=hashlib.sha256(); keys=sorted(k for k in state if k.startswith(prefix))
    if not keys: raise SystemExit(f"no keys for prefix {prefix}")
    for k in keys:
        t=state[k].detach().cpu().contiguous(); h.update(k.encode("utf-8")); h.update(str(tuple(t.shape)).encode("ascii")); h.update(str(t.dtype).encode("ascii")); h.update(t.numpy().tobytes())
    return h.hexdigest()

def restore_prefix(dst:dict,src:dict,prefix:str)->int:
    keys=sorted(k for k in dst if k.startswith(prefix)); src_keys={k for k in src if k.startswith(prefix)}
    if set(keys)!=src_keys: raise SystemExit(f"prefix key mismatch for {prefix}")
    for k in keys:
        if tuple(dst[k].shape)!=tuple(src[k].shape): raise SystemExit(f"shape mismatch: {k}")
        dst[k]=src[k].detach().cpu().clone()
    return len(keys)

def summarize(rows:list[dict])->dict:
    vals=[float(r["rms_dbfs"]) for r in rows]
    return {"rows":len(rows),"pass":sum(r["status"]=="PASS" for r in rows),"fail":sum(r["status"]!="PASS" for r in rows),"rms_dbfs_median":float(np.median(vals)),"rms_dbfs_min":float(min(vals)),"rms_dbfs_max":float(max(vals)),"below_minus55":int(sum(v<RMS_FLOOR_DBFS for v in vals))}

def write_tsv(path:Path,rows:list[dict])->None:
    if not rows:return
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys()),delimiter="\t",lineterminator="\n",extrasaction="ignore"); w.writeheader(); w.writerows(rows)

def torch_rng_snapshot(): return (torch.get_rng_state(),torch.cuda.get_rng_state_all() if torch.cuda.is_available() else None)
def torch_rng_restore(snap)->None:
    cpu,cuda=snap; torch.set_rng_state(cpu)
    if cuda is not None: torch.cuda.set_rng_state_all(cuda)

def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument("--piper-src",required=True); ap.add_argument("--checkpoint256",required=True); ap.add_argument("--abort384",required=True); ap.add_argument("--corpus-root",required=True); ap.add_argument("--acceptance-tsv",required=True); ap.add_argument("--output-dir",required=True); ap.add_argument("--device",default="cuda"); ap.add_argument("--seed",type=int,default=DEFAULT_SEED); ap.add_argument("--probe-every",type=int,default=8); ap.add_argument("--primary-gate-every",type=int,default=32); ap.add_argument("--robust-gate-every",type=int,default=64); ap.add_argument("--max-probe-drop-db",type=float,default=18.0); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True); p256=Path(args.checkpoint256); p384=Path(args.abort384)
    if sha256_file(p256)!=EXPECTED_CK256_SHA256: raise SystemExit("replicate-2 batch-256 checkpoint SHA-256 mismatch")
    if sha256_file(p384)!=EXPECTED_ABORT384_SHA256: raise SystemExit("replicate-2 batch-384 abort checkpoint SHA-256 mismatch")
    corpus=load_corpus(Path(args.corpus_root)); acceptance=load_acceptance(Path(args.acceptance_tsv)); device=torch.device(args.device)
    if device.type=="cuda" and not torch.cuda.is_available(): raise SystemExit("CUDA requested but unavailable")
    c256=torch.load(p256,map_location="cpu",weights_only=False); c384=torch.load(p384,map_location="cpu",weights_only=False)
    for label,payload,expected_batch in (("checkpoint256",c256,256),("abort384",c384,384)):
        if int(payload.get("num_symbols",-1))!=NUM_SYMBOLS or int(payload.get("sample_rate",-1))!=SR or int(payload.get("phase_batch",-1))!=expected_batch: raise SystemExit(f"{label} metadata mismatch")
        if payload.get("source_candidate_sha256")!=EXPECTED_SOURCE_CANDIDATE_SHA256: raise SystemExit(f"{label} source candidate mismatch")
        if payload.get("optimizer_state_restored") is not False: raise SystemExit(f"{label} optimizer provenance mismatch")
    s256=c256["model_state_dict"]; s384=c384["model_state_dict"]
    if set(s256)!=set(s384): raise SystemExit("checkpoint key sets differ")
    for prefix,label in ((PREFIX_FLOW,"flow"),(PREFIX_DP,"dp")):
        if state_prefix_sha256(s256,prefix)!=state_prefix_sha256(s384,prefix): raise SystemExit(f"protected {label} changed between batch256 and batch384")
    candidate_state={k:v.detach().cpu().clone() for k,v in s384.items()}; restored_encp_tensors=restore_prefix(candidate_state,s256,PREFIX_ENCP)
    if restored_encp_tensors!=111: raise SystemExit(f"expected 111 enc_p tensors, restored {restored_encp_tensors}")
    protected_hashes={"flow":state_prefix_sha256(candidate_state,PREFIX_FLOW),"dp":state_prefix_sha256(candidate_state,PREFIX_DP),"enc_p":state_prefix_sha256(candidate_state,PREFIX_ENCP)}
    source_candidate_path=out/"R2C_source_rep2_abort384_encp_restored.pt"; source_payload={"model_state_dict":candidate_state,"num_symbols":NUM_SYMBOLS,"sample_rate":SR,"status":"R2C_SOURCE_CANDIDATE","source_abort384_sha256":EXPECTED_ABORT384_SHA256,"source_checkpoint256_sha256":EXPECTED_CK256_SHA256,"restored_prefix":PREFIX_ENCP,"restored_tensors":restored_encp_tensors,"prior_completed_schedule_rows":FIRST_COMPLETED,"optimizer_state_restored":False}; torch.save(source_payload,source_candidate_path)
    source_candidate={"file":source_candidate_path.name,"bytes":source_candidate_path.stat().st_size,"sha256":sha256_file(source_candidate_path)}
    sys.path.insert(0,str(Path(args.piper_src)/"src")); install_stubs(); from piper.train.vits.lightning import VitsModel; from piper.train.vits.dataset import Batch; from piper.train.vits.mel_processing import spectrogram_torch
    model=VitsModel(num_symbols=NUM_SYMBOLS,num_speakers=1,batch_size=1,mos_metric="none"); missing,unexpected=model.load_state_dict(candidate_state,strict=False)
    if missing or unexpected: raise SystemExit(f"candidate load mismatch missing={missing[:10]} unexpected={unexpected[:10]}")
    model.to(device)
    for module in (model.model_g.flow,model.model_g.dp,model.model_g.enc_p):
        for p in module.parameters(): p.requires_grad_(False)
    if any(p.requires_grad for p in model.model_g.flow.parameters()) or any(p.requires_grad for p in model.model_g.dp.parameters()) or any(p.requires_grad for p in model.model_g.enc_p.parameters()): raise SystemExit("failed to freeze protected modules")
    def current_protected_hashes()->dict:
        st=model.state_dict(); return {"flow":state_prefix_sha256(st,PREFIX_FLOW),"dp":state_prefix_sha256(st,PREFIX_DP),"enc_p":state_prefix_sha256(st,PREFIX_ENCP)}
    if current_protected_hashes()!=protected_hashes: raise SystemExit("protected hash mismatch after model load")
    trainable_g=[p for p in model.model_g.parameters() if p.requires_grad]; opt_g=torch.optim.AdamW(trainable_g,lr=model.hparams.learning_rate,betas=model.hparams.betas,eps=model.hparams.eps); opt_d=torch.optim.AdamW(model.model_d.parameters(),lr=model.hparams.learning_rate_d,betas=model.hparams.betas_d,eps=model.hparams.eps)
    def make_batch(row:dict):
        wav=Path(args.corpus_root)/"audio_22050"/row["file"]
        with wave.open(str(wav),"rb") as w: raw=w.readframes(w.getnframes())
        arr=np.frombuffer(raw,dtype="<i2").astype("float32")/32768.0; audio=torch.from_numpy(arr).to(device).unsqueeze(0)
        if audio.shape[-1]<8192: audio=torch.nn.functional.pad(audio,(0,8192-audio.shape[-1]))
        spec=spectrogram_torch(audio,1024,SR,256,1024,center=False); ids=row["ids"]
        return Batch(torch.tensor([ids],dtype=torch.long,device=device),torch.tensor([len(ids)],device=device),spec,torch.tensor([spec.shape[-1]],device=device),audio.unsqueeze(1),torch.tensor([audio.shape[-1]],device=device),None)
    @torch.inference_mode()
    def infer(ids:list[int],seed:int)->np.ndarray:
        model.eval(); torch.manual_seed(seed)
        if device.type=="cuda": torch.cuda.manual_seed_all(seed)
        x=torch.tensor([ids],dtype=torch.long,device=device); xl=torch.tensor([len(ids)],dtype=torch.long,device=device)
        return model.model_g.infer(x,xl,noise_scale=0.667,length_scale=1.0,noise_scale_w=0.8)[0][0,0].detach().float().cpu().numpy()
    def eval_gate(seed_base:int,persist_dir:Path|None=None)->list[dict]:
        snap=torch_rng_snapshot()
        try:
            rows=[]
            for i,r in enumerate(acceptance):
                audio=infer(r["phoneme_ids"],seed_base+i); st=write_wav(persist_dir/r["audio_filename"],audio) if persist_dir else stats_from_audio(audio); status,notes=machine_status(st); rows.append({"acceptance_row_id":r["acceptance_row_id"],"source_utterance_id":r["source_utterance_id"],"tier":r["tier"],"dwc_text":r["dwc_text"],"seed":seed_base+i,**st,"status":status,"notes":notes,"audio_filename":r["audio_filename"] if persist_dir else ""})
            return rows
        finally: torch_rng_restore(snap)
    seed_bases=[args.seed+3000+1000*k for k in range(5)]
    def robust_gate(label:str,persist_primary:bool=False)->list[dict]:
        summaries=[]
        for j,sb in enumerate(seed_bases,1):
            pdir=out/"wav"/label if (persist_primary and j==1) else None; rows=eval_gate(sb,pdir); write_tsv(out/f"{label}_seed{j}.tsv",rows); summaries.append({"seed_index":j,"seed_base":sb,**summarize(rows)})
        return summaries
    pre_gate=robust_gate("R2C_pre")
    if any(s["pass"]!=125 for s in pre_gate): raise SystemExit(f"R2C repaired batch384 candidate failed pre-gate: {pre_gate}")
    probe_rows=[acceptance[i] for i in [0,5,15,25,40,60,85,110]]; probe_seeds=[args.seed+1000+i for i in range(len(probe_rows))]
    def fixed_probe()->list[dict]:
        snap=torch_rng_snapshot()
        try:
            vals=[]
            for r,seed in zip(probe_rows,probe_seeds): vals.append({"acceptance_row_id":r["acceptance_row_id"],"source_utterance_id":r["source_utterance_id"],**stats_from_audio(infer(r["phoneme_ids"],seed))})
            return vals
        finally: torch_rng_restore(snap)
    baseline_probe=fixed_probe(); baseline_by_id={r["acceptance_row_id"]:r for r in baseline_probe}; baseline_median=float(np.median([r["rms_dbfs"] for r in baseline_probe])); median_floor=max(RMS_FLOOR_DBFS,baseline_median-args.max_probe_drop_db)
    rng=random.Random(args.seed); full_schedule=list(corpus); rng.shuffle(full_schedule); schedule=full_schedule[FIRST_COMPLETED:]
    if len(schedule)!=TOTAL_ROWS-FIRST_COMPLETED: raise SystemExit("remaining schedule length mismatch")
    write_tsv(out/"R2C_schedule_manifest.tsv",[{"global_batch":i+1,"corpus_row_id":r["corpus_row_id"],"source_utterance_id":r["source_utterance_id"],"status":"already_in_r2c_source_state" if i<FIRST_COMPLETED else "to_train_r2c"} for i,r in enumerate(full_schedule)])
    torch.manual_seed(args.seed+900000)
    if device.type=="cuda": torch.cuda.manual_seed_all(args.seed+900000)
    random.seed(args.seed+900000); np.random.seed((args.seed+900000)%(2**32-1))
    guard_events=[]; start=time.time(); metrics_path=out/"R2C_PROTECTED_metrics.jsonl"; rolling_resume=out/"R2C_RESUME_LATEST.pt"
    def save_resume(global_batch:int)->dict:
        payload={"model_state_dict":{k:v.detach().cpu() for k,v in model.state_dict().items()},"optimizer_g_state_dict":opt_g.state_dict(),"optimizer_d_state_dict":opt_d.state_dict(),"torch_rng_state":torch.get_rng_state(),"cuda_rng_state_all":torch.cuda.get_rng_state_all() if device.type=="cuda" else None,"python_random_state":random.getstate(),"numpy_random_state":np.random.get_state(),"num_symbols":NUM_SYMBOLS,"sample_rate":SR,"status":"R2C_ROLLING_RESUME","phase":"R2C_PROTECTED","phase_batch":global_batch,"source_candidate_sha256":source_candidate["sha256"],"optimizer_state_restored":False,"optimizer_state_saved":True,"protected_hashes":protected_hashes}
        tmp=rolling_resume.with_suffix(".tmp"); torch.save(payload,tmp); tmp.replace(rolling_resume); return {"file":rolling_resume.name,"bytes":rolling_resume.stat().st_size,"sha256":sha256_file(rolling_resume),"phase_batch":global_batch}
    def save_model_checkpoint(path:Path,global_batch:int,status:str,reason:str|None=None)->dict:
        torch.save({"model_state_dict":{k:v.detach().cpu() for k,v in model.state_dict().items()},"num_symbols":NUM_SYMBOLS,"sample_rate":SR,"status":status,"phase":"R2C_PROTECTED","phase_batch":global_batch,"reason":reason,"source_candidate_sha256":source_candidate["sha256"],"optimizer_state_restored":False,"protected_hashes":protected_hashes},path); return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha256_file(path)}
    def abort(reason:str,global_batch:int,detail:dict)->None:
        hashes=current_protected_hashes(); ck=save_model_checkpoint(out/f"ABORT_R2C_PROTECTED_batch{global_batch:04d}.pt",global_batch,"ABORT_R2C_PROTECTED_GUARD",reason); resume=save_resume(global_batch); report={"schema_version":"0.1.0","status":"ABORT_R2C_PROTECTED_GUARD","training_performed":True,"r2_complete":False,"human_perceptual_gate":"NOT_RUN","reason":reason,"phase_batch":global_batch,"detail":detail,"checkpoint":ck,"rolling_resume":resume,"source_candidate":source_candidate,"protected_hashes_initial":protected_hashes,"protected_hashes_at_abort":hashes,"pre_five_seed_gate":pre_gate,"guard_events":guard_events,"optimizer_state_restored":False,"optimizer_state_saved_at_abort":True}; (out/"R2C_PROTECTED_RESULT.json").write_text(json.dumps(report,indent=2),encoding="utf-8"); raise GuardAbort(reason)
    try:
        with metrics_path.open("w",encoding="utf-8") as mf:
            for global_batch,row in enumerate(schedule,FIRST_COMPLETED+1):
                model.train(); loss_g,loss_d,met=model._compute_loss(make_batch(row)); opt_g.zero_grad(set_to_none=True); loss_g.backward()
                if any(p.grad is not None for p in model.model_g.flow.parameters()): abort("frozen_flow_received_gradient",global_batch,{})
                if any(p.grad is not None for p in model.model_g.dp.parameters()): abort("frozen_dp_received_gradient",global_batch,{})
                if any(p.grad is not None for p in model.model_g.enc_p.parameters()): abort("frozen_enc_p_received_gradient",global_batch,{})
                opt_g.step(); opt_d.zero_grad(set_to_none=True); loss_d.backward(); opt_d.step(); rec={"phase":"R2C_PROTECTED","global_batch":global_batch,"continuation_batch":global_batch-FIRST_COMPLETED,"corpus_row_id":row["corpus_row_id"],"source_utterance_id":row["source_utterance_id"],"elapsed_s":round(time.time()-start,3),"loss_g":float(loss_g.detach().cpu()),"loss_d":float(loss_d.detach().cpu()),"train_mel":float(met["mel"]),"train_kl":float(met["kl"]),"train_dur":float(met["dur"])}; mf.write(json.dumps(rec)+"\n"); mf.flush()
                if global_batch==FIRST_COMPLETED+1 or global_batch%args.probe_every==0 or global_batch==TOTAL_ROWS:
                    hashes=current_protected_hashes()
                    if hashes!=protected_hashes: abort("protected_prefix_hash_changed",global_batch,{"expected":protected_hashes,"actual":hashes})
                    current=fixed_probe(); violations=[]
                    for cur in current:
                        base=baseline_by_id[cur["acceptance_row_id"]]; drop=float(base["rms_dbfs"]-cur["rms_dbfs"])
                        if cur["rms_dbfs"]<RMS_FLOOR_DBFS or drop>args.max_probe_drop_db: violations.append({"acceptance_row_id":cur["acceptance_row_id"],"source_utterance_id":cur["source_utterance_id"],"baseline_rms_dbfs":base["rms_dbfs"],"current_rms_dbfs":cur["rms_dbfs"],"drop_db":drop})
                    median=float(np.median([r["rms_dbfs"] for r in current])); event={"kind":"fixed_probe","global_batch":global_batch,"median_rms_dbfs":median,"median_floor_dbfs":median_floor,"violations":violations,"rows":current}; guard_events.append(event)
                    if violations or median<median_floor: abort("fixed_probe_amplitude_guard",global_batch,event)
                if global_batch%args.primary_gate_every==0 or global_batch==TOTAL_ROWS:
                    rows=eval_gate(seed_bases[0]); s=summarize(rows); event={"kind":"primary_125_gate","global_batch":global_batch,"summary":s}; guard_events.append(event); write_tsv(out/f"R2C_batch{global_batch:04d}_primary_gate.tsv",rows)
                    if s["pass"]!=125: abort("intermediate_primary_125_gate",global_batch,event)
                if global_batch%args.robust_gate_every==0 and global_batch<TOTAL_ROWS:
                    rs=robust_gate(f"R2C_batch{global_batch:04d}_robust"); event={"kind":"five_seed_125_gate","global_batch":global_batch,"summaries":rs}; guard_events.append(event)
                    if any(s["pass"]!=125 for s in rs): abort("intermediate_five_seed_125_gate",global_batch,event)
                    save_resume(global_batch)
    except GuardAbort: raise SystemExit(12)
    hashes=current_protected_hashes()
    if hashes!=protected_hashes: abort("final_protected_prefix_hash_changed",TOTAL_ROWS,{"expected":protected_hashes,"actual":hashes})
    final_gate=robust_gate("R2C_final",persist_primary=True)
    if any(s["pass"]!=125 for s in final_gate): abort("final_five_seed_125_gate",TOTAL_ROWS,{"summaries":final_gate})
    final_ck=save_model_checkpoint(out/"R2C_PROTECTED_weights_batch0799.pt",TOTAL_ROWS,"PASS_R2C_PROTECTED_MACHINE_GATE"); resume=save_resume(TOTAL_ROWS); report={"schema_version":"0.1.0","status":"PASS_R2C_PROTECTED_MACHINE_GATE","training_performed":True,"r2_complete":True,"r2_total_schedule_rows_covered":TOTAL_ROWS,"r2c_rows_trained":TOTAL_ROWS-FIRST_COMPLETED,"prior_rows_retained_from_repaired_batch384":FIRST_COMPLETED,"optimizer_state_restored":False,"optimizer_state_saved":True,"source_candidate":source_candidate,"final_checkpoint":final_ck,"rolling_resume":resume,"protected_modules":["model_g.flow","model_g.dp","model_g.enc_p"],"protected_hashes_initial":protected_hashes,"protected_hashes_final":hashes,"pre_five_seed_gate":pre_gate,"final_five_seed_gate":final_gate,"guard_events":guard_events,"human_perceptual_gate":"NOT_RUN","interpretation_boundary":"Machine success only. Proceed to separate human CNS perceptual acceptance; do not claim canonical human-quality speech from this script."}; (out/"R2C_PROTECTED_RESULT.json").write_text(json.dumps(report,indent=2),encoding="utf-8"); print(json.dumps(report,indent=2))
if __name__=="__main__": main()
