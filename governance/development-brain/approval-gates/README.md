# Continuous Validation with Human Approval Gates

Release G Step 21 converts validated Step 20 review packages and explicit human decisions into auditable approval-gate records.

Allowed states are `awaiting-owner-approval`, `approved-validation-ready`, `approved-stale`, `rejected`, and `blocked`.

Approval is valid only for the exact package fingerprint named by the decision. Any upstream change invalidates that approval and requires a new human decision. Missing decisions remain pending; rejection leaves canonical content unchanged; blocked gates identify their reason.

An approved gate permits validation readiness only. It does not authorize execution, canonical mutation, merge, promotion, certification, assignment, or scheduling. Approval cannot be inferred from silence, consensus, CI success, or an AI-generated recommendation.

Every state transition preserves actor, action, target package, fingerprint, reason, and timestamp in the audit trail.
