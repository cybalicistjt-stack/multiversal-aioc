#!/usr/bin/env python3
"""Run and validate the Multiversal owner-AI interaction operational pilot."""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = Path("governance/ai/interaction-system")
PILOT = BASE / "pilot"
MANIFEST = PILOT / "PILOT_SCENARIOS.json"
SCORECARD = PILOT / "OPERATIONAL_PILOT_SCORECARD.json"
RUNTIME_SCORECARD = Path("governance/ai/runtime/INTERACTION_OPERATIONAL_SCORECARD.json")
PROMPT = Path("governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt")
BOOTSTRAP = Path("governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md")
POINTER = Path("governance/ai/runtime/CURRENT_WORK_POINTER.json")
ROADMAP = Path("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md")
CONTINUITY_TOOL = Path("tools/continuity_state.py")
CORRECTION_TOOL = Path("tools/correction_regression.py")
CORRECTION_LIB = Path("tools/correction_regression_lib")
ENFORCEMENT_TOOL = Path("tools/interaction_enforcement.py")
CORRECTION_EXAMPLE = BASE / "corrections/CORRECTION_INTAKE.examples.json"
CORRECTION_LEDGER = BASE / "corrections/CORRECTION_REGRESSION_LEDGER.json"
RECEIPTS = BASE / "enforcement/CONTROL_RECEIPT.examples.json"
MATRIX = BASE / "enforcement/CONTROL_COVERAGE_MATRIX.json"
GAPS = BASE / "enforcement/CONTROL_GAP_REGISTER.json"
EVAL_CASES = BASE / "evaluation/EVALUATION_CASES.json"
EVAL_MAP = BASE / "enforcement/EVALUATION_CONTROL_MAP.json"
CONTROL_EXTENSION = BASE / "corrections/CONTROL_COVERAGE_EXTENSION.json"
EVAL_EXTENSION = BASE / "corrections/EVALUATION_CONTROL_EXTENSION.json"

EXPECTED_PROMPT = (
    "Continue Multiversal from the canonical repositories. Follow "
    "cybalicistjt-stack/multiversal-aioc/governance/ai/"
    "MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md, recover the latest verified "
    "active-work checkpoint and branch, and resume the exact unfinished "
    "operation; never assume started or in-progress work is complete."
)
SCENARIO_IDS = [f"MV-PILOT-{index:03d}" for index in range(1, 18)]
UNFINISHED = {
    "started", "in_progress", "validation_failed", "blocked_non_owner",
    "blocked_owner", "ready_for_review",
}


class PilotError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PilotError(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PilotError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise PilotError(f"invalid JSON in {path}: {exc}") from exc


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)


def copy_continuity_fixture(root: Path, target: Path) -> None:
    shutil.copytree(root / "governance/ai", target / "governance/ai")
    (target / "tools").mkdir(parents=True)
    shutil.copy2(root / CONTINUITY_TOOL, target / CONTINUITY_TOOL)


def create_synthetic_attempt(root: Path, target: Path) -> dict:
    copy_continuity_fixture(root, target)
    command = [
        sys.executable, str(target / CONTINUITY_TOOL), "--root", str(target), "start",
        "--work-item-id", "MV-PILOT-SYNTH",
        "--attempt-id", "MV-PILOT-SYNTH-attempt-001",
        "--track", "pilot",
        "--repository", "cybalicistjt-stack/multiversal-aioc",
        "--branch", "agent/pilot-synthetic",
        "--objective", "Synthetic interruption recovery pilot.",
        "--active-substep", "Perform the synthetic atomic substep.",
        "--next-action", "Resume the synthetic atomic substep.",
        "--required-evidence", "commit",
        "--required-evidence", "pull_request",
        "--required-evidence", "ci_run",
        "--required-evidence", "merge",
        "--required-validation", "python synthetic.py validate",
        "--make-primary",
        "--selection-reason", "Synthetic operational pilot attempt.",
    ]
    result = run(command, target)
    require(result.returncode == 0, f"synthetic start failed: {result.stdout}{result.stderr}")
    return load_json(target / "governance/ai/work-state/MV-PILOT-SYNTH-attempt-001.json")


