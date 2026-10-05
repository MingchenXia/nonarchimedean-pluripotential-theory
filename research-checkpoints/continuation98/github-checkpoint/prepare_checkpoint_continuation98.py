"""Freeze quotient supplier100 and the small batch91/92/93."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation98-publication-records"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    p = Path(p)
    assert not p.exists()
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
receipt = json.loads((G / "push-receipt-continuation97.json").read_text())
assert receipt["commit_sha"] == "dde229b76965dedf879bdfea63a3404c42ef2cb2"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation97.json") == receipt["manifest_sha256"]
prep93 = json.loads((R / "round93-continuous-pair-current-research-preparation-20261005.json").read_text())
C93 = Path(prep93["directory"])
assert sha(C93 / "input.json") == prep93["input_sha256"]
assert sha(C93 / "settings.json") == prep93["settings_sha256"]
for b in prep93["embedded_context"]:
    assert sha(b["path"]) == b["sha256"]
F = R / "root-checks/P13.2-geometrically-unibranch-EP-supplier-for-normal-Reeb-quotients-20261005-continuation100.md"
S = R / "root-checks/continuation100-normal-quotient-supplier-primary-read-units"
reading = json.loads((S / "source-read-record.json").read_text())
assert sha(F) == reading["proposal_sha256"] and reading["whole_current_proposal_root_read"]
assert not reading["mathematics_accepted"] and not reading["EP_U_established"]
for unit in reading["units"]:
    assert sha(unit["source"]) == unit["source_sha256"]
    assert sha(unit["literal_file"]) == unit["literal_sha256"]
D.mkdir()
now = datetime.now(timezone.utc).isoformat()
items = []
for atom, no, stem, role, session in [
    ("P16.1", 91, "P16.1-original-reference-first-membership-join-partial-review", "review", 48579),
    ("P16.1", 92, "P16.1-original-singular-unibranch-finite-energy-paper", "codex", 9437),
    ("P21.3", 93, "P21.3-universal-continuous-pair-current-independence", "codex", 50205),
]:
    C = R / f"campaigns/round-{no}" / stem
    database = C / ("review.sqlite" if role == "review" else "campaign.sqlite")
    proc = subprocess.run(
        ["bash", "scripts/cloud.sh", "xean", "--records", "status", str(database)],
        cwd="/workspace/xean", capture_output=True, text=True, check=True,
    )
    state = json.loads(proc.stdout)
    assert state["calls"]["admitted"] == 1
    p = D / f"{atom}-round{no}-native-status.json"
    p.write_text(proc.stdout)
    items.append({
        "atom": atom, "round": no, "directory": str(C), "role": role,
        "tool_session_id": session, "observed_status": state["status"],
        "status": str(p), "status_sha256": sha(p), "hot_feedback_sent": False,
        "completed_result_granted": False, "original_closed": False,
    })
save(D / "round92-automatic-approval-capacity-recovery.json", {
    "recorded_utc": now, "previous_checkpoint97_failure_snapshot_unchanged": True,
    "same_frozen_author_command_later_executed": True,
    "same_author_input_and_requested_model": True, "approval_check_bypassed": False,
    "actual_native_calls_admitted": 1, "session_id": 9437,
    "status_snapshot": next(i["status"] for i in items if i["round"] == 92),
})
batch = {
    "recorded_utc": now, "items": items,
    "active_items": [i for i in items if i["observed_status"] == "running"],
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
    "original_closed": False,
    "focus": "Three frozen native runs on two originals: original-reference join91 and complete P16.1 paper92; universal continuous-pair/current problem P21.3 in93. Root100 prepares the unreviewed normal-quotient QEP supplier after the pending EP join.",
}
save(D / "current-small-batch-observation.json", batch)
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1", "P15.1", "P15.2", "P16.6"]
assert sorted(a["fully_solved_original_atoms"]) == sorted(c["fully_solved_original_atoms"]) == sorted(solved)
assert c["historical_reviewed_scoped_papers"] == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
proposal = {
    "path": str(F), "sha256": sha(F), "whole_current_body_root_read": True,
    "source_read_record": str(S / "source-read-record.json"),
    "mathematics_accepted": False, "QEP_proved": False, "original_closed": False,
}
a["continuation100_normal_quotient_EP_supplier"] = proposal
a["round93_universal_continuous_pair_research"] = {
    "directory": str(C93), "input_sha256": prep93["input_sha256"],
    "model": "gpt-6.1-sol", "reasoning": "xhigh", "original_closed": False,
}
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint98: root100 normal-quotient EP-supplier interface and seven exact primary units, original P21.3 author93 inputs, actual91/92/93 statuses and approval-capacity recovery. No original closure or new accepted paper."
for target in c["targets"]:
    if target["id"] == "P13.2":
        target["continuation100_normal_quotient_EP_supplier"] = proposal
    if target["id"] == "P16.1":
        target["current_focus"] = "Independent first-membership join review91 and complete original paper author92 are admitted with unchanged frozen inputs; full original remains open pending review."
    if target["id"] == "P21.3":
        target["current_focus"] = "Native author93 researches the exact universal continuous-pair ordinary-current identity or an actual analytic counterexample. Only the exact prior real-PL, dual-reduction and pure-curve scopes are granted; no arbitrary-current density or pair-recognition theorem is assumed."
        target["round93_research"] = a["round93_universal_continuous_pair_research"]
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
    files.append({"local": str(p), "path": remote or "research-checkpoints/continuation98/" + str(rel),
                  "bytes": p.stat().st_size, "sha256": sha(p)})


for folder in [S, D]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for p in [
    F, R / "root-checks/continuation100-live-normal-geometrically-unibranch-primary-observation.json",
    R / "prepare_continuation100_normal_quotient_primary_units_20261005.py",
    R / "prepare_round93_continuous_pair_current_research_20261005.py",
    R / "round93-continuous-pair-current-research-preparation-20261005.json",
    G / "prepare_checkpoint_continuation98.py", G / "push-receipt-continuation97.json",
]:
    add(p)
for name in ["input.json", "task-original.json", "assignment-original.txt", "settings.json", "freeze.json"]:
    add(C93 / name)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation98.json"
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"], "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 38, "historical_reviewed_scoped_papers": 43,
    "commit_message": "Preserve normal-quotient EP supplier and universal continuous-pair research",
    "scope": "Unreviewed root100 application with explicit pending EP premise, seven entire pertinent BGM/Stacks units, complete original P21.3 frozen inputs, actual91/92/93 native statuses and approval-service recovery, receipt97. No original closure, new accepted paper, private state/auth, runtime mutation, editor replacement or book edits.",
})
print(json.dumps({"manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
                  "statuses": [(i["atom"], i["round"], i["observed_status"]) for i in items]}, indent=2))
