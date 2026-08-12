# PPIA-15 Foundation — Existing Test Corpus and Coverage-Gap Inventory

**Work item:** PPIA-15 — Internal Alpha Test Content Expansion  
**Milestone:** Foundation / Existing Test Corpus and Coverage-Gap Inventory  
**Status:** FOUNDATION CANDIDATE — NOT PPIA-15 COMPLETION  
**Authority:** current canonical repository evidence and completed_verified owning-domain contracts

## 1. Purpose

PPIA-15 expands the Internal Alpha regression scenario set without padding counts by cloning cases that already exist. This Foundation establishes the inherited test baseline, exact-alias and semantic nonduplication rules, awkward-case taxonomy, gap matrix, deterministic oracle model, fixture isolation rules and an initial synthetic/noncanonical reference corpus before the expanded scenario library is authored.

The canonical completion gate remains: **expanded nonduplicative Internal Alpha regression scenario set covering awkward permission, conflict, recovery, scale, accessibility, mobile and object-edge cases**.

## 2. Existing test baseline

The verified inherited baseline contains four principal deterministic dependency corpora plus the bounded IA-D09 release fixture catalog:

- **IA-D09:** 24 bounded release-design fixtures, `IA09-FX-001..024`.
- **PPIA-09:** 36 Investigation reference cases, including 24 preserved F011 fixtures and 12 PPIA-09 additions.
- **PPIA-10:** 90 Relationship/Social/Faction resolved cases, including 72 imported F009/F010/F016 fixtures and 18 PPIA-10 additions.
- **PPIA-11:** 42 Encounter Lab resolved cases, including 18 noncanonical benchmark methodology fixtures and 24 local integration/recovery/privacy/accessibility/calibration cases.
- **PPIA-14:** 108 effective Error/Recovery/Permission cases: 32 Foundation + 40 Microcopy IAR + 36 integrated workflow cases.

After exact packaging aliases are collapsed, these surfaces contain **300 primary distinct case records**. This count is only a stable-record inventory. It does not claim that all 300 are semantically unique.

### Exact duplicate packaging that must not inflate coverage

The Stage A Tester / Reference Campaign Kit contains 24 scripted journeys mapped exactly one-to-one to `IA09-FX-001..024`. The Internal Alpha Tester Package also contains all 24 IA-D09 scripted scenarios and expected outcomes. Those two packages are portable/tester-facing representations of the same IA-D09 baseline, not 48 additional scenarios.

The Glass Harbor Incident / Meridian Testbed remains a useful deterministic portable fixture because it gives those 24 cases stable synthetic records, reset state and role profiles, but PPIA-15 must not count packaging as new coverage.

## 3. Supporting completed test surfaces

PPIA-15's declared dependencies remain PPIA-09, PPIA-10, PPIA-11 and PPIA-14. Completed object-domain PPIA packages are nevertheless valid secondary grounding for named object-edge cases and do not become new dependencies:

- PPIA-03 supplies Definition/Asset-instance separation, ownership/custody/control, transfer, expected-version concurrency, ambiguous-network recovery and accessible inventory interaction.
- PPIA-04 supplies Vehicle Definition/instance, ownership/custody/control/access/crew/passenger/cargo separation, atomic operation/recovery and compact/mobile/nonvisual operation paths.
- PPIA-05 supplies unusual Species/Form morphology, source-unspecified anatomy/compatibility staying unknown, Adaptation semantics and accessible nonvisual morphology/form interaction.
- PPIA-07 supplies deterministic Rune construction/crafting, proposal/approval, blind GM adjudication, offline-draft boundaries and explicit no-fabricated-completion behavior.
- PPIA-08 supplies Campaign-local content, versioned authoring, hidden state, live-session placement and current-version/recovery boundaries.

PPIA-11 also retains the 8D-007 Golden Test Corpus & Balance Harness: 20 source datasets / 19,199 promoted records, 36 golden fixtures, 24 deterministic scenarios / 72 executions, 36 non-destructive recommendations and seven mutation-sensitivity cases. This is supporting test evidence, not an additional PPIA-15 reference-case schema.

## 4. Nonduplication standard

A new scenario is **not** additive merely because it has a new ID or title. It must change at least one material dimension that can change the safe oracle:

- actor role or authority/entitlement state;
- object identity, ownership or Definition/instance state;
- timing, simultaneity or version/concurrency state;
- failure, ambiguity or recovery path;
- device, interaction or accessibility mode;
- bounded scale/density;
- cross-domain authority/provenance composition.

Exact aliases and execution wrappers add zero scenario count. A cross-domain composition can be new when the combined risk is not proven by its component tests—for example reveal + revocation, vehicle transfer + stale version, or approval + reconnect.

If the changed dimension does not change what is authoritative, visible, recoverable or prohibited, the proposal is presumptively duplicate and should reference the inherited case instead.

## 5. Awkward-case taxonomy

The Foundation defines eight regression families:

1. permission / hidden state;
2. conflict / concurrency;
3. recovery / ambiguous status;
4. scale / density;
5. accessibility / nonvisual;
6. mobile / touch;
7. object identity / edge behavior;
8. cross-domain authority / provenance.

It also locks 18 owner-selected awkward families as `P15-AWK-001..018`:

- simultaneous selection;
- mid-session reveals;
- entitlement loss;
- GM modifications;
- duplicate-name objects;
- version conflict;
- Campaign-local override;
- source-only objects;
- vehicle transfer;
- relationship secret reveal;
- interrupted crafting;
- reconnect during approval;
- large inventories;
- dense creatures;
- unusual species;
- mobile-only flows;
- keyboard/accessibility flows;
- offline/read-only transitions.

