"""Freeze full all-Reeb cone candidate94 and original reviews97/98."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation101-publication-records"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(path, value):
    path = Path(path)
    assert not path.exists()
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
receipt = json.loads((G / "push-receipt-continuation100.json").read_text())
assert receipt["commit_sha"] == "f1a9da3da5d615e32b1d3e2d809420f0851027c0"
assert all(receipt[k] for k in ["remote_ref_verified", "all_file_blob_bindings_verified_remote", "independent_native_git_tree_verified"])
assert sha(G / "upload-manifest-continuation100.json") == receipt["manifest_sha256"]
P = R / "root-checks/public-P13.2-round-94-final-reader"
reading = R / "root-checks/P13.2-round94-root-reading-binding-20261005.json"
v = json.loads(reading.read_text())
assert not v["original_closed"] and sha(v["canonical_result"]) == v["sha256"]
assert json.loads((P / "status.json").read_text())["status"] == "complete_unverified_draft"
D.mkdir()
items = []
for atom, role, no, stem, session, db in [
    ("P16.1", "review", 97, "P16.1-original-full-review-length-recovery", 36343, "review.sqlite"),
    ("P13.2", "review", 98, "P13.2-original-all-Reeb-image-paper-full-review", 14470, "review.sqlite"),
    ("P21.3", "codex", 95, "P21.3-original-pair-multiplier-geometric-research", 66307, "campaign.sqlite"),
]:
    C = R / f"campaigns/round-{no}" / stem
    proc = subprocess.run(
        ["bash", "scripts/cloud.sh", "xean", "--records", "status", str(C / db)],
        cwd="/workspace/xean", capture_output=True, text=True, check=True,
    )
    state = json.loads(proc.stdout)
    assert state["calls"]["admitted"] == 1
    p = D / f"{atom}-round{no}-native-status.json"
    p.write_text(proc.stdout)
    items.append({
        "atom": atom, "role": role, "round": no, "directory": str(C), "tool_session_id": session,
        "observed_status": state["status"], "status": str(p), "status_sha256": sha(p),
        "hot_feedback_sent": False, "original_closed": False,
    })
now = datetime.now(timezone.utc).isoformat()
batch = {
    "recorded_utc": now, "items": items,
    "active_items": [i for i in items if i["observed_status"] == "running"],
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
    "focus": "Three original problems: complete17-page singular-variety candidate92 under full review97, complete13-page all-Reeb cone candidate94 under full review98, original P21.3 geometric research95. Neither candidate is accepted before its complete actual verdict.",
}
save(D / "current-small-batch-observation.json", batch)
paper94 = {
    "reader": str(P), "canonical": v["canonical_result"], "canonical_sha256": v["sha256"],
    "reading_binding": str(reading), "candidate": True, "paper_pages": 13,
    "full_original_review": items[1], "original_closed": False,
    "independent_full_original_review_completed": False,
    "exact_original_task_sha256": "4420d5c79db2fc178119e3f4331df3c2745d4f5be9fb27395659762c55407648",
    "precise_EP_background": "Actual91 discharges countable antecedent E; actual86 supplies its exact arbitrary-cardinality implication. The new application to the original normal rational quotient is independently audited in98.",
}
save(D / "full-original-P13.2-candidate94-review-boundary.json", paper94)
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1", "P15.1", "P15.2", "P16.6"]
assert sorted(a["fully_solved_original_atoms"]) == sorted(c["fully_solved_original_atoms"]) == sorted(solved)
assert c["historical_reviewed_scoped_papers"] == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
a["full_original_P13_2_candidate94"] = paper94
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint101: complete13-page original all-Reeb candidate94, full primary/premise/input bindings, exact full original review98; no original closure or new scoped acceptance."
for t in c["targets"]:
    if t["id"] == "P13.2":
        t["full_original_candidate94"] = paper94
        t["current_focus"] = "Full original all-Reeb13-page candidate94 preserved; whole argument/canonical notes/19 external statements read and29 literal bindings reproduced. Original full review98 admitted. No closure before its complete actual mathematical verdict."
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
    files.append({"local": str(p), "path": remote or "research-checkpoints/continuation101/" + str(rel),
                  "bytes": p.stat().st_size, "sha256": sha(p)})


for folder in [D, P]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for p in [
    R / "root-checks/P13.2-round94-canonical-native-result-20261005.json",
    reading, R / "prepare_round98_P13_original_full_review_20261005.py",
    R / "round98-P13-original-full-review-preparation-20261005.json",
    G / "prepare_checkpoint_continuation101.py", G / "push-receipt-continuation100.json",
]:
    add(p)
C98 = R / "campaigns/round-98/P13.2-original-all-Reeb-image-paper-full-review"
for name in ["task.json", "task-original.json", "argument.md", "primary-catalogue.json", "read-only-references.json", "settings.json", "freeze.json"]:
    add(C98 / name)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation101.json"
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"], "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 38, "historical_reviewed_scoped_papers": 43,
    "commit_message": "Preserve complete all-Reeb cone candidate and full original review",
    "scope": "Full P13.2 candidate94 and original review98 with exact original task, mathematical scopes and primary bindings; P16.1 full review97 and P21.3 research95 continue. No closure, new scoped acceptance, private state/auth, runtime mutation, editor replacement or book edits.",
})
print(json.dumps({"manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
                  "statuses": [(i["atom"], i["round"], i["observed_status"]) for i in items]}, indent=2))
