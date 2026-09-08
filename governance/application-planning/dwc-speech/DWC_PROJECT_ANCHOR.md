# DWC Speech Synthesis Project — Durable Project Anchor

**Project:** DWC language-to-speech / native speech synthesis  
**Owner and final authority:** John Brandon Turner  
**Status:** ACTIVE RESEARCH / IMPLEMENTATION  
**Created:** 2026-09-08  
**Updated:** 2026-09-08  
**Role:** durable human-readable project reference; DWC continuity authority, not Multiversal software-roadmap work selection

## 1. Why this document exists

The DWC project accumulated substantial language-design, pronunciation, corpus, neural-proxy, Piper warm-start, and training work inside long conversations. The technical work advanced, but conversation execution repeatedly regressed to older narrative checkpoints after interruptions, tool timeouts, progress messages, and sandbox changes.

This file exists to keep the DWC project centered outside any one conversation. Future DWC work should recover from this anchor plus `DWC_CURRENT_STATE.json`, then inspect live evidence for mutable runtime facts.

The key operating distinction is:

> **Project state is defined by verified artifacts, code, files, tool results, and explicit owner corrections. Assistant prose is commentary about that state, not the state itself.**

## 2. Project goal

Build a robust speech-generation path for DWC in which DWC's own language and phonological system controls pronunciation from end to end.

The target is not merely to make an English TTS engine approximate DWC. The target is a deterministic, engine-independent DWC pronunciation frontend that can drive neural speech synthesis directly and ultimately support a DWC-native/custom acoustic model.

Primary goals:

- DWC pronunciation is controlled by DWC rules rather than English G2P.
- The frontend preserves exact custom DWC phoneme identities/IDs.
- Equivalent DWC linguistic input produces deterministic phoneme output.
- The pronunciation layer remains portable across TTS engines where practical.
- Training and inference preserve provenance from DWC linguistic representation through phoneme IDs to acoustic output.
- Engine or environment limitations are not mistaken for language-design failures.
- The path can later support Multiversal without prematurely coupling DWC rules to one vendor or runtime.

## 3. Current conceptual architecture

`DWC language / semantic form`  
→ `DWC etymology and lexical rules`  
→ `PSS pronunciation representation`  
→ `CNS canonical sound representation`  
→ `engine-independent exact custom phoneme IDs`  
→ `aligned DWC training / regression corpus`  
→ `acoustic model / TTS engine`  
→ `vocoder / waveform output`

The critical invariant is that English G2P must not silently reinterpret DWC between the DWC frontend and the neural model.

## 4. Established project achievements

The following are settled project achievements unless later evidence contradicts them.

### 4.1 Language-side work reached the pre-audio TTS handoff

DWC language, etymology, PSS, and CNS work progressed to the point where speech synthesis could consume the language output. This is not an open language-design restart point.

### 4.2 Engine-independent exact-ID DWC frontend exists

A frontend exists that produces exact custom phoneme IDs for DWC rather than depending on an engine-specific English pronunciation path. Future speech work must preserve this capability unless the owner explicitly changes the architecture.

### 4.3 Synthetic exact-ID bootstrap corpus exists

A synthetic DWC bootstrap corpus of **799 exact-ID aligned utterances** exists and passed the prior Piper exact-ID dataset preflight.

### 4.4 Neural proxy path was proven

Using the owner-supplied LJSpeech medium ONNX model/config and ONNX Runtime, prior work produced a working neural DWC proxy path:

- **199/199** DWC regression utterances rendered;
- **0 unsupported CNS IPA symbols** in that set;
- approximately **4.6 minutes** of neural DWC audio generated;
- English G2P bypassed, with DWC/CNS pronunciation information sent directly to the neural path.

This proved that the DWC frontend can drive neural speech. It did not itself constitute the final DWC-native acoustic model.

### 4.5 Piper exact-custom-ID and warm-start support was established

Piper v1.8.0 source work established:

- `dataset_type=phoneme_ids` can consume owner-supplied IDs directly;
- `vocoder_warmstart_ckpt` is supported;
- unused English G2P/VAD paths can be bypassed/stubbed as needed for the custom-ID path.

