# AIOC-0-011 Capability Catalog

## Identity and trust
1. Register human identities.
2. Register AI-agent identities.
3. Register service accounts.
4. Bind authentication providers.
5. Assign assurance levels.
6. Establish trusted sessions.
7. Expire trusted sessions.
8. Revoke sessions.
9. Detect anomalous session use.
10. Require re-authentication for sensitive actions.

## Authorization
11. Define roles.
12. Define scoped capabilities.
13. Define deny policies.
14. Resolve effective permissions.
15. Evaluate contextual restrictions.
16. Enforce resource ownership rules.
17. Enforce environment restrictions.
18. Enforce repository restrictions.
19. Prevent agent self-escalation.
20. Explain authorization decisions.

## Approvals and privileged actions
21. Classify action sensitivity.
22. Create privileged-action proposals.
23. Require owner approval.
24. Require multi-party approval.
25. Enforce separation of duties.
26. Expire approvals.
27. Revoke approvals.
28. Bind approval to exact payload and SHA.
29. Verify post-execution result.
30. Record denied attempts.

## Secrets
31. Register secret references.
32. Assign secret scope.
33. Assign secret purpose.
34. Grant temporary secret access.
35. Revoke secret access.
36. Rotate secrets.
37. Detect expired secrets.
38. Detect suspected exposure.
39. Redact secret values.
40. Execute leak-containment workflow.

## Repository protection
41. Read branch protection state.
42. Define required checks.
43. Enforce protected branches.
44. Require current blob SHA for updates.
45. Prevent wrong-repository writes.
46. Require review for sensitive paths.
47. Verify commit provenance.
48. Detect force-push risk.
49. Govern repository automation credentials.
50. Quarantine suspicious mutations.

## Release governance
51. Create release candidates.
52. Verify artifact hashes.
53. Verify test evidence.
54. Verify migration readiness.
55. Verify rollback readiness.
56. Approve release promotion.
57. Publish approved releases.
58. Monitor release health.
59. Roll back releases.
60. Close release records.

## Audit, incidents, and recovery
61. Emit immutable audit events.
62. Search redacted audit evidence.
63. Create security incidents.
64. Contain compromised sessions.
65. Disable compromised credentials.
66. Activate break-glass access.
67. Auto-expire break-glass access.
68. Require retrospective review.
69. Generate security posture reports.
70. Certify governance controls.
