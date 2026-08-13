# CAPP-01 Canonical Source Correction

CAPP-01 derives its 25 appearance profiles directly from `PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json`.

An earlier foundation candidate used a legacy profile reconstruction that did not match the current canonical PPIA-06 profile set. Hosted validation run `31702343075` exposed that mismatch. The validator was not weakened to accept the legacy list. Instead, the substantive CAPP-01 source index, choice registry, constraint model and foundation report were replaced with deterministic outputs generated from the current PPIA-06/PPIA-05 authorities.

Canonical regeneration run `31703091730` succeeded, including embedded foundation validation. The corrected owner-authored foundation head `f460761d323af7c10f54ff85faec553163aa29e9` then passed dedicated foundation validation run `31703316324`, which reported 25 canonical profiles, 10 inherited Appearance Studio choice surfaces and 180 stable source-derived choice IDs.

A later bounded roadmap-index workflow committed from an earlier branch snapshot and removed this small provenance record while leaving the generated substantive registry intact. Completion run `31704068657` caught the missing record. This file restores the provenance evidence; no substantive appearance authority or registry content is changed by this repair.

This record is not a CAPP-01 completion claim and does not activate application runtime or STAGE-A-A2.
