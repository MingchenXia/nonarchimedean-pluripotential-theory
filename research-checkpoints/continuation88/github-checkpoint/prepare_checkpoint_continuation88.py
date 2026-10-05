"""Freeze fixed-reference fiber research and two independent native continuations."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation88-publication-records"
S = R / "root-checks/continuation88-fiber-reference-primary-read-units"
F = R / "root-checks/P16.1-fixed-curve-reference-fiber-constancy-20261005-continuation88.md"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
assert sha(F) == "0c2f95971b70de6a29474c53553314a7263adae73a415392785673779713019e"
receipt = json.loads((G / "push-receipt-continuation87.json").read_text())
assert receipt["commit_sha"] == "75f622f528dc454780e13bff492357bf5fbe3a6a"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation87.json") == receipt["manifest_sha256"]
reading = json.loads((S / "source-read-record.json").read_text())
assert sha(F) == reading["proposal_sha256"]
for unit in reading["units"]:
    source = Path(unit["source"])
    assert sha(source) == unit["source_sha256"]
    first, last = unit["inclusive_one_based_LF"]
    expected = "\n".join(source.read_bytes().decode().split("\n")[first-1:last]).encode()
    assert Path(unit["literal_file"]).read_bytes() == expected
    assert sha(unit["literal_file"]) == unit["literal_sha256"]
now = datetime.now(timezone.utc).isoformat()
D.mkdir()
items = []
for round_no, name, session in [
    (83, "P16.1-original-witness-trace-and-countable-Runge", 10039),
    (84, "P16.1-fiber-reference-and-finite-data-descent", 20275),
]:
    C = R / f"campaigns/round-{round_no}" / name
    proc = subprocess.run(
        ["bash", "scripts/cloud.sh", "xean", "--records", "status", str(C / "campaign.sqlite")],
        cwd="/workspace/xean", capture_output=True, text=True, check=True,
    )
    state = json.loads(proc.stdout)
    p = D / f"P16.1-round{round_no}-native-status.json"
    p.write_text(proc.stdout)
    freeze = json.loads((C / "freeze.json").read_text())
    assert sha(C / "input.json") == freeze["input_sha256"]
    assert sha(C / "settings.json") == freeze["settings_sha256"]
    assert state["calls"]["admitted"] == 1
    items.append({
        "atom": "P16.1", "round": round_no, "directory": str(C), "role": "codex",
        "tool_session_id": session, "observed_status": state["status"],
        "status": str(p), "status_sha256": sha(p), "original_closed": False,
        "input_sha256": freeze["input_sha256"], "input_bytes": freeze["input_bytes"],
        "settings_sha256": freeze["settings_sha256"], "hot_feedback_sent": False,
    })
batch = {
    "recorded_utc": now, "items": items,
    "active_items": [i for i in items if i["observed_status"] == "running"],
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
    "original_closed": False,
    "focus": "Independent countable Runge reconstruction and fixed-reference fiber/finite-data descent; no pending result is granted.",
}
save(D / "current-small-batch-observation.json", batch)
compile_path = R / "deliverables/scoped-P16.1-round77/native-compile-observation.json"
compile_observation = json.loads(compile_path.read_text())
assert compile_observation["waiting_cell_terminated"]
assert compile_observation["native_success"] is False
assert compile_observation["diagnostics_returned"] is False
assert compile_observation["local_two_pass_success"]
save(D / "native-compile-followup.json", compile_observation)
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1", "P15.1", "P15.2", "P16.6"]
assert sorted(t["id"] for t in c["targets"] if t["fully_solved"]) == solved
assert sum(len(t["reviewed_papers"]) for t in c["targets"]) == 43
assert c["historical_reviewed_scoped_papers"] == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
c["active_atoms"] = sorted(set(i["atom"] for i in batch["active_items"]))
a["continuation88_unreviewed_root_proposal"] = {
    "path": str(F), "sha256": sha(F),
    "source_read_record": str(S / "source-read-record.json"),
    "whole_saved_proposal_root_read": True,
    "accepted_dependency": False, "original_closed": False,
}
a["prepared_P16.1_round84"] = json.loads((R / "round84-fiber-reference-preparation-20261005.json").read_text())
a["P16.1_round77_native_compile_observation"] = c["P16.1_round77_native_compile_observation"] = compile_observation
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint88: fixed-reference fiber draft and sixteen exact primary units, independent native original continuations83/84, actual unverified native compiler followup; original solved count remains four."
for t in c["targets"]:
    if t["id"] == "P16.1":
        t["current_focus"] = "Two native gpt-6.1-sol/xhigh continuations: whole-base/countable Runge (83), fixed-reference fiber constancy and finite-data descent (84). Countable C1 is an explicit conditional hypothesis in 84. Actual singular EP/operator/equation and unchanged original remain open."
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
    files.append({
        "local": str(p), "path": remote or "research-checkpoints/continuation88/" + str(rel),
        "bytes": p.stat().st_size, "sha256": sha(p),
    })


for folder in [S, D]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
C = R / "campaigns/round-84/P16.1-fiber-reference-and-finite-data-descent"
for name in ["input.json", "settings.json", "task-original.json", "assignment-original.txt", "freeze.json"]:
    add(C / name)
for p in [
    F, G / "prepare_checkpoint_continuation88.py", G / "push-receipt-continuation87.json",
    R / "prepare_round84_fiber_reference_and_finite_data_20261005.py",
    R / "round84-fiber-reference-preparation-20261005.json", compile_path,
]:
    add(p)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation88.json"
assert not manifest.exists()
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"],
    "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 38,
    "historical_reviewed_scoped_papers": 43,
    "commit_message": "Preserve fixed-reference fiber descent and finite-data research",
    "scope": "Unreviewed fixed-model curve reference/Green correction and conditional target EP/finite-obstacle route, sixteen exact primary statement/proof units with explicit reading limits; fresh independently focused native original continuation84 retains C1 as a conditional premise while continuation83 runs without hot feedback. Compiler wait terminated without diagnostics or native success; unchanged local paper build remains verified. No original closure, private transcripts/SQL/auth, runtime edits, external messages or book edits.",
})
print(json.dumps({
    "manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
    "statuses": [(i["round"], i["observed_status"]) for i in items],
}, indent=2))
