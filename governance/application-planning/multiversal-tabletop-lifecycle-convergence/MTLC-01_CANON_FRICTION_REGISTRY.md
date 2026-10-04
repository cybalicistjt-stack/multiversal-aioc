# MTLC-01 Canon, Friction, and Source Registry

**Program:** MTLC — Multiversal Tabletop Lifecycle Convergence  
**Work package:** MTLC-01  
**Status:** IN_PROGRESS_PLANNING / NO IMPLEMENTATION AUTHORITY  
**Started:** 2026-10-04  
**Purpose:** Establish the authoritative delta between capabilities Multiversal already owns, older source-backed material that must be recovered, features that need convergence into a coherent tabletop lifecycle, genuine additions, and integrations that should remain outside the core client.

## 1. Product goal

The product-level test for MTLC is simple:

> **When people decide to play a tabletop RPG, opening Multiversal should be the natural first action.**

MTLC owns the friction between major systems: finding a table, forming a group, scheduling, preparing, communicating, playing, recovering from disruption, closing a session, advancing, doing downtime, and gathering again.

MTLC does **not** imply that Multiversal must own every transport, media library, encoder, payment rail, calendar provider, or third-party ecosystem. The application should own the workflow and preserve a nearly invisible handoff where outside infrastructure is the better boundary.

## 2. Classification vocabulary

- **CONVERGE** — capability already substantially exists; expose it as part of one lifecycle instead of creating a duplicate system.
- **RECOVER** — older/source-backed Multiversal material exists but is not adequately surfaced in current product planning or implementation evidence.
- **ADD** — genuine new first-party capability candidate.
- **INTEGRATE** — Multiversal should own the workflow and state handoff while using provider-neutral outside infrastructure where appropriate.
- **DEFER** — legitimate capability, but not part of the near-term lifecycle core.
- **VERIFY** — classification is plausible but source/provenance still needs exact confirmation.

## 3. First-pass connective-tissue census

This is the approved 70-item lifecycle inventory, normalized into MTLC-01 classification. The disposition is intentionally about **ownership**, not implementation priority.

| ID | Capability | Initial disposition |
|---:|---|---|
| 01 | Find a Game | ADD |
| 02 | Player and GM Profiles | ADD |
| 03 | Campaign Recruitment | CONVERGE + ADD |
| 04 | Session Zero | RECOVER + CONVERGE |
| 05 | Per-Session Safety | RECOVER + ADD |
| 06 | Scheduling | ADD |
| 07 | Real-World Session Logistics | ADD |
| 08 | Campaign Lounge | ADD |
| 09 | Notification Control | CONVERGE |
| 10 | Session Readiness / Preflight | ADD |
| 11 | Player Homework | ADD |
| 12 | GM Prep Cockpit | CONVERGE |
| 13 | Session Launch | ADD + CONVERGE |
| 14 | Late / Missing / AFK Players | ADD |
| 15 | Live Session Utility Bar | ADD + CONVERGE |
| 16 | Dice and Randomizers | CONVERGE + ADD |
| 17 | Physical-Dice Friendly Mode | ADD |
| 18 | Voice Communication | INTEGRATE |
| 19 | Video and Screen Sharing | INTEGRATE |
| 20 | Live Captions / Speech Accessibility | ADD + INTEGRATE |
| 21 | Session Audio Director | ADD |
| 22 | Bring-Your-Own Audio | ADD |
| 23 | In-Person Table Mode | ADD + CONVERGE |
| 24 | Hybrid Table Mode | ADD |
| 25 | Map Micro-Utilities | CONVERGE |
| 26 | Handouts | CONVERGE + ADD |
| 27 | Personal PDF / Rulebook Library | ADD |
| 28 | Rules Concierge | CONVERGE |
| 29 | Rulings Ledger | ADD |
| 30 | CWKS Documents | CONVERGE |
| 31 | Idea Inbox / Quick Capture | ADD |
| 32 | Between-Session Async Play | CONVERGE |
| 33 | Party Planning Board | ADD |
| 34 | Loot Distribution | CONVERGE |
| 35 | Character Admin Inbox | CONVERGE |
| 36 | Post-Session Closure | CONVERGE + ADD |
| 37 | “Previously on Multiversal…” | ADD |
| 38 | Missed-Session Catch-Up | ADD |
| 39 | Campaign Continuity Memory | CONVERGE |
| 40 | World Time + Real Time | CONVERGE + ADD |
| 41 | GM Random Utility Drawer | ADD |
| 42 | No-Code Automation Studio | ADD |
| 43 | User Macros / Quick Actions | ADD |
| 44 | Extension Framework | ADD |
| 45 | External Integration Hub | INTEGRATE |
| 46 | Multiversal Exchange | ADD / LATER |
| 47 | Marketplace Commerce | DEFER |
| 48 | Community Moderation | ADD — REQUIRED BEFORE PUBLIC COMMUNITY |
| 49 | Observer / Spectator Role | ADD |
| 50 | Actual-Play / Streaming Mode | INTEGRATE |
| 51 | Recording / Transcript Pipeline | INTEGRATE / OPTIONAL |
| 52 | Convention / One-Shot Mode | ADD |
| 53 | Pickup Game Mode | ADD |
| 54 | Campaign Templates | CONVERGE |
| 55 | Party / Club / Store Organizer | DEFER |
| 56 | Print / Physical Output | ADD |
| 57 | Mobile Companion / Table Remote | CONVERGE + ADD |
| 58 | Accessibility Control Center | CONVERGE |
| 59 | New Player Mode | CONVERGE + ADD |
| 60 | New GM Mode | ADD + CONVERGE |
| 61 | Game/System Quickstart | ADD |
| 62 | Next Action Center | ADD — HIGH PRIORITY |
| 63 | GM Attention Center | ADD |
| 64 | Search Everywhere | CONVERGE |
| 65 | Universal “Turn This Into…” | ADD |
| 66 | Universal Share / Link | ADD |
| 67 | Campaign Handoff / Co-GM | CONVERGE + ADD |
| 68 | Support Without Leaving App | CONVERGE |
| 69 | Crash / Disconnect Grace | CONVERGE |
| 70 | Portable Ownership | CONVERGE |

