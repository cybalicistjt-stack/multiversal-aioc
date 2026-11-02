# SA-BILL-01 — Scenario Index

**Current inventory:** 60 adversarial obligations: 20 billing, 24 allowance, 8 offline, 8 privacy. **Verification status: 60 NOT EXECUTED.** This inventory is not a production security test report.

**Open first:** Critical cases SA-T001..004, SA-T021..027, SA-T045..046, SA-T053..054; then high-priority privacy, state-transition and installed device cases. See [full threat model](THREAT_MODEL_AND_BILLING_RULES.md), [source code findings](CURRENT_CODE_REVIEW.md), [machine reference](BILLING_REFERENCE_MODEL.json) and [multi-stage execution playbook](ADVERSARIAL_EXECUTION_PLAYBOOK.md).

## Billing (20)

| ID | Priority | Scenario | Expected decision | Proof required |
|---|---|---|---|---|
| SA-T001 | critical | Unverified client screenshot claims paid subscription | `DENY` | provider-source verification |
| SA-T002 | critical | Replay same verified checkout twice | `IDEMPOTENT` | unique provider transaction + ledger |
| SA-T003 | critical | Reassign purchase token across accounts | `DENY` | canonical A3 purchase owner |
| SA-T004 | high | Out-of-order refund then renewal | `RECONCILE` | provider GET + revision |
| SA-T005 | high | Cancellation before paid-term expiry | `ALLOW` | provider term + owner grace decision |
| SA-T006 | high | Cancellation after paid-term expiry | `DENY` | authoritative clock |
| SA-T007 | high | Payment retry/grace at provider | `ALLOW` | verified provider grace |
| SA-T008 | high | Payment account hold | `DENY` | provider hold |
| SA-T009 | high | Refund revokes active term | `DENY` | provider revocation + epoch |
| SA-T010 | high | Upgrade linked purchase token | `IDEMPOTENT` | purchase token lineage |
| SA-T011 | high | Pending payment never completes | `DENY` | purchase lifecycle |
| SA-T012 | high | Repeated cancellation call | `IDEMPOTENT` | subscription cancellation |
| SA-T013 | high | Signed webhook tampered | `DENY` | signed provider envelope |
| SA-T014 | high | Unknown plan-price manipulation | `DENY` | price catalog |
| SA-T015 | medium | Storefront redirect not enrolled | `DENY` | storefront policy |
| SA-T016 | medium | Hidden recurring plan consent | `DENY` | consent and terms audit |
| SA-T017 | medium | Provider unavailable during verification | `RECONCILE` | provider availability |
| SA-T018 | medium | Grace status has unknown length | `DENY` | bounded grace |
| SA-T019 | high | Two-device same canonical subscriber | `ALLOW` | A3 subject identity |
| SA-T020 | medium | AI cost charged by surprise | `NO_BILL` | AI budget port |

## Allowance (24)

