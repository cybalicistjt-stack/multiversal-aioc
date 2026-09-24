# PCV — Product Convergence & Real-App Validation

**Status:** in_progress — PCV-01 and PCV-02 completed_verified; PCV-03 selected_not_started  
**Lane:** gpr  
**Owner direction:** 2026-09-23

## Mission

Recover product convergence after the BIP-installed beta demonstrated that the repository's current production entry path still exposed a synthetic alpha/authorization harness instead of the intended Multiversal product.

The terminal goal is concrete: **a real Android APK and Windows application in which two distinct people can create/join the same Multiversal campaign, play together across devices, persist/recover their state, and use the actual current feature set rather than a fixture shell.**

PCV is not a rewrite of Multiversal and is not a return to the old Bibles. It converges existing implementation first and implements only missing runtime seams proven missing by live-source evidence.

## Source authority hierarchy for PCV

1. Live repository implementation and current canonical architecture.
2. Newer convergence/implementation/skin/feature decisions created after the original UI/Screen/Feature Bibles.
3. Current Development Bible architecture and approved owner decisions.
4. UI/Screen/Feature Bibles as floor, traceability and unfulfilled-intent references—not as a ceiling that may delete or suppress later features.

The September 2026 UI Implementation Convergence Handoff is especially important: it explicitly says current alpha screens are behavioral evidence only, not final design authority, and maps the already-implemented A2-A12 behavioral seams that should be preserved.

## Live evidence motivating this family

- The installed BIP beta exposed Local Alpha Campaign / fixture Character / authorization-required / diagnostics-first surfaces.
- The production `App.tsx` currently composes local-alpha identity/workspace adapters and only a narrow route shell.
- `apps/client-ui/src` contains hundreds of files and substantial real components across A2-A12 and many later programs; these must be converged rather than discarded.
- Later client families include additional play/creator/simulation systems added after the original Bibles.
- `packages/ui-system` contains current presentation/skin runtime work that the packaged shell does not yet fully express.
- `packages/session-protocol`, `packages/local-store`, `apps/signaling`, and the separate mobile shell paths are still structural placeholders, despite architecture/program proofs around those boundaries.
- Database migration definitions, production-platform contracts, local-first/host-authoritative architecture, rules/projection contracts, and many domain contracts already exist and should be consumed rather than rebuilt.
- The canonical local/online model supports a host-authoritative, multi-transport product with direct/manual WebRTC as a zero-service baseline and optional signaling/TURN/relay adapters.
- SMB-01 selected a managed Postgres production profile but deliberately left live activation false; PCV therefore does not require a paid hosted backend merely to prove two-person play.

## Family invariants

