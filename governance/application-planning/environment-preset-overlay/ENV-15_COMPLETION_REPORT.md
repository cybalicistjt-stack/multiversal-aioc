# ENV-15 — Habitat Signature & Ecological Matching Contract — Completion Report

**Program:** ENV — Environment Preset & Overlay  
**Tranche:** ENV-15 — Habitat Signature & Ecological Matching Contract  
**State:** validation candidate; backlog advancement occurs only after exact-head repository-health success.

## Delivered contract

ENV-15 establishes `ENV-HS-1.0`, a stable environment-side Habitat Signature and categorical ecological matching seam for CEW.

The signature is a derived, read-only projection from the governed ENV composition stack and preserves provenance/contribution trace. It is not a fifth authored environment identity.

## Governed dimensions

The model defines eighteen environment-side comparison dimensions covering:

- habitat medium;
- water salinity, permanence and flow;
- temperature and moisture;
- vegetation density and substrate;
- elevation and depth;
- light, atmosphere, pressure and gravity;
- shelter and food/resource conditions;
- settlement intensity;
- special environmental contexts.

Unknown, not-applicable and unresolved-conflict states remain explicit instead of being collapsed into defaults.

## Ecological matching result

The comparison seam exposes five explainable states only:

- preferred;
- compatible;
- conditional;
- incompatible;
- indeterminate.

No universal numeric ecological-fit score is authorized. Hard incompatibility requires an explicit requirement conflict or exclusion. Material unknowns remain indeterminate rather than being guessed.

## Distribution boundary

Ecological suitability remains distinct from canonical distribution. Habitat fit does not establish native/common/present status, rarity/frequency, World/Reality/Place range, migration, season/activity, campaign visibility, or GM knowledge.

CEW owns creature-side ecology and creature distribution. Existing World/Reality/Setting/Place authorities remain external. ENV-16 must intersect those authorities before projecting creature discovery.

## Composition preservation

ENV-15 consumes the existing composition stack and ENV-04 overlay rules. Active overlays resolve before ecological comparison; effect-key deduplication, scope, explicit relations, input-order independence and visible unresolved conflicts remain intact. Local instances may refine the signature without mutating source presets/archetypes.

## Authority boundaries

ENV-15 creates no creature records, ability links, runtime schemas, encounter behavior, mount/pet/familiar/NPC state, or application authority. `Multiversal-app` runtime/UI/migrations and the active software roadmap remain untouched.

## Validation sequence

- Initial RED head `67f1ab24c66ef1a0ae4c85568b66ad31abe25e32` failed repository-health run **33772786988** because the ENV-15 model/contract/example/report artifacts were intentionally absent.
- Candidate GREEN must pass with ENV-15 still selected and ENV-16 still planned.
- Closed-state GREEN will then advance ENV-15 to `completed_verified` and ENV-16 to `selected_not_started` before merge.

## Artifacts

- `ENV-15_HABITAT_SIGNATURE_MODEL_v1.0.0.json`
- `ENV-15_ECOLOGICAL_MATCHING_CONTRACT.md`
- `ENV-15_SIGNATURE_EXAMPLES_v1.0.0.json`
- `ENV-15_COMPLETION_REPORT.md`
- `tests/control_plane/test_env15_habitat_signature_contract.py`