### 4.6 Direct custom-ID warm-start viability was already proven

The prior DWC work progressed farther than the conversation-local recovery note captured. The owner explicitly corrected the stale frontier on 2026-09-08: the intended pretrained Piper/LJSpeech checkpoint **can warm-start the DWC direct exact-custom-ID path, and this had already been figured out in the preceding work**.

This is now a non-regression boundary.

A future repeat of the tiny warm-start smoke is permitted and useful, but it is a **reproducibility/revalidation gate**, not the first proof of feasibility and not a reason to move the project frontier backward.

### 4.7 Remaining compute limits are execution-surface issues unless evidence shows otherwise

CPU-heavy VITS construction/precompute and sustained training can exceed a conversation-container execution window. Such a limit must be classified at the training/execution layer. It does not reopen DWC phonology, CNS/PSS, exact-ID corpus design, neural-proxy viability, or custom-ID warm-start viability.

## 5. Current technical frontier

The current forward frontier is **controlled DWC-native acoustic training and evaluation**.

The next meaningful result is no longer "can the warm-start work?" It is:

> Can the proven exact-ID warm-start path be reproduced under governed conditions, then carried beyond smoke-test construction into a bounded real training run that produces durable training evidence and a DWC evaluation sample?

The key pretrained checkpoint remains `lj-med_1000.ckpt`, originally supplied inside `lj-med_1000.zip`. Because of connector size limits, the owner split the large ZIP; previous verified Drive state showed eight parts `.001` through `.008` in the `Transfer file` folder.

Missing copies in a new sandbox are a rehydration issue only. They do not reset logical progress.

## 6. Next governed execution chain

Unless newer DWC evidence supersedes this state:

1. Inspect the current execution surface and acquire only missing exact dependencies.
2. Reassemble/integrity-check `lj-med_1000.ckpt` as needed.
3. Repeat the tiny direct DWC exact-ID warm-start smoke as a **reproducibility gate**.
4. Preserve hashes, configuration, exact code path, dependencies, and outcome so the result is not lost inside a conversation again.
5. Advance immediately into a bounded acoustic-training run beyond the smoke test, long enough to show real optimizer/training progress and generate a new checkpoint or equivalent durable training artifact.
6. If the present CPU/container cannot sustain that run, classify **sustained acoustic training** specifically as `environment_unavailable`, preserve all completed milestones, and use/produce an exact GPU-ready harness.
7. Render a controlled DWC sample from the newly trained checkpoint.
8. Evaluate exact phoneme coverage, pronunciation fidelity, intelligibility, failure cases, and voice quality against DWC frontend expectations.
9. Update `DWC_CURRENT_STATE.json` with hashes, configuration, training evidence, evaluation findings, and the next bounded target before treating the work unit as closed.

## 7. Execution rules for DWC conversations

### 7.1 Continue means execution, not recap

When the owner says `Continue` during DWC execution, remain in execution mode until the largest safe bounded unit is completed/verified or a genuine blocker is fully evidenced. A progress update is not a handoff and is not permission to stop.

### 7.2 Recover from evidence, not the last paragraph

After interruption, inspect the latest actual tool/file/evidence state before selecting the next action. Do not restart from an older narrative checkpoint.

### 7.3 Work states are explicit

Use at minimum:

- `not_started`
- `in_progress`
- `verified_complete`
- `blocked_with_evidence`
- `environment_unavailable`

Started work is unfinished. Artifact existence alone is not completion.

### 7.4 Revalidation does not reopen a completed milestone

If a settled result is repeated to make it reproducible or to obtain fresher machine evidence, the project frontier stays advanced unless the rerun produces contradictory evidence. In particular, a repeat warm-start smoke must not be reframed as though DWC warm-start viability had never been established.

### 7.5 Do not rediscover closed facts without cause

Do not repeatedly re-prove:

- the DWC exact-ID frontend exists;
- the 799-row corpus exists and passed prior exact-ID preflight;
- the ONNX neural proxy worked;
- English G2P can be bypassed in the proven path;
- Piper accepts owner-supplied phoneme IDs;
- Piper supports the warm-start mechanism;
- the direct DWC custom-ID warm-start path is viable;

