"""Preserve the actual full-original PASS and prepare its publication edition."""
from datetime import datetime, timezone
from pathlib import Path
import difflib
import hashlib
import json
import shutil

R = Path("/workspace/research")
C = R / "campaigns/round-98/P13.2-original-all-Reeb-image-paper-full-review"
P = R / "root-checks/public-P13.2-round-94-final-reader"
D = R / "deliverables/original-P13.2"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
prep = json.loads((R / "round98-P13-original-full-review-preparation-20261005.json").read_text())
for name, key in [("task.json", "task_sha256"), ("task-original.json", "original_task_sha256"),
                  ("argument.md", "argument_sha256"), ("settings.json", "settings_sha256")]:
    assert sha(C / name) == prep[key]
assert sha(P / "argument.md") == "835acebbc542010d07b208b91513080b59f05886d3bc793eca0ca9ba5bbaaafd"
run = json.loads((C / "run.json").read_text())
v = run["campaign"]["result"]
assert v["verdict"] == "PASS"
assert v["operationId"] == "ec68b0d8-b1a2-4a67-8e81-e1b5a3d131d5"
assert len(v["premises"]) == 22 and len(v["passages"]) == 30
for i, p in enumerate(v["passages"]):
    assert p["id"] == v["operationId"] + "/" + str(i)
    assert isinstance(p["premise"], int) and 0 <= p["premise"] < 22
    assert p["statement"] == v["premises"][p["premise"]]
http = [p for p in v["passages"] if p["url"].startswith("https://")]
grants = [p for p in v["passages"] if p["url"] == "urn:xean:task"]
assert len(http) == 27 and len(grants) == 3
assert {p["premise"] for p in http} == set(range(22))
assert len(http) + len(grants) == 30
canonical = R / "root-checks/P13.2-round98-actual-full-original-review-20261005.json"
binding = R / "root-checks/P13.2-round98-canonical-reading-binding-20261005.json"
save(canonical, v)
save(binding, {
    "canonical_result": str(canonical), "sha256": sha(canonical),
    "verdict": v["verdict"], "operation_id": v["operationId"], "reported_at": v["reportedAt"],
    "whole_report_root_read": True, "all22_premises_root_read": True,
    "all30_passage_objects_root_read": True,
    "all_zero_based_exact_statement_bindings_verified": True,
    "external_http_passages": 27, "external_http_coverage": list(range(22)),
    "additional_task_grant_passages": grants,
    "task_urn_entries_are_external_primary_evidence": False,
    "whole_primary_source_papers_root_read": False,
    "original_task": str(C / "task-original.json"),
    "original_task_sha256": sha(C / "task-original.json"),
    "review_task": str(C / "task.json"), "review_task_sha256": sha(C / "task.json"),
    "reviewed_full_packet": str(C / "argument.md"), "reviewed_full_packet_sha256": sha(C / "argument.md"),
    "proof94": str(P / "argument.md"), "proof94_sha256": sha(P / "argument.md"),
    "full_original_scope_accepted": True,
    "precise_background": "Actual90 QEP-conditional body with its exact P13.1/scoped73/79 inputs; actual91 countable EP and actual86 conditional arbitrary-cardinality implication with E discharged by91. New94 and its original normal quotient application were independently audited, not granted. No dependency on pending full-original P16.1 review99.",
    "review_limit": "Source-aware computational reconstruction by the requested native model; no documentary build certification or formal proof certificate.",
})
D.mkdir()
for src, name in [
    (canonical, "P13.2-original-scope-review.json"),
    (binding, "P13.2-review-reading-binding.json"),
    (C / "task-original.json", "P13.2-original-task.json"),
    (C / "task.json", "P13.2-full-review-task.json"),
    (C / "argument.md", "P13.2-full-review-packet.md"),
    (P / "argument.md", "P13.2-reviewed-argument.md"),
    (P / "P13.2-paper.tex", "P13.2-reviewed-paper.tex"),
    (P / "external-premises.json", "author-primary-premises.json"),
    (P / "source-provenance.json", "author-source-provenance.json"),
    (P / "source-catalogue.json", "author-source-catalogue.json"),
    (P / "input-original.json", "author-original-input.json"),
    (R / "round98-P13-original-full-review-preparation-20261005.json", "full-review-input-preparation.json"),
]:
    shutil.copyfile(src, D / name)
