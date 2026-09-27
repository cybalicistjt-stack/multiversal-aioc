# Retrobit Game Project Format Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement RBCE-01 as a versioned, deterministic, rights-aware Retrobit Game Project contract that composes existing GPR/MRCS/MAI/ISE authorities without creating a parallel game-state engine.

**Architecture:** Add one focused contract family under `packages/contracts/src/retrobit-arcade-creation-engine/` with pure validation/normalization/fingerprint/pack-projection behavior and integration tests under the client test surface. Reuse GPR delivery/runtime IDs and existing deterministic hash primitives; keep runtime rendering/physics, Studio UI and asset-workbench behavior out of RBCE-01.

**Tech Stack:** TypeScript contracts, Vitest integration tests, Python invariant verifier, existing Multiversal validation-core profile, existing deterministic runtime primitives.

**Spec:** `governance/application-planning/retrobit-arcade-creation-engine/RBCE-01_RETROBIT_GAME_PROJECT_FORMAT.md`

## Global Constraints

- Implementation begins only after OPS3 explicitly selects/authorizes RBCE-01 or an equivalent bounded work item; this plan does not alter `operations/CURRENT.json`.
- Portable distribution uses the existing `.pack` extension; RBCE must not introduce another package extension.
- `RBCE01.PROJECT.v1` is the initial schema identifier.
- GPR remains gameplay runtime authority; MRCS/owner domains remain definition authority; MAI/ARI/PCA remain asset/provenance/rights authority; ISE/Scene/World owners retain spatial/scene truth.
- Project source, gameplay save/snapshot and canonical owner state remain distinct.
- No arbitrary JavaScript, Lua, Python or unrestricted scripting field is introduced in v1.
- All semantic output must be deterministic for semantically equivalent input ordering.
- Missing/unsupported required bindings fail closed; no generic fallback invents gameplay definitions or rights.
- Local `playable` and distributable `publishable` are separate lifecycle states.
- Protected NES/SNES/reference material may be research provenance only and may not become a runtime or packaged production dependency without independent rights evidence.
- RBCE-02 rendering/physics behavior is explicitly out of scope.

## Review Focus

1. **Mixed scene projection profiles** — one project containing top-down, fixed-room and side-scroll scenes must validate without inventing RBCE-02 physics behavior; Task 2 tests this.
2. **Rights split** — a project with reference-only local art may be playable but must fail publishability when redistribution capability is absent; Task 5 tests this.
3. **Hidden/persistent state** — save-scoped and campaign-projection variables must preserve visibility/write-policy rules and never become direct campaign mutation; Task 3 tests this.
4. **Semantically equivalent ordering** — reordered ID-addressed arrays must produce the same normalized fingerprint; Task 4 tests this.
5. **Four-Engine expressiveness** — the format must represent top-down traversal, gated connected rooms, platform/hazard recovery and dialogue/persistent-event state without schema escape hatches; Task 6 tests this.

---

## File Structure

Application repository (`cybalicistjt-stack/Multiversal-app`):

- Create `packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-types.ts` — schema/type definitions only.
- Create `packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-validation.ts` — structural/reference/lifecycle validation.
- Create `packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-normalization.ts` — stable normalization and semantic fingerprint.
- Create `packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-pack-projection.ts` — `.pack` publication projection and rights-safe include/reference split.
- Create `packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-migration.ts` — explicit migration receipt/registry boundary for v1 onward.
- Create `apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts` — focused contract integration tests, including Four-Engine fixture.
- Create `fixtures/golden/rbce01-four-engine-test-chamber.fixture-set.json` — original/right-cleared semantic fixture with no protected source expression.
- Create `governance/application-planning/retrobit-arcade-creation-engine/RBCE-01_RETROBIT_GAME_PROJECT_FORMAT.md` — implementation-side mirror of the accepted spec.
- Create `governance/application-planning/validation-core/profiles/RBCE-01.json` — focused validation gate.
- Create `tools/verify_rbce_01.py` — source/invariant verifier.

