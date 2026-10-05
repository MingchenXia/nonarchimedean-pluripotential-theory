"""Freeze exact inconclusive97, incomplete95, and fresh original work99/100."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation102-publication-records"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(path, value):
    path = Path(path)
    assert not path.exists()
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
receipt = json.loads((G / "push-receipt-continuation101.json").read_text())
assert receipt["commit_sha"] == "aa55965e5395ddbea232a8a9a2074ac18ccf88d6"
assert all(receipt[k] for k in ["remote_ref_verified", "all_file_blob_bindings_verified_remote", "independent_native_git_tree_verified"])
assert sha(G / "upload-manifest-continuation101.json") == receipt["manifest_sha256"]
P = R / "root-checks/public-P21.3-round-95-final-reader"
canonical97 = R / "root-checks/P16.1-round97-actual-inconclusive-full-review-20261005.json"
result97 = json.loads(canonical97.read_text())
assert result97["verdict"] == "INCONCLUSIVE"
reading95 = R / "root-checks/P21.3-round95-root-reading-binding-20261005.json"
v = json.loads(reading95.read_text())
assert not v["original_closed"] and sha(v["canonical_result"]) == v["sha256"]
assert json.loads((P / "status.json").read_text())["status"] == "partial"
D.mkdir()
items = []
for atom, role, no, stem, session, db in [
    ("P16.1", "review", 99, "P16.1-original-self-contained-full-review", 82345, "review.sqlite"),
    ("P13.2", "review", 98, "P13.2-original-all-Reeb-image-paper-full-review", 14470, "review.sqlite"),
    ("P21.3", "codex", 100, "P21.3-original-mixed-symmetry-and-arbitrary-current-research", 85644, "campaign.sqlite"),
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
    "focus": "Same three original problems. Full P16.1 review99 losslessly inlines all26 original contexts after97 INCONCLUSIVE access audit; original P13.2 full review98; P21.3 research100 reconstructs new103 continuous-factor mixed symmetry and still targets arbitrary-current equality.",
}
save(D / "current-small-batch-observation.json", batch)
boundaries = {
    "full_review97": {"canonical": str(canonical97), "sha256": sha(canonical97), "verdict": "INCONCLUSIVE",
                     "operation_id": result97["operationId"], "reported_at": result97["reportedAt"],
                     "complete_original_accepted": False, "new_review": items[0]},
    "incomplete_research95": {"canonical": v["canonical_result"], "sha256": v["sha256"], "reader": str(P),
                            "candidate": False, "paper_pages": 10, "new_scoped_paper_accepted": False,
                            "new_research": items[2]},
    "new103": {"proof": str(R / "root-checks/P21.3-generated-Psh-mixed-symmetry-and-BT-closure-20261005-continuation103.md"),
              "independently_accepted": False, "universal_BT_asserted": False},
}
save(D / "actual-results-and-new-work-boundaries.json", boundaries)
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1", "P15.1", "P15.2", "P16.6"]
assert sorted(a["fully_solved_original_atoms"]) == sorted(c["fully_solved_original_atoms"]) == sorted(solved)
assert c["historical_reviewed_scoped_papers"] == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
a["actual_full_original_review97"] = boundaries["full_review97"]
a["incomplete_original_P21_3_result95"] = boundaries["incomplete_research95"]
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint102: exact inconclusive97 and incomplete95; self-contained full-original review99 and new mixed-symmetry original research100; new103 unreviewed; no closure or new scoped acceptance."
for t in c["targets"]:
    if t["id"] == "P16.1":
        t["actual_full_original_review97"] = boundaries["full_review97"]
        t["current_focus"] = "Full original review97 INCONCLUSIVE: complete grant/source audit not achieved through inaccessible local references, no concrete defect demonstrated. Fresh99 losslessly supplies all26 contexts and all primary bodies inline. Original remains open."
    if t["id"] == "P21.3":
        t["incomplete_result95"] = boundaries["incomplete_research95"]
        t["current_focus"] = "95 reconstructs actual middle-positive Borel products and full bounded-generated-Psh positivity, candidate=false.100 reconstructs new103 mixed symmetry with one continuous factor and still targets the arbitrary-current equality or an actual admissible analytic counterexample."
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
    files.append({"local": str(p), "path": remote or "research-checkpoints/continuation102/" + str(rel),
                  "bytes": p.stat().st_size, "sha256": sha(p)})


for folder in [D, P]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for p in [
    canonical97, R / "root-checks/P16.1-round97-canonical-reading-binding-20261005.json",
    R / "root-checks/P21.3-round95-canonical-native-result-20261005.json", reading95,
    R / "root-checks/P21.3-generated-Psh-mixed-symmetry-and-BT-closure-20261005-continuation103.md",
    R / "prepare_round99_P16_self_contained_full_review_20261005.py",
    R / "round99-P16-self-contained-full-review-preparation-20261005.json",
    R / "prepare_round100_P21_mixed_symmetry_research_20261005.py",
    R / "round100-P21-mixed-symmetry-research-preparation-20261005.json",
    G / "prepare_checkpoint_continuation102.py", G / "push-receipt-continuation101.json",
]:
    add(p)
for no, stem, names in [
    (99, "P16.1-original-self-contained-full-review", ["task.json", "task-original.json", "argument.md", "original-grant-primary-catalogue-factored.json", "paper92-external-premises-factored.json", "primary-literal-body-dictionary.json", "settings.json", "freeze.json"]),
    (100, "P21.3-original-mixed-symmetry-and-arbitrary-current-research", ["input.json", "task-original.json", "assignment-original.txt", "CLD-weak-multiplier-LF10257-10281.txt", "new103-primary-reading-binding.json", "settings.json", "freeze.json"]),
]:
    for name in names:
        add(R / f"campaigns/round-{no}" / stem / name)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation102.json"
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"], "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 38, "historical_reviewed_scoped_papers": 43,
    "commit_message": "Preserve exact audits and continue full-original equation and current research",
    "scope": "Actual97 INCONCLUSIVE and95 candidate=false preserved unchanged with complete bindings; full original review99 and original research100 continue exact scopes; new103 unreviewed. No closure, new scoped acceptance, private state/auth, runtime mutation, editor replacement or book edits.",
})
print(json.dumps({"manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
                  "statuses": [(i["atom"], i["round"], i["observed_status"]) for i in items]}, indent=2))
