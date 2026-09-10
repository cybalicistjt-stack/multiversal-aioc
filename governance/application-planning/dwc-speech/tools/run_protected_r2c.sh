#!/usr/bin/env bash
set -euo pipefail
BASE=${DWC_BASE:-$HOME/multiversal/dwc-tts}
G="$BASE/governance/multiversal-aioc"
P="$BASE/src/piper1-gpl"
C="$BASE/corpora/DWC_Synthetic_Bootstrap_Corpus_v0.2.1"
VENV="$BASE/envs/piper-v1.8.0"
TOOLS="$G/governance/application-planning/dwc-speech/tools"
TOOL="$TOOLS/DWC_Protected_R2C_v0.1.0.py"
EXPECTED_ABORT384="5a53ce2dde13df389fada834cc027283ef14dc2be44a102fc9fedd249716fd1b"
EXPECTED_CK256="88afedca8530f95eaa276568c15aa8612570e51f7aad2a04c6c51b49464e8ff6"
R2B=""; ABORT384=""; CK256=""
for d in $(ls -dt "$BASE"/runs/r2b_protected_* 2>/dev/null || true); do
  a="$d/ABORT_R2B_PROTECTED_batch0384.pt"; c="$d/R2B_PROTECTED_weights_batch0256.pt"
  if [[ -f "$a" && -f "$c" ]] && [[ "$(sha256sum "$a" | awk '{print $1}')" == "$EXPECTED_ABORT384" ]] && [[ "$(sha256sum "$c" | awk '{print $1}')" == "$EXPECTED_CK256" ]]; then R2B="$d"; ABORT384="$a"; CK256="$c"; break; fi
done
[[ -n "$R2B" ]] || { echo "Exact governed replicate-2 batch256/batch384 pair not found" >&2; exit 2; }
ACC=""
for d in $(ls -dt "$BASE"/runs/r1_flow_restore_promotion_* 2>/dev/null || true); do a="$d/TTS_ENGINE_03_ACCEPTANCE_UTTERANCES_v0.2.0.tsv"; if [[ -f "$a" ]]; then ACC="$a"; break; fi; done
[[ -n "$ACC" ]] || { echo "Corrected 125-row acceptance table not found" >&2; exit 2; }
for f in "$TOOL" "$ABORT384" "$CK256" "$ACC"; do [[ -f "$f" ]] || { echo "Missing required file: $f" >&2; exit 3; }; done
source "$VENV/bin/activate"
python -m py_compile "$TOOL"
python - <<'PY'
import torch
assert torch.cuda.is_available(), "CUDA unavailable"
print("GPU:", torch.cuda.get_device_name(0))
PY
RUN="$BASE/runs/r2c_protected_$(date +%Y%m%d_%H%M%S)"; mkdir -p "$RUN"
set +e
python "$TOOL" --piper-src "$P" --checkpoint256 "$CK256" --abort384 "$ABORT384" --corpus-root "$C" --acceptance-tsv "$ACC" --output-dir "$RUN" --device cuda --seed 20260908 --probe-every 8 --primary-gate-every 32 --robust-gate-every 64 --max-probe-drop-db 18 | tee "$RUN/console.log"
RC=${PIPESTATUS[0]}; set -e
(
  cd "$RUN"; : > SHA256SUMS.txt; shopt -s nullglob
  files=(R2C_PROTECTED_RESULT.json R2C_PROTECTED_metrics.jsonl R2C_schedule_manifest.tsv console.log R2C_*_seed*.tsv R2C_*_primary_gate.tsv)
  for f in "${files[@]}"; do [[ -f "$f" ]] && sha256sum "$f" >> SHA256SUMS.txt; done
  for big in R2C_source_rep2_abort384_encp_restored.pt R2C_PROTECTED_weights_batch0799.pt R2C_RESUME_LATEST.pt ABORT_R2C_PROTECTED_batch*.pt; do [[ -f "$big" ]] && sha256sum "$big" >> SHA256SUMS.txt; done
)
WIN_HOME=$(cmd.exe /C "echo %USERPROFILE%" 2>/dev/null | tr -d '\r'); WIN_DL="$(wslpath "$WIN_HOME")/Downloads"; PKG="$WIN_DL/DWC_R2C_PROTECTED_RESULT_$(date +%Y%m%d_%H%M%S).zip"
(
  cd "$RUN"; shopt -s nullglob; files=(SHA256SUMS.txt console.log R2C_PROTECTED_RESULT.json R2C_PROTECTED_metrics.jsonl R2C_schedule_manifest.tsv R2C_*_seed*.tsv R2C_*_primary_gate.tsv); zip -9 "$PKG" "${files[@]}" >/dev/null
)
echo "R2B_REPLICATE2_SOURCE=$R2B"; echo "CHECKPOINT256=$CK256"; echo "ABORT384=$ABORT384"; echo "RUN_DIR=$RUN"; echo "UPLOAD_THIS=$PKG"
if [[ $RC -ne 0 ]]; then echo "Protected R2C stopped at a governed guard or runtime error; upload the result ZIP before retrying." >&2; fi
exit $RC
