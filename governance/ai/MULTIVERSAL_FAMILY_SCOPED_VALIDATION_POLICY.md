# Multiversal Family-Scoped Validation Policy

**Document ID:** MV-AI-FAMILY-VALIDATION-001  
**Version:** 1.0.0  
**Status:** ACTIVE — OWNER APPROVED  
**Effective:** 2026-08-27

## Purpose

Keep development sharp by establishing validation authority once when a tranche family begins, preserving that bounded surface through the family, and retiring it when the family ends. Historical proof remains evidence; it does not become permanent automatic ceremony.

## Family-entry rule

Before the first implementation tranche in a new family, establish one active family contract that declares:

- family identity and allowed profile prefix;
- the sealed predecessor application baseline;
- the remaining family work items;
- direct regressions that the new family can actually invalidate;
- the ordinary per-tranche validation shape;
- any explicit exceptional integration scope.

This is a family-boundary operation. It is not repeated for every tranche.

## Mid-family rule

Until the family completes, ordinary tranches:

1. may change exactly one active-family Validation Core profile;
2. run repository/execution-surface health and family-scope selection once;
3. run that one profile on self-hosted Linux and Windows;
4. compare deterministic receipts;
5. do not rerun completed predecessor validators merely because they are predecessors.

A mid-family scope review is required only when the current change touches a declared shared dependency whose proof can actually be invalidated, or when an explicitly reviewed integration tranche needs broader coverage.

## Sealed-proof rule

`completed_verified` predecessor proof is sealed at a known application baseline. Ordinary current-family validation proves that baseline remains in the candidate ancestry and that the active family contract has not been widened. Historical validators remain available through Git history but have no automatic execution authority.

If a completed predecessor's owning code or contract is materially changed, the family contract must explicitly declare the affected regression before the candidate may widen validation.

## Family-exit rule

When the final family tranche becomes `completed_verified`:

- seal the family completion baseline;
- retire the family's automatic validation authority;
- select the successor family/item according to the roadmap;
- establish the successor family contract only when its first tranche is governed-started.

No historical family may remain in automatic CI after retirement merely because its profiles or validators still exist.

## Single live application path

The ordinary application execution surface is one automatic project workflow:

`validate-current-family.yml`

It performs current repository health and family selection, then invokes at most one shared Validation Core profile. `_validation-core-profile.yml` is callable infrastructure, not an independent automatic project workflow.

## Control-plane maintenance lease

An owner-approved repository-health/control-plane remediation may set `exclusive_control_plane_maintenance=true`. While that lease is active, no selected feature tranche may be governed-started by another conversation. The lease is cleared only after the remediation is validated and merged.

## Failure disclosure

If a tranche cannot complete, the owner report must state, without requiring a diagnostic question:

- `BLOCKED AT` — exact operation/gate;
- `CAUSE` — classified reason;
- `WHY I CAN'T RESOLVE IT YET` — remaining limitation;
- `WHAT I ALREADY TRIED` — bounded recovery already performed;
- `NEED FROM YOU` — normally `nothing`, otherwise the exact owner-only action.

A merge-method rejection, queued CI, stale pointer, runner outage, unavailable tool, or external-service failure must not be left ambiguous.

## Complexity budget

A new permanent automatic gate must identify what it replaces or why an existing gate cannot cover the risk, and must include a retirement condition. Permanent gates may not accumulate by default.