Control repository (`cybalicistjt-stack/multiversal-aioc`) on authorized activation/closeout only:

- Preserve this plan and the parent charter/spec.
- Add/modify OPS3 work-item/checkpoint/selectors only through the separately authorized activation flow; do not make those changes as part of ordinary product code tasks.

---

### Task 1: Schema Types and Identity Boundary

**Files:**
- Create: `packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-types.ts`
- Test: `apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts`

**Interfaces:**
- Consumes: `Gpr08DeliveryMode` from `packages/contracts/src/gameplay-pattern-runtime/gpr-08-loop-mini-composer.ts`.
- Produces: `RBCE01_SCHEMA_ID`, `RBCE01_SCHEMA_VERSION`, `RetrobitGameProject`, all RBCE-01 subordinate interfaces, and `Rbce01ProjectLimits`.

- [ ] **Step 1: Write the failing type/identity test**

```ts
it("defines a v1 project identity without creating runtime authority", () => {
  expect(RBCE01_SCHEMA_ID).toBe("RBCE01.PROJECT.v1");
  expect(RBCE01_SCHEMA_VERSION).toBe("1.0.0");
  const project = minimalProject();
  expect(project.identity.projectId).toBe("retrobit-project:test-chamber");
  expect(project.delivery.defaultMode).toBe("direct-play");
});
```

- [ ] **Step 2: Run the focused test and verify RED**

Run: `pnpm --filter @multiversal/app-client-ui exec vitest run src/rbce/rbce-01.retrobit-game-project.integration.test.ts --maxWorkers=1 --minWorkers=1`

Expected: FAIL because the RBCE-01 module/types do not exist.

- [ ] **Step 3: Implement the schema/type module**

Export exactly:

```ts
export const RBCE01_SCHEMA_ID = "RBCE01.PROJECT.v1" as const;
export const RBCE01_SCHEMA_VERSION = "1.0.0" as const;
export interface RetrobitGameProject { /* fields from accepted spec */ }
export interface Rbce01ProjectLimits {
  maxScenes:number;
  maxPlacementsPerScene:number;
  maxActors:number;
  maxTransitions:number;
  maxVariables:number;
  maxInputBindings:number;
  maxOutcomeBindings:number;
  maxAssetBindings:number;
  maxAudioBindings:number;
  maxTests:number;
  maxCommandsPerTest:number;
}
```

Do not add renderer/physics fields or arbitrary script bodies.

- [ ] **Step 4: Run the focused test and verify GREEN**

Run the same Vitest command. Expected: PASS for the identity/type case.

- [ ] **Step 5: Commit**

```bash
git add packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-types.ts apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts
git commit -m "feat(rbce): define Retrobit project schema"
```

### Task 2: Structural, Reference and Scene-Graph Validation

**Files:**
- Create: `packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-validation.ts`
- Modify/Test: `apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts`

**Interfaces:**
- Consumes: RBCE-01 types and a caller-supplied capability/binding snapshot; it must not query providers directly.
- Produces: `validateRbce01Project(input): Rbce01ValidationResult` and typed failure codes.

- [ ] **Step 1: Add failing validation tests**

```ts
it("fails closed for duplicate IDs and broken scene exits", () => {
  const result = validateRbce01Project({project: projectWithBrokenGraph(), capabilities: readyCapabilities(), limits: testLimits()});
  expect(result.accepted).toBe(false);
  expect(result.failures.map(x => x.code)).toEqual(expect.arrayContaining(["duplicate-stable-id","invalid-scene-transition"]));
});

it("accepts mixed top-down fixed-room and side-scroll projection references", () => {
  const result = validateRbce01Project({project: mixedProjectionProject(), capabilities: readyCapabilities(), limits: testLimits()});
  expect(result.failures).not.toContainEqual(expect.objectContaining({code:"invalid-projection-profile"}));
});
```

- [ ] **Step 2: Run focused test and verify RED**

Expected: FAIL because `validateRbce01Project` is absent.

- [ ] **Step 3: Implement `validateRbce01Project`**

