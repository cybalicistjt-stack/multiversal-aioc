#!/usr/bin/env bash
set -euo pipefail
BASE=${DWC_BASE:-$HOME/multiversal/dwc-tts}
G="$BASE/governance/multiversal-aioc"
P="$BASE/src/piper1-gpl"
VENV="$BASE/envs/piper-v1.8.0"
TOOLS="$G/governance/application-planning/dwc-speech/tools"
R2=$(ls -dt "$BASE"/runs/r2_protected_* 2>/dev/null | head -1 || true)
PROMO=$(ls -dt "$BASE"/runs/r1_flow_restore_promotion_* 2>/dev/null | head -1 || true)
[[ -n "$R2" ]] || { echo "No protected R2 run found" >&2; exit 2; }
[[ -n "$PROMO" ]] || { echo "No flow-restore promotion run found" >&2; exit 2; }
ABORT="$R2/ABORT_R2_PROTECTED_batch0064.pt"
SOURCE="$PROMO/R1_flow_restored_candidate.pt"
ACC="$PROMO/TTS_ENGINE_03_ACCEPTANCE_UTTERANCES_v0.2.0.tsv"
TOOL="$TOOLS/DWC_R2_Abort64_Module_Rollback_Diagnostic_v0.1.0.py"
for f in "$ABORT" "$SOURCE" "$ACC" "$TOOL"; do [[ -f "$f" ]] || { echo "Missing required file: $f" >&2; exit 3; }; done
source "$VENV/bin/activate"
python - <<'PY'
import torch
assert torch.cuda.is_available(), 'CUDA unavailable'
print('GPU:',torch.cuda.get_device_name(0))
PY
OUT="$BASE/runs/r2_abort64_module_rollback_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUT"
python "$TOOL" \
  --piper-src "$P" \
  --abort-checkpoint "$ABORT" \
  --promoted-checkpoint "$SOURCE" \
  --acceptance-tsv "$ACC" \
  --output-dir "$OUT" \
  --device cuda \
  --seed 20260908 | tee "$OUT/console.log"
WIN_HOME=$(cmd.exe /C "echo %USERPROFILE%" 2>/dev/null | tr -d '\r')
WIN_DL="$(wslpath "$WIN_HOME")/Downloads"
PKG="$WIN_DL/DWC_R2_ABORT64_MODULE_ROLLBACK_DIAGNOSTIC_$(date +%Y%m%d_%H%M%S).zip"
(
  cd "$OUT"
  zip -9 "$PKG" R2_ABORT64_MODULE_ROLLBACK_REPORT.json SHA256SUMS.txt console.log variant_summary.tsv variant_sensitive_rows.tsv all_variant_seed_rows.tsv >/dev/null
)
echo "ABORT_CHECKPOINT=$ABORT"
echo "PROMOTED_SOURCE=$SOURCE"
echo "DIAGNOSTIC_DIR=$OUT"
echo "UPLOAD_THIS=$PKG"