1. **Real-product proof only.** No user-facing tranche closes on contracts, fixture data, golden files, isolated test modules, or synthetic in-process adapters alone.
2. **Installed-device evidence.** Any tranche claiming persistence, networking, responsive behavior or platform support must exercise the actual packaged application on the relevant platform.
3. **Vertical-slice completeness.** A user-facing capability is complete only when navigation + screen + real governed data + actions + permissions + persistence + failure/recovery + mobile/desktop behavior all work together.
4. **Preserve later work.** The original Bibles are not allowed to erase or downgrade capabilities added afterward.
5. **Converge before rebuilding.** Existing behavioral/runtime/UI implementations are reused unless live evidence proves them unsuitable.
6. **Synthetic harness quarantine.** Fixture/local-alpha adapters remain available for tests/dev tooling if useful, but cannot be the ordinary production entry path.
7. **One app, full capability on every form factor.** Android/phone and Windows/laptop share product state/contracts and capability authority. Mobile is not a reduced feature product: every player, GM and creator capability must remain operable from a phone. Phone defaults to a responsive phone-optimized layout, and the app also provides an optional Desktop View on phone that preserves the wide desktop workspace inside a zoomable/pannable canvas rather than removing or substituting functionality.
8. **Two-human authority proof.** Multiplayer completion requires two distinct identities/devices and role-safe projections, not two objects in one test process.
9. **Local-first remains viable.** Paid cloud/provider activation is not a blocking prerequisite for core play; optional services stay replaceable.
10. **Visual convergence uses current sources.** September UI convergence + later UISK/owner visual decisions outrank temporary alpha CSS.
11. **No stranded substantial feature.** By PCV-08 every production-like user-facing implementation is integrated or explicitly classified internal/deferred with rationale.
12. **No fake readiness labels.** BETA_READY/RELEASE_CANDIDATE_READY terminology may not be reissued until PCV-10 human installed-play proof succeeds.
13. **Asset coverage is product coverage.** Every user-facing visual/audio/3D need must have an explicit state: primary-authored asset, parameterized/composited derivative, procedural/generated presentation, permitted imported asset, approved fallback/placeholder, or visibly unresolved.
14. **Primary-first pixel strategy.** Pixel-art character/creature/item/token work should minimize one-off artwork by using governed primary layers, morphology/animation templates, semantic palette regions, deterministic composition and Character Designer parameters. Generated derivatives retain primary provenance.
15. **No unresolved golden-path assets.** PCV-10 cannot pass while the representative first-party two-human play path contains unresolved required assets.
16. **Games and wagering reuse shared authority.** Casino/table/alien games are reusable GPR loop-mini activities that settle through canonical owner domains; Black Vegas is a flagship venue/catalog, not a separate incompatible game engine.
17. **Two wagering contexts, one runtime.** Campaign play may stake actual in-world character/campaign wealth or other validated fictional assets and applies persistent consequences; Free Play uses an isolated arbitrary resettable wallet with no campaign mutation.
18. **No real-world-value wagering.** Real money, paid entitlement/premium currency, cash-redeemable value, or anything convertible to those may never be accepted as a stake or payout. This restriction does not block ordinary fictional/in-world currency, items, favors or other owner-domain stakes.
19. **Regulation is modular.** MRC and other jurisdiction/regulator systems may enrich wagering, racing and event play, but the GM can disable them entirely or select a light/custom profile without disabling the underlying games, races, markets or settlement.

## Tranche sequence

### 1. PCV-01 — Real Product Spine, Persistence & Convergence Cutover

**Meaningful outcome:** Installed Android and Windows clients boot into the real Multiversal shell, use real persisted local identity/profile/state, load the governed Library/corpus, and no longer expose synthetic local-alpha fixtures as ordinary product data. A live-source convergence ledger classifies every user-facing implementation as integrated, stranded, internal-only, fixture/test-only, or intentionally deferred.

Acceptance:
- Production App entry no longer defaults to LocalAlphaIdentityAdapter, synthetic fixture campaigns/characters, or diagnostic-first navigation.
- packages/local-store (or an architecture-conforming replacement at the approved boundary) contains a real durable local implementation using the canonical application-data location and SQLite/local persistence rules.
- Real profile/identity, selected context, app preferences, and resumable Home state survive process/device restart.
- The actual packaged Library/corpus and provenance support load successfully on Android and Windows, or a concrete missing packaged dependency is repaired rather than hidden behind a generic unavailable state.
- The production shell consumes current UI-convergence + UI-system/skin work and presents mobile/desktop layouts without alpha/debug labels.
- A machine-readable convergence ledger covers all current live user-facing source families, including post-Bible additions; no later feature is silently dropped.
- The convergence ledger includes an Asset Demand Ledger derived from the current engine/product surface. It enumerates required character/creature/entity, item/equipment, environment/terrain, structure/prop, map/token, effect/animation, UI/skin, audio and 3D/specialty needs and classifies each as primary-authored, parameterized/composited, procedural/generated, permitted imported, approved fallback/placeholder, or unresolved.
- The Asset Demand Ledger records primary-art dependencies and variation dimensions so the project can quantify what must actually be authored once versus generated from primaries.

### 2. PCV-02 — Real Character, Campaign, World, Scene & Pixel-Asset Foundation

