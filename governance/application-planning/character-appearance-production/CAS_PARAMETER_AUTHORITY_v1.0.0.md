# Multiversal CAS Parameter Authority

**Document ID:** MV-CAS-PARAM-AUTH-001  
**Authority ID:** CAS-PARAM-1  
**Version:** 1.0.0  
**Status:** CANONICAL DESIGN AUTHORITY  
**Effective date:** 2026-10-03  
**Owner and final authority:** John Brandon Turner  
**Depends on:** CAS-SD1, CAPP-01, PPIA-05/PPIA-06, current MCCS contracts  
**Implementation authority:** none

## 1. Decision

CAS is the player-facing and character-facing appearance authoring profile over the generalized MCCS creator workspace. It is **not** a second engine beside MCCS.

The authority chain is:

```
Character / Species / Form / Equipment truth
                    ↓
           CAS parameter profile
                    ↓
              MCCS draft workspace
                    ↓
        CAPP validation + compilation
                    ↑
         PAPT governed asset vocabulary
                    ↓
             CAS-SD1 renderer
```

CAPP/PPIA remain renderer-neutral appearance authority. MCCS supplies topology-first authoring workspace/orchestration. PAPT/PCA supply reusable production primitives. CAS-PARAM-1 supplies the finite semantic vocabulary that the player edits.

## 2. Audit result

The existing CAPP registry already contains **25 Species profiles, 10 appearance choice surfaces, 74 required-feature contracts, 78 bounded-choice contracts and 28 explicit choice contracts**. Its authority boundaries and nonhumanoid handling are strong.

The missing layer is a concrete, reusable fine-grained CAS parameter vocabulary. MCCS also deliberately stays generic: MCCS-03 accepts arbitrary morphology/silhouette IDs; MCCS-05 accepts topology-aware head features/anchors; MCCS-06 accepts surface/material/pattern/marking references; MCCS-09 accepts wardrobe/equipment presentation compositions. That is the right substrate, but it does not itself define which face/body controls the product exposes.

CAS-PARAM-1 fills that gap without moving authority out of CAPP/PPIA.

## 3. Precision policy

Multiversal does **not** copy a 300+ continuous-slider 3D character creator.

Canonical scalar controls are semantic buckets:

- **ordinal7:** -3 through +3, for high-value proportion differences;
- **ordinal5:** -2 through +2, for smaller but still CAS-SD1-readable differences;
- **enum_ref:** a stable family/profile reference;
- **palette/layer/profile refs:** stable governed references.

Raw integers are storage semantics. The UI may label them with profile-specific language such as Narrow / Average / Wide.

If adjacent values cannot produce a meaningful difference in an authorized CAS-SD1 view, the values must be collapsed. False precision is forbidden.

## 4. Parameter registry

There are **61 core parameter paths**. A character normally exposes only the subset authorized by Species/Form/profile eligibility.

### Body & Proportions

| ID | Parameter | Type | CAPP | MCCS / adapter | Priority | Image/reference match |
|---|---|---|---|---|---:|---|
| CAS-BODY-001 | `body.stature` | ordinal7 | P06-UI-002 | MCCS-03:morphology | 2 | proportion_only |
| CAS-BODY-002 | `body.build_profile` | enum_ref | P06-UI-002 | MCCS-03:silhouette | 1 | family_classifier |
| CAS-BODY-003 | `body.shoulder_width` | ordinal7 | P06-UI-002 | MCCS-03:morphology | 2 | direct_ratio |
| CAS-BODY-004 | `body.torso_length` | ordinal7 | P06-UI-002 | MCCS-03:morphology | 2 | direct_ratio |
| CAS-BODY-005 | `body.torso_width` | ordinal7 | P06-UI-002 | MCCS-03:morphology | 2 | direct_ratio |
| CAS-BODY-006 | `body.waist_width` | ordinal5 | P06-UI-002 | MCCS-03:morphology | 2 | direct_ratio |
| CAS-BODY-007 | `body.hip_width` | ordinal5 | P06-UI-002 | MCCS-03:morphology | 2 | direct_ratio |
| CAS-BODY-008 | `body.arm_length` | ordinal5 | P06-UI-002 | MCCS-03:morphology | 2 | direct_ratio |
| CAS-BODY-009 | `body.leg_length` | ordinal5 | P06-UI-002 | MCCS-03:morphology | 2 | direct_ratio |
| CAS-BODY-010 | `body.head_scale` | ordinal5 | P06-UI-002 | MCCS-03:morphology | 2 | direct_ratio |
| CAS-BODY-011 | `body.posture_profile` | enum_ref | P06-UI-002 | MCCS-03:silhouette | 2 | family_classifier |