| ID | Priority | Scenario | Expected decision | Proof required |
|---|---|---|---|---|
| SA-T021 | critical | Two concurrent one-slot claims | `DENY` | unique tuple + CAS |
| SA-T022 | critical | Player fabricates GM allowance | `DENY` | GM role/source |
| SA-T023 | critical | Unsubscribed GM issues allowance | `DENY` | GM subscription |
| SA-T024 | critical | Cross-campaign grant replay | `DENY` | campaign scope |
| SA-T025 | critical | Cross-player grant replay | `DENY` | subject scope |
| SA-T026 | critical | Setting dependency smuggling | `DENY` | trusted dependency closure |
| SA-T027 | critical | Recursive restricted dependency export | `DENY` | provenance closure |
| SA-T028 | high | Grant issuer removed as GM | `SUSPEND` | current role and epoch |
| SA-T029 | high | GM subscription stops at paid term | `SUSPEND` | issuer effective subscription |
| SA-T030 | high | Player removed from Campaign | `DENY` | current membership |
| SA-T031 | high | Target source release revoked | `SUSPEND` | source lifecycle |
| SA-T032 | high | Target switched without epoch rotation | `DENY` | versioned allowance |
| SA-T033 | high | Same idempotency key repeated | `IDEMPOTENT` | idempotency status lookup |
| SA-T034 | high | Different grant IDs same slot | `DENY` | unique slot |
| SA-T035 | high | Multiple players distinct slots | `ALLOW` | compound unique index |
| SA-T036 | high | Same Player distinct Campaigns | `ALLOW` | campaign-subject composite |
| SA-T037 | high | GM grants non-allowlisted content | `DENY` | registered target allowlist |
| SA-T038 | high | GM grants circular setting dependencies | `DENY` | graph cycle bounds |
| SA-T039 | high | Subscribed player tries to launder GM-dependent item | `DENY` | source provenance |
| SA-T040 | medium | Character retained after entitlement lapse | `RETAIN` | authored-data ownership |
| SA-T041 | medium | GM retires Campaign | `SUSPEND` | campaign lifecycle |
| SA-T042 | medium | Player attempts Character move | `DENY` | character provenance |
| SA-T043 | medium | Receipt claims grant after recipient leaves | `DENY` | fresh A3 campaign binding |
| SA-T044 | medium | Bundled multiple unrelated roots | `DENY` | allowance unit semantics |

## Offline (8)

| ID | Priority | Scenario | Expected decision | Proof required |
|---|---|---|---|---|
| SA-T045 | critical | Copy encrypted offline blob to new phone | `DENY` | hardware-bound key |
| SA-T046 | critical | Rollback phone clock | `DENY` | trusted elapsed time |
| SA-T047 | high | Remote revoke while phone disconnected | `RESTRICT` | offline impossibility and TTL |
| SA-T048 | high | Offline attempts permanent premium grant | `DENY` | no offline entitlement mutation |
| SA-T049 | high | Reconnect stale entitlement epoch | `DENY` | versioned invalidation |
| SA-T050 | high | Offline cached private GM fields leak via search index | `DENY` | cache indexing |
| SA-T051 | medium | Partial download of protected pack | `DENY` | encrypted asset integrity |
| SA-T052 | medium | Same subject multiple installations | `ALLOW` | A3 session/device binding |

## Privacy (8)

| ID | Priority | Scenario | Expected decision | Proof required |
|---|---|---|---|---|
| SA-T053 | critical | Insecure direct asset URL | `DENY` | object-store isolation |
| SA-T054 | critical | Unknown ID search leaks restricted content | `DENY` | query authorization |
| SA-T055 | high | Websocket event delivered after revoke | `DENY` | realtime filtering |
| SA-T056 | high | User-facing export omits taint | `DENY` | export projection |
| SA-T057 | high | Optional AI prompt exfiltrates grant-dependent objects | `DENY` | AI redaction |
| SA-T058 | medium | Diagnostics archive leaks rights and receipt secrets | `DENY` | diagnostic redaction |
| SA-T059 | high | Stale imported save grants ability | `DENY` | import validation |
| SA-T060 | high | Content permission change but cached count remains | `DENY` | visibility epoch |

## Scenario oracle terminology

- **DENY**: No grant, protected action, leak, new charge, or equivalent privilege
- **ALLOW**: Permitted only when all other current permission/rights checks pass
- **SUSPEND**: Freeze premium use without deleting source or historical record
- **RESTRICT**: Only bounded preissued offline read possible; no mutation/instant erase guarantee
- **RETAIN**: Preserve permitted authored raw data while quarantining protected dependencies
- **RECONCILE**: Query authoritative provider/event before taking a financial or privileged action
- **IDEMPOTENT**: Repeated event yields one durable effect
- **NO_BILL**: No unconfirmed provider execution or billing

**Acceptance:** Each case needs independent evidence at the required boundary; an `expectedDecision` here is a specification, not test success. Monetary spend, subscription activation and price approval are outside this study.
