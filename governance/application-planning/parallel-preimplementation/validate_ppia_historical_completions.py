from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK_STATE_DIR = ROOT / "governance" / "ai" / "work-state"
COMPLETE_STATUSES = {"complete", "completed", "completed_verified"}

P7_FINAL_HEAD = "c8e9d1ab677ca4bb37a772b1883099d23abb8187"
P7_FINAL_MERGE = "ac1628227d34df7fc1585b21c21988fb2fd7080a"
P8_FINAL_HEAD = "1a2a8590730a905cf4bba84abd59d0a8f00de89c"
P8_FINAL_MERGE = "09f9df2607398010097e834e8ad7b129cd10645f"
P9_FINAL_HEAD = "7393eac19d88eb5b2c58e44b51c1c3a2f3e2b968"
P9_FINAL_MERGE = "3996ca97a2e31fa89ce5c9d4101c96affb83ea71"
P10_FINAL_HEAD = "507c9da21dd74d771f910861323693e2d7193bfa"
P10_FINAL_MERGE = "b4ac8c080af7055e2d150ab6d37de41e9cc2a68f"
P11_FINAL_HEAD = "9bf4627f9e8e4a4c21dcc2614dcb74d54d62d724"
P11_FINAL_MERGE = "f2274707b1337425f0bc9ac8d1dd5ebb08d9f883"
P11_FINAL_RUN = "31595927902"
P6_FINAL_HEAD = "6d2da6fb5a7c2d62492de895c6a9c7a1fe970a06"
P6_FINAL_MERGE = "ffce4859a8912813021776c4f5825c3d219bb0f2"
P6_FINAL_RUN = "31622184027"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def historical_completion_checks() -> None:
    p1 = load_json(WORK_STATE_DIR / "PPIA-01-attempt-001.json")
    p2 = load_json(WORK_STATE_DIR / "PPIA-02-attempt-001.json")
    p3 = load_json(WORK_STATE_DIR / "PPIA-03-attempt-001.json")
    p4 = load_json(WORK_STATE_DIR / "PPIA-04-attempt-001.json")
    p5 = load_json(WORK_STATE_DIR / "PPIA-05-attempt-001.json")
    p12 = load_json(WORK_STATE_DIR / "PPIA-12-attempt-001.json")
    p7 = load_json(WORK_STATE_DIR / "PPIA-07-attempt-001.json")
    p8 = load_json(WORK_STATE_DIR / "PPIA-08-attempt-001.json")
    p9 = load_json(WORK_STATE_DIR / "PPIA-09-attempt-001.json")
    p10 = load_json(WORK_STATE_DIR / "PPIA-10-attempt-001.json")
    p11 = load_json(WORK_STATE_DIR / "PPIA-11-attempt-001.json")
    p6 = load_json(WORK_STATE_DIR / "PPIA-06-attempt-001.json")

    assert p1["status"] in COMPLETE_STATUSES and p1.get("merge_commit") == "f9e2b1fb7c340d27813b09c180b60d34d5fb6f92"
    assert p2["status"] == "completed_verified" and p2.get("merge_commit") == "f768345a44a662a5a1981f4cb35d218c926a5cb6"
    assert p2["latest_pushed_commit"] == "1909a607bbb3ff57a959ae8cc47058ad2882a4e3" and p2["pull_request"] == 219
    assert p3["status"] == "completed_verified" and p3.get("merge_commit") == "ea08234b9d6bcd4cb942c2de964639b330d9511e"
    assert p3["latest_pushed_commit"] == "c1e00ebf67fe4c78af2ce6e1dd483bb699706047" and p3["pull_request"] == 224
    assert p4["status"] == "completed_verified" and p4.get("merge_commit") == "e8ec662534820e53fcb8a7d958c0946f494faefd"
    assert p4["latest_pushed_commit"] == "a821f53794d675e73ae71d6c02d577141981ba22" and p4["pull_request"] == 229
    assert p5["status"] == "completed_verified" and p5.get("merge_commit") == "0ffaa34ef15f9a7e4b77776688c6be3fc3047446"
    assert p5["latest_pushed_commit"] == "e6e2bcfd0f22f537a73721dfd8069531bd1af24c" and p5["pull_request"] == 234
    assert p5["active_substep"] is None and not p5["unresolved_failures"] and p5["owner_decision_required"] is False
    assert p12["status"] == "completed_verified" and p12.get("merge_commit") == "0ed9f9a0c53b2a132d8f38c0d3cae22cc7ae14a0"
    assert p12["latest_pushed_commit"] == "ae3d538e85e09e52681df5a05bd8ee343aa5e908" and p12["pull_request"] == 239
    assert p12["active_substep"] is None and not p12["unresolved_failures"] and p12["owner_decision_required"] is False
    assert any("31536379370" in item.get("command", "") and item.get("status") == "passed" for item in p12["validation"])
    assert any("0ed9f9a0c53b2a132d8f38c0d3cae22cc7ae14a0" in item.get("value", "") for item in p12["evidence"])
    assert p7["status"] == "completed_verified" and p7.get("merge_commit") == P7_FINAL_MERGE
    assert p7["latest_pushed_commit"] == P7_FINAL_HEAD and p7["pull_request"] == 246
    assert p7["active_substep"] is None and not p7["unresolved_failures"] and p7["owner_decision_required"] is False
    assert any("31545759090" in item.get("command", "") and item.get("status") == "passed" for item in p7["validation"])
    assert any(P7_FINAL_MERGE in item.get("value", "") for item in p7["evidence"])
    assert p8["status"] == "completed_verified" and p8.get("merge_commit") == P8_FINAL_MERGE
    assert p8["latest_pushed_commit"] == P8_FINAL_HEAD and p8["pull_request"] == 251
    assert p8["active_substep"] is None and not p8["unresolved_failures"] and p8["owner_decision_required"] is False
    assert any("31553303602" in item.get("command", "") and item.get("status") == "passed" for item in p8["validation"])
    assert any(P8_FINAL_MERGE in item.get("value", "") for item in p8["evidence"])
    assert p9["status"] == "completed_verified" and p9.get("merge_commit") == P9_FINAL_MERGE
    assert p9["latest_pushed_commit"] == P9_FINAL_HEAD and p9["pull_request"] == 256
    assert p9["active_substep"] is None and not p9["unresolved_failures"] and p9["owner_decision_required"] is False
    assert any("31558007822" in item.get("command", "") and item.get("status") == "passed" for item in p9["validation"])
    assert any(P9_FINAL_MERGE in item.get("value", "") for item in p9["evidence"])
    assert p10["status"] == "completed_verified" and p10.get("merge_commit") == P10_FINAL_MERGE
    assert p10["latest_pushed_commit"] == P10_FINAL_HEAD and p10["pull_request"] == 261
    assert p10["active_substep"] is None and not p10["unresolved_failures"] and p10["owner_decision_required"] is False
    assert any("31585946135" in item.get("command", "") and item.get("status") == "passed" for item in p10["validation"])
    assert any(P10_FINAL_MERGE in item.get("value", "") for item in p10["evidence"])
    assert p11["status"] == "completed_verified" and p11.get("merge_commit") == P11_FINAL_MERGE
    assert p11["latest_pushed_commit"] == P11_FINAL_HEAD and p11["pull_request"] == 267
    assert p11["active_substep"] is None and not p11["unresolved_failures"] and p11["owner_decision_required"] is False
    assert any(P11_FINAL_RUN in item.get("command", "") and item.get("status") == "passed" for item in p11["validation"])
    assert any(P11_FINAL_MERGE in item.get("value", "") for item in p11["evidence"])
    assert p6["status"] == "completed_verified" and p6.get("merge_commit") == P6_FINAL_MERGE
    assert p6["latest_pushed_commit"] == P6_FINAL_HEAD and p6["pull_request"] == 273
    assert p6["active_substep"] is None and not p6["unresolved_failures"] and p6["owner_decision_required"] is False
    assert any(P6_FINAL_RUN in item.get("command", "") and item.get("status") == "passed" for item in p6["validation"])
    assert any(P6_FINAL_MERGE in item.get("value", "") for item in p6["evidence"])
