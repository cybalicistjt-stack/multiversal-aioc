from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location("fg",ROOT/"scripts/ops4_foreground_guard.py")
if spec is None or spec.loader is None:
    raise RuntimeError("unable to load OPS4 foreground guard")
FG=importlib.util.module_from_spec(spec)
spec.loader.exec_module(FG)

def capsule():
    return {
        "work_item_id":"CWKS-10",
        "branch":"work/cwks-10-collaborative-editing",
        "head":"abc123",
        "phase":"task-8-validation",
        "last_material_progress":"Task 7 exact-head green",
        "next_action":"Inspect Task 8 terminal transition once",
        "external_run_id":"37517811500",
    }

def baseline():
    return {
        "mode":"foreground_chat",
        "tool_batches":4,
        "remote_operations":10,
        "ci_observations":1,
        "failed_job_inspections":0,
        "failure_log_fetches":0,
        "sleep_wait_calls":0,
        "recovery_reads":["CURRENT","work-item","resume-capsule","workflow-transition"],
        "same_branch_mutations_while_ci_running":0,
        "interruptions_this_attempt":0,
        "foreground_lease_held":False,
        "bounded_quantum_only":True,
    }

class Ops4ForegroundGuardTests(unittest.TestCase):
    def test_small_foreground_quantum_passes(self):
        self.assertEqual(FG.validate_foreground_trace(baseline()),[])

    def test_tool_and_remote_budgets_are_hard(self):
        t=baseline(); t["tool_batches"]=7; t["remote_operations"]=19
        e=FG.validate_foreground_trace(t)
        self.assertIn(FG.TOOL_BUDGET,e); self.assertIn(FG.REMOTE_BUDGET,e)

    def test_no_sleep_or_ci_polling(self):
        t=baseline(); t["sleep_wait_calls"]=1; t["ci_observations"]=2
        e=FG.validate_foreground_trace(t)
        self.assertIn(FG.SLEEP_WAIT,e); self.assertIn(FG.CI_OBSERVATION_BUDGET,e)

    def test_terminal_failure_inspection_is_bounded(self):
        t=baseline(); t["failed_job_inspections"]=2; t["failure_log_fetches"]=2
        self.assertIn(FG.FAILURE_INSPECTION_BUDGET,FG.validate_foreground_trace(t))

    def test_interruption_recovery_is_small_and_checkpointed(self):
        t=baseline(); t["interrupted"]=True; t["recovery_reads"].append("repository-archaeology")
        e=FG.validate_foreground_trace(t)
        self.assertIn(FG.RECOVERY_BUDGET,e); self.assertIn(FG.RESUME_CAPSULE_REQUIRED,e)
        t["recovery_reads"]=t["recovery_reads"][:4]; t["resume_capsule"]=capsule()
        self.assertEqual(FG.validate_foreground_trace(t),[])

    def test_wait_boundary_releases_lease(self):
        t=baseline(); t["wait_boundary"]=True; t["foreground_lease_held"]=True; t["resume_capsule"]=capsule()
        self.assertIn(FG.LEASE_HELD,FG.validate_foreground_trace(t))

    def test_same_branch_speculation_while_ci_running_is_blocked(self):
        t=baseline(); t["same_branch_mutations_while_ci_running"]=1
        self.assertIn(FG.SAME_BRANCH_SPECULATION,FG.validate_foreground_trace(t))

    def test_two_interruptions_open_circuit(self):
        t=baseline(); t["interruptions_this_attempt"]=2; t["resume_capsule"]=capsule()
        self.assertIn(FG.CIRCUIT_OPEN,FG.validate_foreground_trace(t))
        t["durable_executor_active"]=True
        self.assertNotIn(FG.CIRCUIT_OPEN,FG.validate_foreground_trace(t))

    def test_long_running_invocation_requires_durable_executor_or_bounded_quantum(self):
        t=baseline(); t["bounded_quantum_only"]=False; t["must_survive_disconnect"]=True
        self.assertIn(FG.DURABLE_EXECUTOR_REQUIRED,FG.validate_foreground_trace(t))
        t["durable_executor_active"]=True
        self.assertNotIn(FG.DURABLE_EXECUTOR_REQUIRED,FG.validate_foreground_trace(t))

if __name__=="__main__":
    unittest.main()
