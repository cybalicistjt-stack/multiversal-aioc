# APW-08 — Implementation Handoff and Stage/Internal-Alpha Integration

**Work item:** APW-08  
**Program:** APW — Asynchronous Play & Persistent Workspace  
**Status:** FINAL DESIGN / GOVERNANCE HANDOFF  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-19

## 1. Decision

APW-08 closes the owner-approved APW/APM/CSW design series and converts it into one additive, dependency-ordered application implementation program.

The handoff does **not** itself implement product code or migrations. It defines the implementation destinations, ownership boundaries, current-baseline migration policy, feature/fallback strategy, deterministic acceptance evidence and roadmap placement. Actual application work becomes active only through a separate post-APW-08 selector transition after this tranche is `completed_verified`.

The first recommended implementation item is **APW-I01 — contextual account/role projection and Personal-context authority extensions** because every later Personal, asynchronous, creator and automated-play surface depends on the universal-account/contextual-authority model.

## 2. Verified application baseline

APW-08 is prepared against:

- application repository: `cybalicistjt-stack/Multiversal-app`;
- application `main`: `bf61c64c89e7ea997842ea7442797fba619d0e28`;
- current migration head: `database/migrations/0008_a10_world_content_authoring.json`;
- existing domain architecture including actions/adjudication, Adventure/travel, audit/export/recovery, authoring/provenance, authority/control, Campaign membership, Character/actors, combat/initiative, diagnostics/support, downtime/projects, entitlement/access, entity catalog, visibility/projection and related Stage A roots;
- client shell/UI root: `apps/client-ui/src/**`, including the existing App and Stage A/alpha shells.

The baseline MUST be rechecked when each application slice starts. Existing migrations `0001` through `0008` are immutable historical predecessors. The next additive migration number is `0009` only while this exact application baseline remains current; a later main change may consume that number before activation.

## 3. Authority and persistence principles

1. No APW, CSW or APM implementation creates a second Campaign/game state engine.
2. Existing owning domains continue to own authoritative payloads and Events.
3. APW orchestration records do not absorb Character, Asset, investigation, social, Adventure, World or creator truth.
4. CSW creative-support persistence initially uses bounded additive D29 `authoring-provenance` records; governed content remains referenced from its owning domain.
5. APM automation-run/delegation/provenance records govern automation execution only and never replace ordinary domain state/Event history.
6. D05 visibility-projection filtering occurs before counts, search, topology, notifications, diagnostics, exports and optional-AI context.
7. One stable operation ID represents one authoritative user/controller intent across retries; accepted business effects are at-most-once.
8. Broad offline authoritative mutation remains out of scope. Offline support is approved read-only projection plus local drafts and deterministic reconciliation.
9. Completed Stage A migrations/contracts are not rewritten merely because successor work needs additive capability.

## 4. Final implementation handles

### APW

- **APW-I01 — Contextual account/role projection and Personal-context authority extensions**
- **APW-I02 — Personal Home and workspace switching**
- **APW-I03 — Asynchronous Action submission, durable GM inbox and delayed resolution**
- **APW-I04 — Bounded Campaign Activity/downtime integration**
- **APW-I05 — Creator Workshop, reusable library and Sandbox/Lab integration**
- **APW-I06 — Notification, visibility, recovery and hybrid cross-device integration**
- **APW-I07 — End-to-end hybrid acceptance: live → async → GM resolution → Player return → live continuation**

### CSW

CSW-I01 through CSW-I08 are inherited unchanged from CSW-10. D29 remains the initial creative-support persistence owner and all governed incorporation remains explicit and receipt-bound.

### APM

APM-I01 through APM-I06 are inherited unchanged from APM-06. Automation remains APM-01-bounded, owning-domain authorized, no-AI capable and based on the same ordinary state/Event history.

## 5. Cross-program dependency waves

The implementation program is organized into leverage-first waves. A wave means dependency readiness; governance may still execute one bounded tranche at a time.

### Wave 1 — authority and durable identity foundation

1. **APW-I01**
2. **CSW-I01** after APW-I01
3. **APM-I01** after APW-I01

This establishes the shared subject/context model, D29 creative identity/provenance and automation-run/delegation identity before richer product surfaces depend on them.

