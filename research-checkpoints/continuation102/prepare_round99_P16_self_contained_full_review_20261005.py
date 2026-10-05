"""Preserve inconclusive97 and freeze a losslessly self-contained original review99."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
P = R / "root-checks/public-P16.1-round-92-final-reader"
C97 = R / "campaigns/round-97/P16.1-original-full-review-length-recovery"
C = R / "campaigns/round-99/P16.1-original-self-contained-full-review"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(path, value):
    path = Path(path)
    assert not path.exists()
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not C.exists()
run = json.loads((C97 / "run.json").read_text())["campaign"]
result = run["result"]
assert run["status"] == "completed" and result["verdict"] == "INCONCLUSIVE"
assert result["operationId"] == "0b3f117a-6911-4d15-848e-efba95f6ba5f"
assert (len(result["premises"]), len(result["passages"])) == (7, 224)
cover = set()
for i, b in enumerate(result["passages"]):
    n = b["premise"]
    assert 0 <= n < 7 and b["statement"] == result["premises"][n]
    assert b["id"] == result["operationId"] + "/" + str(i)
    assert b["url"].startswith("https://") and b["quote"]
    cover.add(n)
assert cover == set(range(7))
actual = R / "root-checks/P16.1-round97-actual-inconclusive-full-review-20261005.json"
save(actual, result)
reading = R / "root-checks/P16.1-round97-canonical-reading-binding-20261005.json"
save(reading, {
    "canonical_result": str(actual), "sha256": sha(actual),
    "operation_id": result["operationId"], "reported_at": result["reportedAt"],
    "whole_report_root_read": True, "all7_standalone_premises_root_read": True,
    "all224_passage_URLs_and_quotes_root_read": True,
    "all224_statement_index_and_id_bindings_verified": True,
    "all_primary_sources_whole_read": False, "original_closed": False,
    "mathematical_defect_demonstrated": False,
    "governing_verdict": "INCONCLUSIVE: complete supplied-scope audit not achieved because review could not access six filesystem references.",
})
bindings = json.loads((P / "supplied-bindings.json").read_text())
assert len(bindings) == 26
for b in bindings:
    assert sha(P / b["file"]) == b["preserved_sha256"]
old_catalogue = json.loads((P / bindings[25]["file"]).read_text())
ext = json.loads((P / "external-premises.json").read_text())
bodies = {}


def factor(unit):
    item = dict(unit)
    literal = item.pop("literal")
    key = item["sha256"]
    assert hashlib.sha256(literal.encode()).hexdigest() == key
    if key in bodies:
        assert bodies[key] == literal
    bodies[key] = literal
    item["literal_from_dictionary_sha256"] = key
    return item


compact_catalogue = {
    "sources": old_catalogue["sources"],
    "units": [factor(u) for u in old_catalogue["units"]],
}
compact_ext = {
    "coordinate_rule": ext["coordinate_rule"], "limits": ext["limits"],
    "premises": [{**b, "passages": [factor(q) for q in b["passages"]]} for b in ext["premises"]],
}
for old, compact in zip(old_catalogue["units"], compact_catalogue["units"]):
    recovered = dict(compact)
    recovered["literal"] = bodies[recovered.pop("literal_from_dictionary_sha256")]
    assert recovered == old
for old, compact in zip(ext["premises"], compact_ext["premises"]):
    for q, c in zip(old["passages"], compact["passages"]):
        recovered = dict(c)
        recovered["literal"] = bodies[recovered.pop("literal_from_dictionary_sha256")]
        assert recovered == q
assert len(compact_catalogue["units"]) == 43
assert len(compact_ext["premises"]) == 17
C.mkdir(parents=True)
save(C / "original-grant-primary-catalogue-factored.json", compact_catalogue)
save(C / "paper92-external-premises-factored.json", compact_ext)
save(C / "primary-literal-body-dictionary.json", bodies)
task = json.loads((C97 / "task.json").read_text())
task["completionCriteria"] += """

SELF-CONTAINED ACCESS REPAIR: the preceding full review97 was INCONCLUSIVE
because its review session had no filesystem-reading capability. Its exact
unchanged canonical report is preserved. This fresh review retains ALL original
full-original criteria and accepted-body scopes. Every mathematical grant body,
all26 original context entries and every pertinent primary literal required
from those entries are supplied INLINE here. No indispensable evidence requires
reading a local filesystem path. Paths and preserved-copy hashes are documentary.

