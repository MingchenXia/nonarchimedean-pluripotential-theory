"""Freeze accepted join91, its reading and full original P13.2 author94."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation99-publication-records"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    p = Path(p)
    assert not p.exists()
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
receipt = json.loads((G / "push-receipt-continuation98.json").read_text())
assert receipt["commit_sha"] == "05367f1057adde1eab4a6f27884d2da3d1c18645"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation98.json") == receipt["manifest_sha256"]
prep94 = json.loads((R / "round94-original-fixed-Reeb-image-paper-preparation-20261005.json").read_text())
C94 = Path(prep94["directory"])
assert prep94["exact_E_discharged_by91"] and not prep94["new_normal_quotient_application_granted"]
assert sha(C94 / "input.json") == prep94["input_sha256"]
assert sha(C94 / "settings.json") == prep94["settings_sha256"]
for b in prep94["embedded_context"]:
    assert sha(b["path"]) == b["sha256"]
reading_path = R / "root-checks/P16.1-round91-canonical-reading-binding-20261005.json"
reading = json.loads(reading_path.read_text())
assert reading["whole_report_root_read"] and reading["all_nonnegative_premise_bindings_verified"]
assert sha(reading["canonical_result"]) == reading["sha256"]
assert sha(reading["binding"]) == reading["binding_sha256"]
D.mkdir()
now = datetime.now(timezone.utc).isoformat()
items = []
for atom, no, stem, session in [
    ("P16.1", 92, "P16.1-original-singular-unibranch-finite-energy-paper", 9437),
    ("P21.3", 93, "P21.3-universal-continuous-pair-current-independence", 50205),
    ("P13.2", 94, "P13.2-original-all-Reeb-finite-energy-image-paper", 47338),
]:
    C = R / f"campaigns/round-{no}" / stem
    proc = subprocess.run(
        ["bash", "scripts/cloud.sh", "xean", "--records", "status", str(C / "campaign.sqlite")],
        cwd="/workspace/xean", capture_output=True, text=True, check=True,
    )
    state = json.loads(proc.stdout)
    assert state["calls"]["admitted"] == 1
    p = D / f"{atom}-round{no}-native-status.json"
    p.write_text(proc.stdout)
    items.append({
        "atom": atom, "round": no, "directory": str(C), "role": "codex",
        "tool_session_id": session, "observed_status": state["status"],
        "status": str(p), "status_sha256": sha(p), "hot_feedback_sent": False,
        "completed_result_granted": False, "original_closed": False,
    })
batch = {
    "recorded_utc": now, "items": items,
    "active_items": [i for i in items if i["observed_status"] == "running"],
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
    "original_closed": False,
    "focus": "Three frozen native authors on a few originals: complete P16.1 paper92 and connected P13.2 realization paper94, plus original universal P21.3 research93. The independent join91 passed only its precise first-membership/countable-E scope.",
}
save(D / "current-small-batch-observation.json", batch)
ep = {
    "statement": "EP on every original reduced irreducible geometrically unibranch projective variety and actual ample rational polarization over arbitrary algebraically closed trivially valued characteristic-zero k.",
    "accepted_countable_join": reading,
    "precise_countable_to_arbitrary_implication": str(R / "root-checks/P16.1-local-reference-converse-and-countable-to-arbitrary-EP-20261005-continuation90.md"),
    "implication_review": str(R / "root-checks/P16.1-round86-actual-partial-mathematical-review-20261005.json"),
    "normal_quotient_application_accepted": False, "original_closed": False,
    "full_original_paper_accepted": False, "pending_author92_output_used": False,
}
save(D / "accepted-EP-supplier-and-new-application-boundary.json", ep)
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1", "P15.1", "P15.2", "P16.6"]
assert sorted(a["fully_solved_original_atoms"]) == sorted(c["fully_solved_original_atoms"]) == sorted(solved)
assert c["historical_reviewed_scoped_papers"] == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
a["accepted_original_reference_join91"] = reading
a["accepted_EP_supplier_after_exact_join91"] = ep
a["original_P13_2_paper_author94"] = {
    "directory": str(C94), "input_sha256": prep94["input_sha256"],
    "task_sha256": prep94["task_sha256"], "original_closed": False,
}
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint99: actual partial join PASS91 with full canonical reading/binding, discharged E and precise EP supplier; fresh complete original P13.2 author94 inputs and statuses92/93/94. Full papers and new normal-quotient application remain unaccepted."
for target in c["targets"]:
    if target["id"] == "P16.1":
        target["accepted_original_reference_join91"] = reading
        target["current_focus"] = "Actual91 passes first membership, onto PSH, normalized compactness and every target in countable E. Together with accepted86 this supplies arbitrary-cardinality EP. Complete original operator/equation paper92 and its original-scope review remain pending."
    if target["id"] == "P13.2":
        target["accepted_EP_supplier_after_exact_join91"] = ep
        target["original_paper_author94"] = a["original_P13_2_paper_author94"]
        target["current_focus"] = "Complete original author94 reconstructs the normal rational quotient application of the now available EP supplier and the genuine all-Reeb image theorem. Actual90 remains conditional; the new application and full original paper require review."
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
    files.append({"local": str(p), "path": remote or "research-checkpoints/continuation99/" + str(rel),
                  "bytes": p.stat().st_size, "sha256": sha(p)})


for p in sorted(D.iterdir()):
    if p.is_file():
        add(p)
for p in [
    Path(reading["canonical_result"]), reading_path, Path(reading["binding"]),
    R / "prepare_round94_original_fixed_Reeb_image_paper_20261005.py",
    R / "round94-original-fixed-Reeb-image-paper-preparation-20261005.json",
    G / "prepare_checkpoint_continuation99.py", G / "push-receipt-continuation98.json",
]:
    add(p)
for name in ["input.json", "task-original.json", "assignment-original.txt", "settings.json", "freeze.json"]:
    add(C94 / name)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation99.json"
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"], "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 38, "historical_reviewed_scoped_papers": 43,
    "commit_message": "Preserve accepted first-membership join and full all-Reeb paper research",
    "scope": "Actual canonical partial PASS91 and whole report/premise reading, exact bindings, discharged E and precise EP supplier from accepted86; full original author94 frozen inputs; actual92/93/94 statuses and receipt98. Full original papers, normal quotient application and original closures remain pending. No private state/auth, runtime changes, editor replacement or book edits.",
})
print(json.dumps({"manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
                  "statuses": [(i["atom"], i["round"], i["observed_status"]) for i in items]}, indent=2))
