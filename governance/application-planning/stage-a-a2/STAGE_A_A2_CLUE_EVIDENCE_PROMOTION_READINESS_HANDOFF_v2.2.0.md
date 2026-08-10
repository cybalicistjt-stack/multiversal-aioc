# STAGE-A-A2 Clue / Evidence Promotion Readiness Handoff v2.2.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Status:** final real positive-fixture gap analyzed; source-backed four-record Evidence promotion prepared; permanent identity keys pending owner approval  
**AIOC branch:** `governance/stage-a-a2-detailed-design`  
**Application implementation:** NOT STARTED  
**Release/deployment authority:** NONE

## Artifact

`STAGE_A_A2_CLUE_EVIDENCE_PROMOTION_READINESS_v2.2.0.zip`

SHA-256:

`1bb62448ed64438c06d17d7acd94b59ea7770cbe7250576b69942227471728c3`

Validator:

`A2 CLUE/EVIDENCE PROMOTION READINESS: PASS`

Counts:

- current governed release: 11,877 objects;
- source-backed Evidence candidates: 4;
- current exact-name collisions: 0;
- owner decisions pending: 3;
- Source Record IDs minted: 0;
- Definition IDs minted: 0.

## Source basis

The retained `MV_Master_01_Core.zip` contains `Margot McBride's and Investigation.PDF` (40 pages). Render-first review and extracted text verify that the dossier example **The Vanishing of Dr. Wen** explicitly provides player-facing Evidence objects and GM discovery/reveal context.

Source package SHA-256:

`c5732c5b4c3cdf5eca1d19eef7354289d1f92a87397b56aa7623b3f0a24177ec`

Source PDF SHA-256:

`ac76b433d2b0d007667eaf4701070aae738dd20262b9d9c30d13a09a3a888760`

Rendered source evidence pages 29, 30 and 32 are included in the package with hashes.

## Four promotion candidates

1. **Scorched Notebook** — document/physical Evidence; source player packet page 32; GM clue breakdown page 30 gives discovery on Dr. Wen's desk and incomplete dimensional-rift equations.
2. **Sigil Photograph** — photograph Evidence; player packet page 32; GM material identifies the sigil as a tracker left by the rogue faction.
3. **Assistant Witness Statement** — witness-statement Evidence; player packet page 32; page 29 provides the example statement and GM material establishes hidden knowledge.
4. **Torn Journal Entry** — document Evidence; player packet page 32; source example does not supply an exact discovery position, so none is invented.

All four use `P-A2-EVIDENCE` if promoted. Discovery/reveal state remains projection/campaign state and is not baked into the immutable Definition.

## Recommended permanent identity decisions

The stable-ID contract prevents guessing these values. The exact remaining owner approvals are:

1. approve logical source catalog key **`INV`** for the Investigation Evidence extraction catalog;
2. approve permanent Evidence Definition family prefix **`EVD`**;
3. approve **Evidence** as the canonical semantic family, with **Clue** as an Evidence role/subtype and Document / Photograph / Witness Statement as Evidence forms, all using `P-A2-EVIDENCE`.

Recommended logical catalog ID:

`MV_MASTER_01_CORE::INVESTIGATION_EVIDENCE::THE_VANISHING_OF_DR_WEN`

Deterministic candidate identities under those recommended keys (NOT FROZEN):

- Scorched Notebook — `SRC-INV-62C7BF9B3D87` → `DEF-EVD-A8C83D6F509E`
- Sigil Photograph — `SRC-INV-6021E747D95E` → `DEF-EVD-D870D04A40DE`
- Assistant Witness Statement — `SRC-INV-0E684642C0A6` → `DEF-EVD-38DA7A7007C5`
- Torn Journal Entry — `SRC-INV-6D4542916B72` → `DEF-EVD-131D79099CBF`

These IDs are candidates only. They must not be represented as governed until owner approval and the bounded promotion execute.

## Exact next operation after approval

Execute the four-record Evidence promotion; freeze the four `SRC-INV-*` and four `DEF-EVD-*` identities; add `Master Content::Definition::EVD -> P-A2-EVIDENCE`; regenerate affected search/Inspector/Picker/redaction/deep-link fixtures; rerun affected A2 validators; and rebuild the Sunday master so the prior `P-A2-EVIDENCE` positive-fixture gap is removed.

Until that promotion completes, Sunday master v2.1.0 remains valid and the Evidence gap remains explicit.

## Preservation boundary

This handoff does not activate A2 implementation, change `CURRENT_WORK_POINTER.json`, complete the parallel Design Standards attempt, expand into full investigation/case implementation, fabricate missing discovery metadata, or authorize release/deployment.
