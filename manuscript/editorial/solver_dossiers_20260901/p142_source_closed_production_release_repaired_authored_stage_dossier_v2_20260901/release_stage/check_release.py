from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from pathlib import Path
import re
import shlex
import stat
import sys
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parent
CATALOG_RELATIVE = "runtime/model_catalog.gpt-5.6-sol.json"
CATALOG_BYTES = 41355
CATALOG_SHA256 = "75ecc0f5301dcc5474598335a12e82e9195eeb04f55197f2589109b34f3988fa"
MODEL = "gpt-5.6-sol"
EFFORT = "xhigh"
PINSET_SHA256 = "0412636c6dee5af057f0093075d85de96809719eb55c185b9409c5b71996decf"
PINS_FILE_SHA256 = "5a858706ab908f5da6d6e0fc883b095202562c87bd2fb48ab8f8608e2ca714f6"
CODEX_PATH = "/Applications/ChatGPT.app/Contents/Resources/codex"
CODEX_SHA256 = "a6042937174f72112dbd2d554a4af36936422e0c5ac69e353dc68994458996e9"
MCP_PYTHON_PATH = (
    "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/"
    "agents/verification/tmp/verification-venv/bin/python"
)
MCP_PYTHON_SHA256 = "4d4c42c0ebf9bf42e9aa2c0e56843632347a1f1c22d4a9f680b4f87fb241d0e6"
MCP_PYTHON_RESOLVED_PATH = (
    "/opt/homebrew/Cellar/python@3.14/3.14.6/Frameworks/Python.framework/"
    "Versions/3.14/bin/python3.14"
)
MCP_MACOS_LAUNCHER_PATH = (
    "/opt/homebrew/Cellar/python@3.14/3.14.6/Frameworks/Python.framework/"
    "Versions/3.14/Resources/Python.app/Contents/MacOS/Python"
)
MCP_MACOS_LAUNCHER_SHA256 = "0c4a1621b3b8c1dccaaa8f79da0cc2ad27c2d00fe99dcdf71dc820e32734a8b3"
SMOKE_WAIT_SECONDS = 310
SMOKE_CACHE_HORIZON_SECONDS = 300
SMOKE_INITIAL_SAMPLE_MAX_SECONDS = 30.0
SMOKE_SAMPLE_MIN_GAP_SECONDS = 14.0
SMOKE_SAMPLE_MAX_GAP_SECONDS = 30.0
SMOKE_FINAL_SAMPLE_MAX_AGE_SECONDS = 30.0
SMOKE_CLOCK_SKEW_SECONDS = 5.0
SMOKE_PROCESS_ELAPSED_SKEW_SECONDS = 3.0
SMOKE_MAX_RUN_SECONDS = 920.0
SMOKE_MCP_MAX_OVERRUN_SECONDS = 5.0
# The pinned sampler sleeps for 15 seconds after each bounded process scan;
# the cadence limits below include scan/scheduling slack and drive count bounds.
SMOKE_PROMPT = (
    "This is an infrastructure TTL smoke test. Call the configured "
    "wait_across_catalog_ttl MCP tool exactly once with seconds=310. "
    "After the tool returns, respond exactly STATIC_MODEL_SMOKE_OK. "
    "Do not call any other tool and do not create or modify files."
)
SAMPLE_KEYS = {
    "sampled_at_utc",
    "elapsed_seconds",
    "descendants",
    "sampling_error",
    "root_observation",
}
PROCESS_ROW_KEYS = {"pid", "ppid", "elapsed", "command"}
ROOT_OBSERVATIONS = {"live", "exited_before_scan", "exited_during_scan"}
STATE_WARNING_LIMIT = 200
SHELL_WARNING_LIMIT = 1
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
MCP_RESULT_KEYS = {
    "status",
    "requested_seconds",
    "elapsed_seconds",
    "started_at_utc",
    "completed_at_utc",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reject_duplicates(pairs: List[Tuple[str, Any]]) -> Dict[str, Any]:
    value: Dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def strict_json(path: Path) -> Any:
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicates,
        parse_constant=lambda value: (_ for _ in ()).throw(
            ValueError(f"nonfinite JSON value: {value}")
        ),
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def exact_int(value: Any) -> bool:
    return type(value) is int


def finite_number(value: Any) -> bool:
    return type(value) in (int, float) and math.isfinite(value)


def parse_utc(value: Any, label: str) -> datetime:
    require(isinstance(value, str), f"{label} is not a timestamp string")
    try:
        normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
        parsed = datetime.fromisoformat(normalized)
    except ValueError as error:
        raise RuntimeError(f"{label} is not ISO-8601: {error}") from error
    require(parsed.utcoffset() == timedelta(0), f"{label} is not UTC")
    return parsed


def strict_json_text(value: str) -> Any:
    return json.loads(
        value,
        object_pairs_hook=reject_duplicates,
        parse_constant=lambda item: (_ for _ in ()).throw(
            ValueError(f"nonfinite JSON value: {item}")
        ),
    )


def strict_lf_lines(value: str, label: str) -> List[str]:
    require(not value or value.endswith("\n"), f"{label} lacks terminal LF")
    if not value:
        return []
    lines = value.split("\n")[:-1]
    result: List[str] = []
    for line_number, line in enumerate(lines, 1):
        if line.endswith("\r"):
            line = line[:-1]
        require("\r" not in line, f"{label} line {line_number} contains an embedded CR")
        require(bool(line.strip()), f"{label} line {line_number} is blank")
        result.append(line)
    return result


def process_elapsed_seconds(value: Any) -> int:
    require(isinstance(value, str), "process elapsed value is not a string")
    match = re.fullmatch(r"(?:(\d+)-)?(?:(\d{2}):)?(\d{2}):(\d{2})", value)
    require(match is not None, f"malformed process elapsed value: {value!r}")
    days_text, hours_text, minutes_text, seconds_text = match.groups()
    days = int(days_text or 0)
    hours = int(hours_text or 0)
    minutes = int(minutes_text)
    seconds = int(seconds_text)
    require(minutes < 60 and seconds < 60, f"invalid process elapsed value: {value!r}")
    if days_text is not None:
        require(hours < 24, f"invalid process elapsed value: {value!r}")
    return (((days * 24) + hours) * 60 + minutes) * 60 + seconds


def require_clean_smoke_workspace(workspace: Path, receipt: Dict[str, Any]) -> None:
    info = workspace.lstat()
    require(stat.S_ISDIR(info.st_mode), "smoke workspace is not a real directory")
    require(not stat.S_ISLNK(info.st_mode), "smoke workspace is a symlink")
    entries = list(workspace.iterdir())
    require(not entries, "smoke workspace is not currently empty")
    require(
        receipt.get("workspace_before") == receipt.get("workspace_after") == {},
        "smoke workspace fingerprints are not both empty",
    )


def expected_smoke_command(receipt: Dict[str, Any]) -> List[str]:
    codex = receipt.get("codex")
    mcp = receipt.get("mcp")
    require(isinstance(codex, dict), "smoke Codex binding missing")
    require(isinstance(mcp, dict), "smoke MCP binding missing")
    require(codex.get("path") == CODEX_PATH, "smoke Codex path mismatch")
    require(
        codex.get("sha256") == CODEX_SHA256,
        "smoke Codex digest mismatch",
    )
    codex_path = Path(CODEX_PATH)
    codex_info = codex_path.lstat()
    require(
        stat.S_ISREG(codex_info.st_mode) and not stat.S_ISLNK(codex_info.st_mode),
        "pinned Codex executable type mismatch",
    )
    require(sha256(codex_path) == CODEX_SHA256, "pinned Codex executable digest mismatch")
    mcp_python = mcp.get("python")
    require(
        mcp_python == MCP_PYTHON_PATH,
        "smoke MCP Python path mismatch",
    )
    mcp_python_path = Path(MCP_PYTHON_PATH)
    require(mcp_python_path.is_file(), "pinned MCP Python executable missing")
    require(
        sha256(mcp_python_path) == MCP_PYTHON_SHA256,
        "pinned MCP Python executable digest mismatch",
    )
    script = str((ROOT / "static_model_smoke_mcp.py").resolve())
    workspace = str((ROOT / "STATIC_MODEL_LONG_SMOKE/workspace").resolve())
    catalog = str((ROOT / CATALOG_RELATIVE).resolve())
    return [
        CODEX_PATH,
        "exec",
        "-C",
        workspace,
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
        f'model_reasoning_effort="{EFFORT}"',
        "--config",
        f'model_catalog_json="{catalog}"',
        "--config",
        f'mcp_servers.ttl_smoke.command="{mcp_python}"',
        "--config",
        "mcp_servers.ttl_smoke.args="
        + json.dumps(["-B", script], separators=(",", ":")),
        "--config",
        f'mcp_servers.ttl_smoke.cwd="{ROOT.resolve()}"',
        "--config",
        "mcp_servers.ttl_smoke.required=true",
        "--config",
        "mcp_servers.ttl_smoke.startup_timeout_sec=120",
        "--config",
        "mcp_servers.ttl_smoke.tool_timeout_sec=420",
        "--config",
        'mcp_servers.ttl_smoke.default_tools_approval_mode="approve"',
    ]


def expected_mcp_executables(receipt: Dict[str, Any]) -> set[str]:
    mcp = receipt.get("mcp")
    require(isinstance(mcp, dict), "smoke MCP binding missing")
    configured_text = mcp.get("python")
    require(
        configured_text == MCP_PYTHON_PATH,
        "smoke MCP Python path mismatch",
    )
    configured = Path(MCP_PYTHON_PATH)
    require(configured.is_file(), "pinned MCP Python executable missing")
    require(
        sha256(configured) == MCP_PYTHON_SHA256,
        "pinned MCP Python executable digest mismatch",
    )
    try:
        resolved = configured.resolve(strict=True)
    except (FileNotFoundError, RuntimeError) as error:
        raise RuntimeError(f"smoke MCP Python cannot be resolved: {error}") from error
    require(
        str(resolved) == MCP_PYTHON_RESOLVED_PATH,
        "pinned MCP Python resolution mismatch",
    )
    macos_framework_launcher = Path(MCP_MACOS_LAUNCHER_PATH)
    require(macos_framework_launcher.is_file(), "pinned MCP Python launcher missing")
    require(
        sha256(macos_framework_launcher) == MCP_MACOS_LAUNCHER_SHA256,
        "pinned MCP Python launcher digest mismatch",
    )
    allowed = {str(configured), str(resolved), str(macos_framework_launcher)}
    return allowed


def has_debug_models_command(value: str) -> bool:
    return re.search(r"(?<![a-z0-9_])debug\s+models(?![a-z0-9_])", value.casefold()) is not None


def has_model_cache_marker(value: str) -> bool:
    return (
        re.search(
            r"(?<![a-z0-9_])models?(?:[\s_-]+)cache(?:\.json)?(?![a-z0-9_])",
            value.casefold(),
        )
        is not None
    )


def manifest_rows() -> Dict[str, str]:
    rows: Dict[str, str] = {}
    source = (ROOT / "SHA256SUMS").read_text(encoding="utf-8")
    require(source.endswith("\n"), "SHA256SUMS lacks terminal LF")
    paths: List[str] = []
    for line in source.splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        require(match is not None, f"malformed manifest row: {line!r}")
        digest, relative = match.groups()
        require(relative not in rows, f"duplicate manifest path: {relative}")
        require(not relative.startswith(("/", "../")), f"unsafe manifest path: {relative}")
        rows[relative] = digest
        paths.append(relative)
    require(paths == sorted(paths), "manifest paths are not sorted")
    return rows


def actual_release_files() -> List[str]:
    values: List[str] = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT).as_posix()
        info = path.lstat()
        require(not stat.S_ISLNK(info.st_mode), f"release symlink: {relative}")
        require("__pycache__" not in path.parts, f"bytecode-cache path in release: {relative}")
        if stat.S_ISDIR(info.st_mode):
            continue
        require(stat.S_ISREG(info.st_mode), f"non-regular release file: {relative}")
        require(path.suffix != ".pyc", f"bytecode in release: {relative}")
        require(not relative.startswith("artifacts/"), f"stale artifact file in release: {relative}")
        require(
            not relative.startswith("STATIC_MODEL_LONG_SMOKE/workspace/"),
            f"nonempty smoke workspace file: {relative}",
        )
        if relative == "SHA256SUMS":
            continue
        values.append(relative)
    return sorted(values)


