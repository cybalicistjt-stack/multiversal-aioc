# RBCE-01 — Retrobit Game Project Format

**Work item:** RBCE-01  
**Program:** Retrobit Arcade & Creation Engine (RBCE)  
**Status:** OWNER-APPROVED STEP 1 — DESIGN SPECIFICATION STARTED  
**Spec version:** 0.1.0  
**Owner and final authority:** John Brandon Turner  
**Operational authority:** none; implementation requires OPS3 selection/authorization  
**Parent charter:** `RETROBIT_ARCADE_CREATION_ENGINE_CHARTER.md`

## 1. Purpose

Define one durable, versioned, portable Retrobit Game Project contract that can describe an original 2D game or campaign-embedded arcade experience without creating a second Multiversal rules, world, character, combat, inventory, rights, asset or persistence authority.

The project format is the seam between creator-facing Retrobit tooling and existing Multiversal systems.

A valid project answers:

- What is this game/project?
- Which GPR gameplay patterns and operations does it use?
- Which scenes/levels exist and how are they connected?
- Which actors/roles participate?
- Which MAI-governed visual assets are bound to semantic roles?
- Which inputs map to semantic commands?
- Which project-local variables may persist?
- Which owner-domain outcomes may be proposed back to Multiversal?
- Which audio/presentation resources are referenced?
- What rights/provenance evidence applies?
- Which tests prove the project is playable and portable?

## 2. Architectural rule

The Retrobit Game Project is a **composition document**, not a parallel engine.

Authority stays with existing systems:

| Concern | Authority consumed by Retrobit |
|---|---|
| reusable gameplay patterns / loop execution | GPR |
| reusable rule/content definitions | MRCS and owning domains |
| map/sprite/tile/image source + rights/provenance | MAI + ARI/PCA where applicable |
| Scene/region/trigger semantics | ISE / Scene / World owners |
| Character/NPC identity | Character/NPC owners |
| Combat / Action / Event mutation | owning runtime |
| inventory/economy/rewards | owning runtime |
| audio resource/cue semantics | AAI/MSAS as applicable |
| campaign state / permissions | campaign/session owners |
| skin/UI presentation | UI skin system |

A Retrobit project may reference, compose, preview and request owner operations. It may not silently manufacture canonical owner state.

## 3. Physical representation

### 3.1 Authoring representation

The normative source representation is UTF-8 JSON named:

`retrobit.project.json`

The schema identifier is:

`RBCE01.PROJECT.v1`

During authoring, referenced local assets may live beside the manifest in a project workspace.

### 3.2 Portable package representation

Portable distribution uses Multiversal's approved generic `.pack` extension.

A packaged Retrobit project contains at minimum:

- `retrobit.project.json`;
- package manifest/checksums required by the governing pack system;
- only redistributable embedded assets;
- references/entitlement metadata for assets that may not be redistributed;
- migration/version metadata.

RBCE does not introduce a second package extension.

### 3.3 Deterministic serialization

The canonical project fingerprint is computed from a normalized semantic representation, not source-file whitespace or object-key ordering.

Array ordering is semantic only where the field explicitly says order matters. ID-addressed collections normalize by stable ID before fingerprinting.

## 4. Project identity

Every project has:

```ts
interface RetrobitProjectIdentity {
  projectId: string;
  schemaId: "RBCE01.PROJECT.v1";
  projectVersion: string;
  title: string;
  slug: string;
  description?: string;
  authorRefs: readonly string[];
  createdAt: string;
  updatedAt: string;
}
```

### Requirements

- `projectId` is stable across rename, save-as-version and packaging.
- `projectVersion` uses semantic versioning.
- clone/fork operations create explicit lineage instead of silently reusing identity.
- title/description are presentation metadata and never gameplay authority.

## 5. Top-level project contract

```ts
interface RetrobitGameProject {
  identity: RetrobitProjectIdentity;
  lineage: RetrobitProjectLineage;
  compatibility: RetrobitCompatibilityContract;
  delivery: RetrobitDeliveryContract;
  gameplay: RetrobitGameplayComposition;
  scenes: readonly RetrobitSceneDefinition[];
  actors: readonly RetrobitActorDefinition[];
  assets: readonly RetrobitAssetBinding[];
  inputs: RetrobitInputContract;
  variables: readonly RetrobitVariableDefinition[];
  outcomes: readonly RetrobitOutcomeBinding[];
  audio: readonly RetrobitAudioBinding[];
  accessibility: RetrobitAccessibilityContract;
  provenance: RetrobitProjectProvenance;
  tests: readonly RetrobitProjectTestCase[];
  publishing: RetrobitPublishingContract;
}
```