### Head / Face / Sensory Presentation

| ID | Parameter | Type | CAPP | MCCS / adapter | Priority | Image/reference match |
|---|---|---|---|---|---:|---|
| CAS-HEAD-001 | `head.shape_family` | enum_ref | P06-UI-003 | MCCS-05:feature_profile | 3 | family_classifier |
| CAS-HEAD-002 | `head.face_width` | ordinal7 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-HEAD-003 | `head.face_length` | ordinal7 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-HEAD-004 | `head.forehead_height` | ordinal5 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-HEAD-005 | `head.cheekbone_width` | ordinal5 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-HEAD-006 | `head.cheek_fullness` | ordinal5 | P06-UI-003 | MCCS-05:parameter_extension | 3 | family_classifier |
| CAS-HEAD-007 | `head.jaw_shape_family` | enum_ref | P06-UI-003 | MCCS-05:feature_profile | 3 | family_classifier |
| CAS-HEAD-008 | `head.jaw_width` | ordinal7 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-HEAD-009 | `head.chin_shape_family` | enum_ref | P06-UI-003 | MCCS-05:feature_profile | 3 | family_classifier |
| CAS-HEAD-010 | `head.chin_length` | ordinal5 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-EYE-001 | `eyes.family` | enum_ref | P06-UI-003 | MCCS-05:feature_profile | 3 | family_classifier |
| CAS-EYE-002 | `eyes.size` | ordinal7 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-EYE-003 | `eyes.spacing` | ordinal7 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-EYE-004 | `eyes.slant` | ordinal5 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_landmark |
| CAS-BROW-001 | `brows.family` | enum_ref | P06-UI-003 | MCCS-05:feature_profile | 3 | family_classifier |
| CAS-BROW-002 | `brows.thickness` | ordinal5 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-BROW-003 | `brows.height` | ordinal5 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_landmark |
| CAS-NOSE-001 | `nose.family` | enum_ref | P06-UI-003 | MCCS-05:feature_profile | 3 | family_classifier |
| CAS-NOSE-002 | `nose.length` | ordinal7 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-NOSE-003 | `nose.width` | ordinal7 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-NOSE-004 | `nose.bridge_profile` | ordinal5 | P06-UI-003 | MCCS-05:parameter_extension | 3 | family_classifier |
| CAS-NOSE-005 | `nose.projection` | ordinal5 | P06-UI-003 | MCCS-05:parameter_extension | 3 | family_classifier |
| CAS-MOUTH-001 | `mouth.family` | enum_ref | P06-UI-003 | MCCS-05:feature_profile | 3 | family_classifier |
| CAS-MOUTH-002 | `mouth.width` | ordinal7 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-MOUTH-003 | `mouth.fullness` | ordinal5 | P06-UI-003 | MCCS-05:parameter_extension | 3 | family_classifier |
| CAS-EAR-001 | `ears.family` | enum_ref | P06-UI-003 | MCCS-05:feature_profile | 3 | family_classifier |
| CAS-EAR-002 | `ears.size` | ordinal7 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_ratio |
| CAS-EAR-003 | `ears.angle` | ordinal5 | P06-UI-003 | MCCS-05:parameter_extension | 3 | direct_landmark |
| CAS-FHAIR-001 | `facial_hair.family` | enum_ref | P06-UI-003 | MCCS-05:feature_profile | 4 | family_classifier |
| CAS-FHAIR-002 | `facial_hair.length` | ordinal5 | P06-UI-003 | MCCS-05:parameter_extension | 4 | direct_ratio |

### Hair / Covering Style

