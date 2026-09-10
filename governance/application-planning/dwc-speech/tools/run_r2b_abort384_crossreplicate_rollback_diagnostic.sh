#!/usr/bin/env bash
set -euo pipefail
BASE=${DWC_BASE:-$HOME/multiversal/dwc-tts}
G="$BASE/governance/multiversal-aioc"
P="$BASE/src/piper1-gpl"
VENV="$BASE/envs/piper-v1.8.0"
TOOLS="$G/governance/application-planning/dwc-speech/tools"
BASETOOL="$TOOLS/DWC_R2B_Abort384_Module_Rollback_Diagnostic_v0.1.0.py"

HASH1="c24d461484ebb714fb7484cc1616c2790c12df81c0d2d726f13f852ff01434fc"
HASH2="5a53ce2dde13df389fada834cc027283ef14dc2be44a102fc9fedd249716fd1b"
OLDHASH="c24d461484ebb714fb7484cc1616c2790c12df81c0d2d726f13f852ff01434fc"

PROMO=""
ACC=""
for d in $(ls -dt "$BASE"/runs/r1_flow_restore_promotion_* 2>/dev/null || true); do
  f="$d/R1_flow_restored_candidate.pt"
  a="$d/TTS_ENGINE_03_ACCEPTANCE_UTTERANCES_v0.2.0.tsv"
  if [[ -f "$f" && -f "$a" ]]; then
    PROMO="$f"; ACC="$a"; break
  fi
done
[[ -n "$ACC" ]] || { echo "Corrected acceptance table not found" >&2; exit 2; }
[[ -f "$BASETOOL" ]] || { echo "Missing base diagnostic tool: $BASETOOL" >&2; exit 3; }

find_pair() {
  local expected="$1"
  for d in $(ls -dt "$BASE"/runs/r2b_protected_* 2>/dev/null || true); do
    local a="$d/ABORT_R2B_PROTECTED_batch0384.pt"
    local c="$d/R2B_PROTECTED_weights_batch0256.pt"
    if [[ -f "$a" && -f "$c" ]] && [[ "$(sha256sum "$a" | awk '{print $1}')" == "$expected" ]]; then
      printf '%s|%s|%s\n' "$d" "$c" "$a"
      return 0
    fi
  done
  return 1
}

PAIR1=$(find_pair "$HASH1") || { echo "Replicate-1 batch384 pair not found" >&2; exit 4; }
PAIR2=$(find_pair "$HASH2") || { echo "Replicate-2 batch384 pair not found" >&2; exit 4; }

source "$VENV/bin/activate"
python -m py_compile "$BASETOOL"
python - <<'PY'
import torch
assert torch.cuda.is_available(), "CUDA unavailable"
print("GPU:", torch.cuda.get_device_name(0))
PY

OUT="$BASE/runs/r2b_abort384_crossreplicate_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUT"

run_one() {
  local label="$1"
  local pair="$2"
  local expected="$3"
  IFS='|' read -r run ck256 abort384 <<< "$pair"
  local sub="$OUT/$label"
  mkdir -p "$sub"
  local tool="$sub/diag.py"
  python - "$BASETOOL" "$tool" "$OLDHASH" "$expected" <<'PY'
from pathlib import Path
import sys
src=Path(sys.argv[1]).read_text(encoding="utf-8")
old=sys.argv[3]; new=sys.argv[4]
needle=f'EXPECTED_ABORT_SHA256 = "{old}"'
replacement=f'EXPECTED_ABORT_SHA256 = "{new}"'
if needle not in src:
    raise SystemExit("expected abort-hash constant not found in base diagnostic")
Path(sys.argv[2]).write_text(src.replace(needle,replacement,1),encoding="utf-8")
PY
  python -m py_compile "$tool"
  python "$tool" \
    --piper-src "$P" \
    --checkpoint256 "$ck256" \
    --abort384 "$abort384" \
    --acceptance-tsv "$ACC" \
    --output-dir "$sub" \
    --device cuda \
    --seed 20260908 | tee "$sub/console.log"
  echo "$run" > "$sub/source_run.txt"
}

run_one "replicate1" "$PAIR1" "$HASH1"
run_one "replicate2" "$PAIR2" "$HASH2"

