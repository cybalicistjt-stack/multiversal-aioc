#!/usr/bin/env python3
"""Inference-only diagnosis for protected DWC R2B batch-384 abort.

Uses the last fully strengthened robust R2B checkpoint at global batch 256 as the
reference and the exact batch-384 abort as the later state. model_g.flow and
model_g.dp were frozen throughout R2B and must be bit-identical between the two.

The only generator modules that can affect inference and remained trainable in
R2B are tested by rollback:
  model_g.enc_p.  DWC text/prior encoder
  model_g.dec.    decoder

Variants evaluated on the corrected 125-row acceptance set across the same five
deterministic seed schedules:
  - batch256_as_is
  - abort384_as_is
  - abort384_restore_enc_p_from_256
  - abort384_restore_dec_from_256
  - abort384_restore_enc_p_dec_from_256

This script NEVER trains, changes optimizer state, authorizes continuation, or
performs human CNS perceptual acceptance.
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
EXPECTED_ABORT_SHA256 = "c24d461484ebb714fb7484cc1616c2790c12df81c0d2d726f13f852ff01434fc"
EXPECTED_SOURCE_CANDIDATE_SHA256 = "e0d78cf89a4fd50a79e064837993d8bc11556e03ad2399d64b8cc53ee93c146b"
PREFIXES = {
    "dp": "model_g.dp.",
    "flow": "model_g.flow.",
    "enc_p": "model_g.enc_p.",
    "dec": "model_g.dec.",
    "enc_q": "model_g.enc_q.",
}


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
    required = {
        "acceptance_row_id", "source_utterance_id", "tier", "dwc_text", "ipa",
        "phoneme_id_sequence", "audio_filename",
    }
    if len(rows) != 125 or not rows or not required.issubset(rows[0]):
        raise SystemExit("invalid corrected 125-row acceptance table")
    if len({r["acceptance_row_id"] for r in rows}) != 125:
        raise SystemExit("acceptance_row_id collision")
    if len({r["audio_filename"] for r in rows}) != 125:
        raise SystemExit("acceptance filename collision")
    for r in rows:
        ids = [int(x) for x in r["phoneme_id_sequence"].split()]
        if not ids or min(ids) < 0 or max(ids) >= NUM_SYMBOLS:
            raise SystemExit(f"bad exact IDs: {r['acceptance_row_id']}")
        r["phoneme_ids"] = ids
    return rows


def prefix_hash(state: dict, prefix: str) -> str:
    h = hashlib.sha256()
    keys = sorted(k for k in state if k.startswith(prefix))
    if not keys:
        raise SystemExit(f"no keys for prefix {prefix}")
    for k in keys:
        t = state[k].detach().cpu().contiguous()
        h.update(k.encode("utf-8"))
        h.update(str(tuple(t.shape)).encode("ascii"))
        h.update(str(t.dtype).encode("ascii"))
        h.update(t.numpy().tobytes())
    return h.hexdigest()


def drift(a: dict, b: dict, prefix: str) -> dict:
    keys = sorted(k for k in a if k.startswith(prefix))
    if not keys:
        return {"tensors": 0, "changed_tensors": 0, "relative_l2": None}
    num = den = 0.0
    changed = 0
    for k in keys:
        if k not in b or tuple(a[k].shape) != tuple(b[k].shape):
            raise SystemExit(f"checkpoint mismatch at {k}")
        ta = a[k].detach().cpu().float()
        tb = b[k].detach().cpu().float()
        d = ta - tb
        num += float(torch.sum(d * d))
        den += float(torch.sum(tb * tb))
        if not torch.equal(a[k].detach().cpu(), b[k].detach().cpu()):
            changed += 1
    return {
        "tensors": len(keys),
        "changed_tensors": changed,
        "relative_l2": math.sqrt(num / max(den, 1e-30)),
    }


def restore_prefix(dst: dict, src: dict, prefix: str) -> None:
    keys = sorted(k for k in dst if k.startswith(prefix))
    src_keys = {k for k in src if k.startswith(prefix)}
    if set(keys) != src_keys:
        raise SystemExit(f"prefix key mismatch for {prefix}")
    for k in keys:
        dst[k] = src[k].detach().cpu().clone()


def write_tsv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n"
        )
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--piper-src", required=True)
    ap.add_argument("--checkpoint256", required=True)
    ap.add_argument("--abort384", required=True)
    ap.add_argument("--acceptance-tsv", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = ap.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    p256 = Path(args.checkpoint256)
    p384 = Path(args.abort384)
    acc_path = Path(args.acceptance_tsv)
    for p in (p256, p384, acc_path):
        if not p.exists():
            raise SystemExit(f"missing input: {p}")
    if sha256_file(p384) != EXPECTED_ABORT_SHA256:
        raise SystemExit("batch-384 abort checkpoint SHA-256 mismatch")

    c256 = torch.load(p256, map_location="cpu", weights_only=False)
    c384 = torch.load(p384, map_location="cpu", weights_only=False)
    for label, payload, expected_batch in (("checkpoint256", c256, 256), ("abort384", c384, 384)):
        if int(payload.get("num_symbols", -1)) != NUM_SYMBOLS:
            raise SystemExit(f"{label} num_symbols mismatch")
        if int(payload.get("sample_rate", -1)) != SR:
            raise SystemExit(f"{label} sample_rate mismatch")
        if int(payload.get("phase_batch", -1)) != expected_batch:
            raise SystemExit(f"{label} phase_batch mismatch: {payload.get('phase_batch')}")
        if payload.get("source_candidate_sha256") != EXPECTED_SOURCE_CANDIDATE_SHA256:
            raise SystemExit(f"{label} source_candidate_sha256 mismatch")
        if payload.get("optimizer_state_restored") is not False:
            raise SystemExit(f"{label} optimizer provenance mismatch")

    s256 = c256["model_state_dict"]
    s384 = c384["model_state_dict"]
    if set(s256) != set(s384):
        raise SystemExit("checkpoint key sets differ")
    if prefix_hash(s256, PREFIXES["flow"]) != prefix_hash(s384, PREFIXES["flow"]):
        raise SystemExit("protected flow changed between batch 256 and 384")
    if prefix_hash(s256, PREFIXES["dp"]) != prefix_hash(s384, PREFIXES["dp"]):
        raise SystemExit("protected DP changed between batch 256 and 384")

    module_drift = {name: drift(s384, s256, prefix) for name, prefix in PREFIXES.items()}
    acc = load_acceptance(acc_path)
    device = torch.device(args.device)
    if device.type == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but unavailable")

    sys.path.insert(0, str(Path(args.piper_src) / "src"))
    install_stubs()
    from piper.train.vits.lightning import VitsModel

    model = VitsModel(num_symbols=NUM_SYMBOLS, num_speakers=1, batch_size=1, mos_metric="none").to(device)

    @torch.inference_mode()
    def infer(ids: list[int], seed: int) -> np.ndarray:
        model.eval()
        torch.manual_seed(seed)
        if device.type == "cuda":
            torch.cuda.manual_seed_all(seed)
        x = torch.tensor([ids], dtype=torch.long, device=device)
        xl = torch.tensor([len(ids)], dtype=torch.long, device=device)
        return model.model_g.infer(
            x, xl, noise_scale=0.667, length_scale=1.0, noise_scale_w=0.8
        )[0][0, 0].detach().float().cpu().numpy()

    variants = [
        ("checkpoint256_as_is", "256", ()),
        ("abort384_as_is", "384", ()),
        ("abort384_restore_enc_p_from_256", "384", ("enc_p",)),
        ("abort384_restore_dec_from_256", "384", ("dec",)),
        ("abort384_restore_enc_p_dec_from_256", "384", ("enc_p", "dec")),
    ]
    seed_bases = [args.seed + 3000 + 1000 * k for k in range(5)]
    all_results = []
    summaries = []
    sensitive = []

    for vname, base, restore in variants:
        source = s256 if base == "256" else s384
        state = {k: v.detach().cpu().clone() for k, v in source.items()}
        for mod in restore:
            restore_prefix(state, s256, PREFIXES[mod])
        missing, unexpected = model.load_state_dict(state, strict=False)
        if missing or unexpected:
            raise SystemExit(f"{vname} state mismatch: missing={missing[:10]} unexpected={unexpected[:10]}")

        per_row = {r["acceptance_row_id"]: [] for r in acc}
        seed_summaries = []
        for seed_index, seed_base in enumerate(seed_bases, 1):
            rows = []
            for i, r in enumerate(acc):
                st = stats(infer(r["phoneme_ids"], seed_base + i))
                status, notes = machine_status(st)
                rec = {
                    "variant": vname,
                    "seed_index": seed_index,
                    "seed_base": seed_base,
                    "acceptance_row_id": r["acceptance_row_id"],
                    "source_utterance_id": r["source_utterance_id"],
                    "dwc_text": r["dwc_text"],
                    **st,
                    "status": status,
                    "notes": notes,
                }
                rows.append(rec)
                all_results.append(rec)
                per_row[r["acceptance_row_id"]].append(rec)
            vals = [r["rms_dbfs"] for r in rows]
            passed = sum(r["status"] == "PASS" for r in rows)
            seed_summaries.append({
                "seed_index": seed_index,
                "seed_base": seed_base,
                "pass": passed,
                "fail": 125 - passed,
                "median_dbfs": float(np.median(vals)),
                "min_dbfs": float(min(vals)),
            })

        always = sum(all(x["status"] == "PASS" for x in rs) for rs in per_row.values())
        summaries.append({
            "variant": vname,
            "restored_modules": ",".join(restore) if restore else "none",
            "pass_counts": "/".join(str(x["pass"]) for x in seed_summaries),
            "always_pass_5_of_5": always,
            "rows_failing_any_seed": 125 - always,
            "worst_rms_dbfs": min(x["min_dbfs"] for x in seed_summaries),
            "median_dbfs_seed1": seed_summaries[0]["median_dbfs"],
        })
        for r in acc:
            rs = per_row[r["acceptance_row_id"]]
            passes = sum(x["status"] == "PASS" for x in rs)
            if passes < 5:
                sensitive.append({
                    "variant": vname,
                    "acceptance_row_id": r["acceptance_row_id"],
                    "source_utterance_id": r["source_utterance_id"],
                    "dwc_text": r["dwc_text"],
                    "passes_of_5": passes,
                    "failure_notes": "|".join(x["notes"] for x in rs if x["status"] != "PASS"),
                    "rms_dbfs_min": min(x["rms_dbfs"] for x in rs),
                    "duration_s_min": min(x["duration_s"] for x in rs),
                })

    write_tsv(out / "variant_summary.tsv", summaries)
    write_tsv(out / "variant_sensitive_rows.tsv", sensitive)
    write_tsv(out / "all_variant_seed_rows.tsv", all_results)

    source_summary = next(x for x in summaries if x["variant"] == "checkpoint256_as_is")
    if source_summary["always_pass_5_of_5"] != 125:
        raise SystemExit(f"batch-256 reference did not reproduce 625/625: {source_summary}")

    repaired = [
        x for x in summaries
        if x["variant"].startswith("abort384_restore_") and x["always_pass_5_of_5"] == 125
    ]
    report = {
        "schema_version": "0.1.0",
        "status": "R2B_ABORT384_MODULE_ROLLBACK_DIAGNOSTIC_COMPLETE",
        "training_performed": False,
        "continuation_authorized_by_this_script": False,
        "human_gate_authorized_by_this_script": False,
        "checkpoint256": {
            "file": p256.name,
            "bytes": p256.stat().st_size,
            "sha256": sha256_file(p256),
        },
        "abort384": {
            "file": p384.name,
            "bytes": p384.stat().st_size,
            "sha256": sha256_file(p384),
        },
        "source_candidate_sha256": EXPECTED_SOURCE_CANDIDATE_SHA256,
        "acceptance": {
            "file": acc_path.name,
            "bytes": acc_path.stat().st_size,
            "sha256": sha256_file(acc_path),
            "rows": 125,
        },
        "protected_prefix_hashes": {
            "flow": prefix_hash(s256, PREFIXES["flow"]),
            "dp": prefix_hash(s256, PREFIXES["dp"]),
        },
        "module_drift_batch384_relative_to_batch256": module_drift,
        "seed_bases": seed_bases,
        "variants": summaries,
        "fully_robust_repaired_variants": [x["variant"] for x in repaired],
        "interpretation_boundary": "Inference-only isolation. Review which minimum rollback restores 625/625 before defining any R2C continuation contract.",
    }
    (out / "R2B_ABORT384_MODULE_ROLLBACK_REPORT.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )

    hashes = []
    for p in sorted(out.iterdir()):
        if p.is_file() and p.name != "SHA256SUMS.txt":
            hashes.append(f"{sha256_file(p)}  {p.name}")
    (out / "SHA256SUMS.txt").write_text("\n".join(hashes) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
