# VTI-07 Governed-Start Control-Plane RED

- Exact test-only head: `b608b83ddee459a925088888de9f3722a65fdb6f`
- AIOC run: `34063667213`
- Job: `101568575055`
- Repository-health validator: PASS
- Control-plane regression: expected RED
- Observed failures: VTI-07 checkpoint remained `selected_not_started` instead of `in_progress`, and `implementation_scope` was absent.
- Interpretation: the new VTI-07 registration regression correctly detects the missing governed-start projection. No production permission behavior was present or authorized.
