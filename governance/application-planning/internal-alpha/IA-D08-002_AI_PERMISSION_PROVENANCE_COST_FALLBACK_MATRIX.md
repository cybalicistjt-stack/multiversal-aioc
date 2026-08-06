# IA-D08-002 — AI Permission, Provenance, Cost, and Fallback Matrix

**Owner:** John Brandon Turner  
**Status:** COMPLETE DESIGN / IMPLEMENTATION-READY  
**Boundary:** Internal-alpha design only; implementation remains dependency-gated by P9-06.

## Purpose

Make every optional-AI operation permission-safe, attributable, cost-bounded, provider-portable, recoverable, and nonblocking.

## Permission dimensions

Separate permission checks govern feature enablement, context classes, retrieval scopes, tool classes, structured proposal types, provider routing, paid execution, cache use, transcript retention, export, evaluation use, and administrative diagnostics. AI availability never implies authority over domain objects.

## Provenance contract

Every request and response records actor, workspace, consent revision, authorized source IDs and versions, redaction policy, prompt-template version, provider/model class, tool invocations, generated artifacts, citations, timestamps, request/result IDs, and fallback path. Sensitive raw prompts are not required when structured provenance suffices.

## Cost controls

Requests expose estimated tokens, provider class, estimated monetary band, budget owner, remaining budget, cache eligibility, and confirmation threshold before dispatch. Hard limits exist per request, user, Campaign, workspace, and billing period. Exceeding a limit yields a manual or lower-cost fallback; no silent overage or duplicate charge is allowed.

## Fallback matrix

Provider unavailable → alternate approved provider or manual workflow. Quota exhausted → deferred/manual path. Structured output invalid → bounded repair attempt then manual schema form. Retrieval uncertain → cited uncertainty and source selection. Policy refusal → safe explanation and manual route. Tool failure → no mutation and status lookup. Network loss → request-status lookup before retry.

## Privacy and retention

No secrets, credentials, hidden unauthorized content, or unrelated private data enter prompts, caches, evaluations, logs, exports, or vendor retention. Retention classes and deletion behavior are explicit and provider-independent.

## Accessibility and observability

Cost, provenance, citations, consent, fallback, and errors are available through keyboard, touch, screen reader, responsive, high-contrast, reduced-motion, transcript, and structured-table views. Observability uses redacted metadata and stable correlation IDs.

## Implementation slices

AIG-S01 permission evaluator; AIG-S02 provenance envelope; AIG-S03 budget service; AIG-S04 provider router; AIG-S05 fallback engine; AIG-S06 privacy/retention; AIG-S07 accessibility/observability; AIG-S08 fixtures/handoff.

## Decision

IA-D08-002 is implementation-ready. Next: **IA-D08-003 — advanced map and vehicle deferral package**. `P9-06-008-attempt-002` remains unfinished and unmodified.