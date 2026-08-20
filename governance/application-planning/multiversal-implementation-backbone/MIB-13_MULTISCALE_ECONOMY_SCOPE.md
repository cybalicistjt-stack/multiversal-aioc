# MIB-13 — Multiscale Economy Scope Model

**Status:** OWNER-APPROVED REQUIREMENT
**Applies to:** MIB-13 Economy and Trade Deterministic Engine
**Approved:** 2026-08-20

## Requirement

MIB-13 must support economies whose effective scope may be smaller than a world or may span multiple worlds and realities. Economic scale is therefore a governed data property, not an engine mode.

The same economy engine must be able to represent, compose, query, and transact across scopes such as:

- settlement, district, city or local market;
- region, nation or continent;
- world or planetary economy;
- multi-world, system, interplanetary or interstellar economy;
- branch/reality-local economy;
- cross-reality or multiversal trade network.

No separate continent, planetary, space, or multiversal economy engine may be introduced.

## Canonical economic-scope model

An `EconomicScope` is a stable, versioned definition/reference describing the jurisdiction or market domain in which economic rules apply. A scope may have a parent scope and may participate in explicit trade links to peer or foreign scopes.

Minimum scope attributes:

- stable scope ID and version;
- scope kind/classification;
- parent scope, when one exists;
- associated World/Reality/semantic-location references from the MIB-11 taxonomy rather than duplicated geography truth;
- permitted currencies and conversion policies;
- market/price modifier profile references;
- availability and scarcity profile references;
- import/export restrictions and legality policy references;
- tax/tariff/fee profile references where rules define them;
- explicit trade-route or market-link references;
- isolation/access constraints;
- provenance and visibility metadata.

Scopes form a hierarchy for inheritance but do not imply universal connectivity. A child market may inherit defaults from a continent or world while still having its own prices, availability, currency or restrictions.

## Cross-scope trade

Transactions crossing economic scopes must resolve an explicit route/policy chain. Cross-scope trade may account for deterministic rule-defined effects including:

- currency conversion;
- local price differences;
- scarcity/abundance;
- transport or transfer cost;
- distance/travel tier;
- tariffs, taxes and duties;
- embargoes, legality and permissions;
- route availability;
- dimensional/portal access;
- time or delivery constraints;
- risk/insurance/service modifiers when defined.

A cross-reality transaction is not special-cased mechanically. It is a transaction whose source and destination scopes reference different Reality/Branch contexts and whose declared route/policy permits that exchange.

## Authority boundaries

- MIB-11 remains the owner of Reality/Branch/World classification and semantic-location identity.
- D17 remains the owner of live asset/inventory truth.
- MIB-13 owns economy/trade definitions, price/availability calculations, economic transaction contracts, and their receipts/status.
- Later ICF content supplies ingredient/crop/livestock/production valuation and trade metadata but does not own transaction authority.
- Later MIB-14 vehicle/base systems may supply transport/storage/capacity facts but do not own market authority.
- Later CEL may consume MIB-13 price, availability, budget, order, settlement and status seams but does not become an economy ledger.
- Real-money/payment commerce remains out of scope.

## Determinism and replay

A transaction must bind the exact economic scope IDs and versions, currency/conversion rules, price/availability inputs, route/policy inputs and owner-domain versions that produced its quote or settlement. Replaying the same accepted inputs must produce the same economic result, and retries/ambiguous responses must not duplicate settlement.

## Required MIB-13 acceptance coverage

MIB-13 fixtures/tests must include at least:

1. a local market transaction within one settlement/region;
2. a transaction whose price/availability inherits from a continental or world scope with a local override;
3. a transaction between two distinct world/planet scopes;
4. a cross-reality transaction through an explicitly permitted route;
5. a disconnected/embargoed cross-scope transaction that fails closed;
6. currency conversion across scopes;
7. stale scope/policy/version rejection;
8. retry/lost-response recovery proving no duplicate settlement across any of the above.

## Design consequence

Economic scale must be data-driven and composable. A GM or content pack should be able to define a single isolated village economy, a continent-wide common market, a planetary currency union, several partially connected worlds, or a multiversal trade network by registering scopes and links rather than changing engine code.
