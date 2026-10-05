"""Freeze conditional review90, new join99, running91 and prepared author92."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation97-publication-records"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    p = Path(p)
    assert not p.exists()
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
receipt = json.loads((G / "push-receipt-continuation96.json").read_text())
assert receipt["commit_sha"] == "0f5155aa0e7d687955cb7b54167300c8dace78f8"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation96.json") == receipt["manifest_sha256"]
prep = json.loads((R / "round91-92-original-join-and-paper-preparation-20261005.json").read_text())
for f in prep["frozen"]:
    C = Path(f["directory"])
    for name, b in f["input_bindings"].items():
        assert sha(C / name) == b["sha256"] and (C / name).stat().st_size == b["bytes"]
    for b in f["embedded_context"]:
        assert sha(b["path"]) == b["sha256"]
D.mkdir()
now = datetime.now(timezone.utc).isoformat()
C91 = Path(prep["frozen"][0]["directory"])
C92 = Path(prep["frozen"][1]["directory"])
assert not (C92 / "campaign.sqlite").exists()
proc = subprocess.run(
    ["bash", "scripts/cloud.sh", "xean", "--records", "status", str(C91 / "review.sqlite")],
    cwd="/workspace/xean", capture_output=True, text=True, check=True,
)
state = json.loads(proc.stdout)
assert state["calls"]["admitted"] == 1
status = D / "P16.1-round91-native-status.json"
status.write_text(proc.stdout)
rejection = {
    "recorded_utc": now, "action": "Start frozen native Xean P16.1 author92",
    "attempts_rejected_before_execution": 2, "action_executed": False,
    "database_created": False, "reason": "Automatic approval review failed: Selected model is at capacity. The action was not executed because automatic approval review could not be completed. This is a review failure, not a determination that the action is unsafe.",
    "model_or_approval_route_changed": False, "input_changed": False,
    "next_action": "Retry the same already authorized command and approval path when the transient review service recovers.",
}
save(D / "round92-automatic-approval-capacity-observation.json", rejection)
items = [
    {"atom": "P16.1", "round": 91, "directory": str(C91), "role": "review",
     "tool_session_id": 48579, "observed_status": state["status"],
     "status": str(status), "status_sha256": sha(status),
     "completed_result_granted": False, "original_closed": False},
    {"atom": "P16.1", "round": 92, "directory": str(C92), "role": "codex",
     "observed_status": "prepared-not-started", "automatic_approval_capacity_failure": True,
     "completed_result_granted": False, "original_closed": False},
]
batch = {
    "recorded_utc": now, "items": items,
    "active_items": [i for i in items if i["observed_status"] == "running"],
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
    "original_closed": False,
    "focus": "Review91 audits the first-membership join; full original author92 is frozen but its start awaits recovery of automatic approval review capacity. Actual90 passed only conditionally on QEP.",
}
save(D / "current-small-batch-observation.json", batch)
F = R / "root-checks/P16.1-accepted-fiber-and-contact-to-original-EP-join-20261005-continuation99.md"
actual90 = Path(prep["actual90"])
assert sha(actual90) == prep["actual90_sha256"]
reading90 = R / "root-checks/P13.2-round90-canonical-reading-binding-20261005.json"
read90 = json.loads(reading90.read_text())
assert read90["whole_report_root_read"] and read90["all_nonnegative_premise_bindings_verified"]
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1", "P15.1", "P15.2", "P16.6"]
assert sorted(a["fully_solved_original_atoms"]) == sorted(c["fully_solved_original_atoms"]) == sorted(solved)
assert c["historical_reviewed_scoped_papers"] == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
a["continuation99_original_reference_join"] = {
    "path": str(F), "sha256": sha(F), "whole_current_body_root_read": True,
    "independent_review_round": 91, "new_mathematics_accepted": False, "original_closed": False,
}
a["completed_P13_2_partial_review90"] = read90
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint97: actual QEP-conditional PASS90; new original-reference join99; frozen91/92 inputs, actual91 status and author92 approval-capacity failure. No original closure or accepted paper."
for target in c["targets"]:
    if target["id"] == "P16.1":
        target["continuation99_original_reference_join"] = a["continuation99_original_reference_join"]
        target["current_focus"] = batch["focus"]
    if target["id"] == "P13.2":
        target["completed_partial_review90"] = read90
        target["current_focus"] = "Actual90 accepts genuine all-Reeb realization only under QEP for an actual normal rational quotient; QEP remains unproved pending P16.1 join and EP verification."
for p, value in [(R / "active-work.json", a), (R / "checklist-current.json", c)]:
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    shutil.copyfile(R / name, D / name)
files = []


def add(path, remote=None):
    p = Path(path)
    assert p.is_file() and not p.is_symlink()
    rel = p.relative_to(R)
    assert p.suffix not in {".sqlite", ".jsonl"}
    assert not any(v in {".git", ".codex", ".aws", ".env", "auth.json", "run.json"} for v in rel.parts)
    files.append({"local": str(p), "path": remote or "research-checkpoints/continuation97/" + str(rel),
                  "bytes": p.stat().st_size, "sha256": sha(p)})


for p in sorted(D.iterdir()):
    if p.is_file():
        add(p)
for p in [
    F, actual90, reading90, R / "root-checks/P13.2-round90-binding-reading-clarifications-20261005.md",
    R / "prepare_round91_92_original_join_and_paper_20261005.py",
    R / "round91-92-original-join-and-paper-preparation-20261005.json",
    G / "prepare_checkpoint_continuation97.py", G / "push-receipt-continuation96.json",
]:
    add(p)
for f in prep["frozen"]:
    C = Path(f["directory"])
    for name in list(f["input_bindings"]) + ["freeze.json"]:
        add(C / name)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation97.json"
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"], "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 38, "historical_reviewed_scoped_papers": 43,
    "commit_message": "Preserve conditional all-Reeb review and original-reference join research",
    "scope": "Whole canonical partial PASS90 and reading/binding; unreviewed join99; full frozen91/92 input bindings; running91 and unexecuted92 approval-capacity failure; verified receipt96. No full original closure or new accepted paper, private worker state, authentication, runtime mutation, editor replacement or book edits.",
})
print(json.dumps({"manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
                  "review91_status": state["status"], "author92_started": False}, indent=2))
