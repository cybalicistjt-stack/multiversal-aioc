#!/usr/bin/env python3
"""Inference-only acoustic reset diagnostic for DWC repaired-corpus R1.

No optimizer is created and no weights are trained. The script compares:
1) completed R1 as-is,
2) R1 text side + pristine warm-start decoder,
3) R1 text side + pristine warm-start flow,
4) R1 text side + pristine warm-start decoder+flow,
5) full warm acoustic reset (decoder+posterior encoder+flow; enc_q is training-side only).

The purpose is to determine whether R1's stochastic low-level failures are caused
primarily by drift in the warm-start acoustic backbone versus incomplete DWC
text/prior adaptation.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math, sys, types
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
    return {"duration_s": float(len(x) / SR), "peak_dbfs": dbfs(peak), "rms_dbfs": dbfs(rms)}


def machine_status(st: dict) -> tuple[str, str]:
    notes = []
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
    required = {"acceptance_row_id", "source_utterance_id", "tier", "dwc_text", "ipa", "phoneme_id_sequence", "audio_filename"}
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
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


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
        "below_minus60": int(sum(v < -60.0 for v in vals)),
        "below_minus65": int(sum(v < -65.0 for v in vals)),
        "below_minus70": int(sum(v < -70.0 for v in vals)),
    }


def prefix_drift(r1_sd: dict, warm_sd: dict, prefix: str) -> dict:
    keys = [k for k in r1_sd if k.startswith(prefix) and k in warm_sd and r1_sd[k].shape == warm_sd[k].shape]
    if not keys:
        return {"prefix": prefix, "matching_tensors": 0}
    sq_diff = sq_ref = max_abs = 0.0
    params = changed_tensors = 0
    with torch.no_grad():
        for k in keys:
            a = r1_sd[k].detach().float().cpu()
            b = warm_sd[k].detach().float().cpu()
            d = a - b
            dn = float(torch.sum(d * d))
            rn = float(torch.sum(b * b))
            sq_diff += dn
            sq_ref += rn
            max_abs = max(max_abs, float(torch.max(torch.abs(d))))
            params += a.numel()
            if dn > 0:
                changed_tensors += 1
    return {
        "prefix": prefix,
        "matching_tensors": len(keys),
        "changed_tensors": changed_tensors,
        "parameters": params,
        "relative_l2": math.sqrt(sq_diff) / max(math.sqrt(sq_ref), 1e-12),
        "max_abs_delta": max_abs,
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
    acc_path = Path(args.acceptance_ts_v) if False else Path(args.acceptance_tsv)
    for p in (r1_path, warm_path, acc_path):
        if not p.exists():
            raise SystemExit(f"missing required file: {p}")

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

    drift = {
        "decoder": prefix_drift(r1_sd, warm_sd, "model_g.dec."),
        "posterior_encoder": prefix_drift(r1_sd, warm_sd, "model_g.enc_q."),
        "flow": prefix_drift(r1_sd, warm_sd, "model_g.flow."),
    }

    model = VitsModel(num_symbols=NUM_SYMBOLS, num_speakers=1, batch_size=1, mos_metric="none")
    missing, unexpected = model.load_state_dict(r1_sd, strict=False)
    if missing or unexpected:
        raise SystemExit(f"R1 state mismatch missing={missing[:20]} unexpected={unexpected[:20]}")
    model.to(device)
    model.eval()

    @torch.inference_mode()
    def infer(ids: list[int], seed: int) -> np.ndarray:
        torch.manual_seed(seed)
        if device.type == "cuda":
            torch.cuda.manual_seed_all(seed)
        x = torch.tensor([ids], dtype=torch.long, device=device)
        xl = torch.tensor([len(ids)], dtype=torch.long, device=device)
        return model.model_g.infer(x, xl, noise_scale=0.667, length_scale=1.0, noise_scale_w=0.8)[0][0, 0].detach().float().cpu().numpy()

    def evaluate(label: str, seed_base: int) -> list[dict]:
        rows = []
        for i, r in enumerate(acc):
            st = stats_from_audio(infer(r["phoneme_ids"], seed_base + i))
            status, notes = machine_status(st)
            rows.append({
                "acceptance_row_id": r["acceptance_row_id"],
                "source_utterance_id": r["source_utterance_id"],
                "tier": r["tier"],
                "dwc_text": r["dwc_text"],
                "seed": seed_base + i,
                **st,
                "status": status,
                "notes": notes,
            })
        write_tsv(out / f"{label}.tsv", rows)
        return rows

    def restore_from_r1() -> None:
        model.load_state_dict(r1_sd, strict=True)
        model.to(device)
        model.eval()

    def overwrite(prefixes: tuple[str, ...]) -> dict:
        sd = model.state_dict()
        copied = 0
        for k, v in warm_sd.items():
            if not k.startswith(prefixes):
                continue
            if k in sd and sd[k].shape == v.shape:
                sd[k] = v.to(dtype=sd[k].dtype)
                copied += 1
        model.load_state_dict(sd, strict=True)
        model.to(device)
        model.eval()
        return {"copied_tensors": copied, "prefixes": list(prefixes)}

    variants = {
        "r1_as_is": (),
        "decoder_reset": ("model_g.dec.",),
        "flow_reset": ("model_g.flow.",),
        "decoder_flow_reset": ("model_g.dec.", "model_g.flow."),
        "full_warm_acoustic_reset": ("model_g.dec.", "model_g.enc_q.", "model_g.flow."),
    }
    seed_bases = [args.seed + 3000, args.seed + 4000, args.seed + 5000]
    results = {}

    for name, prefixes in variants.items():
        restore_from_r1()
        action = {"copied_tensors": 0, "prefixes": []}
        if prefixes:
            action = overwrite(prefixes)
        seed_summaries = []
        per_row_pass = {r["acceptance_row_id"]: 0 for r in acc}
        for j, sb in enumerate(seed_bases, 1):
            rows = evaluate(f"{name}_seed{j}", sb)
            seed_summaries.append({"seed_base": sb, **summarize(rows)})
            for row in rows:
                if row["status"] == "PASS":
                    per_row_pass[row["acceptance_row_id"]] += 1
        results[name] = {
            "reset_action": action,
            "seed_summaries": seed_summaries,
            "robustness": {
                "pass_3_of_3": sum(v == 3 for v in per_row_pass.values()),
                "pass_2_of_3": sum(v == 2 for v in per_row_pass.values()),
                "pass_1_of_3": sum(v == 1 for v in per_row_pass.values()),
                "pass_0_of_3": sum(v == 0 for v in per_row_pass.values()),
                "min_passes_any_seed_schedule": min(x["pass"] for x in seed_summaries),
                "max_passes_any_seed_schedule": max(x["pass"] for x in seed_summaries),
            },
        }

    summary = {
        "schema_version": "0.1.0",
        "status": "R1_ACOUSTIC_RESET_INFERENCE_DIAGNOSTIC_COMPLETE",
        "training_performed": False,
        "r2_authorized_by_this_script": False,
        "human_gate_authorized_by_this_script": False,
        "r1_checkpoint": {"file": r1_path.name, "bytes": r1_path.stat().st_size, "sha256": sha256_file(r1_path)},
        "warmstart_checkpoint": {"file": warm_path.name, "bytes": warm_path.stat().st_size, "sha256": sha256_file(warm_path)},
        "acceptance": {"file": acc_path.name, "bytes": acc_path.stat().st_size, "sha256": sha256_file(acc_path), "rows": 125, "unique_acceptance_row_ids": 125, "unique_output_filenames": 125},
        "warmstart_to_r1_parameter_drift": drift,
        "variants": results,
        "interpretation_boundary": "Inference-only hypothesis test. If resetting decoder/flow materially improves multi-seed robustness, use that evidence to design a protected corrective retrain. Do not enter R2 or train based solely on this script."
    }
    (out / "R1_ACOUSTIC_RESET_DIAGNOSTIC_SUMMARY.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    hashes = []
    for p in sorted(out.glob("*")):
        if p.is_file() and p.name != "SHA256SUMS.txt":
            hashes.append(f"{sha256_file(p)}  {p.name}")
    (out / "SHA256SUMS.txt").write_text("\n".join(hashes) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
