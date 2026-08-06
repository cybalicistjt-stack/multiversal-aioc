# IA-D08-001 — MV-IA-F023 Optional AI Assistant Boundaries and Interaction Contract

**Owner:** John Brandon Turner  
**Status:** COMPLETE DESIGN / IMPLEMENTATION-READY  
**Boundary:** Internal-alpha design only; implementation remains dependency-gated by P9-06.

## Purpose

Define an optional, non-authoritative AI assistant that can explain, summarize, draft, compare, suggest, and prepare proposals without independently changing canonical, Campaign, Character, Asset, World, Adventure, combat, permission, or release state.

## Core contract

1. AI is opt-in per user and per workspace context.
2. AI output is advisory until an authorized human explicitly submits or approves a normal governed operation.
3. AI cannot bypass permissions, hidden-information filters, proposal/approval, version checks, idempotency, provenance, or owner gates.
4. Context is assembled only from the requesting user’s authorized projection.
5. Every AI response records provider/model class, prompt-template version, authorized source references, timestamps, cost estimate, tool calls, and fallback outcome.
6. AI never receives secrets, credentials, hidden GM-only data, unrelated private content, or raw production diagnostics.
7. AI may prepare drafts and proposals, but cannot publish, promote, release, deploy, spend paid credits, destroy Assets, resolve combat, reveal secrets, or modify `P9-06-008-attempt-002`.

## Interaction modes

Explain, summarize, compare, brainstorm, draft, classify, retrieve-with-citations, propose structured edits, prepare encounter/world/adventure content, and diagnose bounded validation evidence. Each mode declares allowed inputs, output schema, authority boundary, provenance requirements, and fallback behavior.

## Human control

Users see what context classes will be sent, can exclude sources, can cancel before submission, inspect provenance, and convert results only into ordinary governed drafts or proposals. GM and owner authority remain separate from AI availability.

## Hidden information

Redaction occurs before retrieval, prompt construction, tool selection, token counting, caching, logging, evaluation, exports, notifications, and response assembly.

## Failure and fallback

Unavailable provider, timeout, quota, refusal, malformed output, uncertain retrieval, or policy conflict returns a bounded failure state and deterministic manual alternative. AI failure never blocks core non-AI workflows.

## Accessibility and recovery

Keyboard, touch, screen-reader, responsive, reduced-motion, high-contrast, transcript, citation list, structured diff, and nonvisual parity are required. Requests use idempotency keys and status lookup; no duplicate paid request is silently issued.

## Implementation slices

AI-S01 consent/context; AI-S02 authorized retrieval; AI-S03 provider abstraction; AI-S04 structured proposals; AI-S05 provenance/cost; AI-S06 safety/privacy/accessibility; AI-S07 fallback/recovery; AI-S08 fixtures/handoff.

## Decision

IA-D08-001 is implementation-ready. Next: **IA-D08-002 — AI permission, provenance, cost, and fallback matrix**. `P9-06-008-attempt-002` remains unfinished and unmodified.