def check_manifest() -> None:
    rows = manifest_rows()
    actual = actual_release_files()
    require(sorted(rows) == actual, "manifest inventory differs from release files")
    for relative, expected in rows.items():
        require(sha256(ROOT / relative) == expected, f"digest mismatch: {relative}")


def check_catalog() -> None:
    path = ROOT / CATALOG_RELATIVE
    info = path.lstat()
    require(stat.S_ISREG(info.st_mode) and not stat.S_ISLNK(info.st_mode), "catalog type mismatch")
    require(info.st_size == CATALOG_BYTES, "catalog byte length mismatch")
    require(sha256(path) == CATALOG_SHA256, "catalog digest mismatch")
    value = strict_json(path)
    require(isinstance(value, dict) and set(value) == {"models"}, "catalog keyset mismatch")
    models = value["models"]
    require(isinstance(models, list) and len(models) == 1, "catalog model count mismatch")
    require(isinstance(models[0], dict) and models[0].get("slug") == MODEL, "catalog slug mismatch")
    levels = models[0].get("supported_reasoning_levels")
    require(isinstance(levels, list), "catalog levels missing")
    efforts = [level.get("effort") for level in levels if isinstance(level, dict)]
    require(len(efforts) == len(levels) == len(set(efforts)), "catalog levels invalid")
    require(EFFORT in efforts, "catalog lacks xhigh")