| ID | Parameter | Type | CAPP | MCCS / adapter | Priority | Image/reference match |
|---|---|---|---|---|---:|---|
| CAS-COV-001 | `covering.style_family` | enum_ref | P06-UI-004 | MCCS-06:layer_ref | 4 | family_classifier |
| CAS-COV-002 | `covering.length` | ordinal7 | P06-UI-004 | CAPP:covering_parameter_to_MCCS06_ref | 4 | direct_ratio |
| CAS-COV-003 | `covering.volume` | ordinal5 | P06-UI-004 | CAPP:covering_parameter_to_MCCS06_ref | 4 | family_classifier |
| CAS-COV-004 | `covering.texture` | enum_ref | P06-UI-004 | MCCS-06:material_or_layer_ref | 4 | family_classifier |
| CAS-COV-005 | `covering.fringe_profile` | enum_ref | P06-UI-004 | MCCS-06:layer_ref | 4 | family_classifier |
| CAS-COV-006 | `covering.part_profile` | enum_ref | P06-UI-004 | MCCS-06:layer_ref | 4 | family_classifier |
| CAS-COV-007 | `covering.pattern_ref` | enum_ref | P06-UI-004 | MCCS-06:pattern_ref | 8 | pattern_classifier |

### Surface / Palette / Markings

| ID | Parameter | Type | CAPP | MCCS / adapter | Priority | Image/reference match |
|---|---|---|---|---|---:|---|
| CAS-SURF-001 | `surface.material_appearance_ref` | enum_ref | P06-UI-004 | MCCS-06:material_ref | 6 | material_classifier |
| CAS-SURF-002 | `surface.texture_ref` | enum_ref | P06-UI-004 | MCCS-06:material_ref | 6 | texture_classifier |
| CAS-SURF-003 | `surface.palette_zone_set` | palette_zone_set_ref | P06-UI-005 | MCCS-06:color_ref | 6 | palette_proposal |
| CAS-SURF-004 | `surface.pattern_ref` | enum_ref | P06-UI-005 | MCCS-06:pattern_ref | 8 | pattern_classifier |
| CAS-SURF-005 | `surface.marking_layers` | layer_set_ref | P06-UI-006 | MCCS-06:marking_ref | 8 | marking_segmenter |
| CAS-SURF-006 | `surface.cosmetic_dye_layers` | layer_set_ref | P06-UI-005 | MCCS-06:color_or_pattern_ref | 6 | palette_and_region_proposal |
| CAS-SURF-007 | `surface.scar_layers` | layer_set_ref | P06-UI-006 | MCCS-06:marking_ref | 8 | marking_segmenter |
| CAS-SURF-008 | `surface.tattoo_paint_makeup_layers` | layer_set_ref | P06-UI-006 | MCCS-06:marking_ref | 8 | marking_segmenter |

### Age Presentation

| ID | Parameter | Type | CAPP | MCCS / adapter | Priority | Image/reference match |
|---|---|---|---|---|---:|---|
| CAS-AGE-001 | `age.presentation_profile` | profile_ref | P06-UI-007 | CAPP:age_profile_ref | 3 | family_classifier |

### Pose & Expression Presentation

| ID | Parameter | Type | CAPP | MCCS / adapter | Priority | Image/reference match |
|---|---|---|---|---|---:|---|
| CAS-PRES-001 | `presentation.pose_ref` | profile_ref | P06-UI-011 | MCCS-11:pose | 9 | pose_classifier |
| CAS-PRES-002 | `presentation.expression_ref` | profile_ref | P06-UI-011 | MCCS-11:expression | 9 | expression_classifier |

### Presentation Wardrobe

| ID | Parameter | Type | CAPP | MCCS / adapter | Priority | Image/reference match |
|---|---|---|---|---|---:|---|
| CAS-WARD-001 | `wardrobe.presentation_outfit_ref` | profile_ref | P06-UI-009 | MCCS-09:item_composition | 5 | garment_classifier |

### Actual Equipment Projection

| ID | Parameter | Type | CAPP | MCCS / adapter | Priority | Image/reference match |
|---|---|---|---|---|---:|---|
| CAS-EQUIP-001 | `equipment.visual_projection_ref` | profile_ref | P06-UI-010 | MCCS-09:item_composition | 5 | not_inferred |

## 5. Generic topology-gated feature instances

CAS does not hard-code separate universal sliders for every horn, tail, beak, wing, antenna, fin, mandible or plant growth. Eligible structural features instantiate one reusable feature grammar.

Eligible feature kinds in v1:

- muzzle
- snout
- beak
- horn
- antler
- tusk
- mandible
- antenna
- crest
- sensory_appendage
- tail
- wing
- fin
- gill
- claw
- talon
- stinger
- abdomen
- whisker_set
- plant_growth
- modular_part

