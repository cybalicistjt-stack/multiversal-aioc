#!/usr/bin/env bash
set -euo pipefail
BASE=${DWC_BASE:-$HOME/multiversal/dwc-tts}
G="$BASE/governance/multiversal-aioc"
TOOLS="$G/governance/application-planning/dwc-speech/tools"
TOOL="$TOOLS/DWC_Prepare_R2C_Human_Evaluation_v0.1.0.py"
EXPECTED_FINAL="c26ecb279ed5759a4c251ad54c80ebaa38e055194f6698681922b33e64269a3e"
RUN=""
for d in $(ls -dt "$BASE"/runs/r2c_protected_* 2>/dev/null || true); do
  ck="$d/R2C_PROTECTED_weights_batch0799.pt"
  rs="$d/R2C_PROTECTED_RESULT.json"
  wav="$d/wav/R2C_final"
  if [[ -f "$ck" && -f "$rs" && -d "$wav" ]] && [[ "$(sha256sum "$ck" | awk '{print $1}')" == "$EXPECTED_FINAL" ]]; then RUN="$d"; break; fi
done
[[ -n "$RUN" ]] || { echo "Exact passing R2C batch-799 run not found" >&2; exit 2; }
ACC=""
for d in $(ls -dt "$BASE"/runs/r1_flow_restore_promotion_* 2>/dev/null || true); do
  a="$d/TTS_ENGINE_03_ACCEPTANCE_UTTERANCES_v0.2.0.tsv"
  [[ -f "$a" ]] && { ACC="$a"; break; }
done
[[ -n "$ACC" ]] || { echo "Corrected 125-row acceptance table not found" >&2; exit 2; }
python3 -m py_compile "$TOOL"
WIN_HOME=$(cmd.exe /C "echo %USERPROFILE%" 2>/dev/null | tr -d '\r')
WIN_DL="$(wslpath "$WIN_HOME")/Downloads"
OUT="$WIN_DL/DWC_R2C_HUMAN_REVIEW_$(date +%Y%m%d_%H%M%S)"
python3 "$TOOL" --run-dir "$RUN" --acceptance-tsv "$ACC" --output-dir "$OUT"
echo "MACHINE_RUN=$RUN"
echo "REVIEW_DIR=$OUT"
echo "OPEN_THIS=$OUT/review.html"
echo "PACKAGE_ZIP=$OUT.zip"
