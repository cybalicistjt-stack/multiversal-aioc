# Internal Alpha Scope

**Program:** MV-IA-001  
**Version:** 0.1.0  
**Status:** DESIGN BASELINE  
**Owner:** John Brandon Turner

## 1. Alpha purpose

Internal alpha is the first controlled release in which approved internal testers use a coherent Multiversal product rather than isolated platform tests or mock screens.

It must prove that a Player and Game Master can prepare, enter, conduct, save, interrupt, recover, and resume meaningful play using real governed objects and persistent state.

## 2. Minimum product promise

The internal-alpha product promise is:

> A Game Master can create or open a Campaign, invite a Player, prepare a Scene with real governed content, and launch a Session. The Player can create or open a Character, enter the Session, propose an Action, and receive a persistent result after the GM approves, denies, or modifies it. Both participants can disconnect, reconnect, and safely continue.

## 3. Entry-critical release slice

Internal alpha may not begin until the following integrated slice exists:

1. responsive application shell and workspace navigation;
2. identity entry and role-aware workspace selection;
3. content-pack and entitlement resolution for the approved alpha corpus;
4. universal object browser, inspector, and picker;
5. bounded Character creation and Character workspace;
6. Campaign creation, invitations, and permissions;
7. Scene creation with real objects and hidden-information controls;
8. live Session entry for distinct Player and GM identities;
9. Action proposal and GM approval, denial, and modification;
10. authoritative persistent result and role-filtered updates;
11. autosave, save/load, disconnect/reconnect, and recovery states;
12. accessible desktop and mobile completion of the primary journey;
13. backup, restore, and provider-exit evidence required by the active gates;
14. tester onboarding, issue reporting, diagnostics, and known limitations.

## 4. Alpha-required breadth

The following do not all have to be complete before the first internal-alpha session, but must be implemented and tested before the internal-alpha program may close:

- complete bounded combat encounter;
- personal inventory and equipment;
- shared inventory, ownership, custody, and transfers;
- basic vehicles as shared Assets and Scene participants;
- Relationship Tracker;
- structured Social Interaction Mode;
- Investigation and Clue Board;
- faction standing and reputation;
- Encounter Builder and bounded balance review;
- Adventure and story-flow state;
- at least one Downtime, Crafting, or Project workflow;
- basic World and Setting Builder workflow using governed objects;
- pack installation, update, migration, blocked removal, safe removal, and reinstall;
- internal-alpha accessibility and performance hardening.

## 5. Experimental internal-alpha features

Experimental features may be enabled for selected testers without becoming release blockers unless explicitly promoted:

- governed AI assistance;
- advanced map editing and tactical overlays;
- advanced vehicle, mecha, and starship station operations;
- broad offline authoring and conflict-aware synchronization;
- advanced encounter simulation and recommendation;
- automated world or adventure drafting;
- optional creator submission and packaging flows beyond the bounded alpha corpus.

Experimental features must remain permission-aware, reversible, visibly labeled, and independently disableable.

## 6. Deferred beyond internal alpha

The following remain outside the current internal-alpha commitment:

- public registration;
- public content marketplace;
- creator payouts;
- production billing;
- public community discovery;
- full moderation operations;
- App Store or public mobile distribution;
- unlimited platform scale;
- production support guarantees;
- final formal accessibility conformance claim;
- final balance claim;
- complete coverage of every optional subsystem and setting;
- autonomous AI mutation of Campaign or canonical state.

## 7. Content boundary

Internal alpha uses a bounded, version-pinned content corpus sufficient to test:

- Character creation;
- Actions, Effects, Conditions, and Resources;
- creatures and NPCs;
- items and equipment;
- environments;
- at least one Campaign and adventure path;
- combat and noncombat Scenes;
- relationships and factions;
- pack lifecycle and provenance.

Canonical, Campaign-local, sample, fixture, and AI-proposed content must be visually distinguishable.

## 8. Role boundary

Required roles:

- Owner/Admin;
- Game Master;
- Player.

Optional internal-alpha roles:

- Content Creator;
- Assistant GM;
- Observer or reviewer.

Every role must receive only authorized capabilities and projections.

## 9. Device boundary

The minimum device matrix includes:

- desktop browser;
- mobile browser;
- two distinct connected clients representing Player and GM;
- keyboard-only use of primary workflows;
- touch use of primary workflows;
- at least one screen-reader review path.

Native Apple packaging is handled by the separate WP-011 track and is not an entry condition unless later approved.

## 10. Quality boundary

Internal alpha must preserve honest distinctions among:

- designed;
- implementation-ready;
- implemented;
- validated;
- alpha-ready;
- released to testers.

A feature cannot be called alpha-ready merely because its UI exists.

## 11. Internal-alpha success

The internal-alpha program succeeds when:

- the core Player and GM journey completes without development-only tools;
- accepted state remains durable and recoverable;
- hidden information remains protected;
- the selected combat and noncombat workflows produce persistent consequences;
- pack and data lifecycle operations preserve integrity;
- blocking defects are zero or owner-held with explicit evidence;
- accessibility, performance, cost, privacy, and security evidence supports the bounded tester scope;
- John Brandon Turner approves the exact internal-alpha disposition.

## 12. Nonauthorization

This scope document does not authorize the internal-alpha release itself. Release remains an owner-gated decision bound to an exact candidate, environment, tester group, evidence package, and rollback plan.