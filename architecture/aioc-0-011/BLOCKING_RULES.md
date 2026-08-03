# Blocking Validation Rules

1. Block unknown actor identities.
2. Block expired, revoked, or insufficient-assurance sessions.
3. Block actions without an explicit authorization decision.
4. Block permission evaluation that omits deny policies.
5. Block AI-agent self-granted permissions.
6. Block privileged actions without required approval.
7. Block approval reuse after payload, target, branch, path, or SHA changes.
8. Block approval by an actor prohibited by separation-of-duties policy.
9. Block plaintext secrets in repositories, logs, prompts, exports, or audit records.
10. Block secret access without purpose, scope, and expiry.
11. Block expired or revoked secret references.
12. Block release promotion with failed required checks.
13. Block release promotion without artifact hashes.
14. Block release promotion without rollback evidence.
15. Block destructive migrations without tested recovery.
16. Block writes to an ambiguous repository.
17. Block stale-SHA file replacement.
18. Block unauthorized protected-branch mutation.
19. Block force operations without owner-authorized exception.
20. Block unverified executable artifacts.
21. Block audit-event deletion or mutation.
22. Block unredacted audit export.
23. Block break-glass activation without incident linkage.
24. Block break-glass access without automatic expiry.
25. Block incident closure without containment and verification evidence.
26. Block release closure while monitoring findings remain unresolved.
27. Block agent credentials broader than the dispatched task requires.
28. Block silent fallback from denied action to a less-governed execution path.
29. Block security-control certification when mandatory tests fail.
30. Block claims of security or release completion without verifiable evidence.
