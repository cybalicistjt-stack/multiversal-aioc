#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAMP = "2026-08-15T22:51:20Z"
A10_HEAD = "05d69ece9666fdd4b121461c95a3fdbdd20299dc"
A10_MERGE = "9124860691ea208bded3800008a2d92b4b2c2139"
APP_MAIN = "e0c88756326d00e75d16ee27c198b80b7010f88a"
APP_A9_MERGE = "c2030febf860a4fc9bcac9c65fa44a6b22418dd4"
A10_RUN = 31913130812

POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
INDEX = ROOT / "governance/ai/runtime/ROADMAP_INDEX.json"
CHECKPOINT = ROOT / "governance/ai/work-state/STAGE-A-A10-current-revalidation-attempt-001.json"
BOOTSTRAP = ROOT / "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md"
ROADMAP = ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def project_checkpoint():
    cp = load(CHECKPOINT)
    cp.update({
        "revision": 3,
        "status": "completed_verified",
        "updated_at": STAMP,
        "completed_at": STAMP,
        "latest_pushed_commit": A10_HEAD,
        "expected_remote_head": A10_HEAD,
        "pull_request": 327,
        "merge_commit": A10_MERGE,
        "last_verified_action": (
            "AIOC PR #327 final repaired head 05d69ece9666fdd4b121461c95a3fdbdd20299dc passed focused A10 revalidation, "
            "Conversation Continuity, Workflow Scope, PPIA transition and Operational AIOC Baseline, then squash-merged as GitHub-verified "
            "9124860691ea208bded3800008a2d92b4b2c2139. A10 implementation remains not activated."
        ),
        "active_substep": None,
        "next_action": (
            "Activate STAGE-A-A10 — World Content Authoring as a separate bounded Multiversal-app work order from current post-A9 main "
            f"{APP_MAIN}, preserving the merged A10 revalidation authority. Do not activate A11/A12 or authorize release/deployment/canonical promotion."
        ),
        "validation": [
            {
                "command": "python tools/validate_stage_a_a10_revalidation.py",
                "status": "passed",
                "evidence": f"PR #327 final repaired head run {A10_RUN} passed."
            }
        ],
        "unresolved_failures": [],
        "owner_decision_required": False,
        "evidence": [
            {"kind": "commit", "value": f"STAGE-A-A10 current-revalidation final validated head {A10_HEAD}"},
            {"kind": "pull_request", "value": "STAGE-A-A10 current-revalidation PR #327"},
            {"kind": "ci_run", "value": f"STAGE-A-A10 current-revalidation focused run {A10_RUN} plus exact-head continuity/workflow/PPIA/operational gates PASS"},
            {"kind": "merge", "value": f"STAGE-A-A10 current-revalidation PR #327 verified squash merge {A10_MERGE}"}
        ],
        "roadmap_projection_pending": False,
        "notes": [
            "A10 revalidation is completed_verified; this checkpoint does not itself activate application implementation.",
            "Recovered A10 preparation remains provenance; current-repository revalidation governs activation.",
            "Application A9 is completed_verified through PR #145 / verified merge c2030febf860a4fc9bcac9c65fa44a6b22418dd4 and closure receipt.",
            "A10 implementation must preserve the owner-approved all-bounded-slices-before-broad-checks execution preference unless the owner changes it."
        ]
    })
    completed = cp.setdefault("completed_substeps", [])
    for item in [
        "Final repaired A10 revalidation head passed focused and governance CI.",
        f"PR #327 squash-merged as GitHub-verified {A10_MERGE}.",
        "AIOC recovery projection advanced to A10 implementation authorized/not activated without weakening continuity validators."
    ]:
        if item not in completed:
            completed.append(item)
    dump(CHECKPOINT, cp)


