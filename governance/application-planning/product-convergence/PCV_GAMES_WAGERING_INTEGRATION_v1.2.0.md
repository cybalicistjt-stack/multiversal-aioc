# PCV Games & Wagering Integration

**Document ID:** PCV-GW-01  
**Version:** 1.2.0  
**Supersedes:** 1.1.0  
**Status:** OWNER-APPROVED CROSS-TRANCHE PRODUCT REQUIREMENT  
**Owner direction:** 2026-09-24  
**Primary delivery tranche:** PCV-06  
**Consuming tranches:** PCV-07, PCV-09, PCV-10  
**PCV-01 rule:** Track as an approved deferred journey only; this document does not authorize premature PCV-06 implementation.

## Product intent

Multiversal shall provide one reusable **Games & Wagering** framework that works across the full game, not only inside casinos. It supports:

1. **Intrinsic games** — card, dice, wheel, board, bluffing, auction, press-your-luck and other games whose own rules determine the result.
2. **Wager markets over external events** — bets on races, arena fights, creature competitions, tournaments, expeditions, crafting contests, social contests, fictional political events, hatching outcomes and any other governed event with authoritative outcomes.
3. **Venue and culture layers** — Black Vegas is a flagship catalog/venue, while worlds, settlements, factions and cultures can register their own wagering customs, legal regimes and presentation.

The same game/market definition works in two contexts:

- **Campaign Play** — participants may stake actual validated in-world character/campaign wealth or other fictional assets. Settlement mutates the canonical owning domains and persists as campaign history.
- **Free Play** — participants use an isolated fake wallet with an arbitrary starting balance. It may be reset at will and never mutates campaign wealth/state.

The only categorical wagering prohibition is real-world value.

## Real-world-value boundary

A stake or payout is invalid when it is any of the following:

- real-world money;
- currency/credit/token purchased for real-world money or representing subscription/entitlement value;
- cash-redeemable or externally redeemable value;
- value directly convertible into any of the above.

Ordinary fictional/in-world currencies, abstract wealth, items, vehicles, property, services, favors, debts, contracts, reputation, memories, traits, time/lifespan, soul fragments, alternate-self consequences, subsistence/food-assistance credits and GM-defined fictional stakes may be supported when a canonical owner-domain adapter exists and validates reservation/settlement.

Games & Wagering must never create a cash-out path.

## Event-market architecture

A **BettableEvent** is an adapter over an authoritative Multiversal activity. It does not reimplement that activity. It exposes only wager-relevant facts:

- stable event identity/version;
- participants/entrants/teams;
- authoritative start/lock/finish state;
- legal observable outcome dimensions;
- visibility/publication rules;
- cancellation/no-contest rules;
- owner-domain result receipt;
- optional regulator/sanction context.

A **WagerMarket** declares:

- market type: fixed-odds, pari-mutuel/pool, exchange, bracket/future, proposition/side bet, auction, head-to-head, spread/handicap, winner/place/show, or custom;
- eligible outcomes and settlement rules;
- stake classes and limits;
- market open/lock/close timing;
- house/tax/organizer shares;
- jurisdiction/sanction status;
- integrity/conflict restrictions;
- settlement owner-domain adapters;
- presentation/provenance metadata.

This allows racing, combat, sports, creature contests and other systems to stay authoritative over their own outcomes while Games & Wagering handles markets, stakes and settlement.

## MRC setting integration

The **Multiversal Racing Committee (MRC)** is an in-setting governmental/regulatory authority and must be modeled where its jurisdiction applies. Current setting source establishes it as the official governing body for racing, gambling and competitive events under the Goblin Empire, headquartered on Black Vegas. It licenses events and participants, regulates betting, taxes gambling, uses Steward Corps as referees/arbiters, uses Chaos Patrols against unsanctioned events, and has sponsorship/corporate ties plus documented allegations of race-fixing and rigged odds.

Games & Wagering therefore supports a regulator/jurisdiction projection that can change both mechanics and feel without owning the underlying event.

For MRC-governed content, model at least:

- **sanction state:** sanctioned, provisional, unsanctioned, pirate/illegal, disputed jurisdiction;
- **license state:** organizer/event/participant/vehicle/team licensing and special waivers;
- **Steward presence:** certified officiating, inspection and outcome validation;
- **integrity state:** certified, questioned, suspected manipulation, proven fixing/collusion;
- **safety/risk class:** ordinary through extreme/chaos-realm risk;
- **tax/house take:** MRC levy, organizer take, local levy, sponsor subsidy;
- **sponsorship obligations:** named sponsor restrictions, bonuses, exclusivity, publicity requirements;
- **prestige/access:** invitation tiers, championship qualification, reputation and cultural importance;
- **enforcement heat:** warning, fine, seizure/impound, disqualification, raid/shutdown, arrest/exile or setting-authored response;
- **odds confidence:** regulated/certified markets may have better transparency; illicit markets may have uncertain books, manipulated odds, insider action or settlement risk.

