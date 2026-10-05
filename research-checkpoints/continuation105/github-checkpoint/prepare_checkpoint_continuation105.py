"""Freeze incomplete100 and its new scoped103 audit without original closure."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation105-publication-records"
P = R / "root-checks/public-P21.3-round-100-final-reader"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
receipt = json.loads((G / "push-receipt-continuation104.json").read_text())
assert receipt["commit_sha"] == "8594d09250cc9fa3430ffd83136f002eb08a4509"
assert sha(G / "upload-manifest-continuation104.json") == receipt["manifest_sha256"]
assert all(receipt[k] for k in ["remote_ref_verified", "all_file_blob_bindings_verified_remote",
                               "independent_native_git_tree_verified"])
reading = R / "root-checks/P21.3-round100-root-reading-binding-20261005.json"
binding = json.loads(reading.read_text())
assert not binding["original_closed"] and not binding["new_scoped_paper_accepted"]
assert sha(binding["canonical_result"]) == binding["sha256"]
assert json.loads((P / "status.json").read_text())["status"] == "partial"
D.mkdir()
items = []
for atom, role, no, stem, session, db in [
    ("P16.5", "codex", 102, "P16.5-original-nonample-finite-energy-equation-research", 18947, "campaign.sqlite"),
    ("P21.3", "review", 103, "P21.3-bounded-generated-mixed-symmetry-scoped-review", 22880, "review.sqlite"),
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
                  "status": str(p), "status_sha256": sha(p), "original_closed": False,
                  "hot_feedback_sent": False})
now = datetime.now(timezone.utc).isoformat()
batch = {"recorded_utc": now, "items": items,
         "active_items": [i for i in items if i["observed_status"] == "running"],
         "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
         "focus": "Two-target batch: original nonample equation research102 and partial P21.3 bounded-generated calculus review103. Full P21.3 remains open; no arbitrary-current exhaustion or admissible counterexample."}
save(D / "current-small-batch-observation.json", batch)
solved = ["P13.1", "P13.2", "P15.1", "P15.2", "P16.1", "P16.6"]
for name in ["active-work.json", "checklist-current.json"]:
    p = R / name
    d = json.loads(p.read_text()); assert d["fully_solved_original_atoms"] == solved
    d["updated_utc"] = now; d["current_small_batch"] = batch
    d["github_checkpoint" if name == "active-work.json" else "latest_verified_github_checkpoint"] = receipt
    d["github_pending_checkpoint"] = "Checkpoint105: exact incomplete100 eleven-page paper and source bindings, scoped103 review frozen and running; originals remain six solved,36 open."
    d["incomplete_original_P21_3_result100"] = {
        "canonical": binding["canonical_result"], "sha256": binding["sha256"],
        "candidate": False, "reader": str(P), "original_closed": False,
        "new_scoped_paper_accepted": False, "scoped_review": items[1],
    }
    if name == "checklist-current.json":
        assert d["historical_reviewed_scoped_papers"] == 43
        for t in d["targets"]:
            if t["id"] == "P21.3":
                t["current_focus"] = "Incomplete100 reconstructs all bounded generated stages, one-continuous-factor symmetry and stronger compatibility closure under possibly discontinuous locally bounded generated differentiation. Arbitrary-current exhaustion and admissible counterexample remain open. Separate103 audits this scoped result only."
                t["current_scoped_review"] = items[1]
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    shutil.copyfile(p, D / name)
shutil.copyfile(R / "checklist-current.tsv", D / "checklist-current.tsv")
files = []


def add(path, remote=None):
    p = Path(path); assert p.is_file() and not p.is_symlink()
    rel = p.relative_to(R)
    assert p.suffix not in {".sqlite", ".jsonl"}
    assert not any(x in {".git", ".codex", ".aws", ".env", "auth.json", "run.json"} for x in rel.parts)
    files.append({"local": str(p), "path": remote or "research-checkpoints/continuation105/" + str(rel),
                  "bytes": p.stat().st_size, "sha256": sha(p)})


for folder in [D, P]:
    for p in sorted(folder.rglob("*")):
        if p.is_file(): add(p)
for p in [
    R / "root-checks/P21.3-round100-canonical-native-result-20261005.json", reading,
    R / "prepare_round103_P21_scoped_calculus_review_20261005.py",
    R / "complete_round103_P21_review_preparation_20261005.py",
    R / "round103-P21-scoped-calculus-review-preparation-20261005.json",
    G / "prepare_checkpoint_continuation105.py", G / "push-receipt-continuation104.json",
]:
    add(p)
C = R / "campaigns/round-103/P21.3-bounded-generated-mixed-symmetry-scoped-review"
for name in ["task.json", "task-original.json", "argument.md", "settings.json", "freeze.json"]:
    add(C / name)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation105.json"
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"], "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 36,
    "historical_reviewed_scoped_papers": 43,
    "commit_message": "Preserve bounded generated-current progress and audit its exact scope",
    "scope": "Unverified incomplete100 canonical result and11-page paper preserved with27 literal primary units and original bindings; fresh source-contained scoped review103. No full P21.3 closure or new scoped acceptance. P16.5 research102 continues, exact six original solutions retained,36 open. No private state/auth, runtime/book mutation or editor replacement.",
})
print(json.dumps({"manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
                  "statuses": [(i["atom"], i["round"], i["observed_status"]) for i in items]}, indent=2))
