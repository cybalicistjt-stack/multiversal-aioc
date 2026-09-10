#!/usr/bin/env bash
set -euo pipefail
BASE=${DWC_BASE:-$HOME/multiversal/dwc-tts}
G="$BASE/governance/multiversal-aioc"
P="$BASE/src/piper1-gpl"
C="$BASE/corpora/DWC_Synthetic_Bootstrap_Corpus_v0.2.1"
VENV="$BASE/envs/piper-v1.8.0"
TOOLS="$G/governance/application-planning/dwc-speech/tools"
TOOL="$TOOLS/DWC_Protected_R2B_v0.1.0.py"
EXPECTED_ABORT="ee6f767c2d34a713fd5c7c3834712641129f3bdadf4543e467f61f1c5d943446"
EXPECTED_PROMO="5a060141f20be076a9130c59a7da6d06294f912a3d0aa00b5a0c1b27ffda96e4"

ABORT=""
for d in $(ls -dt "$BASE"/runs/r2_protected_* 2>/dev/null || true); do
  f="$d/ABORT_R2_PROTECTED_batch0064.pt"
  if [[ -f "$f" ]] && [[ "$(sha256sum "$f" | awk '{print $1}')" == "$EXPECTED_ABORT" ]]; then
    ABORT="$f"; break
  fi
done
[[ -n "$ABORT" ]] || { echo "Exact governed batch-64 abort checkpoint not found" >&2; exit 2; }

PROMOTED=""
ACC=""
for d in $(ls -dt "$BASE"/runs/r1_flow_restore_promotion_* 2>/dev/null || true); do
  f="$d/R1_flow_restored_candidate.pt"
  a="$d/TTS_ENGINE_03_ACCEPTANCE_UTTERANCES_v0.2.0.tsv"
  if [[ -f "$f" && -f "$a" ]] && [[ "$(sha256sum "$f" | awk '{print $1}')" == "$EXPECTED_PROMO" ]]; then
    PROMOTED="$f"; ACC="$a"; break
  fi
done
[[ -n "$PROMOTED" ]] || { echo "Exact promoted R1 hybrid not found" >&2; exit 2; }
for f in "$TOOL" "$ABORT" "$PROMOTED" "$ACC"; do
  [[ -f "$f" ]] || { echo "Missing required file: $f" >&2; exit 3; }
done

source "$VENV/bin/activate"
python - <<'PY'
import torch
assert torch.cuda.is_available(), "CUDA unavailable"
print("GPU:", torch.cuda.get_device_name(0))
PY

RUN="$BASE/runs/r2b_protected_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$RUN"
set +e
python "$TOOL" \
  --piper-src "$P" \
  --abort-checkpoint "$ABORT" \
  --promoted-checkpoint "$PROMOTED" \
  --corpus-root "$C" \
  --acceptance-tsv "$ACC" \
  --output-dir "$RUN" \
  --device cuda \
  --seed 20260908 \
  --probe-every 8 \
  --primary-gate-every 64 \
  --robust-gate-every 128 \
  --checkpoint-every 128 \
  --max-probe-drop-db 18 | tee "$RUN/console.log"
RC=${PIPESTATUS[0]}
set -e

(
  cd "$RUN"
  : > SHA256SUMS.txt
  shopt -s nullglob
  files=(R2B_PROTECTED_RESULT.json R2B_PROTECTED_metrics.jsonl R2B_schedule_manifest.tsv console.log R2B_*_seed*.tsv R2B_*_primary_gate.tsv)
  for f in "${files[@]}"; do
    [[ -f "$f" ]] && sha256sum "$f" >> SHA256SUMS.txt
  done
)

WIN_HOME=$(cmd.exe /C "echo %USERPROFILE%" 2>/dev/null | tr -d '\r')
WIN_DL="$(wslpath "$WIN_HOME")/Downloads"
PKG="$WIN_DL/DWC_R2B_PROTECTED_RESULT_$(date +%Y%m%d_%H%M%S).zip"
(
  cd "$RUN"
  shopt -s nullglob
  files=(SHA256SUMS.txt console.log R2B_PROTECTED_RESULT.json R2B_PROTECTED_metrics.jsonl R2B_schedule_manifest.tsv R2B_*_seed*.tsv R2B_*_primary_gate.tsv)
  zip -9 "$PKG" "${files[@]}" >/dev/null
)

echo "ABORT64_SOURCE=$ABORT"
echo "PROMOTED_DP_SOURCE=$PROMOTED"
echo "RUN_DIR=$RUN"
echo "UPLOAD_THIS=$PKG"

if [[ $RC -ne 0 ]]; then
  echo "Protected R2B stopped at a governed guard or runtime error; upload the result ZIP before retrying." >&2
fi
exit $RC