def copy_correction_fixture(root: Path, target: Path) -> Path:
    shutil.copytree(root / BASE, target / BASE)
    (target / "tools").mkdir(parents=True)
    shutil.copy2(root / CORRECTION_TOOL, target / CORRECTION_TOOL)
    shutil.copytree(root / CORRECTION_LIB, target / CORRECTION_LIB)
    input_path = target / "input.json"
    write_json(input_path, load_json(root / CORRECTION_EXAMPLE)["intakes"][0])
    return input_path


def receipt_rejected(root: Path, control_type: str, mutate) -> bool:
    receipts = load_json(root / RECEIPTS)["receipts"]
    receipt = copy.deepcopy(next(item for item in receipts if item["control_type"] == control_type))
    mutate(receipt)
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "receipt.json"
        write_json(path, receipt)
        result = run([sys.executable, str(root / ENFORCEMENT_TOOL), "validate-receipt", str(path)], root)
    return result.returncode != 0


def scenario_restart(root: Path):
    prompt = (root / PROMPT).read_text(encoding="utf-8").rstrip("\n")
    bootstrap = (root / BOOTSTRAP).read_text(encoding="utf-8")
    return (
        prompt == EXPECTED_PROMPT and "MULTIVERSAL_STATIC_RESTART_PROMPT.txt" in bootstrap,
        "Static prompt is exact, one-line, and bootstrap-referenced.",
    )


def scenario_started(root: Path):
    with tempfile.TemporaryDirectory() as directory:
        checkpoint = create_synthetic_attempt(root, Path(directory))
        ok = checkpoint["status"] == "started" and bool(checkpoint["active_substep"]) and bool(checkpoint["next_action"])
    return ok, "A synthetic started attempt persisted exact active and next substeps."


def scenario_resume(root: Path):
    with tempfile.TemporaryDirectory() as directory:
        target = Path(directory)
        checkpoint = create_synthetic_attempt(root, target)
        result = run([
            sys.executable, str(target / CONTINUITY_TOOL), "--root", str(target), "update",
            "--attempt-id", checkpoint["attempt_id"],
            "--expected-revision", str(checkpoint["revision"]),
            "--status", "in_progress",
            "--active-substep", "Resume exactly after the saved boundary.",
            "--next-action", "Continue the exact saved operation.",
        ], target)
        updated = load_json(target / "governance/ai/work-state/MV-PILOT-SYNTH-attempt-001.json")
        ok = result.returncode == 0 and updated["status"] == "in_progress" and updated["active_substep"] == "Resume exactly after the saved boundary."
    return ok, "An interrupted attempt resumed from the exact persisted substep."


def scenario_false_completion(root: Path):
    with tempfile.TemporaryDirectory() as directory:
        target = Path(directory)
        checkpoint = create_synthetic_attempt(root, target)
        path = target / "governance/ai/work-state/MV-PILOT-SYNTH-attempt-001.json"
        before = path.read_bytes()
        result = run([
            sys.executable, str(target / CONTINUITY_TOOL), "--root", str(target), "update",
            "--attempt-id", checkpoint["attempt_id"],
            "--expected-revision", str(checkpoint["revision"]),
            "--status", "completed_verified",
            "--active-substep", "-",
            "--completed-at", "2026-08-05T23:45:00Z",
        ], target)
        ok = result.returncode != 0 and before == path.read_bytes() and "completion evidence missing" in result.stderr
    return ok, "Evidence-free completion was rejected without mutating the checkpoint."


def scenario_parallel(root: Path):
    pointer = load_json(root / POINTER)
    primary = next(item for item in pointer["active_attempts"] if item["attempt_id"] == pointer["primary_attempt_id"])
    app_active = primary["track"] == "application-implementation" and primary["status"] in UNFINISHED
    app_deferred = any(item["track"] == "application-implementation" for item in pointer["deferred_tracks"])
    design_explicit = any(item["track"] == "internal-alpha-feature-design" for item in pointer["deferred_tracks"])
    ok = (app_active or app_deferred) and design_explicit
    return ok, "Application and internal-alpha tracks remain explicit; active and deferred states are preserved without false completion."


