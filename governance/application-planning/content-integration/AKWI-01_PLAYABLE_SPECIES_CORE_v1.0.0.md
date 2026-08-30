# AKWI-01 — Playable Species Core

Version: 1.0.0  
Status: IMPLEMENTATION AUTHORIZED / IN PROGRESS  
Owner authority: John Brandon Turner  
Authorized: 2026-08-30  
Application repository: `cybalicistjt-stack/Multiversal-app`  
Application branch: `integration/akwi-01-playable-species-core`  
Application baseline: `88cb2b44f9aef71844ddf0ea6b06651f1f4d8b01`  
AIOC repository: `cybalicistjt-stack/multiversal-aioc`  
AIOC branch: `integration/akwi-01-playable-species-core`  
AIOC baseline: `60f75d15eb7d197dde2abffccb7a071cbea321f5`

## 1. Objective

Integrate Akwi as a governed playable Species using the existing Universal Object and Character Creation architecture without creating Akwi-specific UI, a parallel character system, a parallel rules engine, or unsupported canonical facts.

AKWI-01 is a bounded content/rules-integration tranche. It establishes reusable Akwi Species truth, fixed creation grants, deterministic rule semantics for the owner-approved Akwi sensory and Burst behavior, provenance/visibility handling, generic A2 Species presentation, generic A4 `species-or-form` selection, and focused acceptance evidence.

## 2. Source basis and evidence classes

The tranche is grounded in three supplied source families:

1. `Akwi Concept Design.mht` — original concept/source conversation and biological/mechanical source assertions.
2. `akwi_game_integration_package_v0.1.zip` — normalized integration package, including Species master, Species features, Character Creation mappings, mechanics proposals, provenance/truth register, visibility projection, and owner-decision register.
3. `akwi_npc_suite_400.csv` — downstream NPC corpus. The copy packaged in the integration ZIP was verified byte-for-byte identical to the separately supplied CSV.

Every implemented claim MUST preserve its evidence class:

- `SOURCE_ESTABLISHED`: directly supported by the original source or normalized source-backed integration records.
- `OWNER_APPROVED`: supplied or explicitly resolved by the Owner in the 2026-08-30 AKWI-01 conversation.
- `IMPLEMENTATION_POLICY`: deterministic game-system interpretation needed to make an approved concept playable where the source does not provide exact system math.
- `PROPOSED` / `UNKNOWN`: retained as noncanonical/nonexecuting unless separately approved.

Implementation policy MUST NOT be rewritten as source canon.

## 3. Owner-approved AKWI-01 rulings

### 3.1 Hearing

- Preserve the source-established statement that Akwi auditory acuity is approximately 20% better than a human baseline.
- Do not convert that percentage into a universal die modifier, DC modifier, or bonus.
- A rules profile may translate the 20% only when it exposes an appropriate auditory quantity or comparison.

### 3.2 Magnetic field orientation

Owner-approved behavior:

- Akwi perceive magnetic-field information as a weak environmental sense.
- On the Akwi homeworld, the naturally shifting field is experienced more like a changing ocean and does not provide reliable intrinsic directional navigation.
- On a planet with a sufficiently stable magnetic field at least as strong as Earth's field, an Akwi can determine direction magnetically if the Akwi stops, becomes calm/still enough to focus, and meaningful local interference is absent.
- The sense is weak and deliberate in this navigational use. It is not passive perfect-compass knowledge, radar, creature detection, dimensional sensing, or a replacement for ordinary navigation.
- Fields weaker than the Earth-minimum threshold, unstable fields, and meaningful electromagnetic interference do not grant reliable directional resolution.

### 3.3 Pressure and airflow sense

- Passive awareness of meaningful nearby airflow and pressure changes.
- Not echolocation and not a replacement for vision.
- Difficult, subtle, noisy, or obstructed cases may require a rules-profile-specific check rather than creating universal numeric mechanics in the Species record.

### 3.4 Spring-Leg Anatomy

- Akwi receive an explicit enhanced-jumping / mobility capability from their biological Spring-Leg Anatomy.
- Do not invent an exact jump-distance, speed, or multiplier unless the active rules profile exposes a governing movement quantity and supplies the translation rule.

