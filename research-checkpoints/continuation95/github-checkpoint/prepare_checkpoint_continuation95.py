"""Freeze the conditional P13.2 normal-quotient interface and review90."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation95-publication-records"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    Path(p).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
receipt = json.loads((G / "push-receipt-continuation94.json").read_text())
assert receipt["commit_sha"] == "ba71dcdbed98d6889a57cf2175469c5ea7f14ddc"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation94.json") == receipt["manifest_sha256"]
D.mkdir()
now = datetime.now(timezone.utc).isoformat()
items = []
for atom, no, stem, session in [
    ("P16.1",88,"P16.1-fixed-actual-reference-all-point-fiber-partial-review",60650),
    ("P16.1",89,"P16.1-Rossi-neighborhood-repaired-countable-global-review",54337),
    ("P13.2",90,"P13.2-normal-quotient-QEP-conditional-realization-partial-review",77740),
]:
    C = R / f"campaigns/round-{no}" / stem
    proc = subprocess.run(["bash","scripts/cloud.sh","xean","--records","status",str(C / "review.sqlite")],
                          cwd="/workspace/xean",capture_output=True,text=True,check=True)
    state = json.loads(proc.stdout)
    assert state["calls"]["admitted"] == 1
    p = D / f"{atom}-round{no}-native-status.json"
    p.write_text(proc.stdout)
    items.append({"atom":atom,"round":no,"directory":str(C),"role":"review",
                  "tool_session_id":session,"observed_status":state["status"],
                  "status":str(p),"status_sha256":sha(p),"hot_feedback_sent":False,
                  "completed_result_granted":False,"original_closed":False})
F = R / "root-checks/P13.2-normal-quotient-EP-to-all-Reeb-realization-interface-20261005-continuation97.md"
S = R / "root-checks/continuation97-normal-quotient-primary-read-units"
reading = json.loads((S / "source-read-record.json").read_text())
assert sha(F) == reading["proposal_sha256"]
assert reading["whole_current_proposal_root_read"] and not reading["QEP_proved"]
batch = {"recorded_utc":now,"items":items,
         "active_items":[i for i in items if i["observed_status"]=="running"],
         "route":"Xean native Codex","model":"gpt-6.1-sol","reasoning":"xhigh",
         "original_closed":False,
         "focus":"Three exact partial reviews on two original problems: P16.1 all-point fiber/reference88 and repaired countable global89; P13.2 actual normal-quotient QEP-conditional all-Reeb realization90. QEP and pending P16.1 C/F are not granted."}
save(D / "current-small-batch-observation.json",batch)
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1","P15.1","P15.2","P16.6"]
assert sorted(a["fully_solved_original_atoms"]) == sorted(c["fully_solved_original_atoms"]) == sorted(solved)
assert c["historical_reviewed_scoped_papers"] == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
proposal = {"path":str(F),"sha256":sha(F),"whole_current_body_root_read":True,
            "source_read_record":str(S / "source-read-record.json"),"review_round":90,
            "QEP_proved":False,"new_mathematics_accepted":False,"original_closed":False}
a["continuation97_normal_quotient_conditional_interface"] = proposal
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint95: exact QEP-conditional normal-quotient to all-Reeb interface97, five pertinent primary units, fresh independent review90 and statuses88/89/90. No original closure or new accepted paper."
for t in c["targets"]:
    if t["id"] == "P13.2":
        t["continuation97_normal_quotient_conditional_interface"] = proposal
        t["current_focus"] = "Review90 assesses actual all-Reeb realization assuming EP at one actual normal rational quotient. This QEP premise remains unproved; original higher-dimensional normal-cone realization remains open."
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
    files.append({"local":str(p),"path":remote or "research-checkpoints/continuation95/"+str(rel),
                  "bytes":p.stat().st_size,"sha256":sha(p)})


for folder in [S,D]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for p in [F,R / "prepare_round90_normal_quotient_conditional_interface_review_20261005.py",
          R / "round90-normal-quotient-conditional-interface-review-preparation-20261005.json",
          G / "prepare_checkpoint_continuation95.py",G / "push-receipt-continuation94.json"]:
    add(p)
C = R / "campaigns/round-90/P13.2-normal-quotient-QEP-conditional-realization-partial-review"
for name in ["task.json","settings.json","argument.md","freeze.json"]:
    add(C / name)
for name in ["active-work.json","checklist-current.json","checklist-current.tsv"]:
    add(D / name,"manuscript/editorial/xean_research_20261003/"+name)
manifest = G / "upload-manifest-continuation95.json"
assert not manifest.exists()
save(manifest,{
    "generated_utc":now,"repository":receipt["repository"],"branch":receipt["branch"],
    "expected_previous_checkpoint":receipt["commit_sha"],"files":files,"file_count":len(files),
    "fully_solved_original_atoms":solved,"remaining_open_atoms":38,"historical_reviewed_scoped_papers":43,
    "commit_message":"Preserve conditional normal-quotient all-Reeb interface and independent review",
    "scope":"Unreviewed root97 conditional P13.2 interface with explicit missing QEP premise, five exact pertinent BJ units, full frozen review90 inputs and preparation, fresh88/89/90 statuses and receipt94. No original closure or new accepted paper; no private SQL/transcripts/auth, runtime/account changes, external messages, editor replacement or book edits.",
})
print(json.dumps({"manifest":str(manifest),"sha256":sha(manifest),"files":len(files),
                  "statuses":[(i["atom"],i["round"],i["observed_status"]) for i in items]},indent=2))