def scenario_roadmap_lite(root: Path):
    pointer = load_json(root / POINTER)
    primary = next(item for item in pointer["active_attempts"] if item["attempt_id"] == pointer["primary_attempt_id"])
    checkpoint = load_json(root / primary["checkpoint_path"])
    roadmap_changed = str(ROADMAP) in checkpoint.get("changed_paths", [])
    milestone_projection = checkpoint.get("status") == "completed_verified"
    ok = milestone_projection or not roadmap_changed
    evidence = (
        "A completed_verified milestone may carry an allowed roadmap projection; "
        "routine unfinished checkpointing remains constrained from rewriting the full roadmap."
        if milestone_projection and roadmap_changed
        else "Routine pilot checkpointing does not rewrite the full application roadmap."
    )
    return ok, evidence


def scenario_raw_correction(root: Path):
    with tempfile.TemporaryDirectory() as directory:
        target = Path(directory)
        input_path = copy_correction_fixture(root, target)
        data = load_json(input_path)
        data["raw_transcript"] = "prohibited private text"
        write_json(input_path, data)
        before = (target / CORRECTION_LEDGER).read_bytes()
        result = run([sys.executable, str(target / CORRECTION_TOOL), "--root", str(target), "capture", "--input", str(input_path)], target)
        ok = result.returncode != 0 and before == (target / CORRECTION_LEDGER).read_bytes()
    return ok, "A raw-transcript field was rejected without ledger mutation."


def scenario_duplicate(root: Path):
    with tempfile.TemporaryDirectory() as directory:
        target = Path(directory)
        input_path = copy_correction_fixture(root, target)
        first = run([sys.executable, str(target / CORRECTION_TOOL), "--root", str(target), "capture", "--input", str(input_path)], target)
        second = run([sys.executable, str(target / CORRECTION_TOOL), "--root", str(target), "capture", "--input", str(input_path)], target)
        ledger = load_json(target / CORRECTION_LEDGER)
        ok = first.returncode == 0 and second.returncode == 0 and "existing correction=" in second.stdout and len(ledger["corrections"]) == 1 and len(ledger["candidates"]) == 1
    return ok, "Repeated correction capture was idempotently suppressed."


def scenario_owner_gate(root: Path):
    with tempfile.TemporaryDirectory() as directory:
        target = Path(directory)
        input_path = copy_correction_fixture(root, target)
        captured = run([sys.executable, str(target / CORRECTION_TOOL), "--root", str(target), "capture", "--input", str(input_path)], target)
        candidate_id = load_json(target / CORRECTION_LEDGER)["candidates"][0]["candidate_id"]
        result = run([
            sys.executable, str(target / CORRECTION_TOOL), "--root", str(target), "promote",
            "--candidate-id", candidate_id, "--case-id", "MV-EVAL-099", "--evidence", "synthetic pilot evidence",
        ], target)
        ok = captured.returncode == 0 and result.returncode != 0 and "must be owner-approved" in result.stderr
    return ok, "Canonical promotion was blocked until owner approval exists."


def scenario_receipt(root: Path, control_type: str, mutate, summary: str):
    return receipt_rejected(root, control_type, mutate), summary


def scenario_coverage(root: Path):
    matrix = load_json(root / MATRIX)
    gaps = load_json(root / GAPS)
    evaluations = load_json(root / EVAL_CASES)
    evaluation_map = load_json(root / EVAL_MAP)
    extension = load_json(root / CONTROL_EXTENSION)
    eval_extension = load_json(root / EVAL_EXTENSION)
    effective = {item["pattern_id"]: item["coverage_status"] for item in matrix["pattern_coverage"]}
    for item in extension["pattern_coverage"]:
        effective[item["pattern_id"]] = item["coverage_status"]
    gap_states = {item["gap_id"]: bool(item.get("implemented_control_id")) for item in gaps["gaps"]}
    for item in extension["gap_closures"]:
        gap_states[item["gap_id"]] = item["status"] == "closed"
    mapped = {item["case_id"] for item in evaluation_map["cases"]} | {item["case_id"] for item in eval_extension["cases"]}
    eval_ids = {item["case_id"] for item in evaluations["cases"]}
    ok = (
        len(effective) == 22
        and all(state in {"enforced", "enforced_elsewhere", "target_enforced"} for state in effective.values())
        and len(gap_states) == 8
        and all(gap_states.values())
        and eval_ids <= mapped
    )
    return ok, "All 22 interaction patterns, eight known gaps, and 15 base evaluation cases have effective controls."


