"""Freeze the unchanged public author83 paper, independent reviews and geometry draft."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation90-publication-records"
P = R / "root-checks/public-P16.1-round-83-final-reader"
S = R / "root-checks/continuation91-geometric-primary-read-units"
F = R / "root-checks/P16.1-geometric-witness-construction-and-countable-local-sequences-20261005-continuation91.md"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    Path(p).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists() and not S.exists()
assert sha(F) == "1b6a3ffdf27b45f892f0bc1e225c721ecb01d4938fe3abeeed1604ac10905eb5"
receipt = json.loads((G / "push-receipt-continuation89.json").read_text())
assert receipt["commit_sha"] == "7f79fe7f3b827e4ee937240dad18680635e8b6e6"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation89.json") == receipt["manifest_sha256"]
prep = json.loads((R / "round85-86-partial-review-preparation-20261005.json").read_text())
for item in prep["items"]:
    C = Path(item["directory"])
    for name, key in [("task.json", "task_sha256"), ("argument.md", "argument_sha256"), ("settings.json", "settings_sha256")]:
        assert sha(C / name) == item[key]
    freeze = json.loads((C / "freeze.json").read_text())
    packet = (C / "argument.md").read_bytes()
    for context in freeze["embedded_context"]:
        p = Path(context["path"])
        assert sha(p) == context["sha256"] and p.stat().st_size == context["bytes"]
        assert p.read_bytes() in packet
D.mkdir()
S.mkdir()
now = datetime.now(timezone.utc).isoformat()
source = R / "shared-sources/Temkin-0904.1592v2-20261005.txt"
pdf = source.with_suffix(".pdf")
assert sha(source) == "c89838b3bca2d63ac132f370bd694d21a4f4ec4987ccd849927160f5576fc5ee"
assert sha(pdf) == "0c5e2f27ff35a48d605ab1573b9acb027b4fd550574855417e643d24336b5cc3"
lines = source.read_bytes().decode().split("\n")
units = []
for first, last in [(83,147),(274,405),(462,553),(1490,1608)]:
    p = S / f"Temkin-0904.1592v2-LF{first}-{last}.txt"
    p.write_bytes("\n".join(lines[first-1:last]).encode())
    units.append({
        "source": str(source), "source_sha256": sha(source),
        "url": "https://arxiv.org/pdf/0904.1592v2",
        "inclusive_one_based_LF": [first,last], "literal_file": str(p),
        "literal_sha256": sha(p), "whole_pertinent_unit_root_read": True,
        "all_recursive_background_proofs_root_read": False,
    })
save(S / "source-read-record.json", {
    "recorded_utc": now, "proposal": str(F), "proposal_sha256": sha(F),
    "whole_current_proposal_root_read": True, "accepted_dependency": False,
    "units": units, "pdf": str(pdf), "pdf_sha256": sha(pdf),
    "live_web_bodies_root_read": [
        {"url":"https://stacks.math.columbia.edu/tag/02O2","rendered_lines":[22,56]},
        {"url":"https://stacks.math.columbia.edu/tag/01OF","rendered_lines":[20,56]},
        {"url":"https://stacks.math.columbia.edu/tag/01VG","rendered_lines":[69,79]},
        {"url":"https://stacks.math.columbia.edu/tag/0HA6","rendered_lines":[61,70]},
        {"url":"https://stacks.math.columbia.edu/tag/01IQ","rendered_lines":[22,26]},
    ],
    "limit": "Rendered web coordinates are not original-HTML LF or immutable editions. Pertinent primary units were read, not all recursively cited proofs or whole sources. New geometry and sequence applications remain unreviewed.",
})
items = []
for round_no, name, database, session in [
    (84, "P16.1-fiber-reference-and-finite-data-descent", "campaign.sqlite", 20275),
    (85, "P16.1-whole-base-trace-and-countable-Runge-partial-review", "review.sqlite", 52293),
    (86, "P16.1-exact-envelope-and-cardinality-reductions-partial-review", "review.sqlite", 43321),
]:
    C = R / f"campaigns/round-{round_no}" / name
    proc = subprocess.run(
        ["bash","scripts/cloud.sh","xean","--records","status",str(C / database)],
        cwd="/workspace/xean", capture_output=True, text=True, check=True,
    )
    state = json.loads(proc.stdout)
    p = D / f"P16.1-round{round_no}-native-status.json"
    p.write_text(proc.stdout)
    assert state["calls"]["admitted"] == 1
    items.append({
        "atom":"P16.1","round":round_no,"directory":str(C),
        "role":"codex" if round_no==84 else "review",
        "tool_session_id":session,"observed_status":state["status"],
        "status":str(p),"status_sha256":sha(p),"original_closed":False,
        "hot_feedback_sent":False,"completed_result_granted":False,
    })
batch = {
    "recorded_utc":now,"items":items,
    "active_items":[i for i in items if i["observed_status"]=="running"],
    "route":"Xean native Codex","model":"gpt-6.1-sol","reasoning":"xhigh",
    "original_closed":False,
    "focus":"Independent fiber-reference continuation84 and two exact partial reviews85/86; completed unchanged author83 public paper is preserved, not accepted before review. New sourced geometry/sequence draft remains unreviewed.",
}
save(D / "current-small-batch-observation.json",batch)
read_state = json.loads((P / "root-preservation-and-read-state-continuation90.json").read_text())
assert read_state["whole_argument_root_read"] and read_state["whole_canonical_notes_root_read"]
assert read_state["literal_units_reproduced"] == 54
assert read_state["external_premise_binding_units_reproduced"] == 13
paper = P / "P16.1-paper.pdf"
tex = P / "P16.1-paper.tex"
assert sha(paper) == "0fd85a26968e72d150ac7f58f8f46125bfdae17ad7376564a97967399e72ade6"
assert sha(tex) == "c95d1e5185b3225a551028c3c92a559f6f02d4821e532f2e41a8fcb37471a838"
save(D / "author83-paper-preservation.json", {
    "reader":str(P),"argument_sha256":sha(P / "P16.1-argument.md"),
    "tex":str(tex),"tex_sha256":sha(tex),"pdf":str(paper),"pdf_sha256":sha(paper),
    "native_author_candidate":False,"independent_mathematical_review":85,
    "accepted_partial_paper":False,"original_closed":False,
    "native_editor_compilation_attempted":False,
    "native_editor_service_prior_observation":"Prior requests yielded no successful native diagnostics. Existing P16.4 editor remains unchanged; no new tab opened and no runtime installation performed.",
})
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1","P15.1","P15.2","P16.6"]
assert sorted(t["id"] for t in c["targets"] if t["fully_solved"]) == solved
assert sum(len(t["reviewed_papers"]) for t in c["targets"]) == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
c["active_atoms"] = sorted(set(i["atom"] for i in batch["active_items"]))
a["continuation91_unreviewed_geometry"] = {
    "path":str(F),"sha256":sha(F),"source_read_record":str(S / "source-read-record.json"),
    "accepted_dependency":False,"original_closed":False,
}
a["prepared_partial_reviews85_86"] = prep
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint90: unchanged public conditional author83 paper/source reader, independent exact reviews85/86, sourced geometric witness/sequence draft and four Temkin proof units. Original solved count remains four."
for t in c["targets"]:
    if t["id"] == "P16.1":
        t["current_focus"] = batch["focus"] + " Actual singular countable EP/full original equation remain open."
save(R / "active-work.json",a)
save(R / "checklist-current.json",c)
for name in ["active-work.json","checklist-current.json","checklist-current.tsv"]:
    shutil.copyfile(R / name,D / name)
files = []


def add(path, remote=None):
    p = Path(path)
    assert p.is_file() and not p.is_symlink()
    rel = p.relative_to(R)
    assert p.suffix not in {".sqlite",".jsonl"}
    assert not any(v in {".git",".codex",".aws",".env","auth.json","run.json"} for v in rel.parts)
    files.append({
        "local":str(p),"path":remote or "research-checkpoints/continuation90/"+str(rel),
        "bytes":p.stat().st_size,"sha256":sha(p),
    })


for folder in [P,S,D]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for no, stem in [
    (85,"P16.1-whole-base-trace-and-countable-Runge-partial-review"),
    (86,"P16.1-exact-envelope-and-cardinality-reductions-partial-review"),
]:
    C = R / f"campaigns/round-{no}" / stem
    for name in ["task.json","argument.md","settings.json","freeze.json"]:
        add(C / name)
for p in [
    F,pdf,source,
    R / "root-checks/continuation90-live-Stacks-primary-observation-20261005.json",
    R / "root-checks/continuation91-geometry-primary-observation-1.json",
    R / "root-checks/continuation91-geometry-primary-observation-2.json",
    R / "root-checks/continuation91-geometry-primary-observation-3.json",
    R / "prepare_round85_86_partial_reviews_20261005.py",
    R / "round85-86-partial-review-preparation-20261005.json",
    G / "prepare_checkpoint_continuation90.py", G / "push-receipt-continuation89.json",
]:
    add(p)
for name in ["active-work.json","checklist-current.json","checklist-current.tsv"]:
    add(D / name,"manuscript/editorial/xean_research_20261003/"+name)
manifest = G / "upload-manifest-continuation90.json"
assert not manifest.exists()
save(manifest, {
    "generated_utc":now,"repository":receipt["repository"],"branch":receipt["branch"],
    "expected_previous_checkpoint":receipt["commit_sha"],
    "files":files,"file_count":len(files),
    "fully_solved_original_atoms":solved,"remaining_open_atoms":38,
    "historical_reviewed_scoped_papers":43,
    "commit_message":"Preserve conditional Runge paper and independently review envelope reductions",
    "scope":"Unchanged actual completed native83 conditional paper, sources and canonical notes, exact independently bound native85/86 partial review inputs, fresh84/85/86 statuses, unreviewed source-aware GEO construction and countable local sequence extraction, primary Temkin theorem/proof units and actual live Stacks observations. No original closure, private transcripts/SQL/auth, account/runtime changes, external messages, editor replacement or book edits.",
})
print(json.dumps({
    "manifest":str(manifest),"sha256":sha(manifest),"files":len(files),
    "statuses":[(i["round"],i["observed_status"]) for i in items],
},indent=2))
