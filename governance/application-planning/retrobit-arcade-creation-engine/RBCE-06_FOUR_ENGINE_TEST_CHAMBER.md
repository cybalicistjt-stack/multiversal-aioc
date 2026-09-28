# RBCE-06 — Four-Engine Test Chamber Golden Game

**Program:** Retrobit Arcade & Creation Engine (RBCE)  
**Work item:** RBCE-06  
**Status:** OWNER-DIRECTED DESIGN BASELINE  
**Operational authority:** none; this artifact does not select implementation and cannot override OPS3  
**Consumes:** RBCE-01 through RBCE-05, GPR, MRCS, MAI, owner-domain receipts and existing save/accessibility/provenance contracts

## 1. Purpose

RBCE-06 turns the existing **Four-Engine Test Chamber** from an expressiveness fixture into the canonical Retrobit golden-game conformance contract.

The name “Four-Engine” is historical product language for four distinct play styles inside one game. It does **not** authorize four gameplay runtimes. All four chambers must use the same governed GPR runtime and the same RBCE project model.

The four play styles are:

1. top-down traversal;
2. gated fixed-room interaction;
3. side-scroll platform/hazard recovery;
4. fixed-room dialogue and persistent state.

RBCE-06 is a design-time golden game plus proof plan. It does not claim that the application runtime already executes these vectors.

## 2. Source baseline

The source project remains `retrobit-project:four-engine-test-chamber` from `RBCE-01_FOUR_ENGINE_TEST_CHAMBER.fixture.json`.

RBCE-06 does not silently rewrite that source fixture. It binds a conformance overlay to the frozen source project and predecessor contracts. If a predecessor contract changes incompatibly, RBCE-06 requires explicit migration rather than reinterpretation.

## 3. Authority

- **GPR** remains runtime, deterministic state-transition and collision/trigger outcome authority.
- **MRCS** remains reusable governed definition authority.
- **MAI** remains asset/provenance/right-capability authority.
- **Canonical owner domains** remain authority for canonical mutations and receipts.
- **RBCE-01** remains project composition authority.
- **RBCE-02** remains 2D projection/movement/constraint-profile authority.
- **RBCE-03** remains Studio authoring interaction authority.
- **RBCE-04** remains Retro asset-workbench authority.
- **RBCE-05** remains Gameplay Parts projection/composition authority.
- **RBCE-07** will own product entry points and final `.pack` packaging.

RBCE-06 verifies seams. It creates no new gameplay authority.

## 4. Golden-game structure

The golden game has four required chambers:

### Traversal Plaza

- scene: `scene:plaza`
- projection: `projection:top-down-2d`
- movement: `movement:top-down-free`
- constraint: `constraint:retrobit-standard`
- proves movement, camera/spatial projection, scene transition and semantic-input normalization.

### Connected Gate Room

- scene: `scene:gate-room`
- projection: `projection:fixed-room-2d`
- movement: `movement:fixed-room-free`
- constraint: `constraint:retrobit-standard`
- proves gated interaction, persistent variable state and fail-closed prerequisite behavior.

### Platform Hazard Foundry

- scene: `scene:foundry`
- projection: `projection:side-scroll-2d`
- movement: `movement:platform-standard`
- constraint: `constraint:retrobit-standard`
- proves side-scroll movement, hazard/checkpoint semantics and recovery without display-frame authority.

### Dialogue Chamber

- scene: `scene:dialogue`
- projection: `projection:fixed-room-2d`
- movement: `movement:fixed-room-free`
- constraint: `constraint:retrobit-standard`
- proves social/investigation binding, persistent branch state, event state and owner-bound outcome proposal.

## 5. Required proof axes

The golden game must cover all of these axes:

- project-format;
- projection-runtime;
- studio-authoring;
- asset-workbench;
- gameplay-parts;
- deterministic-runtime;
- persistence;
- accessibility;
- provenance-rights;
- delivery-boundary;
- owner-authority;
- provider-independence.

No single passing screenshot or happy-path playthrough is sufficient.

## 6. Determinism and replay

The same normalized source project, seed, semantic command sequence and governed bindings must produce the same semantic assertions and deterministic fingerprint regardless of:

- render frame rate;
- visual interpolation;
- optional CRT/scanline/palette effects;
- search or Studio panel ordering;
- constraint profile when the project remains within that profile;
- keyboard versus accessibility input profile when both normalize to the same semantic commands.

Presentation differences are allowed. Semantic outcomes are not.

## 7. Persistence

The chamber proves persistence across:

- gate unlock state;
- checkpoint reference;
- dialogue branch;
- event-seen state.

Save/reload must preserve governed save-scope variables. Campaign-projection state remains a proposal until the canonical owner accepts it.

## 8. Retro constraint invariance