def project_index():
    index = load(INDEX)
    ids = {item["work_item_id"] for item in index["entries"]}
    if "STAGE-A-A10" not in ids:
        index["entries"].append({
            "work_item_id": "STAGE-A-A10",
            "track": "application-implementation",
            "governing_document": "governance/application-planning/stage-a-a10/current-revalidation/STAGE_A_A10_CURRENT_REPOSITORY_REVALIDATION.md",
            "roadmap_document": "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md",
            "roadmap_section": "Phase 10 / Stage A — STAGE-A-A10 World Content Authoring",
            "dependencies": ["STAGE-A-A9"],
            "completion_gate": "All governed A10 World/Setting/Adventure/creator-authoring contracts, source-slice/fixture/acceptance coverage, privacy/accessibility/recovery gates, exact-head predecessor/DT validation, headed-browser evidence, verified merge, and completion-only closure receipt; release/deployment/canonical promotion remain separately gated."
        })
    index["updated_at"] = STAMP
    dump(INDEX, index)


def project_pointer():
    pointer = load(POINTER)
    a10_entry = {
        "work_item_id": "STAGE-A-A10",
        "attempt_id": "STAGE-A-A10-current-revalidation-attempt-001",
        "track": "application-implementation-pre-revalidation",
        "priority": 1,
        "owner_selected": True,
        "repository": "cybalicistjt-stack/multiversal-aioc",
        "branch": "governance/stage-a-a10-current-revalidation",
        "checkpoint_path": "governance/ai/work-state/STAGE-A-A10-current-revalidation-attempt-001.json",
        "status": "completed_verified",
        "updated_at": STAMP,
        "roadmap_projection_pending": False
    }
    retained = [x for x in pointer["active_attempts"] if x["attempt_id"] not in {
        "STAGE-A-A8-R0-attempt-001", "STAGE-A-A10-current-revalidation-attempt-001"
    }]
    for x in retained:
        x["owner_selected"] = False
    pointer["active_attempts"] = [a10_entry, *retained]
    pointer["primary_attempt_id"] = a10_entry["attempt_id"]
    pointer["selection_reason"] = (
        f"STAGE-A-A9 is COMPLETED_VERIFIED in Multiversal-app through PR #145 / verified squash {APP_A9_MERGE} with closure receipt. "
        f"STAGE-A-A10 current-repository revalidation is COMPLETED_VERIFIED through AIOC PR #327 / verified squash {A10_MERGE}. "
        "The exact next application operation is bounded STAGE-A-A10 World Content Authoring activation from current post-A9 application main. "
        "A10 implementation is authorized but not activated by this projection; A11/A12, release, deployment, paid services, real-user content intake, marketplace behavior and canonical promotion remain unauthorized."
    )
    pointer["updated_at"] = STAMP
    app = next(x for x in pointer["deferred_tracks"] if x["track"] == "application-implementation")
    app.update({
        "next_work_item_id": "STAGE-A-A10",
        "state": "authorized_not_activated",
        "reason": (
            "A9 is completed_verified and A10 current-repository revalidation passed/merged. A10 World Content Authoring is the current next application work item for bounded activation; no A10 application implementation branch exists yet."
        ),
        "evidence": (
            f"Multiversal-app PR #145 / verified merge {APP_A9_MERGE}; Multiversal-app/receipts/STAGE-A-A9-CLOSURE.json; "
            f"AIOC PR #327 / verified merge {A10_MERGE}; A10 current-revalidation record; current app main {APP_MAIN}."
        )
    })
    dump(POINTER, pointer)


def project_bootstrap():
    text = BOOTSTRAP.read_text(encoding="utf-8")
    text = text.replace("**Version:** 5.6.2", "**Version:** 5.6.3")
    old = (
        "STAGE-A-A8 is now `COMPLETED_VERIFIED` through application PR #144 / verified squash `e9aaa858b345e6a29e27369c01468551752a2483` with closure receipt `Multiversal-app/receipts/STAGE-A-A8-CLOSURE.json`. "
        "The current next application operation is STAGE-A-A9 current-repository revalidation; A9 is not activated. For A9, inspect recovered `governance/stage-a-a9-preimplementation`, current post-A8 application truth, and PPIA-09/PPIA-10/PPIA-14/PPIA-15 authority before any activation."
    )
    new = (
        f"STAGE-A-A9 is now `COMPLETED_VERIFIED` through application PR #145 / verified squash `{APP_A9_MERGE}` with closure receipt `Multiversal-app/receipts/STAGE-A-A9-CLOSURE.json`. "
        f"STAGE-A-A10 current-repository revalidation is `COMPLETED_VERIFIED` through AIOC PR #327 / verified squash `{A10_MERGE}`. "
        "The current next application operation is bounded STAGE-A-A10 — World Content Authoring activation; A10 implementation is authorized but not yet activated. "
        "For A10, read `governance/application-planning/stage-a-a10/current-revalidation/STAGE_A_A10_CURRENT_REPOSITORY_REVALIDATION.md` before implementation and preserve its D06/D07/D18/D28/D29/D05/D13 ownership, privacy, sandbox, migration-0008 and A9-runtime separation boundaries."
    )
    if old not in text:
        raise SystemExit("bootstrap A8/A9 recovery paragraph not found")
    text = text.replace(old, new)
    BOOTSTRAP.write_text(text, encoding="utf-8")


