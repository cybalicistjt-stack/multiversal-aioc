# RBCE-01 Machine Contract Baseline

**Program:** Retrobit Arcade & Creation Engine (RBCE)  
**Work item:** RBCE-01  
**Status:** OWNER-APPROVED DESIGN CONTRACT — MACHINE BASELINE  
**Authority:** design/content only; does not select or authorize application implementation  
**Normative parent:** `RBCE-01_RETROBIT_GAME_PROJECT_FORMAT.md`  
**Schema:** `RBCE-01_RETROBIT_GAME_PROJECT.schema.json`  
**Golden expressiveness fixture:** `RBCE-01_FOUR_ENGINE_TEST_CHAMBER.fixture.json`

## 1. Purpose

This baseline turns the RBCE-01 prose design into artifacts that an eventual application implementation can consume without re-deciding the project shape.

It intentionally separates three classes of validation:

1. **JSON structural validation** — field shape, enumerations, required properties and v1 scripting exclusions implied by a closed schema.
2. **RBCE semantic validation** — stable-ID uniqueness, internal references, graph consistency, project-local state rules, deterministic normalization and lifecycle gates.
3. **Owner/capability validation** — GPR/MRCS/MAI/ISE/campaign/runtime readiness, rights/provenance capability and accepted canonical mutations.

The JSON Schema does not pretend to replace the second or third class.

## 2. Locked machine identifiers

| Item | Locked value |
|---|---|
| Project schema ID | `RBCE01.PROJECT.v1` |
| Initial schema semantic version | `1.0.0` |
| Authoring filename | `retrobit.project.json` |
| Portable package extension | `.pack` |
| Pack embedded-asset policy | `redistributable-only` |
| Runtime scripting escape hatch | none in v1 |

## 3. Validation ownership matrix

| Requirement | JSON Schema | RBCE semantic validator | External owner/capability snapshot |
|---|---:|---:|---:|
| Required top-level fields | yes | no | no |
| Exact v1 schema ID | yes | yes | no |
| Semantic-version syntax | yes | yes | no |
| Allowed seven GPR delivery modes | yes | yes | GPR readiness |
| Default mode appears in supported modes | no | yes | no |
| Stable IDs globally unique in their identity class | no | yes | no |
| Scene exit destination scene exists | no | yes | no |
| Destination entry exists in destination scene | no | yes | no |
| Actor placement references an existing actor definition | no | yes | no |
| Asset-role reference resolves | no | yes | MAI readiness/rights |
| Scene-local variable reference resolves | no | yes | no |
| Variable default matches declared value type | partial | yes | no |
| Enum default is in enum values | no | yes | no |
| `campaign-projection` cannot directly mutate campaign state | partial | yes | campaign owner receipt |
| Input logic is semantic-command based | shape only | yes | GPR command readiness |
| Projection profile is available | shape only | yes | RBCE-02/runtime capability |
| Required GPR pattern/operation is installed/ready | no | no | GPR |
| Required MRCS/owner definition is ready | no | no | owning definition domain |
| Rights permit local use | no | lifecycle evaluation | MAI/ARI/PCA capability |
| Rights permit redistribution | no | publishability evaluation | MAI/ARI/PCA capability |
| Protected study/reference expression absent from production dependency | no | yes | provenance evidence |
| Project is deterministic under reordered ID-addressed collections | no | yes | deterministic hash primitive |
| Blocking project tests pass | no | yes | runtime execution evidence |
| Canonical owner mutation occurred | never inferred | never performed by RBCE validator | owner runtime receipt only |

## 4. Structural invariants locked by the schema

The schema establishes these v1 boundaries before product implementation exists:

- one `identity`, `lineage`, `compatibility`, `delivery`, `gameplay`, `inputs`, `accessibility`, `provenance` and `publishing` object;
- scenes, actors, assets, variables, outcomes, audio bindings and tests as bounded-by-implementation collections rather than arbitrary object graphs;
- closed objects using `additionalProperties: false` so v1 cannot silently grow ad-hoc script/state fields;
- delivery modes limited to the seven existing GPR delivery modes;
- scene projection represented by `projectionProfileRef`, leaving physics/render semantics to RBCE-02;
- actor definitions distinct from scene placements;
- visual resources bound by semantic asset roles and MAI references;
- raw device inputs mapped to semantic commands;
- project variables limited to boolean, integer, number, string, enum and stable-reference values;
- variable scopes limited to `scene`, `run`, `save` and `campaign-projection`;
- campaign-projection write policy limited to owner-receipt or GM adjudication in the structural baseline;
- outcomes represented as proposals to an owning domain/operation rather than direct owner-state edits;
- project tests represented as semantic command sequences and semantic assertions;
- portable packaging locked to `.pack` and redistributable-only embedded assets.

## 5. Semantic failure codes reserved for implementation

The application implementation should preserve these failure-code families so authoring UI, CI and pack validation can share one vocabulary:

