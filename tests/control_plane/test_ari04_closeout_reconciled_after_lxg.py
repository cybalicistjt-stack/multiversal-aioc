import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
REGISTRY = ROOT / "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json"
INDEX = ROOT / "governance/ai/runtime/ROADMAP_INDEX.json"
BACKLOG = ROOT / "governance/application-planning/asset-resource-ingestion-reuse/ARI_PROGRAM_BACKLOG.json"
ARI04 = ROOT / "governance/ai/work-state/ARI-04-attempt-001.json"
ARI05 = ROOT / "governance/ai/work-state/ARI-05-attempt-001.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_ari04_closeout_is_atomic_and_lxg_remains_parallel():
    pointer = load(POINTER)
    registry = load(REGISTRY)
    index = load(INDEX)
    backlog = load(BACKLOG)
    ari04 = load(ARI04)
    ari05 = load(ARI05)

    assert ari04["status"] == "completed_verified"
    assert ari04["authority_retired"] is True
    assert ari04["application_pr"] == 445
    assert ari04["application_merge_sha"] == "19b85b153afd84c533f2fc10627fd756864047db"
    assert ari04["deterministic_receipt_sha256"] == "3bb6da24052c8526a61db6f95d5f346510f3681d9396caecd127f3c57a729411"

    assert ari05["status"] == "selected_not_started"
    assert ari05["implementation_authority"] is False
    assert ari05["implementation_branch"] is None

    assert pointer["active_attempt"]["work_item_id"] == "ARI-05"
    assert pointer["active_attempt"]["status"] == "selected_not_started"
    assert pointer["bounded_authority"]["ari_implementation"] is False

    assert registry["active_planning_work"]["work_item"] == "ARI-05"
    assert registry["parallel_developer_infrastructure"]["work_item"] == "LXG-01"
    assert registry["parallel_developer_infrastructure"]["product_implementation_authority"] is False

    assert index["current"]["work_item_id"] == "ARI-05"
    assert index["selected_ari"]["completed_through"] == "ARI-04"
    assert index["selected_ari"]["current"] == "ARI-05"
    assert "LXG" not in index["effective_forward_order"]

    assert backlog["completed_through"] == "ARI-04"
    assert backlog["current_item"] == "ARI-05"
    assert backlog["implementation_authority"] is False