The standard, 8-bit-inspired and 16-bit-inspired constraint profiles may change allowed presentation limits, but cannot delete entities, skip rules, change variable values or alter canonical outcomes.

If a chosen profile cannot present the authored content within its limits, validation blocks that profile. It never silently changes gameplay to fit.

## 9. Studio round trip

RBCE-03 must be able to open the source project, inspect all four scenes, edit a non-semantic presentation field, run isolated playtest validation, undo the edit and serialize the project without semantic drift.

Studio playtest remains noncanonical and cannot commit campaign state.

## 10. Asset workbench round trip

RBCE-04 must prove a local-first workflow for an original/right-cleared Retrobit asset:

`intake → pixel/sprite/tile authoring → optional animation/palette work → permission-aware handoff → Studio consumption`

The workbench may not infer gameplay semantics from pixels. Persisted byte-changing transforms require transform permission. Transform permission never implies use or redistribution rights.

## 11. Gameplay Parts round trip

RBCE-05 must prove:

- direct governed binding insertion;
- deterministic recipe expansion;
- preview-before-insert;
- fail-closed unresolved binding;
- no runtime-ID minting;
- no canonical definition creation;
- no owner mutation.

The dialogue chamber uses governed social/investigation bindings. A collect-loop recipe is exercised only in a noncanonical authoring sandbox so the frozen RBCE-01 source project is not silently rewritten.

## 12. Accessibility equivalence

The critical path must be completable through the accessibility input profile with the same semantic command stream and assertions as keyboard play.

Required support includes:

- keyboard-complete authoring/play;
- nonvisual critical path;
- screen-reader summaries;
- non-color diagnostics;
- reduced-motion support;
- high-contrast support;
- scalable UI;
- no drag-only authoring requirement.

## 13. Rights and provenance

Production dependencies remain original or right-cleared. NES/SNES studies may remain research evidence only.

The golden game must fail publication-readiness if:

- a protected production dependency appears;
- redistribution capability is missing;
- a required asset loses provenance;
- an asset transform is performed without transform permission.

RBCE-06 does not package or publish the game. RBCE-07 owns that step.

## 14. Delivery boundary

The RBCE-01 source project explicitly supports:

- `direct-play`;
- `embedded-minigame`;
- `gm-led`.

RBCE-06 verifies those modes and verifies that undeclared modes fail closed rather than being inferred.

## 15. Owner boundary

A successful local game result never proves canonical campaign mutation.

`outcome:test-completion` may produce a typed owner proposal. Campaign state changes only after the owning domain returns an accepted receipt through the governed path.

## 16. Provider-off operation

Every required golden-game proof must be definable and executable without AI or paid cloud services.

Optional AI may explain diagnostics or propose authoring changes, but cannot create missing bindings, mark unresolved content ready, invent rights or alter proof results.

## 17. Negative proofs

RBCE-06 deliberately includes blocked vectors for:

- unresolved Gameplay Part binding;
- unsupported delivery mode;
- missing rights capability;
- attempted direct owner mutation;
- attempted gameplay-changing retro constraint behavior.

A golden game that only proves success paths is incomplete.

## 18. Evidence status

The RBCE-06 fixture records expected proof vectors, not fabricated execution evidence.

Until implementation is selected and exercised:

- implementation authority is false;
- runtime execution performed is false;
- canonical owner mutation performed is false;
- packaging performed is false;
- proof status is `design-baseline`.

Future implementation proof must attach exact application head, platform/build evidence, deterministic receipts and per-vector outcomes without changing the expected contract silently.

## 19. Acceptance

RBCE-06 design is complete when:

1. exactly four chambers are defined from the RBCE-01 source project;
2. all three RBCE-02 projection families are exercised;
3. the four play styles remain one GPR runtime;
4. Studio, Workbench and Gameplay Parts round trips are specified;
5. deterministic replay and save/reload are explicit;
6. accessibility semantic parity is explicit;
7. standard/8-bit/16-bit constraint invariance is explicit;
8. rights/provenance failures block readiness;
9. unsupported delivery and unresolved bindings fail closed;
10. owner proposals cannot become canonical mutations without receipts;
11. provider-off completion is required;
12. RBCE-07 packaging remains out of scope.

## 20. Machine identifiers and activation boundary

- schema ID: `RBCE06.FOUR_ENGINE_TEST_CHAMBER.v1`
- semantic version: `1.0.0`
- proof authority: `verification-only`
- runtime authority: `GPR`
- definition authority: `MRCS`
- asset authority: `MAI`
- source project: `retrobit-project:four-engine-test-chamber`

This is durable content/design only. Product implementation begins only when OPS3 explicitly selects and authorizes RBCE-06 or equivalent governed implementation work.
