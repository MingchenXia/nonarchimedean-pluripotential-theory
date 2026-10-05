"""Freeze new unreviewed reductions, literal primary units and canonical result83."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
G = R / "github-checkpoint"
D = G / "continuation89-publication-records"
S = R / "root-checks/continuation89-envelope-primary-read-units"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


assert not D.exists() and not S.exists()
proposals = [
    (R / "root-checks/P16.1-envelope-to-raw-equation-and-continuous-base-change-20261005-continuation89.md",
     "49f9dde261db15a4df3e8baca0fb0afa4ffab070e8f64a89bd2b531c716943a9"),
    (R / "root-checks/P16.1-local-reference-converse-and-countable-to-arbitrary-EP-20261005-continuation90.md",
     "6c30c2e4c8b93394864fb5b373b2565436b20e0cd140794337541513f7bccec7"),
]
for p, expected in proposals:
    assert sha(p) == expected
receipt = json.loads((G / "push-receipt-continuation88.json").read_text())
assert receipt["commit_sha"] == "1853839149d1defbd61f536c66bc240d8e63e85a"
assert receipt["remote_ref_verified"] and receipt["all_file_blob_bindings_verified_remote"]
assert sha(G / "upload-manifest-continuation88.json") == receipt["manifest_sha256"]
D.mkdir()
S.mkdir()
now = datetime.now(timezone.utc).isoformat()
units = []
for stem, filename, url, expected, ranges in [
    ("BJ-1801.08229v4", "P16-arxiv-1801.08229-20261004.txt",
     "https://arxiv.org/abs/1801.08229v4",
     "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
     [(1400, 1464), (1596, 1735), (2170, 2295), (2408, 2494),
      (2894, 2976), (3650, 3735), (3780, 3840), (3963, 4148),
      (4200, 4288), (4498, 4618), (4835, 5013), (5100, 5180),
      (5190, 5265), (5390, 5485), (6070, 6148), (6302, 6440)]),
    ("BE-1805.01016v3", "P16-arxiv-1805.01016-20261004.txt",
     "https://arxiv.org/abs/1805.01016v3",
     "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
     [(2340, 2422), (2629, 2808), (3118, 3190)]),
]:
    source = R / "shared-sources" / filename
    assert sha(source) == expected
    lines = source.read_bytes().decode("utf-8").split("\n")
    for first, last in ranges:
        literal = "\n".join(lines[first-1:last]).encode("utf-8")
        p = S / f"{stem}-LF{first}-{last}.txt"
        p.write_bytes(literal)
        assert p.read_bytes() == literal
        units.append({
            "source": str(source), "source_sha256": expected, "url": url,
            "inclusive_one_based_LF": [first, last], "literal_file": str(p),
            "literal_sha256": sha(p), "bytes": len(literal),
            "whole_applicable_statement_and_proof_unit_root_read": True,
            "all_recursively_cited_background_proofs_root_read": False,
        })
assert len(units) == 19
visual = []
for name, page in [
    ("BJ-Proposition9.19-PDFpage105.png", 105),
    ("BJ-Proposition7.21-PDFpage84.png", 84),
]:
    p = R / "root-checks/continuation89-primary-page-checks" / name
    visual.append({
        "image": str(p), "image_sha256": sha(p),
        "primary_pdf": str(R / "shared-sources/P16-arxiv-1801.08229-20261004.pdf"),
        "primary_pdf_sha256": sha(R / "shared-sources/P16-arxiv-1801.08229-20261004.pdf"),
        "one_based_pdf_page": page, "root_visually_read": True,
    })
save(S / "source-read-record.json", {
    "recorded_utc": now,
    "proposals": [{"path": str(p), "sha256": sha(p), "bytes": p.stat().st_size,
                   "whole_current_saved_proposal_root_read": True,
                   "accepted_dependency": False} for p, _ in proposals],
    "units": units, "visual_primary_page_checks": visual,
    "live_web_bodies_root_read": [
        {"url": "https://stacks.math.columbia.edu/tag/033G", "rendered_lines": [24, 31]},
        {"url": "https://stacks.math.columbia.edu/tag/0CEX", "rendered_lines": [22, 23]},
        {"url": "https://stacks.math.columbia.edu/tag/0BPZ", "rendered_lines": [23, 24]},
    ],
    "reading_limits": "Web coordinates are rendered tool lines, not cached LF/hash pins. The two selected PDF pages were visually read; no whole-PDF reading is claimed. Whole applicable primary proof units were read, not all recursive background proofs. New applications remain unreviewed.",
})
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
    item = {
        "atom": "P16.1", "round": round_no, "directory": str(C), "role": "codex",
        "tool_session_id": session, "observed_status": state["status"],
        "status": str(p), "status_sha256": sha(p), "original_closed": False,
        "input_sha256": freeze["input_sha256"], "input_bytes": freeze["input_bytes"],
        "settings_sha256": freeze["settings_sha256"], "hot_feedback_sent": False,
    }
    if round_no == 83:
        assert state["status"] == "completed" and state["calls"]["unsettled"] == 0
        result = json.loads((C / "run.json").read_text())["campaign"]["result"]
        assert result["kind"] == "notes" and result["candidate"] is False
        assert len(result["notes"]) == 4
        canonical = D / "P16.1-round83-canonical-native-result.json"
        save(canonical, result)
        for index, note in enumerate(result["notes"], 1):
            (D / f"P16.1-round83-note{index}.md").write_text(note["text"])
        item["canonical_result"] = str(canonical)
        item["canonical_result_sha256"] = sha(canonical)
        item["candidate"] = False
        item["independent_mathematical_review_pending"] = True
    items.append(item)
batch = {
    "recorded_utc": now, "items": items,
    "active_items": [i for i in items if i["observed_status"] == "running"],
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
    "original_closed": False,
    "focus": "Read and independently review completed countable Runge notes83; independent fiber-reference/finite-data continuation84 retains its frozen input. New envelope-to-equation and cardinality reductions are unreviewed.",
}
save(D / "current-small-batch-observation.json", batch)
a = json.loads((R / "active-work.json").read_text())
c = json.loads((R / "checklist-current.json").read_text())
solved = ["P13.1", "P15.1", "P15.2", "P16.6"]
assert sorted(t["id"] for t in c["targets"] if t["fully_solved"]) == solved
assert sum(len(t["reviewed_papers"]) for t in c["targets"]) == 43
a["updated_utc"] = c["updated_utc"] = now
a["current_small_batch"] = c["current_small_batch"] = batch
c["active_atoms"] = sorted(set(i["atom"] for i in batch["active_items"]))
a["continuation89_unreviewed_reductions"] = {
    "proposals": [{"path": str(p), "sha256": sha(p)} for p, _ in proposals],
    "source_read_record": str(S / "source-read-record.json"),
    "accepted_dependency": False, "original_closed": False,
}
a["github_checkpoint"] = c["latest_verified_github_checkpoint"] = receipt
a["github_pending_checkpoint"] = c["github_pending_checkpoint"] = "Checkpoint89: two unreviewed reductions, nineteen literal primary units, two visually checked primary pages, completed native83 canonical notes and fresh84 status. Original solved count remains four."
for t in c["targets"]:
    if t["id"] == "P16.1":
        t["current_focus"] = batch["focus"] + " Countable singular EP/global first membership and the full original equation remain open."
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
        "local": str(p), "path": remote or "research-checkpoints/continuation89/" + str(rel),
        "bytes": p.stat().st_size, "sha256": sha(p),
    })


for folder in [S, D]:
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            add(p)
for p, _ in proposals:
    add(p)
for check in visual:
    add(check["image"])
for p in [G / "prepare_checkpoint_continuation89.py", G / "push-receipt-continuation88.json"]:
    add(p)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation89.json"
assert not manifest.exists()
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"],
    "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 38,
    "historical_reviewed_scoped_papers": 43,
    "commit_message": "Preserve exact envelope reductions and completed native Runge notes",
    "scope": "Unreviewed original-operator/raw-normalization and continuous-base-change reconstruction, local actual-reference FS conversion and countable-to-arbitrary EP implication; nineteen exact primary units with explicit reading limits and two visually checked primary PDF pages. Canonical native83 completed notes explicitly retain candidate=false; independently frozen native84 receives no hot feedback. No original closure, private transcripts/SQL/auth, runtime or book edits.",
})
print(json.dumps({
    "manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
    "statuses": [(i["round"], i["observed_status"]) for i in items],
}, indent=2))
