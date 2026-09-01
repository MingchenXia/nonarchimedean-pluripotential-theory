from __future__ import annotations

import argparse
from collections import Counter
import copy
from datetime import datetime, timedelta
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
from typing import Any, Callable


HERE = Path(__file__).resolve().parent
SOURCE = Path(
    "/private/tmp/"
    "p148_smoke_infrastructure_repaired_authored_stage_dossier_v1_20260901"
)
STAGE = SOURCE / "release_stage"
PACKET = SOURCE / "packet"
SNAPSHOTS = SOURCE / "snapshots"
PREDECESSOR = Path(
    "/private/tmp/p148_repaired_source_release_authored_stage_dossier_v1_20260901"
)
PREDECESSOR_STAGE = PREDECESSOR / "release_stage"
PREDECESSOR_AUDIT = Path(
    "/private/tmp/p148_repaired_source_release_independent_hostile_audit_v1_20260901"
)
TEST_PYTHON = Path(
    "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/"
    "agents/verification/tmp/verification-venv/bin/python"
)

SOURCE_MANIFEST_SHA = "bea75f18d2b5f765d07439c19189fa203b7a7f772a7dff9cd09c1d1d65721a30"
SOURCE_CHECKER_SHA = "eccd356ab12fc8f3405fe4b2f4c090d46215b1be1c9377bca9efcc9afce33064"
STAGE_MANIFEST_SHA = "4c2a6c9d61966aeac3f0c5c27284a0746d1a8bcc4520340016247947f9c9accc"
STAGE_CHECKER_SHA = "2fcacad42bd34caca8763e80d7c326545d189d49cc70e1f4fe0b73a6a41cf356"
RUNNER_SHA = "6898ef6e8789620dafb5ade3b694f82157a3ef11325ae50670c84aaa2ffc8c09"
CONTRACT_SHA = "fd02279e2379d505a033a38500041b1f9541f9a6daa3c55350cc135448e07abf"
TESTS_SHA = "558a7068e2ebe958d7f267033642f6ea9f83e29cfad3fbfb1cbf6ab218fe4ce2"
STAGING_REPORT_SHA = "7437c5c814574ea94ca8c2f9ec28066f965efbd8f8635db6277f015330e86f36"
PACKET_MANIFEST_SHA = "87ca97e402d845d4628f72d67c28e19b05674a23f3aa478be04221cecd5df0ff"
PACKET_CHECKER_SHA = "7cd90ad5ed7615d0470575957eb8f5ed44604a52ea42bab2f0b00e10ceabf040"
STATEMENT_SHA = "9cd8fe1533c99d9d2de9e351610da4b7843d156a523d97344032cf75e3953715"
PROOF_SHA = "adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9"
PREDECESSOR_MANIFEST_SHA = "e06616686dff546abe2e4e5269781273a8d9062f563fad10a618d2061044dea6"
PREDECESSOR_AUDIT_MANIFEST_SHA = "d4086f34593cdd1b02436efe9f8865b1f1b6049a87b5e11a9d9f8fc5d84b4fc3"
TEST_PYTHON_SHA = "4d4c42c0ebf9bf42e9aa2c0e56843632347a1f1c22d4a9f680b4f87fb241d0e6"

CHANGED = {
    "STAGING_REPORT.md": STAGING_REPORT_SHA,
    "check_release.py": STAGE_CHECKER_SHA,
    "run_static_model_long_smoke.py": RUNNER_SHA,
    "runtime/contract.md": CONTRACT_SHA,
    "tests/test_runtime.py": TESTS_SHA,
}


def require(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json(path: Path) -> Any:
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicates,
        parse_constant=lambda value: (_ for _ in ()).throw(
            ValueError(f"nonfinite JSON value: {value}")
        ),
    )


