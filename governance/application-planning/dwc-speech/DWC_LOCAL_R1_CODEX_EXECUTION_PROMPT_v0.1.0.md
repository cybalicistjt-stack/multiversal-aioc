# DWC Local Guarded R1 — Codex Execution Prompt v0.1.0

Use this prompt on the verified local DWC workstation.

---

Continue the DWC speech-synthesis track from the verified local workstation state. This is execution, not environment setup and not a redesign exercise.

First execute:

```bash
/home/antiquaria/multiversal/bootstrap/DWC_Local_Workstation_Bootstrap_v0.1.0/scripts/sync_governance.sh
```

Then read the freshly synchronized:

- `governance/application-planning/dwc-speech/DWC_CURRENT_STATE.json`
- `governance/application-planning/dwc-speech/DWC_REPAIRED_CORPUS_RETRAIN_HANDOFF_v0.1.2.json`
- `governance/application-planning/dwc-speech/DWC_LOCAL_WORKSTATION_SURFACE_2026-09-10.json`

Confirm that the guarded repaired-corpus R1 path remains the latest authorized DWC acoustic operation. If newer verified evidence supersedes it, follow the newer evidence instead and do not run a stale path.

If R1 remains authorized, execute:

```bash
/home/antiquaria/multiversal/bootstrap/DWC_Local_Workstation_Bootstrap_v0.1.0/scripts/run_repaired_retrain.sh
```

Remain in execution mode through the entire safe governed boundary. Do not stop for ordinary progress commentary.

Hard invariants:

- Do not continue from `stageC_weights.pt`.
- Do not run `DWC_Piper_Custom58_StageD_Continuation_v0.1.ipynb` as the normal path.
- Do not use superseded `DWC_Piper_RepairedCorpus_GPU_Retrain_v0.1.ipynb`.
- Do not redesign DWC phonology/PSS/CNS or change exact custom phoneme IDs to accommodate acoustic behavior.
- Do not weaken SHA-256, corpus-identity, waveform RMS, collapse, 125-row acceptance, or human-perceptual gates.
- Do not treat a machine waveform PASS as human CNS perceptual acceptance.
- Use repaired corpus v0.2.1 and the established exact warm-start checkpoint.

Expected governed sequence:

1. Construct the fresh exact-58 Piper model and reuse the already-proven vocoder-only warm-start.
2. Run and preserve the 8-row raw-inference amplitude baseline before adaptation.
3. Run R1 on the 128 unique governed phone-balanced repaired rows.
4. Preserve every scheduled amplitude probe. If the collapse guard fires, abort at that exact point and preserve the diagnostic checkpoint/logs; do not enter R2.
5. If R1 completes, render and evaluate the deterministic 125-row machine waveform acceptance suite using the real governed floor.
6. R2 is authorized only if R1 is genuinely 125/125.
7. If R2 is authorized, complete one deterministic shuffled pass over all 799 repaired rows, with scheduled probes, then apply the real 125-row machine waveform gate again.
8. Human CNS perceptual acceptance remains pending even if the machine gate passes.

Do not alter learning rates or other training parameters preemptively. Corpus repair is the principal changed variable in this experiment. If an evidenced implementation/runtime incompatibility prevents execution, diagnose and minimally repair that incompatibility without changing the experimental question or acceptance thresholds.

Persist a compact result package containing at minimum:

- exact start/end timestamps;
- Piper commit and local patch state;
- Python/PyTorch/CUDA/GPU identity;
- repaired corpus SHA-256;
- warm-start checkpoint SHA-256;
- 8-row baseline metrics and median raw RMS dBFS;
- every R1 probe;
- R1 first/last relevant losses and optimizer-step/batch counts;
- whether the collapse guard fired;
- R1 125-row acceptance counts and any review/failure rows;
- whether R2 was authorized and entered;
- R2 probe/training/acceptance data if entered;
- GPU peak VRAM and elapsed runtime;
- SHA-256 hashes and paths for all resulting checkpoints, result JSON, logs and rendered acceptance audio;
- explicit `human_perceptual_gate: NOT_RUN` unless an actual human review was separately performed.

Also produce one small machine-readable `DWC_LOCAL_RETRAIN_RESULT.json` that another ChatGPT conversation can inspect without parsing the full logs.

Do not modify the global Multiversal software-roadmap pointer. DWC continuity is a separate governed track.

Stop only when the governed run has reached one of these real boundaries:

- R1 collapse-guard abort with preserved diagnostic evidence;
- R1 completes but fails the 125-row machine gate, with evidence preserved;
- R1 passes, R2 runs, and R2 completes or aborts under its governed gate;
- a genuine environment/runtime blocker survives diagnosis and is documented precisely.

At the end, report only the verified result and the exact artifact paths/hashes needed for the next DWC continuation.

---
