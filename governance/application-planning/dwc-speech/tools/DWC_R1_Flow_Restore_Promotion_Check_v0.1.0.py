#!/usr/bin/env python3
"""Create and validate a persisted R1-flow-restored DWC checkpoint.

This tool performs NO TRAINING. It copies only model_g.flow.* from the exact
verified warm-start checkpoint into the completed R1 checkpoint, persists that
hybrid checkpoint with provenance, and evaluates it on the corrected 125-row
acceptance set across five deterministic seed schedules.

R2 is NOT run or authorized by this script. Promotion-ready means only that the
hybrid has passed this strengthened machine waveform check.
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
EXPECTED_FLOW_TENSORS = 112
EXPECTED_WARM_SHA256 = "dcf2449bdbdaad09256a08dfac211c59f6b36ce8d3f244fd844a9eb1d7384c7c"
EXPECTED_WARM_BYTES = 845889993


def sha256_file(path: Path, chunk: int = 16 * 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()


def dbfs(v: float) -> float:
    return 20.0 * math.log10(max(float(v), 1e-12))


def stats(audio: np.ndarray) -> dict:
    x = np.asarray(audio, dtype=np.float32).reshape(-1)
    peak = float(np.max(np.abs(x))) if x.size else 0.0
    rms = float(np.sqrt(np.mean(np.square(x)))) if x.size else 0.0
    return {
        "duration_s": float(len(x) / SR),
        "peak_dbfs": dbfs(peak),
        "rms_dbfs": dbfs(rms),
    }


def status_for(st: dict) -> tuple[str, str]:
    notes: list[str] = []
    if st["duration_s"] < 0.08:
        notes.append("duration")
    if st["peak_dbfs"] > CLIP_FLOOR_DBFS:
        notes.append("clipping")
    if st["rms_dbfs"] < RMS_FLOOR_DBFS:
        notes.append("low_level")
    return ("PASS" if not notes else "FAIL", ";".join(notes))


def install_stubs() -> None:
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


def load_acceptance(path: Path) -> list[dict]:
    rows = list(csv.DictReader(path.open(encoding="utf-8"), delimiter="\t"))
    required = {
        "acceptance_row_id", "source_utterance_id", "tier", "dwc_text", "ipa",
        "phoneme_id_sequence", "audio_filename"
    }
    if len(rows) != 125:
        raise SystemExit(f"acceptance rows={len(rows)} expected 125")
    if not rows or not required.issubset(rows[0]):
        raise SystemExit(f"acceptance fields missing: {sorted(required - set(rows[0] if rows else []))}")
    if len({r["acceptance_row_id"] for r in rows}) != 125:
        raise SystemExit("acceptance_row_id values are not unique")
    if len({r["audio_filename"] for r in rows}) != 125:
        raise SystemExit("acceptance output filenames are not unique")
    for r in rows:
        ids = [int(x) for x in r["phoneme_id_sequence"].split()]
        if not ids or min(ids) < 0 or max(ids) >= NUM_SYMBOLS:
            raise SystemExit(f"bad exact-ID sequence: {r['acceptance_row_id']}")
        r["phoneme_ids"] = ids
    return rows


def write_tsv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=list(rows[0].keys()), delimiter="\t",
            lineterminator="\n", extrasaction="ignore"
        )
        w.writeheader()
        w.writerows(rows)


def write_wav(path: Path, audio: np.ndarray) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    x = np.asarray(audio, dtype=np.float32).reshape(-1)
    pcm = (np.clip(x, -1.0, 1.0) * 32767.0).astype("<i2")
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    return stats(pcm.astype(np.float32) / 32768.0)


def summarize(rows: list[dict]) -> dict:
    vals = [float(r["rms_dbfs"]) for r in rows]
    return {
        "rows": len(rows),
        "pass": sum(r["status"] == "PASS" for r in rows),
        "fail": sum(r["status"] != "PASS" for r in rows),
        "rms_dbfs_median": float(np.median(vals)),
        "rms_dbfs_min": float(min(vals)),
        "rms_dbfs_max": float(max(vals)),
        "below_minus55": int(sum(v < -55.0 for v in vals)),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--piper-src", required=True)
    ap.add_argument("--r1-checkpoint", required=True)
    ap.add_argument("--warmstart-checkpoint", required=True)
    ap.add_argument("--acceptance-tsv", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = ap.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    r1_path = Path(args.r1_checkpoint)
    warm_path = Path(args.warmstart_checkpoint)
    acc_path = Path(args.acceptance_tsv)
    for p in (r1_path, warm_path, acc_path):
        if not p.exists():
            raise SystemExit(f"missing required file: {p}")

    if warm_path.stat().st_size != EXPECTED_WARM_BYTES:
        raise SystemExit(f"warm-start bytes={warm_path.stat().st_size} expected {EXPECTED_WARM_BYTES}")
    warm_sha = sha256_file(warm_path)
    if warm_sha != EXPECTED_WARM_SHA256:
        raise SystemExit(f"warm-start SHA-256 mismatch: {warm_sha}")

    acc = load_acceptance(acc_path)
    device = torch.device(args.device)
    if device.type == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but unavailable")

    sys.path.insert(0, str(Path(args.piper_src) / "src"))
    install_stubs()
    from piper.train.vits.lightning import VitsModel

    r1_payload = torch.load(r1_path, map_location="cpu", weights_only=False)
    if int(r1_payload.get("num_symbols", -1)) != NUM_SYMBOLS:
        raise SystemExit(f"R1 num_symbols={r1_payload.get('num_symbols')} expected {NUM_SYMBOLS}")
    if int(r1_payload.get("sample_rate", -1)) != SR:
        raise SystemExit(f"R1 sample_rate={r1_payload.get('sample_rate')} expected {SR}")
    r1_sd = r1_payload["model_state_dict"]
    warm_payload = torch.load(warm_path, map_location="cpu", weights_only=False)
    warm_sd = warm_payload["state_dict"]

    hybrid_sd = {k: v.clone() if torch.is_tensor(v) else v for k, v in r1_sd.items()}
    copied = []
    for k, v in warm_sd.items():
        if not k.startswith("model_g.flow."):
            continue
        if k in hybrid_sd and hybrid_sd[k].shape == v.shape:
            hybrid_sd[k] = v.clone().to(dtype=hybrid_sd[k].dtype)
            copied.append(k)
    if len(copied) != EXPECTED_FLOW_TENSORS:
        raise SystemExit(f"copied flow tensors={len(copied)} expected {EXPECTED_FLOW_TENSORS}")

    hybrid = dict(r1_payload)
    hybrid["model_state_dict"] = hybrid_sd
    hybrid["hybrid_provenance"] = {
        "kind": "R1_FLOW_RESTORED",
        "training_performed": False,
        "source_r1_file": r1_path.name,
        "source_r1_sha256": sha256_file(r1_path),
        "warmstart_file": warm_path.name,
        "warmstart_sha256": warm_sha,
        "restored_prefix": "model_g.flow.",
        "restored_tensors": len(copied),
        "acceptance_table_sha256": sha256_file(acc_path),
    }
    hybrid_path = out / "R1_flow_restored_candidate.pt"
    torch.save(hybrid, hybrid_path)
    hybrid_sha = sha256_file(hybrid_path)

    model = VitsModel(num_symbols=NUM_SYMBOLS, num_speakers=1, batch_size=1, mos_metric="none")
    missing, unexpected = model.load_state_dict(hybrid_sd, strict=False)
    if missing or unexpected:
        raise SystemExit(f"hybrid state mismatch missing={missing[:20]} unexpected={unexpected[:20]}")
    model.to(device)
    model.eval()

    @torch.inference_mode()
    def infer(ids: list[int], seed: int) -> np.ndarray:
        torch.manual_seed(seed)
        if device.type == "cuda":
            torch.cuda.manual_seed_all(seed)
        x = torch.tensor([ids], dtype=torch.long, device=device)
        xl = torch.tensor([len(ids)], dtype=torch.long, device=device)
        return model.model_g.infer(
            x, xl, noise_scale=0.667, length_scale=1.0, noise_scale_w=0.8
        )[0][0, 0].detach().float().cpu().numpy()

    seed_bases = [args.seed + 3000 + 1000 * k for k in range(5)]
    seed_summaries = []
    per_row_passes = {r["acceptance_row_id"]: 0 for r in acc}

    for j, sb in enumerate(seed_bases, 1):
        rows = []
        for i, r in enumerate(acc):
            audio = infer(r["phoneme_ids"], sb + i)
            if j == 1:
                st = write_wav(out / "primary_gate_wav" / r["audio_filename"], audio)
            else:
                st = stats(audio)
            status, notes = status_for(st)
            if status == "PASS":
                per_row_passes[r["acceptance_row_id"]] += 1
            rows.append({
                "acceptance_row_id": r["acceptance_row_id"],
                "source_utterance_id": r["source_utterance_id"],
                "tier": r["tier"],
                "dwc_text": r["dwc_text"],
                "seed": sb + i,
                **st,
                "status": status,
                "notes": notes,
                "audio_filename": r["audio_filename"] if j == 1 else "",
            })
        write_tsv(out / f"seed_{j}_gate.tsv", rows)
        seed_summaries.append({"seed_base": sb, **summarize(rows)})

    robustness = {
        "pass_5_of_5": sum(v == 5 for v in per_row_passes.values()),
        "pass_4_of_5": sum(v == 4 for v in per_row_passes.values()),
        "pass_3_of_5": sum(v == 3 for v in per_row_passes.values()),
        "pass_2_of_5": sum(v == 2 for v in per_row_passes.values()),
        "pass_1_of_5": sum(v == 1 for v in per_row_passes.values()),
        "pass_0_of_5": sum(v == 0 for v in per_row_passes.values()),
    }
    promotion_ready = (
        all(s["pass"] == 125 for s in seed_summaries)
        and robustness["pass_5_of_5"] == 125
        and len(list((out / "primary_gate_wav").glob("*.wav"))) == 125
    )

    report = {
        "schema_version": "0.1.0",
        "status": "PROMOTION_READY" if promotion_ready else "NOT_PROMOTION_READY",
        "training_performed": False,
        "r2_run": False,
        "r2_authorized_by_this_script": False,
        "hybrid": {
            "file": hybrid_path.name,
            "bytes": hybrid_path.stat().st_size,
            "sha256": hybrid_sha,
            "source_r1_sha256": hybrid["hybrid_provenance"]["source_r1_sha256"],
            "warmstart_sha256": warm_sha,
            "restored_prefix": "model_g.flow.",
            "restored_tensors": len(copied),
        },
        "acceptance": {
            "rows": 125,
            "unique_acceptance_row_ids": 125,
            "unique_output_filenames": 125,
            "persisted_primary_wavs": len(list((out / "primary_gate_wav").glob("*.wav"))),
            "rms_floor_dbfs": RMS_FLOOR_DBFS,
        },
        "five_seed_gate": seed_summaries,
        "robustness": robustness,
        "promotion_condition": "All 125 rows must pass all five deterministic schedules and the primary schedule must persist 125 uniquely identified WAVs.",
        "next_boundary": "If PROMOTION_READY, review this evidence and separately authorize protected R2 with model_g.flow frozen. Human CNS perceptual acceptance remains separate."
    }
    (out / "R1_FLOW_RESTORE_PROMOTION_REPORT.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    hashes = []
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.name != "SHA256SUMS.txt":
            hashes.append(f"{sha256_file(p)}  {p.relative_to(out)}")
    (out / "SHA256SUMS.txt").write_text("\n".join(hashes) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