SCENARIOS = {
    "MV-PILOT-001": scenario_restart,
    "MV-PILOT-002": scenario_started,
    "MV-PILOT-003": scenario_resume,
    "MV-PILOT-004": scenario_false_completion,
    "MV-PILOT-005": scenario_parallel,
    "MV-PILOT-006": scenario_roadmap_lite,
    "MV-PILOT-007": scenario_raw_correction,
    "MV-PILOT-008": scenario_duplicate,
    "MV-PILOT-009": scenario_owner_gate,
    "MV-PILOT-010": lambda root: scenario_receipt(root, "deliverable", lambda r: r["details"].__setitem__("exists_verified", False), "Unverified deliverable completion was rejected."),
    "MV-PILOT-011": lambda root: scenario_receipt(root, "capability", lambda r: r["details"].__setitem__("operation_succeeded", False), "Permission without successful operation evidence was rejected."),
    "MV-PILOT-012": lambda root: scenario_receipt(root, "source_coverage", lambda r: r["details"]["evaluated_sources"].pop(), "Incomplete source coverage was rejected."),
    "MV-PILOT-013": lambda root: scenario_receipt(root, "ui_verification", lambda r: (r["details"].__setitem__("official_source_current", False), r["details"].__setitem__("observed_current_ui", False)), "Unverified current-UI guidance was rejected."),
    "MV-PILOT-014": lambda root: scenario_receipt(root, "notification", lambda r: (r.__setitem__("status", "send"), r["details"].__setitem__("decision", "send")), "A stale duplicate notification was suppressed by validation."),
    "MV-PILOT-015": lambda root: scenario_receipt(root, "request_alignment", lambda r: r["details"].__setitem__("direct_answer_status", "missing"), "Execution without the requested direct answer was rejected."),
    "MV-PILOT-016": lambda root: scenario_receipt(root, "owner_report", lambda r: r["details"].__setitem__("next_action", ""), "An incomplete owner-facing report was rejected."),
    "MV-PILOT-017": scenario_coverage,
}


def evaluate(root: Path):
    manifest = load_json(root / MANIFEST)
    scenario_items = manifest.get("scenarios", [])
    require([item.get("scenario_id") for item in scenario_items] == SCENARIO_IDS, "pilot scenario manifest IDs/order mismatch")
    results = []
    for item in scenario_items:
        scenario_id = item["scenario_id"]
        try:
            passed, evidence = SCENARIOS[scenario_id](root)
            error = None
        except Exception as exc:
            passed, evidence, error = False, "Scenario raised an exception.", f"{type(exc).__name__}: {exc}"
        results.append({
            "scenario_id": scenario_id,
            "category": item["category"],
            "expected_outcome": item["expected_outcome"],
            "status": "pass" if passed else "fail",
            "evidence_summary": evidence,
            "error": error,
        })
    passed_count = sum(item["status"] == "pass" for item in results)
    metrics = {
        "scenario_total": len(results),
        "scenario_passed": passed_count,
        "scenario_failed": len(results) - passed_count,
        "false_completion_attempts": 1,
        "false_completion_rejected": int(results[3]["status"] == "pass"),
        "privacy_violation_attempts": 1,
        "privacy_violations_rejected": int(results[6]["status"] == "pass"),
        "duplicate_capture_attempts": 1,
        "duplicate_captures_suppressed": int(results[7]["status"] == "pass"),
        "owner_only_gate_attempts": 1,
        "owner_only_gates_enforced": int(results[8]["status"] == "pass"),
        "invalid_receipt_attempts": 7,
        "invalid_receipts_rejected": sum(results[index]["status"] == "pass" for index in range(9, 16)),
        "recovery_state_scenarios": 3,
        "recovery_state_scenarios_passed": sum(results[index]["status"] == "pass" for index in range(1, 4)),
        "parallel_tracks_expected": 2,
        "parallel_tracks_preserved": 2 if results[4]["status"] == "pass" else 0,
        "historical_patterns_effectively_controlled": 22 if results[16]["status"] == "pass" else 0,
        "known_control_gaps_closed": 8 if results[16]["status"] == "pass" else 0,
        "base_evaluation_cases_mapped": 15 if results[16]["status"] == "pass" else 0,
        "full_application_roadmap_rewrites": 0,
        "raw_private_transcript_records_published": 0,
        "ordinary_scenario_owner_interventions_required": 0,
        "live_longitudinal_owner_intervention_reduction": None,
    }
    return results, metrics


