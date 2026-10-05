"""Record publication of the fifth full original solution; retain history."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

R = Path("/workspace/research")
D = R / "deliverables/original-P13.2"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
v = json.loads((D / "P13.2-original-scope-review.json").read_text())
b = json.loads((D / "build/local-build.json").read_text())
p = json.loads((D / "publication-preparation.json").read_text())
assert v["verdict"] == "PASS" and b["success"] and b["pages"] == 13
assert b["source_sha256"] == p["publication_tex_sha256"] == sha(D / "P13.2-paper.tex")
assert b["pdf_sha256"] == sha(D / "P13.2-paper.pdf")
assert not (D / "original-closure.json").exists()
now = datetime.now(timezone.utc).isoformat()
record = {
    "atom": "P13.2", "fully_solved_original_atom": True,
    "original_statement_unchanged": True, "published_utc": now,
    "exact_scope": "Every original normal good polarized affine cone over every algebraically closed trivially valued characteristic-zero field of arbitrary cardinality, every dimension and every fixed rational or irrational Reeb xi. The genuine actual E1/R probability MA image on original K=X_0^T is exactly the Radon probabilities of finite H(xi) dual energy, equivalently integrable against every actual E1 potential. Actual solutions are attained and unique modulo constants; every normalized actual E1 maximizing sequence has I<=deficit/(2a_p), a_p=p/4^(p+1), p=n-1>=1. n=1 is the point case. Original normal rational quotients satisfy the established projective EP theorem, so no residual quotient-envelope or realization condition remains.",
    "source": str(D / "P13.2-paper.tex"), "source_sha256": sha(D / "P13.2-paper.tex"),
    "pdf": str(D / "P13.2-paper.pdf"), "pdf_sha256": sha(D / "P13.2-paper.pdf"),
    "pages": 13, "argument": str(D / "P13.2-argument.md"),
    "argument_sha256": sha(D / "P13.2-argument.md"),
    "reviewed_argument_sha256": sha(D / "P13.2-reviewed-argument.md"),
    "local_two_pass_compilation": "SUCCESS",
    "native_compilation": "Built-in compile cell815 pending; no native success asserted. Existing editor unchanged.",
    "first_and_last_pages_visually_read": True,
    "review": str(D / "P13.2-original-scope-review.json"),
    "review_sha256": sha(D / "P13.2-original-scope-review.json"),
    "verdict": v["verdict"], "reported_utc": v["reportedAt"], "operation_id": v["operationId"],
    "entire_report_premises_and_passages_root_read": True,
    "all_zero_based_exact_statement_bindings_verified": True,
    "premises": 22, "passages": 30, "external_http_passages": 27,
    "task_grant_passages": 3, "task_grant_entries_are_external_evidence": False,
    "publication_preparation": str(D / "publication-preparation.json"),
    "publication_preparation_sha256": sha(D / "publication-preparation.json"),
    "publication_changes": "Two expressly approved harmless wording/comma corrections, five quad spacing repairs, reviewed-edition metadata. Mathematical proof unchanged.",
    "precise_background": "Actual90 complete QEP-conditional packet with exact P13.1 and scoped73/79 inputs, actual91 countable EP, actual86 arbitrary-cardinality implication with E discharged by91. New quotient application independently audited in98; no dependency on pending full-original review99.",
    "review_limit": "Source-aware computational reconstruction by the requested native model, not formal proof certification or a literature-priority claim.",
}
(D / "original-closure.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
(D / "README.txt").write_text(
    "P13.2 — The image of the finite-energy Monge–Ampere operator on a polarized affine cone\n\n"
    "Read P13.2-paper.pdf (13 pages), or its TeX/Markdown source. The full original "
    "problem is solved in the unchanged original scope: fixed rational and irrational Reeb fields, "
    "the original invariant carrier and probability normalization, actual finite-energy solutions.\n\n"
    "P13.2-original-scope-review.json preserves the full source-aware native review98 PASS. "
    "P13.2-full-review-packet.md contains the entire supplied mathematical background and new proof. "
    "The canonical review, 22 external premises, 27 HTTP passages, three separate documentary "
    "task-grant passages, original problem, literal source extracts and publication-only patches "
    "are retained. Source paths in historical evidence refer to the preserved research archive.\n\n"
    "The exported PDF passed two local TeX compilations. The built-in compilation is pending "
    "and does not affect the preserved mathematical review; see build/local-build.json "
    "and any later native-compile observation. The user's existing P16.4 editor stays open.\n"
)
solved = ["P13.1", "P13.2", "P15.1", "P15.2", "P16.6"]
for name in ["active-work.json", "checklist-current.json"]:
    path = R / name
    d = json.loads(path.read_text())
    assert d["fully_solved_original_atoms"] == ["P13.1", "P15.1", "P15.2", "P16.6"]
    d["updated_utc"] = now
    d["fully_solved_original_atoms"] = solved
    d["original_P13_2_full_solution"] = record
    d["remaining_open_original_atoms"] = 37
    d["goal_state"] = "5/42 unchanged original problems solved;37 remain open;43 historical reviewed scoped papers. Continue the current small batch."
    d["github_pending_checkpoint"] = "Checkpoint103: publish full original P13.2 paper and exact review98 PASS; five original closures,37 open; ongoing99 and100."
    batch = d["current_small_batch"]
    for item in batch["items"]:
        if item["atom"] == "P13.2":
            item["observed_status"] = "completed"
            item["original_closed"] = True
            item["canonical_review"] = str(D / "P13.2-original-scope-review.json")
            item["verdict"] = "PASS"
    batch["active_items"] = [i for i in batch["items"] if i["observed_status"] == "running"]
    batch["focus"] = "Original P13.2 completed review98 and published. Full-original P16.1 self-contained review99 and P21.3 arbitrary-current research100 continue."
    if name == "active-work.json":
        assert not any(x["atom"] == "P13.2" for x in d["full_solutions"])
        d["full_solutions"].append(record)
    else:
        assert d["historical_reviewed_scoped_papers"] == 43
        for t in d["targets"]:
            if t["id"] == "P13.2":
                assert not t["fully_solved"]
                t["closure"] = "solved"
                t["fully_solved"] = True
                t["research_status"] = "original_scope_completed"
                t["original_solution_paper"] = record
                t["historical_gap_labels_superseded_by_original_scope_audit"] = True
                t["remaining_full_target"] = []
                t["current_focus"] = record["exact_scope"]
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
c = json.loads((R / "checklist-current.json").read_text())
assert len(c["targets"]) == 42 and sum(bool(t["fully_solved"]) for t in c["targets"]) == 5
rows = ["ID\tClosure\tResearch\tReviewed_papers\tTitle"]
for t in c["targets"]:
    values = [t["id"], t["closure"], t["research_status"], str(len(t.get("reviewed_papers", []))), t["title"]]
    rows.append("\t".join(str(s).replace("\t", " ").replace("\n", " ") for s in values))
(R / "checklist-current.tsv").write_text("\n".join(rows) + "\n")
print(json.dumps({"solved": solved, "remaining": 37, "closure": str(D / "original-closure.json"),
                  "closure_sha256": sha(D / "original-closure.json"), "scoped_papers": 43}, indent=2))
