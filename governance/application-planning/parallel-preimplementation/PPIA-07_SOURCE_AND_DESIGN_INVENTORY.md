# PPIA-07 — Rune Construction Source & Design Inventory

Status: **FOUNDATION CANDIDATE — source/design inventory only**  
Work item: **PPIA-07 — Rune Construction RPG System**  
Transition anchor: `a7803f8438a837b741f78c875d7ec2e915d37a19`

## Purpose

Establish the source and governed-design boundary before defining a deterministic rune grammar. The owner-directed target is a compositional system built from **basic reusable runes, connection types, and shaping**, capable of producing many effects from a small vocabulary while remaining **fun and not too hard**. Those are governed design goals; the retained sources do **not** yet publish the corresponding atom catalog or grammar.

## Retained source boundary

The reviewed foundation boundary is **9 PDFs / 170 pages** from `MV_Master_01_Core.zip` (`c5732c5b4c3cdf5eca1d19eef7354289d1f92a87397b56aa7623b3f0a24177ec`). All 170 pages were rendered and visually reviewed; extracted text was used only as a search aid.

### Direct composition / enchanting authority — 3 PDFs / 77 pages
- `Scripts and Macros.PDF` — 27 pages. Scriptcraft, Sigilcrafting, spell overlays, shape/radius changes, chained spells, triggers, conditions, timing, synchronization, materials, progression and Resonance.
- `Crafting, repair, enchanting v2.PDF` — 38 pages. Universal crafting structure, enchanting, rune engraving, infusion, hybrid effects, crafting DCs, failure, removal/reversal, materials and workstations.
- `Magic charge holders.PDF` — 12 pages. Charges/capacity, magical containers, attunement/resonance, item upgrades, and explicit rings fitted with gemstones, symbols or runes representing origin/school.

### Core magic context — 4 PDFs / 66 pages
- `Magic rules.PDF` — 30 pages. Mana costs, spell levels, preparation/known limits, focus, resistance, counterspell, fatigue and Arcane Overreach.
- `Mana.PDF` — 3 pages. Mana pools, per-spell costs, reserve mana and Overreach.
- `Magic Schools and Spells.PDF` — 24 pages. Effect/school vocabulary and spell examples; **not** a rune catalog.
- `Abilities- Magic & Arcane Specializations.PDF` — 9 pages. Specialization/progression context and magic-item enchanting ownership.

### Risk / magical-object context — 2 PDFs / 27 pages
- `Chaos Magic.PDF` — 16 pages. Scope, specificity, instability and misfire patterns; useful risk precedent, not rune grammar.
- `Living Spellbooks.PDF` — 11 pages. Magical storage/casting-object context; not rune grammar.

## Structured source boundary

Four retained CSVs provide **2,225 rows** of structured context. They are not equal authority for rune mechanics.

- `Profession_Crafting_Abilities.csv` — 221 rows. Exactly **3 explicit rune records**: `Magical Item Enchanting Tree`, `Rune Carving Basics`, and `Perfect Rune Placement`.
- `Magic_Faction_Abilities.csv` — 118 rows. Exactly **16 records sourced from Scripts and Macros**, covering its progression and member abilities.
- `Magic_Spells.csv` — 385 rows. **0 explicit rune records**; effect/spell vocabulary context only.
- `Living_Spellbooks.csv` — 1,501 rows. Derived/item catalog context only; it is **not** canonical rune-grammar authority.

## Explicit source facts that matter

1. **Scripts are modular spell overlays.** They are pre-written magical instructions that alter a single spell; examples include damage type, delayed activation, secondary effects, and shape/radius.
2. **Sigilcrafting is explicitly symbolic/structural.** The source describes it as embedding symbols, glyphs, and logic structures into magical casting.
3. **Macros provide direct compositional precedent.** A macro is a magical construct encoded with conditions, activators, timing and spell sequence; it can chain spells, trigger conditionally and synchronize casters.
4. **Composition carries instability.** Multiple spell effects can create Resonance and misfire risk; source progression contains stability/mitigation abilities.
5. **Rune engraving exists in the enchanting rules.** The crafting source says an enchanter binds runes and manages charge capacity. `Rune Carving Basics` gives +2 Arcana when engraving runes and reduces the DC for basic rune engraving by 2. `Perfect Rune Placement` gives +1 to rune-carving rolls and rewards exceeding the crafting DC by 5+.
6. **Runes can be physical identifying/affinity marks.** Magic rings may contain gemstones, symbols or runes representing their origin or school of magic.
7. **Existing magic systems already have costs/counters.** Mana, charges, material cost, crafting time/DC, Resonance, resistance, counterspelling, fatigue, Overreach and disenchantment are all possible integration points—but foundation does not automatically inherit them as rune formulas.

