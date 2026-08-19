# APM-01 Review Receipt

**Work item:** APM-01 — Automated-Play Authority and Mode Contract  
**Attempt:** APM-01-attempt-001  
**Design branch:** `governance/apm-01-automated-play-authority`  
**Review state:** substantive design complete; repository/PR validation pending

## Reviewed source contracts

- APW-01 Authority, Account, Context and Terminology Canonicalization.
- APM owner-approved program and roadmap supplement.
- MV-IA-F005 Campaign, Scene, and Session Builder.
- MV-IA-F006 First Playable Action and GM Approval Loop.
- MV-IA-F020 Permissions and Hidden Information.
- MV-IA-F021 Autosave, Reconnect, Recovery, and Bounded Offline Use.
- IA-D08-001 Optional AI Assistant Boundaries and Interaction Contract.
- IA-D08-002 AI Permission, Provenance, Cost, and Fallback Matrix.

## Findings

1. Automated play can be additive over the existing Campaign/Action/Event architecture; no second state engine is required.
2. AutoGM must be a bounded mode/profile, not a Game Master role. The automation controller is a nonhuman service actor using explicit delegated capabilities and fresh owning-domain authorization.
3. Solo is participation topology, not role or authority. Connected Cozy is CozyMode with invited participants, not a new authority model.
4. Context, Cadence, Connectivity, participation topology and automated-play profile remain orthogonal.
5. A versioned `AutomationDelegationGrant` is required for state-affecting automation and cannot be widened by the controller itself.
6. Every automated operation is classified as automatic, bounded automatic, proposal-required, human-required, or prohibited.
7. Human intent/consent/ownership/high-impact and owner-reserved decisions remain mandatory human choices unless a later owning-domain contract explicitly defines a narrower safe rule.
8. Deterministic/domain-owned systems remain responsible for legality, state mutation, Event acceptance, idempotency, permissions and recovery.
9. Optional AI remains presentation/proposal assistance. It does not acquire mechanical, decision, permission, delegation, or hidden-state authority.
10. AutoGM hidden scenario truth is separated from optional AI: a governed deterministic scenario/controller projection may consume machine-private package state, while AI receives only task-filtered presentation context by default.
11. Exit/disconnect is not background-play permission. Initial AutoGM defaults to foreground-only; any background Cozy progression is explicit and bounded.
12. Automation run records govern execution/provenance only. Ordinary domain state and accepted Events remain the single authoritative state/history model.
13. Start, pause, resume, stop, expiry and revocation have deterministic semantics that preserve accepted history and use status lookup for ambiguous in-flight operations.
14. Eleven additive successor touch points are identified without reopening completed Stage A milestones.

## Gate review

- Mode/context/cadence/connectivity terminology unambiguous: **PASS**
- Automation controller is not a human/global GM role: **PASS**
- Explicit delegation and no self-widening rule defined: **PASS**
- Automatic/proposal/human/prohibited operation classes defined: **PASS**
- Mandatory human-choice baseline defined: **PASS**
- Start/pause/exit/resume/stop/revoke lifecycle defined: **PASS**
- Deterministic/domain authority separated from optional AI: **PASS**
- Hidden scenario truth has bounded non-AI authority path: **PASS**
- Ordinary Event/persistence/recovery remains single state model: **PASS**
- Additive implementation touch points identified: **PASS**
- Application implementation authorized: **NO**
- Global AI/AutoGM GM authority authorized: **NO**
- Public matchmaking authorized: **NO**
- Paid AI/provider use authorized: **NO**
- CCTI-12-T04 resumed: **NO**

Repository-health/PR merge evidence remains to be attached before `completed_verified` is claimed.
