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
CK="$R2/ABORT_R2_PROTECTED_batch0064.pt"
ACC="$PROMO/TTS_ENGINE_03_ACCEPTANCE_UTTERANCES_v0.2.0.tsv"
TOOL="$TOOLS/DWC_R1_Inference_Diagnostic_v0.1.0.py"
for f in "$CK" "$ACC" "$TOOL"; do [[ -f "$f" ]] || { echo "Missing required file: $f" >&2; exit 3; }; done
source "$VENV/bin/activate"
python - <<'PY'
import torch
assert torch.cuda.is_available(), 'CUDA unavailable'
print('GPU:', torch.cuda.get_device_name(0))
PY
OUT="$BASE/runs/r2_abort64_inference_diag_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUT"
python "$TOOL" \
  --piper-src "$P" \
  --r1-checkpoint "$CK" \
  --acceptance-tsv "$ACC" \
  --output-dir "$OUT" \
  --device cuda \
  --seed 20260908 | tee "$OUT/console.log"
python - "$OUT/default_reproduction.tsv" <<'PY'
import csv,sys
p=sys.argv[1]
rows=list(csv.DictReader(open(p,encoding='utf-8'),delimiter='\t'))
bad=[r for r in rows if r['status']!='PASS']
print('PRIMARY_GATE_FAILED_ROWS=',len(bad))
for r in bad:
    print(r['acceptance_row_id'],r['source_utterance_id'],'status='+r['status'],'notes='+r['notes'],'duration='+r['duration_s'],'peak_dbfs='+r['peak_dbfs'],'rms_dbfs='+r['rms_dbfs'],'dwc='+r['dwc_text'])
PY
WIN_HOME=$(cmd.exe /C "echo %USERPROFILE%" 2>/dev/null | tr -d '\r')
WIN_DL="$(wslpath "$WIN_HOME")/Downloads"
PKG="$WIN_DL/DWC_R2_ABORT64_INFERENCE_DIAGNOSTIC_$(date +%Y%m%d_%H%M%S).zip"
(
  cd "$OUT"
  zip -9 "$PKG" R1_INFERENCE_DIAGNOSTIC_SUMMARY.json SHA256SUMS.txt console.log *.tsv >/dev/null
)
echo "ABORT_CHECKPOINT=$CK"
echo "DIAGNOSTIC_DIR=$OUT"
echo "UPLOAD_THIS=$PKG"
