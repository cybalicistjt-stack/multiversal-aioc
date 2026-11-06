# 06 — Resolved owner boundaries and integration architecture

**Status:** owner-approved research/design; **NOT** a new OPS5 work selector, feature, live integration, cross-device proof or product certification. Read together with the earlier five study files in this directory.

## Verified owner-source map

| Extension | Existing authority | Required action | Never allowed |
|---|---|---|---|
| Fashion garment semantics and fit | \`FGA-PARAM-1\` (15 parameters), FGA-02 fit/occlusion, FDE-04 saved design versions | Resolve garment ref/version and fit before any preview; keep the garment checksum stable across background changes | Silent fit, new biology, item ownership or mechanics from fashion |
| Character appearance | \`PPIA-06\` and \`CAPP-07\` existing species-aware appearance/preset design, app \`Casi06AppearanceStudioRuntime.ts\` | Use existing constrained appearance/profile controls and full-body/portrait/token projections | New generic humanoid editor; biological-state rewrite |
| Equipment and cosmetic gear | \`CAPP-06\` and CAS-EQUIP-001 | Actual equipment is a read-only authorized visual projection | Equipping through a cosmetic garment or hidden equipped-item leak |
| Functional cybernetics and prosthetics | \`DPL-13\`, DPL-01 disposition: Character-Actors, D17-Asset, Condition, DPL-05, Progression-Abilities, MIB-12, MIB-13, APW-D26 (CCP for symbiotes) | Refer to those owners; explicit owner validation before any action | Universal slots/humanity meter or automatic implant/stat change |
| Biological modification interoperability | App \`mswi-07-biological-lineage-integration.ts\`, \`bindMswi07EmbodiedModification\` | Request \`graft|implant|symbiote|prosthetic\`; body location, interface, source event/version, \`grant|remove|retain|reverse\`; resolve compatibility rule | Treat accepted reference shape as compatible installation |
| Social presentation | A9 \`social-interaction-port.ts\` and \`social-resolution-port.ts\`; \`MV-IA-F010\` | Project tags/evidence into existing \`structured-challenge\`, recognized resolution, GM decision and filtered Player projection | Free modifier, independent score system, unauthorized NPC truth or auto-outcome |
| Environmental context | ISE-06 \`NativeOrchestratedScene.tsx\`, source-authorized visual/audio intents | View-only deterministic illustrative context; use real renderer only when validated; visibility-filtered | Claim live weather/world/ability gameplay effect from preview |
| Reusable scene/cast style | \`saa-12-reusable-cast-shot-scene-expression-presets.ts\` | Reference/version/availability checks, consumed as read-only optional presentation presets | Duplicate actor identity or import hidden/uncleared resources |

## Resolved questions

- **Who owns functional prosthetics?** DPL-13 already has an explicit multi-owner reference map. The remaining gap is a validated *end-to-end application adapter*, not absence of owners.
- **Can social fashion reuse existing gameplay?** Yes in design: A9 already defines \`freeform|assisted|structured-challenge\` and \`no-roll|fixed-dc|opposed-check|degree-of-success|extended-challenge|gm-determined\`. Clothing supplies narrative criteria and evidence; a GM/domain authority resolves the outcome.
- **Is Multiversal missing preset support?** No. CAPP-07/PPIA-06 specify appearance presets, FDE-04 has versioned garment persistence, and SAA-12 supports multiple style/scene references. A **cross-domain compatibility adapter** remains unproven, not a new independent preset system.
- **Is contextual lighting missing everywhere?** Not established. Inspected FDE-03 displays semantic SVG garment projection with three view profiles; ISE-06 has role-filtered visual intents. The Fashion-to-Scene adapter and fidelity of actual lighting are not independently tested.
- **Does Xbox Labs provide an SDK?** No source establishes an available integration tool; treat it as research watch only, not a dependency.

## Proposed minimal seams

1. FDE-03 ↔ ISE-06: context preset and effect visibility are preview-only. Keep FGA garment semantic identity constant; warn when simulated lighting is illustrative.
2. FDE-04 ↔ CAPP-07/CASI-06 ↔ SAA-12: a thin reference composition, not copied data. Validate source versions, rights, visibility, nonhuman fit, and export review. No duplicate preset authority.
3. FDE/CASI ↔ DPL-13/MSWI-07: read-only body anchor view and explicit routed functional-modification proposal; never auto-install.
4. FDE/CASI ↔ A9: player-visible fashion evidence for a GM-authored social structured challenge, with hidden criteria redacted before output.
5. Interoperability/optional AI: deterministic provider-off engine and serialized references first; AI suggestions produce reviewed drafts only.

## Research-only executable probe

\`prototype_probe.js\` is standalone CommonJS JavaScript. Run \`node prototype_probe.js\`. It exercises representative compatibility, no-mutation, preview-context invariance, stale/missing/hidden owner refs, unknown nonhuman topology, augmentation proposal routing and GM-secret filtering. It is not imported into Multiversal app, does not call actual FGA/ISE/A9/DPL APIs, and **cannot prove** browser, real data store, renderer or multi-device acceptance. Its FNV-like fingerprint is illustrative only and not a security digest or canonical checksum.

### Negative proof obligations before product implementation

1. No automatically acquired inventory item, limb, flight, armor or spell effect from a visual recipe.
2. Missing four-arm/tail/wing fit data reports unresolved/incompatible, never assumes humanoid.
3. No hidden NPC item/form/judge criterion appears in Player output, errors, export, AI prompts or counts.
4. Same outfit and Character owner state across \`neutral\` and other preview contexts; only derived preview identity may differ.
5. Deny stale owner version, revoked asset rights and unknown role permissions.
6. Reject import fields containing executable network/script actions, arbitrary remote assets, gameplay stats, mechanics or world truth.
7. All cross-system effects route through existing GM/Player approval and source-owner validators.

### Development start gate

This research is an on-demand \`research-evaluation\` lane result. FGA/FDE are terminal completed_verified; GPR/PCV-03F and MTLC-14 remain active, and \`operations/CURRENT.json\` has no newly selected appearance successor. Before implementing app code, the owner-directed follow-on must select a governed implementation work item/authority and preserve independent lane, exact-head and protected-main publication discipline. Research-only PR merging would require separate validation/publication evidence; no such completion claim is made here.
