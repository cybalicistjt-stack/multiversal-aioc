# PDCP — GPR Family Design Closure

**Project:** PDCP — Preimplementation Design Closure Project  
**Family:** GPR — Gameplay Pattern Runtime & Loop Minis  
**Status:** DESIGN_CLOSED FOR FAMILY REDUCTION  
**Baseline:** 16 planned tranches  
**Effective implementation/proof plan:** 10 tranches  
**Implementation authority:** none  
**OPS3 mutation:** none

## 1. Closure decision

GPR remains the reusable gameplay-pattern **execution/composition** layer. It does not become a second rule-definition, Character, World, Combat, Inventory, Economy, Project, Action/Event, map, audio, rights/provenance, or generic creator/debug system.

The 16-tranche baseline contains six standalone seams that are no longer justified after MAL completion, MRCS owner boundaries, PDCP Packets 01–08, and the reduced downstream families are applied. The family can be reduced to ten bounded implementation/proof tranches without capability loss.

The surviving sparse order is:

1. `GPR-01` — Gameplay Runtime Authority, Contract Registry & MAL/MRCS Convergence;
2. `GPR-03` — Deterministic Entity/Input/Collision State Kernel;
3. `GPR-05` — Owner-Domain Gameplay Operation & Route Runtime;
4. `GPR-06` — Specialist Pattern Module Pack;
5. `GPR-07` — Encounter/Autonomy/Score/Timing/Loadout/Skill Runtime;
6. `GPR-08` — Loop-Mini Contract, Pattern Composer & Authoring Schema;
7. `GPR-09` — Delivery Modes, Creator/GM Control & World/Roster Binding;
8. `GPR-10` — Rights-Safe Semantic Presentation & Accessibility Projection;
9. `GPR-12` — Multiplayer, Replay, Persistence, Recovery & Version Continuity;
10. `GPR-16` — Full Conformance, Golden Cross-System Proof & Downstream Handoff.

`GPR-01`, `GPR-05`, and `GPR-16` remain stable because they are existing cross-program milestone references.

## 2. Intra-family overlap audit

### 2.1 `GPR-01 + GPR-02 → GPR-01`

The authority/research/MAL-MRCS convergence tranche and semantic runtime-registry/import/lint tranche are one opening runtime contract. MRCS remains definition authority; GPR needs only the executable registry projection, stable runtime IDs, unsupported-state handling, namespace validation, and MAL/research-baseline compatibility checks.

There is no justification for a second tranche solely to re-register already-governed definitions.

### 2.2 `GPR-04 + GPR-05 → GPR-05`

Movement, combat, projectile, ability, resource, interaction, inventory, economy, progression, objective and route behavior all execute through one owner-domain operation adapter model. Canonical mechanics remain with their owner domains. GPR supplies pattern-level binding, orchestration, typed input/output, deterministic ordering where declared, and route/objective composition.

`GPR-05` survives because it is already a MERA rotation milestone. The merged tranche must not implement parallel Combat, Inventory, Economy, Progression, World, or Action/Event truth.

### 2.3 `GPR-06` remains distinct

Puzzle, sports, vehicle/mount, party/companion, tactical/strategy, social/investigation and stealth adapters share the GPR module contract but still require a broad specialist adapter library and domain-specific conformance fixtures. Folding them into `GPR-07` would create an oversized implementation tranche.

### 2.4 `GPR-07` remains distinct

Encounter/autonomous selection, score/timing/rhythm, loadout/build, and skill-resolution execution have different lifecycle and determinism requirements from the `GPR-06` specialist modules. GPR does not own NPC psychology, AI model authority, audio content, Character build truth, or skill definitions; it owns only bounded execution adapters and inspectable Events.

### 2.5 `GPR-09 + GPR-14 → GPR-09`

The seven delivery modes and the Creator/GM loop studio are two views over the same delivery/control seam. Packet 07 already closes generic preview/dry-run/commit/explanation/intervention/recovery semantics. `GPR-09` therefore implements GPR-specific delivery adapters, loop test/preview bindings, GM controls, world/adventure binding, roster injection and mode parity without creating another generic studio framework.

### 2.6 `GPR-10 + GPR-11 → GPR-10`

Semantic asset-role binding, rights filtering, camera/UI/audio/feedback/accessibility/device projection form one presentation adapter surface. ARI/PCA own resource identity, rights and generic provenance; MCS/MCCS/MSAS and other specialist creators own authored presentation resources. GPR maps authorized semantic roles to runtime presentation and preserves functional nonvisual/device-independent parity.