python - "$OUT" <<'PY'
from pathlib import Path
import csv, json, sys
out=Path(sys.argv[1])
reports={}
for label in ("replicate1","replicate2"):
    p=out/label/"R2B_ABORT384_MODULE_ROLLBACK_REPORT.json"
    reports[label]=json.loads(p.read_text(encoding="utf-8"))

by_rep={}
for label,r in reports.items():
    by_rep[label]={x["variant"]:x for x in r["variants"]}

variants=list(by_rep["replicate1"])
rows=[]
for v in variants:
    a=by_rep["replicate1"][v]
    b=by_rep["replicate2"][v]
    rows.append({
        "variant":v,
        "replicate1_pass_counts":a["pass_counts"],
        "replicate1_always_pass_5_of_5":a["always_pass_5_of_5"],
        "replicate2_pass_counts":b["pass_counts"],
        "replicate2_always_pass_5_of_5":b["always_pass_5_of_5"],
        "fully_robust_both":(
            a["always_pass_5_of_5"]==125 and b["always_pass_5_of_5"]==125
        ),
        "replicate1_worst_rms_dbfs":a["worst_rms_dbfs"],
        "replicate2_worst_rms_dbfs":b["worst_rms_dbfs"],
    })

with (out/"crossreplicate_variant_summary.tsv").open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter="\t",lineterminator="\n")
    w.writeheader(); w.writerows(rows)

success=[r["variant"] for r in rows if r["fully_robust_both"] and r["variant"].startswith("abort384_restore_")]
priority=[
    "abort384_restore_enc_p_from_256",
    "abort384_restore_dec_from_256",
    "abort384_restore_enc_p_dec_from_256",
]
minimum=next((v for v in priority if v in success),None)

combined={
    "schema_version":"0.1.0",
    "status":"R2B_ABORT384_CROSSREPLICATE_ROLLBACK_COMPLETE",
    "training_performed":False,
    "replicates":{
        label:{
            "checkpoint256":r["checkpoint256"],
            "abort384":r["abort384"],
            "module_drift_batch384_relative_to_batch256":r["module_drift_batch384_relative_to_batch256"],
            "fully_robust_repaired_variants":r["fully_robust_repaired_variants"],
        } for label,r in reports.items()
    },
    "variants":rows,
    "fully_robust_across_both_replicates":success,
    "minimum_successful_rollback_across_both":minimum,
    "continuation_authorized_by_this_script":False,
    "human_gate_authorized_by_this_script":False,
    "interpretation_boundary":"Cross-replicate inference-only evidence. Review before defining R2C protection/continuation."
}
(out/"R2B_ABORT384_CROSSREPLICATE_REPORT.json").write_text(json.dumps(combined,indent=2),encoding="utf-8")
print(json.dumps(combined,indent=2))
PY

(
  cd "$OUT"
  : > SHA256SUMS.txt
  find replicate1 replicate2 -maxdepth 1 -type f ! -name 'diag.py' -print | sort | while read -r f; do sha256sum "$f" >> SHA256SUMS.txt; done
  sha256sum R2B_ABORT384_CROSSREPLICATE_REPORT.json crossreplicate_variant_summary.tsv >> SHA256SUMS.txt
)

WIN_HOME=$(cmd.exe /C "echo %USERPROFILE%" 2>/dev/null | tr -d '\r')
WIN_DL="$(wslpath "$WIN_HOME")/Downloads"
PKG="$WIN_DL/DWC_R2B_ABORT384_CROSSREPLICATE_ROLLBACK_$(date +%Y%m%d_%H%M%S).zip"
(
  cd "$OUT"
  zip -9 -r "$PKG" \
    R2B_ABORT384_CROSSREPLICATE_REPORT.json \
    crossreplicate_variant_summary.tsv \
    SHA256SUMS.txt \
    replicate1/R2B_ABORT384_MODULE_ROLLBACK_REPORT.json \
    replicate1/variant_summary.tsv \
    replicate1/variant_sensitive_rows.tsv \
    replicate1/all_variant_seed_rows.tsv \
    replicate1/console.log \
    replicate2/R2B_ABORT384_MODULE_ROLLBACK_REPORT.json \
    replicate2/variant_summary.tsv \
    replicate2/variant_sensitive_rows.tsv \
    replicate2/all_variant_seed_rows.tsv \
    replicate2/console.log >/dev/null
)
echo "DIAGNOSTIC_DIR=$OUT"
echo "UPLOAD_THIS=$PKG"
