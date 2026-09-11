# Recovery handoff

Branch: `recovery/dwc-perceptual-collapse-20260910`. Commit: the commit containing
this handoff and recovery-evidence-20260910. No global roadmap pointer changed.

Completed: owner failure recorded; current DWC state corrected; exact final
checkpoint and all 125 human-review WAVs verified; all 799 targets measured;
eight checkpoint conditions and 12 utterances audited; fixed-seed perturbations
and posterior-oracle experiment completed; legacy training entrypoints disabled;
new target/output/authorization gates and tests added. Ten verification checks
pass, including rejection of legacy entrypoints and rejection of final R2C by
the new output gate. Unit tests cover stale/missing/failed human receipts, budget
limits, missing tiny pass, poor retrieval and nonseparating calibration controls.

Read `DWC_RECOVERY_ROOT_CAUSE_REPORT_2026-09-10.md` and
`DWC_RECOVERY_VALIDATION_CONTRACT.md` before further work. Machine calibration is
provisional and cannot authorize training by itself. No tiny adaptation was run
because target human approval is missing. The no-training posterior/conditioning
experiment is complete. No recovered speech candidate or human PASS exists.

Single next action: owner listens to the 12 existing target references in
`C:\Users\Antiquaria\Downloads\DWC_TARGET_SMOKE_12_20260910\review.html`, and reports
whether they are distinguishable speech and which, if any, fail. This is reference
triage, not a new model approval. Persist that direct response against
`AUDIO_MANIFEST.json` SHA-256 in `TARGET_HUMAN_RECEIPT.json`; never infer PASS.

If rejected: obtain only a tiny replacement CNS recording set. If accepted:
resolve explicit target issues and independently calibrate the tiny panel; then
implement the bounded conditioning experiment in the recovery contract. The
remaining production calibration must use actual tiny outputs and independent
positive controls. Do not rerun R1/R2B/R2C or reuse the collapsed encoder.

Artifacts: `/home/antiquaria/multiversal/dwc-tts/runs/perceptual_recovery_20260910`.
Detailed JSON evidence is committed under `recovery-evidence-20260910`; WAVs and
models stay local, with hash manifests. Prior results remain intact. The bootstrap
launcher and local legacy harness also have blocking patches; exact patched-file
hashes are in `LOCAL_GUARD_PATCHES.json`.

Remaining uncertainties: target naturalness/native CNS correctness, exact early
optimizer update at which prior collapse began, independent natural-positive
threshold calibration, whether a new tiny conditioning experiment can overfit,
and final recovered human speech quality. These are not marked passed.