**Meaningful outcome:** A single user can create/open a real campaign/world, create or select a real character, establish ownership/control, prepare a scene, close the app, reopen it, and resume that same governed state. Character visuals are produced by an onboard deterministic pixel-art generator driven by Character Designer parameters and a compact governed primary-art library rather than one-off sprites for every combination.

Acceptance:
- Character creation/sheet/advancement use real repository/persistence boundaries, not fixture adapters.
- Campaign membership, world/campaign ownership, scene preparation, first-party content selection and role-safe projections are durable.
- Home resumes the active campaign/character/scene in <=2 interactions on phone and desktop.
- Every PCV-02 user-facing action remains usable at phone width with a phone-optimized layout; no Character/Campaign/World/Scene capability may be hidden behind a desktop-only implementation. Shared shell work must remain compatible with the later phone Desktop View zoom/pan mode.
- First-party SMB-08/09 content is consumable as product data, not only golden-test input.
- Implement the onboard pixel-art generator around governed primary parts and manifests. At minimum it supports discrete body/morphology templates, skin/fur/scale/material palettes, hair/head features, markings, clothing/armor/equipment layers, pose/animation templates, status/effect overlays and deterministic seed/output identity.
- Character Designer selections update the generated character visual directly; generated visual state is derived presentation and never becomes character-rule truth.
- Primary assets use semantic palette/mask regions and layer/anchor metadata so recolor, equipment substitution and compatible morphology adjustment do not require duplicate source artwork.
- Generated derivatives retain source-primary IDs, version/checksum and provenance; cached/exported derivatives are reproducible from the same visual specification.
- Core generation works offline/on-device without an AI/provider dependency. Optional AI-assisted art generation may supply new reviewed primaries later but is not required to render a valid character.
- PCV-02 publishes the first governed Primary Pixel Asset Pack sufficient for representative humanoid/person-scale character creation and defines extension seams for creature/entity, item and scene families consumed by later PCV tranches.

### 3. PCV-03 — Two-Device Membership, Transport, Presence & Reconnect

**Meaningful outcome:** A Windows host and Android client can join the same campaign/session as distinct subjects, exchange player-safe projections and commands, disconnect/reconnect without duplicate resolution, and retain membership/role continuity.

Acceptance:
- Implement the currently-placeholder session-protocol transport boundary and the minimal signaling/handshake path needed for real devices.
- Preserve the canonical local-capable host-authoritative architecture: direct/manual signaling is the zero-service baseline; optional signaling/TURN/relay remains replaceable and is activated only if required for cross-location reliability.
- Invitation/join, stable subject/device continuity, presence, ordered events, idempotency, resume tokens/checkpoints, authority epoch and hidden-before-publication filtering are real runtime behavior.
- Android<->Windows cross-device evidence is produced from installed builds, not an in-process synthetic test.

### 4. PCV-04 — Live Session, Rules, Actions & Combat Play Loop

**Meaningful outcome:** Two people can actually play a core Multiversal encounter together from scene entry through action choice, GM adjudication, rules/dice resolution, combat, result/log, save, disconnect/reconnect and continuation.

Acceptance:
- Live Scene, available actions, costs/requirements, proposal/approval/modify/reject, rule/calculation inspection and receipts operate over real shared session state.
- Combat timing, targeting, reactions, hazards, conditions/resources and encounter conclusion operate cross-device without page-context loss.
- GM/player secrecy and authority are proven on separate installed clients.
- A completed encounter remains correct after restart/reconnect.

### 5. PCV-05 — First-Party Adventure & Noncombat Play Convergence

**Meaningful outcome:** The first-party campaign can be played beyond combat through exploration/travel/survival, investigation, social/relationships/reputation, downtime/cozy activity and ordinary scene transitions.

Acceptance:
- SMB-09 first-party campaign content is reachable through real campaign/session UI.
- Investigation, social and exploration runtimes consume shared session/state authority and persist outcomes.
- Travel/survival, factions/organizations/settlements and relevant knowledge/reputation systems are integrated where current implementation supports them.
- A cross-device session can move between noncombat and combat activities without losing authoritative context.

