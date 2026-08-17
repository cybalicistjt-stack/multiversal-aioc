# CCTI-05 — IAX-01 Record-Scope Candidate Projection, Tranche 1

**Date:** 2026-08-17  
**Status:** CANDIDATE SIDECAR / NOT ENABLED  
**Source/master CSV mutation:** none  
**Game-ready claim:** none

## Exact source gate

The owner-supplied `Adding.zip` was inspected and the exact checksum-bound preparation packages were recovered:

- Item v0.12.0: `d12feab1375930e1ef5c121d485aee8622f2abfc34c05f23babb26a293ee47ca` — MATCH.
- Platform v0.11.0: `621b498b6d0fa1b99c86a96eac7446f682c715cb576cf0803d233ec2ffe0bdb6` — MATCH.
- Reality v0.14.0 shared context: `928aaacbd84082d88ea9e64fc6c3506a321f26633bce718cfb46199b5364f4d6` — MATCH.

`Adding.zip` SHA-256: `a550ed965e4433dc9a3d800ef7aebda4f699c363db8ef8037d104a4a844d6277`.

The twelve target master CSVs were independently confirmed byte-identical between the retained CSV source export and `MV_Master_01_Core.zip`; their hashes are retained in `SOURCE_MASTER_SHA256_MANIFEST.csv`.

## IAX-01 result

A private derived candidate sidecar was generated for all **5,389 Item-corpus rows** using only exact v0.12.0 IAX-01 controlled values.

- **5,353** current Item Definition rows receive an IAX-01 `record_scope` candidate.
- **36** `Weapons_Ammo.csv` rows remain legacy/reference-only and receive no new Item Definition taxonomy assignment.
- **0** active Item rows are unassigned for IAX-01.
- **4,239** candidate assignments are high confidence.
- **1,150** candidate assignments are medium confidence and remain reviewable.
- source/master rows modified: **0**.
- canonical taxonomy enablement: **false**.

Candidate value distribution:

| IAX-01 value | rows |
|---|---:|
| `standalone_item` | 3,468 |
| `module_component` | 886 |
| `upgrade_modification` | 575 |
| `software_data` | 167 |
| `consumable` | 149 |
| `interface` | 68 |
| `base_chassis` | 26 |
| `non_item_support_record` | 7 |
| `refill_charge` | 4 |
| `accessory` | 2 |
| `package_kit` | 1 |

Private candidate sidecar SHA-256: `0b3c2da9839e3ce687a0766dfb0508cb120a136dcfa28f4358d4e704163c3053`.

The full 5,389-row sidecar is retained in the checksummed tranche artifact rather than copied into the governance repository.

## Assignment posture

Rules are deterministic and conservative. Direct record types/categories control where available; broad current Item rows are not over-inferred merely to reduce the review queue. `Weapons_Ammo.csv` reference identities remain provenance/supersession evidence rather than being minted as duplicate current Definitions.

This tranche completes only IAX-01 candidate projection. **IAX-02 through IAX-10 remain unfinished.**

## Object game-readiness baseline

The same tranche produced a private one-row-per-corpus readiness ledger for all **11,017 / 11,017** target rows.

- 10,981 current-content rows: `NOT_GAME_READY`.
- 36 legacy/reference-only rows: `REFERENCE_ONLY`.
- 5,353 active Item Definition rows inherit only the Item v0.12.0 evidence that minimum domain-defining mechanics/effect fields exist; that is not a complete mechanics certification.
- 5,628 Platform-domain rows have not yet passed the OGR mechanics audit.
- records certified `GAME_READY`: **0**.

Private readiness ledger SHA-256: `3e055ed7fc95bed14555f8e23c7350bfc6e56c5f33d66203bb7e34c53f3b0b8e`.

## Tranche artifact

`CCTI_Game_Readiness_Tranche1_20260817.zip`  
SHA-256: `c586a01d3d542c0230d09de600995df42408532a5f604dfa02d112a724112a9f`

The artifact contains the full candidate IAX-01 sidecar, readiness ledger, source-hash manifest, rules, readiness registries/profile matrix, aggregate baseline and this report.

## Exact next content operation

Continue Item taxonomy projection with **IAX-02 — object_nature** as another bounded candidate sidecar. Preserve source evidence, deterministic rules, confidence and explicit review state; do not mutate source/master CSVs or begin mechanics re-authoring in that taxonomy tranche.
