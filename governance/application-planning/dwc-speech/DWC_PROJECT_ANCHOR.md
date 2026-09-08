# DWC Speech Synthesis Project — Durable Project Anchor

**Project:** DWC language-to-speech / native speech synthesis  
**Owner and final authority:** John Brandon Turner  
**Status:** ACTIVE RESEARCH / IMPLEMENTATION  
**Created:** 2026-09-08  
**Updated:** 2026-09-08  
**Role:** durable human-readable DWC continuity authority; not Multiversal software-roadmap work selection

## 1. Recovery principle

DWC must be recovered from durable evidence rather than reconstructed from chat history.

> **Project state is defined by verified artifacts, code, files, tool results, and explicit owner corrections. Assistant prose is commentary about that state, not the state itself.**

Read `DWC_CURRENT_STATE.json` for the mutable frontier. Newer verified evidence may supersede an older training interpretation without erasing the historical fact that a run occurred.

## 2. Goal and settled architecture

Build a robust speech path in which DWC's own language and phonological system controls pronunciation end to end.

`DWC language / semantic form` → `etymology / lexical rules` → `PSS` → `CNS` → `engine-independent exact custom phoneme IDs` → `aligned corpus` → `acoustic model / TTS` → `waveform`.

Non-regression invariants:

- DWC pronunciation is not delegated to English G2P.
- Exact custom DWC phoneme identity survives into acoustic training/inference.
- Language rules are not changed merely to accommodate a weak acoustic model.
- Temporary bootstrap voices are acoustic scaffolding, not canonical CNS evidence.
- Authorized human CNS recordings will supersede bootstrap proxy audio for the authentic production voice.

## 3. Closed achievements

### Language/PSS/CNS and exact-ID frontend

Language, etymology, PSS, and CNS reached the pre-audio handoff. An engine-independent frontend emits the exact 58-symbol DWC phoneme IDs without English G2P.

### Neural proxy proof

The LJSpeech-medium ONNX neural proxy proved the frontend can drive neural speech: 199/199 regression utterances rendered, 0 unsupported CNS IPA symbols in that set, about 4.6 minutes of audio, and English G2P bypassed.

### Piper exact-ID and warm-start proof

Piper v1.8.0 work established direct exact-ID input, a 58×192 DWC embedding, vocoder-only warm-start from `lj-med_1000.ckpt`, 278 matching acoustic/vocoder tensors copied while preserving the DWC embedding, exact-ID inference, full VITS generator/discriminator loss, gradient flow into the DWC embedding, and real optimizer updates.

Warm-start feasibility is closed. It is reused as a known-good baseline, not rediscovered.

## 4. Historical Stage-A/B/C lineage — execution proven, candidate invalidated

Stages A, B, and C genuinely ran and remain useful execution/training evidence:

- Stage A: 100 batches / 200 optimizer steps.
- Stage B: 200 batches / 400 optimizer steps.
- Stage C: 100 targeted batches / 200 optimizer steps on a 128-row repair set.
- Stage-C weights were later reassembled and hash-verified at 281,775,417 bytes, SHA-256 `d800ae031942c29289ced1cc80c1448fff234c53f42a56f2d69265e7e3ebabb2`.

However, later audit proved that their source bootstrap corpus was not fit for candidate training and that the old Stage-C machine report was weaker than the governed acceptance contract.

Bootstrap corpus v0.1 contained:

- 799 rows but only 769 unique audio filenames;
- 10 filename-collision groups / 30 extra rows on colliding names;
- 290 digital-zero training rows;
- 290 rows below the governed -55 dBFS RMS floor;
- Stage-C's 128-row repair set contained 61 digital-zero rows and only 98 unique audio files.

Raw inference amplitude deteriorated as training proceeded:

- warm-start smoke: about -32.52 dBFS RMS;
- 8-step sample: about -62.23 dBFS RMS;
- Stage-A sample: about -82.89 dBFS RMS;
- Stage-C 125-row set: median about -93.98 dBFS RMS, range about -95.39 to -79.41 dBFS.

The governed acoustic validator requires RMS >= -55 dBFS. Therefore **0/125** Stage-C rows actually pass the intended waveform-level gate. The historical `125/125 PASS` report did not apply that threshold and is superseded for candidate acceptance.

Consequences:

- Stage-A/B/C execution history is preserved.
- Their model lineage is **not** a promotable acoustic candidate.
- `stageC_weights.pt` is diagnostic/provenance material, not the source for continued adaptation.
- `DWC_Piper_Custom58_StageD_Continuation_v0.1.ipynb` is superseded and not authorized as the normal forward path.

See `DWC_BOOTSTRAP_CORPUS_V0_1_FAILURE_AND_V0_2_1_REPAIR.json`.

## 5. Repaired temporary bootstrap corpus v0.2.1

A replacement corpus was created without changing the canonical DWC ID labels.

`DWC_Synthetic_Bootstrap_Corpus_v0.2.1.zip`:

- 799 rows;
- 799 unique governed `corpus_row_id` values (`DWCBOOT-0001`…`DWCBOOT-0799`);
- 799 unique WAV filenames;
- 0 rows below -55 dBFS;
- targets normalized around -24 dBFS RMS;
- exact DWC phoneme-ID sequences preserved as training labels;
- 26,439,488 bytes;
- SHA-256 `99aca0d65596f906b08a99e0f0c9708211fb150013e039c91f0c489fc0d6a4e3`;
- Drive file ID `1HPRmXb-DJOOiR9HW608S2GKP1XAqULzx`.

Its eSpeak 1.48.15 native-phoneme-input mapping is explicitly **noncanonical acoustic bootstrap material**. v0.2.1 supersedes v0.2.0 for governed row identity; the repaired audio bytes are unchanged from v0.2.0.

## 6. Current frontier — guarded repaired-corpus retrain

The authorized forward sequence is:

1. fresh exact-58 Piper model;
2. reuse the already-proven `lj-med_1000.ckpt` vocoder-only warm-start;
3. render an 8-row raw inference amplitude baseline;
4. **R1:** 128 unique governed phone-balanced rows, with probes every 8 batches;
5. apply the real 125-row waveform gate; R2 is prohibited unless R1 is 125/125;
6. **R2:** one deterministic shuffled pass over all 799 repaired rows, with amplitude probes;
7. apply the real 125-row waveform gate again;
8. only after machine success, run the governed human CNS perceptual gate.

The retrain aborts early and preserves diagnostic checkpoint/probe evidence if raw inference amplitude collapses. Piper's established default learning rates are retained so corpus repair is the principal changed variable.

## 7. Prepared execution assets

`DWC_Piper_RepairedCorpus_Retrain_v0.1.0.zip`
- 43,523 bytes;
- SHA-256 `96c978573c3a4d0a21acdd5b6f49fc86f8bfc70be045b4c0f4ae0ae5d2ec9007`;
- Drive file ID `1PnBQjwb5LH1b1xcidUod3xuYGuQbt07z`;
- local governed preflight passed: 799 corpus rows, 799 unique audio files, 128 unique R1 rows, 125 acceptance rows.

`DWC_Piper_RepairedCorpus_GPU_Retrain_v0.1.ipynb`
- 10,508 bytes;
- SHA-256 `e816c8b0b9647723cfa6447f1aaf3b8809b015aa56ada3f5b81a6737d915d99c`;
- Drive file ID `18nu5QdXgKBOw1LyB30QdlM6E3HmNzoWx`;
- Drive read-back verified.

The notebook verifies input hashes, runs the cheap repaired-corpus preflight before expensive setup, reconstructs/verifies the established warm-start checkpoint, installs Piper v1.8.0, runs guarded R1/R2 training, persists diagnostics/checkpoints to Drive, and exposes the human scorecard only after a valid machine pass.

See `DWC_REPAIRED_CORPUS_RETRAIN_HANDOFF_v0.1.0.json`.

## 8. Execution surfaces

The current ChatGPT sandbox has CPU-only PyTorch, no CUDA, and zero CUDA devices. Connected Hugging Face Jobs was also tested: both `cpu-basic` and `zero-a10g` requests returned `402 Payment Required`. Therefore sustained repaired retraining is not executable on those surfaces at present.

The read-back-verified GPU notebook is the exact external execution path unless another authorized GPU surface becomes available.

## 9. Human CNS perceptual gate

Machine waveform success is necessary but not sufficient. Human review remains mandatory for intelligibility, pronunciation, special phones, stress/rhythm, target accent/style, and meaning preservation. A perceptual failure is first a data/model/training problem; it does not authorize changing settled DWC phonology.

## 10. Execution rules

- `Continue` means execute until the largest safe bounded unit closes or a genuine blocker is evidenced.
- A progress update is not a stop boundary.
- Recover from newest verified artifacts, not the last narrative paragraph.
- New sandbox = rehydration problem, not project reset.
- Preserve invalidated evidence and correct its authority instead of deleting it.
- A weak validator may be superseded when the governed acceptance contract proves it insufficient.
- Never promote generated audio/model artifacts without applying the correct machine and human gates.

## 11. Open work

- execute R1/R2 repaired-corpus retraining on a GPU surface;
- determine whether corrected targets preserve healthy raw inference amplitude;
- achieve governed 125/125 waveform acceptance on a valid lineage;
- complete human CNS perceptual acceptance;
- select/export a temporary synthetic candidate only after both gates;
- replace bootstrap proxy targets with authorized human CNS recordings for the authentic production voice;
- production packaging/licensing/deployment/Multiversal integration and final engine selection.

## 12. Recovery instruction

A future DWC conversation should start with these facts:

- language/PSS/CNS, exact-ID frontend, neural proxy, and Piper warm-start are settled;
- historical Stage A/B/C training occurred, but its **candidate lineage is invalidated** by corpus-v0.1 defects and near-silent inference;
- the old Stage-C `125/125` report is **not** a valid governed waveform pass;
- Stage-D continuation from Stage C is superseded/not authorized;
- repaired corpus v0.2.1 is validated and externally stored;
- the exact next acoustic operation is the guarded repaired-corpus R1/R2 GPU retrain using `DWC_Piper_RepairedCorpus_GPU_Retrain_v0.1.ipynb`;
- human CNS listening occurs only after a valid machine waveform pass;
- always read `DWC_CURRENT_STATE.json` before executing.