These variables may affect entry, available wagers, payout, reputation, faction relations, sponsor offers, NPC behavior, law-enforcement attention, event presentation and post-event consequences.

MRC authority is setting-specific. Other worlds/factions may provide different regulator profiles or no regulator at all.

### GM control over regulator complexity

MRC and other regulator systems are **optional campaign overlays**, never prerequisites for using the underlying games, races or wager markets.

The GM may select a regulator profile at campaign, venue, event or market scope:

- **off** — ignore MRC/regulator taxes, licensing, sponsorship, enforcement, integrity bureaucracy and related consequences; keep only the game/race/wager mechanics;
- **light** — use selected flavor/visibility elements such as sanction labels, officials, prestige or simple house/tax effects without full enforcement simulation;
- **custom** — individually enable or disable taxes/fees, licensing, sponsorship, Steward/official presence, integrity/fixing rules, enforcement heat, prestige/access and other regulator modules;
- **full** — use the complete authored MRC/regulator rules for the applicable jurisdiction.

Content may recommend a default profile for setting fidelity, but the GM can override it unless a specific campaign/adventure rule explicitly makes that regulator behavior part of the scenario contract.

Disabling regulator modules must not disable the underlying race, competition, game, wager market, settlement, replay or multiplayer behavior.

## Existing runtime seams to consume

### GPR

Use the completed Gameplay Pattern Runtime rather than creating a parallel minigame engine.

- GPR-08 supports `embedded-minigame` and `user-authored-loop-mini` delivery modes with participants, objectives, operations, resources, rules and rewards.
- GPR-12 supplies single-player/host-authoritative/server-authoritative/GM-authoritative continuity, synchronized commands, replay receipts and deterministic recovery.

Games are data/configuration plus bounded game-specific resolution modules over shared pattern primitives.

External-event wagering binds to the owning event runtime instead of cloning its resolution.

### Economy and owner domains

Use the current MIB-13 economy runtime for currencies, assets and services, including reservation intents, atomic settlement, version checks, idempotency/retry and receipts.

The current economy consumer contract is explicitly in-game-only and records `realMoneySpentCents: 0`. The Development Bible also keeps subscription entitlement separate from in-world ownership.

Do not force every fictional stake into currency. Stakes owned by another canonical domain must use typed reservation/settlement adapters to that owner domain; Games & Wagering orchestrates but does not become the canonical owner of memories, traits, reputation, identity, vehicles, eggs/offspring, etc.

### Persistence and authority

- Campaign games/markets settle through ordinary campaign/session event authority and persist/recover with the campaign.
- Free Play wallets, preferences and local statistics persist through the product local-store boundary but are isolated from campaign state and resettable.
- Authoritative random, hidden-information or external-event outcomes are recorded as receipts/events with deterministic/replay identifiers. Do not regenerate an already-authoritative result.
- House/dealer/NPC participants, bookmakers and two-human tables use the same current participant/authority model as other GPR activities.

## Shared game and market primitives

The framework should provide composable primitives rather than a separate engine per game:

- cards/decks/hands;
- dice and other randomizers;
- wheels/tracks/boards;
- simultaneous or hidden choice;
- betting rounds and stake escalation;
- bluffing/information asymmetry;
- auctions and bidding;
- press-your-luck/cash-out;
- fixed-odds and pari-mutuel pools;
- proposition/side markets and futures;
- racing/sports/arena books;
- spatial/token placement;
- score/round/match/tournament flow;
- dealer/house/bookmaker/NPC behavior;
- cheating, fixing, collusion and insider-information adjudication hooks;
- regulator/jurisdiction hooks.

Game definitions declare flow, legal actions, stake rules, information visibility, settlement mapping, presentation metadata and provenance.

## Multiversal wagering examples

These examples establish breadth; they are not a closed catalog.

### Scarcity and subsistence wagering

Destitute or rationed populations may wager government/charity subsistence credits, meal allotments, ration chits or food-assistance balances when the setting permits it. A local game might use a bingo/lottery-like structure without using modern Earth program branding.

Possible fictional names include **Ration Grid**, **Allotment Draw**, **Meal-Chit Squares**, **Provision Pool** or setting-authored equivalents.

The wager engine treats these as ordinary in-world value owned by the relevant economy/social-service domain. The surrounding setting determines legality, desperation, stigma, exploitation, mutual-aid character or enforcement response.

### Egg and hatch betting

Markets may exist around eggs of exotic creatures: hatch timing, viable hatch count, coloration/morphology, capability traits, pedigree, racing potential or other setting-authored outcomes.

Some egg-laying sapient species may also have illegal or culturally specific betting around offspring eggs. Those are represented as sentient-progeny/guardianship-sensitive content rather than ordinary inventory. The wagering runtime must not silently transfer ownership of a sapient child; any custody, guardianship, crime, trafficking, ransom or protection consequence remains with the owning character/social/legal domains.

Black-market egg pools can therefore create investigation, crime, rescue, reputation and faction consequences in addition to payout.

### Title-stake and pink-slip racing

Races may allow vehicle-title stakes: winner takes ownership, lease, salvage rights, lien, upgrade rights, crew contract or another authored asset interest.