### 6. PCV-06 — Inventory, Economy, Crafting, Games & Wagering, Vehicles, Mounts, Bases & Logistics

**Meaningful outcome:** Long-lived shared assets and operational systems are usable in the real campaign: equipment, containers/transfers, economy/trade, crafting, reusable games/wagering activities, vehicles/living mounts, bases/facilities and logistics persist and synchronize between users.

Acceptance:
- Real inventory/equipment/container ownership and transfers are persistent and permission-safe.
- Economy/trade/contracts/services and crafting/work queues commit through governed events and survive reconnect.
- Implement `PCV_GAMES_WAGERING_INTEGRATION_v1.2.0.md` as a reusable Games & Wagering runtime over current GPR loop-mini/pattern execution plus canonical owner-domain settlement; do not build a Black Vegas-only parallel engine.
- Support Campaign Play using actual validated in-world character/campaign wealth, assets or other fictional stakes with persistent consequences, and Free Play using an isolated arbitrary resettable wallet that never mutates campaign state.
- Ship a substantial Earth casino-game starter pack plus a Black Vegas/Multiversal starter pack, including external-event wager markets (especially races), MRC sanction/jurisdiction behavior where applicable, and culturally/economically distinct wagering such as subsistence-credit games, black-market egg/hatch pools and title-stake racing. Authoritative randomness/hidden information/external outcomes are recorded for replay/audit, and house/bookmaker/NPC/two-human participants use the current authority/continuity model.
- MRC/regulator behavior is GM-selectable as off, light, custom-module or full. Turning it off removes taxes/licensing/sponsorship/enforcement/integrity overlays without removing the underlying games, races, betting markets, ownership settlement or replay/multiplayer behavior.
- Reject real-world-value stake sources and payouts: real money, paid entitlement/premium currency, cash-redeemable value, or anything convertible to those. Ordinary in-world currencies, items, favors and other owner-domain stakes remain allowed when their owning domain validates them.
- Vehicle/mount/cargo/crew and base/facility/logistics views use current capability-driven models rather than hard-coded fantasy/space assumptions.
- Cross-device contention/conflict behavior is explicit and recoverable.

### 7. PCV-07 — GM/Creator Authoring, Library, Rules & Content Sharing

**Meaningful outcome:** A GM/creator can build and maintain actual campaign/world/adventure/content material inside the same product used for play, then share/publish it through existing governed boundaries.

Acceptance:
- World/adventure/scene/content authoring, reusable Library, rules/search, dependencies, provenance/history and validation are integrated into the production shell.
- MRCS and other current rules/content-authoring implementations are surfaced where they are user-facing rather than left as isolated workbenches.
- Campaign-local creation remains distinct from reusable/canonical publishing authority.
- Content can be transferred/shared between the two tester identities without bypassing rights/provenance controls.
- Games & Wagering definitions are authorable as governed reusable content: game rules, table/venue configuration, legal fictional stake classes, house rules, dealer/NPC profiles and setting/alien game packs bind through MRCS/Content Forge boundaries without duplicating runtime or owner-domain authority.

### 8. PCV-08 — Post-Bible Feature Convergence & Stranded-System Elimination

**Meaningful outcome:** All later user-facing work added after the original Bibles is either integrated into coherent product navigation/workflows or explicitly classified as internal/deferred; no substantial implemented feature remains stranded behind a test/workbench.

Acceptance:
- Converge applicable later families such as APM/async-cozy-AutoGM, APW hybrid activity, CSW creator tools, CEL, KFR, ISE, MAL, ODL, SCL, SSA, WCI, ECI and other live-source families discovered by the PCV ledger.
- Preserve newer capabilities that supersede or extend older Bible assumptions.
- Every production-like client surface has a product route/context or an explicit non-product classification with rationale.
- No completion by deleting or hiding later features merely to match older documentation.

### 9. PCV-09 — Full Product UX, Skin, Accessibility, Search, AI & Operations Convergence

