# CEL — Cozy Economy & Life Loop

**Program ID:** CEL  
**Program name:** Cozy Economy & Life Loop  
**Version:** 0.1.0  
**Status:** OWNER-DIRECTED — PLANNED INTERSTITIAL SUBPROJECT  
**Owner and final authority:** John Brandon Turner  
**Directed:** 2026-08-20  
**Roadmap position:** after MIB-14 and before MIB-15

## 1. Purpose

CEL turns the already-designed Cozy Solo, Connected Cozy, Downtime/Projects, crafting, relationship, economy, ingredient/foodcraft and base/facility foundations into a directed, replayable **game experience** rather than a collection of pleasant but disconnected activities.

Cozy remains setting-independent. A CEL experience may be a farm, kitchen, apothecary, workshop, market stall, tavern, research lab, repair bay, magical greenhouse, ranch, fishing operation, starship cabin, home, guild room or another authored low-pressure life/activity profile. Farming or domestic simulation is never mandatory merely because the experience is Cozy.

CEL is not a second rules engine. It orchestrates existing owning-domain operations through APW Downtime/Projects and APM Cozy authority, uses MIB-13 for economy/trade, ICF for ingredients/production/cooking/alchemy, MIB-14 for base/facility foundations, MIB-12 for crafting and existing relationship/reputation mechanics where applicable.

## 2. Core gameplay loop

The intended loop is:

`Orient → choose a meaningful goal/order/project → plan time/resources → perform or bounded-automate routine work → encounter a decision/opportunity/constraint → commit owner-domain results → use/sell/trade outputs → pay costs/reinvest/improve → progress goals/relationships/capabilities → reflect/choose next direction`

The loop must provide reasons to act without punitive engagement mechanics. Players can pursue self-directed goals, authored requests/contracts, production targets, home/base improvements, collection/completion goals, relationship/community goals, research, cooking/alchemy/crafting mastery or setting-specific objectives.

CEL must create feedback between activities. Gathering and production feed crafting/cooking/alchemy; outputs feed use, trade and contracts; trade feeds upgrades and new opportunities; facilities change what projects are possible; relationships and reputation can alter opportunities where the owning rules permit; projects and choices create future goals and constraints.

## 3. Existing systems CEL must reuse

### 3.1 Cozy/APM
Use the existing Cozy operation classes, explicit delegation, fresh authorization, resource budgets, version checks, stop conditions, one-step/until-choice/bounded-batch pacing, optional bounded-background eligibility, no-AI path and mandatory human/GM decision barriers.

### 3.2 Downtime/APW
Use the existing durable Project/activity model for owners/participants, objectives, phases/tasks, prerequisites, inputs, required time, locations/facilities, assigned assets, checks/choices, progress, complications, outputs, cancellation and provenance.

### 3.3 MIB-13 economy
Use canonical in-game currencies, prices/modifiers, merchant/service availability, buy/sell/barter/trade, reservations/contracts/settlements and deterministic local-market profiles. CEL does not own a duplicate wallet, merchant or market ledger.

### 3.4 ICF
Use canonical crops, plants, livestock/aquatic outputs, creature harvests, ingredients, derived preparations, cooking/magical cooking, alchemy, production facilities and recipe definitions.

### 3.5 MIB-14 base/facility foundations
Use base/home/facility/storage/workstation/capacity/resource hooks rather than inventing Cozy-only houses or facilities.

### 3.6 Other owning domains
Crafting, relationships/reputation, progression, inventory, Character and World state remain owned by their existing systems. CEL may coordinate or present them only through governed operations.

## 4. Time and automation rule

CEL supports deterministic **in-world simulation**, not an idle-game loophole.

- Wall-clock elapsed time is not game progress by default.
- The human may authorize an in-world Downtime block, routine batch or authored time-advance operation when the owning rules permit it.
- A bounded Cozy controller may resolve preauthorized routine operations until the next meaningful choice, cost threshold, resource shortage, complication, stale state, completion or other registered stop condition.
- Every automatic operation retains current authorization, exact resource/time budgets, expected versions, idempotency/recovery and owner-domain receipts.
- Automation cannot make human choices, GM adjudications, consent decisions, irreversible advancement choices, ownership transfers or real-money purchases.
- Optional AI remains presentation/suggestion only; the complete life/economy loop works deterministically with AI disabled.

## 5. Anti-aimlessness design rule

A CEL experience must always be able to answer:

