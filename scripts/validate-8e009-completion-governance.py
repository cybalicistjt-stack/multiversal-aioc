from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = {
    "current": ROOT / "governance/current-state/AIOC_CURRENT_STATE.md",
    "handoff": ROOT / "governance/current-state/SESSION_HANDOFF.md",
    "program": ROOT / "governance/object-system/CANONICAL_OBJECT_TEMPLATE_PROGRAM.md",
    "bootstrap": ROOT / "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md",
}
texts = {name: path.read_text(encoding="utf-8") for name, path in files.items()}
required_all = [
    "19,199",
    "20",
    "8D-007",
    "Golden Test Corpus",
    "112ef5116b4090cc266eefe36e1c539b6567f022d6b857db6e1d2bdd77e30e40",
]
for label, text in texts.items():
    for token in required_all:
        assert token in text, (label, token)
assert "0 unprocessed rows" in texts["current"]
assert "0 partially processed datasets" in texts["handoff"]
assert "Status:** COMPLETE" in texts["program"]
assert "Version:** 3.5.0" in texts["bootstrap"]
print("8E-009 completion governance validation: PASS")
