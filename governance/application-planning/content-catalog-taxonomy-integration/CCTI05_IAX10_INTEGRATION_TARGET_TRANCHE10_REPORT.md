# CCTI Write Phase — Tranche 10: Item IAX-10 Integration-Target Candidate Projection

**Date:** 2026-08-17  
**Status:** candidate sidecars produced; source masters unchanged; canonical adoption disabled

## Axis authority

Exact Item Taxonomy v0.12.0 defines `IAX-10 integration_target` as a **multi-select** axis with **16 controlled values** describing the body, equipment, platform, network, facility, storage system, magical holder, biological host, or site an Item Definition is designed to integrate with. It classifies the target host, not what the item itself happens to be.

## Result

All **5,389 Item-corpus rows** have an explicit IAX-10 disposition:

- **5,029** applicable current Definitions — high-confidence candidate set only.
- **317** applicable current Definitions — one or more medium-confidence/review-required candidates.
- **7** IAX-01 `non_item_support_record` rows — not applicable.
- **36** `Weapons_Ammo.csv` legacy/reference-only rows — not applicable.
- silently unaccounted rows — **0**.

Thus all **5,346 applicable current Definitions** carry one or more integration-target candidates. The tranche produces **5,810 candidate assertions**: **5,401 high-confidence** and **409 medium-confidence/reviewable**. **358** applicable rows legitimately have more than one target.

Value distribution:

| Integration target | assertions |
|---|---:|
| `none_general` | 3,525 |
| `computer_device` | 701 |
| `person_body` | 503 |
| `eva_suit` | 405 |
| `biological_host` | 272 |
| `network_system` | 111 |
| `base_facility` | 75 |
| `spacecraft` | 52 |
| `vehicle` | 51 |
| `universal_interface` | 46 |
| `environment_site` | 34 |
| `mecha` | 20 |
| `magic_holder_spellbook` | 14 |
| `clothing_armor` | 1 |
| `weapon` | 0 |
| `container_storage` | 0 |

Zero-count controlled values remain valid registry values. No Item is forced into `weapon` or `container_storage` merely to populate the vocabulary.

## Evidence posture and safeguards

- `none_general` is exclusive: it is never combined with a specific host target.
- EVA `Mount or Slot` and compatibility evidence are used as the preparation package's high-confidence integration seam. Suit modules target `eva_suit`; mecha/spacecraft interfaces add the explicit platform target; universal Vehicle/Habitat interfaces preserve their multi-host compatibility rather than collapsing it.
- Computer modules/components target `computer_device`; true network components and network-purpose software may also target `network_system`. Generic `Network_Range` text alone is **not** sufficient to classify software as network-integrated. Vehicle/ship computers preserve vehicle + spacecraft multi-host intent; infrastructure computers target `base_facility`.
- Cybernetic implants/limbs/frames target `person_body`; actual symbiotes target `biological_host`, with anatomical person/body integration added only where direct body-site evidence supports it. Symbiotech bridges preserve both biological and cybernetic host seams. Support equipment uses its actual enhancement target, and the Universal Augmentation Adapter retains `universal_interface`.
- Living Spellbook ability modules/upgrades target `magic_holder_spellbook`; living spellbooks and charge holders themselves remain `none_general` because being a host, bonded object, wearable focus, or readable tome does not mean the definition integrates into another spellbook.
- Ordinary melee/ranged weapons are standalone; only explicit vehicle-mounted weapon records target a platform. Using ammunition does not itself make the weapon an Item-taxonomy `weapon` integration target.
- General Items remain `none_general` unless the current record explicitly represents a body implant or a truly site-emplaced trap/structure. Wearables, containers, computers, vehicles, and structures are not assumed to integrate with their own object class merely because they *are* that class.
- Magitech infrastructure targets facility/site only where it is actual infrastructure; manufacturing equipment targets a workshop/facility; portable agriculture/life-support tools are not inflated into site/facility integration. The ten Magitech interface rows were reviewed individually against their explicit effects.
- Multi-target candidates are allowed only where the source explicitly crosses host classes. A universal/multi-platform assertion does not erase the known specific targets.
- Candidate integration metadata does not imply that an A8 Asset Instance is currently installed, equipped, loaded, bonded, mounted, or owned.

## Validation

Independent deterministic validation: **PASS**.

- exact axis/cardinality: `IAX-10 integration_target`, multi;
- exact 16-value v0.12.0 registry membership; zero foreign IDs;
- 5,389/5,389 source-row accounting;
- 5,346/5,346 applicable current Definitions carry at least one candidate;
- 7/7 non-item support records explicitly not applicable;
- 36/36 legacy/reference-only rows explicitly not applicable;
- zero silently unaccounted rows;
- zero duplicate same-target assertions per source row;
- `none_general` exclusivity verified;
- candidate counts reconcile row summaries with assertion sidecar;
- all nine Item source/master CSV SHA-256 values match the pre-write manifest;
- candidate taxonomy remains disabled/noncanonical;
- mechanics/runtime/game-ready state unchanged.

Private assertion SHA-256: `ba26f37cda5b7d78dd34090c309bffb3b606e76d32ecdcbf9b7f9eedf7cfaee0`  
Private row-summary SHA-256: `4e5a7d4b658ed44714b3bdf8e0a3ea4eb2de43db3dd7e3b99fc1851e87d6cc90`  
Rule-usage SHA-256: `3641199d7715abc75de30e11a7a7010a51c8450e7d323b1223dd1b64c764904d`  
Baseline SHA-256: `72347e4789755e896084100c91c3ea1ba9a77f10da6b5c86cce576db19b5d52c`

## Universal Item taxonomy milestone

IAX-10 completes the first bounded candidate-disposition pass across **all 10 universal Item taxonomy axes**. This is not yet canonical adoption and does not mean every medium-confidence/unresolved state is resolved. The next content operation is a **cross-axis review/consolidation gate**: reconcile the explicit review queues, validate cross-axis invariants, preserve the exact source/provenance chain, and produce the proposed governed Item taxonomy adoption package before enabling any candidate metadata or beginning mechanics reauthoring.