1. **What am I working toward?** — one or more visible goals, contracts, projects, improvements, collections, relationships or authored milestones.
2. **What can I do now?** — a bounded palette derived from current time, resources, facilities, skills/permissions and project state.
3. **Why does it matter?** — the action changes resources, output quality, economy, capability, project progress, relationship/reputation, facility state or another governed future option.
4. **What choice is approaching?** — meaningful branching, investment, substitution, risk, scheduling, sale/use decision, project direction or other human decision.
5. **What changed when I return?** — an evidence-backed summary of completed routine work, costs, outputs, market/project changes and pending decisions.

CEL must avoid coercive streaks, fake urgency, punishment for not logging in, meaningless click repetition and indefinite automation with no decision boundary.

## 6. Tranche plan

### CEL-01 — Goals, Routines & Cozy Life Loop Foundation
Define goal/objective profiles, routine/activity palettes, project bundles, visible milestones, dependency/next-action projection and a setting-independent loop that references existing owner-domain Activities/Projects rather than duplicating them. Support self-directed goals and authored goal templates without making the controller choose a life direction silently.

### CEL-02 — Personal Economy, Demand, Orders & Reinvestment Loop
Integrate MIB-13 prices, currencies, merchant/service availability, local demand and settlement with Cozy/Downtime. Define safe budgets, ordinary recurring in-game costs where authored, buy/sell/barter/service work, commissions/orders/requests, output valuation, savings/reinvestment choices and deterministic local-market changes tied to governed in-world time/events. Real-money commerce remains absent.

### CEL-03 — Home/Base, Production, Hospitality & Resource Loop
Integrate MIB-14 home/base/facility foundations and ICF production into complete low-pressure activity loops: cultivation, husbandry, fishing/apiary/monster husbandry where authored, cooking/alchemy, workshops, storage/preservation, maintenance, shop/stall/tavern/hospitality/service profiles, facility improvements and resource logistics. The same architecture must support non-farming settings.

### CEL-04 — Bounded Routine Automation & In-World Simulation
Compose APM Cozy automation with APW Downtime projects and CEL goals. Define routine queues/batches, `one-step`, `until-next-choice` and bounded simulation profiles, in-world time-block advancement, recurring deterministic upkeep/production, exact resource/currency ceilings, reservation/retry/recovery behavior, completion summaries and mandatory stop boundaries. No wall-clock progress by default and no indefinite autonomous play.

### CEL-05 — Opportunities, Complications, Relationships & Progression Hooks
Create deterministic opportunity/request/event tables and governed integration hooks for seasonal/setting cadence, scarcity/surplus, customers/clients, research discoveries, project complications, relationship/reputation opportunities, training/eligibility, collections/mastery and facility/economy unlocks. Human consent, hidden Campaign truth, GM adjudication and irreversible progression remain outside automation authority.

### CEL-06 — Integrated Cozy Game Experience, Balance & Connected-Cozy Proof
Build a golden setting-independent Cozy scenario that proves a complete multi-session/in-world-week or longer loop using goals, Downtime, economy, ICF production/foodcraft/alchemy, crafting, base/facility improvement, bounded automation and meaningful stop/choice points. Include Connected Cozy contribution paths, no-AI operation, stale/recovery cases, anti-grind/anti-idle checks, resource-source/sink balance, progress summaries and UI Workbench acceptance. Completion requires that the experience feels directed and consequential rather than a disconnected activity sandbox.

## 7. Completion target

CEL is successful when an ordinary user can enter Cozy with a clear goal, complete meaningful manual and bounded-automated routines, see resources/time/economy change deterministically, make decisions that affect later options, improve an authored home/base/project/life loop, leave at a safe boundary and return to an intelligible summary and next decision—without a GM being required for the supported Personal profile and without AI mechanical authority.

## 8. Boundaries

- No second rules, economy, inventory, Project, Character, relationship, base/facility, ingredient or crafting ledger.
- Cozy remains an orchestration/presentation experience over owning domains.
- MIB-13 owns in-game price/currency/merchant/trade semantics; CEL composes them.
- ICF owns ingredient/production/recipe definitions; CEL consumes them.
- MIB-14 owns base/facility foundations; CEL consumes them.
- APW owns Downtime/Project semantics; APM owns Cozy delegation/automation boundaries.
- Wall-clock elapsed time is not game progress by default.
- No coercive streaks, punitive absence mechanics or dark-pattern engagement loops.
- No automatic human consent, GM adjudication, irreversible advancement, ownership transfer or publication.
- No real-money/payment automation or integration.
- Optional AI is advisory/presentation only and a complete no-AI path is mandatory.
- No production provider selection is implied.
- Migration 0022 remains unreserved unless a selected tranche proves a genuine durable schema delta.