def current_runtime_snapshot() -> Dict[str, Dict[str, Any]]:
    root = ROOT / "runtime"
    result: Dict[str, Dict[str, Any]] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        info = path.lstat()
        require(not stat.S_ISLNK(info.st_mode), f"runtime symlink: {relative}")
        if path.is_dir():
            continue
        require(stat.S_ISREG(info.st_mode), f"runtime special file: {relative}")
        result[relative] = {
            "bytes": info.st_size,
            "sha256": sha256(path),
            "mode": stat.S_IMODE(info.st_mode),
        }
    return result


def check_release_pins() -> None:
    path = ROOT / "runtime/release_pins.py"
    require(sha256(path) == PINS_FILE_SHA256, "release_pins.py digest mismatch")
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("frozen_release_pins", path)
    require(spec is not None and spec.loader is not None, "cannot load release pins")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require(module.RELEASE_PINSET_SHA256 == PINSET_SHA256, "declared pinset mismatch")
    require(module.canonical_pinset_sha256() == PINSET_SHA256, "canonical pinset mismatch")
    require(len(module.SOURCE_BUNDLE_PINS) == 39, "source bundle count mismatch")
    require(len(module.FIXED_SOURCE_RUNTIME_PATHS) == 22, "searchable source count mismatch")
    require(len(module.TARGET_BUNDLE_PINS) == 3, "target bundle count mismatch")
    require(len(module.P142_SOURCE_LOCATORS) == 5, "P14.2 locator route count mismatch")
    require(
        tuple((start, end) for start, end, _ in module.P142_SOURCE_LOCATORS["dxz_2302_02541v3"])
        == ((437, 458), (848, 880), (873, 925)),
        "P14.2 DXZ LF locator mismatch",
    )
    for relative, pin in module.SOURCE_BUNDLE_PINS.items():
        source = ROOT / "runtime" / relative
        require(source.stat().st_size == pin["bytes"], f"source length mismatch: {relative}")
        require(sha256(source) == pin["sha256"], f"source digest mismatch: {relative}")
    for relative, pin in module.TARGET_BUNDLE_PINS.items():
        target = ROOT / relative
        require(target.stat().st_size == pin["bytes"], f"target length mismatch: {relative}")
        require(sha256(target) == pin["sha256"], f"target digest mismatch: {relative}")


def check_code_contract() -> None:
    contract = (ROOT / "runtime/contract.md").read_text(encoding="utf-8")
    service = (ROOT / "runtime/hardened_service.py").read_text(encoding="utf-8")
    mcp = (ROOT / "runtime/hardened_mcp.py").read_text(encoding="utf-8")
    runner = (ROOT / "run_static_model_long_smoke.py").read_text(encoding="utf-8")
    lf_helper = (ROOT / "runtime/lf_source_lines.py").read_text(encoding="utf-8")
    require("input_shape" not in contract + service + mcp, "legacy input_shape remains")
    require('meta={"statement": <exact supplied Statement>}' in contract, "memory_init contract mismatch")
    require(
        "v3.3.3-r5-p142-source-closed-lf-v2" in contract + service + mcp,
        "P14.2 LF-v2 release version mismatch",
    )
    for source in (service, mcp):
        require(CATALOG_SHA256 in source, "catalog digest pin missing from executable")
        require("_assert_static_model_catalog" in source, "catalog assertion missing")
        require("model_catalog_runtime_path" in source, "catalog receipt path binding missing")
        require("model_catalog_sha256" in source, "catalog receipt digest binding missing")
        require("model_catalog_model" in source, "catalog receipt model binding missing")
        require("model_catalog_reasoning_effort" in source, "catalog receipt effort binding missing")
    require("model_catalog_json=" in service, "static catalog launch config missing")
    require("codex_models_manager::manager" not in service, "model-manager raw allowlist was added")
    require("_assert_release_target_bundle" in service, "host target pin gate missing")
    require("_assert_release_target_bundle" in mcp, "MCP target pin gate missing")
    require("_assert_exact_p142_request" in service, "exact P14.2 request gate missing")
    require("P142_SOURCE_LOCATORS" in service + mcp, "P14.2 locator bindings missing")
    require('split(b"\\x0a")' in lf_helper, "byte-level LF-only source split missing")
    require(".splitlines(" not in lf_helper, "generic line splitting remains in LF helper")
    require(service.count("read_lf_only_source_lines(") == 3,
            "host does not route all three source-addressing paths through LF helper")
    require(mcp.count("read_lf_only_source_lines(") == 3,
            "MCP does not route all three source-addressing paths through LF helper")
    require(".splitlines(" not in service + mcp,
            "generic line splitting remains in host/MCP source-addressing runtime")
    require("twenty-two searchable" in contract, "P14.2 source inventory contract missing")
    require("mesh upper-semicontinuity proof" in contract, "P14.2 source scope firewall missing")
    require("848--880 (formula (28)" in contract, "DXZ transition locator missing")
    require("Adding the locally bounded" in contract, "quasi-psh DEL reduction missing")
    require("appends exactly one LF" in contract, "P14.2 source normalization contract missing")
    require("Only byte `0x0a` separates lines" in contract,
            "LF-only source-address contract missing")
    require("437--458" in contract, "DXZ I-maximality tail locator missing")
    require("Codex stdout is strict JSONL" in contract, "split smoke-log contract missing")
    require("terminal process observation" in contract, "terminal process contract missing")
    require("stdout=stdout_handle" in runner and "stderr=stderr_handle" in runner,
            "smoke stdout/stderr split missing")
    require("os.openpty()" in runner and "stdin=stdin_slave_fd" in runner,
            "dedicated terminal stdin strategy missing")
    require("stderr=subprocess.STDOUT" not in runner, "smoke stderr is still merged")
    for marker in ("exited_before_scan", "exited_during_scan"):
        require(marker in runner, f"smoke exit-race state missing: {marker}")


