# Multiversal Self-Hosted Final Validation Policy

**Document ID:** MV-AI-VALIDATION-003  
**Version:** 1.0.0  
**Status:** ACTIVE — OWNER APPROVED  
**Owner and final authority:** John Brandon Turner  
**Effective:** 2026-08-18  
**Controls:** final application/package validation where this policy conflicts with older default GitHub-hosted-compute requirements

## 1. Owner decision

GitHub remains the canonical orchestration, evidence, review, and merge control plane for governed Multiversal work. GitHub-hosted compute is no longer the default final validation requirement.

For ordinary Multiversal application/client/package work, the normal final validation architecture is:

1. exact-final-head execution on repository-scoped self-hosted Windows `multiversal-win-01` when Windows behavior, PowerShell, packaging, launcher, filesystem, or native Windows semantics are relevant;
2. exact-final-head execution on repository-scoped self-hosted Linux `multiversal-linux-02` when Linux, browser/headed Chromium, build, test, typecheck, accessibility, package, or POSIX semantics are relevant;
3. deterministic cross-platform comparison when both lanes are expected to produce the same governed artifact or equivalent normalized output;
4. GitHub-recorded workflow/job/commit/artifact/checksum evidence before merge.

A GitHub-hosted runner is an optional independent audit surface, not a routine completion prerequisite.

## 2. GitHub control-plane requirement

Self-hosted compute does not bypass repository governance.

Final validation evidence must remain bound to GitHub by recording, as applicable:

- repository and pull request;
- exact final head SHA;
- workflow run and job IDs;
- assigned runner identity and required labels;
- validator/test/build outcomes;
- uploaded artifact identity;
- SHA-256 or other governed integrity values;
- deterministic comparator result;
- merge evidence.

Local terminal output that is not bound to the governed exact head is useful construction evidence but is not a substitute for the final GitHub-recorded gate when the work item declares one.

## 3. Standard dual-platform gate

For application/package changes that materially affect cross-platform behavior, the preferred final gate is a dual-lane matrix:

### Windows lane

`runs-on: [self-hosted, windows, x64, multiversal-validation]`

Use for relevant Windows/PowerShell/package/runtime checks, including actual packaged-launcher execution when the deliverable claims Windows operability.

### Linux lane

`runs-on: [self-hosted, linux, x64, multiversal-validation-linux]`

Use for relevant Linux/client/headed-browser/build/test/accessibility checks.

Both lanes must check out the same final candidate SHA unless the workflow explicitly documents why a platform-specific source ref is required.

## 4. Deterministic cross-platform comparison

When Windows and Linux are intended to produce the same distributable or deterministic derived artifact, final completion requires comparison rather than two unrelated green jobs.

The comparison must use one of these evidence classes:

1. exact byte identity, normally demonstrated by equal SHA-256 values; or
2. a governed normalized manifest/semantic comparator when platform-specific container metadata or packaging format intentionally prevents byte identity.

A normalized comparator must identify exactly which platform-dependent fields are excluded and must still compare every governed payload file, stable identity, checksum, manifest entry, and declared boundary relevant to the deliverable.

A comparator harness failure is a validation-infrastructure failure until repaired or separately proven; it must not be silently treated as application success.

## 5. When both self-hosted lanes are required

Use both Windows and Linux at the final gate when any of the following applies:

- the deliverable is distributed to Windows but constructed or tested with Linux tooling;
- platform-dependent packaging/checksum behavior is possible;
- PowerShell/Windows launcher behavior is part of acceptance;
- headed browser or Linux-specific tooling is part of acceptance;
- the work item explicitly declares cross-platform parity;
- deterministic cross-platform comparison is part of the acceptance contract.

For a platform-neutral change whose acceptance contract does not depend on one platform, use only the smallest declared final lane(s). Governance/document-only changes do not need artificial Windows+Linux execution merely to satisfy this policy.

## 6. GitHub-hosted independent audits

GitHub-hosted runners are reserved for occasional independent audits rather than every tranche.

Use a hosted audit when one or more of these conditions applies:

- the owner explicitly requests an independent hosted confirmation;
- a release/security/production gate explicitly requires a third environment;
- self-hosted environment contamination is suspected;
- a toolchain/runner upgrade needs independence verification;
- a periodic sampled audit is due under a later audit schedule;
- an external platform requirement cannot be credibly reproduced on the self-hosted pair.

A hosted audit may be advisory or blocking according to the work item's explicitly declared gate. Merely inheriting older generic language such as “hosted final confirmation” does not make hosted compute blocking after this policy's effective date unless the requirement is reaffirmed for a specific independent-risk reason.

## 7. Historical hosted-compute holds

Older work items or pull requests whose only remaining final-validation blocker is the former project-wide default requirement for GitHub-hosted compute must be re-evaluated under this policy.

Do not automatically mark them complete. Instead:

1. verify their exact current head and mergeability;
2. verify that required self-hosted Windows/Linux evidence still binds to that head;
3. repair and run any missing deterministic cross-platform comparison;
4. rerun changed or stale acceptance gates where the candidate has drifted;
5. retain every separate owner, release, distribution, security, compatibility, runtime, or canonical-content gate.

This policy removes the generic hosted-compute dependency; it does not retroactively create missing evidence or authorize a merge/release.

## 8. Runner availability and persistence

Runner unavailability is validation infrastructure, not application failure.

- `multiversal-win-01` may operate in owner-controlled interactive mode through `C:\actions-runner\run.cmd`.
- `multiversal-linux-02` may operate through the governed WSL/Linux runner configuration.
- A wake/recovery job may establish the Linux listener from the Windows runner when it preserves runner identity, exact-head checkout, and GitHub evidence.
- Temporary wake/repair plumbing must not be confused with the application acceptance gate and should be removed from feature workflows when no longer needed.

## 9. Completion integrity

This policy does not weaken the completion-claim integrity policy.

A final gate is complete only when every declared required lane/comparison/check has passed on the exact final candidate and the evidence has been inspected. Failed required validation remains unfinished.

## 10. Cost and billing posture

Routine final validation should prefer owner-controlled self-hosted compute so development is not blocked by GitHub-hosted minute, allowance, spending-limit, or billing availability.

No policy language may be interpreted as authority to purchase additional Actions capacity, paid runners, cloud compute, or other services without the existing owner spending gate.

## 11. Default pattern

`build complete bounded tranche → exact-head self-hosted Windows/Linux gate as applicable → deterministic cross-platform comparison where applicable → GitHub evidence inspection → merge → occasional hosted independent audit only when specifically justified`