Settlement uses the canonical vehicle/asset owner domain with reservation before the race and atomic transfer only after an authoritative finish. A destroyed, impounded, stolen, disputed or ineligible vehicle follows authored no-contest/alternate-settlement rules rather than duplicating or losing ownership state.

### Event books across Multiversal

Markets may attach to:

- MRC races and unsanctioned/pirate races;
- vehicle, mount, beast, foot, flight, dimensional or reality-bending races;
- arena/combat events;
- creature shows, beast battles and hatch contests;
- crafting, cuisine, performance and skill competitions;
- exploration/expedition milestones;
- tournaments and seasonal festivals;
- faction competitions and fictional political contests;
- campaign events explicitly marked as bettable by the GM/content.

The owning system resolves the event; Games & Wagering resolves the market.

## Starter content requirement

PCV-06 ships a substantial Earth starter pack, including at minimum representative implementations from blackjack, roulette, baccarat, craps, poker variants, video poker, slots, keno, sic bo, pai gow, three-card poker and casino-war style play.

It also ships a Black Vegas/Multiversal starter pack. Initial approved design candidates include:

- **Event Horizon** — press-your-luck orbital probability game;
- **Seven Reflections** — several possible hands collapse as players commit choices;
- **Memory Market** — bluff/auction play around hidden memories;
- **Gravestones** — dice whose results alter the probability behavior of other dice;
- **Three Futures** — wagers move among simultaneous possible outcomes before resolution;
- **The Last Door** — escalating door/choice press-your-luck game;
- **Coliseum Book** — wagering on arena bouts, races or other governed campaign events;
- **Ration Grid / Allotment Draw family** — setting-authored scarcity/subsistence-credit games;
- **Hatch Pools** — regulated or illicit creature/egg outcome markets;
- **Title Run** — race format with vehicle/asset-interest stakes.

These are starter content, not a ceiling. Other settings may register their own game packs, wagering customs, event markets and regulators.

## PCV tranche integration

### PCV-06 — usable runtime

Deliver the real playable runtime, campaign settlement, Free Play wallet, external-event betting markets, optional regulator/jurisdiction projections, starter Earth/Multiversal packs, NPC/house/bookmaker play, multiplayer continuity and failure/recovery behavior. The GM can turn regulator systems fully off, use a light profile, configure individual modules, or use the full authored system without disabling the underlying games/races/markets. A functional phone/desktop surface is required even though final presentation convergence occurs later.

### PCV-07 — authoring

Expose governed authoring for game definitions, BettableEvent adapters, wager markets, legal stake classes, table/venue configuration, regulator/jurisdiction profiles and their off/light/custom/full module defaults, house rules, dealer/bookmaker/NPC profiles and reusable game/market packs through MRCS/Content Forge boundaries. Campaign-local authoring remains distinct from reusable/canonical publishing authority.

### PCV-09 — product presentation

Converge a generic Games & Wagering browser/table/book experience plus venue-aware skins/presentation such as Black Vegas. Campaign Play vs Free Play must be explicit. Hidden information, market status, sanction/jurisdiction, risk, reconnect/recovery and responsive phone/desktop behavior must be coherent.

When enabled, MRC-sanctioned racing books should feel different from pirate/black-market books through presentation, access, inspection, sponsor presence, taxes, odds confidence and enforcement consequences. The GM-selected regulator profile must be visible/configurable without cluttering ordinary game play when the profile is off.

No purchase, deposit, cash-out or real-money wagering affordance is permitted.

### PCV-10 — installed proof

On installed Windows and Android builds prove:

- at least one Earth intrinsic game;
- at least one Black Vegas/alien intrinsic game;
- at least one wager market bound to an independently resolved Multiversal event;
- a campaign-funded wager whose result persists correctly;
- a Free Play wallet reset that does not mutate campaign state;
- a two-human or host-authoritative table/book with disconnect/reconnect/replay continuity;
- prove regulator modularity by running one applicable MRC/event market with the regulator profile enabled and proving the same underlying game/race/market remains usable with the regulator profile off;
- zero real-world-value stake or payout paths.

## Design boundaries

- Do not create a Black Vegas-only engine.
- Do not duplicate GPR authority, economy ownership, inventory ownership, vehicle ownership, identity ownership, event-result authority or other canonical owner domains.
- Do not treat the resettable Free Play wallet as campaign money.
- Do not block fictional campaign stakes merely because they are unusual; validate them through their owning domain.
- Do not treat sapient offspring/children as ordinary transferable inventory merely because a wager references an egg.
- Do not let the wagering layer decide an external race/contest/event result.
- Do not flatten MRC-sanctioned, local-legal, tolerated, unsanctioned and criminal markets into the same play feel when regulator modules are enabled.
- Do not require the GM to use MRC/regulator taxes, licensing, sponsorship, enforcement, integrity or other overlays merely to use games, races or wager markets.
- Do not introduce real-world-value gambling.
- Do not start PCV-06 work while PCV-01 remains the authorized current tranche.