**Meaningful outcome:** The entire integrated product uses the current Multiversal interaction/visual system on phone and desktop, with coherent themes/skins, settings, search/command, notifications, AI proposal surfaces, diagnostics and accessibility instead of generic alpha panels.

Acceptance:
- Consume the September UI Implementation Convergence Handoff and later UISK runtime/amendments as current presentation inputs; old Bibles remain floor/traceability only.
- Global shell, Home, context navigation, inspectors, action docks, mobile transformations and current skin system are applied across real screens.
- Implement explicit display-mode control on phone: **Phone View** uses responsive mobile-native screens and **Desktop View** renders the full desktop workspace in an in-app zoomable/pannable viewport. Both modes operate on the same product state, permissions and actions; Desktop View is not a separate product and Phone View must not remove capabilities.
- GM and creator workflows receive the same mobile capability parity as player workflows. Desktop may expose more simultaneous panes because of screen area, but no GM/creator action is classified desktop-only.
- Search/command, notifications/approvals, settings/accessibility, diagnostics/recovery and optional AI proposal flows are reachable and permission-safe.
- No ordinary-user surface exposes synthetic fixture labels, raw internal IDs or diagnostic-first copy unless explicitly in diagnostics.
- Representative Android and Windows rendered evidence covers major play/authoring/utility surfaces and accessibility states.
- Asset presentation is converged with the current skin/UI system: primary/generated pixel content, maps/tokens, item imagery, effects and approved fallbacks compose coherently with skins rather than reverting to generic empty cards.
- Remaining asset-demand entries are either satisfied or explicitly non-golden-path deferred; no substantial product surface silently ships as an accidental blank.
- Games & Wagering has coherent responsive phone/desktop product surfaces: a generic games browser/table flow plus venue-aware presentation such as Black Vegas, accessible hidden-information handling, clear Campaign vs Free Play context, and no real-money purchase/cash-out affordance.

### 10. PCV-10 — Two-Human Golden Campaign, Recovery & Real Beta Installer

**Meaningful outcome:** Fresh-installed Android and Windows builds support a real two-human Multiversal campaign between owner and second tester, with persistent cross-device play, recovery, meaningful feature breadth and regenerated beta installers from the exact validated head.

Acceptance:
- Fresh install on Windows + Android; create/sign into distinct local tester identities; create or open campaign; invite/join; choose/create characters; enter session.
- Play a representative first-party sequence containing noncombat interaction, inventory/resource use and a combat encounter, with GM/player role separation.
- Disconnect/reconnect, app restart, save/load, update-compatible install and recovery preserve campaign/session history with no duplicate actions.
- Exercise representative later/post-Bible systems appropriate to the campaign rather than proving only the old core.
- Human-visible UI matches current convergence/skin direction on both devices and contains no alpha fixture shell.
- Installed Android proof exercises representative player and GM/creator capabilities in Phone View and also proves the optional Desktop View can zoom/pan through the wide workspace without losing actions, context, focus, permissions or authoritative state.
- Generate final Windows installer + Android APK with checksum/version manifest only after this installed two-human proof passes.
- The representative first-party golden play path contains no unresolved required visual/audio assets; every asset need is fulfilled by shipped primary/generated content, a deliberate procedural presentation, a permitted imported asset, or an explicitly approved intentional fallback.
- Installed proof exercises Games & Wagering on Windows and Android: at least one Earth game and one Black Vegas/alien game, a persistent campaign-funded wager, an isolated Free Play wallet reset, and a two-human or host-authoritative table/reconnect path, with zero real-world-value wagering.


## Owner-review evidence without execution stalls

Major visual/product tranches must produce owner-reviewable Android + desktop renders or recordings, but execution does not stop merely to wait for aesthetic acknowledgment unless a real design fork requires an owner decision. Mandatory owner decision gates remain explicit.

## Terminal definition

PCV is terminal only after PCV-10 proves the installed two-human campaign journey and regenerates Android/Windows beta packages from that exact validated head. At that point the term "beta" refers to the real converged product rather than a validation shell.