def manifest_rows(path: Path) -> dict[str, str]:
    raw = path.read_bytes()
    require(raw.endswith(b"\n"), f"manifest lacks final LF: {path}")
    rows: dict[str, str] = {}
    order: list[str] = []
    for line in raw.decode("utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        require(match is not None, f"malformed manifest row: {path}: {line!r}")
        digest, relative = match.groups()
        require(relative not in rows, f"duplicate manifest path: {path}: {relative}")
        require(not relative.startswith(("/", "../")), f"unsafe manifest path: {relative}")
        rows[relative] = digest
        order.append(relative)
    require(order == sorted(order), f"unsorted manifest: {path}")
    return rows


def actual_files(root: Path, *, exclude_manifest: bool = True) -> list[str]:
    result: list[str] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        info = path.lstat()
        require(not stat.S_ISLNK(info.st_mode), f"symlink in frozen tree: {root}: {relative}")
        require("__pycache__" not in path.parts, f"bytecode cache in frozen tree: {relative}")
        if stat.S_ISDIR(info.st_mode):
            continue
        require(stat.S_ISREG(info.st_mode), f"special file in frozen tree: {relative}")
        require(path.suffix not in {".pyc", ".pyo"}, f"bytecode in frozen tree: {relative}")
        if not (exclude_manifest and relative == "SHA256SUMS"):
            result.append(relative)
    return sorted(result)


def validate_manifest(root: Path, expected_sha: str) -> dict[str, str]:
    manifest = root / "SHA256SUMS"
    require(sha(manifest) == expected_sha, f"manifest digest mismatch: {root}")
    rows = manifest_rows(manifest)
    require(sorted(rows) == actual_files(root), f"manifest inventory mismatch: {root}")
    for relative, digest in rows.items():
        require(sha(root / relative) == digest, f"manifest row mismatch: {root}: {relative}")
    return rows


def fingerprint(root: Path) -> dict[str, str]:
    return {
        relative: sha(root / relative)
        for relative in actual_files(root, exclude_manifest=False)
    }


def import_module(name: str, path: Path):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def expect_failure(call: Callable[[], Any], contains: str | None = None) -> None:
    try:
        call()
    except (RuntimeError, ValueError, json.JSONDecodeError) as error:
        if contains is not None:
            require(contains in str(error), f"wrong failure mode: expected {contains!r}: {error}")
        return
    raise RuntimeError("hostile mutation was unexpectedly accepted")


def check_frozen_boundary() -> tuple[dict[str, str], dict[str, str]]:
    source_rows = validate_manifest(SOURCE, SOURCE_MANIFEST_SHA)
    require(source_rows["check_dossier.py"] == SOURCE_CHECKER_SHA, "source checker binding")
    require(source_rows["release_stage/SHA256SUMS"] == STAGE_MANIFEST_SHA,
            "source-to-stage manifest binding")
    require(source_rows["packet/SHA256SUMS"] == PACKET_MANIFEST_SHA,
            "source-to-packet manifest binding")
    stage_rows = validate_manifest(STAGE, STAGE_MANIFEST_SHA)
    packet_rows = validate_manifest(PACKET, PACKET_MANIFEST_SHA)
    require(len(stage_rows) == 44, "repaired release manifest row count")
    require(len(packet_rows) == 7, "packet manifest row count")
    require(stage_rows["check_release.py"] == STAGE_CHECKER_SHA, "release checker digest")
    require(stage_rows["run_static_model_long_smoke.py"] == RUNNER_SHA, "runner digest")
    require(packet_rows["check_packet.py"] == PACKET_CHECKER_SHA, "packet checker digest")
    require(packet_rows["PROPOSED_STATEMENT.tex"] == STATEMENT_SHA, "statement digest")
    require(packet_rows["PROOF.tex"] == PROOF_SHA, "proof digest")
    require(sha(TEST_PYTHON) == TEST_PYTHON_SHA, "verification Python digest")

    # Root applied the missing directory freeze after the independent audit
    # found the authored 0755 directories.  The authored files remain 0644,
    # which is itself a release-blocking failure of the claimed read-only
    # boundary.  Pin the exact post-freeze state that exposes the test-harness
    # incompatibility instead of silently repairing it here.
    file_modes: Counter[int] = Counter()
    directory_modes: Counter[int] = Counter()
    for path in [SOURCE, *SOURCE.rglob("*")]:
        info = path.lstat()
        mode = stat.S_IMODE(info.st_mode)
        if stat.S_ISDIR(info.st_mode):
            directory_modes[mode] += 1
        elif stat.S_ISREG(info.st_mode):
            file_modes[mode] += 1
    require(directory_modes == Counter({0o555: 7}),
            f"post-freeze directory modes changed: {directory_modes}")
    require(file_modes == Counter({0o644: 67}),
            f"authored writable-file defect changed: {file_modes}")
    for forbidden in ("STATIC_MODEL_LONG_SMOKE", "artifacts", "__pycache__", ".pytest_cache"):
        require(not any(path.name == forbidden for path in SOURCE.rglob("*")),
                f"forbidden cache/artifact path in source: {forbidden}")
    return stage_rows, packet_rows


def check_predecessor_preservation(new_rows: dict[str, str]) -> None:
    require(sha(PREDECESSOR_AUDIT / "SHA256SUMS") == PREDECESSOR_AUDIT_MANIFEST_SHA,
            "predecessor independent-audit binding")
    old_rows = validate_manifest(PREDECESSOR_STAGE, PREDECESSOR_MANIFEST_SHA)
    require(len(old_rows) == len(new_rows) == 44, "44-row predecessor boundary")
    require(set(old_rows) == set(new_rows), "release path inventory changed")
    changed = {relative for relative in old_rows if old_rows[relative] != new_rows[relative]}
    require(changed == set(CHANGED), f"unexpected substantive changes: {sorted(changed)}")
    require(all(new_rows[path] == digest for path, digest in CHANGED.items()),
            "changed-file digest mismatch")
    unchanged = set(new_rows) - changed
    require(len(unchanged) == 39, "39-row byte-preservation count")
    for relative in unchanged:
        require((STAGE / relative).read_bytes() == (PREDECESSOR_STAGE / relative).read_bytes(),
                f"protected predecessor byte drift: {relative}")
    sources = sorted(path for path in new_rows if path.startswith("runtime/sources/"))
    require(len(sources) == 31, "fixed-source count")
    require(all(path in unchanged for path in sources), "fixed-source byte drift")
    for path in (
        "runtime/release_pins.py",
        "runtime/hardened_service.py",
        "runtime/hardened_mcp.py",
        "runtime/canonical_reference.py",
        "runtime/model_catalog.gpt-5.6-sol.json",
        "runtime/memory_record.schema.json",
        "runtime/verification_output.schema.json",
        "static_model_smoke_mcp.py",
    ):
        require(path in unchanged, f"protected runtime/pin byte drift: {path}")
    require((PACKET / "PROPOSED_STATEMENT.tex").read_bytes()
            == (PREDECESSOR / "packet/PROPOSED_STATEMENT.tex").read_bytes(),
            "statement changed relative to predecessor")
    require((PACKET / "PROOF.tex").read_bytes()
            == (PREDECESSOR / "packet/PROOF.tex").read_bytes(),
            "proof changed relative to predecessor")
    require((PACKET / "SHA256SUMS").read_bytes()
            == (PREDECESSOR / "packet/SHA256SUMS").read_bytes(),
            "mathematical packet changed relative to predecessor")


def check_changed_code_contract(checker: Any, runner: Any) -> None:
    require(checker.STATE_WARNING.pattern == runner.STATE_WARNING.pattern,
            "state-warning regex differs between runner and checker")
    require(checker.SHELL_WARNING.pattern == runner.SHELL_WARNING.pattern,
            "shell-warning regex differs between runner and checker")
    require(checker.FORBIDDEN_DIAGNOSTIC_MARKERS == runner.FORBIDDEN_DIAGNOSTIC_MARKERS,
            "forbidden diagnostic set differs between runner and checker")
    require(checker.STATE_WARNING_LIMIT == runner.STATE_WARNING_LIMIT == 200,
            "state-warning bound weakened")
    require(checker.SHELL_WARNING_LIMIT == runner.SHELL_WARNING_LIMIT == 1,
            "shell-warning bound weakened")
    required_markers = {
        "codex_models_manager::manager", "failed to refresh available models",
        "models_cache.json", "model cache", "debug models", "credential",
        "authentication", "unauthorized", "not logged in", "access token",
        "api key", "failed to connect", "websocket", "tls handshake",
        "transport error",
    }
    require(required_markers <= set(checker.FORBIDDEN_DIAGNOSTIC_MARKERS),
            "cache/credential/transport marker gate weakened")
    source = (STAGE / "run_static_model_long_smoke.py").read_text(encoding="utf-8")
    require("stdout=stdout_handle" in source and "stderr=stderr_handle" in source,
            "stdout/stderr are not split")
    require("stderr=subprocess.STDOUT" not in source, "stderr remains merged")
    require("os.openpty()" in source and "stdin=stdin_slave_fd" in source,
            "dedicated PTY stdin is absent")
    require("if not os.isatty(stdin_slave_fd)" in source,
            "PTY terminal assertion is absent")
    require("process.poll()" in source and source.count("process.poll()") >= 4,
            "poll-around-scan and exit handling are absent")
    contract = (STAGE / "runtime/contract.md").read_text(encoding="utf-8")
    for phrase in (
        "Codex stdout is strict JSONL",
        "Codex stderr admits",
        "only two anchored",
        "dedicated no-input pseudo-terminal",
        "polls the Codex root both before and after",
        "terminal process observation",
    ):
        require(phrase in contract, f"contract omission: {phrase}")


def split_failed_evidence(checker: Any) -> tuple[str, str, dict[str, Any], list[Any]]:
    raw_path = SNAPSHOTS / "failed_merged_codex.log"
    require(sha(raw_path) == "68fad3795e6dba22226123c8c4540970a80d94b65a9f8810ca67f15ba8b7b360",
            "failed raw evidence digest")
    lines = raw_path.read_text(encoding="utf-8").splitlines()
    stdout_lines: list[str] = []
    stderr_lines: list[str] = []
    banner = 0
    state = 0
    shell = 0
    for line in lines:
        if line == "Reading additional input from stdin...":
            banner += 1
            continue
        if checker.STATE_WARNING.fullmatch(line):
            state += 1
            stderr_lines.append(line)
            continue
        if checker.SHELL_WARNING.fullmatch(line):
            shell += 1
            stderr_lines.append(line)
            continue
        value = json.loads(line, object_pairs_hook=reject_duplicates)
        require(isinstance(value, dict), "failed raw JSON record is not an object")
        stdout_lines.append(line)
    require((len(stdout_lines), state, shell, banner) == (7, 104, 1, 1),
            "failed raw evidence classification")
    receipt_path = SNAPSHOTS / "failed_receipt_v1.json"
    samples_path = SNAPSHOTS / "failed_process_samples_v1.json"
    require(sha(receipt_path) == "9b54171da78c6ed580b2ba1a1eb1d022f3559c10422685af8d06e8560ae4330c",
            "failed receipt evidence digest")
    require(sha(samples_path) == "e3458a20497ff7b8bf6bf72bdb8575a0bf1f56020e86ce9315c9862ce8947a23",
            "failed process evidence digest")
    receipt = strict_json(receipt_path)
    samples = strict_json(samples_path)
    return "\n".join(stdout_lines) + "\n", "\n".join(stderr_lines) + "\n", receipt, samples


def replay_failed_evidence(checker: Any, runner: Any) -> tuple[
    str, str, dict[str, Any], list[Any], datetime, datetime
]:
    stdout, stderr, receipt, samples = split_failed_evidence(checker)
    receipt = copy.deepcopy(receipt)
    receipt["stdout_forbidden_diagnostic_count"] = 0
    receipt["stderr_forbidden_diagnostic_count"] = 0
    receipt["stderr_warning_counts"] = {"state_db": 104, "shell_snapshot_cleanup": 1}
    receipt["live_process_sample_count"] = 22
    receipt["terminal_process_sample_count"] = 1
    receipt["root_pid"] = 86859
    receipt["stdin_strategy"] = "dedicated-pty-no-input"
    receipt["codex"] = {"path": checker.CODEX_PATH, "sha256": checker.CODEX_SHA256}
    receipt["mcp"]["python"] = checker.MCP_PYTHON_PATH
    receipt["command_without_prompt"] = checker.expected_smoke_command(receipt)
    mcp_started, mcp_completed = checker.validate_stdout_smoke(stdout, receipt)
    checker.validate_stderr_smoke(stderr, receipt)
    runner._parse_stdout_records(stdout.encode("utf-8"))
    runner._classify_stderr(
        stderr.encode("utf-8"),
        datetime.fromisoformat(receipt["started_at_utc"]),
        datetime.fromisoformat(receipt["completed_at_utc"]),
    )
    old_root = (
        "/Users/mingchen/Documents/ChatGPT/Yethlas/runtime/"
        "rethlas_hardened_v3_3_3_r5_p148_retry1_final_20260901"
    )
    for index, sample in enumerate(samples):
        sample["root_observation"] = (
            "live" if index < len(samples) - 1 else "exited_during_scan"
        )
        for row in sample["descendants"]:
            row["command"] = row["command"].replace(old_root, str(STAGE.resolve()))
    checker.validate_process_samples(samples, receipt, mcp_started, mcp_completed)
    return stdout, stderr, receipt, samples, mcp_started, mcp_completed


def run_hostile_mutations(checker: Any, runner: Any) -> int:
    stdout, stderr, receipt, samples, mcp_started, mcp_completed = replay_failed_evidence(
        checker, runner
    )
    checks = 0

    def hostile(call: Callable[[], Any], contains: str | None = None) -> None:
        nonlocal checks
        expect_failure(call, contains)
        checks += 1

    hostile(lambda: checker.validate_stdout_smoke(
        "Reading additional input from stdin...\n" + stdout, receipt
    ), "not strict JSON")
    hostile(lambda: checker.validate_stdout_smoke(
        stdout.replace("\n", "\n\n", 1), receipt
    ), "blank")
    hostile(lambda: checker.validate_stdout_smoke(stdout[:-1], receipt), "terminal LF")
    hostile(lambda: checker.validate_stdout_smoke(
        stdout.replace('{"type":"turn.started"}',
                       '{"type":"turn.started","type":"turn.started"}', 1), receipt
    ), "duplicate JSON key")
    hostile(lambda: checker.validate_stdout_smoke(
        stdout.replace('{"type":"turn.started"}',
                       '{"type":"turn.started","x":NaN}', 1), receipt
    ), "nonfinite JSON value")
    hostile(lambda: checker.validate_stdout_smoke(
        stdout.replace("\n", "\n" + stderr.splitlines()[0] + "\n", 1), receipt
    ), "not strict JSON")
    hostile(lambda: checker.validate_stderr_smoke(
        "Reading additional input from stdin...\n", {
            **receipt,
            "stderr_warning_counts": {"state_db": 0, "shell_snapshot_cleanup": 0},
        }
    ), "not an allowlisted warning")
    hostile(lambda: runner._classify_stderr(b"Reading additional input from stdin...\n"),
            "not an allowlisted warning")
    hostile(lambda: checker.validate_stderr_smoke(
        stderr.splitlines()[0] + " suffix\n", {
            **receipt,
            "stderr_warning_counts": {"state_db": 1, "shell_snapshot_cleanup": 0},
        }
    ), "not an allowlisted warning")
    shell_line = stderr.splitlines()[-1]
    hostile(lambda: checker.validate_stderr_smoke(
        shell_line.replace("/Users/mingchen/.codex/shell_snapshots/", "/private/tmp/") + "\n",
        {**receipt, "stderr_warning_counts": {"state_db": 0, "shell_snapshot_cleanup": 1}},
    ), "not an allowlisted warning")
    late_state = re.sub(
        r"^[^ ]+", (datetime.fromisoformat(receipt["started_at_utc"])
                     + timedelta(seconds=6)).isoformat().replace("+00:00", "Z"),
        stderr.splitlines()[0], count=1,
    )
    hostile(lambda: checker.validate_stderr_smoke(
        late_state + "\n",
        {**receipt, "stderr_warning_counts": {"state_db": 1, "shell_snapshot_cleanup": 0}},
    ), "outside the startup window")
    state_line = stderr.splitlines()[0]
    hostile(lambda: checker.validate_stderr_smoke(
        (state_line + "\n") * 201,
        {**receipt, "stderr_warning_counts": {"state_db": 201, "shell_snapshot_cleanup": 0}},
    ), "too many state-database")
    hostile(lambda: checker.validate_stderr_smoke(
        shell_line + "\n" + shell_line + "\n",
        {**receipt, "stderr_warning_counts": {"state_db": 0, "shell_snapshot_cleanup": 2}},
    ), "too many shell-snapshot")
    state_later = re.sub(
        r"^[^ ]+", (datetime.fromisoformat(receipt["started_at_utc"])
                     + timedelta(seconds=2)).isoformat().replace("+00:00", "Z"),
        state_line, count=1,
    )
    hostile(lambda: checker.validate_stderr_smoke(
        state_later + "\n" + state_line + "\n",
        {**receipt, "stderr_warning_counts": {"state_db": 2, "shell_snapshot_cleanup": 0}},
    ), "timestamps regress")
    hostile(lambda: checker.validate_stderr_smoke(
        "2026-09-01T16:11:53Z ERROR transport error: failed to connect to websocket\n",
        {**receipt, "stderr_forbidden_diagnostic_count": 3,
         "stderr_warning_counts": {"state_db": 0, "shell_snapshot_cleanup": 0}},
    ), "diagnostic count mismatch")
    hostile(lambda: checker.validate_stderr_smoke(
        "2026-09-01T16:11:53Z ERROR credential unavailable\n",
        {**receipt, "stderr_warning_counts": {"state_db": 0, "shell_snapshot_cleanup": 0}},
    ), "diagnostic count mismatch")
    hostile(lambda: checker.validate_stderr_smoke(
        state_line + "\n",
        {**receipt, "stderr_warning_counts": {"state_db": 0, "shell_snapshot_cleanup": 0}},
    ), "warning-count receipt mismatch")

    wrong = copy.deepcopy(samples)
    wrong[-1]["descendants"][0]["pid"] += 1
    hostile(lambda: checker.validate_process_samples(
        wrong, receipt, mcp_started, mcp_completed
    ), "terminal zombie PID mismatch")
    wrong = copy.deepcopy(samples)
    wrong[-1]["descendants"][0]["ppid"] += 1
    hostile(lambda: checker.validate_process_samples(
        wrong, receipt, mcp_started, mcp_completed
    ), "terminal zombie PPID mismatch")
    wrong = copy.deepcopy(samples)
    wrong[-1]["descendants"][0]["elapsed"] = "00:01"
    hostile(lambda: checker.validate_process_samples(
        wrong, receipt, mcp_started, mcp_completed
    ), "terminal zombie age")
    wrong = copy.deepcopy(samples)
    wrong[-1]["descendants"].append(copy.deepcopy(wrong[-2]["descendants"][1]))
    hostile(lambda: checker.validate_process_samples(
        wrong, receipt, mcp_started, mcp_completed
    ))
    wrong = copy.deepcopy(samples)
    wrong[0]["descendants"][0]["command"] += " --tamper"
    hostile(lambda: checker.validate_process_samples(
        wrong, receipt, mcp_started, mcp_completed
    ), "bound Codex root")
    wrong = copy.deepcopy(samples)
    wrong[10]["descendants"][1]["command"] = "/bin/evil"
    hostile(lambda: checker.validate_process_samples(
        wrong, receipt, mcp_started, mcp_completed
    ), "unexpected descendant command")

    horizon = mcp_started + timedelta(seconds=checker.SMOKE_CACHE_HORIZON_SECONDS)
    before = max(
        (i for i, sample in enumerate(samples)
         if datetime.fromisoformat(sample["sampled_at_utc"]) <= horizon),
        key=lambda i: datetime.fromisoformat(samples[i]["sampled_at_utc"]),
    )
    wrong = copy.deepcopy(samples)
    wrong[before]["descendants"] = [
        row for row in wrong[before]["descendants"]
        if row["pid"] == receipt["root_pid"]
        or "static_model_smoke_mcp.py" not in row["command"]
    ]
    hostile(lambda: checker.validate_process_samples(
        wrong, receipt, mcp_started, mcp_completed
    ), "pre-horizon")
    wrong = copy.deepcopy(samples)
    wrong[before]["descendants"] = [
        row for row in wrong[before]["descendants"]
        if "codex-code-mode-host" not in row["command"]
    ]
    hostile(lambda: checker.validate_process_samples(
        wrong, receipt, mcp_started, mcp_completed
    ), "pre-horizon")
    hostile(lambda: checker.validate_cache_horizon_bracketing(
        [horizon - timedelta(seconds=2), mcp_completed - timedelta(seconds=1)],
        [{"codex", "mcp-python", "code-mode-host"}, set()],
        ["live", "exited_during_scan"],
        mcp_started, mcp_completed,
    ), "does not follow horizon-crossing")
    hostile(lambda: checker.validate_cache_horizon_bracketing(
        [horizon - timedelta(seconds=2), mcp_completed + timedelta(seconds=1)],
        [{"codex", "mcp-python", "code-mode-host"}, {"codex"}],
        ["live", "exited_during_scan"],
        mcp_started, mcp_completed,
    ), "partial process roles")
    wrong = copy.deepcopy(samples)
    wrong.append(copy.deepcopy(wrong[-2]))
    wrong[-1]["sampled_at_utc"] = receipt["completed_at_utc"]
    wrong[-1]["elapsed_seconds"] = receipt["elapsed_seconds"]
    wrong_receipt = {**receipt, "process_sample_count": len(wrong),
                     "live_process_sample_count": receipt["live_process_sample_count"] + 1}
    hostile(lambda: checker.validate_process_samples(
        wrong, wrong_receipt, mcp_started, mcp_completed
    ), "terminal process observation is not final")

    require(checks == 28, f"hostile mutation count mismatch: {checks}")
    return checks


def run_frozen_checker(path: Path, cwd: Path, timeout: int = 180) -> str:
    completed = subprocess.run(
        [sys.executable, "-B", str(path)],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    require(completed.returncode == 0,
            f"frozen checker failed: {path}:\n{completed.stdout}\n{completed.stderr}")
    return completed.stdout.strip()


EXPECTED_READONLY_FAILURES = {
    "test_extra_source_is_rejected_pre_start",
    "test_mcp_independently_rejects_mutated_source_before_server_start",
    "test_mcp_independently_rejects_mutated_static_catalog_before_server_start",
    "test_missing_source_is_rejected_pre_start",
    "test_static_catalog_mutation_and_missing_file_fail_closed_pre_start",
    "test_symlinked_source_is_rejected_pre_start",
}


def require_expected_readonly_test_failure(completed: subprocess.CompletedProcess[str],
                                           label: str) -> float:
    output = completed.stdout + "\n" + completed.stderr
    match = re.search(r"Ran 158 tests in ([0-9.]+)s", output)
    failures = set(re.findall(r"^ERROR: ([^ ]+) ", output, flags=re.MULTILINE))
    require(completed.returncode == 1, f"{label} did not fail with exit 1")
    require(match is not None, f"{label} lacks 158-test timing")
    require("FAILED (errors=6)" in output, f"{label} lacks exact six-error summary")
    require(failures == EXPECTED_READONLY_FAILURES,
            f"{label} failure inventory changed: {sorted(failures)}")
    require(output.count("PermissionError: [Errno 13] Permission denied:") == 6,
            f"{label} does not contain six permission failures")
    return float(match.group(1))


def run_test_suite_twice() -> list[float]:
    times: list[float] = []
    for index in range(2):
        completed = subprocess.run(
            [str(TEST_PYTHON), "-B", "-m", "unittest", "discover", "-s", "tests"],
            cwd=STAGE,
            capture_output=True,
            text=True,
            timeout=240,
            check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        times.append(require_expected_readonly_test_failure(
            completed, f"independent read-only test run {index + 1}"
        ))
    return times


def check_audit_ledgers() -> None:
    result = strict_json(HERE / "AUDIT_RESULT.json")
    require(result.get("verdict") == "FAIL_NOT_READY_FOR_FINAL_PATH_SMOKE",
            "audit result verdict")
    require(result.get("binary_pass") is False, "audit result binary flag")
    require(result.get("source_manifest_sha256") == SOURCE_MANIFEST_SHA,
            "audit result source binding")
    require(result.get("release_stage_manifest_sha256") == STAGE_MANIFEST_SHA,
            "audit result stage binding")
    require(result.get("blocking_defects") and len(result["blocking_defects"]) == 2,
            "audit result blocker inventory")
    require(result.get("post_freeze_error_count") == 6,
            "audit result error count")
    require(result.get("independent_hostile_mutations_rejected") == 28,
            "audit result hostile count")
    require(result.get("authorized_next_actions") == {
        "repair_sibling": True,
        "final_install": False,
        "smoke": False,
        "production_submit": False,
        "live_integration": False,
        "p148_retirement": False,
    }, "audit result authorization boundary")

    tests = strict_json(HERE / "TEST_RUNS.json")
    require(tests.get("test_python_sha256") == TEST_PYTHON_SHA,
            "test ledger Python binding")
    require(tests.get("test_inventory") == 158, "test ledger inventory")
    require({item["result"] for item in tests["pre_directory_freeze_nonadmissible_runs"]}
            == {"OK_ON_WRITABLE_0755_DIRECTORIES"},
            "test ledger pre-freeze classification")
    require({item["result"] for item in tests["post_directory_freeze_direct_runs"]}
            == {"FAILED_ERRORS_6"}, "test ledger direct failure classification")
    require({item["result"] for item in tests["post_directory_freeze_checker_runs"]}
            == {"FAILED_ERRORS_6"}, "test ledger checker failure classification")
    require(set(tests.get("exact_error_tests", [])) == EXPECTED_READONLY_FAILURES,
            "test ledger exact failure inventory")

    modes = strict_json(HERE / "MODE_OBSERVATIONS.json")
    require(modes["authored_pre_freeze_observation"] == {
        "directories": {"count": 7, "mode_octal": "0755"},
        "regular_files": {"count": 67, "mode_octal": "0644"},
        "read_only_claim_valid": False,
    }, "pre-freeze mode ledger")
    require(modes["post_directory_freeze_observation"] == {
        "directories": {"count": 7, "mode_octal": "0555"},
        "regular_files": {"count": 67, "mode_octal": "0644"},
        "fully_read_only": False,
    }, "post-freeze mode ledger")
    report = (HERE / "REPORT.md").read_text(encoding="utf-8")
    for phrase in (
        "FAIL_NOT_READY_FOR_FINAL_PATH_SMOKE",
        "Blocking defect 1",
        "Blocking defect 2",
        "Required sibling repair",
        "No final path may be installed",
    ):
        require(phrase in report, f"audit report omission: {phrase}")


def check_own_manifest() -> None:
    manifest = HERE / "SHA256SUMS"
    rows = manifest_rows(manifest)
    require(sorted(rows) == actual_files(HERE), "audit dossier manifest inventory")
    for relative, digest in rows.items():
        require(sha(HERE / relative) == digest,
                f"audit dossier manifest row: {relative}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-tests", action="store_true")
    parser.add_argument("--run-authored-checker", action="store_true")
    args = parser.parse_args()

    before = fingerprint(SOURCE)
    stage_rows, _ = check_frozen_boundary()
    check_predecessor_preservation(stage_rows)
    checker = import_module("p148_infra_audited_release_checker", STAGE / "check_release.py")
    runner = import_module("p148_infra_audited_smoke_runner", STAGE / "run_static_model_long_smoke.py")
    checker.check_manifest()
    checker.check_catalog()
    checker.check_release_pins()
    checker.check_code_contract()
    check_changed_code_contract(checker, runner)
    hostile_checks = run_hostile_mutations(checker, runner)
    check_audit_ledgers()
    check_own_manifest()
    packet_output = run_frozen_checker(PACKET / "check_packet.py", PACKET)
    require("PASS_AUTHORED_NONCIRCULAR_DEPENDENCY_PACKET_V3" in packet_output,
            "packet checker verdict")
    test_times: list[float] = []
    if args.run_tests:
        test_times = run_test_suite_twice()
    authored_output = None
    if args.run_authored_checker:
        completed = subprocess.run(
            [sys.executable, "-B", str(SOURCE / "check_dossier.py")],
            cwd=SOURCE,
            capture_output=True,
            text=True,
            timeout=360,
            check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        authored_output = completed.stdout + "\n" + completed.stderr
        require_expected_readonly_test_failure(completed, "authored top checker")
        require("158-test pass 1 failed" in authored_output,
                "authored top checker did not propagate the test failure")
    require(fingerprint(SOURCE) == before, "source dossier mutated during independent audit")
    print("PASS_FROZEN_P148_SMOKE_INFRASTRUCTURE_INDEPENDENT_FAIL_DOSSIER")
    print(json.dumps({
        "candidate_verdict": "FAIL",
        "hostile_mutations_rejected": hostile_checks,
        "tests": 158 if args.run_tests else 0,
        "test_seconds": test_times,
        "authored_checker_rerun": bool(args.run_authored_checker),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