Every required collection may be empty only where the validation profile permits it. A playable project must satisfy the playable gate in Section 18.

## 6. Lineage and versioning

```ts
interface RetrobitProjectLineage {
  originProjectId: string;
  parentProjectId?: string;
  parentProjectVersion?: string;
  forkReason?: string;
  migrationReceipts: readonly string[];
}
```

Rules:

- a normal new project has `originProjectId === projectId`;
- a fork receives a new `projectId` and preserves the prior project/version as parent;
- migration never rewrites historical source identity invisibly;
- unsupported future schemas fail closed with a visible `migration-required` result.

## 7. Compatibility contract

```ts
interface RetrobitCompatibilityContract {
  minRbceSchemaVersion: string;
  gprSchemaRefs: readonly string[];
  requiredDefinitionRefs: readonly string[];
  requiredCapabilityRefs: readonly string[];
  optionalCapabilityRefs: readonly string[];
}
```

The project does not assume every installed Multiversal environment has every capability. Required unresolved capability references block play. Optional unresolved references degrade explicitly and may use an authored fallback only when one is declared.

## 8. Delivery contract

Retrobit consumes the existing GPR delivery vocabulary:

- `direct-play`
- `cozy-low-pressure`
- `gm-led`
- `world-map-ttrpg-bridge`
- `embedded-minigame`
- `user-authored-loop-mini`
- `roster-injection`

```ts
interface RetrobitDeliveryContract {
  supportedModes: readonly GprDeliveryMode[];
  defaultMode: GprDeliveryMode;
  campaignEmbeddingAllowed: boolean;
  standalonePlayAllowed: boolean;
  rosterInjectionAllowed: boolean;
}
```

Unsupported modes fail closed. A different delivery mode must not fork the semantic mechanics of the project.

## 9. Gameplay composition

```ts
interface RetrobitGameplayComposition {
  primaryLoopMiniRef: string;
  secondaryLoopMiniRefs: readonly string[];
  patternRuntimeRefs: readonly string[];
  operationRuntimeRefs: readonly string[];
  resourceRuntimeRefs: readonly string[];
  ruleDefinitionRefs: readonly string[];
  objectiveDefinitionRefs: readonly string[];
  rewardDefinitionRefs: readonly string[];
  difficultyRef?: string;
}
```

The format may embed an RBCE-owned normalized projection of the corresponding GPR-08 configuration for portability, but the GPR stable IDs and versions remain the authority for runtime semantics.

No `customScript`, arbitrary JavaScript, Lua, Python or unrestricted expression field exists in RBCE-01.

Bounded formulas/predicates must reference governed MRCS expression/rule definitions.

## 10. Scene / level definitions

A project contains one or more scenes/levels. The format calls them `scenes` to align with Multiversal Scene ownership while allowing arcade-friendly labels such as level, room, screen, arena or course.

```ts
interface RetrobitSceneDefinition {
  sceneId: string;
  label: string;
  sceneOwnerRef?: string;
  mapRef?: string;
  projectionProfileRef: string;
  boundsRef?: string;
  entryPoints: readonly RetrobitEntryPoint[];
  exits: readonly RetrobitSceneExit[];
  placements: readonly RetrobitPlacement[];
  triggerRefs: readonly string[];
  localVariableRefs: readonly string[];
  presentationProfileRef?: string;
}
```

### 10.1 Projection profiles

RBCE-01 stores `projectionProfileRef`; RBCE-02 owns the detailed 2D runtime semantics.

The first implementation must be able to represent at least:

- top-down 2D scene projection;
- side-scrolling/platform 2D scene projection;
- fixed-screen/connected-room 2D projection.

A project may mix profiles across scenes. The Four-Engine Test Chamber depends on this.

### 10.2 Entries and exits

```ts
interface RetrobitEntryPoint {
  entryId: string;
  locationRef: string;
  facingHint?: string;
}

interface RetrobitSceneExit {
  exitId: string;
  triggerRef: string;
  destinationSceneId: string;
  destinationEntryId: string;
  prerequisiteRuleRefs: readonly string[];
}
```

Scene transitions are explicit graph edges. An exit may be gated by accepted rules/conditions/items/abilities. Missing destination identities block validation.

