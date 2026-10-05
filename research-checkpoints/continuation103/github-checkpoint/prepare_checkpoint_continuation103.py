"""Freeze publication of the full original P13.2 solution and current work."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation103-publication-records"
P = R / "deliverables/original-P13.2"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
receipt = json.loads((G / "push-receipt-continuation102.json").read_text())
assert receipt["commit_sha"] == "05315e86580f79f29b957d83cdef4126a5faaf58"
assert sha(G / "upload-manifest-continuation102.json") == receipt["manifest_sha256"]
assert all(receipt[k] for k in ["remote_ref_verified", "all_file_blob_bindings_verified_remote",
                               "independent_native_git_tree_verified"])
closure = json.loads((P / "original-closure.json").read_text())
assert closure["fully_solved_original_atom"] and closure["verdict"] == "PASS"
assert closure["source_sha256"] == sha(P / "P13.2-paper.tex")
assert closure["pdf_sha256"] == sha(P / "P13.2-paper.pdf")
assert closure["review_sha256"] == sha(P / "P13.2-original-scope-review.json")
D.mkdir()
items = []
for atom, role, no, stem, session, db in [
    ("P16.1", "review", 99, "P16.1-original-self-contained-full-review", 82345, "review.sqlite"),
    ("P21.3", "codex", 100, "P21.3-original-mixed-symmetry-and-arbitrary-current-research", 85644, "campaign.sqlite"),
]:
    C = R / f"campaigns/round-{no}" / stem
    proc = subprocess.run(["bash", "scripts/cloud.sh", "xean", "--records", "status", str(C / db)],
                          cwd="/workspace/xean", capture_output=True, text=True, check=True)
    state = json.loads(proc.stdout)
    assert state["calls"]["admitted"] == 1
    p = D / f"{atom}-round{no}-native-status.json"
    p.write_text(proc.stdout)
    items.append({"atom": atom, "role": role, "round": no, "directory": str(C),
                  "tool_session_id": session, "observed_status": state["status"],
                  "status": str(p), "status_sha256": sha(p),
                  "hot_feedback_sent": False, "original_closed": False})
now = datetime.now(timezone.utc).isoformat()
batch = {"recorded_utc": now, "items": items,
         "active_items": [i for i in items if i["observed_status"] == "running"],
         "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
         "focus": "P13.2 full original solution published after98 PASS. P16.1 original full review99 and P21.3 original arbitrary-current research100 continue; neither receives hot feedback."}
save(D / "current-small-batch-observation.json", batch)
save(D / "five-original-closures.json", [
    json.loads((R / f"deliverables/original-{a}/original-closure.json").read_text())
    for a in ["P13.1", "P13.2", "P15.1", "P15.2", "P16.6"]
])
solved = ["P13.1", "P13.2", "P15.1", "P15.2", "P16.6"]
for name in ["active-work.json", "checklist-current.json"]:
    path = R / name
    d = json.loads(path.read_text())
    assert d["fully_solved_original_atoms"] == solved
    d["updated_utc"] = now
    d["current_small_batch"] = batch
    d["github_pending_checkpoint"] = "Checkpoint103: full original P13.2 published13 pages, exact full review98 PASS; five original solutions,37 open; ongoing99/100."
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    shutil.copyfile(path, D / name)
shutil.copyfile(R / "checklist-current.tsv", D / "checklist-current.tsv")
files = []


def add(path, remote=None):
    p = Path(path)
    assert p.is_file() and not p.is_symlink()
    rel = p.relative_to(R)
    assert p.suffix not in {".sqlite", ".jsonl"}
    assert not any(x in {".git", ".codex", ".aws", ".env", "auth.json", "run.json"} for x in rel.parts)
    files.append({"local": str(p), "path": remote or "research-checkpoints/continuation103/" + str(rel),
                  "bytes": p.stat().st_size, "sha256": sha(p)})


for folder in [D, P]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for p in [
    R / "root-checks/P13.2-round98-actual-full-original-review-20261005.json",
    R / "root-checks/P13.2-round98-canonical-reading-binding-20261005.json",
    R / "publish_original_P13_2_review98_20261005.py",
    R / "complete_original_P13_2_publication_20261005.py",
    G / "prepare_checkpoint_continuation103.py", G / "push-receipt-continuation102.json",
]:
    add(p)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation103.json"
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"], "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 37,
    "historical_reviewed_scoped_papers": 43,
    "commit_message": "Publish complete fixed-Reeb finite-energy image theorem and original-scope review",
    "scope": "Full original P13.2,13-page reviewed edition, actual98 PASS, complete original packet and source premises with documentary grants distinguished, exact publication-only corrections and local export diagnostics. Five originals solved;37 open. Native editor unchanged, native compiler pending, no new scoped acceptance or claims for pending99/100.",
})
print(json.dumps({"manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
                  "statuses": [(i["atom"], i["round"], i["observed_status"]) for i in items]}, indent=2))