### 3.5 Burst usefulness, overuse, recovery, exhaustion, and injury risk

Source-established biological truths retained by AKWI-01:

- a fully recovered Akwi has two Burst reserves;
- only one reserve may be active at a time;
- the reserves cannot be combined into one super-discharge;
- one active reserve supports one Burst discharge event;
- an activated reserve may be held for approximately one minute; expiry consumes/wastes that reserve;
- recovery requires rest/inactivity and sufficient nourishment; sleep plus a large meal is the ideal recovery condition;
- ideal full recovery is approximately two days;
- the source/integration package associates recovery burden with an approximately 3:1 relationship to Burst use.

Owner-approved gameplay requirement:

- normal use must be frequent enough that choosing Akwi is mechanically meaningful;
- there must be a safe-use band with no exhaustion;
- continued use beyond that band must progressively add exhaustion/strain;
- exceeding the 3:1 use-to-recovery boundary must produce more severe exhaustion and injury risk.

AKWI-01 deterministic implementation policy:

1. **Safe band — uses 1–2 in a recovery cycle.** These are the two ordinary biological reserves. They add no Burst-specific exhaustion.
2. **Strain band — forced uses 3–6 before full recovery.** These represent emergency overuse after normal reserves are depleted. Each forced use increases `burstStrainLevel` by one step. This band permits heroic/emergency play but marks accumulating physiological exhaustion.
3. **Overload band — use 7 and above before full recovery.** Seven uses exceed a 3:1 ratio against the normal fully recovered capacity of two reserves. Every use in this band sets `severeExhaustion=true` and `injuryRisk=true`, in addition to continued strain accumulation.
4. **No invented universal injury roll.** AKWI-01 records deterministic injury risk, but the current application has no authoritative generic exhaustion/injury resolution engine. A future rules profile/runtime may resolve that risk using its own governed condition/injury mechanics.
5. **No infinite-free pushing.** A forced Burst is never treated as a normal restored reserve. It increases the tracked cycle-use count and strain. A rules profile may prohibit further forced Burst when its generic incapacitation/injury rules say the character cannot exert themselves.
6. **Recovery-cycle reset.** A qualifying full-recovery event resets cycle Burst uses and Burst strain and restores the two normal reserves. The source-established ideal full-recovery reference is approximately 48 hours with safe rest/sleep and substantial nourishment. Nonideal recovery may take longer according to the active rules profile/GM adjudication.
7. **Partial recovery is not fabricated in AKWI-01.** No unsupported fixed 24-hour one-reserve rule or percentage formula is canonized. Future rules profiles may define partial recovery while preserving the source/owner constraints.

This balance intentionally gives an Akwi two meaningful Burst uses without penalty, four increasingly costly emergency pushes, and a clearly dangerous overload threshold beyond six uses without full recovery.

## 4. Required reusable Akwi content

AKWI-01 SHALL create a stable `species.akwi` Species definition and reusable fixed Species feature/grant records sufficient to represent the approved core. The integration package's existing stable feature identifiers should be preserved where compatible, including at minimum:

- `feature.akwi.aural_complex`
- `feature.akwi.hearing_acuity`
- `feature.akwi.magnetic_sense`
- `feature.akwi.pressure_flow_sense`
- `feature.akwi.spring_legs`
- `feature.akwi.temperature_limits`
- `feature.akwi.burst_reserves`
- `feature.akwi.active_burst`
- `feature.akwi.burst_duration`
- `feature.akwi.burst_discharge`
- `feature.akwi.burst_recovery`

Additional source-established feature rows from the 17-row integration package may be included when they remain fixed creation grants and do not require unresolved P1/P2 mechanics.

Proposed example actions such as specific Burst movement/break/endure implementations MUST remain proposals unless the source/owner decision already establishes their semantics independent of a rules profile.

## 5. Character Creation contract

- Akwi SHALL be available through the existing A4 single-selection `species-or-form` stage.
- Selecting Akwi SHALL store a stable Species reference/receipt and remain nonauthoritative draft intent until normal A4 validation/commit boundaries are satisfied.
- Akwi has no approved alternate Form, lineage, subspecies, or optional Species-choice branch in AKWI-01. Do not fabricate one.
- Fixed Species grants SHALL be represented as reusable references with grant reason and source/provenance references rather than copying free-form mechanics onto each Character.
- Background, language, culture, profession, equipment, and upbringing are not automatically inherited biology and are outside the fixed Akwi Species grant bundle unless separately source-established and approved.