def validate_stdout_smoke(stdout: str, receipt: Dict[str, Any]) -> Tuple[datetime, datetime]:
    stdout_folded = stdout.casefold()
    recomputed_diagnostic_count = sum(
        stdout_folded.count(value.casefold()) for value in FORBIDDEN_DIAGNOSTIC_MARKERS
    )
    require(
        exact_int(receipt.get("stdout_forbidden_diagnostic_count"))
        and receipt["stdout_forbidden_diagnostic_count"]
        == recomputed_diagnostic_count
        == 0,
        "stdout diagnostic count mismatch",
    )
    for forbidden in FORBIDDEN_DIAGNOSTIC_MARKERS:
        require(
            forbidden.casefold() not in stdout_folded,
            f"forbidden diagnostic in smoke stdout: {forbidden}",
        )
    require(not has_model_cache_marker(stdout), "model-cache marker in smoke stdout")
    require(not has_debug_models_command(stdout), "debug-model command in smoke stdout")

    records: List[Tuple[int, Dict[str, Any]]] = []
    for line_number, line in enumerate(strict_lf_lines(stdout, "Codex stdout"), 1):
        try:
            value = strict_json_text(line)
        except (json.JSONDecodeError, ValueError) as error:
            raise RuntimeError(
                f"Codex stdout line {line_number} is not strict JSON: {error}"
            ) from error
        require(isinstance(value, dict), f"Codex stdout line {line_number} is not an object")
        records.append((line_number, value))
    require(len(records) >= 6, "stdout smoke JSON lifecycle is incomplete")

    allowed_item_types = {"error", "mcp_tool_call", "agent_message"}
    for _, record in records:
        item = record.get("item")
        if isinstance(item, dict):
            require(
                item.get("type") in allowed_item_types,
                "raw smoke contains an unexpected item type",
            )

    mcp_records = [
        (line_number, record, record["item"])
        for line_number, record in records
        if isinstance(record.get("item"), dict)
        and record["item"].get("type") == "mcp_tool_call"
    ]
    require(len(mcp_records) == 2, "raw smoke contains an unexpected MCP event count")
    started_line, started_record, started_item = mcp_records[0]
    completed_line, completed_record, completed_item = mcp_records[1]
    require(started_record.get("type") == "item.started", "raw smoke MCP start event missing")
    require(completed_record.get("type") == "item.completed", "raw smoke MCP completion event missing")
    require(started_line < completed_line, "raw smoke MCP event order mismatch")
    for item in (started_item, completed_item):
        require(item.get("server") == "ttl_smoke", "raw smoke MCP server mismatch")
        require(item.get("tool") == "wait_across_catalog_ttl", "raw smoke MCP tool mismatch")
        require(item.get("arguments") == {"seconds": SMOKE_WAIT_SECONDS}, "raw smoke MCP arguments mismatch")
    require(
        isinstance(started_item.get("id"), str)
        and started_item.get("id") == completed_item.get("id"),
        "raw smoke MCP identity mismatch",
    )
    require(
        started_item.get("status") == "in_progress"
        and started_item.get("result") is None
        and started_item.get("error") is None,
        "raw smoke MCP start state mismatch",
    )
    require(
        completed_item.get("status") == "completed" and completed_item.get("error") is None,
        "raw smoke MCP completion state mismatch",
    )
    result = completed_item.get("result")
    require(isinstance(result, dict), "raw smoke MCP result missing")
    structured = result.get("structured_content")
    require(
        isinstance(structured, dict) and set(structured) == MCP_RESULT_KEYS,
        "raw smoke MCP structured result shape mismatch",
    )
    require(
        structured.get("status") == "ok"
        and exact_int(structured.get("requested_seconds"))
        and structured["requested_seconds"] == SMOKE_WAIT_SECONDS,
        "raw smoke MCP result contract mismatch",
    )
    mcp_elapsed = structured.get("elapsed_seconds")
    require(finite_number(mcp_elapsed), "raw smoke MCP elapsed value invalid")
    require(
        SMOKE_WAIT_SECONDS <= mcp_elapsed <= SMOKE_WAIT_SECONDS + SMOKE_MCP_MAX_OVERRUN_SECONDS,
        "raw smoke MCP elapsed value outside bounds",
    )
    receipt_elapsed = receipt.get("elapsed_seconds")
    require(
        finite_number(receipt_elapsed) and mcp_elapsed <= receipt_elapsed,
        "raw smoke MCP elapsed value exceeds total smoke duration",
    )
    content = result.get("content")
    require(
        isinstance(content, list)
        and len(content) == 1
        and isinstance(content[0], dict)
        and content[0].get("type") == "text"
        and isinstance(content[0].get("text"), str),
        "raw smoke MCP text result shape mismatch",
    )
    require(
        strict_json_text(content[0]["text"]) == structured,
        "raw smoke MCP text and structured results differ",
    )
    mcp_started = parse_utc(structured.get("started_at_utc"), "raw MCP start")
    mcp_completed = parse_utc(structured.get("completed_at_utc"), "raw MCP completion")
    require(mcp_started < mcp_completed, "raw smoke MCP timestamps are not increasing")
    require(
        mcp_started + timedelta(seconds=SMOKE_CACHE_HORIZON_SECONDS)
        <= mcp_completed,
        "raw MCP interval does not cross the model-cache horizon",
    )
    require(
        abs((mcp_completed - mcp_started).total_seconds() - mcp_elapsed)
        <= SMOKE_CLOCK_SKEW_SECONDS,
        "raw smoke MCP wall/monotonic duration mismatch",
    )

    agent_messages = [
        (line_number, record)
        for line_number, record in records
        if isinstance(record.get("item"), dict)
        and record["item"].get("type") == "agent_message"
    ]
    require(
        len(agent_messages) == 1
        and agent_messages[0][1]["item"].get("text") == "STATIC_MODEL_SMOKE_OK",
        "raw smoke terminal marker mismatch",
    )
    require(
        completed_line < agent_messages[0][0],
        "raw smoke terminal marker precedes MCP completion",
    )

    record_values = [record for _, record in records]
    require(
        record_values[0].get("type") == "thread.started"
        and set(record_values[0]) == {"type", "thread_id"}
        and isinstance(record_values[0].get("thread_id"), str)
        and bool(record_values[0]["thread_id"]),
        "raw smoke thread start mismatch",
    )
    require(record_values[1] == {"type": "turn.started"}, "raw smoke turn start mismatch")
    require(
        record_values[-1].get("type") == "turn.completed"
        and set(record_values[-1]) == {"type", "usage"}
        and isinstance(record_values[-1].get("usage"), dict),
        "raw smoke turn completion mismatch",
    )
    started_position = next(
        index for index, record in enumerate(record_values) if record is started_record
    )
    completed_position = next(
        index for index, record in enumerate(record_values) if record is completed_record
    )
    agent_position = next(
        index for index, record in enumerate(record_values) if record is agent_messages[0][1]
    )
    require(
        (started_position, completed_position, agent_position)
        == (len(record_values) - 4, len(record_values) - 3, len(record_values) - 2),
        "raw smoke thread/turn lifecycle order mismatch",
    )
    pre_tool_items = record_values[2:started_position]
    require(len(pre_tool_items) <= 1, "too many pre-tool error items")
    skills_budget_warning = re.compile(
        r"Exceeded skills context budget\. All skill descriptions were removed and "
        r"([1-9]\d{0,3}) additional skills were not included in the "
        r"model-visible skills list\."
    )
    for record in pre_tool_items:
        item = record.get("item")
        require(
            record.get("type") == "item.completed"
            and isinstance(item, dict)
            and set(item) == {"id", "type", "message"}
            and isinstance(item.get("id"), str)
            and item.get("type") == "error"
            and isinstance(item.get("message"), str)
            and skills_budget_warning.fullmatch(item["message"]) is not None,
            "raw smoke pre-tool item mismatch",
        )
    require(
        agent_messages[0][1].get("type") == "item.completed",
        "raw smoke agent-message lifecycle mismatch",
    )
    return mcp_started, mcp_completed


