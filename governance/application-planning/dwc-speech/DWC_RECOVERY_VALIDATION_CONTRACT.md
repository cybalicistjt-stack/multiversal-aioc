# DWC recovery validation contract

Effective 2026-09-10 after catastrophic owner perceptual rejection. This overrides
all earlier DWC waveform-only promotion and continuation instructions. The global
Multiversal roadmap is outside this contract.

## Current disposition

R2C remains a historical machine waveform PASS and is a rejected speech candidate.
No current checkpoint or corpus has the required human smoke PASS. Legacy R1,
R2, R2B and R2C training entrypoints are disabled. Diagnostic inference is allowed.
No recovered candidate has earned release or a candidate listening package.

## Gates and budgets

1. Target preflight: verify exact hashes, row identities, no silence/clipping,
   adequate duration, and canonical 58-ID labels. Measure acoustic diversity,
   inspect exact and near duplicates, and test deliberate phonemic contrasts.
   Repeated identical text is not automatically corruption; its sampling weight
   must be explicit. A punctuation-only mapping collision must not be described
   as a lost segmental contrast. Resolve all unexplained clusters before PASS.
2. Target human smoke: review 8-12 reference clips, including contrast pairs and
   ordinary words. Record explicit PERCEPTUAL_SMOKE_PASS or PERCEPTUAL_SMOKE_FAIL
   against the exact audio manifest hash. Synthetic references remain noncanonical.
   Numbers, embeddings, or a recognizer cannot grant this human result.
3. Tiny overfit: select 8-16 approved, unique target utterances; initial hard budget
   at most 200 optimizer updates and 300 seconds. Save input hashes, model hashes,
   complete optimizer/RNG state, elapsed time and intermediate outputs. Compare
   inference to its own targets, not only posterior reconstruction or loss.
   Every own target must rank first with positive margin; chosen contrasts must
   survive. Run fixed-seed identity perturbations and zero-noise/fixed-duration
   controls. Abort if conditioning/diversity deteriorates. A failed tiny attempt
   does not authorize another attempt or a full corpus pass automatically.
4. Calibration: `dwc_audio_gate.py` combines target retrieval, target margin and
   contrast preservation. Current thresholds separate exact reference controls
   from rejected R2C. This is a diagnostic calibration only. Before production
   authorization, use human-approved target controls with mild level/time/noise
   perturbations, a disjoint panel, rejected R2C, and actual tiny-overfit outputs.
   Require all metrics to separate; otherwise UNCALIBRATED_BLOCK. Publish
   calibration panels and hashes. Do not tune the
   threshold to make a candidate pass. Global spectral diversity alone is unsafe.
5. Output human smoke: release only the tiny candidate's 8-12 deliberately chosen
   clips if it earns machine review. Require explicit PERCEPTUAL_SMOKE_PASS on
   the exact files before any further tranche. The owner must judge recognizably
   human speech, different words, and intended contrasts.
6. Small tranche: only an explicit bounded authorization following all prior gates.
   Suggested first bound is 32 new rows, at most 200 updates/300 seconds. Repeat
   machine, conditioning, contrast, and tiny human smoke on persisted outputs.
7. Larger tranches: separate finite row/update/time budgets and exact source model
   identity in the owner authorization. Every tranche rechecks these gates. No
   indefinite retries, automatic full-corpus sweep, or waveform-only promotion.

`dwc_training_gate.py` checks receipts, identities, tiny requirements and bounded
requests. It cannot authenticate a human by itself: receipts are durable owner
records, never assistant-created approvals. A new trainer must call this gate
before allocating its model/optimizers and must enforce update/time bounds inside
its loop. Legacy launchers remain retired even if a receipt later exists.

## Smallest recovery experiment

Completed now: no-training causal perturbation and posterior-oracle comparison
at eight checkpoints. This localizes damage without another adaptation run.

Next, after reference review: use the original verified acoustic checkpoint, keep
the posterior encoder/flow/decoder fixed as a teacher, and fit only the exact-ID
conditioning path on the approved tiny set. Compare both posterior reconstruction
and text-only inference at steps 0/8/16/32/64/128/200. Never initialize from final
R2C or freeze its collapsed enc_p. A possible implementation can initialize
shape-compatible non-embedding text/duration weights from the existing source
checkpoint, while keeping the 58 DWC embeddings separate; this is an experiment,
not proven recovery. Exact source ID meanings must not be assumed interchangeable.

If target references are rejected, first replace only those 8-12 recordings with
owner CNS recordings; run target preflight and human smoke again. Do not regenerate
799 targets. If the bounded experiment still cannot reconstruct the tiny set,
reassess architecture or engine against that same panel before any migration.

## Result semantics

Machine waveform PASS, machine diversity PASS, tiny overfit PASS and human speech
PASS are separate fields. Only the owner can supply perceptual approval. None
alone establishes the DWC language or production voice complete.
