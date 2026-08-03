# AIOC-0-011 Acceptance and Integration Test Matrix

## Identity and sessions
1. Valid owner identity authenticates.
2. Unknown identity is rejected.
3. Expired session is rejected.
4. Revoked session is rejected.
5. Sensitive action requires elevated assurance.
6. Re-authentication refreshes assurance.
7. Session revocation propagates to active operations.
8. AI-agent identity cannot impersonate owner.

## Authorization
9. Explicit allow permits ordinary scoped action.
10. Explicit deny overrides allow.
11. Missing policy decision blocks execution.
12. Repository scope is enforced.
13. Environment scope is enforced.
14. Resource ownership is enforced.
15. Agent self-escalation is blocked.
16. Authorization explanation identifies controlling rules.

## Privileged actions and approvals
17. Privileged action without approval is blocked.
18. Approved exact payload executes.
19. Changed payload invalidates approval.
20. Changed target SHA invalidates approval.
21. Expired approval is blocked.
22. Revoked approval is blocked.
23. Separation-of-duties violation is blocked.
24. Post-execution verification is recorded.

## Secrets
25. Plaintext secret pattern in source is rejected.
26. Secret reference without scope is rejected.
27. Secret reference without purpose is rejected.
28. Temporary access expires.
29. Revoked secret access fails immediately.
30. Secret rotation preserves authorized service operation.
31. Old secret is revoked after rotation.
32. Logs redact secret values.
33. Prompt evidence redacts secret values.
34. Suspected leak creates incident and revokes access.

## Repository governance
35. Wrong-repository ambiguity blocks write.
36. App write explicitly targets Multiversal-app.
37. AIOC write explicitly targets multiversal-aioc.
38. Stale blob SHA blocks replacement.
39. Protected branch rejects unauthorized direct mutation.
40. Sensitive path requires review.
41. Force operation requires owner exception.
42. Commit provenance is captured.

## Release governance
43. Candidate with passing checks advances.
44. Failed required check blocks promotion.
45. Missing artifact hash blocks promotion.
46. Hash mismatch blocks promotion.
47. Missing migration evidence blocks promotion.
48. Missing rollback evidence blocks promotion.
49. Approved exact candidate publishes.
50. Candidate mutation invalidates approval.
51. Monitoring regression triggers rollback workflow.
52. Rollback restores prior verified candidate.
53. Release cannot close with unresolved findings.
54. Emergency release receives retrospective review.

## Audit, incidents, and recovery
55. Governed action emits audit event.
56. Audit event cannot be edited.
57. Audit export is redacted.
58. Incident containment disables compromised session.
59. Break-glass requires incident linkage.
60. Break-glass access automatically expires.
61. Break-glass scope cannot expand silently.
62. Incident closure requires verification evidence.
63. Security posture report reflects open findings.
64. Certification fails when a mandatory test fails.
65. Certification passes when all blocking controls pass.
66. Denied action cannot silently fall back to an ungoverned path.
67. Automation uses least-privilege credentials.
68. Agent credentials are revoked after task completion.
69. Cross-repository action records both source and target context.
70. Recovery preserves immutable incident evidence.
