"""Freeze complete original92, incomplete93, fresh research95 and full review recovery97."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation100-publication-records"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(path, value):
    path = Path(path)
    assert not path.exists()
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
receipt = json.loads((G / "push-receipt-continuation99.json").read_text())
assert receipt["commit_sha"] == "7b517101fa286f9c3ea692c96e1d6d5d9e3a1826"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation99.json") == receipt["manifest_sha256"]
P92 = R / "root-checks/public-P16.1-round-92-final-reader"
P93 = R / "root-checks/public-P21.3-round-93-final-reader"
assert json.loads((P92 / "status.json").read_text())["status"] == "complete-proof-draft"
assert json.loads((P93 / "status.json").read_text())["status"] == "partial"
for stem in ["P16.1-round92", "P21.3-round93"]:
    p = R / ("root-checks/" + stem + "-root-reading-binding-20261005.json")
    v = json.loads(p.read_text())
    assert not v["original_closed"] and sha(v["canonical_result"]) == v["sha256"]
D.mkdir()
items = []
for atom, role, no, stem, session, db in [
    ("P16.1", "review", 97, "P16.1-original-full-review-length-recovery", 36343, "review.sqlite"),
    ("P13.2", "codex", 94, "P13.2-original-all-Reeb-finite-energy-image-paper", 47338, "campaign.sqlite"),
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
        "hot_feedback_sent": False, "completed_result_granted": False, "original_closed": False,
    })
now = datetime.now(timezone.utc).isoformat()
batch = {
    "recorded_utc": now, "items": items,
    "active_items": [i for i in items if i["observed_status"] == "running"],
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
    "focus": "Three originals: complete P16.1 paper92 receives full original review97; full all-Reeb paper94; P21.3 research95 reconstructs new bounded-Psh induction and targets actual pair equality. Review96 input-too-large is preserved; no original closure yet.",
}
save(D / "current-small-batch-observation.json", batch)
paper92 = {
    "reader": str(P92), "canonical": str(R / "root-checks/P16.1-round92-canonical-native-result-20261005.json"),
    "candidate": True, "paper_pages": 17, "full_original_review": items[0],
    "original_closed": False, "independent_full_original_review_completed": False,
}
partial93 = {
    "reader": str(P93), "canonical": str(R / "root-checks/P21.3-round93-canonical-native-result-20261005.json"),
    "candidate": False, "paper_pages": 10, "new_scoped_paper_accepted": False, "original_closed": False,
    "new_research": items[2],
}
save(D / "complete-paper92-and-incomplete-paper93-boundaries.json", {"P16.1": paper92, "P21.3": partial93})
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1", "P15.1", "P15.2", "P16.6"]
assert sorted(a["fully_solved_original_atoms"]) == sorted(c["fully_solved_original_atoms"]) == sorted(solved)
assert c["historical_reviewed_scoped_papers"] == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
a["full_original_P16_1_candidate92"] = paper92
a["incomplete_original_P21_3_result93"] = partial93
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint100: full original P16.1 paper92 and complete source bindings, unresolved P21.3 paper93 and exact gap; new101 normal quotient EP application and new102 bounded-Psh induction remain unreviewed; fresh95 and original full review97; length-blocked96 preserved."
for target in c["targets"]:
    if target["id"] == "P16.1":
        target["full_original_candidate92"] = paper92
        target["current_focus"] = "Complete17-page original proof draft92 preserved and fully read as argument/canonical notes. Independent whole-original review97 is running after preserving96 input-length failure; no original closure until its complete actual verdict."
    if target["id"] == "P21.3":
        target["incomplete_result93"] = partial93
        target["current_focus"] = "93 remains unresolved: exact pair-class interpolation criterion is a reformulation, not a universal proof or analytic counterexample.95 reconstructs new102 bounded-generated-Psh multiplier positivity and targets the remaining equality."
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
    files.append({"local": str(p), "path": remote or "research-checkpoints/continuation100/" + str(rel),
                  "bytes": p.stat().st_size, "sha256": sha(p)})


for folder in [D, P92, P93]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for p in [
    R / "root-checks/P16.1-round92-canonical-native-result-20261005.json",
    R / "root-checks/P16.1-round92-root-reading-binding-20261005.json",
    R / "root-checks/P21.3-round93-canonical-native-result-20261005.json",
    R / "root-checks/P21.3-round93-root-reading-binding-20261005.json",
    R / "root-checks/P13.2-discharged-EP-supplier-and-calibration-independence-20261005-continuation101.md",
    R / "root-checks/P21.3-bounded-generated-Psh-multiplier-induction-20261005-continuation102.md",
    R / "prepare_round95_original_pair_multiplier_research_20261005.py",
    R / "round95-original-pair-multiplier-research-preparation-20261005.json",
    R / "prepare_round96_P16_original_full_review_20261005.py",
    R / "round96-P16-original-full-review-preparation-20261005.json",
    R / "prepare_round97_P16_full_review_length_recovery_20261005.py",
    R / "round97-P16-full-review-length-recovery-preparation-20261005.json",
    G / "prepare_checkpoint_continuation100.py", G / "push-receipt-continuation99.json",
]:
    add(p)
for no, stem, names in [
    (95, "P21.3-original-pair-multiplier-geometric-research", ["input.json", "task-original.json", "assignment-original.txt", "settings.json", "freeze.json"]),
    (96, "P16.1-original-singular-unibranch-paper-full-review", ["task.json", "task-original.json", "argument.md", "primary-catalogue.json", "settings.json", "freeze.json"]),
    (97, "P16.1-original-full-review-length-recovery", ["task.json", "task-original.json", "argument.md", "primary-catalogue.json", "settings.json", "freeze.json", "previous96-input-length-failure.json"]),
]:
    for name in names:
        add(R / f"campaigns/round-{no}" / stem / name)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation100.json"
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"], "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 38, "historical_reviewed_scoped_papers": 43,
    "commit_message": "Preserve full singular-variety proof and continue original-pair research",
    "scope": "Full P16.1 candidate92 and incomplete P21.3 result93 with exact evidence/reading scopes and input serialization bindings; new101/102 remain unreviewed; original full review97, length failure96 and research95; no original closure, private state/auth, runtime changes, editor replacement or book edits.",
})
print(json.dumps({"manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
                  "statuses": [(i["atom"], i["round"], i["observed_status"]) for i in items]}, indent=2))
