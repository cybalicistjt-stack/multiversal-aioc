# DWC Speech Synthesis Project — Durable Project Anchor

**Project:** DWC language-to-speech / native speech synthesis
**Owner and final authority:** John Brandon Turner
**Status:** ACTIVE RESEARCH / IMPLEMENTATION
**Created:** 2026-09-08
**Role:** durable human-readable project reference; DWC continuity authority, not Multiversal software-roadmap work selection

## 1. Why this document exists

The DWC project accumulated substantial language-design, pronunciation, corpus, neural-proxy, and Piper-training work inside long conversations. The work advanced, but conversation execution repeatedly regressed to older narrative checkpoints after interruptions, tool timeouts, progress messages, and sandbox changes.

This file exists to keep the DWC project centered outside any one conversation. Future DWC work should recover from this anchor plus `DWC_CURRENT_STATE.json`, then inspect live evidence for mutable runtime facts.

The key operating distinction is:

> **Project state is defined by verified artifacts, code, files, and tool results. Assistant prose is commentary about that state, not the state itself.**

## 2. Project goal

Build a robust speech-generation path for DWC in which DWC's own language and phonological system controls pronunciation from end to end.

The target is not merely to make an English TTS engine approximate DWC. The target is a deterministic, engine-independent DWC pronunciation frontend that can drive neural speech synthesis directly and can ultimately support a DWC-native/custom acoustic model.

Primary goals:

- DWC pronunciation must be controlled by DWC rules rather than English G2P.
- The frontend must preserve exact custom DWC phoneme identities/IDs.
- Equivalent DWC linguistic input should produce deterministic phoneme output.
- The pronunciation layer should be portable across TTS engines where practical.
- Training and inference must preserve provenance from DWC text/language representation through phoneme IDs to acoustic output.
- Engine or environment limitations must not be mistaken for language-design failures.
- The path must be suitable for eventual Multiversal use without prematurely coupling language rules to one TTS vendor or runtime.

## 3. Current conceptual architecture

The working architecture is:

`DWC language / semantic form`
→ `DWC etymology and lexical rules`
→ `PSS pronunciation representation`
→ `CNS canonical sound representation`
→ `engine-independent exact custom phoneme IDs`
→ `aligned DWC training / regression corpus`
→ `acoustic model / TTS engine`
→ `vocoder / waveform output`

The critical invariant is that English G2P is not allowed to silently reinterpret DWC between the DWC frontend and the neural model.

## 4. Established project achievements

The following items are treated as established unless later artifact evidence contradicts them.

### 4.1 Language-side work reached the pre-audio TTS handoff

The DWC language, etymology, PSS, and CNS work progressed to the point where speech synthesis could consume the language output. This is not considered an open language-design restart point.

### 4.2 Engine-independent DWC frontend exists

A frontend exists that produces exact custom phoneme IDs for DWC rather than depending on an engine-specific English pronunciation path.

This is a major architectural achievement and a non-regression boundary: future TTS experimentation must preserve this ability unless the owner explicitly changes the design.

### 4.3 Synthetic exact-ID bootstrap corpus exists

A synthetic DWC bootstrap corpus of **799 exact-ID aligned utterances** exists. Previous Piper preflight work found that this corpus passes the exact-ID dataset checks.

### 4.4 Neural proxy path was proven

Using the owner-supplied LJSpeech medium ONNX model/config and ONNX Runtime, the prior conversation produced a working neural DWC proxy path.

Verified results recorded in the prior conversation:

- **199/199** DWC regression utterances rendered;
- **0 unsupported CNS IPA symbols** in that regression set;
- approximately **4.6 minutes** of neural DWC audio generated;
- English G2P was bypassed and CNS pronunciation information was sent directly to the neural path.

This proves that the DWC frontend can drive a neural speech system. It does **not** prove that the final native DWC acoustic model is trained.

### 4.5 Piper custom-ID feasibility was established at source level

Piper v1.8.0 source was inspected and prior work established that:

