#!/usr/bin/env bash
set -euo pipefail
BASE=${DWC_BASE:-$HOME/multiversal/dwc-tts}
G="$BASE/governance/multiversal-aioc"
P="$BASE/src/piper1-gpl"
VENV="$BASE/envs/piper-v1.8.0"
TOOLS="$G/governance/application-planning/dwc-speech/tools"
TOOL="$TOOLS/DWC_R2B_Abort384_Module_Rollback_Diagnostic_v0.1.0.py"
EXPECTED_ABORT="c24d461484ebb714fb7484cc1616c2790c12df81c0d2d726f13f852ff01434fc"
EXPECTED_PROMO="5a060141f20be076a9130c59a7da6d06294f912a3d0aa00b5a0c1b27ffda96e4"

R2B=""
ABORT=""
CK256=""
for d in $(ls -dt "$BASE"/runs/r2b_protected_* 2>/dev/null || true); do
  a="$d/ABORT_R2B_PROTECTED_batch0384.pt"
  c="$d/R2B_PROTECTED_weights_batch0256.pt"
  if [[ -f "$a" && -f "$c" ]] && [[ "$(sha256sum "$a" | awk '{print $1}')" == "$EXPECTED_ABORT" ]]; then
    R2B="$d"; ABORT="$a"; CK256="$c"; break
  fi
done
[[ -n "$R2B" ]] || { echo "Exact governed R2B batch-384 run/checkpoint pair not found" >&2; exit 2; }

PROMO=""
ACC=""
for d in $(ls -dt "$BASE"/runs/r1_flow_restore_promotion_* 2>/dev/null || true); do
  f="$d/R1_flow_restored_candidate.pt"
  a="$d/TTS_ENGINE_03_ACCEPTANCE_UTTERANCES_v0.2.0.tsv"
  if [[ -f "$f" && -f "$a" ]] && [[ "$(sha256sum "$f" | awk '{print $1}')" == "$EXPECTED_PROMO" ]]; then
    PROMO="$f"; ACC="$a"; break
  fi
done
[[ -n "$PROMO" ]] || { echo "Exact promoted R1 hybrid / corrected acceptance table not found" >&2; exit 2; }

for f in "$TOOL" "$ABORT" "$CK256" "$ACC"; do
  [[ -f "$f" ]] || { echo "Missing required file: $f" >&2; exit 3; }
done

source "$VENV/bin/activate"
python -m py_compile "$TOOL"
python - <<'PY'
import torch
assert torch.cuda.is_available(), "CUDA unavailable"
print("GPU:", torch.cuda.get_device_name(0))
PY

OUT="$BASE/runs/r2b_abort384_module_rollback_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUT"
python "$TOOL" \
  --piper-src "$P" \
  --checkpoint256 "$CK256" \
  --abort384 "$ABORT" \
  --acceptance-tsv "$ACC" \
  --output-dir "$OUT" \
  --device cuda \
  --seed 20260908 | tee "$OUT/console.log"

WIN_HOME=$(cmd.exe /C "echo %USERPROFILE%" 2>/dev/null | tr -d '\r')
WIN_DL="$(wslpath "$WIN_HOME")/Downloads"
PKG="$WIN_DL/DWC_R2B_ABORT384_MODULE_ROLLBACK_DIAGNOSTIC_$(date +%Y%m%d_%H%M%S).zip"
(
  cd "$OUT"
  zip -9 "$PKG" R2B_ABORT384_MODULE_ROLLBACK_REPORT.json SHA256SUMS.txt console.log variant_summary.tsv variant_sensitive_rows.tsv all_variant_seed_rows.tsv >/dev/null
)

echo "R2B_RUN=$R2B"
echo "CHECKPOINT256=$CK256"
echo "ABORT384=$ABORT"
echo "DIAGNOSTIC_DIR=$OUT"
echo "UPLOAD_THIS=$PKG"