### Wave 2 — core Personal and asynchronous utility

4. **APW-I02** — Personal Home/workspace switching
5. **APW-I03** — async Action/GM inbox
6. **APW-I04** — Campaign Activity/downtime after APW-I03
7. **CSW-I02** — Creative Library/Story Bible/Project Memory after CSW-I01

### Wave 3 — first creator and automated-play value

8. **APM-I02** — Cozy Solo after APW-I02/APW-I04/APM-I01
9. **APM-I03** — AutoGM Single Encounter after APM-I01
10. **APW-I05** — Creator Workshop/Sandbox after APW-I01/APW-I02 and compatible creator foundations
11. **CSW-I03** — Idea Inbox/Inspiration
12. **CSW-I04** — Guided Creation

### Wave 4 — deep creator tooling

13. **CSW-I05** — Narrative Lab + Continuity/Open Threads
14. **CSW-I06** — Writing Studio + Revision
15. **CSW-I07** — Reuse/Remix after APW-I05

### Wave 5 — shared shell/recovery integration

16. **APW-I06** — notification/visibility/recovery/hybrid integration after APW-I03/APW-I04/APW-I05
17. **CSW-I08** — Creator Command Center after all prior CSW slices and APW-I05/APW-I06

### Wave 6 — connected and multi-scene automated play

18. **APM-I04** — Connected Cozy after APM-I02 and APW-I06
19. **APM-I05** — AutoGM Mini-Campaign after APM-I03 and bounded Adventure support
20. **APM-I06** — automated-play recovery/safety/E2E after APM-I04/APM-I05 and APW-I06

This preserves the approved product ladder: Cozy Solo → Single-Encounter AutoGM → Connected Cozy → AutoGM Mini-Campaign.

### Wave 7 — whole-program acceptance

21. **APW-I07** — final hybrid end-to-end acceptance after APW-I06, CSW-I08 and APM-I06.

## 6. Default strict execution order

When a single linear order is required, use:

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

A later slice may move earlier only when its declared dependencies remain satisfied and the owner approves the reorder. The default order maximizes reuse while preserving the owner-approved automated-play progression.

## 7. Persistence and migration inventory

### 7.1 Current rule

At baseline `bf61c64…`, migration `0008` is the current head. No existing migration may be edited. Every implementation tranche that requires schema changes must inspect current `main` immediately before branching and claim the next unused additive migration number.

### 7.2 Expected additive change families

**APW durable workspace/async changes** may require additive records or fields for Personal workspace metadata, async operation/status/inbox projections, Campaign Activity bookkeeping, durable attention/notification metadata, recovery receipts/cursors and cross-device reconciliation. These records must remain under their established owning domains rather than one APW table family.

**CSW creative-support changes** are expected under D29 authoring-provenance for creative fragments/projects, Story Bible/project-memory references, guided workflow state, narrative plans/open threads, writing revisions, derivative lineage and explicit incorporation receipts. Governed payloads are stable references, not copied truth.

**APM automated-play changes** may require additive automation-run/delegation/profile/package linkage, controller operation provenance, participant/shared-activity contribution bookkeeping and parent/child completion receipts. Ordinary Character, Asset, encounter, Adventure and Campaign state remains in existing owners.

### 7.3 Migration numbering policy

- `0009` is the current next slot, **not permanently reserved** by this document.
- Do not pre-create empty future migrations.
- A slice with no durable schema delta uses no migration.
- When multiple adjacent changes have the same owner and atomic rollback boundary, one additive migration may cover them; cross-owner tables still retain explicit ownership.
- If application `main` changes before activation, re-evaluate names/numbers before the first slice; never renumber an already merged migration.

## 8. Additive application touch-point map

### Identity, account and authority

Primary roots: authority/control, Campaign membership, entitlement/access, identity/context contracts and client context projections. APW-I01 adds universal-account/contextual-role projection semantics; it does not invent permanent Player/GM account types.

### Personal Home and workspace shell

Primary client root: `apps/client-ui/src/**` plus existing Personal/Character/library/domain APIs. APW-I02 adds Personal Home projections and context switching without creating a Personal authority super-domain.

### Campaign / Scene / Session

