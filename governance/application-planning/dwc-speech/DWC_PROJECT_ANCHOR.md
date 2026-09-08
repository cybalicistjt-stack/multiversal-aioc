# DWC Speech Synthesis Project — Durable Project Anchor

**Project:** DWC language-to-speech / native speech synthesis  
**Owner and final authority:** John Brandon Turner  
**Status:** ACTIVE RESEARCH / IMPLEMENTATION  
**Created:** 2026-09-08  
**Updated:** 2026-09-08  
**Role:** durable human-readable project reference; DWC continuity authority, not Multiversal software-roadmap work selection

## 1. Why this document exists

The DWC project accumulated substantial language-design, pronunciation, corpus, neural-proxy, warm-start, and real acoustic-training work inside long conversations. The technical work advanced farther than some narrative summaries recorded, while conversation execution repeatedly regressed after interruptions, tool timeouts, progress messages, and sandbox changes.

This file exists so DWC can be recovered from durable evidence rather than reconstructed from chat history.

> **Project state is defined by verified artifacts, code, files, tool results, and explicit owner corrections. Assistant prose is commentary about that state, not the state itself.**

Use `DWC_CURRENT_STATE.json` for the mutable execution frontier and `DWC_TRAINING_EVIDENCE_STAGE_C_v0.1.0.json` for the latest closed machine-training milestone.

## 2. Project goal

Build a robust speech-generation path for DWC in which DWC's own language and phonological system controls pronunciation end to end.

The target is not to make an English TTS engine approximate DWC. The target is a deterministic, engine-independent DWC pronunciation frontend that directly drives neural speech synthesis and can support a DWC-native/custom acoustic model.

Primary goals:

- DWC pronunciation is controlled by DWC rules rather than English G2P.
- The frontend preserves exact custom DWC phoneme identities/IDs.
- Equivalent DWC linguistic input produces deterministic phoneme output.
- The pronunciation layer remains engine-independent where practical.
- Training/inference preserve provenance from DWC linguistic representation through phoneme IDs to waveform output.
- Model/environment limitations are not mistaken for language-design failures.
- The architecture can later serve Multiversal without hard-coupling DWC language rules to one speech vendor/runtime.

## 3. Settled architecture

`DWC language / semantic form`  
→ `DWC etymology and lexical rules`  
→ `PSS pronunciation representation`  
→ `CNS canonical sound representation`  
→ `engine-independent exact custom phoneme IDs`  
→ `aligned DWC training / regression corpus`  
→ `acoustic model / TTS engine`  
→ `vocoder / waveform output`

Critical invariant: **English G2P must not silently reinterpret DWC between the DWC frontend and the neural model.**

## 4. Settled achievements

These are closed project facts unless contrary evidence appears.

### 4.1 Language/PSS/CNS reached the pre-audio handoff

The DWC language, etymology, PSS, and CNS work progressed far enough for speech synthesis to consume governed pronunciation output. This is not an open language-redesign restart point.

### 4.2 Engine-independent exact-ID frontend exists

A frontend exists that emits exact DWC phoneme IDs without delegating pronunciation to an English engine. This is an architectural non-regression boundary.

### 4.3 Synthetic exact-ID corpus exists

The synthetic bootstrap corpus contains **799 exact-ID aligned utterances** and passed the prior Piper exact-ID dataset preflight.

### 4.4 Neural proxy proof succeeded

The owner-supplied LJSpeech medium ONNX model/config was used to prove the DWC frontend could drive a neural speech path:

- **199/199** regression utterances rendered;
- **0 unsupported CNS IPA symbols** in that set;
- approximately **4.6 minutes** of neural DWC audio generated;
- English G2P bypassed.

Proxy success is not the same milestone as native/custom acoustic adaptation.

### 4.5 Piper exact-ID and warm-start viability succeeded

Piper v1.8.0 work established:

- direct owner-supplied `phoneme_ids` dataset input;
- a 58×192 DWC phoneme embedding;
- vocoder-only warm-start from the LJSpeech checkpoint;
- 278 matching acoustic/vocoder tensors copied while preserving the DWC embedding;
- exact DWC-ID inference;
- full VITS generator/discriminator loss;
- gradient flow into the DWC embedding;
- real optimizer updates.

Warm-start feasibility is closed. Repeating it is revalidation only.

### 4.6 Real acoustic adaptation progressed through Stage C

Later Drive recovery evidence superseded the older conversation-local recovery note.

**Stage A — balanced subset adaptation**