def validate_stderr_smoke(stderr: str, receipt: Dict[str, Any]) -> None:
    folded = stderr.casefold()
    recomputed_diagnostic_count = sum(
        folded.count(value.casefold()) for value in FORBIDDEN_DIAGNOSTIC_MARKERS
    )
    require(
        exact_int(receipt.get("stderr_forbidden_diagnostic_count"))
        and receipt["stderr_forbidden_diagnostic_count"]
        == recomputed_diagnostic_count
        == 0,
        "stderr diagnostic count mismatch",
    )
    for forbidden in FORBIDDEN_DIAGNOSTIC_MARKERS:
        require(
            forbidden.casefold() not in folded,
            f"forbidden diagnostic in smoke stderr: {forbidden}",
        )
    require(not has_model_cache_marker(stderr), "model-cache marker in smoke stderr")
    require(not has_debug_models_command(stderr), "debug-model command in smoke stderr")

    receipt_started = parse_utc(receipt.get("started_at_utc"), "smoke receipt start")
    receipt_completed = parse_utc(receipt.get("completed_at_utc"), "smoke receipt completion")
    require(receipt_started < receipt_completed, "smoke receipt timestamps are not increasing")
    counts = {"state_db": 0, "shell_snapshot_cleanup": 0}
    previous_time: Optional[datetime] = None
    for line_number, line in enumerate(strict_lf_lines(stderr, "Codex stderr"), 1):
        state = STATE_WARNING.fullmatch(line)
        shell = SHELL_WARNING.fullmatch(line)
        if state is not None:
            kind = "state_db"
            timestamp_text = state.group(1)
        elif shell is not None:
            kind = "shell_snapshot_cleanup"
            timestamp_text = shell.group(1)
        else:
            raise RuntimeError(
                f"Codex stderr line {line_number} is not an allowlisted warning"
            )
        warning_time = parse_utc(timestamp_text, f"Codex stderr line {line_number}")
        require(
            receipt_started <= warning_time <= receipt_completed,
            f"Codex stderr line {line_number} is outside the smoke interval",
        )
        if kind == "state_db":
            require(
                warning_time <= receipt_started + timedelta(seconds=5),
                f"state warning line {line_number} is outside the startup window",
            )
        if previous_time is not None:
            require(previous_time <= warning_time, "Codex stderr warning timestamps regress")
        previous_time = warning_time
        counts[kind] += 1
    require(counts["state_db"] <= STATE_WARNING_LIMIT, "too many state-database stderr warnings")
    require(
        counts["shell_snapshot_cleanup"] <= SHELL_WARNING_LIMIT,
        "too many shell-snapshot stderr warnings",
    )
    recorded = receipt.get("stderr_warning_counts")
    require(
        isinstance(recorded, dict)
        and set(recorded) == set(counts)
        and all(exact_int(recorded[key]) for key in counts)
        and recorded == counts,
        "stderr warning-count receipt mismatch",
    )


