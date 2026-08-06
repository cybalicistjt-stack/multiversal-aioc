# IA-D07-004 — World/Adventure Content Authority Matrix

**Owner:** John Brandon Turner  
**Status:** COMPLETE DESIGN / IMPLEMENTATION-READY

## Purpose

Prove consistent authority across World and Setting Management, Adventure and Module Management, and Creator/Campaign-local Content.

## Authority dimensions

The matrix separates ownership, authorship, edit, review, publish, install, enable, reveal, runtime advance, export, import, deprecate, delete, and canonical-promotion authority. No role inherits one dimension merely by holding another.

## Source classes

Canonical source, private creator release, Campaign-local object, Campaign overlay, published adventure version, campaign run state, imported content, and historical tombstone remain visibly distinct and provenance-complete.

## Core rules

1. Published source versions are immutable.
2. Campaign runs and overlays never mutate source definitions.
3. Creator approval produces bounded installable content, not canonical promotion.
4. Reveal and runtime progression are server-authoritative and independent from authoring rights.
5. Hidden content is filtered before aggregation, graph traversal, search, previews, exports, diagnostics, notifications, and optional-AI context.
6. Source updates require explicit reviewed migration for pinned Campaign bindings.
7. Disablement blocks new use but preserves historical interpretation.
8. Reversal uses compensating Events; history is never silently rewritten.
9. Canonical promotion requires John Brandon Turner and is outside internal-alpha authorization.
10. `P9-06-008-attempt-002` remains unfinished and unmodified.

## Conflict precedence

Runtime Campaign authority may choose installed versions and local overlays but cannot rewrite upstream source. Source owners may publish successors but cannot silently migrate Campaigns. Reviewers may accept or reject proposals but cannot reveal content or advance runs. GMs may reveal and advance authorized Campaign state but cannot publish creator releases or promote canonical content.

## Atomic operations

Publish, install, migrate, reveal, advance, reward, disable, import, and export each produce one authoritative result group with expected versions, idempotency, ordered mutations, Events, role-filtered projections, provenance, and recovery status.

## Accessibility and recovery

Every authority decision and conflict is operable through list, table, detail, diff, dependency outline, review queue, keyboard, touch, screen reader, responsive, high-contrast, reduced-motion, and nonvisual flows. Lost responses use status lookup; Event gaps use snapshot-plus-tail repair.

## Decision

The authority model is coherent and implementation-ready. Next: **IA-D07-005 — authoring integration review**.