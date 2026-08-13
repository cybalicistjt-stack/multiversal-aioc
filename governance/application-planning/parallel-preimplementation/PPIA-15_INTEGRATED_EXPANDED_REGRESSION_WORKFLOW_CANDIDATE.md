# PPIA-15 Integrated Expanded Regression Workflows / Traceability

**Work item:** PPIA-15 — Internal Alpha Test Content Expansion  
**Milestone:** Integrated Expanded Regression Workflows / Traceability  
**Status:** candidate  
**Classification:** synthetic, noncanonical QA/reference material  
**Canonical game content:** no

## Purpose

This milestone composes the verified PPIA-15 Foundation and Expanded Regression Inspector-Action-Reference contracts into end-to-end deterministic regression workflows. It expands integration coverage without cloning already-sufficient inherited tests and without creating application runtime authority.

The verified predecessor surface is retained unchanged:

- Foundation exact head `d876093989e656d3cf8366c19755295ef0f785e8`, 62/62 hosted workflows, run `31652241636`, PR #286, merge `a1f6b7380a07e65469ba8072e8aa4135d7b1e42f`;
- Expanded Regression IAR exact head `94029c704fa097f99440a58a64c4293d52b4ad36`, 63/63 hosted workflows, run `31653764114`, successor-safe transition run `31653764056`, PR #287, merge `740683e33ff6e3a0b1a8672c06fbbf9d87fa3bf5`.

## Integrated surface

The package defines **18 integrated workflows**, exactly one primary workflow for each of the **18 required awkward families**. The workflows compose all **24 stable scenario contracts**, **12 Inspector projection groups**, **20 action/reference contracts**, and **12 cross-domain authority/presentation handoffs**.

All **32 Foundation cases** and **40 IAR cases** are assigned **exactly once** across the integrated workflows. Eighteen new synthetic noncanonical integrated cases are added only where end-to-end composition changes what must be proven. The effective PPIA-15 reference corpus at this milestone is therefore **90 cases** rather than an inflated duplicate count.

## Deterministic workflow order

Every integrated workflow follows the same governing order unless its owning domain resolves earlier:

1. establish case-local synthetic fixture and authority inputs;
2. resolve current actor, permission, entitlement, and visibility;
3. bind stable identity and owning domain before display-name reasoning or derivatives;
4. obtain or confirm authoritative state from the owning domain;
5. apply hidden-information and minimum-disclosure reduction;
6. derive the PPIA-15 Inspector projection;
7. expose only governed read actions or presentations of already-existing upstream commands;
8. execute or observe a scenario-specific external Event only when its owning domain authorizes it;
9. handle conflict, status, projection lag, or offline transition without inventing authority;
10. reauthorize and reproject after any authority change;
11. compare visual, nonvisual, mobile, keyboard, touch, noncolor, high-zoom, and reduced-motion semantics at the same disclosure ceiling where applicable;
12. assert the deterministic authoritative/projection/action/recovery oracle and forbidden outcomes;
13. record case-local provenance plus explicit no-activation assertions.

## Cross-domain handoffs

The package keeps authority in the completed owning contracts:

- PPIA-03: stable object identity, Definition/instance separation, expected version, inventory/object mutation authority;
- PPIA-09: investigation truth/belief/knowledge/reveal audience and reveal Events;
- PPIA-10: relationship secret truth, audience, entitlement/revocation, social mutation authority;
- PPIA-07: construction/crafting proposals, approvals, costs, modify-and-approve semantics;
- PPIA-14: safe error/recovery/status/conflict presentation, including status-unknown and projection lag;
- PPIA-08: Campaign-local override scope and provenance;
- PPIA-04: Vehicle ownership/custody/control/access/crew/passenger/cargo relation authority;
- PPIA-11: uncertainty-bounded encounter analysis without false balance guarantees;
- PPIA-05/PPIA-06: known/unknown Species/Form morphology and appearance semantics;
- PPIA-14 presentation/accessibility: semantic parity without creating authority;
- owning domain plus PPIA-14 recovery: offline/read-only/reconnect status resolution;
- unresolved MV-IA-F024 source authority: Pack lifecycle behavior remains unsupported.

PPIA-15 itself creates no command, mutation protocol, entitlement, reveal decision, approval decision, conflict resolution, canonical-content rule, or Pack lifecycle rule.

## Locked safety and provenance behavior

Permission and entitlement filtering occur before protected derivatives and before action availability. Hidden and missing remain externally equivalent whenever existence is protected. Stable IDs control identity; display names cannot merge or retarget objects.

`status-unknown` is not failure. An accepted durable Event remains distinct from a lagging derived projection. Offline/local state is not authoritative mutation. Blind ambiguous mutation retry remains forbidden; any retry presentation requires the owning domain's compatible operation/idempotency proof.

The 512-record inventory and 128-record Creature/NPC fixtures remain deterministic **case-local QA fixture sizes only**. They do not establish supported product capacity, performance, release, or scale promises.

PPIA-11 encounter analysis remains uncertainty-bounded. No PPIA-15 workflow may certify an encounter as balanced, fair, safe, winnable, optimal, or guaranteed.

Ordinary GM modification remains a protected inherited baseline with **zero standalone PPIA-15 clones**. `P15-SCN-005` is additive only because stale-version conflict changes the safe oracle.

`P15-GAP-001` / inherited `P14-GAP-001` / `P13-GAP-001` / **MV-IA-F024** remains open. The integrated source-gap workflow returns `indeterminate-blocked-source-gap / unsupported`; it does not invent install, activate, update, remove, promotion, or canonical Pack lifecycle behavior.

## Completion boundary

This package is **not PPIA-15 completion**. It is a bounded intermediate milestone. PPIA-15 remains active until a separate completion/evidence-closure operation verifies the tranche completion gate against the full retained corpus.

No application runtime, STAGE-A-A2, tester access, release, deployment, paid service, production credential, or unsupported canonical promotion is activated by this milestone.