The exact nine PPIA-14/F025 actor IDs, twenty contexts and seven delivery channels are retained as test dimensions. Device, interaction, connection and accessibility modes are orthogonal test dimensions rather than new permission roles.

## 6. Coverage-gap result

The 18 required families resolve to:

- **7 direct gaps** with no existing direct awkward proof;
- **10 partial awkward variants** where baseline behavior exists but the named timing/composition/device/scale edge is not yet proven;
- **1 baseline already covered and protected from cloning**: ordinary GM modification.

The baseline GM-modification cases are IA09-FX-003 and PPIA-07 blind `modify-and-approve`. PPIA-15 should only add a GM-modification case when it combines with an unproven edge such as stale version, reconnect or hidden-state change.

Direct gaps include simultaneous selection, duplicate-name runtime identity, vehicle relation transfer, interrupted crafting phase recovery, large inventories, dense creatures and unusual-species awkward flow. Partial gaps include mid-session reveal, entitlement loss, version conflict, inherited-change/Campaign-local override, source-only objects, relationship-secret reveal, reconnect during approval, mobile-only, composed keyboard/accessibility and offline/read-only cache/reconnect behavior.

## 7. Deterministic oracle model

Every expanded case must bind:

- its awkward-family ID(s);
- nearest inherited anchor(s);
- the material differential that makes it additive;
- exact synthetic fixture state;
- actor role, context, device and interaction mode;
- authority/entitlement precondition;
- operation/read phase;
- expected authoritative outcome;
- expected visible and nonvisual projections;
- expected recovery/conflict state;
- expected provenance;
- forbidden outcomes.

The oracle must use governing-source behavior only. When upstream authority does not define an outcome, the correct deterministic result is explicit unsupported/indeterminate behavior—not a guessed rule.

Key inherited invariants remain blocking:

- permission/entitlement filtering before protected resolution and every derivative;
- hidden/missing external equivalence when existence is protected;
- local draft, save intent, authoritative command, accepted durable Event and derived projection are distinct;
- `status-unknown` is not failure;
- accepted Event + projection lag is not unsuccessful command;
- no blind retry of ambiguous mutation;
- no offline fabricated canonical Event;
- no silent last-write-wins;
- no AI decision authority;
- PPIA-11 never certifies balanced/fair/safe/winnable/optimal/guaranteed outcomes.

## 8. Scale fixture rule

Scale/density tests use explicit deterministic **case-local** fixture counts. This Foundation includes a 512-record synthetic inventory fixture and a 128-record synthetic Creature/NPC fixture to make initial cases reproducible. Those counts are QA inputs only. They are **not** supported-capacity, performance, release or product promises.

## 9. Accessibility and mobile rule

PPIA-15 inherits keyboard, touch, screen-reader, mobile single-focus, high-zoom/reflow, reduced-motion, noncolor, meaning-not-icon-only, required-recovery-not-transient-only and visual/nonvisual safe semantic parity requirements.

An accessibility/mobile expansion must prove an awkward workflow, not just the basic smoke path at another viewport. For example, keyboard-only version-conflict recovery and phone-only one-focus-at-a-time conflict review are additive; another keyboard replay of the ordinary first playable loop is not.

## 10. Initial Foundation reference corpus

`PPIA-15_FOUNDATION_REFERENCE_CASES_v0.1.0.json` establishes **32 synthetic noncanonical Foundation cases**. They cover:

- simultaneous same-object and duplicate-name targeting;
- live clue reveal and nonvisual reveal update;
- entitlement-loss cache purge;
- stale GM modification;
- duplicate-name stable identity;
- two-editor version conflict;
- Campaign-local override against inherited Definition change;
- source-only Item selection without silent instance creation;
- Vehicle ownership transfer without collapsing control/crew/cargo relations;
- bounded relationship-secret reveal and revocation;
- crafting interruption at local-draft and post-submission/preapproval boundaries;
- reconnect after approval acceptance with projection lag;
- 512-record inventory and 128-record Creature/NPC bounded stress fixtures;
- unusual nonhuman morphology without human defaults;
- phone-only conflict review;
- keyboard-only conflict recovery;
- offline/read-only cached source browsing and revoked-cache reconnect;
- status-unknown conflict recovery;
- accepted reveal Event + projection lag;
- F024 source-gap behavior.

These cases are design-time QA references, not executed candidate evidence and not PPIA-15 completion.

## 11. F024 / source-gap boundary

`P15-GAP-001` inherits `P14-GAP-001 / P13-GAP-001`: MV-IA-F024 Pack Lifecycle / Canonical Content Registry remains unresolved upstream authority. PPIA-15 may test that unsupported behavior remains explicit, but it may not invent install/activate/update/remove states, permissions, operations or expected results.

## 12. Nonactivation boundary

This Foundation does not activate or authorize:

- application runtime;
- STAGE-A-A2;
- tester access;
- Internal Alpha release;
- deployment/public release;
- paid services;
- production credentials;
- real-user data collection;
- unsupported canonical promotion.

## 13. Next milestone after verified merge

After this Foundation exact head passes its dedicated hosted gate and all applicable regressions, and the PR merges, the next bounded PPIA-15 milestone is **Expanded Regression Scenario Library / Inspector-Action-Reference Contracts**. That milestone should turn the gap matrix into the stable nonduplicate scenario library and trace each additive case to its inherited anchors, governed actions/projections and deterministic oracle without claiming final PPIA-15 completion.