Reuse existing Campaign membership and Stage A Campaign/Scene/Session contracts. APW adds cadence/pending/workspace behavior but does not redefine Campaign identity or Session authority.

### Action / proposal / approval

Reuse existing A6 Action/approval persistence and `actions-adjudication` contracts. APW-I03 extends durable asynchronous submission/status/inbox/decision-return behavior with stable operation IDs and expected versions.

### Downtime / crafting / research / social / investigation

Reuse `downtime-projects` and existing A8/A9 ownership. APW-I04 is an orchestration/workspace layer; it cannot silently advance training, reveal hidden investigation state, consent socially for humans, or bypass Asset ownership/economy rules.

### Creator / World / Adventure

APW-I05 and CSW reuse D29 authoring-provenance, D18 World/location, D28 Adventure/travel, D07 entity catalog, D06 pack registry, D13 media and D05 visibility. Workshop/Sandbox does not become the owner of governed definitions.

### Notifications / visibility / recovery

APW-I06 composes existing visibility-projection, audit/export/recovery, diagnostics/support and UI shell surfaces. Durable source outcomes remain in their owner; notification cards/badges are reconstructable filtered projections.

### Automated play

APM-I01..I06 compose authority/control, Action/Event, downtime, combat, Adventure, Campaign membership, resource owners, visibility and recovery. Automation-run state is execution governance/provenance, not canonical game state.

## 9. Feature flags and fallback policy

Each major implementation family should be independently disableable without corrupting stored compatible data:

- Personal Home/workspace switching;
- async Action/GM inbox;
- Campaign Activity/downtime workspace;
- Creator Workshop/Sandbox;
- Storycraft foundation/library/inspiration/guidance/narrative/writing/reuse/Command Center;
- automated-run foundation;
- Cozy Solo;
- AutoGM Encounter;
- Connected Cozy;
- AutoGM Mini-Campaign;
- optional AI presentation/assistance;
- enhanced hybrid/recovery diagnostics.

Fallbacks:

- ordinary live Campaign play remains available if async surfaces are disabled;
- Personal-owned data remains accessible from owning screens if dashboards/Command Center are disabled;
- creator documents/history remain exportable/readable if advanced creator assistance is disabled;
- AutoGM/Cozy failures fall back to manual/ordinary play or safe pause;
- optional AI can be fully disabled with core workflows intact;
- blocking acceptance must be runnable without paid services.

Flags control product availability only; they never grant authority.

## 10. Deterministic fixture and validator program

Each implementation tranche requires focused deterministic fixtures during construction and a declared final gate at exact head.

Minimum cross-program blocking scenarios:

1. universal account switches Personal → Campaign → Session without role/authority bleed;
2. Player async Action disconnects, GM later resolves it, Player returns to one result;
3. duplicate async submit returns prior status and does not duplicate the Event;
4. stale Action/proposal cannot silently overwrite current state;
5. Campaign Activity resource reservation expires/refunds correctly;
6. hidden investigation/social/GM-only data does not leak through counts/search/notifications;
7. Personal creator material is independent from Campaign authority;
8. Workshop/Sandbox experimentation cannot mutate Campaign/global canonical truth;
9. creative `haunted lighthouse` proof completes Capture → Develop → Connect → Structure → Write → Check → Use → Reuse with explicit D18/D28 incorporation;
10. writing revisions/export are exact-revision and recoverable;
11. creator derivative lineage survives source drift without silent propagation;
12. Cozy Solo recovers exact-once progress and resources;
13. AutoGM encounter recovers without reroll/reseed/duplicate effects;
14. Connected Cozy preserves participant consent/authority and exact contribution accounting;
15. Mini-Campaign child completion advances its parent exactly once;
16. optional AI unavailable/illegal cannot alter mechanics or authority;
17. cross-device reconnect reauthorizes context and cannot restore revoked/hidden cache;
18. live → async → GM resolution → Player return → live resumes one Campaign/Event history;
19. mobile/keyboard/screen-reader/nonvisual paths expose equivalent state and recovery actions;
20. zero-paid-service validation passes.

Final product/package completion continues to use the governing self-hosted Windows + Linux + deterministic comparison policy unless an explicit bounded exception is approved.