def project_roadmap():
    text = ROADMAP.read_text(encoding="utf-8")
    text = text.replace("**Version:** 2.14.0", "**Version:** 2.15.0")
    text = text.replace(
        "**Status:** ACTIVE — BOUNDED IMPLEMENTATION AUTHORIZED; STAGE-A-A8 COMPLETED_VERIFIED; A9 REVALIDATION NEXT; PPIA/CAPP COMPLETED_VERIFIED",
        "**Status:** ACTIVE — BOUNDED IMPLEMENTATION AUTHORIZED; STAGE-A-A9 COMPLETED_VERIFIED; A10 REVALIDATION COMPLETED / ACTIVATION NEXT; PPIA/CAPP COMPLETED_VERIFIED"
    )
    old = (
        "- **STAGE-A-A9 — Investigation and Social Workspaces is the current next application target for current-repository revalidation and is not activated.** Recovered `governance/stage-a-a9-preimplementation` remains provenance/input only until its historical 70-path preparation, D24/D25 ownership assumptions, storage/migrations, privacy boundaries, graph implementation assumptions and A9/A10 faction split are refreshed against current post-A8 repository truth and PPIA-09/PPIA-10/PPIA-14/PPIA-15 authority."
    )
    new = (
        f"- **STAGE-A-A9 — Investigation and Social Workspaces is `COMPLETED_VERIFIED`.** All 48 source slices were constructed before checks; 144 source fixtures and 168 published blocking acceptance IDs were preserved; the final A1–A9 + DT-008 + P9 wrapper matrix passed; headed Chromium passed 8/8; application PR #145 squash-merged as GitHub-verified `{APP_A9_MERGE}`; closure is recorded in `Multiversal-app/receipts/STAGE-A-A9-CLOSURE.json`. Release/deployment remained false.\n"
        f"- **STAGE-A-A10 — World Content Authoring has completed current-repository revalidation and is the current next application target for bounded activation.** AIOC PR #327 squash-merged as GitHub-verified `{A10_MERGE}` with verdict `PASS — READY FOR BOUNDED A10 ACTIVATION`. The revalidation preserves the 32 WSM/AM/CC/AI source slices, 120 deterministic fixtures, 140 published blocking criteria, split D06/D07/D18/D28/D29/D05/D13 ownership, owner-only canonical promotion, privacy-before-derived-output, declarative creator sandboxing and additive migration `0008_a10_world_content_authoring.json`. A10 implementation is not activated by the governance merge itself."
    )
    if old not in text:
        raise SystemExit("roadmap current A9 paragraph not found")
    text = text.replace(old, new)
    text = text.replace(
        "- **STAGE-A-A9:** current next application target for revalidation, not activated;",
        "- **STAGE-A-A10:** current next application target; current-repository revalidation completed_verified, implementation authorized/not activated;"
    )
    ROADMAP.write_text(text, encoding="utf-8")


def main():
    project_checkpoint()
    project_index()
    project_pointer()
    project_bootstrap()
    project_roadmap()
    subprocess.run(["python", "tools/continuity_state.py", "refresh-status"], cwd=ROOT, check=True)
    subprocess.run(["python", "tools/continuity_state.py", "validate"], cwd=ROOT, check=True)
    subprocess.run(["python", "governance/application-planning/parallel-preimplementation/validate_ppia_program_state.py"], cwd=ROOT, check=True)
    print("STAGE-A-A10 recovery projection: PASS")


if __name__ == "__main__":
    main()
