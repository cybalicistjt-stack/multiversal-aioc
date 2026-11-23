# VCSR-18 — Source-to-Golden Proof Crosswalk

**Status:** standalone source reference demonstration; no gameplay writes. Owner-directed Cycle18 is the final approved numbered VCSR cycle. See [VCSR_PROGRAM.md](VCSR_PROGRAM.md).

## Three distinct fixtures (do not merge identities)

| Case | Authoritative visible source fixture | Spatial/asset reference | Expected proof | Disposition |
|---|---|---|---|---|
| Blackglass authored scavenge | `site:blackglass`, `outcome:wreck-yard:surface-brass` (2 authored pieces) | `v14:fixture:8` linked to Blackglass wreck; independent `asset:brass-scrap:lot` (3 physical synthetic pieces) | LSS-05/10 authored opportunity; MIB12 `lss08-rule:lantern-brass-cannibalization` with damaged `asset:lantern-bracket:target` and physical brass; Character/Action item-use request; D17 storage request | **Eight local reference stages only.** No assertion that Blackglass 2 pieces and D17 3-piece lot have common lineage. Explicit *unverified* cross-owner binding required |
| Utility Rover sensor | `site:rover`, `slot:sensor` (exact authored LSS06 source) | `v14:fixture:6` is the **cargo context only**, not wreck location; repair target `asset:rover:repair-target` and donor `asset:sensor-mast:donor`; existing physical `demo:owned:rover-sensor`, `demo:vehicle:rover-01`, `rover:sensor` | Explicit exact slot → MIB12 `lss08-rule:rover-sensor-replacement` → MIB14 allowed module `module:sensor-mast-standard` and rover slot → D17 transfer/storage intent `space:rover:cargo` | **Eight local reference stages only.** Distinct LSS/D17/MIB14 identities not auto-aliased or installed |
| Unidentified GM-only ship | `site:ship` with unrecoverable `slot:module`, quantity unknown | **No MMHT map/ref is authored** for ship wreck; no recovery outcome or owned physical module | GM may locate and inspect; scavenge marked not applicable; strip must reject unapproved extraction slot and unknown quantity | **Must stop at stage 4.** No hidden ship in Player projection/counts, no source-created parts |

## Ordered cross-domain handoffs

| Stage | Owning/controlling authority | Source-backed decision tested | What is never inferred |
|---|---|---|---|
| 1. Locate | World/MMHT, LSS | Exact site locationRef and optional visible VCSR14 map pointer/revision; rover map kept cargo-only | Authoritative coordinates, navigable geometry, route safety |
| 2. Inspect | LSS-02/03, D17 | Source identity, condition/slot metadata, author visibility and expected version | Salvage quantities, ownership, rarity-derived yield |
| 3. Scavenge | LSS-05/LSS-10 | Only Blackglass's authored two-piece outcome; explicit nonapplicability for others | New Asset or item actually awarded |
| 4. Strip | LSS-06, D17 | Rover `slot:sensor` recoverable quantity; Blackglass nonapplicable; ship rejected | Extraction profile for ship/mecha with unknown slot |
| 5. Repair | MIB-12, D17, APW/D26 | Existing exact donor/target/rule and owner version checked by Cycle12 `v12Inspect`; explicit external lineage ref | Material consumption, repaired Asset or campaign time |
| 6. Mount / use | MIB-14/A8, Character/Action | Rover explicit module/mount allow-list and physical `demo:owned:rover-sensor`; lantern requires Character/Action rule ref | Installation, activation, granted ability or pilot control |
| 7. Transfer / store | D17, MIB-03, MIB-14 | Existing physical asset/quantity/version, requested owner authorization, dest `space:rover:cargo` capacity evidence | Actual transfer, storage, owner/custodian change, duplicate inventory |
| 8. Checkpoint | OPS5/VCSR browser only | Cumulative local JSON, exact real browser download and fresh import, stage order preserved | Remote server persistence, D17 owner receipt, online/Android sync |

## Acceptance and UX conformance limits

- New Cycle18 49-source invariant suite, with Cycles01–17 suites invoked but not presented as an independently re-counted aggregate.
- Real desktop/mobile keyboard Enter and local focus-visible, native buttons, labeled forms, status announcements; new route controls locally target at least 44×44 CSS px. W3C WCAG2.2 SC2.5.8 AA minimum is 24×24 CSS px subject to exceptions: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum
- Pass/blocked/current stages include text, not color alone. 8 source-to-owner crosswalk rows per journey; native keyboard controls, no drag-only dependency.
- Only GM may author local proof evidence. Player only sees authorized case labels/coarse progress, with GM-only ship and stage evidence/operation receipts removed before counts/export. Prior VCSR14 spatial, VCSR15 Project, VCSR16 Character and VCSR17 economy handoffs preserved.
- **No claim of full WCAG compliance, screen-reader testing, keyboard-only full-app testing, physical device or live app integration.** Exact-file CI must verify test truth before any green status.
