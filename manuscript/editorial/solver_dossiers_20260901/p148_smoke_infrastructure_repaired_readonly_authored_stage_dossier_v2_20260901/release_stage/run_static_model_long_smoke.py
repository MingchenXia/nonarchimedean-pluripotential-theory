from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import signal
import stat
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from typing import Any, Callable, Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parent
RUNTIME_ROOT = ROOT / "runtime"
CATALOG_PATH = RUNTIME_ROOT / "model_catalog.gpt-5.6-sol.json"
CODEX = Path("/Applications/ChatGPT.app/Contents/Resources/codex")
MCP_PYTHON = Path(
    "/Users/mingchen/Projects/Yethlas/"
    "Rethlas_mixed_hessian_20260827/agents/verification/tmp/verification-venv/bin/python"
)
MCP_SCRIPT = ROOT / "static_model_smoke_mcp.py"
OUTPUT_ROOT = ROOT / "STATIC_MODEL_LONG_SMOKE"
WORKSPACE = OUTPUT_ROOT / "workspace"
STDOUT_LOG = OUTPUT_ROOT / "codex.stdout.jsonl"
STDERR_LOG = OUTPUT_ROOT / "codex.stderr.log"
PROCESS_SAMPLES = OUTPUT_ROOT / "process_samples.json"
RECEIPT = OUTPUT_ROOT / "receipt.json"
EXPECTED_CATALOG_BYTES = 41355
EXPECTED_CATALOG_SHA256 = (
    "75ecc0f5301dcc5474598335a12e82e9195eeb04f55197f2589109b34f3988fa"
)
MODEL = "gpt-5.6-sol"
REASONING_EFFORT = "xhigh"
WAIT_SECONDS = 310
STATE_WARNING_LIMIT = 200
SHELL_WARNING_LIMIT = 1
ROOT_OBSERVATIONS = {
    "live",
    "exited_before_scan",
    "exited_during_scan",
}
STATE_WARNING = re.compile(
    r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z)  WARN "
    r"codex_rollout::list: state db discrepancy during "
    r"find_thread_path_by_id_str_in_subdir: falling_back"
)
SHELL_WARNING = re.compile(
    r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z)  WARN "
    r"codex_core::shell_snapshot: Failed to delete shell snapshot at "
    r"AbsolutePathBuf\(\"/Users/mingchen/\.codex/shell_snapshots/"
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\."
    r"[0-9]{10,}\.sh\"\): Os \{ code: 2, kind: NotFound, "
    r"message: \"No such file or directory\" \}"
)
FORBIDDEN_DIAGNOSTIC_MARKERS = (
    "codex_models_manager::manager",
    "failed to refresh available models",
    "models_cache.json",
    "model cache",
    "debug models",
    "credential",
    "authentication",
    "unauthorized",
    "not logged in",
    "access token",
    "api key",
    "failed to connect",
    "websocket",
    "tls handshake",
    "transport error",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _fingerprint(root: Path) -> Dict[str, Dict[str, Any]]:
    result: Dict[str, Dict[str, Any]] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        info = path.lstat()
        if stat.S_ISLNK(info.st_mode):
            raise RuntimeError(f"symlink forbidden in fingerprint: {relative}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise RuntimeError(f"special file forbidden in fingerprint: {relative}")
        result[relative] = {
            "bytes": info.st_size,
            "sha256": _sha256_file(path),
            "mode": stat.S_IMODE(info.st_mode),
        }
    return result


def _reject_duplicate_pairs(pairs: List[Tuple[str, Any]]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _strict_lf_lines(value: bytes, label: str) -> List[str]:
    if value and not value.endswith(b"\n"):
        raise RuntimeError(f"{label} lacks terminal LF")
    try:
        text = value.decode("utf-8")
    except UnicodeDecodeError as error:
        raise RuntimeError(f"{label} is not strict UTF-8: {error}") from error
    if not text:
        return []
    lines = text.split("\n")[:-1]
    result: List[str] = []
    for line_number, line in enumerate(lines, 1):
        if line.endswith("\r"):
            line = line[:-1]
        if "\r" in line:
            raise RuntimeError(f"{label} line {line_number} contains an embedded CR")
        if not line.strip():
            raise RuntimeError(f"{label} line {line_number} is blank")
        result.append(line)
    return result


def _parse_stdout_records(value: bytes) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for line_number, line in enumerate(_strict_lf_lines(value, "Codex stdout"), 1):
        try:
            record = json.loads(
                line,
                object_pairs_hook=_reject_duplicate_pairs,
                parse_constant=lambda item: (_ for _ in ()).throw(
                    ValueError(f"nonfinite JSON value: {item}")
                ),
            )
        except (json.JSONDecodeError, ValueError) as error:
            raise RuntimeError(
                f"Codex stdout line {line_number} is not strict JSON: {error}"
            ) from error
        if not isinstance(record, dict):
            raise RuntimeError(f"Codex stdout line {line_number} is not an object")
        records.append(record)
    return records


def _parse_warning_utc(value: str, label: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as error:
        raise RuntimeError(f"{label} has an invalid UTC timestamp: {error}") from error
    if parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        raise RuntimeError(f"{label} timestamp is not UTC")
    return parsed


def _classify_stderr(
    value: bytes,
    smoke_started: Optional[datetime] = None,
    smoke_completed: Optional[datetime] = None,
) -> Dict[str, int]:
    if (smoke_started is None) != (smoke_completed is None):
        raise RuntimeError("stderr interval bounds must be supplied together")
    counts = {"state_db": 0, "shell_snapshot_cleanup": 0}
    previous_time: Optional[datetime] = None
    for line_number, line in enumerate(_strict_lf_lines(value, "Codex stderr"), 1):
        state = STATE_WARNING.fullmatch(line)
        shell = SHELL_WARNING.fullmatch(line)
        if state is not None:
            counts["state_db"] += 1
            timestamp_text = state.group(1)
        elif shell is not None:
            counts["shell_snapshot_cleanup"] += 1
            timestamp_text = shell.group(1)
        else:
            raise RuntimeError(
                f"Codex stderr line {line_number} is not an allowlisted warning"
            )
        timestamp = _parse_warning_utc(timestamp_text, f"Codex stderr line {line_number}")
        if smoke_started is not None and smoke_completed is not None:
            if not smoke_started <= timestamp <= smoke_completed:
                raise RuntimeError(
                    f"Codex stderr line {line_number} is outside the smoke interval"
                )
            if state is not None and timestamp > smoke_started + timedelta(seconds=5):
                raise RuntimeError(
                    f"Codex stderr state warning line {line_number} is outside startup"
                )
        if previous_time is not None and timestamp < previous_time:
            raise RuntimeError("Codex stderr warning timestamps regress")
        previous_time = timestamp
    if counts["state_db"] > STATE_WARNING_LIMIT:
        raise RuntimeError("too many state-database stderr warnings")
    if counts["shell_snapshot_cleanup"] > SHELL_WARNING_LIMIT:
        raise RuntimeError("too many shell-snapshot stderr warnings")
    return counts


def _descendants(root_pid: int) -> List[Dict[str, Any]]:
    result = subprocess.run(
        ["/bin/ps", "-axo", "pid=,ppid=,etime=,command="],
        capture_output=True,
        text=True,
        timeout=10,
        check=True,
    )
    rows: Dict[int, Dict[str, Any]] = {}
    for line in result.stdout.splitlines():
        parts = line.strip().split(None, 3)
        if len(parts) != 4:
            continue
        try:
            pid = int(parts[0])
            ppid = int(parts[1])
        except ValueError:
            continue
        rows[pid] = {
            "pid": pid,
            "ppid": ppid,
            "elapsed": parts[2],
            "command": parts[3],
        }
    selected = {root_pid}
    changed = True
    while changed:
        changed = False
        for pid, row in rows.items():
            if row["ppid"] in selected and pid not in selected:
                selected.add(pid)
                changed = True
    return [rows[pid] for pid in sorted(selected) if pid in rows]


def _observe_process(
    process: Any,
    scanner: Callable[[int], List[Dict[str, Any]]] = _descendants,
) -> Tuple[str, List[Dict[str, Any]]]:
    """Return a process-tree observation without confusing an exit race with drift."""
    if process.poll() is not None:
        return "exited_before_scan", []
    descendants = scanner(process.pid)
    if process.poll() is not None:
        return "exited_during_scan", descendants
    return "live", descendants


def _write_json(path: Path, value: Any) -> None:
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False, sort_keys=True)
        handle.write("\n")


def main() -> int:
    if OUTPUT_ROOT.exists():
        raise RuntimeError(f"immutable smoke output already exists: {OUTPUT_ROOT}")
    OUTPUT_ROOT.mkdir(exist_ok=False)
    WORKSPACE.mkdir(exist_ok=False)

    errors: List[str] = []
    catalog_bytes = CATALOG_PATH.read_bytes()
    if len(catalog_bytes) != EXPECTED_CATALOG_BYTES:
        errors.append("catalog byte length mismatch before launch")
    if _sha256_bytes(catalog_bytes) != EXPECTED_CATALOG_SHA256:
        errors.append("catalog digest mismatch before launch")
    catalog = json.loads(catalog_bytes)
    models = catalog.get("models") if isinstance(catalog, dict) else None
    if not isinstance(models, list) or len(models) != 1:
        errors.append("catalog does not contain exactly one model")
        parsed_model = None
        parsed_efforts: List[str] = []
    else:
        parsed_model = models[0].get("slug")
        levels = models[0].get("supported_reasoning_levels", [])
        parsed_efforts = [
            level.get("effort") for level in levels if isinstance(level, dict)
        ]
    if parsed_model != MODEL:
        errors.append("catalog model mismatch before launch")
    if REASONING_EFFORT not in parsed_efforts:
        errors.append("catalog lacks xhigh before launch")
    if errors:
        raise RuntimeError("; ".join(errors))

    runtime_before = _fingerprint(RUNTIME_ROOT)
    workspace_before = _fingerprint(WORKSPACE)
    prompt = (
        "This is an infrastructure TTL smoke test. Call the configured "
        "wait_across_catalog_ttl MCP tool exactly once with seconds=310. "
        "After the tool returns, respond exactly STATIC_MODEL_SMOKE_OK. "
        "Do not call any other tool and do not create or modify files."
    )
    command = [
        str(CODEX),
        "exec",
        "-C",
        str(WORKSPACE),
        "-m",
        MODEL,
        "--sandbox",
        "read-only",
        "--ignore-user-config",
        "--ignore-rules",
        "--strict-config",
        "--skip-git-repo-check",
        "--ephemeral",
        "--json",
        "--enable",
        "skip_host_skill_discovery",
        "--config",
        'approval_policy="never"',
        "--config",
        "suppress_unstable_features_warning=true",
        "--config",
        f'model_reasoning_effort="{REASONING_EFFORT}"',
        "--config",
        f'model_catalog_json="{CATALOG_PATH}"',
        "--config",
        f'mcp_servers.ttl_smoke.command="{MCP_PYTHON}"',
        "--config",
        f"mcp_servers.ttl_smoke.args={json.dumps(['-B', str(MCP_SCRIPT)], separators=(',', ':'))}",
        "--config",
        f'mcp_servers.ttl_smoke.cwd="{ROOT}"',
        "--config",
        "mcp_servers.ttl_smoke.required=true",
        "--config",
        "mcp_servers.ttl_smoke.startup_timeout_sec=120",
        "--config",
        "mcp_servers.ttl_smoke.tool_timeout_sec=420",
        "--config",
        'mcp_servers.ttl_smoke.default_tools_approval_mode="approve"',
        prompt,
    ]
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    started_at_utc = _utc_now()
    started = time.monotonic()
    samples: List[Dict[str, Any]] = []
    process: subprocess.Popen[str]
    with (
        STDOUT_LOG.open("x", encoding="utf-8") as stdout_handle,
        STDERR_LOG.open("x", encoding="utf-8") as stderr_handle,
    ):
        stdin_master_fd, stdin_slave_fd = os.openpty()
        if not os.isatty(stdin_slave_fd):
            os.close(stdin_master_fd)
            os.close(stdin_slave_fd)
            raise RuntimeError("dedicated Codex stdin is not a terminal")
        try:
            process = subprocess.Popen(
                command,
                cwd=WORKSPACE,
                env=environment,
                stdin=stdin_slave_fd,
                stdout=stdout_handle,
                stderr=stderr_handle,
                text=True,
                start_new_session=True,
            )
        finally:
            os.close(stdin_slave_fd)
        deadline = started + 900
        while time.monotonic() < deadline:
            try:
                root_observation, descendants = _observe_process(process)
                sampling_error = None
            except Exception as error:
                root_observation = "live"
                descendants = []
                sampling_error = repr(error)
                errors.append(f"process-tree sampling failed: {error!r}")
            sampled_at_utc = _utc_now()
            sample_elapsed = time.monotonic() - started
            samples.append(
                {
                    "sampled_at_utc": sampled_at_utc,
                    "elapsed_seconds": sample_elapsed,
                    "descendants": descendants,
                    "sampling_error": sampling_error,
                    "root_observation": root_observation,
                }
            )
            print(
                f"static-model smoke running: {sample_elapsed:.1f}s",
                flush=True,
            )
            if sampling_error is not None:
                if process.poll() is None:
                    os.killpg(process.pid, signal.SIGTERM)
                    process.wait(timeout=15)
                break
            if root_observation != "live":
                break
            time.sleep(15)
        if process.poll() is None:
            errors.append("Codex exceeded the 900-second smoke timeout")
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait(timeout=15)
        return_code = process.returncode
        os.close(stdin_master_fd)

    elapsed = time.monotonic() - started
    completed_at_utc = _utc_now()
    runtime_after = _fingerprint(RUNTIME_ROOT)
    workspace_after = _fingerprint(WORKSPACE)
    stdout_bytes = STDOUT_LOG.read_bytes()
    stderr_bytes = STDERR_LOG.read_bytes()
    try:
        stdout_records = _parse_stdout_records(stdout_bytes)
    except RuntimeError as error:
        stdout_records = []
        errors.append(str(error))
    try:
        stderr_warning_counts = _classify_stderr(
            stderr_bytes,
            datetime.fromisoformat(started_at_utc),
            datetime.fromisoformat(completed_at_utc),
        )
    except RuntimeError as error:
        stderr_warning_counts = {"state_db": 0, "shell_snapshot_cleanup": 0}
        errors.append(str(error))
    stdout_text = stdout_bytes.decode("utf-8", errors="replace")
    stderr_text = stderr_bytes.decode("utf-8", errors="replace")
    if return_code != 0:
        errors.append(f"Codex returned exit code {return_code}")
    if elapsed < 300:
        errors.append(f"smoke did not cross 300 seconds: {elapsed:.3f}")
    if "STATIC_MODEL_SMOKE_OK" not in stdout_text:
        errors.append("terminal smoke marker missing")
    folded_stdout = stdout_text.casefold()
    folded_stderr = stderr_text.casefold()
    for forbidden in FORBIDDEN_DIAGNOSTIC_MARKERS:
        if forbidden.casefold() in folded_stdout:
            errors.append(f"forbidden diagnostic in Codex stdout: {forbidden}")
        if forbidden.casefold() in folded_stderr:
            errors.append(f"forbidden diagnostic in Codex stderr: {forbidden}")
    if runtime_after != runtime_before:
        errors.append("runtime changed during smoke")
    if workspace_after != workspace_before:
        errors.append("model workspace changed during smoke")

    completed_wait_calls = 0
    for record in stdout_records:
        item = record.get("item") if isinstance(record, dict) else None
        if (
            isinstance(item, dict)
            and item.get("type") == "mcp_tool_call"
            and item.get("tool") == "wait_across_catalog_ttl"
            and item.get("status") == "completed"
        ):
            completed_wait_calls += 1
    if completed_wait_calls != 1:
        errors.append(
            f"expected one completed TTL MCP call, observed {completed_wait_calls}"
        )

    process_commands = [
        row["command"]
        for sample in samples
        for row in sample["descendants"]
        if row["pid"] != process.pid and isinstance(row.get("command"), str)
    ]
    for forbidden in FORBIDDEN_DIAGNOSTIC_MARKERS:
        if any(forbidden.casefold() in command_text.casefold() for command_text in process_commands):
            errors.append(f"forbidden subprocess diagnostic observed: {forbidden}")

    live_sample_count = sum(
        sample["root_observation"] == "live" for sample in samples
    )
    terminal_sample_count = sum(
        sample["root_observation"] in {"exited_before_scan", "exited_during_scan"}
        for sample in samples
    )
    if terminal_sample_count != 1 or samples[-1]["root_observation"] == "live":
        errors.append("successful smoke lacks exactly one terminal process observation")

    _write_json(PROCESS_SAMPLES, samples)
    receipt = {
        "format": "rethlas-static-model-long-smoke-v2",
        "status": "passed" if not errors else "failed",
        "errors": errors,
        "started_at_utc": started_at_utc,
        "completed_at_utc": completed_at_utc,
        "elapsed_seconds": elapsed,
        "wait_seconds": WAIT_SECONDS,
        "return_code": return_code,
        "completed_wait_calls": completed_wait_calls,
        "model_manager_strategy": "StaticModelsManager",
        "stdin_strategy": "dedicated-pty-no-input",
        "catalog": {
            "path": str(CATALOG_PATH),
            "bytes": len(catalog_bytes),
            "sha256": _sha256_bytes(catalog_bytes),
            "model": parsed_model,
            "supported_reasoning_efforts": parsed_efforts,
            "selected_reasoning_effort": REASONING_EFFORT,
        },
        "codex": {
            "path": str(CODEX),
            "sha256": _sha256_file(CODEX),
        },
        "mcp": {
            "python": str(MCP_PYTHON),
            "script": str(MCP_SCRIPT),
            "script_sha256": _sha256_file(MCP_SCRIPT),
        },
        "command_without_prompt": command[:-1],
        "prompt_sha256": _sha256_bytes(prompt.encode("utf-8")),
        "runtime_before": runtime_before,
        "runtime_after": runtime_after,
        "workspace_before": workspace_before,
        "workspace_after": workspace_after,
        "stdout_log_sha256": _sha256_file(STDOUT_LOG),
        "stderr_log_sha256": _sha256_file(STDERR_LOG),
        "stderr_warning_counts": stderr_warning_counts,
        "process_samples_sha256": _sha256_file(PROCESS_SAMPLES),
        "process_sample_count": len(samples),
        "live_process_sample_count": live_sample_count,
        "terminal_process_sample_count": terminal_sample_count,
        "root_pid": process.pid,
        "stdout_forbidden_diagnostic_count": sum(
            folded_stdout.count(value.casefold()) for value in FORBIDDEN_DIAGNOSTIC_MARKERS
        ),
        "stderr_forbidden_diagnostic_count": sum(
            folded_stderr.count(value.casefold()) for value in FORBIDDEN_DIAGNOSTIC_MARKERS
        ),
    }
    _write_json(RECEIPT, receipt)
    print(json.dumps({"receipt": str(RECEIPT), "status": receipt["status"]}))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