- `dataset_type=phoneme_ids` supports owner-supplied phoneme IDs directly;
- Piper's model path supports `vocoder_warmstart_ckpt`;
- work progressed into direct `VitsDataModule` / `VitsModel` custom-ID smoke attempts;
- unused English G2P/VAD dependencies were being bypassed or stubbed as needed.

### 4.6 Training limitation was narrowed to execution surface

CPU-heavy VITS construction/precompute exceeded the available conversation-container execution window.

This is currently classified as an execution-surface limitation, not evidence that DWC phonology, CNS/PSS, exact-ID corpus design, or Piper's custom-ID input path is invalid.

## 5. Current technical frontier

The next meaningful proof is a **direct Piper custom-ID warm-start smoke test** using the DWC exact-ID corpus and the pretrained LJSpeech checkpoint.

The checkpoint involved is `lj-med_1000.ckpt`, originally supplied inside `lj-med_1000.zip`.

Because the Drive connector had a per-file size limit, the owner split the large ZIP into eight parts under the connector limit. Previous verified Drive state showed parts `.001` through `.008` present in the `Transfer file` folder.

The final prior runtime had progressed beyond simple discovery. Its recovery record states that local runtime material included `.001-.004` while Drive exposed all eight parts. A new conversation/sandbox must not interpret missing local temporary files as project regression; it should rehydrate only what the new runtime actually lacks.

## 6. Exact next validation chain

Unless newer DWC evidence supersedes it, the unfinished sequence is:

1. Rehydrate only the checkpoint parts missing from the current runtime.
2. Reassemble all eight parts in numeric order.
3. Verify integrity:
   - validate the ZIP central directory;
   - use the split/checksum manifest if present;
   - verify extracted checkpoint size/hash when available.
4. Extract `lj-med_1000.ckpt`.
5. Inspect checkpoint keys, tensor shapes, and Piper-version compatibility.
6. Run a tiny direct custom-ID DWC warm-start smoke test using the exact-ID dataset path.
7. Bypass unused English G2P/VAD paths rather than reintroducing English pronunciation semantics.
8. If CPU model construction remains too heavy, classify the sustained acoustic-training surface specifically as `environment_unavailable`, preserve all earlier successful evidence, and produce/use a GPU-ready exact harness rather than backtracking.
9. Once warm-start viability is proven, move to controlled DWC-native acoustic training/evaluation rather than treating the ONNX proxy as the final architecture.

## 7. Execution rules for DWC conversations

These rules are part of the project continuity contract.

### 7.1 Continue means execution, not recap

When the owner says `Continue` during DWC execution, remain in execution mode until the largest safe bounded unit is completed/verified or a genuine blocker is fully evidenced.

A progress update is not a handoff and is not permission to stop.

### 7.2 Recover from evidence, not the last paragraph

After interruption, inspect the latest actual tool/file/scratchpad evidence before selecting the next action. Do not restart from an older narrative checkpoint merely because it is easier to remember.

### 7.3 Work states are explicit

Use, at minimum:

- `not_started`
- `in_progress`
- `verified_complete`
- `blocked_with_evidence`
- `environment_unavailable`

Started work is unfinished. Generated artifacts are not automatically completion evidence.

### 7.4 Do not rediscover closed facts without cause

Do not repeatedly re-prove:

- that the DWC exact-ID frontend exists;
- that the 799-row corpus exists/passed the prior exact-ID preflight;
- that the ONNX neural proxy worked;
- that English G2P can be bypassed in the proven proxy path;
- that Piper supports `dataset_type=phoneme_ids` and `vocoder_warmstart_ckpt`;

unless newer evidence conflicts with one of those facts.

### 7.5 New sandbox does not mean new project

Distinguish:

- **logical project progress** — durable and preserved;
- **ephemeral runtime material** — temporary files/packages that may need to be reacquired.

Rehydrate missing physical dependencies without resetting the technical frontier.

### 7.6 Classify blockers precisely

Do not collapse all failures into "the environment cannot do this." Distinguish file-transfer limits, dependency-install issues, CPU-duration limits, missing exact bytes, model incompatibility, dataset failure, and genuine architecture failure.

### 7.7 Preserve exact artifacts and provenance