def validate_cache_horizon_bracketing(
    timestamps: List[datetime],
    roles_by_sample: List[set[str]],
    root_observations: List[str],
    mcp_started: datetime,
    mcp_completed: datetime,
) -> None:
    require(
        len(timestamps) == len(roles_by_sample) == len(root_observations)
        and bool(timestamps),
        "cache-horizon sample metadata mismatch",
    )
    horizon = mcp_started + timedelta(seconds=SMOKE_CACHE_HORIZON_SECONDS)
    require(
        horizon <= mcp_completed,
        "raw MCP interval does not cross the model-cache horizon",
    )

    before_indexes = [
        index for index, sampled_at in enumerate(timestamps) if sampled_at <= horizon
    ]
    require(before_indexes, "no process sample brackets the cache horizon from before")
    before_index = max(before_indexes, key=lambda index: timestamps[index])
    require(
        (horizon - timestamps[before_index]).total_seconds()
        <= SMOKE_SAMPLE_MAX_GAP_SECONDS,
        "process sample before cache horizon is too distant",
    )
    require(
        {"codex", "mcp-python", "code-mode-host"}
        <= roles_by_sample[before_index],
        "pre-horizon process sample lacks the expected bound process roles",
    )

    after_indexes = [
        index for index, sampled_at in enumerate(timestamps) if sampled_at >= horizon
    ]
    require(after_indexes, "no process sample brackets the cache horizon from after")
    after_index = min(after_indexes, key=lambda index: timestamps[index])
    after_time = timestamps[after_index]
    require(
        (after_time - horizon).total_seconds() <= SMOKE_SAMPLE_MAX_GAP_SECONDS,
        "process sample after cache horizon is too distant",
    )
    after_roles = roles_by_sample[after_index]
    if {"codex", "code-mode-host"} <= after_roles:
        if after_time <= mcp_completed:
            require(
                "mcp-python" in after_roles,
                "in-wait post-horizon sample lacks the bound MCP role",
            )
        else:
            require(
                horizon <= mcp_completed <= after_time,
                "raw MCP completion does not bridge the post-horizon sample interval",
            )
        return
    require(
        root_observations[after_index] in {"exited_before_scan", "exited_during_scan"},
        "post-horizon live process sample lacks the bound Codex/host roles",
    )
    require(not after_roles, "terminal post-horizon observation has partial process roles")
    require(
        horizon <= mcp_completed <= after_time,
        "terminal process observation does not follow horizon-crossing MCP completion",
    )