## 11. Actor definitions and placements

The project distinguishes reusable actor definition from placed actor instance.

```ts
interface RetrobitActorDefinition {
  actorDefinitionId: string;
  roleRuntimeRef: string;
  canonicalEntityRef?: string;
  definitionRefs: readonly string[];
  defaultAssetRoleRef?: string;
  controllerPolicy: "player" | "gm" | "runtime-bounded" | "external-owner";
}

interface RetrobitPlacement {
  placementId: string;
  actorDefinitionId?: string;
  semanticObjectRef?: string;
  locationRef: string;
  assetRoleRef?: string;
  initialStateRef?: string;
  visibilityRef?: string;
}
```

A player character injected from Multiversal keeps its canonical character identity. Retrobit may project that entity into an actor role but does not clone its authoritative Character state.

## 12. Asset bindings

```ts
interface RetrobitAssetBinding {
  assetRoleId: string;
  semanticRole: string;
  maiAssetRef: string;
  sourceClass: string;
  presentationProfileRef?: string;
  requiredForPlay: boolean;
  fallbackRoleRef?: string;
}
```

Examples of semantic roles include player visual, enemy visual, door visual, pickup visual, tileset, background, foreground, effect, UI motif and portrait.

RBCE does not infer usage rights from file possession. MAI/ARI/PCA provenance and capability evidence remain authoritative.

Missing optional art must not block semantic play when an accessible fallback exists. Missing required semantic definitions may block play even if attractive art exists.

## 13. Input contract

Raw devices map to semantic GPR commands.

```ts
interface RetrobitInputContract {
  commandSetRef: string;
  profiles: readonly RetrobitInputProfile[];
}

interface RetrobitInputProfile {
  profileId: string;
  deviceClass: "keyboard" | "gamepad" | "touch" | "pointer" | "accessibility" | "custom-supported";
  bindings: readonly RetrobitInputBinding[];
}

interface RetrobitInputBinding {
  physicalInputRef: string;
  semanticCommandRef: string;
  contextRuleRefs: readonly string[];
}
```

Project logic may not branch on vendor-specific key/gamepad codes once semantic command normalization occurs.

A playable project must expose an accessible nonvisual or keyboard-equivalent route for consequential required actions where the host platform supports those accessibility paths.

## 14. Project variables and persistence

RBCE-01 provides a bounded project-local variable registry for game-specific state such as a switch, checkpoint, conversation branch, score flag or visited-room marker.

```ts
interface RetrobitVariableDefinition {
  variableId: string;
  valueType: "boolean" | "integer" | "number" | "string" | "enum" | "stable-ref";
  defaultValue: unknown;
  enumValues?: readonly string[];
  scope: "scene" | "run" | "save" | "campaign-projection";
  writePolicy: "gpr-transition" | "owner-receipt" | "gm-adjudication";
  visibilityRef?: string;
}
```

### Rules

- `scene` resets on scene re-entry according to the declared scene lifecycle.
- `run` lasts for one gameplay run/session.
- `save` persists through Retrobit save/snapshot semantics.
- `campaign-projection` is not direct campaign mutation. It is a proposed/projected value requiring a matching owner operation/receipt.
- hidden/GM-only variables are permission-filtered before client projection, diagnostics, export and AI context.
- arbitrary nested object blobs are not allowed in v1; use stable references and governed definitions instead.

This variable system is intentionally small so Retrobit does not become a second general-purpose database.

## 15. Outcomes and campaign return values

Embedded games can return typed proposals to canonical Multiversal owners.

```ts
interface RetrobitOutcomeBinding {
  outcomeId: string;
  triggerRuleRef: string;
  ownerDomain: string;
  operationRuntimeRef: string;
  parameterBindings: readonly RetrobitParameterBinding[];
  deliveryModes: readonly GprDeliveryMode[];
}
```

Potential outcomes include governed reward proposals, item/economy changes, injuries/conditions, discoveries, relationship changes, objective progress, scene transitions and score/result records.

The Retrobit project records the calculated/requested outcome separately from any accepted owner mutation. Campaign embedding must preserve GM approval/adjudication where the owning workflow requires it.

## 16. Audio bindings

```ts
interface RetrobitAudioBinding {
  audioRoleId: string;
  semanticIntentRef: string;
  audioAssetRef?: string;
  triggerRuleRefs: readonly string[];
  requiredForPlay: boolean;
}
```

