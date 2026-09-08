# DWC Stage-C Perceptual CNS Gate

**Project:** DWC Speech Synthesis  
**Status:** REQUIRED HUMAN-AUDITORY GATE  
**Machine baseline:** Stage-C acceptance 125/125 waveform-sanity PASS  
**Stage-C weights:** `d800ae031942c29289ced1cc80c1448fff234c53f42a56f2d69265e7e3ebabb2`

## Purpose

Stage C has passed the machine waveform gate, but machine waveform sanity is not a substitute for hearing whether DWC/CNS is actually being pronounced correctly. This gate is perceptual and must be completed by a human reviewer using the 125-item acoustic acceptance suite.

The canonical scorecard/template and scorer already exist in `DWC_TTS_ENGINE_03_Acoustic_Spike_Harness_v0.1.0.zip`:

- `DWC_TTS_HUMAN_ACCEPTANCE_SCORECARD_TEMPLATE.tsv`
- `score_human_acceptance.py`
- `TTS_ENGINE_03_ACCEPTANCE_CONTRACT.md`

The Stage-D continuation harness renders deterministic pre-Stage-D and post-Stage-D versions of all 125 acceptance utterances so the reviewer can compare Stage C against Stage D without changing the DWC frontend.

## Required thresholds

The candidate passes only when all of these are true:

- intelligibility mean >= 4.0/5;
- pronunciation-accuracy mean >= 4.2/5;
- special-phone-accuracy mean >= 4.2/5;
- stress/rhythm mean >= 4.0/5 with full unstressed vowels preserved;
- Roman/Russian-accent target mean >= 4.0/5;
- style fidelity mean >= 3.8/5 where a style target exists;
- meaning preservation = 100%.

## Mandatory special-phone focus

The acceptance suite explicitly covers the governed difficult CNS phones/units, including:

- RH /ʁ/;
- TR /tʁ/;
- ZR /zɹ/;
- CH /tʃ/;
- ZH /ʒ/;
- SH /ɕ/;
- KH /x/;
- Nasal-M /mj/;
- Ň /ɲ/;
- governed vowel units/diphthongs and full-vowel preservation.

## Stage-B to Stage-C repair evidence

Stage B had exactly two machine-review rows:

- `CONTRAST-a_-01` — `ai`, IPA `[aɪ]`;
- `CONTRAST-_-05` — `sher`, IPA `[ɕɛr]`.

Stage C targeted 128 rows: 75 special-phone contrast rows plus 53 lexical phone-coverage rows. After Stage C, the machine acceptance suite reported 125/125 PASS. These two repaired cases should receive explicit perceptual attention, but machine PASS must not be interpreted as proof that they sound correct.

## Reviewer workflow

1. Use the deterministic 125 WAV files rendered from the verified Stage-C weights (the Stage-D harness writes them under `pre_stage_d_stage_c_acceptance/`).
2. Score every row in `DWC_TTS_HUMAN_ACCEPTANCE_SCORECARD_TEMPLATE.tsv`.
3. Record artifact notes for any phone, vowel, stress, rhythm, accent, style, or meaning defect.
4. Run `score_human_acceptance.py --scorecard <completed.tsv>`.
5. Preserve the completed scorecard, scorer JSON/output, reviewer name, Stage-C weight hash, render settings, and acceptance WAV hashes as durable evidence.
6. Repeat on the selected post-Stage-D candidate before promotion/export is treated as accepted.

## Non-regression rule

A perceptual failure is diagnostic evidence for data/model/training repair. It is **not** permission to alter DWC phonology, PSS/CNS rules, or exact phoneme IDs merely to make the model easier to train unless independent linguistic evidence shows the language standard itself is wrong.