def validate_process_samples(
    samples: Any,
    receipt: Dict[str, Any],
    mcp_started: datetime,
    mcp_completed: datetime,
) -> None:
    require(isinstance(samples, list), "process samples are not a list")
    sample_count = receipt.get("process_sample_count")
    require(exact_int(sample_count), "receipt process sample count is not an integer")
    require(sample_count == len(samples), "receipt/process sample count mismatch")
    live_count = receipt.get("live_process_sample_count")
    terminal_count = receipt.get("terminal_process_sample_count")
    require(exact_int(live_count) and live_count > 0, "receipt live sample count invalid")
    require(
        exact_int(terminal_count) and terminal_count == 1,
        "receipt terminal sample count invalid",
    )
    receipt_root_pid = receipt.get("root_pid")
    require(exact_int(receipt_root_pid) and receipt_root_pid > 0, "receipt root PID invalid")

    receipt_elapsed = receipt.get("elapsed_seconds")
    require(finite_number(receipt_elapsed), "smoke elapsed value invalid")
    require(
        SMOKE_WAIT_SECONDS <= receipt_elapsed <= SMOKE_MAX_RUN_SECONDS,
        "smoke elapsed value outside bounds",
    )
    minimum_samples = (
        math.ceil(
            max(
                0.0,
                receipt_elapsed
                - SMOKE_INITIAL_SAMPLE_MAX_SECONDS
                - SMOKE_FINAL_SAMPLE_MAX_AGE_SECONDS,
            )
            / SMOKE_SAMPLE_MAX_GAP_SECONDS
        )
        + 1
    )
    maximum_samples = math.floor(receipt_elapsed / SMOKE_SAMPLE_MIN_GAP_SECONDS) + 2
    require(
        minimum_samples <= len(samples) <= maximum_samples,
        "process sample count outside cadence-derived bounds",
    )
    receipt_started = parse_utc(receipt.get("started_at_utc"), "smoke receipt start")
    receipt_completed = parse_utc(receipt.get("completed_at_utc"), "smoke receipt completion")
    require(receipt_started < receipt_completed, "smoke receipt timestamps are not increasing")
    require(
        abs((receipt_completed - receipt_started).total_seconds() - receipt_elapsed)
        <= SMOKE_CLOCK_SKEW_SECONDS,
        "smoke receipt wall/monotonic duration mismatch",
    )
    require(
        receipt_started <= mcp_started < mcp_completed <= receipt_completed,
        "raw MCP interval is outside smoke receipt interval",
    )

    expected_command = expected_smoke_command(receipt)
    command = receipt.get("command_without_prompt")
    require(command == expected_command, "smoke command does not exactly bind this release")
    expected_root_command = " ".join(expected_command + [SMOKE_PROMPT])
    host_command = str(Path(CODEX_PATH).with_name("codex-code-mode-host"))
    mcp_script = str((ROOT / "static_model_smoke_mcp.py").resolve())
    mcp_executables = expected_mcp_executables(receipt)

    elapsed_values: List[float] = []
    timestamps: List[datetime] = []
    roles_by_sample: List[set[str]] = []
    root_observations: List[str] = []
    root_pid = receipt_root_pid
    root_ppid: Optional[int] = None
    seen_processes: Dict[int, Tuple[int, str, int, float]] = {}
    all_commands: List[str] = []
    observed_live_count = 0
    observed_terminal_count = 0

    for index, sample in enumerate(samples):
        require(isinstance(sample, dict) and set(sample) == SAMPLE_KEYS, f"sample {index} shape mismatch")
        require(sample.get("sampling_error") is None, f"sample {index} has a sampling error")
        root_observation = sample.get("root_observation")
        require(
            root_observation in ROOT_OBSERVATIONS,
            f"sample {index} root observation invalid",
        )
        if root_observation == "live":
            observed_live_count += 1
            require(observed_terminal_count == 0, f"sample {index} is live after terminal exit")
        else:
            observed_terminal_count += 1
            require(index == len(samples) - 1, "terminal process observation is not final")
        sample_elapsed = sample.get("elapsed_seconds")
        require(
            finite_number(sample_elapsed) and sample_elapsed >= 0,
            f"sample {index} elapsed value invalid",
        )
        sampled_at = parse_utc(sample.get("sampled_at_utc"), f"sample {index} timestamp")
        require(
            receipt_started <= sampled_at <= receipt_completed,
            f"sample {index} timestamp is outside receipt interval",
        )
        require(
            abs((sampled_at - receipt_started).total_seconds() - sample_elapsed)
            <= SMOKE_CLOCK_SKEW_SECONDS,
            f"sample {index} wall/monotonic timestamp mismatch",
        )
        descendants = sample.get("descendants")
        require(isinstance(descendants, list), f"sample {index} process tree is not a list")
        rows: Dict[int, Dict[str, Any]] = {}
        row_elapsed_values: Dict[int, int] = {}
        for row_index, row in enumerate(descendants):
            require(
                isinstance(row, dict) and set(row) == PROCESS_ROW_KEYS,
                f"sample {index} process row {row_index} shape mismatch",
            )
            pid = row.get("pid")
            ppid = row.get("ppid")
            command_text = row.get("command")
            require(exact_int(pid) and pid > 0, f"sample {index} process PID invalid")
            require(exact_int(ppid) and ppid >= 0, f"sample {index} process PPID invalid")
            require(pid not in rows, f"sample {index} contains a duplicate PID")
            require(isinstance(command_text, str) and command_text, f"sample {index} command invalid")
            process_elapsed = process_elapsed_seconds(row.get("elapsed"))
            require(
                process_elapsed <= sample_elapsed + SMOKE_PROCESS_ELAPSED_SKEW_SECONDS,
                f"sample {index} process age exceeds the smoke age",
            )
            rows[pid] = row
            row_elapsed_values[pid] = process_elapsed
            all_commands.append(command_text)
        role_counts = {"codex": 0, "mcp-python": 0, "code-mode-host": 0}
        role_bearing_tree = False
        if root_observation == "exited_before_scan":
            require(not descendants, "exited-before-scan observation contains processes")
        elif (
            root_observation == "exited_during_scan"
            and len(descendants) == 1
            and descendants[0].get("command") == "(codex)"
        ):
            zombie = descendants[0]
            require(zombie["pid"] == root_pid, "terminal zombie PID mismatch")
            require(root_ppid is not None and zombie["ppid"] == root_ppid,
                    "terminal zombie PPID mismatch")
            require(
                abs(row_elapsed_values[root_pid] - sample_elapsed)
                <= SMOKE_PROCESS_ELAPSED_SKEW_SECONDS,
                "terminal zombie age does not bind the smoke start",
            )
        elif root_observation == "exited_during_scan" and not descendants:
            pass
        else:
            require(descendants, f"sample {index} live process tree is empty")
            roots = [row for row in descendants if row["command"] == expected_root_command]
            require(
                len(roots) == 1,
                f"sample {index} does not contain exactly one bound Codex root",
            )
            root = roots[0]
            if root_ppid is None:
                root_ppid = root["ppid"]
            require(
                (root["pid"], root["ppid"]) == (root_pid, root_ppid),
                f"sample {index} Codex root identity changed",
            )
            require(root_ppid not in rows, f"sample {index} Codex root parent is inside its subtree")
            require(
                abs(row_elapsed_values[root_pid] - sample_elapsed)
                <= SMOKE_PROCESS_ELAPSED_SKEW_SECONDS,
                f"sample {index} Codex root age does not bind the smoke start",
            )
            role_counts["codex"] = 1
            role_bearing_tree = True
            for pid, row in rows.items():
                if pid == root_pid:
                    continue
                visited = {pid}
                parent = row["ppid"]
                while parent != root_pid:
                    require(parent in rows, f"sample {index} contains an orphan process")
                    require(parent not in visited, f"sample {index} contains a process-parent cycle")
                    visited.add(parent)
                    parent = rows[parent]["ppid"]
                command_text = row["command"]
                if command_text == host_command:
                    role_counts["code-mode-host"] += 1
                    continue
                try:
                    tokens = shlex.split(command_text)
                except ValueError as error:
                    raise RuntimeError(
                        f"sample {index} contains an unparseable command: {error}"
                    ) from error
                if (
                    len(tokens) == 3
                    and tokens[0] in mcp_executables
                    and tokens[1:] == ["-B", mcp_script]
                ):
                    role_counts["mcp-python"] += 1
                    continue
                raise RuntimeError(f"sample {index} contains an unexpected descendant command")
            require(
                role_counts["mcp-python"] <= 1
                and role_counts["code-mode-host"] <= 1,
                f"sample {index} contains duplicate expected process roles",
            )

        if root_observation == "live":
            require(role_bearing_tree, f"sample {index} live root is not bound")
        if role_bearing_tree:
            for pid, row in rows.items():
                command_text = row["command"]
                process_elapsed = row_elapsed_values[pid]
                previous = seen_processes.get(pid)
                if previous is not None:
                    old_ppid, old_command, old_process_elapsed, old_sample_elapsed = previous
                    require(
                        (row["ppid"], command_text) == (old_ppid, old_command),
                        f"process identity changed for PID {pid}",
                    )
                    require(
                        process_elapsed >= old_process_elapsed,
                        f"process elapsed time regressed for PID {pid}",
                    )
                    require(
                        abs(
                            (process_elapsed - old_process_elapsed)
                            - (sample_elapsed - old_sample_elapsed)
                        )
                        <= SMOKE_PROCESS_ELAPSED_SKEW_SECONDS,
                        f"process/sample elapsed time mismatch for PID {pid}",
                    )
                seen_processes[pid] = (
                    row["ppid"], command_text, process_elapsed, float(sample_elapsed)
                )
        elapsed_values.append(float(sample_elapsed))
        timestamps.append(sampled_at)
        roles_by_sample.append(
            {role for role, count in role_counts.items() if count == 1}
        )
        root_observations.append(root_observation)

    require(observed_live_count == live_count, "receipt/live sample count mismatch")
    require(observed_terminal_count == terminal_count == 1,
            "receipt/terminal sample count mismatch")
    require(root_observations[0] == "live", "initial process observation is not live")
    require(root_observations[-1] != "live", "final process observation is not terminal")
    require(root_ppid is not None, "no bound live Codex root was observed")
    require(timestamps[-1] >= mcp_completed, "terminal observation precedes MCP completion")
    require(elapsed_values[0] <= SMOKE_INITIAL_SAMPLE_MAX_SECONDS, "initial process sample is too late")
    for index, (left, right) in enumerate(zip(elapsed_values, elapsed_values[1:]), 1):
        gap = right - left
        if root_observations[index] == "live":
            require(
                SMOKE_SAMPLE_MIN_GAP_SECONDS <= gap <= SMOKE_SAMPLE_MAX_GAP_SECONDS,
                f"live process sample cadence mismatch at sample {index}",
            )
        else:
            require(
                0 <= gap <= SMOKE_SAMPLE_MAX_GAP_SECONDS,
                f"terminal process observation cadence mismatch at sample {index}",
            )
    require(
        0 <= receipt_elapsed - elapsed_values[-1] <= SMOKE_FINAL_SAMPLE_MAX_AGE_SECONDS,
        "final process sample is too far from smoke completion",
    )
    require(
        all(left < right for left, right in zip(timestamps, timestamps[1:])),
        "process sample timestamps are not strictly increasing",
    )
    samples_before_mcp = [
        value
        for value, observation in zip(timestamps, root_observations)
        if value <= mcp_started and observation == "live"
    ]
    require(samples_before_mcp, "no process sample precedes the MCP wait")
    require(
        (mcp_started - samples_before_mcp[-1]).total_seconds() <= SMOKE_SAMPLE_MAX_GAP_SECONDS,
        "process samples do not cover MCP wait startup",
    )
    validate_cache_horizon_bracketing(
        timestamps,
        roles_by_sample,
        root_observations,
        mcp_started,
        mcp_completed,
    )

    for command_text in all_commands:
        folded = command_text.casefold()
        for forbidden in FORBIDDEN_DIAGNOSTIC_MARKERS:
            require(
                forbidden.casefold() not in folded,
                f"forbidden subprocess diagnostic observed: {forbidden}",
            )
        require(not has_model_cache_marker(command_text), "model-cache subprocess observed")
        require(not has_debug_models_command(command_text), "debug-model subprocess observed")