## 11. Internal Alpha amendments

The implementation program should enter Internal Alpha incrementally rather than waiting for all 21 slices to land.

### Alpha milestone A — persistent personal/async foundation

APW-I01, APW-I02, APW-I03. Prove account/context switching plus delayed Player→GM→Player Action outcome.

### Alpha milestone B — between-session and creator foundation

APW-I04, CSW-I01, CSW-I02, APW-I05. Prove useful no-Campaign Personal value, Campaign Activity and safe reusable creation.

### Alpha milestone C — first creator/automated experiences

CSW-I03/I04, APM-I01/I02/I03. Prove Inspiration/Guided Creation, Cozy Solo and Single-Encounter AutoGM.

### Alpha milestone D — deep creator workspace

CSW-I05/I06/I07. Prove narrative planning, continuity, writing and reuse/remix.

### Alpha milestone E — integrated shell and connected automation

APW-I06, CSW-I08, APM-I04/I05/I06. Prove Command Center, Connected Cozy, Mini-Campaign and cross-mode recovery.

### Alpha milestone F — whole-system hybrid proof

APW-I07. Prove final live/async/creator/automated continuity on supported desktop/mobile/accessibility paths.

Tester distribution remains separately owner-gated; implementation acceptance does not automatically authorize distribution.

## 12. Compatibility and rollback

- No completed Stage A migration is rewritten.
- Existing public contracts are extended additively; compatibility adapters are preferred where old client/fixture shapes must coexist temporarily.
- Feature disablement must not delete valid persisted records.
- New projections may be rebuilt from authoritative data where designed; stored authoritative domain state is never rolled back merely to hide a feature.
- Failed migration deployment must use the tranche's explicit rollback/forward-fix plan and cannot erase accepted Event history.
- A successor regression is attributed to the successor until evidence proves a predecessor defect; completed Stage A milestones are not reopened by assumption.
- Every migration/contract version change is reflected in deterministic fixtures and recovery/version compatibility tests.

## 13. Completion evidence for application tranches

A future implementation slice may be claimed complete only when:

1. its exact application head is identified;
2. all declared slice fixtures/tests pass;
3. required migration/schema/contract compatibility checks pass;
4. hidden-information and authority boundaries pass;
5. accessibility/mobile/nonvisual acceptance relevant to the slice passes;
6. recovery/idempotency checks relevant to the slice pass;
7. exact-head repository-health passes;
8. the declared final platform gate passes when the tranche is product/package-affecting;
9. PR merge evidence exists;
10. canonical work state records `completed_verified` only after evidence inspection.

Artifact existence or a green partial check is never enough.

## 14. Roadmap activation recommendation

After APW-08 itself passes exact-head AIOC repository health and merges, perform a **separate state transition** that:

1. records APW-08 `completed_verified`;
2. closes the APW planning program `completed_verified`;
3. records the combined APW/APM/CSW design series as completed handoff authority;
4. updates the application roadmap from the stale APW-01 design selection to the new implementation sequence;
5. selects **APW-I01-attempt-001** in `cybalicistjt-stack/Multiversal-app` as `selected_not_started`;
6. grants only the bounded application implementation authority required for APW-I01;
7. leaves T04 owner-deferred until September, WP-011 dormant, DS-008 blocked and tester distribution/release/deployment unauthorized.

This separate transition is the explicit implementation activation. APW-08 design completion alone is not.

## 15. Stage A non-reopening rule

APW/APM/CSW are additive successor work over completed Stage A. A new failure does not invalidate prior Stage A completion unless fresh evidence independently demonstrates a predecessor regression. When a successor exposes such evidence, isolate and repair the minimal owning predecessor contract while preserving all unaffected completion evidence.

## 16. Final design-series completion gate

The APW/APM/CSW design series is complete when APW-08 is `completed_verified`, the APW program is closed, the roadmap and runtime selectors agree on the next application implementation item, and no implementation slice depends on an unstated authority, persistence, visibility, recovery, fallback or acceptance assumption.

The recommended next canonical work after closure is **APW-I01**. T04 cannot preempt it in August under the current owner deferral; WP-011 may still temporarily preempt if the required borrowed Mac environment becomes available.
