# 05 — Research-to-Implementation Roadmap and Acceptance Matrix

## Scope and status
Owner explicitly approved the research-to-implementation tranches **and future body-plan foundation** on 2026-10-19 and directed execution. Application candidate [PR #861](https://github.com/cybalicistjt-stack/Multiversal-app/pull/861) contains isolated source work. Approval of scope is distinct from an OPS5 CURRENT-selected implementation item and production publication. The parallel GPR/MTLC selectors remain unchanged. See [07](07_OWNER_APPROVED_EXECUTION.md).

## Five owner-approved directions (not yet certified product tranches)
| ID | Research outcome | Minimal adoption path | Exit proof |
|---|---|---|---|
| UX-01 | FDE scene/context preview UX and gap closure | extend existing FDE projection/UI only | deterministic invariance, real renderer preview if claimed, accessibility and cross-platform evidence |
| COMP-01 | Cross-owner recipe and compatibility manifest | adapters around FDE-04/CAPP-07, no duplicate preset owner | round trip, checksum/version/rights, authorization/visibility negative proofs |
| FORM-01 | Modular form/augmentation **proposal** design | read-only topology map + action routed to actual owner | anatomical immutability until authorized owner acceptance; nonhuman and secret tests |
| SOC-01 | GM-authored presentation challenges | social runtime projection and existing adjudication | fairness/usability study; GM secrecy; no free modifiers |
| PORT-01 | Creator API, portability and optional AI proposal path | provider-off contract first, optional bounded AI later | reproducible import/export, entitlement/provenance, multi-device proof only where executed |

## Dependency order
1. **Existing owner contracts review:** CASI, CAPP/PPIA, FGA/FDE, equipment/abilities, social action authority, ARI permissions. Confirm semantic terms and current API before shipping interfaces.
2. UX-01 and COMP-01 may each begin after the fit/preset review; COMP-01 must not replace CAPP-07 presets.
3. FORM-01 depends on Species/Form & actual augmentation rule ownership. Its cosmetic part can be designed without authorizing functional limbs.
4. SOC-01 depends on accepted social mechanics and GM visibility conventions. Evaluation must not hardcode rules the user has not approved.
5. PORT-01 consumes stable schemas and real importer diagnostics; AI is optional, never provider-mandatory.

## Acceptance classes
- **R: research evidence**: confirm source text, date, feature status, licensing context, no contradictory caveats.
- **D: design review**: domain-owners/owner approve exact IDs, schema and interfaces, no unauthorized domains.
- **F: focused deterministic proof**: compile/types/semantic validators, representative fixtures for permitted/partial/unresolved/forbidden.
- **I: independent integration**: full Creator session and real local storage; explicit cross-app/device if claimed.
- **P: publication**: exact-head PR, target-main integration, required validation, OPS5 reconciliation. A draft PR or local test does not grant P.

## Negative tests that must always pass
1. Fashion dye/preview/ability cosmetic does not change mana cost, attack bonus, spell DC, damage or ability availability.
2. Cosmetic wing/tail/extra limb cannot grant anatomy, flight, carrying capacity or movement modes.
3. Same appearance recipe cannot insert actual item into inventory or equip slot.
4. Hidden NPC state cannot appear in player preview, error messages, portable export or AI suggestion prompt.
5. Unsupported/nonhuman topology yields explicit unresolved/incompatible receipt, no default humanoid.
6. Import with stale owner ref/version cannot silently overwrite new data; requires review.
7. Export/import with missing copyrighted or unavailable assets retains semantics and reports missing visuals, not silently downloads content.
8. Same recipe and registry versions give same checksum regardless of client device/renderer.
9. Unknown fields cannot trigger executable actions or network calls.
10. Optional AI cannot submit owner action or spend credits without explicit configured permission.
11. Offline/provider-off FDE path remains usable.
12. GM social criteria remain filtered from unauthorized player views.

## Five evaluation questions for owner usability playtests
- How many interactions until a saved design can be previewed in another context?
- Can a player distinguish **appearance** from functionality without tutorial intervention?
- Are import failures actionable: *what* is missing, *why*, and *how to repair*?
- Can a GM adjudicate presentation challenges using current rules without unplanned extra bookkeeping?
- Does the player see one consistent design across full-body, portrait and token modes with clear degradation when an asset is missing?

Collect measured time, counts and errors; do not assign invented performance targets or completion scores.

## Proposed first implementation slice
One context-preview selector on existing FDE, one portable presentation-only appearance recipe, one validator/compatibility report covering human + Vespin + Moravi + Mythragara + ManyToms. Gate behind domain review first; do not begin a second fashion engine.

## Risks/decisions
- Is **environmental contextual preview** merely an illustrative compositor or actual target-renderer parity? Must label truthfully.
- Does a universal appearance recipe add any value beyond existing CAPP/FDE preset contracts? Implement only the missing orchestration seam.
- Functional prosthetic owners are mapped by DPL-13 and MSWI-07 to Character-Actors, D17-Asset, DPL-05, Condition, Progression-Abilities, MIB-12, MIB-13 and APW-D26 (CCP where applicable); the missing proof is real end-to-end authorized orchestration. See 06.
- Which exact social mechanic may be modified by wardrobe? No default automatic modifiers.
- Do we have user-approved sharing/public collection/licensing/monetization policy? Not yet established by this study.
- Platform limitations, performance, and user benefits remain *untested*; external sources are inspiration, not acceptance evidence.

## Prototype/checking evidence in this research package
Static source comparison and structured example authored. No application change, automated test run, live UI review, playtest, or CI required/claimed. Review/merge of research docs must still obey protected-main policy; research PR can remain draft.

## Owner-approved implementation continuation — 2026-10-19

The owner explicitly directed continuation of the **entire** Appearance/Identity and future Species/body-plan line. The first implementation candidate is [Multiversal-app PR #861](https://github.com/cybalicistjt-stack/Multiversal-app/pull/861). Its OPS5 [AXI selector #1904](https://github.com/cybalicistjt-stack/multiversal-aioc/pull/1904) was merged to AIOC main as `a5c129c4402e4d69d365845ece4f49c196ae6778`; GPR and MTLC selections remain independent.

The app candidate now combines: 66 synthetic general body-plan templates; owner-created novel structural regions and parent relationships; editable open-ended cardinality; per-region skin materials/textures/patterns/palettes/markings; provider-off/nonhumanoid structural preview; local and portable Species designs; authenticated subject-bound Creator-to-Character reuse; explicit A10 draft/A4 design/CASI surface/FGA garment proposal seams; and MSWI-07/A9 bounded proposals. Creator remains the body-plan source; Fashion consumes it without a Human fallback. No Species/Form canon or gameplay permissions are inferred.

**Acceptance is layered:** a green Node/Vitest/TypeScript Linux+Windows and deterministic receipt validates only source/runtime tests in that bounded fixture environment. Separate owner and real-boundary proof remains required for registered/playable user Species, A10 publication, actual A2 picker entitlement, production CAPP rigs and FGA-02 fit for novel shapes, real CASI Character appearance commits, GM-committed A9 interactions and installed/native-device parity. Preserve **CORE26-CURRENT-01** as current canon; the 66 examples are noncanonical. The current app candidate and CI result are maintained on PR #861, not copied as a second status authority here.