### 2.7 `GPR-12 + GPR-13 → GPR-12`

Multiplayer authority, deterministic replay/Event trace, snapshots, migration, restore, recovery and version compatibility all operate on the same versioned runtime-state/command/history seam. They must share one continuity contract so multiplayer/replay and persisted state cannot disagree on authority, ordering, version or recovery semantics.

Generic owner-domain version/idempotency/recovery semantics remain external; GPR owns only gameplay-instance continuity and its receipts.

### 2.8 `GPR-15 + GPR-16 → GPR-16`

`GPR-15` contains no independent runtime. Its 168-pattern/85-operation/672-variant conformance is part of the final proof required before downstream handoff. It therefore becomes a required section of `GPR-16` rather than a separate implementation tranche.

## 3. Cross-family/shared-owner audit

### MRCS

MRCS owns reusable rules/content definitions, including Actions, Effects, Conditions, Resources, abilities, items, creatures, vehicles, environments, encounters and scoped rules. GPR imports/binds accepted definitions; it does not author or canonicalize them.

### MAL

MAL-01..10 remain `completed_verified` and frozen. GPR extends broad gameplay-pattern coverage but does not rebuild MAL primitive/input/tiny-state-machine/accessibility/golden foundations where those contracts are already sufficient.

### Action/Event and canonical gameplay owners

Action/Event plus Character, Combat, Inventory/Asset, Economy, Progression, World/Scene/Map, Vehicle/Mount, Project/Time and other domain owners retain canonical mutation truth. GPR composes operations and emits typed outcomes/Events; it never creates a parallel owner ledger.

### PDCP Packet 03

Autonomous actor and offscreen behavior contracts are already design-closed. `GPR-07` implements bounded deterministic selection and optional AI/Encounter integration only; it does not invent a second autonomy/goal/resource model.

### PDCP Packet 04

Semantic affordance/Effect composition is already closed over MRCS/GPR owner seams. GPR retains runtime execution/composition adapters, not a second semantic-definition system.

### PDCP Packet 06

Multi-resolution transition semantics remain with domain owners. GPR delivery modes may execute coarse/fine projections but do not invent aggregate truth.

### PDCP Packet 07

Generic proposal/preview/dry-run/commit/explanation/intervention/compensation/debug/recovery semantics are shared infrastructure. `GPR-08/09/12/16` implement only GPR-specific authoring, delivery, inspection and continuity bindings.

### PDCP Packet 08 / PCA-12

Generic simulation/formal-analysis engines remain with PCA-12/Packet 08. GPR supplies executable models, route/state graphs, conformance fixtures and interpretation; it does not build another solver/simulation laboratory.

### ARI/PCA and specialist creator families

ARI/PCA own generic resource identity, rights, derivative provenance, version/review/import/export. MCS/MCCS/MNCS/MSAS own maps, appearance/actors, NPC/creature content and audio. GPR `GPR-10` binds authorized outputs through semantic roles only.

### Reduced downstream families

Reduced MERA, MBES, MSLR and MSWI consume GPR execution/composition instead of implementing their own generic gameplay engines. Conversely, GPR may not absorb engineering, built-environment, spatial-law or systemic-world consequence truth merely because those domains use GPR loops.

## 4. Runtime identity/state contract

GPR preserves these distinctions:

- reusable `PatternDefinition` / accepted MRCS definition references;
- `PatternConfiguration` / loop-mini authored configuration;
- `GameplayInstance` identity;
- bound owner-domain participant/asset/world references;
- delivery-mode projection/configuration;
- live deterministic or explicitly nondeterministic runtime state;
- command/input stream;
- typed Event/outcome trace;
- persisted snapshot/replay receipt;
- presentation projection.

A definition is not a live instance. A preview is not a committed owner mutation. A snapshot is not source-definition truth. A presentation role is not an Asset identity.

## 5. Execution contract

A gameplay instance follows this bounded path:

1. resolve pattern/configuration and versions;
2. authorize visible/bindable owner-domain inputs;
3. bind runtime roles to stable owner IDs;
4. validate supported operations and declared deterministic/nondeterministic policy;
5. create or restore a versioned gameplay instance;
6. accept semantic input/commands under declared authority;
7. execute GPR state transitions and owner-domain operations;
8. record ordered typed Events/outcomes and resource/condition/reward/story/map deltas;
9. hand canonical mutations to their owning domains;
10. update replay/snapshot/continuity receipts;
11. project authorized presentation and explanation.

