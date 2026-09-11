# MIB-09 / MNCS Party-Association Reputation Integration Amendment — 2026-09-11

**Status:** OWNER-APPROVED DOWNSTREAM INTEGRATION REQUIREMENT  
**Reopens MIB-09:** no  
**Implementation authority:** none

## Purpose

Preserve the owner's requirement that, within a Campaign, one player Character's actions can affect another party member's reputation with a specific group/faction when the owning reputation rules treat party association as relevant.

MIB-09 remains the completed deterministic Relationship/Reputation engine owner. MNCS must consume that engine rather than creating a separate reputation ledger.

## Required model

A reputation projection may incorporate separately attributable components such as:

- the target Character's direct reputation;
- association-derived influence from membership in the relevant party/group at the time of an Event;
- faction-specific collective-responsibility, fame, gratitude, suspicion or similar authored modifiers;
- source Event and initiating Character attribution;
- Campaign and party/group scope;
- visibility/reveal rules;
- trend/history/provenance receipts.

## Invariants

1. No account-global or cross-Campaign spillover.
2. No universal rule that every party member receives the same change.
3. Direct reputation is not overwritten by association-derived reputation.
4. Each faction/group may weight or ignore association according to its governed definitions.
5. Joining/leaving a party changes future association context; past consequences persist or decay only according to owning reputation rules.
6. Every propagated effect remains attributable and replayable where MIB-09 provides replay.
7. Hidden faction/reputation information is filtered before player-facing summaries, search/counts, diagnostics and optional-AI context.
8. MNCS-08 owns the creator/GM-facing integration and acceptance proof; MIB-09 retains mutation authority.

## Golden proof requirement

MNCS-24 must prove both:

- one Campaign in which PC-A's attributed action causes a faction-defined association effect on PC-B while their direct reputations remain distinct; and
- a second Campaign proving the effect does not cross Campaign scope.
