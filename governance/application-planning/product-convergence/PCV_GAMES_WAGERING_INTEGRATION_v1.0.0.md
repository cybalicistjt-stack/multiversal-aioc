# PCV Games & Wagering Integration

**Document ID:** PCV-GW-01  
**Version:** 1.0.0  
**Status:** OWNER-APPROVED CROSS-TRANCHE PRODUCT REQUIREMENT  
**Owner direction:** 2026-09-24  
**Primary delivery tranche:** PCV-06  
**Consuming tranches:** PCV-07, PCV-09, PCV-10  
**PCV-01 rule:** Track as an approved deferred journey only; this document does not authorize premature PCV-06 implementation.

## Product intent

Multiversal shall provide one reusable **Games & Wagering** framework capable of running ordinary Earth casino/table games and setting-specific or invented games, with **Black Vegas** as a flagship venue/catalog rather than a separate incompatible casino application.

The same game definition and runtime must work in two contexts:

1. **Campaign Play** — participants may stake actual validated in-world character/campaign wealth or other fictional assets. Settlement mutates the canonical owning domains and persists as campaign history.
2. **Free Play** — participants use an isolated fake wallet with an arbitrary starting balance. It may be reset at will and never mutates campaign wealth/state.

The only categorical wagering prohibition is real-world value.

## Real-world-value boundary

A stake or payout is invalid when it is any of the following:

- real-world money;
- currency/credit/token purchased for real-world money or representing subscription/entitlement value;
- cash-redeemable or externally redeemable value;
- value directly convertible into any of the above.

Ordinary fictional/in-world currencies, abstract wealth, items, services, favors, debts, contracts, reputation, memories, traits, time/lifespan, soul fragments, alternate-self consequences, and GM-defined fictional stakes may be supported when a canonical owner-domain adapter exists and validates reservation/settlement.

Games & Wagering must never create a cash-out path.

## Existing runtime seams to consume

### GPR

Use the completed Gameplay Pattern Runtime rather than creating a parallel minigame engine.

- GPR-08 already supports `embedded-minigame` and `user-authored-loop-mini` delivery modes with participants, objectives, operations, resources, rules and rewards.
- GPR-12 already supplies single-player/host-authoritative/server-authoritative/GM-authoritative continuity, synchronized commands, replay receipts and deterministic recovery.

Games are therefore data/configuration plus bounded game-specific resolution modules over shared pattern primitives.

### Economy and owner domains

Use the current MIB-13 economy runtime for currencies, assets and services, including reservation intents, atomic settlement, version checks, idempotency/retry and receipts.

The current economy consumer contract is explicitly in-game-only and records `realMoneySpentCents: 0`. The Development Bible also keeps subscription entitlement separate from in-world ownership.

Do not force every fictional stake into currency. Stakes owned by another canonical domain must use typed reservation/settlement adapters to that owner domain; Games & Wagering orchestrates but does not become the canonical owner of memories, traits, reputation, identity, etc.

### Persistence and authority

- Campaign games settle through ordinary campaign/session event authority and persist/recover with the campaign.
- Free Play wallets, preferences and local statistics persist through the product local-store boundary but are isolated from campaign state and resettable.
- Authoritative random or hidden-information outcomes are recorded as receipts/events with deterministic/replay identifiers. Do not regenerate an already-authoritative result.
- House/dealer/NPC participants and two-human tables use the same current participant/authority model as other GPR activities.

## Shared game primitives

The framework should provide composable primitives rather than a separate engine per game:

- cards/decks/hands;
- dice and other randomizers;
- wheels/tracks/boards;
- simultaneous or hidden choice;
- betting rounds and stake escalation;
- bluffing/information asymmetry;
- auctions and bidding;
- press-your-luck/cash-out;
- racing/sports/arena book;
- spatial/token placement;
- score/round/match/tournament flow;
- dealer/house/NPC behavior;
- cheating detection/adjudication hooks.

Game definitions declare flow, legal actions, stake rules, information visibility, settlement mapping, presentation metadata and provenance.

## Starter content requirement

PCV-06 ships a substantial Earth starter pack, including at minimum representative implementations from blackjack, roulette, baccarat, craps, poker variants, video poker, slots, keno, sic bo, pai gow, three-card poker and casino-war style play.

It also ships a Black Vegas alien-game starter pack. Initial approved design candidates include:

- **Event Horizon** — press-your-luck orbital probability game;
- **Seven Reflections** — several possible hands collapse as players commit choices;
- **Memory Market** — bluff/auction play around hidden memories;
- **Gravestones** — dice whose results alter the probability behavior of other dice;
- **Three Futures** — wagers move among simultaneous possible outcomes before resolution;
- **The Last Door** — escalating door/choice press-your-luck game;
- **Coliseum Book** — wagering on arena bouts, races or other governed campaign events.

These are starter content, not a ceiling. Other settings may register their own game packs and venues.

## PCV tranche integration

### PCV-06 — usable runtime

Deliver the real playable runtime, campaign settlement, Free Play wallet, starter Earth/alien packs, NPC/house play, multiplayer continuity and failure/recovery behavior. A functional phone/desktop surface is required even though final presentation convergence occurs later.

### PCV-07 — authoring

Expose governed authoring for game definitions, legal stake classes, table/venue configuration, house rules, dealer/NPC profiles and reusable game packs through MRCS/Content Forge boundaries. Campaign-local authoring remains distinct from reusable/canonical publishing authority.

### PCV-09 — product presentation

Converge a generic Games & Wagering browser/table experience plus venue-aware skins/presentation such as Black Vegas. Campaign Play vs Free Play must be explicit. Hidden information, keyboard/touch/screen-reader operation, reconnect/recovery and responsive phone/desktop behavior must be coherent.

No purchase, deposit, cash-out or real-money wagering affordance is permitted.

### PCV-10 — installed proof

On installed Windows and Android builds prove:

- at least one Earth game;
- at least one Black Vegas/alien game;
- a campaign-funded wager whose result persists correctly;
- a Free Play wallet reset that does not mutate campaign state;
- a two-human or host-authoritative table with disconnect/reconnect/replay continuity;
- zero real-world-value stake or payout paths.

## Design boundaries

- Do not create a Black Vegas-only engine.
- Do not duplicate GPR authority, economy ownership, inventory ownership, identity ownership or other canonical owner domains.
- Do not treat the resettable Free Play wallet as campaign money.
- Do not block fictional campaign stakes merely because they are unusual; validate them through their owning domain.
- Do not introduce real-world-value gambling.
- Do not start PCV-06 work while PCV-01 remains the authorized current tranche.
