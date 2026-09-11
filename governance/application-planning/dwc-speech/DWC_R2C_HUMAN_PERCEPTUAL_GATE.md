# DWC R2C Human CNS Perceptual Gate

**Project:** DWC Speech Synthesis  
**Status:** REQUIRED HUMAN-AUDITORY GATE  
**Machine candidate:** `R2C_PROTECTED_weights_batch0799.pt`  
**Machine candidate SHA-256:** `c26ecb279ed5759a4c251ad54c80ebaa38e055194f6698681922b33e64269a3e`  
**Machine gate:** 125/125 on each of five deterministic seed schedules; 625/625 total

## Purpose

The repaired exact-ID Piper candidate has passed the strengthened machine waveform gate. Machine success does not establish that DWC/CNS is perceptually correct. Human review must use the exact 125 seed-1 WAV files persisted by the passing R2C final gate; do not rerender a substitute set for this acceptance decision.

## Required thresholds

The candidate passes only when all applicable thresholds are satisfied:

- intelligibility mean >= 4.0/5;
- pronunciation-accuracy mean >= 4.2/5;
- special-phone-accuracy mean >= 4.2/5 on special-phone rows;
- stress/rhythm mean >= 4.0/5 with full unstressed vowels preserved;
- Roman/Russian-accent target mean >= 4.0/5;
- style fidelity mean >= 3.8/5 where a style or stance target exists;
- meaning preservation = 100%.

## Mandatory special-phone focus

The review must pay explicit attention to governed difficult CNS phones/units including RH /ʁ/, TR /tʁ/, ZR /zɹ/, CH /tʃ/, ZH /ʒ/, SH /ɕ/, KH /x/, Nasal-M /mj/, Ň /ɲ/, governed vowel units/diphthongs, and full-vowel preservation.

## Reviewer workflow

1. Run `tools/run_prepare_r2c_human_evaluation.sh` after syncing governance.
2. Open the generated `review.html` from the Windows Downloads review folder.
3. Listen to all 125 exact final-gate WAVs and score every required field.
4. Export the completed TSV from the review page.
5. Optionally run `python score_human_acceptance.py <completed.tsv>`; the project chat can also score the completed TSV.
6. Preserve the completed scorecard, scorer JSON, reviewer identity/name as desired, machine checkpoint hash, acceptance WAV manifest/hashes, and review-package evidence.

## Non-regression rule

A human perceptual failure is evidence for model/data/training repair. It is not permission to alter canonical DWC phonology, PSS/CNS rules, exact custom phoneme IDs, or meaning merely to make the acoustic model easier to train unless independent linguistic evidence shows the language standard itself is wrong.

## Boundary

No further acoustic training is authorized by default after the passing R2C machine gate. Human review is the next governed stage. Machine PASS must never be reported as human CNS perceptual PASS.