No GPR-local success state can prove that an external owner mutation occurred without its owner receipt/evidence.

## 6. Delivery-mode contract

The seven supported modes remain:

- direct play;
- cozy/low-pressure play;
- GM-led play;
- world-map/TTRPG bridge;
- embedded minigame;
- user-authored loop mini;
- Multiversal roster injection.

Mode changes may alter governed timer/aggression/resource/retry/hint/control/presentation policies. They may not fork canonical mechanics truth or silently change Character/World/Inventory ownership.

## 7. Multiplayer, replay and persistence contract

`GPR-12` must distinguish:

- player/controller slot authority;
- shared versus local presentation state;
- authoritative command ordering;
- deterministic modules versus explicitly nondeterministic modules;
- replay inputs versus derived presentation frames;
- snapshot schema/version;
- migration path and unsupported-version state;
- idempotent/recoverable owner-operation receipts;
- reconnect/resume state;
- corruption/incomplete-history failure states.

A replay advertised as deterministic must reproduce governed semantic state/Event results from the same declared inputs, configuration, seed and versions. Bit-identical rendering is not required unless separately promised.

## 8. Rights, privacy and visibility

Visibility/permission filtering occurs before participant lists, target choices, counts, summaries, diagnostics, replay exports, creator views, AI context and presentation-role binding are constructed for an audience.

Rights/use capability is checked before a resource becomes a production presentation binding or export. Reference-only/commercial benchmark material remains planning evidence only.

## 9. Accessibility and provider independence

Every blocking gameplay operation has a semantic non-drag/non-twitch alternative where the governing pattern allows equivalent semantics. Visual-only cues require equivalent textual/audio/haptic or other governed alternatives. GPR cannot require a 3D renderer or paid/cloud provider for blocking execution, authoring, test, replay, recovery or proof.

Optional AI remains advisory and visibility-safe. It may propose patterns/configuration or explain traces; it cannot grant permissions, mutate owner state, canonize definitions or declare a proof passed.

## 10. Failure/unknown rules

- Unsupported pattern/operation remains unsupported; no generic fallback may silently invent semantics.
- Unknown owner data remains unknown rather than zero/empty/unlimited/compatible.
- Missing rights remains blocked/unresolved, not assumed permitted.
- Snapshot migration failure does not partially mutate the live gameplay instance.
- Replay mismatch is a diagnostic failure, not permission to rewrite history.
- Network ambiguity resolves through authoritative operation/status evidence before retry.
- Hidden information cannot be inferred through counts, route availability, error detail, timing, replay/export metadata or AI explanation.

## 11. Golden vectors

`GPR-16` owns the complete reduced-family proof. The following vectors are mandatory design-level acceptance cases:

1. `GPR-PDCP-001` — MAL-completed primitive is reused without reopening MAL authority.
2. `GPR-PDCP-002` — MRCS accepted definition binds by stable ID/version.
3. `GPR-PDCP-003` — unsupported definition/operation fails closed.
4. `GPR-PDCP-004` — namespace collision is rejected deterministically.
5. `GPR-PDCP-005` — runtime instance does not mutate reusable definition.
6. `GPR-PDCP-006` — semantic input mapping is device-independent.
7. `GPR-PDCP-007` — collision/trigger transition is replay-stable where declared deterministic.
8. `GPR-PDCP-008` — fixed-step/state ordering does not depend on UI frame order.
9. `GPR-PDCP-009` — movement operation hands canonical movement to the proper owner.
10. `GPR-PDCP-010` — combat/projectile operation cannot create parallel Combat truth.
11. `GPR-PDCP-011` — ability/resource operation commits costs/results atomically through owners.
12. `GPR-PDCP-012` — inventory/economy reward remains a typed proposal/outcome until owner commit.
13. `GPR-PDCP-013` — progression/unlock cannot bypass Progression authority.
14. `GPR-PDCP-014` — world-route/objective loop uses stable World/Scene references.
15. `GPR-PDCP-015` — puzzle pattern executes through reusable operations, not bespoke game code.
16. `GPR-PDCP-016` — sports possession/score pattern preserves explicit authority/state.
17. `GPR-PDCP-017` — vehicle/mount loop consumes vehicle owner state without cloning it.
18. `GPR-PDCP-018` — party/companion loop preserves Character/NPC identities.
19. `GPR-PDCP-019` — tactical/strategy loop emits typed owner-domain deltas.
20. `GPR-PDCP-020` — social/investigation loop respects Packet 01/02 visibility and evidence semantics.
21. `GPR-PDCP-021` — stealth/detection loop cannot infer hidden actors through counts/errors.
22. `GPR-PDCP-022` — autonomous/encounter selection is bounded and non-omniscient.
23. `GPR-PDCP-023` — optional AI is advisory only and can be disabled.
24. `GPR-PDCP-024` — score/timing/rhythm result is semantic and not tied to renderer frame rate.
25. `GPR-PDCP-025` — loadout/build runtime cannot change Character/Asset ownership implicitly.
26. `GPR-PDCP-026` — skill resolution consumes governed skill/rule definitions without redefining them.
27. `GPR-PDCP-027` — loop-mini authoring produces noncanonical configuration until executed/committed.
28. `GPR-PDCP-028` — authoring cap rejects unbounded recursion/spawn/persistent-object configuration.
29. `GPR-PDCP-029` — direct and cozy modes share one mechanics truth.
30. `GPR-PDCP-030` — GM-led mode uses governed intervention rather than bespoke hidden mutation.
31. `GPR-PDCP-031` — world/TTRPG bridge emits explicit success/partial/failure typed outcomes.
32. `GPR-PDCP-032` — embedded minigame returns controlled deltas to its Adventure/session owner.
33. `GPR-PDCP-033` — user-authored loop mini revalidates permissions and limits at execution.
34. `GPR-PDCP-034` — roster injection preserves Character identity, equipment and ability ownership.
35. `GPR-PDCP-035` — hidden roster/world facts are filtered before creator/player projection.
36. `GPR-PDCP-036` — semantic asset role accepts an authorized original/right-cleared binding.
37. `GPR-PDCP-037` — reference-only/commercial asset binding is rejected for production/export.
38. `GPR-PDCP-038` — camera/UI/audio presentation can change without changing mechanics truth.
39. `GPR-PDCP-039` — equivalent nonvisual gameplay path exists for a visual presentation flow.
40. `GPR-PDCP-040` — multiplayer command authority is explicit and not arrival-order dependent.
41. `GPR-PDCP-041` — deterministic replay reproduces governed state/Event outcomes.
42. `GPR-PDCP-042` — snapshot/restore preserves instance and owner-reference identity.
43. `GPR-PDCP-043` — version migration is explicit and an unsupported version fails closed.
44. `GPR-PDCP-044` — reconnect/retry does not duplicate owner mutations or rewards.
45. `GPR-PDCP-045` — replay/export respects visibility and rights filters.
46. `GPR-PDCP-046` — full 168-pattern/85-operation/672-variant conformance evidence is attached to final proof.
47. `GPR-PDCP-047` — provider-off local execution/authoring/replay/recovery succeeds.
48. `GPR-PDCP-048` — final original-content proof hands reusable execution to MERA/MBES/MSLR/MSWI/SMB without owner bleed.

## 12. Residual implementation mapping

| Survivor | Baseline absorbed | Repository-bound residual |
|---|---|---|
| `GPR-01` | 01, 02 | runtime authority/registry projection, MAL/MRCS import adapters, namespace/schema validation |
| `GPR-03` | 03 | deterministic instance/input/collision/state kernel and bounded caps |
| `GPR-05` | 04, 05 | owner-domain gameplay operation adapters, objectives/routes, typed handoffs; preserves MERA rotation gate |
| `GPR-06` | 06 | specialist reusable module adapters and fixtures |
| `GPR-07` | 07 | encounter/autonomy/score/timing/loadout/skill execution adapters |
| `GPR-08` | 08 | loop-mini schema/composer and bounded authoring validation |
| `GPR-09` | 09, 14 | seven delivery adapters, GPR-specific Creator/GM UX, world/adventure/roster binding over Packet 07 |
| `GPR-10` | 10, 11 | rights-safe semantic presentation bindings, camera/UI/audio/accessibility/device projection |
| `GPR-12` | 12, 13 | multiplayer authority, replay/Event trace, snapshot/migration/recovery/version continuity |
| `GPR-16` | 15, 16 | complete conformance/regression/golden proof and downstream handoff |

No baseline capability is removed. The family simply stops implementing the same execution-adjacent concern in multiple standalone tranches.
