"""Freeze actual GEO acceptance and the immutable all-point fiber review input."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation92-publication-records"
S = R / "root-checks/continuation93-curve-current-primary-read-units"
V = R / "root-checks/P16.1-round87-actual-partial-mathematical-review-20261005.json"
F = R / "root-checks/P16.1-curve-current-identity-and-boundary-clarifications-20261005-continuation93.md"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, v):
    Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
receipt = json.loads((G / "push-receipt-continuation91.json").read_text())
assert receipt["commit_sha"] == "67fc5cf18c57a68fb9f367d1edc4a2d408b7c9b5"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation91.json") == receipt["manifest_sha256"]
assert sha(V) == "915213c661085fbb723973f27cfaa732d3cdbf3893088c47120900d0ac7af50f"
review = json.loads(V.read_text())
assert review["verdict"] == "PASS" and len(review["premises"]) == 10 and len(review["passages"]) == 15
assert {p["premise"] for p in review["passages"]} == set(range(10))
for p in review["passages"]:
    assert isinstance(p["premise"],int) and p["premise"]>=0
    assert p["statement"] == review["premises"][p["premise"]]
prep = json.loads((R / "round88-fixed-reference-fiber-review-preparation-20261005.json").read_text())
C = Path(prep["directory"])
for n,k in [("task.json","task_sha256"),("argument.md","argument_sha256"),("settings.json","settings_sha256")]:
    assert sha(C / n) == prep[k]
packet = (C / "argument.md").read_bytes()
for x in prep["embedded_context"]:
    p = Path(x["path"])
    assert sha(p) == x["sha256"] and p.read_bytes() in packet
rr = json.loads((S / "source-read-record.json").read_text())
assert rr["proposal_sha256"] == sha(F) and rr["whole_current_proposal_root_read"]
for u in rr["units"]:
    p = Path(u["literal_file"])
    source = Path(u["source"])
    assert sha(p)==u["literal_sha256"] and sha(source)==u["source_sha256"]
    first,last = u["inclusive_one_based_LF"]
    assert p.read_bytes()=="\n".join(source.read_bytes().decode().split("\n")[first-1:last]).encode()
pdf = Path(rr["GK_pdf"])
assert sha(pdf) == rr["GK_pdf_sha256"]
D.mkdir()
now = datetime.now(timezone.utc).isoformat()
save(D / "round87-actual-review-root-reading.json", {
    "recorded_utc":now,"canonical":str(V),"sha256":sha(V),"verdict":"PASS",
    "operation_id":review["operationId"],"reported_utc":review["reportedAt"],
    "whole_report_premises_and_passages_root_read":True,
    "all_nonnegative_exact_statement_bindings_verified":True,
    "premises":10,"passages":15,"all_external_primary_proof_bodies_root_read":False,
    "binding_clarifications":str(R / "root-checks/P16.1-round87-binding-reading-clarifications-20261005.md"),
    "original_closed":False,
})
items = []
for no,stem,database,session in [
    (84,"P16.1-fiber-reference-and-finite-data-descent","campaign.sqlite",20275),
    (85,"P16.1-whole-base-trace-and-countable-Runge-partial-review","review.sqlite",52293),
    (87,"P16.1-geometric-witness-and-countable-sequence-partial-review","review.sqlite",98926),
    (88,"P16.1-fixed-actual-reference-all-point-fiber-partial-review","review.sqlite",60650),
]:
    c = R / f"campaigns/round-{no}" / stem
    proc = subprocess.run(["bash","scripts/cloud.sh","xean","--records","status",str(c / database)],
                          cwd="/workspace/xean",capture_output=True,text=True,check=True)
    state = json.loads(proc.stdout)
    p = D / f"P16.1-round{no}-native-status.json"
    p.write_text(proc.stdout)
    assert state["calls"]["admitted"]==1
    items.append({"atom":"P16.1","round":no,"directory":str(c),
                  "role":"codex" if no==84 else "review","tool_session_id":session,
                  "observed_status":state["status"],"status":str(p),"status_sha256":sha(p),
                  "completed_result_granted":no==87,"original_closed":False,"hot_feedback_sent":False})
batch = {"recorded_utc":now,"items":items,
         "active_items":[i for i in items if i["observed_status"]=="running"],
         "route":"Xean native Codex","model":"gpt-6.1-sol","reasoning":"xhigh","original_closed":False,
         "focus":"Conditional reductions86 and geometric/sequence construction87 independently accepted; original-witness/global C1 review85 and fixed-reference all-point fiber review88 pending, with independent author84 still running. Fresh current/boundary addendum93 remains unreviewed."}
save(D / "current-small-batch-observation.json",batch)
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1","P15.1","P15.2","P16.6"]
assert sorted(a["fully_solved_original_atoms"])==sorted(c["fully_solved_original_atoms"])==sorted(solved)
assert c["historical_reviewed_scoped_papers"]==43
a["updated_utc"]=c["updated_utc"]=now
a["current_small_batch"]=c["current_small_batch"]=batch
a["P16.1_round87_reviewed_geometry_and_sequences"]=json.loads((D / "round87-actual-review-root-reading.json").read_text())
a["prepared_P16.1_round88_fiber_review"]=prep
a["continuation91_unreviewed_geometry"]["accepted_dependency"]=True
a["continuation91_unreviewed_geometry"]["binding_actual_partial_review"]=str(V)
a["continuation93_unreviewed_current_addendum"]={
    "path":str(F),"sha256":sha(F),"whole_saved_proposal_root_read":True,
    "source_read_record":str(S / "source-read-record.json"),"accepted_dependency":False,"original_closed":False}
a["github_checkpoint"]=c["latest_verified_github_checkpoint"]=receipt
a["github_pending_checkpoint"]=c["github_pending_checkpoint"]="Checkpoint92: actual GEO/sequence partial PASS87, immutable all-point fiber review88, exact current/boundary addendum93, four new primary units and fixed GK source. Original solved count remains four."
for t in c["targets"]:
    if t["id"]=="P16.1":
        t["current_focus"]=batch["focus"]+" Full original remains open."
save(R / "active-work.json",a)
save(R / "checklist-current.json",c)
for name in ["active-work.json","checklist-current.json","checklist-current.tsv"]:
    shutil.copyfile(R / name,D / name)
files = []


def add(path,remote=None):
    p = Path(path)
    assert p.is_file() and not p.is_symlink()
    rel = p.relative_to(R)
    assert p.suffix not in {".sqlite",".jsonl"}
    assert not any(v in {".git",".codex",".aws",".env","auth.json","run.json"} for v in rel.parts)
    files.append({"local":str(p),"path":remote or "research-checkpoints/continuation92/"+str(rel),
                  "bytes":p.stat().st_size,"sha256":sha(p)})


for folder in [S,D]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for name in ["task.json","argument.md","settings.json","freeze.json"]:
    add(C / name)
for p in [
    V,F,R / "root-checks/P16.1-round87-binding-reading-clarifications-20261005.md",
    R / "root-checks/continuation93-live-curve-model-and-fiber-primary-observation.json",
    pdf,pdf.with_suffix(".txt"),R / "prepare_round88_fixed_reference_fiber_review_20261005.py",
    R / "round88-fixed-reference-fiber-review-preparation-20261005.json",
    G / "prepare_checkpoint_continuation92.py",G / "push-receipt-continuation91.json",
]:
    add(p)
for name in ["active-work.json","checklist-current.json","checklist-current.tsv"]:
    add(D / name,"manuscript/editorial/xean_research_20261003/"+name)
manifest = G / "upload-manifest-continuation92.json"
assert not manifest.exists()
save(manifest,{
    "generated_utc":now,"repository":receipt["repository"],"branch":receipt["branch"],
    "expected_previous_checkpoint":receipt["commit_sha"],"files":files,"file_count":len(files),
    "fully_solved_original_atoms":solved,"remaining_open_atoms":38,"historical_reviewed_scoped_papers":43,
    "commit_message":"Record geometric witness review and independently assess all-point fiber descent",
    "scope":"Actual precise GEO/sequence partial PASS87 with bindings, immutable native fiber review88 inputs, new unreviewed exact current/boundary addendum93, four pertinent literal primary units, fixed GK v3 PDF/text and actual live primary observations, fresh84/85/87/88 statuses. No original closure or new reviewed paper; no private SQL/transcripts/auth, runtime/account changes, messages, editor replacement or book edits.",
})
print(json.dumps({"manifest":str(manifest),"sha256":sha(manifest),"files":len(files),
                  "statuses":[(i["round"],i["observed_status"]) for i in items]},indent=2))
