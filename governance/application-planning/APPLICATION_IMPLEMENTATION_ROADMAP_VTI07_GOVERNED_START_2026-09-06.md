# Application Implementation Roadmap — VTI-07 Governed Start

**Work item:** VTI-07 — Permissions, Hidden Information & GM Authority  
**State of this commit:** acceptance-only governed-start contract; production mutation remains locked pending genuine matching application RED.  
**Application baseline:** `1e325045b2fc65d067a5e587f8cde78dcba9f766`  
**Implementation branch after this AIOC governed start validates and merges:** `integration/vti-07-permissions-hidden-information-gm-authority`

## Bounded objective

VTI-07 preserves canonical Multiversal ownership, consent, visibility, authorization, hidden-information and GM-authority decisions across provider-neutral derivative external-VTT presentation. It does not create a second permission engine and does not make an external VTT authoritative for permissions, adjudication or hidden state.

## Acceptance-only authority opened by this governed start

- create the registered VTI-07 application branch from the exact application baseline only after this AIOC governed start merges;
- add the bounded VTI-07 acceptance profile, fixtures, invariant verifier and tests;
- define provider-neutral authorization-presentation envelopes that consume canonical Multiversal decisions;
- prove hidden counts/content, redacted identities and GM-only material fail closed with no inference channel;
- prove unsafe target fidelity downgrades to explicit `redacted` or `unsupported`;
- prove expected absence of the VTI-07 production contract by genuine matching Linux and Windows RED before production mutation authority opens.

## Production authority remains locked until matching RED

The following remain unauthorized before matching RED is sealed:
- production permission/hidden-information/GM-authority preservation implementation;
- a new or parallel permission, ownership, consent, visibility, adjudication or hidden-state authority engine;
- provider-specific schemas, vendor selection/ranking, credentials, external accounts or adapter implementation;
- live external synchronization mutation or canonical game-state mutation;
- durable VTI persistence or a new migration;
- provider activation, tester distribution, release or deployment;
- VTI-08+ and SGC-01+ implementation.

## Canonical-authority reuse requirement

VTI-07 must consume existing canonical Multiversal authorization, visibility, ownership, consent and GM-authority decisions. Hidden information must remain fail-closed, and an external VTT's weaker capability may only reduce fidelity; it may never broaden disclosure or authority.

## Exact next action after this governed start merges

Create `integration/vti-07-permissions-hidden-information-gm-authority` from exact application main `1e325045b2fc65d067a5e587f8cde78dcba9f766`, add acceptance-only VTI-07 validation, and obtain genuine matching self-hosted Linux/Windows RED before any production permission-preservation code is authorized.
