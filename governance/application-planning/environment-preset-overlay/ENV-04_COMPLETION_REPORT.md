# ENV-04 Completion Report

**Program:** ENV — Environment Preset & Overlay  
**Tranche:** ENV-04 — Overlay Taxonomy & Stacking Rules  
**Status:** completion candidate pending exact-head repository-health validation

## Completed

ENV-04 establishes the reusable overlay classification and deterministic stacking contract required before converting the existing forty environments into modular presets.

Delivered authority:

- 12 broad overlay families covering weather, thermal, hydrology, atmosphere, light/visibility, gravity, pressure, contamination/radiation, geologic/disaster, ecological/landscape state, infrastructure/operational state, and supernatural/Multiversal influence;
- explicit separation between overlay family classification and precedence;
- optional five-band shared intensity vocabulary with bounded comparison rules;
- typed delta operations and per-effect stack modes;
- explicit relation types (`requires`, `excludes`, `supersedes`, `transforms_with`, `amplifies`, `dampens`);
- a deterministic nine-stage, input-order-independent stacking pipeline;
- stable `effect_key`-based duplicate suppression so multiple overlays cannot silently double-apply the same environmental effect;
- explicit visible conflict behavior instead of last-write-wins or hidden priorities;
- contribution-level provenance/audit trace requirements;
- explicit guidance keeping broad styles/states such as post-apocalyptic and cyberpunk from becoming accidental monolithic overlays;
- downstream ownership boundaries for ENV-05, ENV-11 through ENV-13, ENV-15, ENV-16 and CEW.

## Deferred by design

ENV-04 does not author the complete concrete overlay library. That remains split across:

- ENV-11 — weather, climate and disaster overlays;
- ENV-12 — planetary and physical-condition overlays;
- ENV-13 — magical, supernatural and Multiversal overlays.

ENV-04 also does not finalize Habitat Signature vocabulary, which remains ENV-15.

## Non-interference

No `Multiversal-app` runtime schema, SCL behavior, migrations, encounter runtime, creature distribution, mount/familiar/pet/NPC runtime behavior, or environment UI is modified or authorized by this tranche. Existing source profiles remain preserved.

## Validation target

The exact candidate head must pass:

1. canonical AIOC repository-health validation;
2. all current control-plane regressions;
3. ENV-04 overlay-model regressions;
4. progression-aware ENV-01 through ENV-03 historical regressions;
5. preservation of the independently governed active software pointer.

On successful merge, ENV-04 becomes `completed_verified` and ENV-05 — Existing 40 Preset Conversion — becomes `selected_not_started`.