shutil.copytree(P / "source-extracts", D / "source-extracts")
save(D / "review-primary-premises.json", {
    "premises": v["premises"], "external_passages": http, "task_grant_passages": grants,
    "canonical_review": "P13.2-original-scope-review.json",
    "external_http_covers_every_premise": True,
    "task_grant_entries_are_documentary": True,
})
edits = []
for name, src in [("P13.2-argument.md", P / "argument.md"), ("P13.2-paper.tex", P / "P13.2-paper.tex")]:
    old = src.read_text()
    text = old

    def replace(before, after, count=1):
        global text
        assert text.count(before) == count, (name, before, text.count(before))
        text = text.replace(before, after)
        edits.append({"file": name, "before": before, "after": after, "occurrences": count})

    replace("Standalone mathematical draft", "Research manuscript", 2 if name.endswith(".tex") else 1)
    replace(",quad", r",\quad", 4)
    replace(")quad", r")\quad")
    replace("C(K),,g", "C(K),g")
    if name.endswith(".md"):
        replace("documentary checks; this manuscript is an unverified mathematical draft.",
                "documentary checks. This reviewed edition retains the stated mathematical\nbackground; its review and build records accompany the paper.")
        replace("$-\\infty$. Its zero parameter is the raw root\n$\\mathcal R_{\\eta\\xi}u$.",
                "$-\\infty$. The zero parameter of a finite orbit is the raw root\n$\\mathcal R_{\\eta\\xi}u$; on an identically $-\\infty$ orbit, the root\nhas the singular value supplied by the decreasing-limit extension.")
    else:
        replace("compilation are documentary checks; this manuscript is an unverified\nmathematical draft.",
                "compilation are documentary checks. This reviewed edition retains the\nstated mathematical background; its review and build records accompany\nthe paper.")
        replace("identically \\(-\\infty\\). Its zero parameter is the raw root\n\\(\\mathcal R_{\\eta\\xi}u\\).",
                "identically \\(-\\infty\\). The zero parameter of a finite orbit is the\nraw root \\(\\mathcal R_{\\eta\\xi}u\\); on an identically \\(-\\infty\\)\norbit, the root has the singular value supplied by the decreasing-limit\nextension.")
    (D / name).write_text(text)
    patch = "".join(difflib.unified_diff(old.splitlines(True), text.splitlines(True),
                                      fromfile="reviewed/" + name, tofile="publication/" + name))
    (D / (name + ".publication-only.patch")).write_text(patch)
save(D / "publication-only-edits.json", {
    "mathematical_proof_changed": False,
    "review_report_corrections": ["duplicated comma in8.2", "finite-orbit zero versus singular root wording"],
    "additional_typesetting_repairs": "five missing quad backslashes in each presentation",
    "metadata_update": "reviewed edition, with no assigned human authorship",
    "edits": edits,
})
save(D / "publication-preparation.json", {
    "created_utc": datetime.now(timezone.utc).isoformat(), "atom": "P13.2",
    "state": "Full original scope reviewed PASS; publication source saved; compilation/export pending.",
    "canonical_review": str(canonical), "canonical_review_sha256": sha(canonical),
    "reading_binding": str(binding), "reading_binding_sha256": sha(binding),
    "reviewed_argument_sha256": sha(P / "argument.md"), "reviewed_tex_sha256": sha(P / "P13.2-paper.tex"),
    "publication_argument_sha256": sha(D / "P13.2-argument.md"),
    "publication_tex_sha256": sha(D / "P13.2-paper.tex"),
    "publication_edits": str(D / "publication-only-edits.json"),
    "publication_edits_sha256": sha(D / "publication-only-edits.json"),
    "native_editor": "Existing P16.4 editor remains open unchanged; no new tab or replacement.",
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
})
receipt = json.loads((R / "github-checkpoint/push-receipt-continuation102.json").read_text())
assert receipt["commit_sha"] == "05315e86580f79f29b957d83cdef4126a5faaf58"
assert sha(R / "github-checkpoint/upload-manifest-continuation102.json") == receipt["manifest_sha256"]
assert all(receipt[k] for k in ["remote_ref_verified", "all_file_blob_bindings_verified_remote",
                               "independent_native_git_tree_verified"])
for name in ["active-work.json", "checklist-current.json"]:
    p = R / name
    d = json.loads(p.read_text())
    d["github_checkpoint" if name == "active-work.json" else "latest_verified_github_checkpoint"] = receipt
    d["github_pending_checkpoint"] = None
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"publication": str(D), "canonical": str(canonical), "canonical_sha256": sha(canonical),
                  "premises": 22, "external_passages": 27, "task_passages": 3,
                  "source_tex_sha256": sha(D / "P13.2-paper.tex"), "build_pending": True}, indent=2))
