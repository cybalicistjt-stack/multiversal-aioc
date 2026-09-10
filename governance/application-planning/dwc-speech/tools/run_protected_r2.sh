#!/usr/bin/env bash
set -euo pipefail
BASE=${DWC_BASE:-$HOME/multiversal/dwc-tts}
G="$BASE/governance/multiversal-aioc"
H="$BASE/harness/DWC_Piper_RepairedCorpus_Retrain_v0.1.0"
P="$BASE/src/piper1-gpl"
C="$BASE/corpora/DWC_Synthetic_Bootstrap_Corpus_v0.2.1"
VENV="$BASE/envs/piper-v1.8.0"
TOOLS="$G/governance/application-planning/dwc-speech/tools"
LEGACY="$H/TTS_ENGINE_03_ACCEPTANCE_UTTERANCES.tsv"
PROMO=$(ls -dt "$BASE"/runs/r1_flow_restore_promotion_* 2>/dev/null | head -1 || true)
if [[ -z "$PROMO" ]]; then echo "No flow-restore promotion run found" >&2; exit 2; fi
HYBRID="$PROMO/R1_flow_restored_candidate.pt"
PROMO_REPORT="$PROMO/R1_FLOW_RESTORE_PROMOTION_REPORT.json"
for f in "$HYBRID" "$PROMO_REPORT" "$LEGACY" "$TOOLS/DWC_REPAIR_ACCEPTANCE_IDENTITIES_v0.1.0.py" "$TOOLS/DWC_Protected_R2_v0.1.0.py"; do
  [[ -f "$f" ]] || { echo "Missing required file: $f" >&2; exit 3; }
done
source "$VENV/bin/activate"
python - <<PY
import hashlib, json, pathlib, torch
p=pathlib.Path(r'''$HYBRID''')
r=json.load(open(r'''$PROMO_REPORT''',encoding='utf-8'))
assert r['status']=='PROMOTION_READY', r['status']
h=hashlib.sha256(p.read_bytes()).hexdigest()
assert h==r['hybrid']['sha256'], (h,r['hybrid']['sha256'])
assert p.stat().st_size==r['hybrid']['bytes'], (p.stat().st_size,r['hybrid']['bytes'])
assert torch.cuda.is_available(), 'CUDA unavailable'
print('GPU:',torch.cuda.get_device_name(0))
print('PROMOTED_HYBRID_SHA256:',h)
PY
FIXED="$PROMO/TTS_ENGINE_03_ACCEPTANCE_UTTERANCES_v0.2.0.tsv"
python "$TOOLS/DWC_REPAIR_ACCEPTANCE_IDENTITIES_v0.1.0.py" "$LEGACY" "$FIXED"
RUN="$BASE/runs/r2_protected_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$RUN"
set +e
python "$TOOLS/DWC_Protected_R2_v0.1.0.py" \
  --piper-src "$P" \
  --checkpoint "$HYBRID" \
  --corpus-root "$C" \
  --acceptance-tsv "$FIXED" \
  --output-dir "$RUN" \
  --device cuda \
  --seed 20260908 \
  --probe-every 8 \
  --full-gate-every 64 \
  --checkpoint-every 128 \
  --max-probe-drop-db 18 | tee "$RUN/console.log"
RC=${PIPESTATUS[0]}
set -e
(
  cd "$RUN"
  : > SHA256SUMS.txt
  for f in R2_PROTECTED_RESULT.json R2_PROTECTED_metrics.jsonl console.log R2_seed_*_gate.tsv R2_PROTECTED_weights_batch*.pt ABORT_R2_PROTECTED_batch*.pt; do
    for x in $f; do
      [[ -f "$x" ]] && sha256sum "$x" >> SHA256SUMS.txt
    done
  done
)
WIN_HOME=$(cmd.exe /C "echo %USERPROFILE%" 2>/dev/null | tr -d '\r')
WIN_DL="$(wslpath "$WIN_HOME")/Downloads"
PKG="$WIN_DL/DWC_R2_PROTECTED_RESULT_$(date +%Y%m%d_%H%M%S).zip"
(
  cd "$RUN"
  FILES=(SHA256SUMS.txt console.log R2_PROTECTED_metrics.jsonl)
  [[ -f R2_PROTECTED_RESULT.json ]] && FILES+=(R2_PROTECTED_RESULT.json)
  for f in R2_seed_*_gate.tsv; do [[ -f "$f" ]] && FILES+=("$f"); done
  zip -9 "$PKG" "${FILES[@]}" >/dev/null
)
echo "SOURCE_HYBRID=$HYBRID"
echo "RUN_DIR=$RUN"
echo "UPLOAD_THIS=$PKG"
if [[ $RC -ne 0 ]]; then
  echo "Protected R2 stopped at a governed guard or runtime error; upload the result ZIP before retrying." >&2
fi
exit $RC
