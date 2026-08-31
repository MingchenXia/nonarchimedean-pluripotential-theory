"""Capture the configured local verifier's non-secret runtime provenance."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

DEST = Path(__file__).resolve().parent
ROOT = Path("/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification")
LAUNCHER = Path("/Users/mingchen/Projects/Yethlas/popovici_audit_20260827/main_theorem_rechecks/P027/rethlas_local_service.py")
OUT = DEST / "RUNTIME_CAPTURE.json"
if OUT.exists():
    raise RuntimeError("Refusing to overwrite a runtime capture")
responses = {}
for endpoint in ("health", "audit-runtime", "openapi.json"):
    with urlopen("http://127.0.0.1:8107/" + endpoint, timeout=20) as response:
        raw = response.read()
        responses[endpoint] = {
            "status": response.status,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "body": json.loads(raw),
        }
runtime = responses["audit-runtime"]["body"]
assert runtime["model"] == "gpt-5.6-sol"
assert runtime["reasoning_effort"] == "xhigh"
assert runtime["sandbox"] == "workspace-write"
assert runtime["verifier_root"] == str(ROOT)
paths = [LAUNCHER, ROOT / "api/server.py", ROOT / "AGENTS.md"]
pins = []
for file in paths:
    raw = file.read_bytes()
    pins.append({"path": str(file), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})
record = {
    "captured_at_utc": datetime.now(timezone.utc).isoformat(),
    "responses": responses,
    "source_pins": pins,
    "protocol": "Sequential Markdown verification, three-key report; not strict v0.2.",
    "boundary": "Runtime/source provenance only; no proof was submitted by this capture.",
}
with OUT.open("x", encoding="utf-8") as handle:
    json.dump(record, handle, indent=2, sort_keys=True)
    handle.write("\n")
print(json.dumps({"runtime_capture": str(OUT), "model": runtime["model"], "effort": runtime["reasoning_effort"], "sandbox": runtime["sandbox"], "source_pins": len(pins)}))