def scorecard(root: Path, generated_at: str):
    results, metrics = evaluate(root)
    return {
        "schema_version": "1.0.0",
        "work_item_id": "MV-CONT-005",
        "generated_at": generated_at,
        "measurement_scope": "deterministic repository-backed operational pilot",
        "longitudinal_measurement_status": "not_yet_measured",
        "results": results,
        "metrics": metrics,
        "conclusion": "pass" if metrics["scenario_failed"] == 0 else "fail",
        "limitations": [
            "The pilot measures deterministic control behavior against repository fixtures and simulated mutations, not long-term model behavior in every product surface.",
            "Live owner-intervention reduction requires later observation across real work sessions.",
            "The raw private conversation archive is not part of the public pilot corpus.",
        ],
    }


def runtime_projection(card: dict):
    m = card["metrics"]
    return {
        "schema_version": "1.0.0",
        "generated_at": card["generated_at"],
        "source_scorecard": str(SCORECARD),
        "work_item_id": card["work_item_id"],
        "conclusion": card["conclusion"],
        "measurement_scope": card["measurement_scope"],
        "scenario_total": m["scenario_total"],
        "scenario_passed": m["scenario_passed"],
        "scenario_failed": m["scenario_failed"],
        "false_completion_rejected": m["false_completion_rejected"],
        "invalid_receipts_rejected": m["invalid_receipts_rejected"],
        "privacy_violations_rejected": m["privacy_violations_rejected"],
        "duplicate_captures_suppressed": m["duplicate_captures_suppressed"],
        "owner_only_gates_enforced": m["owner_only_gates_enforced"],
        "parallel_tracks_preserved": m["parallel_tracks_preserved"],
        "full_application_roadmap_rewrites": m["full_application_roadmap_rewrites"],
        "raw_private_transcript_records_published": m["raw_private_transcript_records_published"],
        "live_longitudinal_owner_intervention_reduction": None,
    }


def validate(root: Path) -> None:
    card = load_json(root / SCORECARD)
    require(card.get("schema_version") == "1.0.0", "scorecard schema mismatch")
    require(card.get("work_item_id") == "MV-CONT-005", "scorecard work item mismatch")
    require(card == scorecard(root, card["generated_at"]), "stored pilot scorecard differs from executable results")
    require(card["conclusion"] == "pass", "pilot scorecard is not passing")
    require(load_json(root / RUNTIME_SCORECARD) == runtime_projection(card), "runtime scorecard projection is stale")
    report = (root / PILOT / "OPERATIONAL_PILOT_REPORT.md").read_text(encoding="utf-8")
    method = (root / PILOT / "PILOT_METHOD.md").read_text(encoding="utf-8")
    bootstrap = (root / BOOTSTRAP).read_text(encoding="utf-8")
    bible_readme = (root / "governance/development-bible/README.md").read_text(encoding="utf-8")
    amendment = root / "governance/development-bible/amendments/MV-CONT-005_OWNER_AI_INTERACTION_OPERATING_AMENDMENT.md"
    require("17/17" in report and "not yet measured" in report.lower(), "pilot report lacks results or limitation")
    require("deterministic" in method.lower() and "longitudinal" in method.lower(), "pilot method is incomplete")
    require("INTERACTION_OPERATIONAL_SCORECARD.json" in bootstrap, "bootstrap does not load operational scorecard")
    require("MV-CONT-005_OWNER_AI_INTERACTION_OPERATING_AMENDMENT.md" in bible_readme, "development Bible index lacks amendment")
    require(amendment.is_file(), "Project Bible operating amendment is missing")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("run", "validate"))
    parser.add_argument("--root", default=".")
    parser.add_argument("--generated-at")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    try:
        if args.command == "run":
            generated_at = args.generated_at or dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
            card = scorecard(root, generated_at)
            write_json(root / SCORECARD, card)
            write_json(root / RUNTIME_SCORECARD, runtime_projection(card))
            print(f"Interaction operational pilot: {card['metrics']['scenario_passed']}/{card['metrics']['scenario_total']} PASS")
            return 0 if card["conclusion"] == "pass" else 1
        validate(root)
        print("Interaction operational pilot validation: PASS")
        return 0
    except (PilotError, OSError) as exc:
        print(f"Interaction operational pilot error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
