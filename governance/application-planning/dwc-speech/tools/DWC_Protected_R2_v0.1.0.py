#!/usr/bin/env python3
"""Protected DWC R2 continuation from the promoted R1+warm-flow hybrid.

Governed behavior:
- starts only from a previously promoted flow-restored R1 checkpoint;
- freezes model_g.flow for the entire R2 stage;
- performs one deterministic shuffled pass over all 799 repaired corpus rows;
- applies fixed-seed row-level amplitude guards every 8 batches;
- applies a full corrected 125-row primary machine gate every 64 batches;
- aborts immediately and preserves a diagnostic checkpoint if any guard regresses;
- applies a five-seed 125/125 machine gate at the end;
- never performs or claims human CNS perceptual acceptance.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math, random, sys, time, types, wave
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

def wav_stats(path: Path) -> dict:
    with wave.open(str(path), "rb") as w:
        ch, sw, sr, n = w.getnchannels(), w.getsampwidth(), w.getframerate(), w.getnframes()
        raw = w.readframes(n)
    if not (ch == 1 and sw == 2 and sr == SR):
        raise ValueError(f"bad WAV format {path.name}: ch={ch} sw={sw} sr={sr}")
    x = np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32768.0
    peak = float(np.max(np.abs(x))) if x.size else 0.0
    rms = float(np.sqrt(np.mean(np.square(x)))) if x.size else 0.0
    return {"duration_s": len(x) / sr if sr else 0.0, "peak_dbfs": dbfs(peak), "rms_dbfs": dbfs(rms)}

def stats_from_audio(audio: np.ndarray) -> dict:
    x = np.asarray(audio, dtype=np.float32).reshape(-1)
    peak = float(np.max(np.abs(x))) if x.size else 0.0
    rms = float(np.sqrt(np.mean(np.square(x)))) if x.size else 0.0
    return {"duration_s": float(len(x) / SR), "peak_dbfs": dbfs(peak), "rms_dbfs": dbfs(rms)}

def write_wav(path: Path, audio: np.ndarray) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    x = np.asarray(audio, dtype=np.float32).reshape(-1)
    pcm = (np.clip(x, -1.0, 1.0) * 32767.0).astype("<i2")
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    return wav_stats(path)

def machine_status(st: dict) -> tuple[str, str]:
    notes = []
    if st["duration_s"] < 0.08: notes.append("duration")
    if st["peak_dbfs"] > CLIP_FLOOR_DBFS: notes.append("clipping")
    if st["rms_dbfs"] < RMS_FLOOR_DBFS: notes.append("low_level")
    return ("PASS" if not notes else "FAIL", ";".join(notes))

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

def load_corpus(root: Path) -> list[dict]:
    manifest = list(csv.DictReader((root / "SYNTHETIC_BOOTSTRAP_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\t"))
    lines = (root / "piper_synthetic_bootstrap_custom_ids.csv").read_text(encoding="utf-8").splitlines()
    if len(manifest) != 799 or len(lines) != 799:
        raise SystemExit(f"expected 799 repaired corpus rows: manifest={len(manifest)} csv={len(lines)}")
    by_filename = {r["piper_audio_filename"]: r for r in manifest}
    if len(by_filename) != 799 or len({r["corpus_row_id"] for r in manifest}) != 799:
        raise SystemExit("repaired corpus identity collision")
    rows = []
    for i, line in enumerate(lines, 1):
        parts = line.split("|")
        if len(parts) != 3: raise SystemExit(f"bad corpus csv row {i}")
        fn, text, ids_s = parts
        ids = [int(x) for x in ids_s.split()]
        if not ids or min(ids) < 0 or max(ids) >= NUM_SYMBOLS: raise SystemExit(f"bad IDs at corpus row {i}")
        m = by_filename.get(fn)
        if m is None: raise SystemExit(f"corpus filename missing from manifest: {fn}")
        wav = root / "audio_22050" / fn
        if not wav.exists(): raise SystemExit(f"missing corpus WAV: {wav}")
        st = wav_stats(wav); status, notes = machine_status(st)
        if status != "PASS": raise SystemExit(f"corpus target gate failed: {fn}: {notes}: {st}")
        rows.append({"file": fn, "text": text, "ids": ids, "corpus_row_id": m["corpus_row_id"], "source_utterance_id": m["source_utterance_id"]})
    return rows

def load_acceptance(path: Path) -> list[dict]:
    rows = list(csv.DictReader(path.open(encoding="utf-8"), delimiter="\t"))
    required = {"acceptance_row_id", "source_utterance_id", "tier", "dwc_text", "ipa", "phoneme_id_sequence", "audio_filename"}
    if len(rows) != 125: raise SystemExit(f"acceptance rows={len(rows)} expected 125")
    if not required.issubset(rows[0] if rows else {}): raise SystemExit("acceptance fields missing")
    if len({r["acceptance_row_id"] for r in rows}) != 125 or len({r["audio_filename"] for r in rows}) != 125:
        raise SystemExit("acceptance identity/output filename collision")
    for r in rows:
        ids = [int(x) for x in r["phoneme_id_sequence"].split()]
        if not ids or min(ids) < 0 or max(ids) >= NUM_SYMBOLS: raise SystemExit(f"bad acceptance IDs: {r['acceptance_row_id']}")
        r["phoneme_ids"] = ids
    return rows

def state_prefix_sha256(state: dict, prefix: str) -> str:
    h = hashlib.sha256()
    for k in sorted(k for k in state if k.startswith(prefix)):
        t = state[k].detach().cpu().contiguous()
        h.update(k.encode("utf-8")); h.update(str(tuple(t.shape)).encode("ascii")); h.update(str(t.dtype).encode("ascii")); h.update(t.numpy().tobytes())
    return h.hexdigest()

def save_state(model, path: Path, meta: dict) -> dict:
    payload = {"model_state_dict": {k: v.detach().cpu() for k, v in model.state_dict().items()}, "num_symbols": NUM_SYMBOLS, "sample_rate": SR, **meta}
    torch.save(payload, path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha256_file(path)}

def summarize(rows: list[dict]) -> dict:
    vals = [float(r["rms_dbfs"]) for r in rows]
    return {"rows": len(rows), "pass": sum(r["status"] == "PASS" for r in rows), "fail": sum(r["status"] != "PASS" for r in rows), "rms_dbfs_median": float(np.median(vals)), "rms_dbfs_min": float(min(vals)), "rms_dbfs_max": float(max(vals)), "below_minus55": int(sum(v < RMS_FLOOR_DBFS for v in vals))}

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--piper-src", required=True); ap.add_argument("--checkpoint", required=True)
    ap.add_argument("--corpus-root", required=True); ap.add_argument("--acceptance-tsv", required=True)
    ap.add_argument("--output-dir", required=True); ap.add_argument("--device", default="cuda")
    ap.add_argument("--seed", type=int, default=DEFAULT_SEED); ap.add_argument("--probe-every", type=int, default=8)
    ap.add_argument("--full-gate-every", type=int, default=64); ap.add_argument("--checkpoint-every", type=int, default=128)
    ap.add_argument("--max-probe-drop-db", type=float, default=18.0)
    args = ap.parse_args()
    out = Path(args.output_dir); out.mkdir(parents=True, exist_ok=True)
    ckpt_path = Path(args.checkpoint)
    if not ckpt_path.exists(): raise SystemExit(f"missing promoted hybrid checkpoint: {ckpt_path}")
    corpus = load_corpus(Path(args.corpus_root)); acceptance = load_acceptance(Path(args.acceptance_tsv))
    device = torch.device(args.device)
    if device.type == "cuda" and not torch.cuda.is_available(): raise SystemExit("CUDA requested but unavailable")
    sys.path.insert(0, str(Path(args.piper_src) / "src")); install_stubs()
    from piper.train.vits.lightning import VitsModel
    from piper.train.vits.dataset import Batch
    from piper.train.vits.mel_processing import spectrogram_torch
    payload = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    if int(payload.get("num_symbols", -1)) != NUM_SYMBOLS or int(payload.get("sample_rate", -1)) != SR: raise SystemExit("hybrid checkpoint metadata mismatch")
    model = VitsModel(num_symbols=NUM_SYMBOLS, num_speakers=1, batch_size=1, mos_metric="none")
    missing, unexpected = model.load_state_dict(payload["model_state_dict"], strict=False)
    if missing or unexpected: raise SystemExit(f"checkpoint state mismatch missing={missing[:20]} unexpected={unexpected[:20]}")
    model.to(device)
    for p in model.model_g.flow.parameters(): p.requires_grad_(False)
    if any(p.requires_grad for p in model.model_g.flow.parameters()): raise SystemExit("failed to freeze model_g.flow")
    flow_hash_initial = state_prefix_sha256(model.state_dict(), "model_g.flow.")
    trainable_g = [p for p in model.model_g.parameters() if p.requires_grad]
    opt_g = torch.optim.AdamW(trainable_g, lr=model.hparams.learning_rate, betas=model.hparams.betas, eps=model.hparams.eps)
    opt_d = torch.optim.AdamW(model.model_d.parameters(), lr=model.hparams.learning_rate_d, betas=model.hparams.betas_d, eps=model.hparams.eps)
    def make_batch(row: dict):
        wav = Path(args.corpus_root) / "audio_22050" / row["file"]
        with wave.open(str(wav), "rb") as w: raw = w.readframes(w.getnframes())
        arr = np.frombuffer(raw, dtype="<i2").astype("float32") / 32768.0
        audio = torch.from_numpy(arr).to(device).unsqueeze(0)
        if audio.shape[-1] < 8192: audio = torch.nn.functional.pad(audio, (0, 8192 - audio.shape[-1]))
        spec = spectrogram_torch(audio, 1024, SR, 256, 1024, center=False); ids = row["ids"]
        return Batch(torch.tensor([ids], dtype=torch.long, device=device), torch.tensor([len(ids)], device=device), spec, torch.tensor([spec.shape[-1]], device=device), audio.unsqueeze(1), torch.tensor([audio.shape[-1]], device=device), None)
    @torch.inference_mode()
    def infer(ids: list[int], seed: int) -> np.ndarray:
        model.eval(); torch.manual_seed(seed)
        if device.type == "cuda": torch.cuda.manual_seed_all(seed)
        x = torch.tensor([ids], dtype=torch.long, device=device); xl = torch.tensor([len(ids)], dtype=torch.long, device=device)
        return model.model_g.infer(x, xl, noise_scale=0.667, length_scale=1.0, noise_scale_w=0.8)[0][0, 0].detach().float().cpu().numpy()
    def eval_gate(seed_base: int, persist_dir: Path | None = None) -> list[dict]:
        rows = []
        for i, r in enumerate(acceptance):
            audio = infer(r["phoneme_ids"], seed_base + i)
            st = write_wav(persist_dir / r["audio_filename"], audio) if persist_dir else stats_from_audio(audio)
            status, notes = machine_status(st)
            rows.append({"acceptance_row_id": r["acceptance_row_id"], "source_utterance_id": r["source_utterance_id"], "tier": r["tier"], "dwc_text": r["dwc_text"], "seed": seed_base + i, **st, "status": status, "notes": notes, "audio_filename": r["audio_filename"] if persist_dir else ""})
        return rows
    seed_bases = [args.seed + 3000 + 1000 * k for k in range(5)]
    start_seed_summaries = []
    for sb in seed_bases:
        s = summarize(eval_gate(sb)); start_seed_summaries.append({"seed_base": sb, **s})
        if s["pass"] != 125: raise SystemExit(f"promoted hybrid failed pre-R2 robust gate at seed_base={sb}: {s}")
    probe_rows = [acceptance[i] for i in [0, 5, 15, 25, 40, 60, 85, 110]]
    def fixed_probe() -> list[dict]:
        vals = []
        for i, r in enumerate(probe_rows):
            st = stats_from_audio(infer(r["phoneme_ids"], args.seed + 1000 + i))
            vals.append({"acceptance_row_id": r["acceptance_row_id"], "source_utterance_id": r["source_utterance_id"], **st})
        return vals
    baseline_probe = fixed_probe(); baseline_by_id = {r["acceptance_row_id"]: r for r in baseline_probe}
    baseline_median = float(np.median([r["rms_dbfs"] for r in baseline_probe])); median_floor = max(RMS_FLOOR_DBFS, baseline_median - args.max_probe_drop_db)
    rng = random.Random(args.seed); schedule = list(corpus); rng.shuffle(schedule)
    metrics_path = out / "R2_PROTECTED_metrics.jsonl"; checkpoints = []; guard_events = []; start = time.time()
    def abort(reason: str, batch: int, detail: dict) -> None:
        ck = save_state(model, out / f"ABORT_R2_PROTECTED_batch{batch:04d}.pt", {"status": "ABORT_PROTECTED_R2_GUARD", "phase": "R2_PROTECTED", "phase_batch": batch, "reason": reason, "detail": detail, "source_checkpoint_sha256": sha256_file(ckpt_path), "flow_frozen": True, "flow_hash_initial": flow_hash_initial})
        report = {"status": "ABORT_PROTECTED_R2_GUARD", "training_performed": True, "r2_complete": False, "human_perceptual_gate": "NOT_RUN", "reason": reason, "phase_batch": batch, "detail": detail, "checkpoint": ck, "flow_hash_initial": flow_hash_initial, "flow_hash_at_abort": state_prefix_sha256(model.state_dict(), "model_g.flow."), "start_five_seed_gate": start_seed_summaries, "guard_events": guard_events}
        (out / "R2_PROTECTED_RESULT.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        raise SystemExit(f"PROTECTED R2 ABORT: {reason} at batch {batch}; checkpoint={ck['file']}")
    model.train()
    with metrics_path.open("w", encoding="utf-8") as mf:
        for batch, row in enumerate(schedule, 1):
            model.train(); loss_g, loss_d, met = model._compute_loss(make_batch(row))
            opt_g.zero_grad(set_to_none=True); loss_g.backward()
            if any(p.grad is not None for p in model.model_g.flow.parameters()): abort("frozen_flow_received_gradient", batch, {})
            opt_g.step(); opt_d.zero_grad(set_to_none=True); loss_d.backward(); opt_d.step()
            rec = {"phase": "R2_PROTECTED", "phase_batch": batch, "corpus_row_id": row["corpus_row_id"], "source_utterance_id": row["source_utterance_id"], "elapsed_s": round(time.time() - start, 3), "loss_g": float(loss_g.detach().cpu()), "loss_d": float(loss_d.detach().cpu()), "train_mel": float(met["mel"]), "train_kl": float(met["kl"]), "train_dur": float(met["dur"])}
            mf.write(json.dumps(rec) + "\n"); mf.flush()
            if batch == 1 or batch % args.probe_every == 0 or batch == len(schedule):
                current = fixed_probe(); violations = []
                for cur in current:
                    base = baseline_by_id[cur["acceptance_row_id"]]; drop = float(base["rms_dbfs"] - cur["rms_dbfs"])
                    if cur["rms_dbfs"] < RMS_FLOOR_DBFS or drop > args.max_probe_drop_db:
                        violations.append({"acceptance_row_id": cur["acceptance_row_id"], "source_utterance_id": cur["source_utterance_id"], "baseline_rms_dbfs": base["rms_dbfs"], "current_rms_dbfs": cur["rms_dbfs"], "drop_db": drop})
                median = float(np.median([r["rms_dbfs"] for r in current])); event = {"kind": "fixed_probe", "batch": batch, "median_rms_dbfs": median, "median_floor_dbfs": median_floor, "violations": violations, "rows": current}; guard_events.append(event)
                if median < median_floor: abort("median_probe_guard", batch, event)
                if violations: abort("row_level_probe_guard", batch, event)
            if batch % args.full_gate_every == 0 and batch < len(schedule):
                s = summarize(eval_gate(args.seed + 3000)); event = {"kind": "primary_125_gate", "batch": batch, **s}; guard_events.append(event)
                if s["pass"] != 125: abort("intermediate_primary_125_gate", batch, event)
            if batch % args.checkpoint_every == 0:
                checkpoints.append(save_state(model, out / f"R2_PROTECTED_weights_batch{batch:04d}.pt", {"status": "IN_PROGRESS", "phase": "R2_PROTECTED", "phase_batch": batch, "source_checkpoint_sha256": sha256_file(ckpt_path), "flow_frozen": True, "flow_hash_initial": flow_hash_initial}))
    flow_hash_final = state_prefix_sha256(model.state_dict(), "model_g.flow.")
    if flow_hash_final != flow_hash_initial: abort("flow_hash_changed_despite_freeze", 799, {"flow_hash_initial": flow_hash_initial, "flow_hash_final": flow_hash_final})
    final_checkpoint = save_state(model, out / "R2_PROTECTED_weights_batch0799.pt", {"status": "R2_TRAINING_COMPLETE_MACHINE_GATE_PENDING", "phase": "R2_PROTECTED", "phase_batch": 799, "source_checkpoint_sha256": sha256_file(ckpt_path), "flow_frozen": True, "flow_hash_initial": flow_hash_initial, "flow_hash_final": flow_hash_final})
    final_seed_summaries = []; primary_dir = out / "R2_primary_gate_wav"
    for j, sb in enumerate(seed_bases, 1):
        rows = eval_gate(sb, primary_dir if j == 1 else None); s = summarize(rows); final_seed_summaries.append({"seed_base": sb, **s})
        with (out / f"R2_seed_{j}_gate.tsv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
    final_pass = all(s["pass"] == 125 for s in final_seed_summaries)
    report = {"schema_version": "0.1.0", "status": "PASS_PROTECTED_R2_MACHINE_GATE" if final_pass else "STOP_PROTECTED_R2_MACHINE_GATE", "training_performed": True, "r2_complete": True, "r2_batches": 799, "flow_frozen": True, "flow_hash_initial": flow_hash_initial, "flow_hash_final": flow_hash_final, "source_hybrid": {"file": ckpt_path.name, "bytes": ckpt_path.stat().st_size, "sha256": sha256_file(ckpt_path)}, "start_five_seed_gate": start_seed_summaries, "final_checkpoint": final_checkpoint, "final_five_seed_gate": final_seed_summaries, "primary_persisted_unique_wavs": len(list(primary_dir.glob("*.wav"))), "governed_rms_floor_dbfs": RMS_FLOOR_DBFS, "guard_events": guard_events, "checkpoints": checkpoints, "human_perceptual_gate": "NOT_RUN_BY_THIS_SCRIPT", "next_boundary": "If PASS_PROTECTED_R2_MACHINE_GATE, review machine evidence and prepare governed human CNS perceptual gate. Machine success does not equal human acceptance."}
    (out / "R2_PROTECTED_RESULT.json").write_text(json.dumps(report, indent=2), encoding="utf-8"); print(json.dumps(report, indent=2))

if __name__ == "__main__": main()