A feature instance may expose only the fields that are meaningful for that feature: family, size, length, width, curvature, angle, spread, orientation profile, palette zone, pattern and nonmechanical presentation pose.

Feature kind/cardinality remains Species/Form/PPIA truth or an explicitly authorized optional appearance choice. CAS cannot add anatomy merely because the feature editor knows how to draw it.

## 6. Visibility and CAS-SD1 rule

Each parameter carries a CAS-SD1 detail priority and target-view list. A parameter may remain valid semantic state even when a smaller renderer intentionally omits it.

Examples:

- build/head scale/eye family are strong identity signals and survive aggressively;
- cheek fullness, brow height and nose projection are primarily portrait controls;
- markings and fine covering patterns may disappear in smaller derivatives;
- microdetail that cannot survive CAS-SD1 is not a primary parameter at all.

This is how one semantic character remains recognizable at 128×160, portrait 96×96, token 64×64 and Retrobit derivatives without pretending every representation carries identical pixels.

## 7. Species/Profile eligibility

The registry is a **vocabulary, not a universal control sheet**.

CAPP-01 and PPIA-05/PPIA-06 determine eligibility. A Gray does not receive hair controls. A Vespin does not receive a two-arm body assumption. A Moravi retains two arms/four legs. A Suula retains nested hand/claw topology. A Rakuuta's swept-back structures remain ears, not horns. Required/source-owned anatomy is not cosmetically deleted.

Unavailable controls are omitted or explicitly disabled with reason; they are never replaced with a humanoid approximation.

## 8. CAS ↔ MCCS integration decision

The current MCCS contracts are reused rather than replaced:

- **MCCS-01:** CAS workspace/draft/version/recovery shell.
- **MCCS-03:** body proportions, silhouette, appendages and modular anatomy.
- **MCCS-05:** head/sensory feature structure and anchors.
- **MCCS-06:** coverings, palette, material appearance, patterns and markings.
- **MCCS-09:** wardrobe, accessories and actual-equipment visual projection.
- **MCCS-11:** pose/expression presentation.
- **MCCS-13:** portrait/token/sprite and other derivative planning.
- **MCCS-16:** style/templates/renderer profiles.
- **MCCS-18:** Form/lifecycle/temporary appearance state.
- **MCCS-19:** appearance interchange and round-trip mapping.

One real gap exists: MCCS-05 presently transports feature/anchor/count structures but not a generic scalar parameter map for face-shape controls. That needs a bounded adapter/extension during implementation; it does **not** justify a new CAS engine.

## 9. Reference-image matching

Image matching is an **input proposal adapter**.

```
reference image
    ↓
measure/classify visible features
    ↓
quantize to CAS-PARAM-1 values
    ↓
apply Species/Form/CAPP constraints
    ↓
ranked editable CAS draft + confidence
    ↓
user accepts/edits
    ↓
normal CAPP compilation
```

The matcher cannot change Species/topology truth, infer equipment ownership/mechanics, commit without review, or turn the source image into canonical appearance truth. Generative image synthesis is not required.

## 10. Known integration gaps

| Gap | Finding | Follow-on |
|---|---|---|
| CAS-GAP-001 | MCCS-05 lacks generic detailed face scalar transport. | Add bounded renderer-neutral feature-parameter transport/adapter. |
| CAS-GAP-002 | CAPP-05 compiles semantic choice IDs but not CAS-PARAM-1 paths/buckets explicitly. | Define deterministic parameter-state input and asset/variant/palette resolution. |
| CAS-GAP-003 | Historical CAPP canvases predate CAS-SD1 logical/native distinction. | Add CAS-SD1 density/profile metadata adapters without rewriting historical provenance. |
| CAS-GAP-004 | PAPT needs reusable assets for the finite parameter vocabulary. | Produce a parameter-driven asset demand/coverage ledger and golden packs. |
| CAS-GAP-005 | Wardrobe currently references outfits, not garment construction grammar. | Create the later Fashion/Garment Parameter Authority. |

## 11. Boundaries

This authority does not activate runtime code, mutate Species biology, change mechanics or equipment ownership, authorize a marketplace, or require generative AI.

The next implementation-design task is the **CAS → CAPP compiler handoff**, followed by the **PAPT parameter-driven asset demand ledger**.
