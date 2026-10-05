"""Publish the sixth original solution and freeze the next two-problem batch."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

R = Path("/workspace/research")
G = R / "github-checkpoint"
P = R / "deliverables/original-P16.1"
D = G / "continuation104-publication-records"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists() and not (P / "original-closure.json").exists()
receipt = json.loads((G / "push-receipt-continuation103.json").read_text())
assert receipt["commit_sha"] == "07c8d3ee3a53512ec8c974a6996b592ec7fa2c16"
assert sha(G / "upload-manifest-continuation103.json") == receipt["manifest_sha256"]
assert all(receipt[k] for k in ["remote_ref_verified", "all_file_blob_bindings_verified_remote",
                               "independent_native_git_tree_verified"])
v = json.loads((P / "P16.1-original-scope-review.json").read_text())
b = json.loads((P / "build/local-build.json").read_text())
p = json.loads((P / "publication-preparation.json").read_text())
assert v["verdict"] == "PASS" and b["success"] and b["pages"] == 17
assert b["source_sha256"] == p["publication_tex_sha256"] == sha(P / "P16.1-paper.tex")
assert b["pdf_sha256"] == sha(P / "P16.1-paper.pdf")
now = datetime.now(timezone.utc).isoformat()
closure = {
    "atom": "P16.1", "fully_solved_original_atom": True, "original_statement_unchanged": True,
    "published_utc": now,
    "exact_scope": "All dimensions, every algebraically closed trivially valued characteristic-zero field of arbitrary cardinality, every reduced irreducible geometrically unibranch projective variety including nonnormal varieties, and every actual ample rational line bundle. Original-target EP and normalized compactness, genuine actual E1 raw mixed products of original intersection mass, unbounded decreasing and integrable weighted limits, intrinsic finite-dual-energy/integrability characterization, comparison, actual variational existence and uniqueness modulo constants for arbitrary-support Radon targets of mass V=(L^n). Normalization transport is onto only after EP and preserves actual energy, raw cycles and measures. n=0 is proved directly. No claim for other P16 axes.",
    "source": str(P / "P16.1-paper.tex"), "source_sha256": sha(P / "P16.1-paper.tex"),
    "pdf": str(P / "P16.1-paper.pdf"), "pdf_sha256": sha(P / "P16.1-paper.pdf"),
    "pages": 17, "argument": str(P / "P16.1-argument.md"),
    "argument_sha256": sha(P / "P16.1-argument.md"),
    "reviewed_argument_sha256": sha(P / "P16.1-reviewed-argument.md"),
    "review": str(P / "P16.1-original-scope-review.json"),
    "review_sha256": sha(P / "P16.1-original-scope-review.json"),
    "verdict": "PASS", "operation_id": v["operationId"], "reported_utc": v["reportedAt"],
    "entire_report_premises_and_passages_root_read": True,
    "all_zero_based_exact_statement_bindings_verified": True,
    "premises": 10, "passages": 11, "all_external_http": True,
    "local_two_pass_compilation": "SUCCESS",
    "native_compilation": "Built-in compile cell831 pending; no native success asserted. Editor unchanged.",
    "first_and_last_pages_visually_read": True,
    "publication_preparation": str(P / "publication-preparation.json"),
    "publication_preparation_sha256": sha(P / "publication-preparation.json"),
    "publication_changes": "Reviewed-edition and author metadata only; entire mathematical proof and appendix unchanged.",
    "precise_background": "Exact original partial80/contact bridge,86 local conversion/arbitrary-field implication/general equation,87 geometry,88 all-point fiber/normalization,89 repaired original-reference affine chain, with all binding qualifications supplied. New membership and countability application independently reconstructed in99.",
    "review_limit": "Source-aware computational reconstruction by the requested native model, not formal proof certification or a priority claim.",
}
save(P / "original-closure.json", closure)
(P / "README.txt").write_text(
    "P16.1 — Finite-energy non-Archimedean equations on geometrically unibranch projective varieties\n\n"
    "P16.1-paper.pdf is the17-page full-original reviewed edition. Its actual ample-bundle "
    "domain includes nonnormal geometrically unibranch targets over arbitrary-cardinality "
    "algebraically closed trivially valued characteristic-zero fields, with arbitrary target "
    "support and the original raw mass. Other P16 axes remain distinct.\n\n"
    "P16.1-original-scope-review.json preserves the complete native99 PASS. "
    "P16.1-full-review-packet.md retains the exact supplied mathematical background, "
    "new proof and primary literal dictionary; all26 original contexts were supplied inline. "
    "The original task,10 external premises,11 exact HTTP passages, source extracts, "
    "supplied binding qualifications and publication-only patches accompany the paper.\n\n"
    "The PDF passed two local TeX compilations and first/last-page inspection. "
    "Built-in compilation is pending; see any later native-compile observation. "
    "The user's P16.4 editor stays open unchanged.\n"
)
D.mkdir()
items = []
for atom, no, stem, session in [
    ("P21.3", 100, "P21.3-original-mixed-symmetry-and-arbitrary-current-research", 85644),
    ("P16.5", 102, "P16.5-original-nonample-finite-energy-equation-research", 18947),
]:
    C = R / f"campaigns/round-{no}" / stem
    proc = subprocess.run(["bash", "scripts/cloud.sh", "xean", "--records", "status", str(C / "campaign.sqlite")],
                          cwd="/workspace/xean", capture_output=True, text=True, check=True)
    state = json.loads(proc.stdout)
    assert state["calls"]["admitted"] == 1
    q = D / f"{atom}-round{no}-native-status.json"
    q.write_text(proc.stdout)
    items.append({"atom": atom, "role": "codex", "round": no, "directory": str(C),
                  "tool_session_id": session, "observed_status": state["status"],
                  "status": str(q), "status_sha256": sha(q),
                  "hot_feedback_sent": False, "original_closed": False})
batch = {"recorded_utc": now, "items": items,
         "active_items": [i for i in items if i["observed_status"] == "running"],
         "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
         "focus": "P16.1 full original review99 completed and paper published. Current two-target batch: P21.3 arbitrary-current research100 and P16.5 actual nonample finite-energy equation research102;101 schema rejection preserved."}
save(D / "current-small-batch-observation.json", batch)
solved = ["P13.1", "P13.2", "P15.1", "P15.2", "P16.1", "P16.6"]
for name in ["active-work.json", "checklist-current.json"]:
    path = R / name
    d = json.loads(path.read_text())
    assert d["fully_solved_original_atoms"] == ["P13.1", "P13.2", "P15.1", "P15.2", "P16.6"]
    d["updated_utc"] = now
    d["fully_solved_original_atoms"] = solved
    d["original_P16_1_full_solution"] = closure
    d["remaining_open_original_atoms"] = 36
    d["goal_state"] = "6/42 unchanged original problems solved;36 remain open;43 historical reviewed scoped papers. Continue the current two-target batch."
    d["current_small_batch"] = batch
    d["github_checkpoint" if name == "active-work.json" else "latest_verified_github_checkpoint"] = receipt
    d["github_pending_checkpoint"] = "Checkpoint104: full original P16.1 paper and actual99 PASS, six original closures,36 open; original P16.5 research102 and preserved101 schema rejection."
    if name == "active-work.json":
        assert not any(t["atom"] == "P16.1" for t in d["full_solutions"])
        d["full_solutions"].append(closure)
    else:
        assert d["historical_reviewed_scoped_papers"] == 43
        for t in d["targets"]:
            if t["id"] == "P16.1":
                assert not t["fully_solved"]
                t["closure"] = "solved"; t["fully_solved"] = True
                t["research_status"] = "original_scope_completed"
                t["original_solution_paper"] = closure
                t["historical_gap_labels_superseded_by_original_scope_audit"] = True
                t["remaining_full_target"] = []
                t["current_focus"] = closure["exact_scope"]
            if t["id"] == "P16.5":
                t["current_focus"] = "Full nonample axis remains open;102 first actual big/pseudoeffective equation attempt under explicit retained hypotheses;101 pre-admission schema rejection preserved."
                t["current_native_research"] = next(i for i in items if i["atom"] == "P16.5")
                t["research_status"] = "original_nonample_equation_research_running"
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    shutil.copyfile(path, D / name)
c = json.loads((R / "checklist-current.json").read_text())
assert len(c["targets"]) == 42 and sum(bool(t["fully_solved"]) for t in c["targets"]) == 6
rows = ["ID\tClosure\tResearch\tReviewed_papers\tTitle"]
for t in c["targets"]:
    values = [t["id"], t["closure"], t["research_status"], str(len(t.get("reviewed_papers", []))), t["title"]]
    rows.append("\t".join(str(x).replace("\t", " ").replace("\n", " ") for x in values))
(R / "checklist-current.tsv").write_text("\n".join(rows) + "\n")
shutil.copyfile(R / "checklist-current.tsv", D / "checklist-current.tsv")
save(D / "six-original-closures.json", [
    json.loads((R / f"deliverables/original-{a}/original-closure.json").read_text()) for a in solved
])
files = []


def add(path, remote=None):
    p = Path(path); assert p.is_file() and not p.is_symlink()
    rel = p.relative_to(R)
    assert p.suffix not in {".sqlite", ".jsonl"}
    assert not any(x in {".git", ".codex", ".aws", ".env", "auth.json", "run.json"} for x in rel.parts)
    files.append({"local": str(p), "path": remote or "research-checkpoints/continuation104/" + str(rel),
                  "bytes": p.stat().st_size, "sha256": sha(p)})


for folder in [D, P]:
    for q in sorted(folder.rglob("*")):
        if q.is_file(): add(q)
for q in [
    R / "root-checks/P16.1-round99-actual-full-original-review-20261005.json",
    R / "root-checks/P16.1-round99-canonical-reading-binding-20261005.json",
    R / "publish_original_P16_1_review99_20261005.py",
    R / "prepare_round101_P16_nonample_equation_research_20261005.py",
    R / "round101-P16-nonample-equation-research-preparation-20261005.json",
    R / "prepare_round102_P16_nonample_schema_recovery_20261005.py",
    R / "round102-P16-nonample-schema-recovery-preparation-20261005.json",
    G / "publish_P16_1_and_prepare_checkpoint_continuation104.py", G / "push-receipt-continuation103.json",
]:
    add(q)
for no in [101, 102]:
    C = R / f"campaigns/round-{no}/P16.5-original-nonample-finite-energy-equation-research"
    names = ["task-original.json", "input.json", "assignment-original.txt", "settings.json", "freeze.json"]
    names += ["pre-admission-schema-rejection.json"] if no == 101 else ["previous101-schema-rejection.json"]
    for name in names: add(C / name)
for name in ["active-work.json", "checklist-current.json", "checklist-current.tsv"]:
    add(D / name, "manuscript/editorial/xean_research_20261003/" + name)
manifest = G / "upload-manifest-continuation104.json"
save(manifest, {
    "generated_utc": now, "repository": receipt["repository"], "branch": receipt["branch"],
    "expected_previous_checkpoint": receipt["commit_sha"], "files": files, "file_count": len(files),
    "fully_solved_original_atoms": solved, "remaining_open_atoms": 36,
    "historical_reviewed_scoped_papers": 43,
    "commit_message": "Publish full singular unibranch finite-energy equation theorem and advance nonample research",
    "scope": "Full original P16.1 reviewed17-page edition and actual99 PASS with all exact original grants, primary units and unchanged proof. Six original problems solved;36 open. P16.5 fresh102 research admits unchanged mathematics after101 pre-admission schema correction. Current two-target batch100/102. No other axis, new scoped acceptance, private state/auth, runtime mutation or editor replacement claimed.",
})
print(json.dumps({"manifest": str(manifest), "sha256": sha(manifest), "files": len(files),
                  "solved": solved, "remaining": 36,
                  "statuses": [(i["atom"], i["round"], i["observed_status"]) for i in items]}, indent=2))
