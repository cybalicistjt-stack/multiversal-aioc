# IA-D09 — Permission, Accessibility, and Recovery Matrix

**Status:** release-design blocking matrix

## Permission and authority

| Requirement | Player | GM | Owner | AI/automation | Release-blocking failure |
|---|---|---|---|---|---|
| Read permitted campaign state | yes | yes | yes | permission-filtered | unauthorized data exposure |
| Read hidden/GM-only state | no | yes | yes | only when explicitly permitted and filtered | hidden state reaches unauthorized client/context |
| Propose governed action | yes where allowed | yes | yes | proposal only | proposal bypasses owning-domain validation |
| Approve/modify governed action | no unless rule explicitly grants authority | yes where campaign authority permits | yes | no | AI or unauthorized actor commits decision |
| Promote content to canonical/global scope | no implicit right | governed | owner-gated where required | no | Campaign-local content silently promoted |
| Release/deploy/public access | no | no | owner only | no | release state changed without owner gate |

Permission checks are server/authority-side requirements. Sensitive state must not be delivered to an unauthorized client and merely hidden in presentation.

## Accessibility

| Surface family | Keyboard | Screen reader | Touch alternative | Non-color semantics | Text scale | Reduced motion | Blocking condition |
|---|---|---|---|---|---|---|---|
| preparation/forms | required | labels, errors, progress | required | required | 200% | required | primary task becomes unavailable |
| proposal/approval | required | actor/action/target/result/context announced | 44x44 targets | required | 200% | required | approve/modify/deny cannot be completed |
| combat/runtime | required | turn/result/status announcements | required | targeting/status alternatives | 200% without loss of critical controls | required | time-critical core action inaccessible |
| clue/relationship graphs | full semantic navigation | relationship summaries | non-drag alternative | labeled connections | 200% | required | meaning exists only spatially or by color |
| maps | keyboard controls where map task required | permitted location/selection summary | non-precision alternative | pattern/label alternatives | critical controls preserved | required | core bounded map workflow pointer-only |
| authoring | keyboard-first editing/review | landmarks and validation linkage | drag alternatives | validation labels/icons | 200% review/edit where required | required | validation or save/recovery inaccessible |

Accessibility is not optional capability isolation. Disabling visual effects, AI, advanced maps, or other optional systems must not remove the semantic accessible path.

## Recovery and interruption

| Scenario | Required authoritative behavior | Forbidden behavior |
|---|---|---|
| client drops before submit acknowledgement | status lookup determines whether proposal exists | blind duplicate resubmit |
| player drops while GM reviews | proposal remains authoritative; player can recover status | client guesses approval state |
| GM drops after committing decision | decision recovered from Event/history sequence | reroll/re-decide without idempotency evidence |
| stale object version | conflict response identifies authoritative version and recoverable draft | silent overwrite |
| role or permission changed while disconnected | reauthorize before replay/mutation | replay under stale authority |
| Event gap detected | fetch/replay authoritative missing range | fabricate local Events |
| optional provider fails | typed optional failure; manual path remains | core workflow blocks indefinitely |
| unsupported extension encountered | preserve opaque versioned payload and report unsupported semantics | discard or reinterpret silently |
| broad offline canonical mutation | reject or retain only explicitly replay-safe intent | offline peer becomes canonical authority |

## Cross-cutting release gates

A future candidate is blocked if any of the following are true:

- unauthorized hidden information is exposed;
- approval authority can be bypassed;
- reconnect can duplicate canonical actions or outcomes;
- authoritative result/history cannot reconstruct the accepted outcome;
- critical workflows are pointer-, color-, motion-, or spatial-only;
- optional AI/provider availability is required for core completion;
- unsupported extension data is silently lost or reinterpreted;
- stale offline authority can mutate canonical state;
- release/deployment state can change without the owner gate.