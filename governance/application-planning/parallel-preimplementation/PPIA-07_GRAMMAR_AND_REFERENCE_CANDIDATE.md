# PPIA-07 — Deterministic Rune Grammar & Reference Candidate

Status: **DESIGN CANDIDATE — grammar/reference milestone only**  
Work item: **PPIA-07 — Rune Construction RPG System**  
Verified foundation merge: `183d199d69f5cce121d4b971f33fe6c0145a6c45`

## What is source-grounded

The retained sources establish rune engraving, Scriptcraft/Sigilcrafting, modular overlays, shape/radius changes, symbolic/glyph logic structures, chained sequences, triggers, conditions, timing, synchronization, enchanting, failure/removal, Resonance, resistance/counterspell and magical-object context. They do **not** provide a canonical rune-atom catalog, connection grammar, rune-specific shaping syntax, arbitrary-construction cost formula or automatic spell-to-rune mapping.

Accordingly, the grammar in this milestone is a governed **proposal candidate**, not recovered source canon.

## Candidate design choice

The candidate uses a deliberately small **functional atom vocabulary** rather than turning spell names into runes:

- `SOURCE` — introduce/manifest a typed payload.
- `MOVE` — move/direct/redirect the active context.
- `SHAPE` — apply geometry/topology.
- `BIND` — attach/anchor/constrain.
- `CHANGE` — transform into a declared result.
- `SENSE` — detect/observe a typed property.
- `WARD` — oppose/block/mitigate a typed payload/effect.
- `LINK` — route/couple/share output.

This satisfies the owner-directed goal that a small number of basic runes can be reused in many ways. Typed payloads/modifiers remain references to owning vocabularies; a spell name is not automatically a rune.

## Four explicit connection types

- `>` — **THEN**: feed the left result/context into the right expression.
- `&` — **WITH**: explicit parallel/composite siblings.
- `@` — **WHEN**: left event/trigger gates the right expression.
- `?` — **IF**: left condition/result gates the right expression.

The source provides sequence/trigger/condition/composition precedent. The exact four tokens and grammar are proposal-stage design.

## Low-cognitive-burden parsing rule

There is **no implicit precedence** among the four connectors. Mixed connector types at the same nesting level are invalid unless parentheses make the grouping explicit. Same-connector chains evaluate left-to-right.

That means:

- `SOURCE[payload=force]>MOVE[direction=away]` is valid.
- `SOURCE[payload=force]>MOVE[direction=away]&WARD[payload=force]` is invalid because the parser refuses to guess.
- `(SOURCE[payload=force]>MOVE[direction=away])&WARD[payload=force]` is valid and explicit.

Every visual graph must have an equivalent ordered text serialization and must round-trip to the same typed AST.

## Modifier slots

The candidate provides typed modifier slots for payload, target, geometry, direction, range/area/duration references, timing, conditions, triggers, channels, anchors and transformation results. Numeric costs, mana, XP, charge, material and Resonance values are **not encoded into the syntax**. They remain external annotations/references until a later cost/balance contract is independently validated.

## Boundary rules

- `SOURCE`, `SHAPE`, `CHANGE`, `SENSE` and `WARD` require their declared core slots.
- Unknown atoms are rejected; spell/action names do not auto-promote.
- Mixed connectors require explicit grouping.
- Registry references resolve only inside the caller's permission scope.
- Setting-local magic remains setting-local without explicit promotion authority.
- Item inscription does not transfer Item Definition/instance ownership away from PPIA-03.
- Grammar validity does not guarantee resolution success or balance; counterspell/resistance/disruption remain external runtime/balance concerns.
- Authoritative writes use expected-version plus operation-id/idempotent recovery.

## Reference corpus

`PPIA-07_RUNE_REFERENCE_CORPUS_v0.1.0.json` contains **20 bounded cases** covering:

- simple source, move, shape, ward, sense, bind, change and link examples;
- trigger, condition, chained and parallel composition;
- inscription/item-bound handoff;
- missing-required-slot, unknown-atom and ungrouped-mixed-connector rejection;
- explicit grouping recovery;
- permission-filtered hidden references;
- countered/disrupted resolution;
- ambiguous authoritative-write recovery.

The examples are QA/design fixtures. Example payload IDs do not create new canonical spells or universal rune meanings.

## Complexity guidance

The builder may warn above six atoms or two nested groups and offer explanation/simplification help. These are **usability warnings only**, not parser hard caps or balance limits.

## What remains intentionally unresolved

This milestone does not finalize:

- whether the eight candidate atom IDs are the permanent vocabulary;
- the full payload/domain registry;
- numeric cost/mana/XP/material/charge/Resonance equations;
- balance bands or progression unlock prices;
- automatic conversion of existing spells;
- universalization of setting-local magic.

## Next bounded milestone

If this candidate passes exact-head validation and merges, define the **cost/complexity/stability and progression contract** against the verified grammar. That contract should use the 20 reference cases plus an expanded benchmark set to determine how construction complexity, execution context, resources, Resonance/risk, counterplay, crafting/inscription and unlock progression interact—without promising guaranteed balance and without silently inheriting source-specific numeric formulas.
