"""Freeze the conditional first-membership interface and smooth current proof."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation93-publication-records"
S = R / "root-checks/continuation94-95-interface-primary-read-units"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, v):
    Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2) + "\n")


assert not D.exists() and not S.exists()
receipt = json.loads((G / "push-receipt-continuation92.json").read_text())
assert receipt["commit_sha"]=="5c800d601024c7c306ff7d49d2c434d8e808f69a"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation92.json")==receipt["manifest_sha256"]
F94 = R / "root-checks/P16.1-countable-first-membership-join-interface-20261005-continuation94.md"
F95 = R / "root-checks/P16.1-smooth-fixed-bundle-current-proof-20261005-continuation95.md"
old = json.loads((R / "root-checks/continuation89-envelope-primary-read-units/source-read-record.json").read_text())
bj = [u for u in old["units"] if "1801.08229" in str(u["source"])]
assert bj and len({u["source_sha256"] for u in bj})==1
D.mkdir()
S.mkdir()
now = datetime.now(timezone.utc).isoformat()
units = []
for label,source,expected,url,ranges in [
    ("BJ-1801.08229v4",R / "shared-sources/P16-arxiv-1801.08229-20261004.txt",
     bj[0]["source_sha256"],"https://arxiv.org/pdf/1801.08229v4",[(882,920),(1174,1242),(2330,2380)]),
    ("BE-1805.01016v3",R / "shared-sources/P16-arxiv-1805.01016-20261004.txt",
     "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
     "https://arxiv.org/pdf/1805.01016v3",[(2605,2767)]),
]:
    assert sha(source)==expected
    lines = source.read_bytes().decode().split("\n")
    for first,last in ranges:
        p = S / f"{label}-LF{first}-{last}.txt"
        p.write_bytes("\n".join(lines[first-1:last]).encode())
        units.append({"source":str(source),"source_sha256":sha(source),"url":url,
                      "inclusive_one_based_LF":[first,last],"literal_file":str(p),"literal_sha256":sha(p),
                      "whole_pertinent_unit_root_read":True,"whole_source_file_root_read":False,
                      "all_recursive_primary_proofs_root_read":False})
save(S / "source-read-record.json",{
    "recorded_utc":now,
    "proposals":[{"path":str(p),"sha256":sha(p),"whole_current_proposal_root_read":True,
                  "accepted_dependency":False,"original_closed":False} for p in [F94,F95]],
    "units":units,
    "author83_interface_reread_inclusive_LF":[[1,31],[297,315],[365,378]],
    "scope":"Only pertinent source bodies read. The first-membership join retains pending F and C; the direct smooth-current proof is new unreviewed mathematics, not feedback to pending88.",
})
pdf = R / "shared-sources/Baker-Payne-Rabinoff-1404.0279v1-20261005.pdf"
txt = pdf.with_suffix(".txt")
assert sha(pdf)=="5e40117270a0051d9661c9bbd0317968b810573796a5c2408582f20692568a11"
assert sha(txt)=="b48912660955537923070fa3448ed9c9b01780d98e69d661bee1aa4dcbf8cc43"
save(D / "unused-BPR-source-acquisition-reading-limits.json",{
    "recorded_utc":now,"url":"https://arxiv.org/pdf/1404.0279v1",
    "pdf":str(pdf),"pdf_sha256":sha(pdf),"text":str(txt),"text_sha256":sha(txt),
    "live_abstract_edition_verified":True,"whole_theorem_proof_bodies_root_read":False,
    "metadata_and_search_only":True,"mathematical_premise_of_new_proposals":False,
    "discovery_observation":str(R / "root-checks/continuation95-curve-skeleton-primary-observation.json"),
    "unrelated_guessed_Springer_DOI_is_not_evidence":True,
})
items = []
for no,stem,database,session in [
    (84,"P16.1-fiber-reference-and-finite-data-descent","campaign.sqlite",20275),
    (85,"P16.1-whole-base-trace-and-countable-Runge-partial-review","review.sqlite",52293),
    (88,"P16.1-fixed-actual-reference-all-point-fiber-partial-review","review.sqlite",60650),
]:
    C = R / f"campaigns/round-{no}" / stem
    proc = subprocess.run(["bash","scripts/cloud.sh","xean","--records","status",str(C / database)],
                          cwd="/workspace/xean",capture_output=True,text=True,check=True)
    state = json.loads(proc.stdout)
    p = D / f"P16.1-round{no}-native-status.json"
    p.write_text(proc.stdout)
    assert state["calls"]["admitted"]==1
    items.append({"atom":"P16.1","round":no,"directory":str(C),
                  "role":"codex" if no==84 else "review","tool_session_id":session,
                  "observed_status":state["status"],"status":str(p),"status_sha256":sha(p),
                  "completed_result_granted":False,"hot_feedback_sent":False,"original_closed":False})
batch = {"recorded_utc":now,"items":items,
         "active_items":[i for i in items if i["observed_status"]=="running"],
         "route":"Xean native Codex","model":"gpt-6.1-sol","reasoning":"xhigh","original_closed":False,
         "focus":"Native84 independent author and exact partial reviews85/88 retain frozen inputs. Conditional reductions86 and GEO87 are accepted. Fresh first-membership interface94 and direct smooth fixed-bundle current proof95 remain unreviewed and do not grant pending C or F."}
save(D / "current-small-batch-observation.json",batch)
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1","P15.1","P15.2","P16.6"]
assert sorted(a["fully_solved_original_atoms"])==sorted(c["fully_solved_original_atoms"])==sorted(solved)
assert c["historical_reviewed_scoped_papers"]==43
a["updated_utc"]=c["updated_utc"]=now
a["current_small_batch"]=c["current_small_batch"]=batch
a["continuation94_95_unreviewed_join_and_current_proof"]={
    "proposals":[{"path":str(p),"sha256":sha(p),"whole_saved_proposal_root_read":True} for p in [F94,F95]],
    "source_read_record":str(S / "source-read-record.json"),
    "accepted_dependency":False,"original_closed":False,"pending_C_and_F_not_granted":True,
}
a["github_checkpoint"]=c["latest_verified_github_checkpoint"]=receipt
a["github_pending_checkpoint"]=c["github_pending_checkpoint"]="Checkpoint93: exact conditional first-membership interface94 and direct same-actual-bundle smooth-current proof95, four literal primary units and fresh84/85/88 statuses. No original closure."
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
    files.append({"local":str(p),"path":remote or "research-checkpoints/continuation93/"+str(rel),
                  "bytes":p.stat().st_size,"sha256":sha(p)})


for folder in [S,D]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for p in [F94,F95,R / "root-checks/continuation95-curve-skeleton-primary-observation.json",
          G / "prepare_checkpoint_continuation93.py",G / "push-receipt-continuation92.json"]:
    add(p)
for name in ["active-work.json","checklist-current.json","checklist-current.tsv"]:
    add(D / name,"manuscript/editorial/xean_research_20261003/"+name)
manifest = G / "upload-manifest-continuation93.json"
assert not manifest.exists()
save(manifest,{
    "generated_utc":now,"repository":receipt["repository"],"branch":receipt["branch"],
    "expected_previous_checkpoint":receipt["commit_sha"],"files":files,"file_count":len(files),
    "fully_solved_original_atoms":solved,"remaining_open_atoms":38,"historical_reviewed_scoped_papers":43,
    "commit_message":"Preserve exact first-membership interface and smooth fixed-bundle current proof",
    "scope":"New unreviewed conditional join94 and smooth same-actual-bundle current proof95, four exact pertinent primary units, honest unused source acquisition limits, fresh84/85/88 statuses and receipt92. Pending F and C are not granted, and no original or new paper is accepted. No private SQL/transcripts/auth, runtime/account changes, external messages, editor replacement or book edits.",
})
print(json.dumps({"manifest":str(manifest),"sha256":sha(manifest),"files":len(files),
                  "statuses":[(i["round"],i["observed_status"]) for i in items]},indent=2))
