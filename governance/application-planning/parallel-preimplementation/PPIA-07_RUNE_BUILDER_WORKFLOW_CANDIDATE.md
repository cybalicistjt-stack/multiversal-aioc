# PPIA-07 — Integrated Rune Builder Workflow / Authoring Contract Candidate

Status: **IMPLEMENTATION-READY DESIGN CONTRACT CANDIDATE — not PPIA-07 completion**  
Work item: **PPIA-07 — Rune Construction RPG System**  
Verified input merges: foundation `183d199d69f5cce121d4b971f33fe6c0145a6c45`; grammar/reference `15202626a0ba96d7675ee4ab4cbec4923158cd63`; cost/stability/progression `210ca8f13eaba7c1ea295c280368c68a13a300f3`.

## Purpose

Integrate the verified PPIA-07 design layers into one end-to-end Rune Builder authoring and inspection contract before final Experience Specification/completion work. This milestone defines how users move through rune discovery, construction editing, topology/shaping, validation, SCI/CSL/resource previews, progression guidance, counterplay, inscription, runtime handoff, permissions, proposals, recovery and accessible operation.

It does **not** invent new source facts, promote proposal-stage rune mechanics to recovered canon, establish final power/balance, or activate application runtime.

## Verified inputs preserved

The workflow contract consumes without redefining:

- the retained PPIA-07 source/design foundation: 9 PDFs / 170 pages plus 4 structured CSVs / 2,225 rows, including 3 explicit rune-crafting records and 16 structured Scripts & Macros records;
- the verified 15-layer Rune Construction identity/state taxonomy;
- the verified proposal-stage grammar: 8 functional atoms, 4 explicit connectors, 12 validity rules and canonical linear serialization with no implicit mixed-connector precedence;
- all 20 `PPIA07-RC-*` grammar/reference cases;
- the verified cost/stability/progression contract: 4 SCI bands, 12 typed resource adapters, 4 CSL bands, 6 counterplay hooks, 4 proposal-stage progression bands;
- all 16 `PPIA07-CSP-*` deterministic/guardrail benchmarks.

## Integrated workflow set

The contract defines **16 workflows**:

1. Rune library, inspector and comparison.
2. Create a Rune Construction.
3. Edit atoms, modifiers and typed references.
4. Edit connection topology and grouping.
5. Edit shaping, targeting and scope.
6. Parse, validate, serialize and debug.
7. SCI, CSL and resource preview.
8. Progression guidance and adopted gating.
9. Counterplay and disruption inspection.
10. Apply or remove rune inscription/enchantment.
11. Prepared macro, ritual and cast execution handoff.
12. Campaign and Scene runtime handoff.
13. Permission-safe hidden reference handling.
14. Generated proposal review and governed acceptance.
15. Provenance, conflict, history and recovery.
16. Accessible visual and linear Rune Builder operation.

The workflow set is deliberately broader than the parser. A valid expression is only one input to authoring, resource, permission, ownership, progression, counterplay, recovery and accessibility behavior.

## Action contract

The workflow matrix defines **18 governed actions**. Exactly **7** are PPIA-07 authoritative mutations:

- create construction;
- edit atom/modifier;
- edit connection topology;
- edit shape/scope;
- apply inscription;
- remove inscription;
- accept a generated/imported proposal.

Every such mutation requires authorization, reference revalidation, `expected_version`, `operation_id`, and operation/current-version lookup before retrying an ambiguous response. The remaining actions are inspection, validation, preview, handoff, proposal generation, history/recovery or accessible projection operations.

## Cross-domain handoffs

The contract defines **10 explicit handoffs**:

- MV-IA-F002 — generic object browsing/inspection/provenance;
- PPIA-03 — Item Definition/instance ownership and item mutation;
- PPIA-08 — Campaign/Scene runtime instantiation and current state;
- PPIA-11 — final balance calibration;
- PPIA-12 — setting-local rule scope;
- MV-IA-F006/F007 and owning Action/Ability/magic rules — effect registries and authoritative resolution;
- MV-IA-F020 — permission/reveal filtering;
- MV-IA-F021 — recovery/idempotency;
- MV-IA-F022 — accessibility/adaptive interface;
- Screen Design V08 / SD-707 — Enchanting & Enhancement workbench conventions.

These handoffs prevent Rune Construction from absorbing ownership that belongs to Items, Campaign/Scene state, setting-local rules, core magic/action resolution or balance calibration.

## Structural complexity and stability remain separate from balance

The Rune Builder may display and explain SCI and CSL, but:

- SCI is not power or resource cost;
- CSL is not failure probability, damage or backlash;
- resource costs are typed owning-rule references, not a universal rune formula;
- unresolved required adapters are shown as unresolved and block authoritative execution/crafting where the owning rule requires them;
- final power/balance calibration remains PPIA-11 or separately adopted owning rules.

The UI must explain *why* SCI or CSL changed rather than presenting them as opaque scores.

## Permission behavior

Permission filtering occurs before resolving hidden payloads, targets, anchors, channels, inscriptions, constructions, labels, existence, counts, previews, diagnostics, exports, notifications or AI context. A structurally valid hidden reference can remain redacted/unresolved without leaking what it points to.

Cached, deep-linked and restored Rune Builder views reauthorize before showing restricted semantic data.

## Visual and nonvisual operation

A visual graph is never authoritative by itself. Every Rune Construction has a canonical ordered linear representation and equivalent typed AST. Required workflows support keyboard, touch, high-zoom/reflow and screen-reader operation. Drag, hover, color, animation and spatial memory are supplemental only.

Validation errors, SCI factors, CSL factors, unresolved resource adapters, permission state, progression guidance, provenance and recovery status must all have text/non-color representations.

## Proposal and provenance behavior

AI-generated, imported or suggested Rune Constructions remain proposals until explicit governed acceptance. Proposal generation does not mutate canonical content. Acceptance revalidates grammar, references, permissions, SCI/CSL/resource state and authority, then uses the normal mutation protocol.

The Scripts & Macros progression-cost conflict remains attributable. No workflow silently selects one source value, and setting-local magic cannot universalize by being referenced in a Rune Construction.

## Coverage lock for this milestone

`PPIA-07_RUNE_BUILDER_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json` must demonstrate non-empty coverage for:

- all 15 taxonomy layers;
- all 20 grammar/reference cases;
- all 16 cost/stability/progression benchmarks;
- all 18 action contracts;
- all 10 handoff contracts;
- all 16 workflows.

Any gap fails deterministic validation.

## What this milestone does not do

This milestone does not lock the eight atom IDs as final game canon, define a universal mana/material/charge/XP equation, invent a Resonance failure percentage, guarantee balance, convert the spell catalog to runes, resolve source progression conflicts, mutate application runtime, activate STAGE-A-A2, deploy/release, provide tester access, purchase services or use production credentials.

## Next bounded milestone

After exact-head validation and merge, create the **final PPIA-07 Rune Construction Experience Specification v1.0.0, acceptance/traceability matrix and deterministic completion contract**. That final package must decide which proposal-stage mechanics are implementation-ready design commitments, trace all verified foundation/grammar/cost/workflow evidence, preserve final-balance ownership with PPIA-11, and only then claim PPIA-07 `completed_verified` if every applicable gate passes.