- `unsupported-schema`
- `migration-required`
- `invalid-project-identity`
- `duplicate-stable-id`
- `limit-exceeded`
- `invalid-delivery-mode`
- `default-delivery-not-supported`
- `unresolved-required-capability`
- `unresolved-required-definition`
- `unresolved-runtime-binding`
- `invalid-projection-profile`
- `invalid-scene-transition`
- `invalid-entry-reference`
- `invalid-actor-reference`
- `invalid-asset-role-reference`
- `invalid-variable-reference`
- `invalid-variable-default`
- `invalid-input-binding`
- `unauthorized-variable-write-policy`
- `invalid-outcome-owner-binding`
- `accessibility-critical-path-missing`
- `blocking-project-test-failed`
- `protected-reference-production-dependency`
- `redistribution-rights-missing`
- `local-absolute-path-forbidden`
- `nondeterministic-project-normalization`

Failure ordering must be deterministic: `code`, then semantic path, then reference.

## 6. Lifecycle decision table

### `draft`

The project is editable but does not yet satisfy the structural gate.

### `structurally-valid`

Requires the JSON shape plus RBCE semantic identity/reference checks. It does not imply that gameplay dependencies are installed or usable.

### `playable`

Requires structural validity plus:

- at least one reachable scene/entry;
- required GPR patterns/operations/resources ready;
- required owner definitions ready;
- required projection capabilities ready;
- required input semantic commands ready;
- required visual/audio roles resolved or explicitly fallback-safe;
- local-use rights capability where applicable;
- blocking project tests passing.

### `publishable`

Requires playability plus:

- redistribution capability for every embedded asset;
- zero protected-reference production dependencies;
- complete package/dependency metadata;
- no local absolute paths;
- deterministic semantic fingerprint;
- migration baseline;
- publication-target policy satisfied.

A project may intentionally be `playable=true` and `publishable=false`.

### `migration-required`

Returned for a known project whose schema cannot be consumed safely without an explicit migration path. Never silently reinterpret a future schema as v1.

### `blocked`

Returned when a required binding, authority, rights capability or blocking test prevents the requested lifecycle transition.

## 7. Deterministic normalization contract

The eventual implementation must normalize before fingerprinting.

ID-addressed collections normalize by their stable identity:

- scenes by `sceneId`;
- scene entries by `entryId`;
- scene exits by `exitId`;
- placements by `placementId`;
- actors by `actorDefinitionId`;
- assets by `assetRoleId`;
- variables by `variableId`;
- outcomes by `outcomeId`;
- audio by `audioRoleId`;
- input profiles by `profileId`;
- project tests by `testId`.

Sets of stable references normalize lexically when order has no authored semantic meaning.

These sequences remain ordered because order is semantic:

- a project's test `commandSequence`;
- any future explicitly declared timeline/sequence field;
- any ordered dialogue/choice sequence owned by a referenced governed definition.

Whitespace, JSON object-key order and editor-only presentation state must not change the semantic fingerprint.

## 8. Four-Engine golden fixture obligations

`RBCE-01_FOUR_ENGINE_TEST_CHAMBER.fixture.json` is original Multiversal test content. It contains no copied ROM asset, map, dialogue or proprietary implementation.

The fixture intentionally proves one RBCE project can represent:

1. **top-down traversal** — `scene:plaza` uses `projection:top-down-2d` and transitions by semantic triggers;
2. **connected-room gated exploration** — `scene:gate-room` uses `projection:fixed-room-2d`, a persistent gate variable and a prerequisite rule reference;
3. **platform/hazard recovery** — `scene:foundry` uses `projection:side-scroll-2d`, a checkpoint variable and hazard semantic object;
4. **branching dialogue/persistent event state** — `scene:dialogue` uses persistent enum/boolean state with semantic interaction commands.

The fixture also demonstrates:

- mixed projection profiles in one project;
- keyboard and accessibility input profiles feeding the same semantic commands;
- a campaign-projection value that requires owner receipt;
- a typed outcome proposal to `campaign/objectives`;
- MAI-style asset references with separate rights evidence;
- NES/SNES research appearing only as non-production research provenance;
- `.pack` public-distribution intent with redistributable-only embedding.

RBCE-02 may later make the projection profiles executable, but it may not require RBCE-01 to fork this project into separate game formats.

## 9. Explicit non-decisions

This baseline does **not** decide:

- exact runtime/project caps (`Rbce01ProjectLimits` values);
- physics constants, gravity, jump arcs, collision resolution, slopes or one-way-platform behavior;
- sprite atlas slicing/animation schema beyond MAI references;
- Studio/editor UI layout;
- implementation repository placement beyond the already-approved implementation plan;
- public marketplace/community publishing policy;
- exact owner-domain parameter-binding vocabulary where the owner operation contract is more specific than the generic `parameterRef`/`valueRef` planning shape.

These remain implementation or later-tranche decisions and must not be smuggled into RBCE-01 design as fake canon.

## 10. Activation boundary

The implementation plan remains at:

`docs/superpowers/plans/2026-09-27-retrobit-game-project-format.md`

Actual application code under `packages/contracts/src/retrobit-arcade-creation-engine/` remains unauthorized until OPS3 selects RBCE-01 (or an equivalent bounded owner-approved implementation item). The currently selected GPR work is not altered by this machine-contract baseline.
