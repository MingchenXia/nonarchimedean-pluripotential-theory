"""Preserve101's pre-admission schema rejection and freeze an equivalent102."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

R = Path("/workspace/research")
A = R / "campaigns/round-101/P16.5-original-nonample-finite-energy-equation-research"
C = R / "campaigns/round-102/P16.5-original-nonample-finite-energy-equation-research"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not C.exists()
old = json.loads((A / "input.json").read_text())
freeze = json.loads((A / "freeze.json").read_text())
assert sha(A / "input.json") == freeze["input_sha256"]
assert sha(A / "task-original.json") == freeze["task_sha256"]
assert sha(A / "assignment-original.txt") == freeze["assignment_sha256"]
assert sha(A / "settings.json") == freeze["settings_sha256"]
assert (A / "run.json").stat().st_size == 0
assert not (A / "campaign.sqlite").exists()
assert isinstance(old["task"]["completionCriteria"], list)
failure = {
    "observed_utc": datetime.now(timezone.utc).isoformat(), "round": 101,
    "native_command_exit_code": 1, "failure_stage": "input schema validation before campaign admission",
    "actual_relevant_diagnostic": "/task/completionCriteria: must be string",
    "empty_run_json": True, "campaign_database_created": False,
    "mathematical_result": None, "original_closed": False,
    "recovery": "Fresh102 joins the exact unchanged completion sentences into a string; no mathematical change.",
    "original_input_sha256": sha(A / "input.json"),
}
save(A / "pre-admission-schema-rejection.json", failure)
task = dict(old["task"])
task["completionCriteria"] = "\n\n".join(old["task"]["completionCriteria"])
assert task["problem"] == old["task"]["problem"]
assert task["completionCriteria"].split("\n\n") == old["task"]["completionCriteria"]
value = {"task": task, "notes": old["notes"], "assignment": old["assignment"]}
assert value["assignment"] == (A / "assignment-original.txt").read_text()
C.mkdir(parents=True)
(C / "artifacts").mkdir()
save(C / "task-original.json", task)
save(C / "input.json", value)
(C / "assignment-original.txt").write_bytes((A / "assignment-original.txt").read_bytes())
settings = json.loads((A / "settings.json").read_text())
settings["usagePrefix"] = "catalogue-20261003/r102/P16.5-original-nonample-equation"
settings["codex"]["workspace"] = str(C / "artifacts")
save(C / "settings.json", settings)
save(C / "previous101-schema-rejection.json", failure)
v = {
    "prepared_utc": datetime.now(timezone.utc).isoformat(), "round": 102, "atom": "P16.5",
    "directory": str(C), "previous_round": 101,
    "previous_failure": str(A / "pre-admission-schema-rejection.json"),
    "task_sha256": sha(C / "task-original.json"), "input_sha256": sha(C / "input.json"),
    "input_bytes": (C / "input.json").stat().st_size,
    "input_characters": len((C / "input.json").read_text()),
    "assignment_sha256": sha(C / "assignment-original.txt"),
    "settings_sha256": sha(C / "settings.json"), "embedded_context": freeze["embedded_context"],
    "mathematical_task_or_assignment_changed": False, "nonample_theory_granted": False,
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
    "submission_attempted": False, "original_closed": False,
}
save(C / "freeze.json", v)
save(R / "round102-P16-nonample-schema-recovery-preparation-20261005.json", v)
print(json.dumps({k: x for k, x in v.items() if k != "embedded_context"}, indent=2))
