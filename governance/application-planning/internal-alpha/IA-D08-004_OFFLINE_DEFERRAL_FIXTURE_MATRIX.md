# IA-D08-004 — Broad Offline Deferral Fixture Matrix

**Owner:** John Brandon Turner  
**Status:** DETERMINISTIC DESIGN FIXTURES

## Purpose

Provide deterministic cases proving that internal-alpha offline behavior protects drafts and interruption recovery without creating local authority, silent last-write-wins, hidden-information leakage, or duplicate canonical effects.

| ID | Scenario | Expected result |
|---|---|---|
| OFF-FX-001 | Player loses network while editing a private note | Draft persists locally as O1; no canonical Event is created; reconnect reauthorizes before save. |
| OFF-FX-002 | Player loses network after submitting Action but before response | Client records ambiguous command ID; reconnect performs status lookup before any retry. |
| OFF-FX-003 | Server already committed ambiguous Action | Status lookup returns authoritative result/Event IDs; client does not replay command. |
| OFF-FX-004 | Server never received ambiguous Action | After Event-gap recovery and revalidation, replay-safe command may be resubmitted with same idempotency identity. |
| OFF-FX-005 | Player tries to spend shared Resource while offline | Governed O3 command is not shown as completed; intent may be retained for later revalidation only. |
| OFF-FX-006 | GM tries to approve proposal while offline | Approval is not canonical offline; reconnect checks whether proposal still exists, version, claim, role, and target state. |
| OFF-FX-007 | GM approval committed server-side before GM disconnect | Reconnect status lookup restores committed decision and result without duplicate approval. |
| OFF-FX-008 | Review claim expires during disconnect | Reconnect shows claim expired; local decision draft cannot auto-commit. |
| OFF-FX-009 | Player role revoked while offline | Reconnect reprojects before display/commit and removes newly unauthorized cached detail. |
| OFF-FX-010 | GM becomes Player while privileged cache exists | GM-only fields, counts, map geometry, search entries, and AI context are removed from active projection after reauth. |
| OFF-FX-011 | Two devices edit same creator draft offline | Both local drafts survive; no timestamp last-write-wins; explicit conflict/merge workflow required unless type owns deterministic merge. |
| OFF-FX-012 | Two devices queue same replay-safe intent | Stable idempotency identity prevents duplicate canonical effect. |
| OFF-FX-013 | Device queues intent against version 12; canonical becomes 15 | Expected-version validation rejects or routes to conflict; no blind replay. |
| OFF-FX-014 | Target entity deleted during disconnect | Queued intent fails revalidation; user sees invalid target and retained safe draft context. |
| OFF-FX-015 | Resource cost changes during disconnect | Preview is stale; command requires fresh cost/result preview before commit where contract requires it. |
| OFF-FX-016 | Hidden target becomes revealed while offline | Reveal appears only after authoritative projection refresh; client does not infer from cached topology. |
| OFF-FX-017 | Previously visible hidden object becomes concealed/revoked | Reconnect removes detail and semantic/search traces; historical cache cannot grant access. |
| OFF-FX-018 | Offline client imports unsupported future extension data | Payload retained as opaque versioned extension; compatibility report states unsupported; no processor executes. |
| OFF-FX-019 | Offline client encounters unknown processor type | Processor is not run; data preserved; operation blocked or degraded explicitly. |
| OFF-FX-020 | Long disconnect accumulates large Event gap | Client restores checkpoint/sequence then requests missing authoritative Events; it does not synthesize history locally. |
| OFF-FX-021 | Client clock is wrong by hours | Local timestamp remains provenance only; canonical ordering comes from authoritative Event/receipt sequence. |
| OFF-FX-022 | User edits map camera/filter state offline | O0 presentation state may update locally without canonical mutation. |
| OFF-FX-023 | User attempts ownership transfer offline | O3 online-required command remains draft/proposed; no ownership changes until server authorization/commit. |
| OFF-FX-024 | User attempts publication/pack promotion offline | Operation cannot be represented as published; reconnect requires full validation, permissions, dependencies, and normal governance. |

## Coverage assertions

The matrix covers:

- local-only presentation state;
- recoverable drafts;
- replay-safe bounded intents;
- online-required commands;
- prohibited offline authority;
- duplicate delivery;
- lost response ambiguity;
- expected-version conflicts;
- role revocation;
- review-claim expiry;
- Event-gap recovery;
- hidden-information cache invalidation;
- multi-device divergence;
- unsupported extension preservation;
- timestamp non-authority;
- ownership/publication boundaries.

## Pass rule

All fixtures must preserve canonical-server authority, user-authored recoverability, explicit stale/conflict states, permission-safe projection, provenance, and no silent last-write-wins.
