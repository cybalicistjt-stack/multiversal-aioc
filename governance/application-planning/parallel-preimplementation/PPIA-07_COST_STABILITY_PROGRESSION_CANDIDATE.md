# PPIA-07 — Cost, Complexity, Stability & Progression Candidate

Status: **DESIGN CANDIDATE — not final balance**  
Work item: **PPIA-07 — Rune Construction RPG System**  
Verified grammar/reference merge: `15202626a0ba96d7675ee4ab4cbec4923158cd63`

## Purpose

Turn the verified eight-atom/four-connector Rune Construction grammar into an explainable gameplay-facing contract for complexity, external resource inputs, structural stability/risk, counterplay, inscription/crafting and progression **without pretending the retained sources contain a universal arbitrary-rune cost equation or final balance table**.

## Four separate axes

The candidate deliberately keeps four questions separate:

1. **How hard is the construction to understand?** → Structural Complexity Index (SCI).
2. **What resources does the owning rule require?** → typed resource adapters, not one rune-wide equation.
3. **How much composition-stability attention does the structure warrant?** → Composition Stability Load (CSL), informed by Scripts/Macros Resonance precedent.
4. **How powerful/balanced is the result in play?** → later calibration, ultimately owned by PPIA-11 and adopted runtime rules.

A higher SCI does not automatically mean greater power, resource cost or failure chance. A higher CSL is not a percentage chance to fail and does not create automatic backlash damage.

## Structural Complexity Index

The proposal-stage SCI is deterministic and intended for explainability/usability:

`SCI = atom_count + connector_points + group_nesting_points + modifier_density_points`

Connector points are THEN=1, WITH=2, WHEN=2, IF=2. Group nesting adds two points for each explicit depth above one. Optional modifiers add one point per two non-required modifiers, rounded up.

Bands are simple (1–3), standard (4–6), advanced (7–10), and expert (11+). The previously verified builder warnings above six atoms or group depth two remain warnings, not parser caps or balance limits.

## Resource adapters

The Rune system asks the owning rules for typed resource inputs such as mana, charges, materials, time, crafting DC, capacity, fatigue, Overreach, Resonance handling, resistance/counterspell and progression references. Each adapter is `not_applicable`, `unresolved`, or `resolved`.

When an owning rule declares an adapter required, an authoritative execution/crafting operation cannot invent a missing numeric default. Source-specific values remain scoped to their source/owning system rather than being repriced through a universal rune formula.

## Composition Stability Load

The proposal-stage CSL is a structural warning signal:

`CSL = WITH + WHEN + IF + extra LINK + extra payload domains + depth above two + prepared-macro context`

Bands are baseline (0), watch (1–2), strained (3–4), and high-attention (5+). This gives the builder an explainable reason to surface stability review and mitigation/counterplay information while preserving that actual Resonance effects, failure chances, backlash and encounter balance require adopted rules or later PPIA-11 calibration.

## Counterplay and crafting

The contract exports hooks for recognition, resistance, counterspell/disruption, severing LINK channels, disabling triggers, and dispelling/removing persistent inscriptions. It does not redefine those owning systems.

For inscription/item-bound use, PPIA-03 retains Item Definition/instance ownership. PPIA-07 supplies the rune-extension construction, SCI/CSL, compatibility/resource adapter state, predicted effect summary, provenance/version and expected-version/operation-id recovery contract. The surface remains aligned with V08 / SD-707 Enchanting & Enhancement.

## Progression

A four-band proposal supports the owner's low-cognitive-burden goal without silently importing source XP prices:

- **Band 0 — literacy:** single atoms and inspect/validate/explain.
- **Band 1 — composition:** small sequential constructions, shaping, movement, binding and basic inscription.
- **Band 2 — logic:** explicit grouping, WITH/WHEN/IF and prepared logic.
- **Band 3 — architecture:** advanced/expert structures and synchronization/LINK-heavy constructions.

The recommended minimum band starts from SCI, escalates WHEN/IF and prepared macros to at least band 2, and escalates two or more LINK atoms to band 3. This is a candidate teachability/unlock contract, not a silently chosen Scripts & Macros XP price. The known source progression-price conflict remains provenance-visible.

## Deterministic benchmark set

`PPIA-07_COST_STABILITY_PROGRESSION_BENCHMARKS_v0.1.0.json` contains 16 cases: nine deterministic metric fixtures spanning every SCI band and progression band plus seven adapter/permission/counterplay/recovery/invalid-grammar guardrails. The validator recomputes SCI, CSL and recommended progression band from the verified grammar instead of trusting hand-entered values.

## Boundaries preserved

- No universal mana/material/charge/XP formula is created.
- No final power formula, failure table or guaranteed balance claim is created.
- Spells remain typed effect references, not automatic rune atoms.
- Setting-local magic remains setting-local without explicit promotion authority.
- Hidden facts are permission-filtered before labels, external resource values, previews, exports, diagnostics or AI context.
- Ambiguous authoritative writes use expected-version plus operation-id recovery and do not duplicate inscriptions or resource consumption.
- Visual topology always has an equivalent linear/nonvisual representation.

## Next bounded milestone

After exact-head validation and merge, define the **PPIA-07 integrated Rune Builder workflow/authoring contract** across library/inspection, construction editing, shaping/topology, cost/stability preview, progression gating, counterplay preview, inscription/enchanting, campaign/runtime handoff, permission filtering, recovery and accessibility. That milestone should exercise the verified 20 grammar cases plus the 16 cost/stability/progression benchmarks before final PPIA-07 experience/completion work.
