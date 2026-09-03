# CEW-07 — Existing Creature Coverage Audit Contract

**Contract:** `CEW-COV-1.0`  
**Work item:** CEW-07 — Existing Creature Coverage Audit  
**Authority:** content/recovery/design/provenance only; **no application implementation authority**.

## Purpose

CEW-07 measures what the existing creature corpus is actually covered by after CEW-01 through CEW-06. It consumes `CEW-ID-1.0`, `CEW-TAX-1.0`, `CEW-CLASS-1.0`, `CEW-HAB-1.0`, `CEW-DIST-1.0`, and `CEW-ECO-1.0` without changing any of them.

**Coverage is evidence accounting, not a substitute for creature truth.** A coverage count records what governed evidence is presently available and bound at a defined scope. It does not claim that the creature itself lacks every unrecorded property.

**Canonical object presence does not mean source recovery is complete.** The 27 currently governed Creature Definitions have stable identity, while the retained source corpus contains 826 safe statblock records and additional unresolved/deferred source evidence. Canonical identity coverage and source-recovery coverage are therefore separate audit layers.

## Coverage layers

CEW-07 keeps these layers distinct:

1. **Canonical identity coverage** — exact `CEW-ID-1.0` stable IDs. All 27 current Creature Definitions are covered here.
2. **Source recovery accounting** — candidate starts and safe statblock records from the retained 23-document creature corpus. Source-only records remain noncanonical until separately normalized.
3. **Stable-ID fact coverage** — CEW facts that are explicitly bound to a current canonical stable ID.
4. **Source-label evidence** — source-backed facts whose subject is a source record or label but whose canonical identity binding is unresolved.
5. **Deferred/unresolved evidence** — formal deferrals, semantic-review candidates, diagnostic packets and unresolved source starts. Their existence is tracked without promotion.

These layers must not be collapsed into a single percentage or score.

## Source recovery accounting

The retained dedicated creature-source corpus has:

- 23 source documents;
- 878 candidate starts;
- 826 safe statblock records;
- 52 candidate starts not represented by a safe statblock record;
- 14 documents whose nonzero candidate starts are fully represented by safe statblock records;
- 6 documents with partial safe-statblock accounting;
- 3 documents with no safe statblock records: `Creature types.PDF`, `Vampirism&Lycanthropy.PDF`, and `animals 11-16-24.PDF`.

The three no-safe-statblock documents are not treated as empty sources. `Creature types.PDF` already supplied taxonomy authority to CEW-02, while the other gaps remain explicit recovery limitations.

The corpus also retains 324 source-signature candidates, 93 formally deferred source candidates, and 30 unresolved review/diagnostic creature candidates (18 direct-review, 9 semantic-validation pending, 3 GPT diagnostic packets). None are promoted by this audit.

## Canonical stable-ID fact coverage

For the 27 current Creature Definitions, CEW-07 finds the following directly bound CEW-01..06 coverage:

- identity: 27;
- game type/taxonomy: 0 stable-ID bindings;
- habitat/ecology: 0 stable-ID bindings;
- distribution scope: 5 stable-ID bindings;
- ecological-role/encounter-use: 0 stable-ID bindings.

The five distribution-covered stable IDs are the current Havalaea-setting Creature Definitions. `CEW-DIST-1.0` asserts that they are present in Havalaea, but their native status remains **unknown**. Setting namespace or setting presence does not establish native lineage; CEW-10 owns that dedicated question.

Zero stable-ID bindings on an axis does not mean the source corpus has no relevant information. CEW-04 and CEW-06 contain representative source-label evidence; CEW-07 refuses to convert that source-label evidence into stable-ID facts merely because a name appears to match.

## Identity-binding rule

**A source-label match does not create a canonical identity binding.** Exact display-name overlap, pluralization, punctuation, heading similarity, type similarity, mechanics, source family, or setting context cannot replace the explicit identity/alias authority required by `CEW-ID-1.0`.

CEW-07 therefore retains an unresolved overlap queue for:

- `Jungle-Slip Beetle` ↔ `mv.setting.havalaea.creature.jungle-slip-beetle`;
- `Rootstalker` ↔ `mv.setting.havalaea.creature.rootstalker`;
- `Sapcrawl Varnet` ↔ `mv.setting.havalaea.creature.sapcrawl-varnet`;
- `3. Rift-Touched Animals (Optional)` ↔ possible `mv.adventure.lost-key.creature.rift-touched-animal`.

No binding is created by CEW-07 for any of them.

## Unknown and gap semantics

**Unknown remains a valid audited result.** CEW-07 does not fill missing taxonomy, habitat, distribution, ecological-role, intelligence, personhood, domestication, partnership or relationship-pathway facts from names, general knowledge, plausible biology, similar creatures, mechanics, or environmental fit.

A descriptive gap is not an instruction to invent content. Missing facts remain assigned to their governed future owners.

## Successor and future-owner boundary

**CEW-08 owns the Creature-Type Coverage Audit.** It receives the measured current corpus and the recovered CEW-02 taxonomy, and it may determine type-family coverage without CEW-07 prematurely assigning types to stable IDs.

Subsequent owners remain:

- CEW-09 — intelligence, personhood, domestication and partnership classification;
- CEW-10 — Havalaea native fauna and Time-of-Troubles lineage;
- CEW-11 — mount, pet, familiar and companion-system crosswalk;
- CEW-12 — Earthlike animal and wildlife baseline;
- CEW-13..15 — governed gap expansion only after the preceding audits/classifications.

## Non-authorities

CEW-07 does not:

- promote source-only records to canonical Creature Definitions;
- create aliases or duplicate merges;
- bind source-label facts to stable IDs by name similarity;
- infer missing creature types, habitat facts, distribution, native status or ecological roles;
- calculate a creature-quality, ecological-fit, encounter-use or completeness score;
- create new creatures or expand the corpus;
- modify `Multiversal-app` schemas, runtime, UI, search behavior, migrations or placement state.

## Handoff

CEW-07 closes when the canonical corpus/source-accounting ledger is verified and **CEW-08 — Creature-Type Coverage Audit** is selected as the strict successor.