## 6. A2 presentation and discoverability

- Akwi SHALL use generic `P-A2-SPECIES` presentation.
- Akwi-specific UI is prohibited unless a missing field is demonstrably generic Species capability that should be added for all Species.
- The Species object should expose approved player-visible overview, biology/appearance, culture/society links where approved, and reusable traits/abilities.
- Unknown or unresolved biology must remain unknown; do not default missing Akwi facts to human biology.

## 7. Runtime boundary

At authorization time, `packages/rules-runtime` is a placeholder scaffold and the current A4 integration flow proves governed selection intent but does not execute a concrete authoritative Species calculation/exhaustion/injury engine.

Therefore AKWI-01 SHALL NOT claim or fake live engine execution that does not exist.

AKWI-01 SHALL instead:

- encode deterministic reusable Species/grant semantics through current contracts and fixtures;
- encode Burst state/balance as a deterministic generic contract/fixture suitable for later runtime consumption;
- add focused tests proving content identity, projection, selection, grant intent, provenance, and deterministic Burst-band classification;
- preserve a clean future seam for the generic rules runtime to execute the same contract when that subsystem becomes authoritative.

Any extension required for Burst MUST be generic and reusable, not an Akwi-only hidden rules subsystem.

## 8. Visibility and provenance

- Player-visible Species truths may be projected through normal authorization/entitlement boundaries.
- Proposed authoring notes, unresolved mechanics, hidden weaknesses, private Character facts, GM-only facts, protected counts, and unrevealed biology must not leak through search, facets, relationships, compare, selection, diagnostics, export, or AI context.
- Provenance must remain attached to reusable Species/feature/grant semantics.
- Generated NPC/world scaffolding is not promoted by AKWI-01.

## 9. Explicit exclusions

AKWI-01 does NOT authorize:

- bulk import of the 400 Akwi NPCs;
- canonization/import of the generated NPC dependency universe;
- bulk faction/setting/place creation;
- full Twil/Twii language integration;
- full culture/background package integration beyond links needed for approved Species presentation;
- invented Akwi lineages, subspecies, alternate Forms, transformations, or adaptations;
- universal exhaustion/injury engine implementation;
- Akwi-specific character-creation UI;
- production migration unless repository evidence demonstrates that an existing generic contract cannot represent the required data;
- changes to SSA-07 authority or its selected-not-started software track state.

## 10. Acceptance criteria

AKWI-01 can be called implementation-complete only when evidence demonstrates all applicable current-runtime assertions:

1. `species.akwi` has stable governed identity and source/provenance metadata.
2. Approved reusable Species features exist without copying mechanics into Character state.
3. The generic A2 Species profile can inspect Akwi without Akwi-only presentation code.
4. Generic A2/A4 discovery/picker flow can expose and select Akwi under normal policy filtering.
5. A4 draft state stores the Akwi stable selection reference and does not perform authoritative mutation at selection time.
6. Deterministic fixtures/contracts define the fixed Akwi grant bundle with source/provenance references.
7. Deterministic Burst classification proves: 1–2 safe; 3–6 escalating strain; 7+ severe exhaustion plus injury-risk flag; full recovery resets the cycle; no unsupported partial-recovery formula is embedded.
8. Magnetic sense fixtures prove the owner-approved Earth-minimum/stability/focus/interference semantics without treating the sense as universally perfect direction.
9. No hidden/proposed/GM-only source state leaks into player projection.
10. Existing generic Species/Character flows remain passing.
11. Validation evidence is exact-head and follows current repository-health / self-hosted deterministic policy before any completion claim.

## 11. Completion language constraint

Until a later generic runtime actually consumes the rules contract, AKWI-01 completion means **Akwi is integrated as a governed playable Species at the current application's implemented A2/A4/content-contract boundary**. It does not mean the placeholder runtime has begun executing a full live exhaustion/injury simulation.
