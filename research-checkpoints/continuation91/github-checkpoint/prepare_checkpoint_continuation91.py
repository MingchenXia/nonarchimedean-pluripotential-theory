"""Freeze reviewed reductions, the independent GEO review and the new fiber draft."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation91-publication-records"
S = R / "root-checks/continuation92-fixed-reference-primary-read-units"
F = R / "root-checks/P16.1-fixed-actual-ample-perturbation-fiber-descent-20261005-continuation92.md"
V = R / "root-checks/P16.1-round86-actual-partial-mathematical-review-20261005.json"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, v):
    Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2) + "\n")


assert not D.exists() and not S.exists()
receipt = json.loads((G / "push-receipt-continuation90.json").read_text())
assert receipt["commit_sha"] == "185b8faac5e3e44c4d3270d9c8fc7d527beb5eae"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation90.json") == receipt["manifest_sha256"]
assert sha(V) == "7b995e992b639a526491b52eb85255c613e3f1e980235490858be3c6fde6616c"
review = json.loads(V.read_text())
assert review["verdict"] == "PASS" and len(review["premises"]) == 27 and len(review["passages"]) == 39
assert {p["premise"] for p in review["passages"]} == set(range(27))
for p in review["passages"]:
    assert isinstance(p["premise"], int) and p["premise"] >= 0
    assert p["statement"] == review["premises"][p["premise"]]
prep = json.loads((R / "round87-geometric-witness-review-preparation-20261005.json").read_text())
C87 = Path(prep["directory"])
for n, key in [("task.json", "task_sha256"), ("argument.md", "argument_sha256"), ("settings.json", "settings_sha256")]:
    assert sha(C87 / n) == prep[key]
for c in prep["embedded_context"]:
    p = Path(c["path"])
    assert sha(p) == c["sha256"] and p.stat().st_size == c["bytes"]
    assert p.read_bytes() in (C87 / "argument.md").read_bytes()
D.mkdir()
S.mkdir()
now = datetime.now(timezone.utc).isoformat()
units = []
sources = [
    ("BE-1805.01016v3", R / "shared-sources/P16-arxiv-1805.01016-20261004.txt",
     "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
     "https://arxiv.org/pdf/1805.01016v3", [(1514,1590),(1970,1995),(2765,2808)]),
    ("Thuillier-tel-00010990v1", R / "shared-sources/Thuillier-tel-00010990v1.txt",
     "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
     "https://theses.hal.science/tel-00010990v1/document", [(3366,3445),(4800,4902)]),
    ("Wanner-1801.04713v3", R / "shared-sources/Wanner-1801.04713v3-20261004.txt",
     None, "https://arxiv.org/pdf/1801.04713v3", [(735,821)]),
]
old = json.loads((R / "root-checks/continuation88-fiber-reference-primary-read-units/source-read-record.json").read_text())
for label, source, expected, url, ranges in sources:
    if expected is None:
        bindings = [u for u in old["units"] if "Wanner" in str(u["source"])]
        assert bindings and len({u["source_sha256"] for u in bindings}) == 1
        expected = bindings[0]["source_sha256"]
    assert sha(source) == expected
    lines = source.read_bytes().decode().split("\n")
    for first, last in ranges:
        p = S / f"{label}-LF{first}-{last}.txt"
        p.write_bytes("\n".join(lines[first-1:last]).encode())
        units.append({
            "source": str(source), "source_sha256": sha(source), "url": url,
            "inclusive_one_based_LF": [first,last], "literal_file": str(p),
            "literal_sha256": sha(p), "whole_pertinent_unit_root_read": True,
            "whole_source_file_root_read": False, "all_recursive_proofs_root_read": False,
        })
save(S / "source-read-record.json", {
    "recorded_utc": now, "proposal": str(F), "proposal_sha256": sha(F),
    "whole_current_proposal_root_read": True, "accepted_dependency": False,
    "units": units,
    "prior_pertinent_primary_units": str(R / "root-checks/continuation88-fiber-reference-primary-read-units/source-read-record.json"),
    "limit": "Only exact pertinent bodies read, not whole source files or every recursive semistable/model/curve-chain proof. New fixed-reference fiber descent and its proposed join remain unreviewed.",
})
save(D / "round86-actual-review-root-reading.json", {
    "recorded_utc": now, "canonical": str(V), "sha256": sha(V),
    "verdict": review["verdict"], "operation_id": review["operationId"],
    "reported_utc": review["reportedAt"], "whole_report_root_read": True,
    "all_27_premises_and_39_passages_root_read": True,
    "all_nonnegative_exact_statement_bindings_verified": True,
    "all_listed_external_proof_bodies_root_read": False,
    "binding_clarifications": str(R / "root-checks/P16.1-round86-binding-reading-clarifications-20261005.md"),
    "scope": "Only exact conditional partial review task. E, fiber constancy and countable C1 remain missing. No original closure.",
})
P83 = R / "root-checks/public-P16.1-round-83-final-reader"
external = json.loads((P83 / "external-premises.json").read_text())
assert len(external["premises"]) == 13
save(D / "round83-external-primary-reading-addendum.json", {
    "recorded_utc": now, "reader": str(P83),
    "unchanged_preservation_record": str(P83 / "root-preservation-and-read-state-continuation90.json"),
    "all_13_external_primary_statement_and_proof_literal_bodies_root_read": True,
    "whole_source_files_root_read": False, "all_54_primary_literal_units_root_read": False,
    "independently_accepts_author83_mathematics": False,
    "units": [{"file": str(P83 / p["literal_file"]), "sha256": sha(P83 / p["literal_file"])}
              for p in external["passages"]],
    "scope": "Later primary reading addendum only; frozen continuation90 preservation record remains unchanged.",
})
items = []
for no, stem, database, session in [
    (84, "P16.1-fiber-reference-and-finite-data-descent", "campaign.sqlite", 20275),
    (85, "P16.1-whole-base-trace-and-countable-Runge-partial-review", "review.sqlite", 52293),
    (86, "P16.1-exact-envelope-and-cardinality-reductions-partial-review", "review.sqlite", 43321),
    (87, "P16.1-geometric-witness-and-countable-sequence-partial-review", "review.sqlite", 98926),
]:
    C = R / f"campaigns/round-{no}" / stem
    proc = subprocess.run(["bash","scripts/cloud.sh","xean","--records","status",str(C / database)],
                          cwd="/workspace/xean", capture_output=True, text=True, check=True)
    state = json.loads(proc.stdout)
    p = D / f"P16.1-round{no}-native-status.json"
    p.write_text(proc.stdout)
    assert state["calls"]["admitted"] == 1
    items.append({
        "atom":"P16.1", "round":no, "directory":str(C),
        "role":"codex" if no==84 else "review", "tool_session_id":session,
        "observed_status":state["status"], "status":str(p), "status_sha256":sha(p),
        "original_closed":False, "hot_feedback_sent":False,
        "completed_result_granted":no==86,
    })
batch = {
    "recorded_utc": now, "items": items,
    "active_items":[i for i in items if i["observed_status"]=="running"],
    "route":"Xean native Codex", "model":"gpt-6.1-sol", "reasoning":"xhigh",
    "original_closed":False,
    "focus":"Exact envelope/cardinality reductions86 accepted conditionally; independent fiber author84, original-witness/global-chain review85 and geometric-witness review87 remain independent. New fixed-actual-ample-perturbation fiber draft92 is unreviewed.",
}
save(D / "current-small-batch-observation.json", batch)
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1","P15.1","P15.2","P16.6"]
assert sorted(a["fully_solved_original_atoms"]) == sorted(c["fully_solved_original_atoms"]) == sorted(solved)
assert c["historical_reviewed_scoped_papers"] == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
a["P16.1_round86_reviewed_conditional_reductions"] = json.loads((D / "round86-actual-review-root-reading.json").read_text())
a["prepared_P16.1_round87_geometric_review"] = prep
a["continuation92_unreviewed_fiber_proposal"] = {
    "path":str(F),"sha256":sha(F),"whole_saved_proposal_root_read":True,
    "source_read_record":str(S / "source-read-record.json"),
    "accepted_dependency":False,"original_closed":False,
}
a["continuation89_unreviewed_reductions"]["accepted_dependency"] = True
a["continuation89_unreviewed_reductions"]["binding_actual_partial_review"] = str(V)
a["continuation89_unreviewed_reductions"]["binding_clarifications"] = str(R / "root-checks/P16.1-round86-binding-reading-clarifications-20261005.md")
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint91: actual conditional reductions PASS86, independent GEO review87, unreviewed fixed-actual-bundle fiber draft92 and six literal primary units. Original solved count remains four."
for t in c["targets"]:
    if t["id"] == "P16.1":
        t["current_focus"] = batch["focus"] + " Full original remains open."
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
    files.append({"local":str(p),"path":remote or "research-checkpoints/continuation91/"+str(rel),
                  "bytes":p.stat().st_size,"sha256":sha(p)})


for folder in [S,D]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for name in ["task.json","argument.md","settings.json","freeze.json"]:
    add(C87 / name)
for p in [
    F,V,R / "root-checks/P16.1-round86-binding-reading-clarifications-20261005.md",
    R / "prepare_round87_geometric_witness_review_20261005.py",
    R / "round87-geometric-witness-review-preparation-20261005.json",
    G / "prepare_checkpoint_continuation91.py", G / "push-receipt-continuation90.json",
]:
    add(p)
for label, source, expected, url, ranges in sources:
    add(source)
for name in ["active-work.json","checklist-current.json","checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/"+name)
manifest = G / "upload-manifest-continuation91.json"
assert not manifest.exists()
save(manifest, {
    "generated_utc":now,"repository":receipt["repository"],"branch":receipt["branch"],
    "expected_previous_checkpoint":receipt["commit_sha"],
    "files":files,"file_count":len(files),
    "fully_solved_original_atoms":solved,"remaining_open_atoms":38,
    "historical_reviewed_scoped_papers":43,
    "commit_message":"Record conditional envelope review and fixed-reference fiber descent draft",
    "scope":"Actual partial PASS86 with binding scope and clarifications, independent immutable GEO/sequence review87 inputs, unreviewed fixed-actual-ample-perturbation fiber draft92, six exact pertinent primary units, later author83 external-proof reading addendum, and fresh84/85/86/87 statuses. No original closure or new reviewed paper; no private transcripts/SQL/auth, runtime/account changes, external messages, editor replacement or book edits.",
})
print(json.dumps({"manifest":str(manifest),"sha256":sha(manifest),"files":len(files),
                  "statuses":[(i["round"],i["observed_status"]) for i in items]},indent=2))
