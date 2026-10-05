"""Preserve round82's zero-admission config failure; relaunch unchanged mathematics."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
OLD = R / "campaigns/round-82/P16.1-original-witness-trace-and-countable-Runge"
NEW = R / "campaigns/round-83/P16.1-original-witness-trace-and-countable-Runge"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()


def save(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


assert not NEW.exists()
assert sha(OLD / "input.json") == "60f88dcda881afafd9786f30f2333ec817b79349df1d75bb7f300f11e552491f"
assert sha(OLD / "settings.json") == "23cdd81750b29e539b1b0301429d0d82003cab0356bcc2346408ee2d51f60c29"
proc = subprocess.run(
    ["bash", "scripts/cloud.sh", "xean", "--records", "status", str(OLD / "campaign.sqlite")],
    cwd="/workspace/xean", capture_output=True, text=True, check=True,
)
status = json.loads(proc.stdout)
assert status["status"] == "blocked" and status["error"] == "Codex worker is not configured"
assert status["calls"]["admitted"] == 0
assert json.loads((OLD / "run.json").read_text())["campaign"]["result"] is None
failure = {
    "recorded_utc": datetime.now(timezone.utc).isoformat(), "failed_round": 82,
    "status": status, "actual_native_result": None,
    "input_sha256": sha(OLD / "input.json"), "settings_sha256": sha(OLD / "settings.json"),
    "cause": "Preparation reused review settings, which lack the native writer codex config object.",
    "repair": "A new round83 uses byte-identical mathematical input with the previously successful round77 native codex model/command configuration and a fresh own artifact workspace. Old input, config and failed campaign remain unchanged.",
    "authentication_or_runtime_change": False,
}
save(R / "round82-zero-admission-config-failure-20261005.json", failure)
NEW.mkdir(parents=True)
for name in ["input.json", "assignment-original.txt", "task-original.json"]:
    shutil.copyfile(OLD / name, NEW / name)
settings = json.loads((R / "campaigns/round-77/P16.1-public-source-compact-IBP-and-smooth-weak-global-equation/settings.json").read_text())
settings["usagePrefix"] = "catalogue-20261003/r83/P16.1-trace-Runge-reconstruction"
settings["codex"]["workspace"] = str(NEW / "artifacts")
assert settings["codex"]["command"] == "/workspace/xean/scripts/cloud-codex.sh"
assert settings["codex"]["model"] == "gpt-6.1-sol" and settings["codex"]["reasoning"] == "xhigh"
assert len(settings["usagePrefix"]) <= 91
save(NEW / "settings.json", settings)
record = json.loads((OLD / "freeze.json").read_text())
record.update({
    "prepared_utc": datetime.now(timezone.utc).isoformat(), "round": 83,
    "directory": str(NEW), "input_sha256": sha(NEW / "input.json"),
    "settings_sha256": sha(NEW / "settings.json"),
    "prior_failed_round": 82, "prior_failure_record": str(R / "round82-zero-admission-config-failure-20261005.json"),
    "prior_failure_sha256": sha(R / "round82-zero-admission-config-failure-20261005.json"),
    "mathematical_input_byte_identical_to_failed_round82": True,
    "submission_attempted": False,
})
save(NEW / "freeze.json", record)
save(R / "round83-trace-Runge-preparation-20261005.json", record)
print(json.dumps({"directory": str(NEW), "input_sha256": sha(NEW / "input.json"), "settings_sha256": sha(NEW / "settings.json"), "native_codex_config": settings["codex"], "prior_calls_admitted": 0}, indent=2))
