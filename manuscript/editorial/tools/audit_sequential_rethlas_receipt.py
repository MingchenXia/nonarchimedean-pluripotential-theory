"""Read-only binding of a sequential Rethlas receipt to exact submitted bytes.

This checks provenance and the actual three-key protocol. It is not the strict
v0.2 attestation checker, a mathematical proof, or an independent source audit.
"""
import argparse
import hashlib
import json
import shlex
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
for name in ("statement", "proof", "request", "response", "headers", "log", "result", "runtime"):
    parser.add_argument(name, type=Path)
args = parser.parse_args()
sha = lambda b: hashlib.sha256(b).hexdigest()
statement = args.statement.read_text(encoding="utf-8")
proof = args.proof.read_text(encoding="utf-8")
request = json.loads(args.request.read_bytes())
response = json.loads(args.response.read_bytes())
headers = json.loads(args.headers.read_bytes())
result = json.loads(args.result.read_bytes())
runtime = json.loads(args.runtime.read_bytes())
assert request["statement"] == statement and request["proof"] == proof
assert headers["status_code"] == 200
assert response == result
assert set(response) == {"verification_report", "verdict", "repair_hints"}
report = response["verification_report"]
assert set(report) == {"summary", "critical_errors", "gaps"}
assert isinstance(report["summary"], str)
assert isinstance(report["critical_errors"], list) and isinstance(report["gaps"], list)
assert response["verdict"] in ("correct", "wrong")
assert isinstance(response["repair_hints"], str)
correct = not report["critical_errors"] and not report["gaps"]
assert (response["verdict"] == "correct") == correct
assert (response["repair_hints"] == "") == correct
for issues in (report["critical_errors"], report["gaps"]):
    for issue in issues:
        assert isinstance(issue, dict) and set(issue) == {"location", "issue"}
        assert all(isinstance(v, str) for v in issue.values())

config = runtime["responses"]["audit-runtime"]["body"]
assert config["model"] == "gpt-5.6-sol"
assert config["reasoning_effort"] == "xhigh"
assert config["sandbox"] == "workspace-write"
for pin in runtime["source_pins"]:
    raw = Path(pin["path"]).read_bytes()
    assert len(raw) == pin["bytes"] and sha(raw) == pin["sha256"]

assert args.log.name == "log.md"
assert args.result.name in ("verification.json", "verificationt.json")
assert args.log.parent.resolve() == args.result.parent.resolve()
run_id = args.log.parent.name
assert sha(statement.encode())[:12] in run_id
log = args.log.read_text(encoding="utf-8")
assert log.startswith("started_at_utc: ")
command = log.split("\ncommand: ", 1)[1]
lexer = shlex.shlex(command, posix=True)
lexer.whitespace_split = True
lexer.commenters = ""
tokens = [lexer.get_token() for _ in range(19)]
expected = [
    "/Applications/ChatGPT.app/Contents/Resources/codex", "exec",
    "-C", config["verifier_root"], "-m", "gpt-5.6-sol",
    "--sandbox", "workspace-write",
    "--config", 'approval_policy="never"',
    "--config", 'model_reasoning_effort="xhigh"',
    "--config", "sandbox_workspace_write.network_access=false",
    "--config", 'mcp_servers.verification_agent.command="' + config["mcp_python"] + '"',
    "--config", 'mcp_servers.verification_agent.cwd="' + config["verifier_root"] + '"',
    "Run_id: " + run_id + ". Statement: " + statement + ". Proof:\n" + proof
    + "\n\nUse AGENTS.md to verify the above proof for the statement.",
]
assert tokens == expected
assert "--dangerously-bypass-approvals-and-sandbox" not in tokens
paths = [getattr(args, name) for name in
         ("statement", "proof", "request", "response", "headers", "log", "result", "runtime")]
print(json.dumps({
    "audit": "PASS",
    "scope": "Exact-input, actual launcher and three-key sequential receipt binding only",
    "run_id": run_id,
    "verdict": response["verdict"],
    "critical_errors": len(report["critical_errors"]),
    "gaps": len(report["gaps"]),
    "independent_mathematical_and_reference_review_still_required": True,
    "strict_v02_attestation": False,
    "files": {str(p): {"bytes": p.stat().st_size, "sha256": sha(p.read_bytes())} for p in paths},
}, indent=2, sort_keys=True))