Signature:

```ts
export function validateRbce01Project(input:{
  project:RetrobitGameProject;
  capabilities:Rbce01CapabilitySnapshot;
  limits:Rbce01ProjectLimits;
}):Rbce01ValidationResult;
```

Validate identity/version, ID uniqueness, internal refs, caps, scene graph, entry/exit pairs, actor placements, projection-profile capability refs, seven GPR delivery modes, required gameplay bindings and required owner definitions. Sort failures deterministically by code/path/reference.

- [ ] **Step 4: Run focused test and verify GREEN**

- [ ] **Step 5: Commit**

```bash
git add packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-validation.ts apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts
git commit -m "feat(rbce): validate project graph and bindings"
```

### Task 3: Variables, Inputs, Outcomes and Lifecycle Evaluation

**Files:**
- Modify: `packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-validation.ts`
- Modify/Test: `apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts`

**Interfaces:**
- Consumes: validated project + capability snapshot.
- Produces: `evaluateRbce01Lifecycle(input): Rbce01LifecycleEvaluation` with `draft|structurally-valid|playable|publishable|migration-required|blocked` and separate play/publish blockers.

- [ ] **Step 1: Add failing tests for semantic input and state authority**

```ts
it("rejects raw-device branching and invalid campaign-projection writes", () => {
  const result = validateRbce01Project({project: invalidStateAuthorityProject(), capabilities: readyCapabilities(), limits: testLimits()});
  expect(result.failures.map(x => x.code)).toEqual(expect.arrayContaining(["invalid-input-binding","unauthorized-variable-write-policy"]));
});

it("keeps campaign projection as an owner operation proposal", () => {
  const result = evaluateRbce01Lifecycle({project: campaignProjectionProject(), capabilities: readyCapabilities(), limits: testLimits()});
  expect(result.canonicalOwnerMutationPerformed).toBe(false);
  expect(result.playable).toBe(true);
});
```

- [ ] **Step 2: Run focused test and verify RED**

- [ ] **Step 3: Implement variable/input/outcome validation and lifecycle evaluation**

Exact function:

```ts
export function evaluateRbce01Lifecycle(input:{
  project:RetrobitGameProject;
  capabilities:Rbce01CapabilitySnapshot;
  limits:Rbce01ProjectLimits;
}):Rbce01LifecycleEvaluation;
```

Enforce typed variable defaults, enum membership, allowed scopes/write policies, semantic command refs, owner-domain outcome bindings, required accessible critical path markers and playable/publishable separation.

- [ ] **Step 4: Run focused test and verify GREEN**

- [ ] **Step 5: Commit**

```bash
git add packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-validation.ts apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts
git commit -m "feat(rbce): enforce project state and outcome authority"
```

### Task 4: Deterministic Normalization, Fingerprint and Migration Receipt

**Files:**
- Create: `packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-normalization.ts`
- Create: `packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-migration.ts`
- Modify/Test: `apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts`

**Interfaces:**
- Consumes: valid RBCE-01 project and existing `deterministicRuntimeHash`.
- Produces: `normalizeRbce01Project`, `fingerprintRbce01Project`, `migrateRbce01Project`, `Rbce01MigrationReceipt`.

- [ ] **Step 1: Add failing deterministic-order test**

```ts
it("fingerprints semantically equivalent collection ordering identically", () => {
  expect(fingerprintRbce01Project(projectOrderA())).toBe(fingerprintRbce01Project(projectOrderB()));
});
```

- [ ] **Step 2: Add failing future-schema migration test**

```ts
it("fails closed on unknown newer schema", () => {
  const result = migrateRbce01Project({source: futureSchemaProject(), targetSchemaId: RBCE01_SCHEMA_ID});
  expect(result.status).toBe("unsupported-source-schema");
});
```

- [ ] **Step 3: Run focused test and verify RED**

- [ ] **Step 4: Implement deterministic normalization and migration boundary**

Signatures:

```ts
export function normalizeRbce01Project(project:RetrobitGameProject):Rbce01NormalizedProject;
export function fingerprintRbce01Project(project:RetrobitGameProject):string;
export function migrateRbce01Project(input:Rbce01MigrationInput):Rbce01MigrationResult;
```

Normalize ID-addressed collections by stable ID, preserve explicitly ordered command sequences, exclude editor-only UI state, and include semantic compatibility/rights/test fields in the fingerprint. Migration receipts contain source schema, target schema, before fingerprint and after fingerprint.

- [ ] **Step 5: Run focused test and verify GREEN**

- [ ] **Step 6: Commit**

```bash
git add packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-normalization.ts packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-migration.ts apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts
git commit -m "feat(rbce): add deterministic project fingerprints"
```

### Task 5: Rights-Safe `.pack` Projection

**Files:**
- Create: `packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-pack-projection.ts`
- Modify/Test: `apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts`

**Interfaces:**
- Consumes: lifecycle-evaluated project + rights capability snapshot.
- Produces: `buildRbce01PackProjection(input): Rbce01PackProjectionResult`.

- [ ] **Step 1: Add failing playable-vs-publishable rights test**

```ts
it("allows local play with permitted reference-only art but blocks redistribution", () => {
  const lifecycle = evaluateRbce01Lifecycle({project: referenceOnlyArtProject(), capabilities: localUseOnlyCapabilities(), limits: testLimits()});
  expect(lifecycle.playable).toBe(true);
  expect(lifecycle.publishable).toBe(false);
  const pack = buildRbce01PackProjection({project: referenceOnlyArtProject(), rights: localUseOnlyRights()});
  expect(pack.includedAssetRefs).not.toContain("asset:reference-only");
  expect(pack.referenceOnlyAssetRefs).toContain("asset:reference-only");
});
```

- [ ] **Step 2: Run focused test and verify RED**

- [ ] **Step 3: Implement pack projection**

Signature:

```ts
export function buildRbce01PackProjection(input:{
  project:RetrobitGameProject;
  rights:Rbce01RightsCapabilitySnapshot;
}):Rbce01PackProjectionResult;
```

Require `.pack`, emit `retrobit.project.json`, split redistributable vs reference-only assets, preserve dependency refs and reject protected production references. Do not copy source bytes in this contract layer.

- [ ] **Step 4: Run focused test and verify GREEN**

- [ ] **Step 5: Commit**

```bash
git add packages/contracts/src/retrobit-arcade-creation-engine/rbce-01-pack-projection.ts apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts
git commit -m "feat(rbce): add rights-safe pack projection"
```

### Task 6: Four-Engine Golden Fixture and Semantic Tests

**Files:**
- Create: `fixtures/golden/rbce01-four-engine-test-chamber.fixture-set.json`
- Modify/Test: `apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts`

**Interfaces:**
- Consumes: all RBCE-01 functions from Tasks 1–5.
- Produces: one original/right-cleared fixture proving v1 schema expressiveness; no renderer output required.

- [ ] **Step 1: Create the golden fixture as data only**

The fixture must contain:

- top-down start scene and explicit scene transition;
- connected-room gate that rejects before prerequisite and accepts after governed state change;
- side-scroll scene carrying move/jump semantic command refs, hazard trigger and checkpoint/save variable;
- NPC interaction with branching rule refs and a save-scoped event variable;
- no protected reference asset dependency;
- at least one blocking semantic project test per engine slice.

- [ ] **Step 2: Add failing fixture acceptance test**

```ts
it("represents all four engine slices without schema escape hatches", () => {
  const project = loadFourEngineFixture();
  const result = evaluateRbce01Lifecycle({project, capabilities: fourEngineCapabilities(), limits: goldenLimits()});
  expect(result.playable).toBe(true);
  expect(result.blockers).toEqual([]);
  expect(project.scenes.map(x => x.projectionProfileRef)).toEqual(expect.arrayContaining(["projection:top-down-2d","projection:fixed-room-2d","projection:side-scroll-2d"]));
});
```