Audio may be absent or disabled without changing authoritative gameplay results unless a specific accessible game mechanic explicitly uses governed audio semantics and provides the required equivalent path.

## 17. Accessibility contract

```ts
interface RetrobitAccessibilityContract {
  keyboardComplete: boolean;
  nonvisualCriticalPathRef?: string;
  screenReaderSummaryProfileRef?: string;
  reducedMotionSupported: boolean;
  highContrastSupported: boolean;
  scalableUiSupported: boolean;
}
```

A Retrobit project must not encode a required semantic state solely as color, animation, sound or pixel position when a nonvisual/equivalent path is required by the host accessibility contract.

## 18. Validation and lifecycle gates

Project lifecycle states:

1. `draft`
2. `structurally-valid`
3. `playable`
4. `publishable`
5. `migration-required`
6. `blocked`

### 18.1 Structurally valid

Requires:

- valid project identity/version;
- unique stable IDs;
- resolvable internal references;
- recognized schema;
- valid delivery declarations;
- bounded collection sizes according to implementation limits;
- no malformed variable/type/default combinations.

### 18.2 Playable

Additionally requires:

- at least one scene and valid entry point;
- ready required GPR pattern/operation bindings;
- valid scene transition graph for declared required routes;
- required actor/semantic definitions available;
- required input semantic commands available;
- required visual/audio semantics either resolved or explicitly fallback-safe;
- no required unresolved rights/capability dependency;
- all blocking project tests pass.

### 18.3 Publishable

Additionally requires:

- provenance/rights capability permits intended distribution;
- package dependency manifest complete;
- no protected-reference production dependency;
- no local absolute file paths;
- deterministic fingerprint produced;
- migration baseline recorded;
- publication-target policy satisfied.

A project may be playable locally but not publishable.

## 19. Provenance and rights

```ts
interface RetrobitProjectProvenance {
  projectSourceRefs: readonly string[];
  researchEvidenceRefs: readonly string[];
  assetEvidenceRefs: readonly string[];
  licenseCapabilityRefs: readonly string[];
  protectedReferenceDependencies: readonly string[];
}
```

For publishable production projects, `protectedReferenceDependencies` must be empty.

Historical NES/SNES study material may appear only in `researchEvidenceRefs` or equivalent non-production provenance. It may not be required at runtime or packaged as production content unless the specific material has independent lawful rights evidence.

## 20. Project tests

Tests are first-class project data rather than external prose.

```ts
interface RetrobitProjectTestCase {
  testId: string;
  label: string;
  seed?: string;
  startingSceneId: string;
  startingEntryId: string;
  setupVariableValues: readonly RetrobitVariableValue[];
  commandSequence: readonly RetrobitTestCommand[];
  expectedAssertions: readonly RetrobitTestAssertion[];
  blocking: boolean;
}
```

Initial assertion families must cover:

- scene reached;
- entry/exit transition accepted or rejected;
- collision/trigger result;
- variable value;
- objective/result state;
- owner operation proposed/not-proposed;
- deterministic replay fingerprint;
- hidden information not projected.

RBCE-01 tests operate at semantic command/state level. Pixel rendering assertions belong to RBCE-02+ visual tests.

## 21. Publishing contract

```ts
interface RetrobitPublishingContract {
  visibility: "private" | "campaign" | "shared" | "public-candidate";
  redistributableAssetRefs: readonly string[];
  referenceOnlyAssetRefs: readonly string[];
  dependencyPackRefs: readonly string[];
  exportPolicyRef: string;
}
```

The packager must exclude reference-only assets from redistribution and preserve enough metadata for the consumer to resolve legitimate local/provider assets when allowed.

## 22. Normalized fingerprint

The normalized project fingerprint must include all semantic fields that affect play or compatibility, including:

- project/schema version;
- GPR/MRCS/owner definition references;
- scenes/transitions/placements;
- input semantic mappings;
- variables/scopes/write policies;
- outcomes;
- required asset/audio role bindings and capability references;
- test definitions;
- compatibility requirements.

Pure authoring UI state such as editor panel positions, zoom level and temporary selection must not affect the semantic fingerprint.

## 23. Save / snapshot distinction

Three things remain distinct:

1. **Project source** — authored game definition.
2. **Gameplay snapshot/save** — runtime state for a run/save slot.
3. **Canonical owner state** — campaign/character/world/etc. state controlled outside Retrobit.

