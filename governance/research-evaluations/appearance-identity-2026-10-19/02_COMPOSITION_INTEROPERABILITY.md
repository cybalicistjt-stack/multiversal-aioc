# 02 — Cross-system Appearance Recipe (COMP-01) — proposed contract

## Design objective
A portable **manifest of references and presentation choices**, not a flattened image and not a new owner of anatomy, mechanics, inventory, outfits or effects. One accepted recipe can request full-body, portrait or token projections and optionally other supported preview contexts without creating new character truth. This proposal must first be reconciled against CAPP-07/PPIA-06 existing presets.

## Proposed envelope
`recipeId`, `schemaVersion`, `authorRef`, `ownerEntityRef` + version, `speciesFormRef` + version, `appearanceProfileRef`, `wardrobeDesignRef` + version + garment checksum, `equipmentVisualRefs`, `abilityAppearanceRefs`, `presentation`, `resourceRefs`, `provenance`, and `capabilityRequirements`.

**Refs, not truth:** the `wardrobeDesignRef` is an FDE-04 design; `speciesFormRef` remains owned by Species/Form; `equipmentVisualRefs` read projections from equipment owner; `abilityAppearanceRefs` reference authorized ability appearance configurations and never the ability's rules data. Each upstream owner resolves the ref and version. Unavailable reference remains an explicit partial/unsupported result. No synthetic stats/bonus/magic trait fields permitted.

**Presentation-only fields:** palette override *only if FGA and the given garment family permit it*; approved effect visibility preference; pose/expression; selected derivative view profile; one of enumerated environment preview presets; nonvisual caption. Camera change is constrained by CAPP/PPIA fixed 3/4 full-body profile; no free orbit or revealing hidden anatomy. Scene context is a local, noncanonical rendering simulation, not authoritative weather/world state.

**Provenance:** stable author/source identification, source asset IDs, license/rights metadata through ARI, software/template schema versions, build-independent checksum over normalized semantic IDs, imported/AI-suggested flag and explicit review receipt after approval. Do not treat AI-generated output as owner canon.

## Proposal processing protocol
1. **Parse safely**: size/field limits, schema version, reject executable data and unapproved URLs, preserve audit origin.
2. **Resolve references**: fetch from allowed owner/read projections with version and entitlement checks. Apply GM/Player visibility filter **before** diff, preview, export, or text diagnostics; never disclose hidden refs in rejection.
3. **Check eligibility**: Species/Form/Topology, garment-family controls, FGA-02 fit, FGA-03 coverage, CAPP restrictions, resource license and active ability/equipment visual ownership. Default to `unknown`, never humanoid.
4. **Project a diff**: display actionable compatible choices; unresolved ID/asset in-place warnings; incompatible changes; safe alternatives only when supported by authority.
5. **User review**: explicit accept/reject per change, no automatic commit from import/AI. A recipe may be saved as a personal preset even when display coverage is partial.
6. **Commit**: call only domain-authorized mutation surfaces for presentation choices; anatomy, hardware, equipment, ability mechanics and gameplay state require independent owner operations/approvals. Use expected versions/idempotency and recovery for ambiguous responses.
7. **Render**: derive full-body/portrait/token and optional contextual view with a shared semantic identity; label unsupported partial projections and preserve inaccessible nonvisual summary.
8. **Export**: export the filtered, authorized subset with provenance and compatibility needs, never live entitlement secrets or remote image-source contents.

## Suggested normalized result
`compatible` if every required authority resolves and the requested edit is allowed; `partial` for missing noncritical visual components; `unresolved` for unverified owner-version/rights; `incompatible` for proven conflict; `forbidden` for policy/visibility violation. `unknown` source state cannot turn into compatible by default. Return a stable, display-safe reason code, a human text summary, and explicit next action (replace component, keep as partial, request owner authority, cancel).

## Example of user flow
Creator loads an existing FDE jacket design and a Species/Form projection for a Vespin. Recipe uses existing clothing and color choices plus approved pose. The FGA fit check must report genuine four-arm/wing constraints; inability to render a sleeve cannot be concealed by treating the Vespin as humanoid. A costume wing is only presentation, never flight. The creator can review incompatibility and choose another eligible garment. No inventory item appears as a side effect.

## Ability-style and item-style bridges
- **Cosmetic ability appearance**: store display config ref, enabled effects, palette and resource manifests against an existing ability key/version. Never modify spell cost, range, modifiers, roll result, action availability, timing or GM approval.
- **Equipment visual**: `equipmentVisualRef` references the owner-approved equipped visual projection. An item-shaped cosmetic cannot confer actual armor/weapon inventory.
- **Forms/augmentations**: the recipe may preview the authorized currently selected Form; creating/attaching a new functional form or replacement component is a *proposed operation* to Species/Form/equipment/augmentation owner, not an appearance receipt.
- **Image sources**: only ARI-approved, owner-entitled assets; source upload remains behind explicit intake review and licensing.

## Import/portability
Portable semantic JSON can be carried between Creator, GM tools, character sheets, NPC studio and standalone style products through adapters. Each adapter advertises capabilities, supported profiles and entitlement; it must not assume platform parity. Unknown future fields preserved only in quarantined provenance metadata, never silently executed as controls. Migrations require versioned adapters and preview-diff.

## Deliberately excluded
Invented owner/domain references; direct arbitrary Internet download; auto-installation; fashion challenges writing mechanic scores; custom body topology authored from an outfit; arbitrary shader upload; marketplace publication; sync assertions without cross-device proof.

## Compact compatibility decision examples
1. Known human + valid FDE garment design + supported view → compatible, presentation-only.
2. Vespin + human two-arm garment with no four-arm fit rule → unresolved/incompatible, never default to human.
3. Invented `equipmentVisualRef` → unresolved, not granted as an owned item.
4. Referenced ability with altered `damage` property → reject schema; no mechanics field exists.
5. Missing effect asset → partial display / effect disabled with warning, preserve underlying recipe.
6. Hidden NPC visual reference → filtered; no explanatory message revealing it.
7. Old design schema → require version adapter and explicit review.
8. AI-generated reference proposal → no commit until review.

## Decision questions for implementation owner
Confirm exact current owner IDs/API for CAPP presets, ability visual configuration, item/equipment projection, Species/Form modifications; decide acceptable bounded environment context list; define privacy and sharing; approve schema only after source-owner review.