- [ ] **Step 3: Run focused test and verify GREEN after fixing only RBCE-01 contract gaps**

Do not add renderer/physics implementation to make this test pass. If the fixture exposes a physics requirement, preserve it as a capability reference for RBCE-02.

- [ ] **Step 4: Commit**

```bash
git add fixtures/golden/rbce01-four-engine-test-chamber.fixture-set.json apps/client-ui/src/rbce/rbce-01.retrobit-game-project.integration.test.ts
git commit -m "test(rbce): prove four-engine project expressiveness"
```

### Task 7: Governed Verifier, Validation Profile and Implementation-Side Spec

**Files:**
- Create: `tools/verify_rbce_01.py`
- Create: `governance/application-planning/validation-core/profiles/RBCE-01.json`
- Create: `governance/application-planning/retrobit-arcade-creation-engine/RBCE-01_RETROBIT_GAME_PROJECT_FORMAT.md`

**Interfaces:**
- Consumes: final RBCE-01 source/test/fixture paths.
- Produces: invariant verifier and focused exact-head acceptance profile.

- [ ] **Step 1: Add verifier invariants**

`tools/verify_rbce_01.py` must require:

- schema ID/version markers;
- all five contract modules;
- the focused integration test and Four-Engine fixture;
- seven GPR delivery modes reused rather than redefined incompatibly;
- `.pack` packaging marker;
- no `customScript`/arbitrary script execution field;
- explicit protected-reference rejection;
- deterministic fingerprint function;
- lifecycle distinction between playable and publishable.

- [ ] **Step 2: Create the focused validation profile**

Profile commands must run at least:

```text
python tools/verify_rbce_01.py
pnpm --filter @multiversal/app-client-ui exec vitest run src/rbce/rbce-01.retrobit-game-project.integration.test.ts --maxWorkers=1 --minWorkers=1
pnpm --filter @multiversal/app-client-ui typecheck
```

Use the repository's current validation-core schema and cross-platform requirements at execution time; do not copy a stale profile shape from this plan.

- [ ] **Step 3: Mirror the accepted RBCE-01 spec into the application repository**

Copy semantic requirements from the accepted control-repository spec without changing owner decisions during implementation.

- [ ] **Step 4: Run focused verifier/test/typecheck**

Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add tools/verify_rbce_01.py governance/application-planning/validation-core/profiles/RBCE-01.json governance/application-planning/retrobit-arcade-creation-engine/RBCE-01_RETROBIT_GAME_PROJECT_FORMAT.md
git commit -m "test(rbce): govern project format acceptance"
```

## Final Verification Before Completion

- [ ] Run the selected RBCE-01 validation-core profile on the immutable candidate head.
- [ ] Confirm the Four-Engine fixture remains original/right-cleared and has zero protected-reference runtime dependencies.
- [ ] Confirm no files from RBCE-02+ were introduced.
- [ ] Confirm reordered semantic collections preserve the same fingerprint while ordered test command sequences remain order-sensitive.
- [ ] Confirm a local-use/reference-only asset case is playable but not publishable.
- [ ] Confirm unknown future schema fails closed with `migration-required`/unsupported-source behavior rather than being guessed.
- [ ] Confirm project loading, gameplay snapshot loading and canonical owner mutation remain three distinct operations.
- [ ] Publish only through the OPS3 mode selected at execution time; do not write protected `main` directly.

## Self-Review Result

Spec coverage: all RBCE-01 sections map to Tasks 1–7. Renderer/physics, Studio UI, asset workbench, human-readable pattern catalog and production Four-Engine art/gameplay remain deliberately deferred.

Type consistency: schema/type interfaces originate in Task 1; all later task signatures consume those types. GPR delivery vocabulary is imported rather than independently forked.

Review-focus coverage: mixed projection profiles → Task 2; rights split → Task 5; hidden/persistent state → Task 3; deterministic ordering → Task 4; Four-Engine expressiveness → Task 6.

Proportion: the plan fixes interfaces, test assertions and authority boundaries without transcribing implementation bodies.
