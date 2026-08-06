from pathlib import Path

ROOT = Path(__file__).parent
required = [
    "IA-D07-002_ADVENTURE_MODULE_MANAGEMENT_SPEC.md",
    "IA-D07-002_ADVENTURE_MODULE_FIXTURE_MATRIX.md",
    "IA-D07-002_ADVENTURE_MODULE_TRACEABILITY.md",
    "IA-D07-002_ADVENTURE_MODULE_READINESS.md",
    "IA-D07-002_COMPLETION_RECORD.md",
]
errors = [f"missing {name}" for name in required if not (ROOT / name).exists()]
spec = (ROOT / required[0]).read_text(encoding="utf-8") if not errors else ""
for phrase in ["Published versions are immutable", "atomic authoritative result groups", "filtered before search", "P9-06-008-attempt-002"]:
    if phrase not in spec:
        errors.append(f"spec missing {phrase}")
if errors:
    print("IA-D07-002 ADVENTURE/MODULE VALIDATION: FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)
print("IA-D07-002 ADVENTURE/MODULE VALIDATION: PASS")