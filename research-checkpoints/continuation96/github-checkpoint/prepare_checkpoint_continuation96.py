"""Preserve completed partial reviews88/89 and corrected stable-model sources."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation96-publication-records"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    p = Path(p)
    assert not p.exists()
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
receipt = json.loads((G / "push-receipt-continuation95.json").read_text())
assert receipt["commit_sha"] == "d03d38fd320196e3c8063930c6dc07ee0fb352ac"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation95.json") == receipt["manifest_sha256"]
D.mkdir()
now = datetime.now(timezone.utc).isoformat()
items = []
reports = []
for atom, no, stem, session in [
    ("P16.1", 88, "P16.1-fixed-actual-reference-all-point-fiber-partial-review", 60650),
    ("P16.1", 89, "P16.1-Rossi-neighborhood-repaired-countable-global-review", 54337),
    ("P13.2", 90, "P13.2-normal-quotient-QEP-conditional-realization-partial-review", 77740),
]:
    C = R / f"campaigns/round-{no}" / stem
    proc = subprocess.run(
        ["bash", "scripts/cloud.sh", "xean", "--records", "status", str(C / "review.sqlite")],
        cwd="/workspace/xean", capture_output=True, text=True, check=True,
    )
    state = json.loads(proc.stdout)
    assert state["calls"]["admitted"] == 1
    p = D / f"{atom}-round{no}-native-status.json"
    assert not p.exists()
    p.write_text(proc.stdout)
    items.append({
        "atom": atom, "round": no, "directory": str(C), "role": "review",
        "tool_session_id": session, "observed_status": state["status"],
        "status": str(p), "status_sha256": sha(p), "hot_feedback_sent": False,
        "completed_result_granted": no in (88, 89), "original_closed": False,
    })
    if no not in (88, 89):
        continue
    run = json.loads((C / "run.json").read_text())["campaign"]
    result = run["result"]
    assert state["status"] == run["status"] == "completed"
    assert result["verdict"] == "PASS" and result["kind"] == "codex-report"
    counts = {88: (18, 29), 89: (23, 32)}
    assert (len(result["premises"]), len(result["passages"])) == counts[no]
    coverage = set()
    for passage in result["passages"]:
        index = passage["premise"]
        if index < 0:
            continue
        assert index < len(result["premises"])
        premise = result["premises"][index]
        statement = premise["statement"] if isinstance(premise, dict) else premise
        assert statement == passage["statement"]
        coverage.add(index)
    assert coverage == set(range(len(result["premises"])))
    actual = R / f"root-checks/P16.1-round{no}-actual-partial-mathematical-review-20261005.json"
    save(actual, result)
    binding = R / f"root-checks/P16.1-round{no}-binding-reading-clarifications-20261005.md"
    assert binding.exists()
    record = {
        "round": no, "canonical_result": str(actual), "canonical_sha256": sha(actual),
        "operation_id": result["operationId"], "reported_at": result["reportedAt"],
        "input_argument": str(C / "argument.md"), "input_argument_sha256": sha(C / "argument.md"),
        "input_task": str(C / "task.json"), "input_task_sha256": sha(C / "task.json"),
        "binding": str(binding), "binding_sha256": sha(binding),
        "whole_canonical_report_root_read": True, "all_premises_and_passages_root_read": True,
        "all_nonnegative_passage_bindings_verified": True,
        "premise_count": len(result["premises"]), "passage_count": len(result["passages"]),
        "all_recursive_primary_proofs_root_read": False,
        "accepted_scope": (
            "All-point fiber constancy, scalar usc descent and actual resolution fibers of root92+93."
            if no == 88 else
            "Exact repaired original-witness trace, controlled tools, conditional countable global contact and original-reference projective membership consequence."
        ),
        "global_join_accepted": False, "original_closed": False, "new_paper_accepted": False,
    }
    save(D / f"P16.1-round{no}-canonical-reading-binding.json", record)
    reports.append(record)
F = R / "root-checks/P16.1-stable-domination-of-the-specified-curve-graph-model-20261005-continuation98.md"
S = R / "root-checks/continuation98-stable-model-primary-read-units"
reading = json.loads((S / "source-read-record.json").read_text())
assert sha(F) == reading["proposal_sha256"]
assert reading["whole_current_proposal_root_read"] and not reading["mathematics_accepted"]
for unit in reading["units"]:
    assert sha(unit["source"]) == unit["source_sha256"]
    assert sha(unit["literal_file"]) == unit["literal_sha256"]
batch = {
    "recorded_utc": now, "items": items,
    "active_items": [i for i in items if i["observed_status"] == "running"],
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
    "original_closed": False,
    "focus": "Completed partial PASS88/89 now await a new original-reference join and full theorem review; QEP-conditional P13.2 review90 is independent.",
}
save(D / "current-small-batch-observation.json", batch)
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1", "P15.1", "P15.2", "P16.6"]
assert sorted(a["fully_solved_original_atoms"]) == sorted(c["fully_solved_original_atoms"]) == sorted(solved)
assert c["historical_reviewed_scoped_papers"] == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
a["completed_partial_reviews88_89"] = reports
proposal = {
    "path": str(F), "sha256": sha(F), "whole_current_body_root_read": True,
    "source_read_record": str(S / "source-read-record.json"),
    "new_mathematics_accepted": False, "original_closed": False,
    "correction": reading["source_body_correction"],
}
a["continuation98_stable_model_source_correction"] = proposal
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint96: actual partial PASS88/89 with complete report reading and exact bindings; corrected complete Temkin source and unreviewed root98. No original closure or new paper."
for target in c["targets"]:
    if target["id"] == "P16.1":
        target["completed_partial_reviews88_89"] = reports
        target["current_focus"] = "All-point fiber descent88 and repaired conditional global contact89 separately passed; application of contacts to descended potentials and a full original theorem remain unreviewed."
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
    files.append({
        "local": str(p), "path": remote or "research-checkpoints/continuation96/" + str(rel),
        "bytes": p.stat().st_size, "sha256": sha(p),
    })


for folder in [S, D]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for p in [
    F, R / "root-checks/continuation98-live-stable-modification-primary-observation.json",
    R / "prepare_continuation98_stable_model_primary_units_20261005.py",
    G / "prepare_checkpoint_continuation96.py", G / "push-receipt-continuation95.json",
]:
    add(p)
for record in reports:
    add(record["canonical_result"])
    add(record["binding"])
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation96.json"
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"], "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 38,
    "historical_reviewed_scoped_papers": 43,
    "commit_message": "Preserve all-point descent and repaired global contact partial reviews",
    "scope": "Actual completed partial PASS88/89, whole reports and premise bindings, complete valuation-ring gluing source correction98 and its unreviewed model application, statuses88/89/90 and receipt95. Full join and original P16.1 remain open. No private SQL/transcripts/auth, runtime/account changes, editor replacement or book edits.",
})
print(json.dumps({
    "manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
    "statuses": [(i["atom"], i["round"], i["observed_status"]) for i in items],
    "reports": [(r["round"], r["canonical_sha256"]) for r in reports],
}, indent=2))
