"""Preserve the full-original review99 and prepare its unchanged proof edition."""
from datetime import datetime, timezone
from pathlib import Path
import difflib
import hashlib
import json
import shutil

R = Path("/workspace/research")
C = R / "campaigns/round-99/P16.1-original-self-contained-full-review"
P = R / "root-checks/public-P16.1-round-92-final-reader"
D = R / "deliverables/original-P16.1"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, v):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(v, ensure_ascii=False, indent=2) + "\n")


assert not D.exists()
prep = json.loads((R / "round99-P16-self-contained-full-review-preparation-20261005.json").read_text())
for name, key in [("task.json", "task_sha256"), ("task-original.json", "original_task_sha256"),
                  ("argument.md", "argument_sha256"), ("settings.json", "settings_sha256")]:
    assert sha(C / name) == prep[key]
assert sha(P / "argument.md") == "6cd26d798b63a388bd9a5e6dcd0583a7cd9c7417648efe390f4d4d00d28646b9"
v = json.loads((C / "run.json").read_text())["campaign"]["result"]
assert v["verdict"] == "PASS"
assert v["operationId"] == "dc2dd0f9-7938-4e83-b050-18b619a51906"
assert len(v["premises"]) == 10 and len(v["passages"]) == 11
for i, p in enumerate(v["passages"]):
    assert p["id"] == v["operationId"] + "/" + str(i)
    assert 0 <= p["premise"] < 10 and p["statement"] == v["premises"][p["premise"]]
    assert p["url"].startswith("https://")
assert {p["premise"] for p in v["passages"]} == set(range(10))
canonical = R / "root-checks/P16.1-round99-actual-full-original-review-20261005.json"
binding = R / "root-checks/P16.1-round99-canonical-reading-binding-20261005.json"
save(canonical, v)
save(binding, {
    "canonical_result": str(canonical), "sha256": sha(canonical), "verdict": "PASS",
    "operation_id": v["operationId"], "reported_at": v["reportedAt"],
    "whole_report_root_read": True, "all10_premises_root_read": True,
    "all11_passage_objects_root_read": True,
    "all_zero_based_exact_statement_bindings_verified": True,
    "all_premises_have_external_http_passages": True,
    "whole_primary_source_papers_root_read": False,
    "original_task": str(C / "task-original.json"), "original_task_sha256": sha(C / "task-original.json"),
    "review_task": str(C / "task.json"), "review_task_sha256": sha(C / "task.json"),
    "reviewed_full_packet": str(C / "argument.md"), "reviewed_full_packet_sha256": sha(C / "argument.md"),
    "proof92": str(P / "argument.md"), "proof92_sha256": sha(P / "argument.md"),
    "all26_original_contexts_and_primary_bodies_supplied_inline": True,
    "full_original_scope_accepted": True,
    "precise_background": "Exactly the original supplied mathematical bodies and binding clarifications: contact bridge and partial80, local conversion/arbitrary-field implication/general equation86, geometry87, all-point fiber and normalization88, repaired original-reference affine chain89. The new first-membership/countability application was independently audited, not granted.",
    "review_limit": "Source-aware native computational mathematical reconstruction, not documentary build or formal proof certification.",
})
D.mkdir()
for src, name in [
    (canonical, "P16.1-original-scope-review.json"), (binding, "P16.1-review-reading-binding.json"),
    (C / "task-original.json", "P16.1-original-task.json"), (C / "task.json", "P16.1-full-review-task.json"),
    (C / "argument.md", "P16.1-full-review-packet.md"),
    (P / "argument.md", "P16.1-reviewed-argument.md"),
    (P / "P16.1-paper.tex", "P16.1-reviewed-paper.tex"),
    (P / "external-premises.json", "author-primary-premises.json"),
    (P / "source-provenance.json", "author-source-provenance.json"),
    (P / "source-catalogue.json", "author-source-catalogue.json"),
    (P / "supplied-bindings.json", "author-supplied-bindings.json"),
    (P / "input-original.json", "author-original-input.json"),
    (R / "round99-P16-self-contained-full-review-preparation-20261005.json", "full-review-input-preparation.json"),
]:
    shutil.copyfile(src, D / name)
for name in ["original-grant-primary-catalogue-factored.json", "paper92-external-premises-factored.json",
             "primary-literal-body-dictionary.json"]:
    shutil.copyfile(C / name, D / name)
shutil.copytree(P / "source-extracts", D / "source-extracts")
shutil.copytree(P / "granted", D / "granted")
save(D / "review-primary-premises.json", {"premises": v["premises"], "passages": v["passages"],
                                        "canonical_review": "P16.1-original-scope-review.json"})
edits = []
for name, src in [("P16.1-argument.md", P / "argument.md"), ("P16.1-paper.tex", P / "P16.1-paper.tex")]:
    old = src.read_text()
    text = old

    def replace(before, after):
        global text
        assert text.count(before) == 1, (name, before, text.count(before))
        text = text.replace(before, after)
        edits.append({"file": name, "before": before, "after": after})

    if name.endswith(".md"):
        replace('author: "Research draft reconstructed from the specified primary sources and task-granted lemmas"',
                'author: "Research manuscript"')
        replace("This is an unverified research draft.", "This is the reviewed edition of the research manuscript.")
        replace("The mathematical conclusion is a proof draft, not a certification by compilation, hashes or prior historical verdicts.",
                "The complete original statement and new applications received the separate source-aware review99; the canonical review accompanies this edition. Compilation, hashes and historical verdicts have no mathematical force.")
    else:
        replace("pdfauthor={Research draft reconstructed from the specified primary sources and task-granted lemmas}",
                "pdfauthor={Research manuscript}")
        replace("\\author{Research draft reconstructed from the specified primary sources\nand task-granted lemmas}",
                "\\author{Research manuscript}")
        replace("This is an unverified research draft.", "This is the reviewed edition of the research manuscript.")
        replace("The mathematical conclusion is a proof draft, not a certification by\ncompilation, hashes or prior historical verdicts.",
                "The complete original statement and new applications received the separate\nsource-aware review99; the canonical review accompanies this edition.\nCompilation, hashes and historical verdicts have no mathematical force.")
    (D / name).write_text(text)
    (D / (name + ".publication-only.patch")).write_text("".join(
        difflib.unified_diff(old.splitlines(True), text.splitlines(True),
                             fromfile="reviewed/" + name, tofile="publication/" + name)))
save(D / "publication-only-edits.json", {"mathematical_proof_changed": False, "edits": edits})
save(D / "publication-preparation.json", {
    "created_utc": datetime.now(timezone.utc).isoformat(), "atom": "P16.1",
    "state": "Full original scope independently reviewed PASS; publication source saved; compilation/export pending.",
    "canonical_review": str(canonical), "canonical_review_sha256": sha(canonical),
    "reviewed_argument_sha256": sha(P / "argument.md"), "reviewed_tex_sha256": sha(P / "P16.1-paper.tex"),
    "publication_argument_sha256": sha(D / "P16.1-argument.md"),
    "publication_tex_sha256": sha(D / "P16.1-paper.tex"),
    "publication_edits_sha256": sha(D / "publication-only-edits.json"),
    "native_editor": "Existing P16.4 editor stays open unchanged; no new tab or replacement.",
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
})
print(json.dumps({"publication": str(D), "canonical": str(canonical), "canonical_sha256": sha(canonical),
                  "premises": 10, "passages": 11, "source_tex_sha256": sha(D / "P16.1-paper.tex"),
                  "build_pending": True}, indent=2))