## Important source gaps

The sources do **not** publish:
- a canonical list of basic rune atoms;
- rune-to-rune connection types;
- a deterministic connection/topology grammar;
- a rune-specific shaping syntax;
- a deterministic cost formula for arbitrary rune constructions;
- a universal mapping from spells to runes;
- a rule saying `rune == sigil`, `rune == script`, or `macro == rune construction`.

These gaps are design work, not permission to infer canon.

## Source conflict

`Scripts and Macros.PDF` contains a progression-cost conflict: its detailed progression and Appendix D publish different higher-tier unlock values. Existing structured source handling preserves that conflict and treats the detailed-tree values as the operational record. PPIA-07 must keep the conflict attributable rather than silently harmonizing it.

## Governed design direction

The source evidence supports using Scriptcraft/Sigilcrafting/Macros as the **closest precedent**, while the owner-directed rune system remains a distinct design. Foundation therefore separates:
- **source-explicit mechanics** — may be referenced directly;
- **governed owner intent** — basic runes, connection types, shaping, combinatorial reuse, low cognitive burden;
- **derived taxonomy** — implementation organization only;
- **future proposal** — any new atom vocabulary, grammar, cost equation, balance numbers or automatic conversions.

## 15-layer identity/state taxonomy

The foundation taxonomy organizes the future system into: rune atom; effect/payload; connection topology; shaping/geometry; target/range/area/scope; trigger/condition/timing; sequence/branch/composition; execution/casting context; resource/cost/capacity; stability/resonance/risk/failure; counterplay/resistance/disruption; progression/knowledge/unlock; crafting/inscription/container/item link; visibility/permission/accessibility; and provenance/conflict/version/recovery.

## UI/design precedent

`V08_Crafting.md` already defines **SD-707 — Enchanting & Enhancement** with base item, rune/ingredient selection, compatibility, predicted effects, risks and stability, plus Apply/Remove/Preview/Validate actions. Shared crafting behavior includes provenance, autosave, offline recovery, keyboard operation, screen-reader summaries, non-color indicators, responsive layouts and advisory-only AI suggestions. PPIA-07 should integrate with this surface instead of inventing a separate incompatible crafting UI.

## Foundation invariants

- A spell name is not automatically a rune.
- A glyph, sigil, script and rune may relate, but co-occurrence does not prove identity.
- Unknown grammar remains unknown until explicitly designed and accepted.
- Source-specific XP, mana, material or Resonance values do not automatically become universal rune formulas.
- PPIA-03 retains Item Definition/instance ownership; PPIA-07 owns rune-extension semantics.
- PPIA-12 retains setting-local scope; setting-specific magic cannot silently universalize.
- PPIA-11 remains the later balance-calibration authority; PPIA-07 may build benchmarks but cannot promise guaranteed balance.
- Hidden facts must be permission-filtered before search, counts, exports, diagnostics, notifications or AI context.
- Visual topology/shaping must always have a keyboard/screen-reader-usable ordered textual representation.
- AI/generated constructions are proposals until accepted with provenance.
- Authoritative mutations use expected-version plus operation-id/idempotent recovery patterns.

## What this milestone does not do

It does **not** choose the basic rune vocabulary, define the final connection types, define shaping syntax, set a cost equation, convert the spell catalog into runes, balance the system, activate STAGE-A-A2, mutate application runtime, or authorize release/deployment/tester/paid/credential operations.

## Next bounded milestone

Define a **deterministic Rune Construction grammar candidate and bounded reference corpus**: a deliberately small atom vocabulary, explicit connection types, shaping/modifier slots, validity rules, parse/evaluation order, and worked constructions that can be explained linearly. Every new mechanic must be marked as source-derived, owner-directed, or proposal, and no candidate cost/balance rule may be promoted without its own evidence and acceptance tests.
