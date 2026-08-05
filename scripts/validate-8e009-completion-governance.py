from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
files = {
    "current": ROOT / "governance/current-state/AIOC_CURRENT_STATE.md",
    "handoff": ROOT / "governance/current-state/SESSION_HANDOFF.md",
    "program": ROOT / "governance/object-system/CANONICAL_OBJECT_TEMPLATE_PROGRAM.md",
    "bootstrap": ROOT / "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md",
}
texts = {name: path.read_text(encoding="utf-8") for name, path in files.items()}
required_completion = [
    "19,199",
    "20",
    "8D-007",
    "Golden Test Corpus",
    "112ef5116b4090cc266eefe36e1c539b6567f022d6b857db6e1d2bdd77e30e40",
]
for label in ("current", "handoff", "program"):
    for token in required_completion:
        assert token in texts[label], (label, token)
assert "0 unprocessed rows" in texts["current"]
assert "0 partially processed datasets" in texts["handoff"]
assert "Status:** COMPLETE" in texts["program"]
match = re.search(r"\*\*Version:\*\*\s+(\d+)\.(\d+)\.(\d+)", texts["bootstrap"])
assert match and tuple(map(int, match.groups())) >= (5, 0, 0), "bootstrap version must support continuity runtime"
for token in (
    "governance/ai/runtime/CURRENT_WORK_POINTER.json",
    "governance/ai/runtime/ROADMAP_INDEX.json",
    "completed_verified",
    "tools/continuity_state.py validate",
):
    assert token in texts["bootstrap"], ("bootstrap", token)
print("8E-009 completion governance validation: PASS")