Do not reconstruct checksum-bound model files, corpora, or checkpoint parts from prose. Exact external bytes must be reacquired from their real source when needed.

## 8. Known artifact/source lineage

The following artifacts or evidence were involved in the work and should be preserved or rediscovered by exact name/source when needed:

- `DWC-Semantic-Lexicon-Redesign-v2-2026-09-07.zip` — referenced in the preceding conversation as a language/semantic artifact.
- DWC engine-independent exact-phoneme-ID frontend.
- 799-utterance exact-ID synthetic bootstrap corpus.
- 199-utterance DWC regression corpus / neural proxy package.
- owner-supplied LJSpeech medium ONNX model and config.
- ONNX Runtime wheel used in the prior execution surface.
- Piper v1.8.0 source.
- `lj-med_1000.zip` / extracted `lj-med_1000.ckpt`.
- split checkpoint parts `.001` through `.008` in Google Drive `Transfer file` as of the last verified prior state.
- split/checksum manifest if present.
- `Multiversal app - Synth V Uses (1).mht` — conversation export containing direct transcript evidence.
- `DWC_CONVERSATION_EXECUTION_RECOVERY (1).md` — conversation-local recovery state created at the end of the prior conversation.

The MHT and recovery file are historical/provenance inputs. This repository anchor is the durable DWC recovery reference going forward; mutable execution facts belong in `DWC_CURRENT_STATE.json` and should be updated when verified state advances.

## 9. What has NOT yet been proven

Do not overstate current completion. At the time this anchor was created, the following were **not yet established as complete**:

- successful inspection/compatibility confirmation of the reassembled `lj-med_1000.ckpt` in the current Piper path;
- successful direct custom-ID Piper warm-start model construction on DWC data;
- sustained DWC acoustic training to convergence;
- a final DWC-native trained voice model;
- formal voice-quality / intelligibility / pronunciation evaluation beyond the neural-proxy proof;
- production packaging, licensing review, deployment, or Multiversal-app integration of the final TTS stack;
- a final decision that Piper must remain the production engine if another engine later proves better while preserving DWC exact-ID control.

## 10. Architectural non-regression boundaries

Future work should not silently undo these decisions:

1. DWC language rules remain upstream of speech synthesis.
2. DWC pronunciation must not be delegated to English G2P.
3. Exact custom phoneme identity must survive into the acoustic-training/inference boundary.
4. The frontend should remain engine-independent where practical.
5. Proxy success and native-model success are separate milestones.
6. Training environment limitations do not reopen settled language design without evidence.
7. A conversation reset does not reset the project.

## 11. Relation to the Multiversal application

DWC speech synthesis is a Multiversal capability/research program, but this document does not authorize a software-roadmap implementation tranche by itself.

Application integration should occur only when the owning Multiversal software roadmap selects it. When that happens, implementation should consume the DWC language/pronunciation artifacts as governed inputs rather than reproducing or simplifying them inside UI/client code.

Potential future Multiversal uses include spoken DWC dialogue, generated setting-language audio, pronunciation/reference tools, NPC speech, authoring previews, and content-production pipelines. Those are downstream applications, not proof requirements for the current acoustic-model research frontier.

## 12. Recovery instruction for a future conversation

A future DWC conversation should begin with this statement of state:

- the language/PSS/CNS work has reached the pre-audio handoff;
- an exact custom-phoneme-ID frontend exists;
- the 799-row exact-ID bootstrap corpus exists and passed prior preflight;
- the ONNX neural proxy proof succeeded on 199/199 regression utterances with no unsupported CNS IPA symbols in that set;
- Piper source-level custom-ID and warm-start support has been established;
- the unfinished frontier is checkpoint rehydration/integrity as needed, checkpoint compatibility inspection, and the direct custom-ID Piper warm-start smoke;
- CPU-heavy VITS work may require a GPU execution surface, but that does not invalidate prior DWC achievements;
- read `DWC_CURRENT_STATE.json` for the latest mutable state before doing anything.

Do not resume from the beginning unless newer evidence proves that one of these settled facts is wrong.
