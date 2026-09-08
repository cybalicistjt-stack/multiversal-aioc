#!/usr/bin/env python3
"""Continue DWC Piper/VITS adaptation from verified Stage-C weights.

This deliberately does NOT repeat the LJSpeech warm-start, Stage A, Stage B, or
Stage C. It loads the exact 58-symbol Stage-C model state, runs a deterministic
Stage-D curriculum, saves durable weight checkpoints, renders the 125-item
acceptance suite before and after Stage D, and writes machine evidence.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import sys
import time
import types
import wave
from pathlib import Path

import numpy as np
import torch

EXPECTED_STAGE_C_SHA256 = "d800ae031942c29289ced1cc80c1448fff234c53f42a56f2d69265e7e3ebabb2"
EXPECTED_STAGE_C_BYTES = 281_775_417


def sha256_file(path: Path, chunk: int = 16 * 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def install_unused_dependency_stubs() -> None:
    if "pysilero_vad" not in sys.modules:
        m = types.ModuleType("pysilero_vad")
        class DummyVAD:
            pass
        m.SileroVoiceActivityDetector = DummyVAD
        sys.modules["pysilero_vad"] = m
    if "pathvalidate" not in sys.modules:
        m = types.ModuleType("pathvalidate")
        m.sanitize_filename = lambda s, *a, **k: s
        sys.modules["pathvalidate"] = m


def read_piper_csv(path: Path) -> list[dict]:
    rows = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        parts = line.split("|")
        if len(parts) != 3:
            raise ValueError(f"CSV row {i} has {len(parts)} columns")
        fn, text, ids_s = parts
        ids = [int(x) for x in ids_s.split()]
        if not ids or min(ids) < 0 or max(ids) >= 58:
            raise ValueError(f"CSV row {i} has invalid DWC IDs")
        rows.append({"file": fn, "text": text, "ids": ids, "stem": Path(fn).stem})
    if len(rows) != 799:
        raise ValueError(f"Expected 799 corpus rows, found {len(rows)}")
    return rows


def read_target_ids(path: Path) -> list[str]:
    rows = list(csv.DictReader(path.open(encoding="utf-8"), delimiter="\t"))
    ids = [r["utterance_id"] for r in rows]
    if len(ids) != 128:
        raise ValueError(f"Expected 128 Stage-C target rows, found {len(ids)}")
    return ids


def deterministic_stage_d_schedule(full_rows: list[dict], target_ids: list[str], seed: int) -> list[dict]:
    """One shuffled full-corpus pass + one extra shuffled Stage-C repair pass.

    The 128 repair rows are distributed proportionally through the 799-row full
    pass so Stage-D does not end with a target-only tail. Total = 927 batches.
    """
    by_stem = {r["stem"]: r for r in full_rows}
    missing = [x for x in target_ids if x not in by_stem]
    if missing:
        raise ValueError(f"Stage-C target rows missing from corpus: {missing[:10]}")

    rng = random.Random(seed)
    full = list(full_rows)
    target = [by_stem[x] for x in target_ids]
    rng.shuffle(full)
    rng.shuffle(target)

    schedule = []
    j = 0
    n_full = len(full)
    n_target = len(target)
    for i, row in enumerate(full, 1):
        schedule.append(row)
        should_have_inserted = math.floor(i * n_target / n_full)
        while j < should_have_inserted:
            extra = dict(target[j])
            extra["stage_d_role"] = "repair_reinforcement"
            schedule.append(extra)
            j += 1
    while j < n_target:
        extra = dict(target[j])
        extra["stage_d_role"] = "repair_reinforcement"
        schedule.append(extra)
        j += 1

    for r in schedule:
        r.setdefault("stage_d_role", "full_corpus")
    assert len(schedule) == 927, len(schedule)
    return schedule


def write_wav(path: Path, audio: np.ndarray, sample_rate: int = 22050) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    audio = np.asarray(audio, dtype=np.float32).reshape(-1)
    if audio.size == 0:
        raise ValueError("empty audio")
    peak = float(np.max(np.abs(audio)))
    if peak > 1.0:
        audio = audio / peak
    pcm = np.clip(audio, -1.0, 1.0)
    pcm16 = (pcm * 32767.0).astype("<i2")
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sample_rate)
        w.writeframes(pcm16.tobytes())
    rms = float(np.sqrt(np.mean(np.square(pcm)))) if pcm.size else 0.0
    return {"duration_s": float(len(pcm16) / sample_rate), "peak": peak, "rms": rms}


def machine_waveform_status(stats: dict) -> str:
    if stats["duration_s"] < 0.08:
        return "REVIEW"
    if stats["peak"] >= 0.995:
        return "REVIEW"
    if stats["rms"] < 10 ** (-55 / 20):
        return "REVIEW"
    return "PASS"


def save_state(model, path: Path, metadata: dict) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    cpu_state = {k: v.detach().cpu() for k, v in model.state_dict().items()}
    payload = {
        "model_state_dict": cpu_state,
        "num_symbols": 58,
        "sample_rate": 22050,
        "segment_size": 2048,
        **metadata,
    }
    torch.save(payload, path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha256_file(path)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--piper-src", required=True)
    ap.add_argument("--stage-c-weights", required=True)
    ap.add_argument("--csv", required=True)
    ap.add_argument("--audio-dir", required=True)
    ap.add_argument("--stage-c-selection", required=True)
    ap.add_argument("--acceptance-tsv", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--batches", type=int, default=927)
    ap.add_argument("--seed", type=int, default=20260908)
    ap.add_argument("--checkpoint-every", type=int, default=300)
    ap.add_argument("--device", default="cuda")
    a = ap.parse_args()

    out = Path(a.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    stage_c_path = Path(a.stage_c_weights)

    if stage_c_path.stat().st_size != EXPECTED_STAGE_C_BYTES:
        raise SystemExit(f"Stage-C byte-size mismatch: {stage_c_path.stat().st_size}")
    stage_c_sha = sha256_file(stage_c_path)
    if stage_c_sha != EXPECTED_STAGE_C_SHA256:
        raise SystemExit(f"Stage-C SHA mismatch: {stage_c_sha}")

    device = torch.device(a.device)
    if device.type == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but no CUDA device is available")

    sys.path.insert(0, str(Path(a.piper_src) / "src"))
    install_unused_dependency_stubs()
    from piper.train.vits.lightning import VitsModel
    from piper.train.vits.dataset import Batch
    from piper.train.vits.mel_processing import spectrogram_torch

    corpus = read_piper_csv(Path(a.csv))
    audio_dir = Path(a.audio_dir)
    for r in corpus:
        if not (audio_dir / r["file"]).exists():
            raise SystemExit(f"Missing audio: {r['file']}")
    target_ids = read_target_ids(Path(a.stage_c_selection))
    schedule = deterministic_stage_d_schedule(corpus, target_ids, a.seed)
    if not (1 <= a.batches <= len(schedule)):
        raise SystemExit(f"--batches must be 1..{len(schedule)}")
    schedule = schedule[: a.batches]

    saved = torch.load(stage_c_path, map_location="cpu", weights_only=False)
    if saved.get("num_symbols") != 58:
        raise SystemExit(f"Unexpected num_symbols: {saved.get('num_symbols')}")

    torch.manual_seed(a.seed)
    np.random.seed(a.seed % (2**32 - 1))
    if device.type == "cuda":
        torch.cuda.manual_seed_all(a.seed)

    model = VitsModel(num_symbols=58, num_speakers=1, batch_size=1, mos_metric="none")
    incompat = model.load_state_dict(saved["model_state_dict"], strict=True)
    if getattr(incompat, "missing_keys", None) or getattr(incompat, "unexpected_keys", None):
        raise SystemExit(f"Stage-C state load mismatch: {incompat}")
    model.to(device)

    acceptance_rows = list(csv.DictReader(Path(a.acceptance_tsv).open(encoding="utf-8"), delimiter="\t"))
    if len(acceptance_rows) != 125:
        raise SystemExit(f"Expected 125 acceptance rows, found {len(acceptance_rows)}")

    @torch.inference_mode()
    def render_acceptance(label: str) -> dict:
        model.eval()
        render_dir = out / label
        render_dir.mkdir(parents=True, exist_ok=True)
        manifest = []
        for idx, r in enumerate(acceptance_rows):
            ids = [int(x) for x in r["phoneme_id_sequence"].split()]
            x = torch.tensor([ids], dtype=torch.long, device=device)
            xl = torch.tensor([len(ids)], dtype=torch.long, device=device)
            torch.manual_seed(a.seed + idx)
            if device.type == "cuda":
                torch.cuda.manual_seed_all(a.seed + idx)
            audio = model.model_g.infer(
                x, xl, noise_scale=0.667, length_scale=1.0, noise_scale_w=0.8
            )[0][0, 0].detach().float().cpu().numpy()
            wav_path = render_dir / r["audio_filename"]
            stats = write_wav(wav_path, audio, 22050)
            manifest.append({
                "utterance_id": r["utterance_id"],
                "tier": r["tier"],
                "dwc_text": r["dwc_text"],
                "ipa": r["ipa"],
                **stats,
                "status": machine_waveform_status(stats),
                "file": wav_path.name,
            })
        with (out / f"{label}_manifest.tsv").open("w", encoding="utf-8", newline="") as f:
            fields = list(manifest[0].keys())
            w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
            w.writeheader(); w.writerows(manifest)
        result = {
            "rows": len(manifest),
            "pass": sum(x["status"] == "PASS" for x in manifest),
            "review": sum(x["status"] != "PASS" for x in manifest),
        }
        (out / f"{label}_machine_report.json").write_text(json.dumps(result, indent=2))
        return result

    pre_report = render_acceptance("pre_stage_d_stage_c_acceptance")

    def make_batch(row: dict):
        with wave.open(str(audio_dir / row["file"]), "rb") as w:
            raw = w.readframes(w.getnframes())
            if not (w.getframerate() == 22050 and w.getnchannels() == 1 and w.getsampwidth() == 2):
                raise ValueError(f"Unexpected WAV format: {row['file']}")
        arr = np.frombuffer(raw, dtype="<i2").astype("float32") / 32768.0
        audio = torch.from_numpy(arr).to(device).unsqueeze(0)
        if audio.shape[-1] < 8192:
            audio = torch.nn.functional.pad(audio, (0, 8192 - audio.shape[-1]))
        spec = spectrogram_torch(audio, 1024, 22050, 256, 1024, center=False)
        ids = row["ids"]
        return Batch(
            torch.tensor([ids], dtype=torch.long, device=device),
            torch.tensor([len(ids)], dtype=torch.long, device=device),
            spec,
            torch.tensor([spec.shape[-1]], dtype=torch.long, device=device),
            audio.unsqueeze(1),
            torch.tensor([audio.shape[-1]], dtype=torch.long, device=device),
            None,
        )

    model.train()
    opts, _ = model.configure_optimizers()
    opt_g, opt_d = opts
    lr_g = opt_g.param_groups[0]["lr"]
    lr_d = opt_d.param_groups[0]["lr"]

    metrics_path = out / "stageD_metrics.jsonl"
    start = time.time()
    first_metric = None
    last_metric = None
    checkpoints = []
    with metrics_path.open("w", encoding="utf-8") as mf:
        for batch_idx, row in enumerate(schedule, 1):
            lg, ld, met = model._compute_loss(make_batch(row))
            opt_g.zero_grad(set_to_none=True); lg.backward(); opt_g.step()
            opt_d.zero_grad(set_to_none=True); ld.backward(); opt_d.step()
            rec = {
                "batch_idx": batch_idx,
                "optimizer_steps_total": batch_idx * 2,
                "elapsed_s": round(time.time() - start, 3),
                "utterance_id": row["stem"],
                "stage_d_role": row["stage_d_role"],
                "loss_g": float(lg.detach().cpu()),
                "loss_d": float(ld.detach().cpu()),
                "train_mel": float(met["mel"]),
                "train_kl": float(met["kl"]),
                "train_dur": float(met["dur"]),
            }
            if first_metric is None:
                first_metric = rec
            last_metric = rec
            mf.write(json.dumps(rec) + "\n")
            mf.flush()
            if (batch_idx % a.checkpoint_every == 0) or (batch_idx == len(schedule)):
                ck = save_state(model, out / f"stageD_weights_batch{batch_idx:04d}.pt", {
                    "stage": "D",
                    "stageD_batches_completed": batch_idx,
                    "stageD_optimizer_steps": batch_idx * 2,
                    "source_stageC_sha256": stage_c_sha,
                    "optimizer_state_preserved_from_stageC": False,
                    "optimizer_reinitialized_for_stageD": True,
                    "curriculum": "one full 799-row pass plus one interleaved extra pass over the 128 Stage-C repair rows",
                    "seed": a.seed,
                })
                checkpoints.append(ck)

    post_report = render_acceptance("post_stage_d_acceptance")
    result = {
        "status": "PASS_STAGE_D_ADAPTATION",
        "batches_completed": len(schedule),
        "optimizer_steps": len(schedule) * 2,
        "schedule_full_corpus_rows": sum(r["stage_d_role"] == "full_corpus" for r in schedule),
        "schedule_repair_reinforcement_rows": sum(r["stage_d_role"] == "repair_reinforcement" for r in schedule),
        "seed": a.seed,
        "device": str(device),
        "learning_rate_g": lr_g,
        "learning_rate_d": lr_d,
        "optimizer_reinitialized_from_stageC": True,
        "source_stageC_sha256": stage_c_sha,
        "first_metric": first_metric,
        "last_metric": last_metric,
        "pre_stage_d_machine_acceptance": pre_report,
        "post_stage_d_machine_acceptance": post_report,
        "checkpoints": checkpoints,
    }
    (out / "stageD_result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