## 4. Known current anchors

MTLC-01 must preferentially reuse current Multiversal authority rather than invent parallel records. Current planning and product evidence already indicate substantial foundations in these areas:

- campaign creation, participation and player/role management;
- campaign invitations and durable session membership;
- live session lifecycle and reconnect/recovery behavior;
- GM/player permissions and hidden-information handling;
- campaign/session builder workflows;
- characters, advancement, inventory and loot;
- rules browsing and contextual rules assistance;
- investigation, relationship/faction and social tooling;
- maps, handouts and shared assets;
- offline/reconnect, accessibility and multi-device behavior;
- post-session state, history and campaign continuity;
- CWKS structured documents and authoring;
- notification/interruption concepts;
- campaign export/ownership/recovery.

These anchors are **reuse candidates**, not proof that every connective workflow is already product-complete.

## 5. Mandatory recovery target: Consent and Veils

Owner correction is authoritative: Multiversal already has consent and Veils material in older source content, likely in the original PDF corpus.

MTLC-01 therefore classifies Session Zero / consent / Veils as **RECOVER + CONVERGE**, not as a blank-slate feature invention.

Required recovery behavior:

1. locate the original source-backed material if available;
2. preserve source terminology and provenance;
3. identify which parts are rules/content versus product workflow;
4. map existing material into current campaign/session authority;
5. record any genuine source gap instead of fabricating original wording;
6. only then specify missing UI/workflow around that recovered canon.

## 6. Group/human-continuity decision

The approved Group architecture is recorded separately in `MTLC_GROUP_LIFECYCLE_SPEC.md`.

Core decision:

`User -> Group -> Campaign / One-shot / Trial Game / Game Event -> Session`

A Group is the durable human continuity layer. Campaign membership and Group membership are intentionally separate lifecycles. The Group layer must reuse existing campaign/session/identity/invitation/permission authority rather than becoming a second campaign system.

## 7. Initial convergence clusters

To keep implementation from becoming 70 disconnected feature tickets, MTLC-01 groups the inventory into lifecycle clusters.

### A. Find and form the table
01, 02, 03, 04, 05, 46, 48, 52, 53, 55.

### B. Keep the humans together
06, 07, 08, 09, 10, 11, 14, 32, 33, 37, 38, 39, 40, 62, 63, 67.

### C. Run game night
13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 41, 49, 50, 51, 57.

### D. Close the loop after play
34, 35, 36, 37, 38, 39, 54, 56, 61, 68, 69, 70.

### E. Make everything connected
27, 30, 31, 42, 43, 44, 45, 58, 59, 60, 64, 65, 66.

### F. Later public/commercial ecosystem
46, 47, 48, 55.

Items may belong to more than one cluster when the workflow legitimately crosses boundaries.

## 8. Native versus integrated boundary

Keep these responsibilities provider-neutral unless later evidence proves a first-party stack is strategically necessary:

- voice transport;
- video transport;
- screen sharing transport;
- speech-to-text / caption providers;
- external calendars;
- external notification bridges;
- streaming/OBS transport;
- large hosted media libraries;
- recording storage;
- commerce/payment rails.

Multiversal should still own permissions, lifecycle state, user intent, session context, attachment/linkage, failure handling and the user-facing handoff.

## 9. Core-client size rule

MTLC features should primarily be structured data, UI and logic.

Do not make the mandatory client large merely because lifecycle features can reference media. Heavy art, audio, maps, transcripts and similar payloads should remain optional packs, selected offline content, local user assets, bounded caches or provider-backed content.

## 10. MTLC-01 exit criteria

MTLC-01 is complete only when:

1. every one of the 70 inventory items has an authoritative disposition;
2. every CONVERGE claim names the current Multiversal authority it reuses;
3. every RECOVER claim names the recovered source or an explicit unresolved provenance gap;
4. duplicate candidate data owners are removed before implementation;
5. native/integrated/deferred boundaries are explicit;
6. privacy/moderation/public-community gates are explicit;
7. the inventory is partitioned into bounded implementation tranches;
8. the first implementation tranche can be selected without reopening broad archaeology.

## 11. Current execution note

As of 2026-10-04, OPS3 persistent implementation slots are occupied by active GPR, CWKS and CASI work. MTLC-01 is therefore proceeding as bounded planning/source-convergence work without taking implementation authority or displacing an active lane.

Persistent MTLC implementation activation is a later governance action after a slot becomes available or the owner explicitly reprioritizes a live slot.
