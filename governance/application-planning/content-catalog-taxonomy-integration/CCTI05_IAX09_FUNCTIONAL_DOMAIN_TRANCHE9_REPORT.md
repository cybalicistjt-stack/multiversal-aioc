# CCTI Write Phase — Tranche 9: Item IAX-09 Functional-Domain Candidate Projection

**Date:** 2026-08-17  
**Status:** candidate sidecars produced; source masters unchanged; canonical adoption disabled

## Axis authority

Exact Item Taxonomy v0.12.0 defines `IAX-09 functional_domain` as a **multi-select** axis with **40 controlled values** describing what an item is principally useful for. Functional-domain metadata is intentionally independent of setting/genre, technology era, rarity, price, mechanical power, and A8 instance state.

## Result

All **5,389 Item-corpus rows** have an explicit IAX-09 disposition:

- **2,185** applicable current Definitions — high-confidence candidate set only.
- **3,161** applicable current Definitions — one or more medium-confidence/review-required candidates.
- **7** IAX-01 `non_item_support_record` rows — not applicable.
- **36** `Weapons_Ammo.csv` legacy/reference-only rows — not applicable.
- silently unaccounted rows — **0**.

Thus **5,346 applicable current Definitions** carry one or more functional-domain candidates. The tranche produces **12,028 candidate assertions**: **7,370 high-confidence** and **4,658 medium-confidence/reviewable**.

Largest candidate domains are `magic_casting` 1,556; `computation` 1,088; `information_media` 1,037; `offense` 883; `companion_support` 798; `environment_adaptation` 682; `protection` 562; `storage` 554; `communication` 456; and `general_utility` 413. The full 40-value registry remains valid even where this corpus has no conservative assignment; `clothing_personal` receives zero assignments in this tranche rather than being forced onto merely wearable gear.

## Evidence posture and safeguards

The projection uses domain-native categories/families and explicit item-function text, not genre/tech/rarity shortcuts. Examples:

- Melee/Ranged weapon definitions receive offense from their governed weapon-domain identity; secondary domains require separate functional evidence.
- EVA `Module Family` remains authoritative and drives life-support, mobility, sensing, communications, environment, defense, power, medical, navigation, repair, rescue, and related candidates without converting implementation-flavor text into functionality.
- Computers receive `computation` plus evidence-backed functional categories such as storage, navigation, communication, security, medical, manufacturing, science/research, targeting/fire-control, or infrastructure support. Mechanical-effect content types are not mistaken for functions.
- Living Spellbooks/charge holders receive `magic_casting`; Sentient Tomes also support information-media/companion functions, while spell/effect suites add only explicit functional domains. Genre-integration flavor clauses are stripped before functional inference.
- Magitech uses its functional Category/Subcategory and actual effect. Infrastructure records are routed by explicit utility/transit/storage/defense/manufacturing/construction functions rather than assuming all infrastructure equals construction.
- Symbiote/Cybernetic definitions use subtype and actual primary/mechanical benefits; strain-construction/provenance language and black-market sourcing do not become trade/construction functions.
- General Items use governed Category/Subcategory plus explicit effect. Merely being magical or wearable does not automatically become `magic_casting` or `clothing_personal`.
- Food/nutrition requires actual sustenance/water/meal provision, not incidental phrases such as “drinker” or “without food.” Entertainment requires recreation/entertainment purpose, not incidental music used during rescue.

These assertions remain additive search/catalog candidates and do not replace domain mechanics or imply runtime ownership/equipment state.

## Validation

Independent deterministic validation: **PASS**.

- exact axis/cardinality: `IAX-09 functional_domain`, multi;
- exact 40-value v0.12.0 registry membership; zero foreign IDs;
- 5,389/5,389 source-row accounting;
- 5,346/5,346 applicable current Definitions carry at least one candidate;
- 7/7 non-item support records explicitly not applicable;
- 36/36 legacy/reference-only rows explicitly not applicable;
- zero silently unaccounted rows;
- zero duplicate same-domain assertions per source row;
- candidate-count totals reconcile row summaries with assertion sidecar;
- all nine Item source/master CSV SHA-256 values match the pre-write manifest;
- private ZIP entries are byte-identical to the validated tranche files;
- candidate taxonomy remains disabled/noncanonical;
- mechanics/runtime/game-ready state unchanged.

Private assertion SHA-256: `5620d96dad88f4ed6e913e79fa4113ab63cd9c49856f3eb4256b6dde629e6e19`  
Private row-summary SHA-256: `5cd3571b2046f564615484d57bf851c90ce56cddc464c44b9cafda64b07bec2d`  
Rule-usage SHA-256: `871659cd224b5b737cc9d0246000156ffc8e3b57768ac052d732b1564f264dfd`  
Baseline SHA-256: `a5ad85fe3f0a8b1f0143a961a1583db5022df18fa6c1c8f79e2cd01613700bb3`

Private artifact: `CCTI_Item_Taxonomy_Tranche9_IAX09_20260817.zip`  
SHA-256: `38a0e64c957398b4844006f93653bb7ad918c58753cd37aaf107b07f69d6ff99`

## Exact next content operation

Proceed to **IAX-10 — integration_target**, the final universal Item-taxonomy axis. Preserve all prior-axis review/unknown/not-applicable states independently. Mechanics reauthoring remains outside taxonomy projection.