def check_long_smoke(smoke_override: Optional[Path] = None) -> None:
    smoke = ROOT / "STATIC_MODEL_LONG_SMOKE" if smoke_override is None else smoke_override
    info = smoke.lstat()
    require(stat.S_ISDIR(info.st_mode) and not stat.S_ISLNK(info.st_mode), "smoke root type mismatch")
    for name in (
        "receipt.json",
        "codex.stdout.jsonl",
        "codex.stderr.log",
        "process_samples.json",
    ):
        artifact_info = (smoke / name).lstat()
        require(
            stat.S_ISREG(artifact_info.st_mode) and not stat.S_ISLNK(artifact_info.st_mode),
            f"smoke artifact type mismatch: {name}",
        )
    receipt = strict_json(smoke / "receipt.json")
    require(isinstance(receipt, dict), "smoke receipt is not an object")
    require(receipt.get("format") == "rethlas-static-model-long-smoke-v2", "smoke receipt format mismatch")
    require(receipt.get("status") == "passed" and receipt.get("errors") == [], "smoke did not pass")
    require(
        exact_int(receipt.get("wait_seconds")) and receipt["wait_seconds"] == SMOKE_WAIT_SECONDS,
        "smoke wait contract mismatch",
    )
    require(
        exact_int(receipt.get("completed_wait_calls")) and receipt["completed_wait_calls"] == 1,
        "smoke MCP call count mismatch",
    )
    require(exact_int(receipt.get("return_code")) and receipt["return_code"] == 0, "smoke Codex exit mismatch")
    require(receipt.get("model_manager_strategy") == "StaticModelsManager", "smoke model manager mismatch")
    require(
        receipt.get("stdin_strategy") == "dedicated-pty-no-input",
        "smoke stdin strategy mismatch",
    )
    require(receipt.get("runtime_before") == receipt.get("runtime_after"), "smoke runtime drift")
    require(
        receipt.get("runtime_before") == current_runtime_snapshot(),
        "smoke does not bind the current release runtime",
    )
    require_clean_smoke_workspace(smoke / "workspace", receipt)
    catalog = receipt.get("catalog", {})
    require(
        isinstance(catalog, dict)
        and catalog.get("path") == str((ROOT / CATALOG_RELATIVE).resolve()),
        "smoke catalog path belongs to another release",
    )
    require(catalog.get("bytes") == CATALOG_BYTES, "smoke catalog length mismatch")
    require(catalog.get("sha256") == CATALOG_SHA256, "smoke catalog digest mismatch")
    require(catalog.get("model") == MODEL, "smoke model mismatch")
    require(catalog.get("selected_reasoning_effort") == EFFORT, "smoke effort mismatch")
    mcp = receipt.get("mcp", {})
    require(
        isinstance(mcp, dict)
        and mcp.get("script") == str((ROOT / "static_model_smoke_mcp.py").resolve()),
        "smoke MCP path belongs to another release",
    )
    require(mcp.get("script_sha256") == sha256(ROOT / "static_model_smoke_mcp.py"), "smoke MCP digest mismatch")
    require(receipt.get("prompt_sha256") == hashlib.sha256(SMOKE_PROMPT.encode("utf-8")).hexdigest(), "smoke prompt mismatch")
    stdout_path = smoke / "codex.stdout.jsonl"
    stderr_path = smoke / "codex.stderr.log"
    samples_path = smoke / "process_samples.json"
    require(
        sha256(stdout_path) == receipt.get("stdout_log_sha256"),
        "smoke stdout-log digest mismatch",
    )
    require(
        sha256(stderr_path) == receipt.get("stderr_log_sha256"),
        "smoke stderr-log digest mismatch",
    )
    require(sha256(samples_path) == receipt.get("process_samples_sha256"), "sample digest mismatch")
    stdout = stdout_path.read_text(encoding="utf-8")
    stderr = stderr_path.read_text(encoding="utf-8")
    samples = strict_json(samples_path)
    validate_stderr_smoke(stderr, receipt)
    mcp_started, mcp_completed = validate_stdout_smoke(stdout, receipt)
    validate_process_samples(samples, receipt, mcp_started, mcp_completed)


def main() -> None:
    check_manifest()
    check_catalog()
    check_release_pins()
    check_code_contract()
    check_long_smoke()
    print("PASS_AUTHOR_FREEZE_NOT_INDEPENDENTLY_AUDITED")


if __name__ == "__main__":
    main()