To remain within the native input length limit, repeated IDENTICAL literal text
is factored into an INLINE SHA256-keyed dictionary. An entry with
literal_from_dictionary_sha256 means substitute the exact literal string at that
key. The original43 grant-source units and every passage in all17 new-paper
premises reconstruct exactly, with all other values unchanged; their full
statements, hypotheses and pertinent proof bodies are retained. This is only a
lossless representation of duplicated primary evidence, not a new grant or
truncated proof. All first25 original supplied mathematical/primary entries are
inline in their original text. The26th is the losslessly factored primary
catalogue. Audit the complete body-scope match directly in these supplied data.

The previous verdict is not a mathematical premise or proof. Do not grant the
new whole paper, infer success from historical labels, or alter the original
scope. If an actual indispensable mathematical gap remains, identify its exact
statement and issue FAIL or INCONCLUSIVE as appropriate. Read public primary
sources as available; no shell/filesystem tool is necessary for any supplied
grant scope in this input. Do not inspect active original review98 or research
artifacts of other workers. Use the exact authorized Xean native Codex
gpt-6.1-sol/xhigh review route, with no additional model/worker.
"""
save(C / "task.json", task)
(C / "task-original.json").write_bytes((C97 / "task-original.json").read_bytes())
context = []
parts = ["# Self-contained FULL ORIGINAL P16.1 review evidence\n\nThe complete new proof remains independently unverified. All necessary mathematical scope bodies are supplied inline.\n"]


def embed(label, path):
    path = Path(path)
    context.append({"label": label, "path": str(path), "bytes": path.stat().st_size, "sha256": sha(path), "inline": True})
    parts.append("\n\nBEGIN MATHEMATICAL DATA: " + label + "\n" + path.read_text() + "\nEND MATHEMATICAL DATA\n")


embed("COMPLETE unchanged17-page original proof92", P / "argument.md")
embed("Exact unchanged original task", C / "task-original.json")
embed("Complete original supplied body bindings", P / "supplied-bindings.json")
for b in bindings[:25]:
    embed("Original context " + str(b["index"]) + ": " + b["title"], P / b["file"])
embed("Original context25 primary catalogue: losslessly factored literal strings", C / "original-grant-primary-catalogue-factored.json")
embed("All17 new proof92 external premises: losslessly factored passage literals", C / "paper92-external-premises-factored.json")
embed("COMPLETE exact literal body dictionary for both catalogues", C / "primary-literal-body-dictionary.json")
parts.append("\n\nPREVIOUS FULL REVIEW97 REPORT, diagnostic only; not a mathematical premise:\n" + result["report"] + "\n")
(C / "argument.md").write_text("\n".join(parts))
argument_chars = len((C / "argument.md").read_text())
task_chars = len((C / "task.json").read_text())
assert argument_chars + task_chars < 1000000
settings = json.loads((C97 / "settings.json").read_text())
settings["usagePrefix"] = "catalogue-20261003/r99/P16.1-self-contained-full-review"
save(C / "settings.json", settings)
freeze = {
    "prepared_utc": datetime.now(timezone.utc).isoformat(), "round": 99, "atom": "P16.1",
    "directory": str(C), "canonical97": str(actual), "reading97": str(reading),
    "task_sha256": sha(C / "task.json"), "original_task_sha256": sha(C / "task-original.json"),
    "argument_sha256": sha(C / "argument.md"), "argument_bytes": (C / "argument.md").stat().st_size,
    "argument_characters": argument_chars, "task_characters": task_chars,
    "settings_sha256": sha(C / "settings.json"), "embedded_context": context,
    "all26_original_contexts_supplied_inline": True,
    "primary_literal_dictionary_entries": len(bodies),
    "original_catalogue_and_new_premise_values_reconstruct_exactly": True,
    "prior97_or_new_paper_granted": False, "original_closed": False,
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
    "submission_attempted": False, "full_original_review": True, "hot_feedback_to98": False,
}
save(C / "freeze.json", freeze)
save(R / "round99-P16-self-contained-full-review-preparation-20261005.json", freeze)
print(json.dumps({k: v for k, v in freeze.items() if k != "embedded_context"}, indent=2))
