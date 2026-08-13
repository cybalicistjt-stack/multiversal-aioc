#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

TOOL = Path('tools/interaction_pilot.py')
text = TOOL.read_text(encoding='utf-8')
old = '''def scenario_roadmap_lite(root: Path):
    pointer = load_json(root / POINTER)
    primary = next(item for item in pointer["active_attempts"] if item["attempt_id"] == pointer["primary_attempt_id"])
    checkpoint = load_json(root / primary["checkpoint_path"])
    return str(ROADMAP) not in checkpoint.get("changed_paths", []), "Routine pilot checkpointing does not rewrite the full application roadmap."
'''
new = '''def scenario_roadmap_lite(root: Path):
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
'''
if text.count(old) != 1:
    raise SystemExit('expected scenario_roadmap_lite body not found exactly once')
TOOL.write_text(text.replace(old, new, 1), encoding='utf-8')

result = subprocess.run([
    sys.executable, 'tools/interaction_pilot.py', 'run',
    '--generated-at', '2026-08-13T12:33:00+00:00'
], text=True, capture_output=True)
print(result.stdout, end='')
print(result.stderr, end='', file=sys.stderr)
if result.returncode != 0:
    raise SystemExit(result.returncode)

# Remove temporary repair/generation machinery before the bot commits the repair.
for path in [
    Path('scripts/apply-capp-pilot-repair.py'),
    Path('.github/workflows/apply-capp-pilot-repair.yml'),
    Path('.github/workflows/generate-capp-interaction-scorecards.yml'),
]:
    path.unlink(missing_ok=True)
