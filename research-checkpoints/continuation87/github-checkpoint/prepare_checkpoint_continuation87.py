"""Freeze two precise-scope PASS publications and the next unchanged original continuation."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation87-publication-records"
S = R / "root-checks/continuation87-Runge-primary-read-units"
F = R / "root-checks/P16.1-Runge-barriers-pole-clearing-and-split-trace-20261005-continuation87.md"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
assert sha(F) == "975bcc9b423528c07d9fb7e8d0f13929a86f71a4b8e85896636e713c2ed5ab2d"
receipt = json.loads((G / "push-receipt-continuation86.json").read_text())
assert receipt["commit_sha"] == "06ee2da1a57841d80d6d804665d410472399591d"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation86.json") == receipt["manifest_sha256"]
pubs = [R / "deliverables/scoped-P16.1-round77", R / "deliverables/scoped-P13.2-round79"]
for pub in pubs:
    rec = json.loads((pub / "publication-preparation.json").read_text())
    review = json.loads(Path(rec["review"]).read_text())
    assert rec["verdict"] == review["verdict"] == "PASS"
    assert sha(rec["review"]) == rec["review_sha256"]
    assert rec["full_original_atom_solved"] is False
    for key in ["source", "pdf", "argument"]:
        assert sha(rec[key]) == rec[key + "_sha256"]
now = datetime.now(timezone.utc).isoformat()
D.mkdir()
items = []
for round_no, atom, name, role, database, session in [
    (80, "P16.1", "P16.1-compact-IBP-smooth-gate-partial-mathematical-review", "review", "review.sqlite", 82517),
    (81, "P13.2", "P13.2-smooth-rational-quotient-actual-realization-partial-review", "review", "review.sqlite", 75571),
    (82, "P16.1", "P16.1-original-witness-trace-and-countable-Runge", "codex", "campaign.sqlite", None),
    (83, "P16.1", "P16.1-original-witness-trace-and-countable-Runge", "codex", "campaign.sqlite", 10039),
]:
    C = R / f"campaigns/round-{round_no}" / name
    proc = subprocess.run(["bash", "scripts/cloud.sh", "xean", "--records", "status", str(C / database)],
                          cwd="/workspace/xean", capture_output=True, text=True, check=True)
    state = json.loads(proc.stdout)
    p = D / f"{atom}-round{round_no}-native-status.json"
    p.write_text(proc.stdout)
    item = {"atom": atom, "round": round_no, "directory": str(C), "role": role,
            "tool_session_id": session, "observed_status": state["status"],
            "status": str(p), "status_sha256": sha(p), "original_closed": False}
    if role == "review":
        assert state["status"] == "completed"
        actual = json.loads((C / "run.json").read_text())["campaign"]["result"]
        assert actual["verdict"] == "PASS"
        item.update({"actual_verdict": "PASS", "operation_id": actual["operationId"],
                     "task_sha256": sha(C / "task.json"), "argument_sha256": sha(C / "argument.md"),
                     "settings_sha256": sha(C / "settings.json"), "hot_feedback_sent": False})
    else:
        rec = json.loads((C / "freeze.json").read_text())
        assert sha(C / "input.json") == rec["input_sha256"]
        assert sha(C / "settings.json") == rec["settings_sha256"]
        item.update({"input_sha256": rec["input_sha256"], "settings_sha256": rec["settings_sha256"],
                     "input_bytes": (C / "input.json").stat().st_size})
        if round_no == 82:
            assert state["status"] == "blocked" and state["calls"]["admitted"] == 0
            item["actual_native_result"] = None
    items.append(item)
batch = {"recorded_utc": now, "items": items,
         "active_items": [i for i in items if i["observed_status"] == "running"],
         "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
         "original_closed": False, "focus": "Same-witness weak trace, repaired pole clearing and full countable Runge/Hartogs/singular-stratum chain."}
save(D / "current-small-batch-observation.json", batch)
save(D / "native-compile-observation.json", {
    "P13.2_round79": json.loads((pubs[1] / "native-compile-observation.json").read_text()),
    "P16.1_round77": {"cell_id": "385", "path": str(pubs[0] / "P16.1-paper.tex"),
                    "state": "Pending actual built-in response; no native success or diagnostics asserted.",
                    "local_two_pass_compilation": "SUCCESS, unchanged author source/PDF."},
    "existing_P16_4_editor_unchanged_and_open": True,
})
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1", "P15.1", "P15.2", "P16.6"]
assert sorted(t["id"] for t in c["targets"] if t["fully_solved"]) == solved
assert sum(len(t["reviewed_papers"]) for t in c["targets"]) == 43
assert c["historical_reviewed_scoped_papers"] == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
c["active_atoms"] = [i["atom"] for i in batch["active_items"]]
a["continuation87_unreviewed_root_proposal"] = {
    "path": str(F), "sha256": sha(F), "source_read_record": str(S / "source-read-record.json"),
    "whole_saved_proposal_root_read": True, "accepted_dependency": False, "original_closed": False,
}
a["prepared_P16.1_round83"] = json.loads((R / "round83-trace-Runge-preparation-20261005.json").read_text())
a["round82_config_failure"] = str(R / "round82-zero-admission-config-failure-20261005.json")
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint87: two genuine exact-scope partial PASS papers, repaired Runge draft, preserved zero-admission config failure and new native original continuation83."
save(R / "active-work.json", a)
save(R / "checklist-current.json", c)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    shutil.copyfile(R / name, D / name)
files = []


def add(path, remote=None):
    p = Path(path)
    assert p.is_file() and not p.is_symlink()
    rel = p.relative_to(R)
    assert p.suffix not in {".sqlite", ".jsonl"}
    assert not any(x in {".git", ".codex", ".aws", ".env", "auth.json", "run.json"} for x in rel.parts)
    files.append({"local": str(p), "path": remote or "research-checkpoints/continuation87/" + str(rel),
                  "bytes": p.stat().st_size, "sha256": sha(p)})


for folder in [*pubs, S, D]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for round_no in [82, 83]:
    C = R / f"campaigns/round-{round_no}/P16.1-original-witness-trace-and-countable-Runge"
    for name in ["input.json", "settings.json", "task-original.json", "assignment-original.txt", "freeze.json"]:
        add(C / name)
for p in [
    F, G / "prepare_checkpoint_continuation87.py", G / "push-receipt-continuation86.json",
    R / "root-checks/P16.1-round80-actual-partial-mathematical-review-20261005.json",
    R / "root-checks/P13.2-round81-actual-partial-mathematical-review-20261005.json",
    R / "publish_scoped_P16_1_round77_review80_20261005.py",
    R / "publish_scoped_P13_2_round79_review81_20261005.py",
    R / "prepare_round82_trace_Runge_reconstruction_20261005.py",
    R / "prepare_round83_correct_codex_worker_20261005.py",
    R / "round82-trace-Runge-preparation-20261005.json",
    R / "round83-trace-Runge-preparation-20261005.json",
    R / "round82-zero-admission-config-failure-20261005.json",
]:
    add(p)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation87.json"
assert not manifest.exists()
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"], "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 38,
    "historical_reviewed_scoped_papers": 43,
    "commit_message": "Preserve reviewed compact gates and actual smooth-quotient realization",
    "scope": "Unchanged round77 and round79 standalone partial papers with actual independent round80/81 precise-scope PASS, complete reports and bound inputs; binding harmless reading errata retained. New unreviewed pole-clearing/entropy-barrier/split-trace reconstruction and ten literal primary units. Zero-admission round82 writer-config failure preserved; byte-identical native mathematical continuation83 uses prior successful writer model/command config. No new original closure, auth/runtime edits, private records/transcripts, external messages or live book changes.",
})
print(json.dumps({"manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
                  "statuses": [(i["round"], i["atom"], i["observed_status"]) for i in items]}, indent=2))
