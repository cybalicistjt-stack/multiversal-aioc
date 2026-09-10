# DWC Speech Synthesis — Local Workstation Anchor Addendum — 2026-09-10

**Status:** VERIFIED EXECUTION-SURFACE ADDENDUM  
**Authority:** DWC project continuity only; does not select or alter the Multiversal software roadmap.

## Superseding execution-surface fact

The earlier DWC anchor described the corrected v0.1.1 Colab notebook as the exact external GPU path because no persistent authorized GPU surface was then available. That execution-surface statement is now superseded.

A persistent local WSL2 workstation is verified and is the preferred DWC acoustic-training surface:

- WSL 2.7.11.0, kernel 6.18.33.2;
- Ubuntu 26.04 LTS;
- NVIDIA GeForce RTX 4060 Laptop GPU, 8,188 MiB VRAM;
- NVIDIA driver 610.78; NVIDIA-SMI visible in Windows and WSL; driver reports CUDA 13.3;
- Python 3.14.4;
- PyTorch 2.14.0+cu130 with CUDA available;
- a real GPU allocation and computation test passed;
- OHF-Voice/piper1-gpl v1.8.0 at commit `639388b6317fc4731e91d53da42aea68fd4166ff`;
- Piper monotonic alignment compiled and passed a functional test;
- the workstation records a one-line v1.8.0 compatibility correction for the alignment import path;
- repaired corpus, warm-start checkpoint parts, retrain harness and corrected v0.1.1 notebook passed the local setup/preflight verification;
- no required retrain files are missing.

The persistent DWC root is:

`/home/antiquaria/multiversal/dwc-tts`

The exact preferred launch sequence is:

```bash
/home/antiquaria/multiversal/bootstrap/DWC_Local_Workstation_Bootstrap_v0.1.0/scripts/sync_governance.sh
/home/antiquaria/multiversal/bootstrap/DWC_Local_Workstation_Bootstrap_v0.1.0/scripts/run_repaired_retrain.sh
```

The first command must immediately recheck mutable DWC governance before the second command executes.

## Training authority preserved

The workstation changes **where** the next experiment runs, not **what** the experiment is.

The authorized forward sequence remains:

1. fresh exact-58 Piper model;
2. proven `lj-med_1000.ckpt` vocoder-only warm-start;
3. 8-row raw inference amplitude baseline;
4. R1 over 128 unique governed repaired rows with periodic amplitude probes;
5. real deterministic 125-row waveform gate;
6. R2 only if R1 is genuinely 125/125;
7. R2 over one deterministic shuffled pass of the 799 repaired rows with periodic probes;
8. real 125-row waveform gate again;
9. governed human CNS perceptual evaluation only after a valid machine candidate exists.

The collapse guard and -55 dBFS waveform floor remain unchanged. Historical Stage-C weights remain diagnostic/provenance only and are not an authorized forward-training source.

## Colab status

`DWC_Piper_RepairedCorpus_GPU_Retrain_v0.1.1.ipynb` remains a verified fallback artifact if the local workstation becomes unavailable. It is no longer the preferred normal execution surface.

## Recovery rule

Future DWC conversations must read `DWC_CURRENT_STATE.json` and `DWC_LOCAL_WORKSTATION_SURFACE_2026-09-10.json` before directing acoustic training. Do not regress to the obsolete assumption that the project is blocked on obtaining a GPU runtime.