unless newer evidence conflicts with one of those facts.

### 7.6 New sandbox does not mean new project

Distinguish durable **logical project progress** from temporary **runtime material**. Rehydrate physical dependencies without resetting the technical frontier.

### 7.7 Classify blockers precisely

Distinguish file-transfer limits, dependency issues, CPU-duration limits, GPU unavailability, missing exact bytes, checkpoint corruption, model incompatibility, dataset failure, and genuine architecture failure.

### 7.8 Preserve exact artifacts and provenance

Do not reconstruct checksum-bound models, corpora, checkpoint parts, or training outputs from prose. Preserve or reacquire exact bytes and record hashes/configuration whenever a reproducibility gate is run.

## 8. Known artifact/source lineage

Important artifacts/evidence include:

- `DWC-Semantic-Lexicon-Redesign-v2-2026-09-07.zip`;
- DWC engine-independent exact-phoneme-ID frontend;
- 799-utterance exact-ID synthetic bootstrap corpus;
- 199-utterance DWC regression / neural-proxy package;
- owner-supplied LJSpeech medium ONNX model and config;
- Piper v1.8.0 source;
- `lj-med_1000.zip` / `lj-med_1000.ckpt`;
- split checkpoint parts `.001` through `.008` in Google Drive `Transfer file` as of the prior verified state;
- split/checksum manifest if present;
- `Multiversal app - Synth V Uses (1).mht` for transcript provenance;
- `DWC_CONVERSATION_EXECUTION_RECOVERY (1).md` as a historical recovery aid;
- `DWC_CURRENT_STATE.json` as the mutable durable frontier going forward.

Historical MHT/recovery material is provenance, not a reason to override newer durable state or explicit owner correction.

## 9. What remains open

Do not overstate completion. The following remain open:

- sustained DWC acoustic training to a useful convergence point;
- a durable newly trained DWC checkpoint produced from the exact-ID training path;
- a final DWC-native trained voice model;
- formal intelligibility/pronunciation/voice-quality evaluation beyond the proxy proof;
- production packaging, licensing review, deployment, and Multiversal-app integration;
- a final decision on Piper versus another engine, provided any alternative preserves the DWC exact-ID architecture.

Warm-start feasibility is **not** in this open list anymore.

## 10. Architectural non-regression boundaries

1. DWC language rules remain upstream of speech synthesis.
2. DWC pronunciation is not delegated to English G2P.
3. Exact custom phoneme identity survives into the acoustic-training/inference boundary.
4. The frontend remains engine-independent where practical.
5. Proxy success, warm-start success, bounded training success, and final-model success are separate milestones.
6. Environment limitations do not reopen settled language or warm-start design without contrary evidence.
7. A conversation reset does not reset the project.
8. Revalidation of a completed milestone does not move the logical frontier backward.

## 11. Relation to Multiversal

DWC speech synthesis is a Multiversal capability/research program, but this document does not itself authorize a software-roadmap implementation tranche.

Potential later uses include spoken DWC dialogue, setting-language audio, pronunciation/reference tools, NPC speech, authoring previews, and content-production pipelines. Application integration should consume the governed DWC language/pronunciation artifacts rather than reimplementing them in client/UI code.

## 12. Recovery instruction for a future conversation

Recover DWC with these facts already established:

- language/PSS/CNS reached the pre-audio handoff;
- an engine-independent exact custom-phoneme-ID frontend exists;
- the 799-row exact-ID bootstrap corpus exists and passed prior preflight;
- the ONNX neural proxy succeeded on 199/199 regression utterances with no unsupported CNS IPA symbols in that set;
- Piper source-level custom-ID and warm-start support is established;
- **direct DWC exact-custom-ID warm-start viability is already established**;
- a repeat warm-start is revalidation/reproducibility, not rediscovery;
- the active frontier is bounded DWC acoustic training, durable checkpoint/sample production, and pronunciation/intelligibility evaluation;
- CPU/GPU execution limitations must be classified at the training layer rather than used to reopen earlier milestones;
- read `DWC_CURRENT_STATE.json` before executing because it contains the latest mutable frontier.

Do not resume from the beginning unless newer evidence proves one of these settled facts wrong.