- 128 selected corpus rows;
- 100 training batches / 200 optimizer steps;
- training time ~114.68 s on the prior GPU surface;
- generator loss 287.7846 → 11.8234;
- mel loss 0.71298 → 0.10692.

**Stage B — full-corpus adaptation**

- all 799 synthetic rows;
- 200 training batches / 400 optimizer steps;
- training time ~228.52 s;
- machine waveform acceptance: **123/125 PASS**, 2 REVIEW.

The two Stage-B machine-review cases were:

- `CONTRAST-a_-01` — `ai`, IPA `[aɪ]`;
- `CONTRAST-_-05` — `sher`, IPA `[ɕɛr]`.

**Stage C — short-form / special-phone repair**

- 128 targeted rows: 75 special-phone contrast rows + 53 lexical phone-coverage rows;
- 100 training batches / 200 optimizer steps;
- training time ~114.28 s;
- generator loss 15.4027 → 6.5376;
- mel loss 0.05651 → 0.03367;
- machine waveform acceptance: **125/125 PASS**.

### 4.7 Stage-C model state is durably recovered and verified

The four Stage-C Drive parts were re-downloaded and reassembled in the 2026-09-08 recovery conversation.

Verified Stage-C state:

- file: `stageC_weights.pt`;
- size: **281,775,417 bytes**;
- SHA-256: **`d800ae031942c29289ced1cc80c1448fff234c53f42a56f2d69265e7e3ebabb2`**;
- 784 model-state tensor keys;
- `num_symbols = 58`;
- `sample_rate = 22050`;
- `segment_size = 2048`;
- `stageC_global_step = 200`.

The current reassembly hash exactly matched the earlier recovery hash. See `DWC_TRAINING_EVIDENCE_STAGE_C_v0.1.0.json`.

## 5. Current forward frontier

The project is now at:

> **Human/perceptual CNS evaluation + Stage-D continuation from the verified Stage-C weights + candidate export.**

It is no longer at checkpoint discovery, warm-start proof, initial optimizer proof, Stage A, Stage B, or Stage C.

Two independent gates now matter:

1. **GPU execution:** longer Stage-D adaptation must run on a GPU-capable surface. The current ChatGPT sandbox has CPU-only PyTorch and zero CUDA devices.
2. **Human auditory evaluation:** 125/125 machine waveform sanity does not establish correct CNS pronunciation, intelligibility, stress/rhythm, accent/style, or meaning preservation.

## 6. Prepared Stage-D continuation

The governed Stage-D continuation harness is:

`governance/application-planning/dwc-speech/dwc_stage_d_continue.py`

It starts from the exact Stage-C SHA above and deliberately does not re-enter LJSpeech warm-start or Stages A/B/C.

Default deterministic Stage-D curriculum:

- one shuffled complete pass over all **799** corpus rows;
- one extra shuffled pass over the **128** Stage-C repair rows;
- repair rows interleaved proportionally through the full-corpus pass rather than appended as a target-only tail;
- total **927 training batches / 1,854 optimizer steps**;
- seed `20260908`;
- checkpoints every 300 batches by default;
- 125-item deterministic machine acceptance rendered before and after Stage D.

Because the recovered Stage-C artifact stores model state rather than optimizer state, Stage D explicitly reinitializes generator/discriminator optimizers and records that fact in its evidence.

A self-contained Colab notebook is preserved in Google Drive `Transfer file`:

`DWC_Piper_Custom58_StageD_Continuation_v0.1.ipynb`

Drive file ID: `1zuU3BBs8SySNVroYsjY3Nf3SbE2bZUiY`  
Size: **28,123 bytes**  
SHA-256: **`1c871076abba8c0538553073cc645c2fc49e03fdb48736830b01a075f2854241`**

The notebook:

1. mounts Drive;
2. hard-gates on GPU availability;
3. reconstructs/verifies the Stage-C weights from the four Drive parts;
4. extracts the corpus/recovery/acceptance packages;
5. installs Piper v1.8.0;
6. materializes the Stage-D harness;
7. runs Stage D from Stage C;
8. writes persistent checkpoints/metrics/125-row pre/post renders to Drive;
9. preserves the human scorecard;
10. can export a selected custom model to ONNX;
11. writes output hashes.

## 7. Human CNS perceptual gate

Machine waveform sanity is not pronunciation certification.

`DWC_STAGE_C_PERCEPTUAL_GATE.md` governs the human auditory review. Existing acceptance assets include:

- `DWC_TTS_HUMAN_ACCEPTANCE_SCORECARD_TEMPLATE.tsv`;
- `score_human_acceptance.py`;
- `TTS_ENGINE_03_ACCEPTANCE_CONTRACT.md`;
- the 125-row acoustic acceptance suite.

Required thresholds include:

- intelligibility mean >= 4.0/5;
- pronunciation accuracy >= 4.2/5;
- special-phone accuracy >= 4.2/5;
- stress/rhythm >= 4.0/5 with full unstressed vowels preserved;
- Roman/Russian-accent target >= 4.0/5;
- style fidelity >= 3.8/5 where applicable;
- meaning preservation = 100%.

Special-phone coverage explicitly includes RH /ʁ/, TR /tʁ/, ZR /zɹ/, CH /tʃ/, ZH /ʒ/, SH /ɕ/, KH /x/, Nasal-M /mj/, Ň /ɲ/, and governed vowels/diphthongs.

## 8. Execution rules

### 8.1 `Continue` means execution

A DWC `Continue` remains active until the largest safe bounded unit is completed/verified or a genuine blocker is fully evidenced. A progress report is not a stop boundary.

### 8.2 Recover from latest evidence

Inspect the newest actual files/tool evidence before selecting work. Newer externally preserved evidence supersedes a stale narrative recovery summary.

### 8.3 Do not rediscover closed milestones

Do not rerun language design, exact-ID frontend discovery, proxy proof, warm-start proof, Stage A, Stage B, or Stage C merely because a new conversation or sandbox lacks their temporary local files.

### 8.4 Revalidation is not regression

A repeated test may verify reproducibility, but it does not move the logical project frontier backward unless the new evidence contradicts the prior milestone.

### 8.5 Distinguish project state from runtime material

Missing temporary files are a rehydration issue. They do not erase verified project progress.

### 8.6 Classify blockers precisely

Distinguish missing bytes, transfer limits, dependency failure, CPU limits, GPU unavailability, checkpoint incompatibility, dataset failure, perceptual failure, and actual architecture failure.

### 8.7 Preserve exact artifacts/provenance

Do not reconstruct checksum-bound model/corpus/training artifacts from prose. Preserve exact bytes and hashes.

## 9. What remains open

The following are genuinely open:

- human perceptual confirmation of Stage-C CNS pronunciation/quality;
- the longer Stage-D GPU adaptation from the verified Stage-C state;
- post-Stage-D machine + human acceptance evidence;
- selection/export of the temporary synthetic DWC candidate model;
- replacement of the temporary synthetic acoustic target with authentic human CNS recordings;
- production packaging/licensing/deployment/Multiversal-app integration;
- final production-engine selection if a later engine better preserves the exact-ID architecture.

## 10. Architectural non-regression boundaries

1. DWC language rules remain upstream of speech synthesis.
2. DWC pronunciation is not delegated to English G2P.
3. Exact custom phoneme identity survives into acoustic training/inference.
4. The frontend remains engine-independent where practical.
5. Proxy, warm-start, Stage A/B/C, Stage D, perceptual acceptance, and production-model success are distinct milestones.
6. Environment limits do not reopen settled language or training milestones without contrary evidence.
7. A conversation reset does not reset the project.
8. Revalidation does not reopen completed milestones.
9. Human auditory judgment remains required where the acceptance contract requires perception rather than waveform sanity.

## 11. Relation to Multiversal

DWC speech synthesis is a Multiversal capability/research program, but this anchor does not itself authorize a software-roadmap implementation tranche.

Potential downstream uses include spoken DWC dialogue, setting-language audio, pronunciation/reference tools, NPC speech, authoring previews, and content-production pipelines. Application integration should consume the governed DWC language/pronunciation artifacts rather than reimplementing them in client/UI code.

## 12. Recovery instruction

A future DWC conversation should begin with these facts already established:

- language/PSS/CNS reached pre-audio handoff;
- exact custom-ID frontend exists;
- 799-row exact-ID corpus exists;
- ONNX neural proxy succeeded;
- exact-ID Piper warm-start succeeded;
- real acoustic training completed through Stage A, Stage B, and Stage C;
- Stage-C machine acceptance is 125/125;
- Stage-C weights are hash-verified at `d800ae031942c29289ced1cc80c1448fff234c53f42a56f2d69265e7e3ebabb2`;
- Stage-D continuation and human perceptual gates are already prepared;
- the active frontier is Stage-D GPU continuation + human CNS evaluation + candidate export;
- always read `DWC_CURRENT_STATE.json` before executing because it contains the latest mutable state.

Do not resume from the beginning unless newer evidence proves one of these settled facts wrong.
