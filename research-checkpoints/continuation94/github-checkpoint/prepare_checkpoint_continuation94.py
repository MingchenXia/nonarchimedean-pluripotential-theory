"""Freeze completed author84, actual FAIL85, and fresh repaired review89."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation94-publication-records"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    Path(p).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
receipt = json.loads((G / "push-receipt-continuation93.json").read_text())
assert receipt["commit_sha"] == "cd5139764c00092b581da0b258cb51f516ea1377"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation93.json") == receipt["manifest_sha256"]
D.mkdir()
now = datetime.now(timezone.utc).isoformat()
reader = R / "root-checks/public-P16.1-round-84-final-reader"
canonical84 = R / "root-checks/P16.1-round84-canonical-native-result-20261005.json"
actual85 = R / "root-checks/P16.1-round85-actual-partial-mathematical-review-20261005.json"
assert sha(canonical84) == "939f274e0ee284c1bd5c4fd99a7dfbe60d3392daeba3068eb04e929de82d9158"
assert sha(actual85) == "a3540b6d2d3fc7845ca896b559abbdc477633afbe9fbab2e4682723d241a5c9c"
assert json.loads(canonical84.read_text())["candidate"] is False
assert json.loads(actual85.read_text())["verdict"] == "FAIL"
save(D / "round84-completed-public-argument-reading-addendum.json", {
    "recorded_utc": now, "reader": str(reader), "canonical": str(canonical84),
    "whole_actual_four_notes_root_read": True, "whole_current_argument_root_read": True,
    "inclusive_LF_ranges_whole_read": [[1,95],[96,180],[181,265]],
    "argument_sha256": sha(reader / "argument.md"),
    "whole_tex_root_read": False, "all_70_primary_units_root_read": False,
    "all_recursive_primary_proofs_root_read": False, "new_mathematics_accepted": False,
    "original_closed": False, "local_two_pass_compilation_reported_by_author": True,
    "native_compilation_attempted_on_reader": False,
    "scope": "Completed 16-page conditional draft preserves unproved original-class C1. The new model-domination and fiber arguments are not independently accepted. Preserved documentary diagnostics are not certificates.",
})
save(D / "round89-preparation-assertion-failure-and-recovery.json", {
    "recorded_utc": now,
    "first_helper": str(R / "prepare_round89_rossi_repair_and_round84_reader_20261005.py"),
    "first_helper_sha256": sha(R / "prepare_round89_rossi_repair_and_round84_reader_20261005.py"),
    "actual_failure": "AssertionError at line57: premise entries were dictionaries, while the helper compared the whole dictionary against the passage statement.",
    "completed_actions_before_failure": "Public author84 copy and all70 literal-unit hashes reproduced; no review89 input existed.",
    "recovery_helper": str(R / "complete_round89_rossi_repair_and_round84_reader_20261005.py"),
    "recovery_helper_sha256": sha(R / "complete_round89_rossi_repair_and_round84_reader_20261005.py"),
    "actual_recovery": "New helper verified the entire existing public copy, compared each passage to its indexed premise statement, and completed review89 preparation without modifying the original failed helper.",
    "both_helpers_whole_saved_source_root_read_before_execution": True,
    "all_27_premise_bindings_nonnegative_and_covered": True,
    "mathematical_verdict_from_this_observation": False,
    "round84_terminal_resume_failure": "Transport disconnected on PTY20275 after documented status completed. Completed canonical result was preserved; no private worker state was consulted.",
})
items = []
for no, stem, session in [
    (88, "P16.1-fixed-actual-reference-all-point-fiber-partial-review", 60650),
    (89, "P16.1-Rossi-neighborhood-repaired-countable-global-review", 54337),
]:
    C = R / f"campaigns/round-{no}" / stem
    proc = subprocess.run(["bash","scripts/cloud.sh","xean","--records","status",str(C / "review.sqlite")],
                          cwd="/workspace/xean", capture_output=True, text=True, check=True)
    state = json.loads(proc.stdout)
    assert state["calls"]["admitted"] == 1
    p = D / f"P16.1-round{no}-native-status.json"
    p.write_text(proc.stdout)
    items.append({"atom":"P16.1","round":no,"directory":str(C),"role":"review",
                  "tool_session_id":session,"observed_status":state["status"],
                  "status":str(p),"status_sha256":sha(p),
                  "hot_feedback_sent":False,"completed_result_granted":False,"original_closed":False})
batch = {"recorded_utc":now,"items":items,
         "active_items":[i for i in items if i["observed_status"]=="running"],
         "route":"Xean native Codex","model":"gpt-6.1-sol","reasoning":"xhigh","original_closed":False,
         "focus":"Exact fiber/reference review88 and fresh essential Rossi-neighborhood repair review89. Actual85 is FAIL and grants none of author83's new chain. Completed conditional author84 remains unreviewed. Accepted86/87 retain only their precise reduction/geometry scopes."}
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1","P15.1","P15.2","P16.6"]
assert sorted(a["fully_solved_original_atoms"]) == sorted(c["fully_solved_original_atoms"]) == sorted(solved)
assert c["historical_reviewed_scoped_papers"] == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
completed = {
    "canonical":str(canonical84),"canonical_sha256":sha(canonical84),
    "reader":str(reader),"candidate":False,"whole_canonical_and_argument_root_read":True,
    "literal_units_reproduced":70,"independently_accepted":False,"original_closed":False,
}
failed = {
    "actual_review":str(actual85),"actual_review_sha256":sha(actual85),"actual_verdict":"FAIL",
    "whole_canonical_report_premises_passages_root_read":True,
    "all_28_nonnegative_bindings_verified":True,"repaired_review_round":89,
    "author83_new_mathematics_granted":False,"original_closed":False,
}
a["continuation96_completed_author84"] = completed
a["continuation96_actual_fail85_and_fresh_repair89"] = failed
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint94: complete conditional author84 public draft and evidence, actual85 FAIL, exact Rossi-neighborhood repair96 and fresh review89. No original closure or new accepted paper."
for t in c["targets"]:
    if t["id"] == "P16.1":
        t["current_focus"] = batch["focus"] + " Full original remains open."
        t["continuation96_completed_author84"] = completed
        t["continuation96_actual_fail85_and_fresh_repair89"] = failed
save(R / "active-work.json", a)
save(R / "checklist-current.json", c)
for name in ["active-work.json","checklist-current.json","checklist-current.tsv"]:
    shutil.copyfile(R / name, D / name)
files = []


def add(path, remote=None):
    p = Path(path)
    assert p.is_file() and not p.is_symlink()
    rel = p.relative_to(R)
    assert p.suffix not in {".sqlite",".jsonl"}
    assert not any(v in {".git",".codex",".aws",".env","auth.json","run.json"} for v in rel.parts)
    files.append({"local":str(p),"path":remote or "research-checkpoints/continuation94/"+str(rel),
                  "bytes":p.stat().st_size,"sha256":sha(p)})


for folder in [reader,D]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for p in [
    canonical84,actual85,
    R / "root-checks/P16.1-round85-actual-review-root-reading-20261005.json",
    R / "root-checks/P16.1-round83-Rossi-neighborhood-repaired-argument-20261005-continuation96.md",
    R / "root-checks/P16.1-round85-Rossi-repair-binding-20261005-continuation96.md",
    R / "prepare_round89_rossi_repair_and_round84_reader_20261005.py",
    R / "complete_round89_rossi_repair_and_round84_reader_20261005.py",
    R / "round89-Rossi-repair-and-round84-reader-preparation-20261005.json",
    G / "prepare_checkpoint_continuation94.py",G / "push-receipt-continuation93.json",
]:
    add(p)
C = R / "campaigns/round-89/P16.1-Rossi-neighborhood-repaired-countable-global-review"
for name in ["task.json","settings.json","argument.md","freeze.json"]:
    add(C / name)
for name in ["active-work.json","checklist-current.json","checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/"+name)
manifest = G / "upload-manifest-continuation94.json"
assert not manifest.exists()
save(manifest, {
    "generated_utc":now,"repository":receipt["repository"],"branch":receipt["branch"],
    "expected_previous_checkpoint":receipt["commit_sha"],"files":files,"file_count":len(files),
    "fully_solved_original_atoms":solved,"remaining_open_atoms":38,"historical_reviewed_scoped_papers":43,
    "commit_message":"Preserve conditional fiber paper and review failure with essential Rossi repair",
    "scope":"Completed conditional author84 public paper and literal evidence, actual85 FAIL with exact root reading scope, essential Rossi neighborhood repair96 and fresh independently reviewed input89, statuses88/89 and verified receipt93. No original closure, new accepted paper, private SQL/transcripts/auth, runtime/account changes, messages to others, editor replacement or book edits.",
})
print(json.dumps({"manifest":str(manifest),"sha256":sha(manifest),"files":len(files),
                  "statuses":[(i["round"],i["observed_status"]) for i in items]},indent=2))
