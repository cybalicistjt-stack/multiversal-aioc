#!/usr/bin/env python3
"""Inference-only diagnostic for the completed DWC repaired-corpus R1 checkpoint.

This script NEVER trains or updates model weights. It:
1) loads the completed exact-58 R1 checkpoint,
2) uses a repaired 125-row acceptance table with unique governed row IDs and filenames,
3) reproduces the original default R1 machine gate using the original seed schedule,
4) runs a five-seed robustness sweep at the original inference settings,
5) runs a bounded inference-noise ablation grid to separate duration-noise and latent-noise effects,
6) writes machine-readable diagnostic evidence.

It does not authorize R2 or human acceptance.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
import types
import wave
from pathlib import Path

import numpy as np
import torch

NUM_SYMBOLS = 58
SR = 22050
RMS_FLOOR_DBFS = -55.0
CLIP_FLOOR_DBFS = -0.05
DEFAULT_SEED = 20260908


def sha256_file(path: Path, chunk: int = 16 * 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()


def dbfs(v: float) -> float:
    return 20.0 * math.log10(max(float(v), 1e-12))


def stats_from_audio(audio: np.ndarray) -> dict:
    x = np.asarray(audio, dtype=np.float32).reshape(-1)
    peak = float(np.max(np.abs(x))) if x.size else 0.0
    rms = float(np.sqrt(np.mean(np.square(x)))) if x.size else 0.0
    return {"duration_s": float(len(x) / SR), "peak": peak, "rms": rms, "peak_dbfs": dbfs(peak), "rms_dbfs": dbfs(rms)}


def machine_status(st: dict) -> tuple[str, str]:
    notes: list[str] = []
    if st["duration_s"] < 0.08:
        notes.append("duration")
    if st["peak_dbfs"] > CLIP_FLOOR_DBFS:
        notes.append("clipping")
    if st["rms_dbfs"] < RMS_FLOOR_DBFS:
        notes.append("low_level")
    return ("PASS" if not notes else "FAIL", ";".join(notes))


def write_wav(path: Path, audio: np.ndarray) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    x = np.asarray(audio, dtype=np.float32).reshape(-1)
    pcm = (np.clip(x, -1.0, 1.0) * 32767.0).astype("<i2")
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    return stats_from_audio(pcm.astype(np.float32) / 32768.0)


def install_stubs() -> None:
    if "pysilero_vad" not in sys.modules:
        m = types.ModuleType("pysilero_vad")
        class DummyVAD: pass
        m.SileroVoiceActivityDetector = DummyVAD
        sys.modules["pysilero_vad"] = m
    if "pathvalidate" not in sys.modules:
        m = types.ModuleType("pathvalidate")
        m.sanitize_filename = lambda s, *a, **k: s
        sys.modules["pathvalidate"] = m


def load_acceptance(path: Path) -> list[dict]:
    rows = list(csv.DictReader(path.open(encoding="utf-8"), delimiter="\t"))
    if len(rows) != 125:
        raise SystemExit(f"acceptance rows must be 125; got {len(rows)}")
    required = {"acceptance_row_id","source_utterance_id","tier","dwc_text","ipa","phoneme_id_sequence","audio_filename"}
    if not rows or not required.issubset(rows[0]):
        raise SystemExit(f"acceptance table missing fields: {sorted(required - set(rows[0] if rows else []))}")
    ids = [r["acceptance_row_id"] for r in rows]
    wavs = [r["audio_filename"] for r in rows]
    if len(set(ids)) != 125: raise SystemExit("acceptance_row_id values are not unique")
    if len(set(wavs)) != 125: raise SystemExit("acceptance audio filenames are not unique")
    for r in rows:
        pids = [int(x) for x in r["phoneme_id_sequence"].split()]
        if not pids or min(pids) < 0 or max(pids) >= NUM_SYMBOLS:
            raise SystemExit(f"bad exact-ID sequence: {r['acceptance_row_id']}")
        r["phoneme_ids"] = pids
    return rows


def write_tsv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader(); w.writerows(rows)


def summarize(rows: list[dict]) -> dict:
    vals = [float(r["rms_dbfs"]) for r in rows]
    statuses = [r["status"] for r in rows]
    return {"rows":len(rows),"pass":sum(s=="PASS" for s in statuses),"fail":sum(s!="PASS" for s in statuses),"rms_dbfs_median":float(np.median(vals)),"rms_dbfs_min":float(min(vals)),"rms_dbfs_max":float(max(vals)),"below_minus55":int(sum(v < -55.0 for v in vals)),"below_minus60":int(sum(v < -60.0 for v in vals)),"below_minus65":int(sum(v < -65.0 for v in vals)),"below_minus70":int(sum(v < -70.0 for v in vals))}


def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("--piper-src",required=True); ap.add_argument("--r1-checkpoint",required=True); ap.add_argument("--acceptance-tsv",required=True); ap.add_argument("--output-dir",required=True); ap.add_argument("--prior-manifest"); ap.add_argument("--device",default="cuda"); ap.add_argument("--seed",type=int,default=DEFAULT_SEED); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True); ckpt_path=Path(args.r1_checkpoint)
    if not ckpt_path.exists(): raise SystemExit(f"missing R1 checkpoint: {ckpt_path}")
    acc=load_acceptance(Path(args.acceptance_tsv)); device=torch.device(args.device)
    if device.type=="cuda" and not torch.cuda.is_available(): raise SystemExit("CUDA requested but unavailable")
    sys.path.insert(0,str(Path(args.piper_src)/"src")); install_stubs(); from piper.train.vits.lightning import VitsModel
    payload=torch.load(ckpt_path,map_location="cpu",weights_only=False)
    if int(payload.get("num_symbols",-1))!=NUM_SYMBOLS: raise SystemExit(f"R1 checkpoint num_symbols={payload.get('num_symbols')} expected {NUM_SYMBOLS}")
    if int(payload.get("sample_rate",-1))!=SR: raise SystemExit(f"R1 checkpoint sample_rate={payload.get('sample_rate')} expected {SR}")
    model=VitsModel(num_symbols=NUM_SYMBOLS,num_speakers=1,batch_size=1,mos_metric="none")
    missing,unexpected=model.load_state_dict(payload["model_state_dict"],strict=False)
    if missing or unexpected: raise SystemExit(f"R1 state mismatch: missing={missing[:20]} unexpected={unexpected[:20]}")
    model.to(device); model.eval()

    @torch.inference_mode()
    def infer(ids:list[int],seed:int,noise_scale:float,noise_scale_w:float)->np.ndarray:
        torch.manual_seed(seed)
        if device.type=="cuda": torch.cuda.manual_seed_all(seed)
        x=torch.tensor([ids],dtype=torch.long,device=device); xl=torch.tensor([len(ids)],dtype=torch.long,device=device)
        return model.model_g.infer(x,xl,noise_scale=noise_scale,length_scale=1.0,noise_scale_w=noise_scale_w)[0][0,0].detach().float().cpu().numpy()

    def eval_rows(label:str,seed_base:int,noise_scale:float,noise_scale_w:float,persist_wavs:bool)->list[dict]:
        result=[]; wav_dir=out/"wav"/label
        for i,r in enumerate(acc):
            audio=infer(r["phoneme_ids"],seed_base+i,noise_scale,noise_scale_w)
            st=write_wav(wav_dir/r["audio_filename"],audio) if persist_wavs else stats_from_audio(audio)
            status,notes=machine_status(st)
            result.append({"acceptance_row_id":r["acceptance_row_id"],"source_utterance_id":r["source_utterance_id"],"tier":r["tier"],"dwc_text":r["dwc_text"],"ipa":r["ipa"],"phoneme_id_sequence":r["phoneme_id_sequence"],"seed":seed_base+i,"noise_scale":noise_scale,"noise_scale_w":noise_scale_w,**st,"status":status,"notes":notes,"audio_filename":r["audio_filename"] if persist_wavs else ""})
        write_tsv(out/f"{label}.tsv",result,list(result[0].keys())); return result

    reproduction=eval_rows("default_reproduction",args.seed+3000,0.667,0.8,True); reproduction_summary=summarize(reproduction)
    prior_check=None
    if args.prior_manifest:
        prior=list(csv.DictReader(Path(args.prior_manifest).open(encoding="utf-8"),delimiter="\t"))
        if len(prior)!=125: raise SystemExit(f"prior manifest rows={len(prior)}, expected 125")
        diffs=[]; mismatch=[]
        for i,(old,new) in enumerate(zip(prior,reproduction)):
            diffs.append(abs(float(new["rms_dbfs"])-float(old["rms_dbfs"])))
            if new["status"]!=old["status"]: mismatch.append({"row":i+1,"acceptance_row_id":new["acceptance_row_id"],"old_status":old["status"],"new_status":new["status"],"old_rms_dbfs":float(old["rms_dbfs"]),"new_rms_dbfs":float(new["rms_dbfs"])})
        prior_check={"rows":125,"status_mismatch_count":len(mismatch),"max_abs_rms_delta_db":max(diffs),"status_mismatches":mismatch}

    seed_bases=[args.seed+3000+1000*k for k in range(5)]; seed_summaries=[]; records={r["acceptance_row_id"]:[] for r in acc}
    for j,sb in enumerate(seed_bases,1):
        rows=eval_rows(f"seed_sweep_{j}",sb,0.667,0.8,False); seed_summaries.append({"seed_base":sb,**summarize(rows)})
        for r in rows: records[r["acceptance_row_id"]].append(r)
    robust=[]
    for r in acc:
        rs=records[r["acceptance_row_id"]]; vals=[float(x["rms_dbfs"]) for x in rs]; passes=sum(x["status"]=="PASS" for x in rs)
        robust.append({"acceptance_row_id":r["acceptance_row_id"],"source_utterance_id":r["source_utterance_id"],"dwc_text":r["dwc_text"],"passes_of_5":passes,"fails_of_5":5-passes,"rms_dbfs_min":min(vals),"rms_dbfs_median":float(np.median(vals)),"rms_dbfs_max":max(vals),"rms_range_db":max(vals)-min(vals)})
    write_tsv(out/"seed_robustness.tsv",robust,list(robust[0].keys()))

    configs=[("default",0.667,0.8),("no_duration_noise",0.667,0.0),("no_latent_noise",0.0,0.8),("reduced_noise",0.35,0.4),("deterministic_zero_noise",0.0,0.0)]; config_summaries=[]
    for name,ns,nsw in configs:
        rows=eval_rows(f"config_{name}",args.seed+3000,ns,nsw,False); config_summaries.append({"name":name,"noise_scale":ns,"noise_scale_w":nsw,**summarize(rows)})

    summary={"schema_version":"0.1.0","status":"INFERENCE_DIAGNOSTIC_COMPLETE","training_performed":False,"r2_authorized_by_this_script":False,"human_gate_authorized_by_this_script":False,"r1_checkpoint":{"file":ckpt_path.name,"bytes":ckpt_path.stat().st_size,"sha256":sha256_file(ckpt_path),"num_symbols":int(payload.get("num_symbols",-1)),"sample_rate":int(payload.get("sample_rate",-1))},"acceptance":{"file":Path(args.acceptance_tsv).name,"sha256":sha256_file(Path(args.acceptance_tsv)),"rows":125,"unique_acceptance_row_ids":125,"unique_output_filenames":125},"default_reproduction":reproduction_summary,"prior_manifest_comparison":prior_check,"seed_sweep":seed_summaries,"seed_robustness":{"always_pass_5_of_5":sum(r["passes_of_5"]==5 for r in robust),"always_fail_0_of_5":sum(r["passes_of_5"]==0 for r in robust),"seed_sensitive_1_to_4_passes":sum(0<r["passes_of_5"]<5 for r in robust)},"inference_noise_ablation":config_summaries,"interpretation_boundary":"Diagnostic only. Do not enter R2 or resume training from this script's output. Review results and explicitly authorize the next governed experiment."}
    (out/"R1_INFERENCE_DIAGNOSTIC_SUMMARY.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    hashes=[]
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.name!="SHA256SUMS.txt": hashes.append(f"{sha256_file(p)}  {p.relative_to(out)}")
    (out/"SHA256SUMS.txt").write_text("\n".join(hashes)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))

if __name__=="__main__": main()
