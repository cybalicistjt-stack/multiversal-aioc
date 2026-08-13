# CAPP-01 Foundation Report
## 25-Species Appearance Choice Registry + Constraint Model

**Work item:** CAPP-01  
**Status:** STARTED — FOUNDATION CANDIDATE  
**Base:** `ac830d90945424eccf3ef99ed85abc6883e430b9`  
**Owner:** John Brandon Turner

This foundation turns completed PPIA-05 Species/Form biology authority and PPIA-06 Character Appearance Creator authority into the first production-preparation data contract for appearance choices. It covers exactly 25 governed Species/Form profiles and 14 stable appearance categories. It deliberately does not invent aesthetic option lists where source material names a dimension or variability without enumerating legal values.

Authority order: PPIA-05 owns reusable Species/Form biology and source-truth boundaries; PPIA-06 owns the normalized 25-profile morphology set, appearance semantics, owner visual decisions, studio controls, coverage and renderer separation; PPIA-03 remains authority for actual Asset/equipment ownership and mechanics. Renderer availability is never source truth.

Stable categories are `scale.relative_size`, `body_shape.silhouette`, `symmetry.laterality`, `locomotion.appendages`, `texture.covering`, `coloration.marking`, `head_face.structure`, `hair_crest_spine`, `evolutionary_residue`, `age_bearing_posture`, `gender_manifestation`, `adornment`, `presentation_wardrobe`, and `equipment_state`.

Explicit special states preserve Munyubbles and Wogol as unresolved morphology rather than false/default-human anatomy; Thetans delegate physical appearance to the occupied/current body; Raconite native single-cell topology does not receive invented limb/head/hair controls; Crystal Dragon and Logical Stage phase changes are explicit; Malaphant environment/diet/allergen-dependent form is current-state dependency rather than rewritten Species truth; Regalian, Nekron and ManyToms preserve sourced gender/phase/grooming distinctions; Iaoth, Ganymede, Gliesian and Whimsbug preserve nonstandard appendage topology rather than collapsing to a two-arm humanoid template.

The constraint model implements topology, species, form, phase, dependency, exclusion, cardinality and permission classes. Unknown propagates as unknown; invalidated committed choices enter explicit review/diagnostic state; no silent substitution or blind retry is allowed; renderer unsupported/unknown/error cannot invalidate identity truth; source-unspecified values are not invented; appearance cannot imply equipment ownership/mechanics; downstream randomization may only use currently eligible source-supported pools.

This is the first substantive CAPP-01 foundation candidate, not CAPP-01 completion. No application runtime, STAGE-A-A2 activation, release, deployment, tester access, paid service, production credential, or unsupported canonical-content promotion is authorized.