Loading a project never silently applies a gameplay save. Loading a gameplay save never silently commits campaign outcomes. Owner mutations require owner receipts/accepted events.

## 24. Four-Engine Test Chamber requirements inherited by RBCE-01

RBCE-01 must be expressive enough to describe a future original/right-cleared golden project containing:

### Engine A — top-down exploration
- top-down projection scene;
- player movement semantic commands;
- collision boundaries;
- scene exit/entry transition.

### Engine B — connected-room gating
- multiple connected scenes/rooms;
- locked/gated route;
- prerequisite tied to governed item/ability/variable state;
- rejection before prerequisite and acceptance after it.

### Engine C — platform/hazard/dependency
- side-scroll projection scene;
- jump/move semantic commands;
- hazard trigger;
- checkpoint or dependency state;
- deterministic failure/recovery path.

### Engine D — dialogue/persistent event state
- NPC actor/placement;
- interaction semantic command;
- branching choice represented through governed rules/operations;
- persistent save-scoped variable;
- later scene/dialogue result changes from the stored state.

The detailed 2D physics/render implementation is RBCE-02. The project format must not need a schema migration merely to represent this golden game.

## 25. Failure taxonomy

At minimum validators distinguish:

- invalid-project-identity;
- unsupported-schema-version;
- migration-required;
- duplicate-stable-id;
- broken-internal-reference;
- unresolved-required-capability;
- unresolved-gpr-binding;
- unresolved-owner-definition;
- unsupported-delivery-mode;
- invalid-scene-transition;
- invalid-projection-profile;
- invalid-input-binding;
- invalid-variable-definition;
- unauthorized-variable-write-policy;
- invalid-outcome-owner-binding;
- unresolved-required-asset-role;
- rights-capability-unresolved;
- protected-production-reference;
- blocking-test-failed;
- deterministic-fingerprint-mismatch;
- package-dependency-unresolved.

No failure may be repaired by silently inventing a gameplay definition or rights grant.

## 26. Initial authoring limits

Implementation must define explicit caps rather than accept unbounded project graphs. Exact numeric caps are an implementation/performance decision to be proved under RBCE-01 acceptance and may vary by profile/platform, but the format requires that the active caps be discoverable and validated before play.

The first implementation must cap at least:

- scenes;
- placements per scene;
- total actors;
- transitions;
- project variables;
- input bindings;
- outcome bindings;
- asset/audio bindings;
- project tests;
- test command length.

## 27. Migration policy

Schema evolution follows explicit migrations:

- readers may accept compatible older versions through registered migrations;
- writers emit the current selected schema version;
- migrations produce receipts containing source schema, target schema and before/after fingerprints;
- unknown newer schemas fail closed;
- removed/deprecated references remain visible until resolved;
- migration cannot silently convert protected/reference-only assets into redistributable assets.

## 28. Step-1 acceptance criteria

RBCE-01 design is ready for implementation planning when the following are true:

1. the top-level project contract and authority boundaries are accepted;
2. the `.pack` packaging rule is accepted;
3. scene/actor/asset/input/variable/outcome/audio/test sections cover the Four-Engine Test Chamber without schema escape hatches;
4. GPR seven-mode compatibility is preserved;
5. no arbitrary scripting dependency exists in v1;
6. local playable versus publishable rights states are distinguishable;
7. project source, gameplay save and canonical owner state remain distinct;
8. deterministic semantic fingerprint and explicit migration are required;
9. accessibility-equivalent consequential interaction is represented;
10. an implementation plan names exact repository contracts/tests to add without starting RBCE-02 prematurely.

## 29. Deferred to later RBCE steps

RBCE-01 intentionally does not define:

- tile/sprite renderer internals;
- physics formulas;
- animation scheduler implementation;
- pixel scaling algorithm;
- creator UI layout;
- sprite slicing UX;
- gameplay-parts catalog copy;
- Four-Engine production content/art;
- public marketplace/distribution infrastructure.

Those belong to RBCE-02 through RBCE-07.

## 30. Current design conclusion

The Retrobit Game Project should be a thin, explicit composition format over existing Multiversal authorities. Its key job is to make a small game **portable, inspectable, testable and editable** while preventing the creator layer from becoming a second rules engine or a rights/provenance bypass.

The next RBCE-01 action is implementation planning against the live GPR/MRCS/MAI/ISE contracts.
