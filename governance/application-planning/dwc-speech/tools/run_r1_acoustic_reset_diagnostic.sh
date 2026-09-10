#!/usr/bin/env bash
set -euo pipefail
BASE=${DWC_BASE:-$HOME/multiversal/dwc-tts}
G="$BASE/governance/multiversal-aioc"
H="$BASE/harness/DWC_Piper_RepairedCorpus_Retrain_v0.1.0"
P="$BASE/src/piper1-gpl"
VENV="$BASE/envs/piper-v1.8.0"
RUN=$(ls -dt "$BASE"/runs/repair_retrain_* 2>/dev/null | head -1 || true)
if [[ -z "$RUN" ]]; then echo "No repair_retrain run found under $BASE/runs" >&2; exit 2; fi
CK="$RUN/R1_phone_balanced_weights_batch0128.pt"
LEGACY="$H/TTS_ENGINE_03_ACCEPTANCE_UTTERANCES.tsv"
TOOLS="$G/governance/application-planning/dwc-speech/tools"
FIXED="$RUN/TTS_ENGINE_03_ACCEPTANCE_UTTERANCES_v0.2.0.tsv"
DIAG="$BASE/runs/r1_acoustic_reset_diag_$(date +%Y%m%d_%H%M%S)"
WARM=$(find "$BASE" -type f -name 'lj-med_1000.ckpt' -print -quit 2>/dev/null || true)
if [[ -z "$WARM" ]]; then echo "Could not locate lj-med_1000.ckpt under $BASE" >&2; exit 3; fi
for f in "$CK" "$WARM" "$LEGACY" "$TOOLS/DWC_REPAIR_ACCEPTANCE_IDENTITIES_v0.1.0.py" "$TOOLS/DWC_R1_Acoustic_Reset_Diagnostic_v0.1.0.py"; do
  [[ -f "$f" ]] || { echo "Missing required file: $f" >&2; exit 4; }
done
source "$VENV/bin/activate"
python - <<'PY'
import torch
assert torch.cuda.is_available(), 'CUDA unavailable'
print('GPU:', torch.cuda.get_device_name(0))
PY
python "$TOOLS/DWC_REPAIR_ACCEPTANCE_IDENTITIES_v0.1.0.py" "$LEGACY" "$FIXED"
mkdir -p "$DIAG"
python "$TOOLS/DWC_R1_Acoustic_Reset_Diagnostic_v0.1.0.py" \
  --piper-src "$P" \
  --r1-checkpoint "$CK" \
  --warmstart-checkpoint "$WARM" \
  --acceptance-tsv "$FIXED" \
  --output-dir "$DIAG" \
  --device cuda \
  --seed 20260908 | tee "$DIAG/console.log"
WIN_HOME=$(cmd.exe /C "echo %USERPROFILE%" 2>/dev/null | tr -d '\r')
WIN_DL="$(wslpath "$WIN_HOME")/Downloads"
PKG="$WIN_DL/DWC_R1_ACOUSTIC_RESET_DIAGNOSTIC_$(date +%Y%m%d_%H%M%S).zip"
(
  cd "$DIAG"
  zip -9 "$PKG" R1_ACOUSTIC_RESET_DIAGNOSTIC_SUMMARY.json SHA256SUMS.txt console.log *.tsv >/dev/null
)
echo "DIAGNOSTIC_DIR=$DIAG"
echo "UPLOAD_THIS=$PKG"
