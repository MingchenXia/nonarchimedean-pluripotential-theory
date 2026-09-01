from __future__ import annotations

import ast
import copy
from collections import Counter
from datetime import datetime, timedelta, timezone
import importlib.util
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))
SPEC = importlib.util.spec_from_file_location(
    "hardened_service_v332", ROOT / "runtime" / "hardened_service.py"
)
assert SPEC is not None and SPEC.loader is not None
SERVICE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SERVICE)


def load_local_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SMOKE_RUNNER = load_local_module(
    "p148_smoke_runner", ROOT / "run_static_model_long_smoke.py"
)
RELEASE_CHECKER = load_local_module(
    "p148_release_checker", ROOT / "check_release.py"
)

from canonical_reference import canonicalize_external_reference_record


def mcp_item(
    event: str,
    item_id: str,
    tool: str,
    *,
    arguments=None,
    error=None,
    result=None,
    status=None,
):
    if status is None:
        status = "in_progress" if event == "item.started" else "completed"
    return {
        "type": event,
        "item": {
            "id": item_id,
            "type": "mcp_tool_call",
            "server": "verification_agent",
            "tool": tool,
            "arguments": {} if arguments is None else arguments,
            "status": status,
            "error": error,
            "result": result,
        },
    }


def completed_mcp_pair(item_id: str, tool: str, arguments, structured_content):
    result = {
        "content": [
            {
                "type": "text",
                "text": json.dumps(structured_content, ensure_ascii=False),
            }
        ],
        "structured_content": structured_content,
    }
    return [
        mcp_item(
            "item.started", item_id, tool, arguments=arguments, result=None
        ),
        mcp_item(
            "item.completed",
            item_id,
            tool,
            arguments=arguments,
            result=result,
        ),
    ]


def clean_transcript():
    usage = {
        "input_tokens": 0,
        "cached_input_tokens": 0,
        "cache_write_input_tokens": 0,
        "output_tokens": 0,
        "reasoning_output_tokens": 0,
    }
    return [
        {"type": "thread.started", "thread_id": "thread"},
        {"type": "turn.started"},
        *completed_mcp_pair("init", "memory_init", {}, {"status": "ok"}),
        *completed_mcp_pair(
            "write", "write_verification_output", {}, {"status": "ok"}
        ),
        {"type": "turn.completed", "usage": usage},
    ]


EXACT_DIAGNOSTIC = (
    "Exceeded skills context budget. All skill descriptions were removed and "
    "33 additional skills were not included in the model-visible skills list."
)
EXACT_RAW_DIAGNOSTIC = (
    "2026-08-31T23:50:25.884322Z ERROR "
    "codex_api::endpoint::responses_websocket: failed to connect to websocket: "
    "IO error: tls handshake eof, url: "
    "wss://chatgpt.com/backend-api/codex/responses"
)


def parse_raw_lines(lines):
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "codex.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return SERVICE._parse_jsonl_log(path)


def parse_raw_bytes(value):
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "codex.jsonl"
        path.write_bytes(value)
        return SERVICE._parse_jsonl_log(path)


class RawDiagnosticGateTests(unittest.TestCase):
    def test_exact_pre_mcp_diagnostic_is_recorded(self):
        records, invalid, allowed = parse_raw_lines([EXACT_RAW_DIAGNOSTIC])
        self.assertEqual(records, [])
        self.assertEqual(invalid, [])
        self.assertEqual(len(allowed), 1)
        self.assertEqual(allowed[0]["message"], EXACT_RAW_DIAGNOSTIC)

    def test_raw_diagnostic_suffix_is_rejected(self):
        _, invalid, allowed = parse_raw_lines([EXACT_RAW_DIAGNOSTIC + " suffix"])
        self.assertTrue(invalid)
        self.assertEqual(allowed, [])

    def test_raw_diagnostic_prefix_only_is_rejected(self):
        _, invalid, allowed = parse_raw_lines(
            ["ERROR codex_api::endpoint::responses_websocket: failed to connect"]
        )
        self.assertTrue(invalid)
        self.assertEqual(allowed, [])

    def test_duplicate_raw_diagnostic_is_rejected(self):
        _, invalid, allowed = parse_raw_lines(
            [EXACT_RAW_DIAGNOSTIC, EXACT_RAW_DIAGNOSTIC]
        )
        self.assertEqual(len(allowed), 1)
        self.assertTrue(invalid)

    def test_raw_diagnostic_after_mcp_is_rejected(self):
        mcp_start = mcp_item("item.started", "init", "memory_init")
        _, invalid, allowed = parse_raw_lines(
            [json.dumps(mcp_start), EXACT_RAW_DIAGNOSTIC]
        )
        self.assertTrue(invalid)
        self.assertEqual(allowed, [])

    def test_recursive_duplicate_key_is_rejected(self):
        raw = '{"type":"thread.started","thread_id":"one","nested":{"x":1,"x":2}}'
        _, invalid, allowed = parse_raw_lines([raw])
        self.assertTrue(invalid)
        self.assertEqual(allowed, [])

    def test_invalid_utf8_is_rejected_without_replacement(self):
        records, invalid, allowed = parse_raw_bytes(b'{"type":"thread.started"}\xff\n')
        self.assertEqual(records, [])
        self.assertTrue(any("invalid UTF-8" in item for item in invalid))
        self.assertEqual(allowed, [])

    def test_blank_lf_line_is_rejected(self):
        _, invalid, _ = parse_raw_bytes(b"\n")
        self.assertTrue(any("blank or whitespace-only" in item for item in invalid))

    def test_blank_crlf_line_is_rejected(self):
        _, invalid, _ = parse_raw_bytes(b"\r\n")
        self.assertTrue(any("blank or whitespace-only" in item for item in invalid))

    def test_whitespace_only_line_is_rejected(self):
        _, invalid, _ = parse_raw_bytes(b" \t \n")
        self.assertTrue(any("blank or whitespace-only" in item for item in invalid))

    def test_unterminated_final_line_is_rejected(self):
        _, invalid, _ = parse_raw_bytes(b'{"type":"thread.started","thread_id":"t"}')
        self.assertTrue(any("missing terminal LF" in item for item in invalid))

    def test_crlf_json_record_is_accepted(self):
        records, invalid, _ = parse_raw_bytes(
            b'{"type":"thread.started","thread_id":"t"}\r\n'
        )
        self.assertEqual(invalid, [])
        self.assertEqual(records[0]["thread_id"], "t")


SMOKE_BASE = datetime(2026, 9, 1, tzinfo=timezone.utc)


def smoke_iso(seconds):
    return (SMOKE_BASE + timedelta(seconds=seconds)).isoformat()


def strict_smoke_stdout_fixture():
    structured = {
        "status": "ok",
        "requested_seconds": 310,
        "elapsed_seconds": 310.0,
        "started_at_utc": smoke_iso(18),
        "completed_at_utc": smoke_iso(328),
    }
    result = {
        "content": [
            {
                "type": "text",
                "text": json.dumps(structured, separators=(",", ":")),
            }
        ],
        "structured_content": structured,
    }
    records = [
        {"type": "thread.started", "thread_id": "thread"},
        {"type": "turn.started"},
        {
            "type": "item.started",
            "item": {
                "id": "call",
                "type": "mcp_tool_call",
                "server": "ttl_smoke",
                "tool": "wait_across_catalog_ttl",
                "arguments": {"seconds": 310},
                "result": None,
                "error": None,
                "status": "in_progress",
            },
        },
        {
            "type": "item.completed",
            "item": {
                "id": "call",
                "type": "mcp_tool_call",
                "server": "ttl_smoke",
                "tool": "wait_across_catalog_ttl",
                "arguments": {"seconds": 310},
                "result": result,
                "error": None,
                "status": "completed",
            },
        },
        {
            "type": "item.completed",
            "item": {
                "id": "message",
                "type": "agent_message",
                "text": "STATIC_MODEL_SMOKE_OK",
            },
        },
        {"type": "turn.completed", "usage": {}},
    ]
    stdout = "".join(json.dumps(record, separators=(",", ":")) + "\n" for record in records)
    receipt = {
        "started_at_utc": smoke_iso(0),
        "completed_at_utc": smoke_iso(345),
        "elapsed_seconds": 345.0,
        "stdout_forbidden_diagnostic_count": 0,
    }
    return stdout, receipt


def state_db_warning(seconds=1):
    timestamp = (SMOKE_BASE + timedelta(seconds=seconds)).strftime(
        "%Y-%m-%dT%H:%M:%S.%fZ"
    )
    return (
        f"{timestamp}  WARN codex_rollout::list: state db discrepancy during "
        "find_thread_path_by_id_str_in_subdir: falling_back"
    )


def shell_snapshot_warning(seconds=340):
    timestamp = (SMOKE_BASE + timedelta(seconds=seconds)).strftime(
        "%Y-%m-%dT%H:%M:%S.%fZ"
    )
    return (
        f'{timestamp}  WARN codex_core::shell_snapshot: Failed to delete shell '
        'snapshot at AbsolutePathBuf("/Users/mingchen/.codex/shell_snapshots/'
        '01a05dbd-c4cf-7b12-ab1a-3a4fcf9207ec.1788279112915432000.sh"): '
        'Os { code: 2, kind: NotFound, message: "No such file or directory" }'
    )


def stderr_receipt(state_count, shell_count):
    return {
        "started_at_utc": smoke_iso(0),
        "completed_at_utc": smoke_iso(345),
        "stderr_forbidden_diagnostic_count": 0,
        "stderr_warning_counts": {
            "state_db": state_count,
            "shell_snapshot_cleanup": shell_count,
        },
    }


class SplitSmokeLogGateTests(unittest.TestCase):
    def test_separated_jsonl_and_known_stderr_warnings_pass(self):
        stdout, receipt = strict_smoke_stdout_fixture()
        started, completed = RELEASE_CHECKER.validate_stdout_smoke(stdout, receipt)
        self.assertEqual((completed - started).total_seconds(), 310)
        stderr = state_db_warning() + "\n" + shell_snapshot_warning() + "\n"
        RELEASE_CHECKER.validate_stderr_smoke(stderr, stderr_receipt(1, 1))

    def test_runner_accepts_only_the_split_fixture(self):
        stdout, _ = strict_smoke_stdout_fixture()
        records = SMOKE_RUNNER._parse_stdout_records(stdout.encode("utf-8"))
        self.assertEqual(len(records), 6)
        stderr = state_db_warning() + "\n" + shell_snapshot_warning() + "\n"
        self.assertEqual(
            SMOKE_RUNNER._classify_stderr(stderr.encode("utf-8")),
            {"state_db": 1, "shell_snapshot_cleanup": 1},
        )

    def test_state_warning_interleaved_into_stdout_fails(self):
        stdout, receipt = strict_smoke_stdout_fixture()
        lines = stdout.splitlines()
        lines.insert(2, state_db_warning())
        with self.assertRaisesRegex(RuntimeError, "stdout line 3 is not strict JSON"):
            RELEASE_CHECKER.validate_stdout_smoke("\n".join(lines) + "\n", receipt)

    def test_runner_rejects_state_warning_interleaved_into_stdout(self):
        stdout, _ = strict_smoke_stdout_fixture()
        lines = stdout.splitlines()
        lines.insert(2, state_db_warning())
        with self.assertRaisesRegex(RuntimeError, "stdout line 3 is not strict JSON"):
            SMOKE_RUNNER._parse_stdout_records(
                ("\n".join(lines) + "\n").encode("utf-8")
            )

    def test_stderr_warning_suffix_fails(self):
        with self.assertRaisesRegex(RuntimeError, "not an allowlisted warning"):
            RELEASE_CHECKER.validate_stderr_smoke(
                state_db_warning() + " suffix\n", stderr_receipt(1, 0)
            )

    def test_transport_stderr_fails(self):
        value = (
            "2026-09-01T00:00:01.000000Z ERROR transport error: "
            "failed to connect to websocket\n"
        )
        receipt = stderr_receipt(0, 0)
        receipt["stderr_forbidden_diagnostic_count"] = 3
        with self.assertRaisesRegex(RuntimeError, "diagnostic count mismatch"):
            RELEASE_CHECKER.validate_stderr_smoke(value, receipt)

    def test_runner_rejects_transport_stderr(self):
        value = b"2026-09-01T00:00:01.000000Z ERROR transport error\n"
        with self.assertRaisesRegex(RuntimeError, "not an allowlisted warning"):
            SMOKE_RUNNER._classify_stderr(value)

    def test_credential_stderr_fails_even_with_zero_receipt_count(self):
        value = "2026-09-01T00:00:01.000000Z ERROR credential unavailable\n"
        with self.assertRaisesRegex(RuntimeError, "diagnostic count mismatch"):
            RELEASE_CHECKER.validate_stderr_smoke(value, stderr_receipt(0, 0))

    def test_shell_snapshot_path_escape_fails(self):
        value = shell_snapshot_warning().replace(
            "/Users/mingchen/.codex/shell_snapshots/", "/private/tmp/"
        )
        with self.assertRaisesRegex(RuntimeError, "not an allowlisted warning"):
            RELEASE_CHECKER.validate_stderr_smoke(value + "\n", stderr_receipt(0, 1))

    def test_state_warning_outside_startup_window_fails(self):
        with self.assertRaisesRegex(RuntimeError, "outside the startup window"):
            RELEASE_CHECKER.validate_stderr_smoke(
                state_db_warning(6) + "\n", stderr_receipt(1, 0)
            )

    def test_runner_state_warning_outside_startup_window_fails(self):
        with self.assertRaisesRegex(RuntimeError, "outside startup"):
            SMOKE_RUNNER._classify_stderr(
                (state_db_warning(6) + "\n").encode("utf-8"),
                SMOKE_BASE,
                SMOKE_BASE + timedelta(seconds=345),
            )

    def test_stderr_receipt_count_mismatch_fails(self):
        with self.assertRaisesRegex(RuntimeError, "warning-count receipt mismatch"):
            RELEASE_CHECKER.validate_stderr_smoke(
                state_db_warning() + "\n", stderr_receipt(0, 0)
            )

    def test_exact_optional_stdin_banner_is_not_allowlisted_by_checker(self):
        banner = "Reading additional input from stdin...\n"
        with self.assertRaisesRegex(RuntimeError, "not an allowlisted warning"):
            RELEASE_CHECKER.validate_stderr_smoke(banner, stderr_receipt(0, 0))

    def test_exact_optional_stdin_banner_is_not_allowlisted_by_runner(self):
        banner = b"Reading additional input from stdin...\n"
        with self.assertRaisesRegex(RuntimeError, "not an allowlisted warning"):
            SMOKE_RUNNER._classify_stderr(banner)


class FakePolledProcess:
    def __init__(self, values, pid=42):
        self.values = list(values)
        self.pid = pid

    def poll(self):
        return self.values.pop(0)


def process_elapsed_text(seconds):
    minutes, remainder = divmod(int(seconds), 60)
    return f"{minutes:02d}:{remainder:02d}"


def terminal_race_process_fixture():
    receipt = {
        "started_at_utc": smoke_iso(0),
        "completed_at_utc": smoke_iso(345),
        "elapsed_seconds": 345.0,
        "process_sample_count": 23,
        "live_process_sample_count": 22,
        "terminal_process_sample_count": 1,
        "root_pid": 42,
        "codex": {
            "path": RELEASE_CHECKER.CODEX_PATH,
            "sha256": RELEASE_CHECKER.CODEX_SHA256,
        },
        "mcp": {"python": RELEASE_CHECKER.MCP_PYTHON_PATH},
    }
    command = RELEASE_CHECKER.expected_smoke_command(receipt)
    receipt["command_without_prompt"] = command
    root_command = " ".join(command + [RELEASE_CHECKER.SMOKE_PROMPT])
    mcp_command = (
        f"{RELEASE_CHECKER.MCP_PYTHON_PATH} -B "
        f"{(ROOT / 'static_model_smoke_mcp.py').resolve()}"
    )
    host_command = str(
        Path(RELEASE_CHECKER.CODEX_PATH).with_name("codex-code-mode-host")
    )
    samples = []
    for index in range(22):
        elapsed = 0.1 + 15 * index
        descendants = [
            {
                "pid": 42,
                "ppid": 1,
                "elapsed": process_elapsed_text(elapsed),
                "command": root_command,
            }
        ]
        if index >= 1:
            descendants.append(
                {
                    "pid": 43,
                    "ppid": 42,
                    "elapsed": process_elapsed_text(elapsed - 10),
                    "command": mcp_command,
                }
            )
        if index >= 2:
            descendants.append(
                {
                    "pid": 44,
                    "ppid": 42,
                    "elapsed": process_elapsed_text(elapsed - 20),
                    "command": host_command,
                }
            )
        samples.append(
            {
                "sampled_at_utc": smoke_iso(elapsed),
                "elapsed_seconds": elapsed,
                "descendants": descendants,
                "sampling_error": None,
                "root_observation": "live",
            }
        )
    terminal_elapsed = 330.1
    samples.append(
        {
            "sampled_at_utc": smoke_iso(terminal_elapsed),
            "elapsed_seconds": terminal_elapsed,
            "descendants": [
                {
                    "pid": 42,
                    "ppid": 1,
                    "elapsed": process_elapsed_text(terminal_elapsed),
                    "command": "(codex)",
                }
            ],
            "sampling_error": None,
            "root_observation": "exited_during_scan",
        }
    )
    return receipt, samples


class SmokeProcessObservationTests(unittest.TestCase):
    def test_runner_uses_dedicated_terminal_stdin_and_split_streams(self):
        source = (ROOT / "run_static_model_long_smoke.py").read_text(encoding="utf-8")
        self.assertIn("os.openpty()", source)
        self.assertIn("stdin=stdin_slave_fd", source)
        self.assertIn("stdout=stdout_handle", source)
        self.assertIn("stderr=stderr_handle", source)
        self.assertNotIn("stderr=subprocess.STDOUT", source)

    def test_dedicated_stdin_pty_slave_is_a_terminal(self):
        master_fd, slave_fd = os.openpty()
        try:
            self.assertTrue(os.isatty(slave_fd))
        finally:
            os.close(slave_fd)
            os.close(master_fd)

    def test_live_observation_polls_around_scan(self):
        process = FakePolledProcess([None, None])
        state, descendants = SMOKE_RUNNER._observe_process(
            process, lambda pid: [{"pid": pid}]
        )
        self.assertEqual(state, "live")
        self.assertEqual(descendants, [{"pid": 42}])

    def test_exit_between_poll_and_ps_is_terminal_not_identity_drift(self):
        zombie = [{"pid": 42, "ppid": 1, "elapsed": "05:30", "command": "(codex)"}]
        process = FakePolledProcess([None, 0])
        state, descendants = SMOKE_RUNNER._observe_process(
            process, lambda pid: zombie
        )
        self.assertEqual(state, "exited_during_scan")
        self.assertEqual(descendants, zombie)

    def test_exit_before_scan_does_not_call_ps(self):
        process = FakePolledProcess([0])

        def forbidden_scan(_):
            raise AssertionError("scanner called after process exit")

        state, descendants = SMOKE_RUNNER._observe_process(process, forbidden_scan)
        self.assertEqual((state, descendants), ("exited_before_scan", []))

    def test_terminal_horizon_bridge_after_mcp_completion_passes(self):
        mcp_started = SMOKE_BASE + timedelta(seconds=18)
        mcp_completed = SMOKE_BASE + timedelta(seconds=328)
        timestamps = [
            SMOKE_BASE + timedelta(seconds=316),
            SMOKE_BASE + timedelta(seconds=331),
        ]
        roles = [
            {"codex", "mcp-python", "code-mode-host"},
            set(),
        ]
        observations = ["live", "exited_during_scan"]
        RELEASE_CHECKER.validate_cache_horizon_bracketing(
            timestamps, roles, observations, mcp_started, mcp_completed
        )

    def test_terminal_horizon_bridge_before_mcp_completion_fails(self):
        mcp_started = SMOKE_BASE + timedelta(seconds=18)
        mcp_completed = SMOKE_BASE + timedelta(seconds=328)
        timestamps = [
            SMOKE_BASE + timedelta(seconds=316),
            SMOKE_BASE + timedelta(seconds=325),
        ]
        with self.assertRaisesRegex(RuntimeError, "does not follow horizon-crossing"):
            RELEASE_CHECKER.validate_cache_horizon_bracketing(
                timestamps,
                [{"codex", "mcp-python", "code-mode-host"}, set()],
                ["live", "exited_during_scan"],
                mcp_started,
                mcp_completed,
            )

    def test_full_process_validator_accepts_bound_terminal_zombie(self):
        receipt, samples = terminal_race_process_fixture()
        RELEASE_CHECKER.validate_process_samples(
            samples,
            receipt,
            SMOKE_BASE + timedelta(seconds=18),
            SMOKE_BASE + timedelta(seconds=328),
        )

    def test_full_process_validator_rejects_unbound_terminal_zombie(self):
        receipt, samples = terminal_race_process_fixture()
        samples[-1]["descendants"][0]["pid"] = 99
        with self.assertRaisesRegex(RuntimeError, "terminal zombie PID mismatch"):
            RELEASE_CHECKER.validate_process_samples(
                samples,
                receipt,
                SMOKE_BASE + timedelta(seconds=18),
                SMOKE_BASE + timedelta(seconds=328),
            )


class TranscriptGateTests(unittest.TestCase):
    def test_clean_transcript(self):
        evidence = SERVICE._tool_evidence(clean_transcript())
        self.assertEqual(evidence["structural_errors"], [])
        self.assertEqual(evidence["suspicious_tool_records"], [])

    def test_exact_diagnostic_is_the_only_allowed_shape(self):
        records = clean_transcript()
        records.insert(
            2,
            {
                "type": "item.completed",
                "item": {"id": "diagnostic", "type": "error", "message": EXACT_DIAGNOSTIC},
            },
        )
        evidence = SERVICE._tool_evidence(records)
        self.assertEqual(evidence["structural_errors"], [])
        self.assertEqual(len(evidence["allowed_diagnostics"]), 1)

    def test_diagnostic_suffix_is_rejected(self):
        records = clean_transcript()
        records.insert(
            2,
            {
                "type": "item.completed",
                "item": {
                    "id": "diagnostic",
                    "type": "error",
                    "message": EXACT_DIAGNOSTIC + " fatal suffix",
                },
            },
        )
        self.assertTrue(SERVICE._tool_evidence(records)["structural_errors"])

    def test_prefix_only_is_rejected(self):
        records = clean_transcript()
        records.insert(
            2,
            {
                "type": "item.completed",
                "item": {
                    "id": "diagnostic",
                    "type": "error",
                    "message": "Exceeded skills context budget.",
                },
            },
        )
        self.assertTrue(SERVICE._tool_evidence(records)["structural_errors"])

    def test_wrong_diagnostic_event_is_rejected(self):
        records = clean_transcript()
        records.insert(
            2,
            {
                "type": "item.started",
                "item": {"id": "diagnostic", "type": "error", "message": EXACT_DIAGNOSTIC},
            },
        )
        self.assertTrue(SERVICE._tool_evidence(records)["structural_errors"])

    def test_duplicate_diagnostics_are_rejected(self):
        records = clean_transcript()
        diagnostic = {
            "type": "item.completed",
            "item": {"id": "diagnostic", "type": "error", "message": EXACT_DIAGNOSTIC},
        }
        records[2:2] = [diagnostic, diagnostic]
        self.assertTrue(SERVICE._tool_evidence(records)["structural_errors"])

    def test_non_mcp_operation_is_rejected(self):
        records = clean_transcript()
        records.insert(
            4,
            {
                "type": "item.started",
                "item": {"id": "shell", "type": "command_execution", "command": "touch x"},
            },
        )
        self.assertTrue(SERVICE._tool_evidence(records)["suspicious_tool_records"])

    def test_failed_call_before_init_is_rejected(self):
        records = clean_transcript()
        records[2:2] = [
            mcp_item("item.started", "early", "memory_query"),
            mcp_item(
                "item.completed",
                "early",
                "memory_query",
                error={"message": "not initialized"},
                status="failed",
            ),
        ]
        evidence = SERVICE._tool_evidence(records)
        self.assertTrue(evidence["structural_errors"])
        self.assertNotEqual(evidence["operation_started_sequence"][0], "memory_init")

    def test_canonical_reference_append_is_allowlisted(self):
        records = clean_transcript()
        records[4:4] = completed_mcp_pair(
            "reference", "memory_append_reference", {}, {"status": "ok"}
        )
        evidence = SERVICE._tool_evidence(records)
        self.assertEqual(evidence["structural_errors"], [])
        self.assertEqual(evidence["suspicious_tool_records"], [])
        self.assertIn("memory_append_reference", SERVICE.ALLOWED_MCP_TOOLS)

    def test_unlisted_reference_append_name_is_rejected(self):
        records = clean_transcript()
        records[4:4] = [
            mcp_item("item.started", "reference", "memory_append_reference_raw"),
            mcp_item("item.completed", "reference", "memory_append_reference_raw"),
        ]
        self.assertTrue(
            SERVICE._tool_evidence(records)["suspicious_tool_records"]
        )

    def test_completed_call_arguments_must_equal_started_arguments(self):
        structured = {"status": "ok"}
        records = completed_mcp_pair(
            "call", "memory_init", {"run_id": "one"}, structured
        )
        records[1]["item"]["arguments"] = {"run_id": "two"}
        _, errors = SERVICE._completed_mcp_calls(records)
        self.assertTrue(any("arguments changed" in error for error in errors))

    def test_boolean_and_integer_arguments_are_not_exactly_equal(self):
        records = completed_mcp_pair(
            "call", "memory_query", {"limit": True}, {"status": "ok"}
        )
        records[1]["item"]["arguments"] = {"limit": 1}
        _, errors = SERVICE._completed_mcp_calls(records)
        self.assertTrue(any("arguments changed" in error for error in errors))

    def test_completed_call_text_and_structured_results_must_agree(self):
        records = completed_mcp_pair(
            "call", "memory_init", {"run_id": "one"}, {"status": "ok"}
        )
        records[1]["item"]["result"]["content"][0]["text"] = json.dumps(
            {"status": "forged"}
        )
        _, errors = SERVICE._completed_mcp_calls(records)
        self.assertTrue(
            any("text/structured results differ" in error for error in errors)
        )

    def test_boolean_and_integer_text_results_are_not_exactly_equal(self):
        records = completed_mcp_pair(
            "call", "memory_append", {"run_id": "one"}, {"index": 1}
        )
        records[1]["item"]["result"]["content"][0]["text"] = json.dumps(
            {"index": True}
        )
        _, errors = SERVICE._completed_mcp_calls(records)
        self.assertTrue(
            any("text/structured results differ" in error for error in errors)
        )

    def test_completed_calls_must_not_overlap(self):
        first = completed_mcp_pair(
            "first", "memory_init", {"run_id": "one"}, {"status": "ok"}
        )
        second = completed_mcp_pair(
            "second", "memory_query", {"run_id": "one"}, {"status": "ok"}
        )
        records = [first[0], second[0], first[1], second[1]]
        _, errors = SERVICE._completed_mcp_calls(records)
        self.assertTrue(any("overlap" in error for error in errors))

    def test_turn_completed_reordering_is_rejected(self):
        records = clean_transcript()
        records.insert(0, records.pop())
        self.assertTrue(SERVICE._tool_evidence(records)["structural_errors"])

    def test_turn_started_before_thread_is_rejected(self):
        records = clean_transcript()
        records[0], records[1] = records[1], records[0]
        self.assertTrue(SERVICE._tool_evidence(records)["structural_errors"])

    def test_record_after_turn_completed_is_rejected(self):
        records = clean_transcript()
        records.append(
            {
                "type": "item.completed",
                "item": {"id": "late", "type": "agent_message", "text": "late"},
            }
        )
        self.assertTrue(SERVICE._tool_evidence(records)["structural_errors"])

    def test_extra_top_level_key_is_rejected(self):
        records = clean_transcript()
        records[2]["unexpected"] = True
        self.assertTrue(SERVICE._tool_evidence(records)["structural_errors"])

    def test_extra_mcp_item_key_is_rejected(self):
        records = clean_transcript()
        records[2]["item"]["command"] = "forged"
        self.assertTrue(SERVICE._tool_evidence(records)["structural_errors"])

    def test_extra_text_block_key_is_rejected(self):
        records = clean_transcript()
        records[3]["item"]["result"]["content"][0]["unexpected"] = True
        self.assertTrue(SERVICE._tool_evidence(records)["structural_errors"])

    def test_extra_agent_message_key_is_rejected(self):
        records = clean_transcript()
        records.insert(
            -1,
            {
                "type": "item.completed",
                "item": {
                    "id": "message",
                    "type": "agent_message",
                    "text": "done",
                    "unexpected": True,
                },
            },
        )
        self.assertTrue(SERVICE._tool_evidence(records)["structural_errors"])

    def test_boolean_turn_usage_is_rejected(self):
        for field in clean_transcript()[-1]["usage"]:
            with self.subTest(field=field):
                records = clean_transcript()
                records[-1]["usage"][field] = True
                self.assertTrue(
                    SERVICE._tool_evidence(records)["structural_errors"]
                )

    def test_production_log_shape_is_accepted(self):
        log = Path(
            "/Users/mingchen/Projects/Yethlas/rethlas_hardened_v3_2_20260901/"
            "artifacts/results/20260901T001434Z_159f10ec53e3_d1b40588/codex.jsonl"
        )
        records, invalid, raw = SERVICE._parse_jsonl_log(log)
        evidence = SERVICE._tool_evidence(records)
        calls, binding_errors = SERVICE._completed_mcp_calls(records)
        self.assertEqual(len(records), 140)
        self.assertEqual(len(calls), 65)
        self.assertEqual(invalid, [])
        self.assertEqual(raw, [])
        self.assertEqual(evidence["structural_errors"], [])
        self.assertEqual(evidence["suspicious_tool_records"], [])
        self.assertEqual(binding_errors, [])


class RuntimeStaticTests(unittest.TestCase):
    def test_mcp_declarations_equal_host_allowlist(self):
        source = (ROOT / "runtime" / "hardened_mcp.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        declared = set()
        signatures = {}
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            for decorator in node.decorator_list:
                if not isinstance(decorator, ast.Call):
                    continue
                if not (
                    isinstance(decorator.func, ast.Attribute)
                    and isinstance(decorator.func.value, ast.Name)
                    and decorator.func.value.id == "APP"
                    and decorator.func.attr == "tool"
                ):
                    continue
                name_keyword = next(
                    (keyword for keyword in decorator.keywords if keyword.arg == "name"),
                    None,
                )
                self.assertIsNotNone(name_keyword)
                self.assertIsInstance(name_keyword.value, ast.Constant)
                tool_name = name_keyword.value.value
                declared.add(tool_name)
                signatures[tool_name] = [argument.arg for argument in node.args.args]
        self.assertEqual(declared, SERVICE.ALLOWED_MCP_TOOLS)
        self.assertEqual(
            signatures,
            {
                "memory_init": ["run_id", "meta"],
                "memory_append": ["run_id", "channel", "record"],
                "memory_append_reference": ["run_id", "record"],
                "memory_query": ["run_id", "channel", "contains", "limit", "reverse"],
                "search_arxiv_theorems": ["query", "num_results"],
                "search_fixed_source": ["source_id", "query", "context_lines", "max_hits"],
                "read_fixed_source_lines": ["source_id", "start_line", "end_line"],
                "validate_verification_output": ["run_id", "payload"],
                "write_verification_output": ["run_id", "payload"],
            },
        )

    def test_versions_are_consistently_v333r5p148retry1(self):
        self.assertEqual(
            SERVICE.SERVICE_VERSION, "rethlas-hardened-service-v3.3.3-r5-p148-retry1"
        )
        self.assertEqual(
            SERVICE.RUNTIME_CONTRACT_VERSION,
            "rethlas-hardened-runtime-contract-v3.3.3-r5-p148-retry1",
        )
        self.assertEqual(SERVICE.app.version, "3.3.3-r5-p148-retry1")
        contract = (ROOT / "runtime" / "contract.md").read_text(encoding="utf-8")
        mcp = (ROOT / "runtime" / "hardened_mcp.py").read_text(encoding="utf-8")
        self.assertIn("contract v3.3.3-r5-p148-retry1", contract)
        self.assertIn("rethlas-hardened-runtime-contract-v3.3.3-r5-p148-retry1", mcp)
        self.assertEqual(
            SERVICE.EXPECTED_RELEASE_PINSET_SHA256,
            "3f7e644253d2e77395fa17c55b8a1f8ddf4e56b07eeeeab430a6c0898ac53020",
        )

    def test_memory_init_contract_is_statement_only(self):
        contract = (ROOT / "runtime" / "contract.md").read_text(encoding="utf-8")
        mcp = (ROOT / "runtime" / "hardened_mcp.py").read_text(encoding="utf-8")
        service = (ROOT / "runtime" / "hardened_service.py").read_text(
            encoding="utf-8"
        )
        self.assertIn('meta={"statement": <exact supplied Statement>})', contract)
        self.assertNotIn("input_shape", contract)
        self.assertNotIn("input_shape", mcp)
        self.assertNotIn("input_shape", service)

    def test_static_model_catalog_bytes_selection_and_launch_are_exact(self):
        catalog_path = ROOT / "runtime" / "model_catalog.gpt-5.6-sol.json"
        self.assertEqual(SERVICE.MODEL_CATALOG_PATH, catalog_path)
        self.assertTrue(catalog_path.is_file())
        self.assertFalse(catalog_path.is_symlink())
        self.assertEqual(catalog_path.stat().st_size, 41355)
        self.assertEqual(
            SERVICE._sha256_file(catalog_path),
            "75ecc0f5301dcc5474598335a12e82e9195eeb04f55197f2589109b34f3988fa",
        )
        bound = SERVICE._assert_static_model_catalog()
        self.assertEqual(bound["runtime_path"], "model_catalog.gpt-5.6-sol.json")
        self.assertEqual(bound["model"], "gpt-5.6-sol")
        self.assertEqual(bound["reasoning_effort"], "xhigh")
        self.assertIn("xhigh", bound["supported_reasoning_efforts"])
        self.assertEqual(bound["manager"], "StaticModelsManager")

        command = SERVICE._build_command(
            "static_catalog_test",
            "a" * 64,
            Path("/tmp/rethlas-static-catalog-test"),
            "statement",
            "proof",
        )
        catalog_config = f'model_catalog_json="{catalog_path}"'
        self.assertEqual(command.count(catalog_config), 1)
        self.assertEqual(command[command.index(catalog_config) - 1], "--config")
        self.assertEqual(command.count('-m'), 1)
        self.assertEqual(command[command.index('-m') + 1], "gpt-5.6-sol")
        self.assertIn('model_reasoning_effort="xhigh"', command)

    def test_codex_debug_models_uses_exact_static_catalog_without_refresh_diagnostic(self):
        environment = dict(os.environ)
        environment["RUST_LOG"] = "info"
        result = subprocess.run(
            [
                str(SERVICE.CODEX),
                "debug",
                "models",
                "--config",
                f'model_catalog_json="{SERVICE.MODEL_CATALOG_PATH}"',
            ],
            cwd=ROOT,
            env=environment,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        parsed = SERVICE._strict_json_loads(result.stdout)
        self.assertEqual(set(parsed), {"models"})
        self.assertEqual(len(parsed["models"]), 1)
        self.assertEqual(parsed["models"][0]["slug"], "gpt-5.6-sol")
        combined = result.stdout + "\n" + result.stderr
        for forbidden in (
            "codex_models_manager::manager",
            "failed to refresh available models",
            "models cache",
        ):
            self.assertNotIn(forbidden, combined)

    def test_fixed_source_maps_are_exact_and_consistent(self):
        expected = {
            "bmps_2603_08664": "sources/bmps_2603.08664.txt",
            "bc_0911_2923v1": "sources/bc_0911.2923v1.txt",
            "berman_0710_4375v2": "sources/berman_0710.4375v2.txt",
            "cld_1204_6277": "sources/cld_1204.6277.txt",
            "dxz_2302_02541v3": "sources/dxz_2302.02541v3.txt",
            "ducros_aif_2009": "sources/AIF_2009__59_4_1443_0.txt",
            "gk_1406_7637": "sources/gk_1406.7637.txt",
            "gk_1509_09079": "sources/gk_1509.09079.txt",
            "stacks_01PR": "sources/stacks_01PR.html",
            "stacks_02O1": "sources/stacks_02O1.html",
            "stacks_0AY8": "sources/stacks_0AY8.html",
            "stacks_0BXQ": "sources/stacks_0BXQ.html",
            "gz_1403_7247": "sources/gz_1403_7247.txt",
            "boucksom_l2": "sources/boucksom_l2.txt",
            "begz_0812_3674v2": "sources/begz_0812_3674v2.txt",
            "bt82_new_capacity": "sources/bt82_new_capacity.txt",
            "km_1102_5596": "sources/km_1102_5596.txt",
            "p148_ch51_dependency_v3": "sources/p148_ch51_dependency_v3.txt",
        }
        self.assertEqual(SERVICE.FIXED_SOURCE_RUNTIME_PATHS, expected)
        source = (ROOT / "runtime" / "hardened_mcp.py").read_text(encoding="utf-8")
        self.assertIn(
            "for source_id, relative in _release_pins.FIXED_SOURCE_RUNTIME_PATHS.items()",
            source,
        )
        self.assertEqual(dict(SERVICE._release_pins.FIXED_SOURCE_RUNTIME_PATHS), expected)
        for relative in expected.values():
            path = ROOT / "runtime" / relative
            self.assertTrue(path.is_file())
            self.assertFalse(path.is_symlink())

    def test_source_bundle_pins_and_exact_runtime_test_inventory(self):
        source_pins = {
            "sources/AIF_2009__59_4_1443_0.pdf": (1090874, "bfa8c478551c0e15e43fe5cfeb99211d35ec144ddb1c39b31a73ed2613aa05f0"),
            "sources/AIF_2009__59_4_1443_0.txt": (309747, "180642ff21eaec9a16b4eeeb88b96efb127e007acec69057aaa1896e1bc0914a"),
            "sources/bmps_2603.08664.pdf": (774717, "5cf7e68ee9113f1dc813f9aefa5f9ca72cba02fc4fa688f1a61e4b7f0d1223e7"),
            "sources/bmps_2603.08664.txt": (231469, "f53dbe010f5ce481ebb4ee4954be0aa148729313d68c3fb79c34af1bc6873fea"),
            "sources/bc_0911.2923v1.pdf": (238010, "1dca3f1a575a97e98e5fd5dd78063c1d84f61c377ea8c5fef3ba5afc50e6d027"),
            "sources/bc_0911.2923v1.txt": (69671, "1d7dfef7bd658066848109de54fb438af00f3403221f2490e7df2e393ce2075e"),
            "sources/berman_0710.4375v2.pdf": (490866, "6b1d6a1f595a9353d928d26c13c417fd560d1c63e248d054e4ac5de03d3af7c0"),
            "sources/berman_0710.4375v2.txt": (117136, "f2edcf529dce1fb39a711f3e2f56bc942952d75df483835d624de75486e4f53f"),
            "sources/cld_1204.6277.pdf": (4659053, "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719"),
            "sources/cld_1204.6277.txt": (2150944, "021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e"),
            "sources/dxz_2302.02541v3.pdf": (534767, "7fede7c413e396008217a4a4c9638776dbdd7cacff90fdd463bf5ae48220246c"),
            "sources/dxz_2302.02541v3.txt": (141745, "7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244"),
            "sources/gk_1406.7637.pdf": (1066195, "62c7e4dfebab75d725f529c6ef78c300856c63fd050a9399e8a86879e569315d"),
            "sources/gk_1406.7637.txt": (311700, "be0b9b4afc76b71d652772de6d6e720fe1620149b9470ed903a1de3cb3b470e6"),
            "sources/gk_1509.09079.pdf": (446717, "36ce3e8bb8758eb67af4320dd4e23bf65297fb80abea64ce87a160683b300dbd"),
            "sources/gk_1509.09079.txt": (126873, "3ce89f11fed97fadd6199a2a1fa6a5be0e34f7c878615a18ea6db4ddfd02e4d5"),
            "sources/stacks_01PR.html": (48192, "10e5729facc1f46a826ad3adad02c107aa2d7aec3f87b7650122c46c5d9a59c1"),
            "sources/stacks_02O1.html": (14863, "95b2a9b89f899192d71a6ced00b482b5901ab512daa9a63d7d568e424c7adfcb"),
            "sources/stacks_0AY8.html": (15046, "b5d4fecb3d75b8f51b93e134bcaafabf3d47810370ad356e79de23907de18d75"),
            "sources/stacks_0BXQ.html": (25115, "7fc401b609392d9dc1bf78bdd534a1dc0bf40fcbe6ddc2d97d15795a5b191737"),
            "sources/begz_0812_3674v2.pdf": (414218, "43097be8459edfd948929fade34367fa7bbd0fe691d9cba1a4f27a11181214cd"),
            "sources/begz_0812_3674v2.txt": (163107, "890173e309165984432e7326d13b7e096662cc805fbc19045a297f12211254c7"),
            "sources/boucksom_l2.pdf": (552046, "5e3b9441461c6eab35f546c35087cdec0dd146daa84460a00058750eb5cd0909"),
            "sources/boucksom_l2.txt": (147498, "4a3fa01a21b1cc66fe174460732fe80a29914f26279c04d2824223fc7d9ab0a4"),
            "sources/bt82_new_capacity.pdf": (1560096, "e75ea91e48c14a9838a800aee25b68ed04169c4372f2ce4b399967b53005b758"),
            "sources/bt82_new_capacity.txt": (83498, "716a2e1012a35ab6811873bc9f84d981627b7d6f4d9e6e4c8d48b0b525460d8b"),
            "sources/gz_1403_7247.pdf": (351472, "13abbf7960f8c3619f040e28aed9d1e63dac854ab5e92fdf37db3df734ef88aa"),
            "sources/gz_1403_7247.txt": (104796, "27b2cde510c3204fe672de367119644dd917f0abe0487af256d43db4a5287f10"),
            "sources/km_1102_5596.pdf": (194428, "56f18ebf925b06d8b29fac3388c9be42dfe23d5365b3f10d12ff8f7088319f1e"),
            "sources/km_1102_5596.txt": (48316, "fd59393dbbd2c98820bf217b5bd94ec1b786e125c7fa53b00900d56f6bc19cf7"),
            "sources/p148_ch51_dependency_v3.txt": (34444, "c2404ea689ed09cf80fb8059145bc74bab123fd39c7e1d3b70f2f37b4c484fce"),
        }
        for relative, (size, digest) in source_pins.items():
            path = ROOT / "runtime" / relative
            self.assertTrue(path.is_file(), relative)
            self.assertFalse(path.is_symlink(), relative)
            self.assertEqual(path.stat().st_size, size, relative)
            self.assertEqual(SERVICE._sha256_file(path), digest, relative)
        expected = {
            "runtime/canonical_reference.py",
            "runtime/contract.md",
            "runtime/hardened_mcp.py",
            "runtime/hardened_service.py",
            "runtime/memory_record.schema.json",
            "runtime/model_catalog.gpt-5.6-sol.json",
            "runtime/release_pins.py",
            "runtime/verification_output.schema.json",
            *("runtime/" + relative for relative in source_pins),
            "tests/test_runtime.py",
        }
        actual = {
            path.relative_to(ROOT).as_posix()
            for parent in (ROOT / "runtime", ROOT / "tests")
            for path in parent.rglob("*")
            if path.is_file()
        }
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), 40)

    def test_real_source_byte_search_and_read_anchors(self):
        anchors = {
            "bmps_2603_08664": ("Definition 2.31", 532, 543),
            "bc_0911_2923v1": ("Lemma 1.6.", 368, 375),
            "berman_0710_4375v2": ("Theorem 1.4.", 247, 267),
            "dxz_2302_02541v3": ("Definition 4.1.", 1342, 1365),
            "gk_1406_7637": ("(1.4.3)", 518, 528),
            "gk_1509_09079": ("Theorem 8.4", 1463, 1492),
            "stacks_01PR": ('Proposition <span data-tag="01Q3">28.27.13', 363, 363),
            "stacks_02O1": ('Lemma <span data-tag="02O1">30.16.2', 175, 175),
            "stacks_0AY8": ('Lemma <span data-tag="0AY8">37.53.6', 175, 175),
            "stacks_0BXQ": ('Lemma <span data-tag="0BXR">33.27.1', 164, 164),
            "gz_1403_7247": ("Theorem 1.1.", 39, 39),
            "boucksom_l2": ("Corollary 10.18.", 2369, 2414),
            "begz_0812_3674v2": ("Definition 1.1.", 211, 215),
            "bt82_new_capacity": ("THEOREM 6.9.", 1107, 1131),
            "km_1102_5596": ("(3.4)", 389, 395),
            "p148_ch51_dependency_v3": ("cor:ch51-choquet", 28, 28),
        }
        runtime_before = SERVICE._runtime_fingerprint()
        for source_id, (query, lf_line_number, runtime_line_number) in anchors.items():
            relative = SERVICE.FIXED_SOURCE_RUNTIME_PATHS[source_id]
            path = ROOT / "runtime" / relative
            decoded = path.read_text(encoding="utf-8", errors="replace")
            lf_lines = decoded.split("\n")
            self.assertIn(query.casefold(), lf_lines[lf_line_number - 1].casefold(), source_id)
            lines = decoded.splitlines()
            matches = [index + 1 for index, line in enumerate(lines) if query.casefold() in line.casefold()]
            self.assertIn(runtime_line_number, matches, source_id)
            search_body = {
                "source_id": source_id,
                "source_sha256": SERVICE._sha256_file(path),
                "query": query,
                "count": len(matches),
                "hits": [
                    {
                        "match_line": number,
                        "start_line": number,
                        "end_line": number,
                        "text": f"{number}: {lines[number - 1]}",
                    }
                    for number in matches
                ],
            }
            search_body["result_sha256"] = SERVICE._sha256_bytes(
                SERVICE._canonical_json_bytes(search_body)
            )
            search_call = {
                "arguments": {"source_id": source_id, "query": query, "context_lines": 0, "max_hits": 50},
                "structured_content": search_body,
            }
            detail, errors = SERVICE._fixed_search_reconstruction(search_call, runtime_before)
            self.assertEqual(errors, [], source_id)
            self.assertEqual(detail["hits"], len(matches), source_id)
            read_body = {
                "source_id": source_id,
                "source_sha256": SERVICE._sha256_file(path),
                "start_line": runtime_line_number,
                "end_line": runtime_line_number,
                "text": f"{runtime_line_number}: {lines[runtime_line_number - 1]}",
            }
            read_call = {
                "arguments": {"source_id": source_id, "start_line": runtime_line_number, "end_line": runtime_line_number},
                "structured_content": read_body,
            }
            detail, errors = SERVICE._fixed_read_reconstruction(read_call, runtime_before)
            self.assertEqual(errors, [], source_id)
            self.assertEqual(detail["start_line"], runtime_line_number, source_id)

    def test_ch51_external_anchors_and_p148_internal_packet_are_separated(self):
        anchors = {
            "bt82_new_capacity": {
                462: "Definition 3.1.",
                963: "C*(E)",
                1107: "THEOREM 6.9.",
            },
            "begz_0812_3674v2": {
                211: "Definition 1.1.",
                326: "Proposition 1.6.",
            },
        }
        for source_id, expected_lines in anchors.items():
            path = ROOT / "runtime" / SERVICE.FIXED_SOURCE_RUNTIME_PATHS[source_id]
            lines = path.read_text(encoding="utf-8", errors="replace").split("\n")
            for line_number, marker in expected_lines.items():
                self.assertIn(marker.casefold(), lines[line_number - 1].casefold())

        source_id = "p148_ch51_dependency_v3"
        source_path = ROOT / "runtime/sources/p148_ch51_dependency_v3.txt"
        self.assertEqual(
            SERVICE.FIXED_SOURCE_RUNTIME_PATHS[source_id],
            "sources/p148_ch51_dependency_v3.txt",
        )
        self.assertTrue(source_path.is_file())
        self.assertFalse(source_path.is_symlink())
        self.assertEqual(source_path.stat().st_size, 34444)
        self.assertEqual(
            SERVICE._sha256_file(source_path),
            "c2404ea689ed09cf80fb8059145bc74bab123fd39c7e1d3b70f2f37b4c484fce",
        )
        packet = source_path.read_text(encoding="utf-8")
        self.assertEqual(len(packet.splitlines()), 784)
        for required in (
            "cor:ch51-choquet",
            "lem:ch51-lelong-increasing",
            "thm:complex-strong-openness",
            "lem:ch51-npp-bidegree-one",
            "the product charges no pluripolar set",
            "def:complex-i-preorder",
            "def:complex-i-envelope",
            "eq:complex-i-envelope",
            "lem:ch51-polar-cantor",
            "choice \\(\\ell_0=1\\) and \\(\\ell_m=\\rme^{-4^m}\\) for \\(m\\geq1\\)",
            "\\ell_1/\\ell_0=\\rme^{-4}\\leq1/2",
        ):
            self.assertIn(required, packet)
        for forbidden in (
            "thm:complex-i-projection",
            "eq:complex-i-projection",
            "Zero mass is not an \\(\\mathcal I\\)-condition",
            "\\varphi_s:=sG_\\mu",
            "potentials of every mass",
            "P14.8",
        ):
            self.assertNotIn(forbidden, packet)
        removed_id = "p148_ch51_dependency_v2"
        self.assertNotIn(removed_id, SERVICE.FIXED_SOURCE_RUNTIME_PATHS)
        self.assertFalse((ROOT / "runtime/sources/p148_ch51_dependency_v2.txt").exists())
        self.assertFalse((ROOT / "runtime/sources/p148_ch51_dependency_v1.txt").exists())
        contract = (ROOT / "runtime/contract.md").read_text(encoding="utf-8")
        self.assertIn("eighteen searchable text/HTML files and thirteen companion PDFs", contract)
        self.assertIn(source_id, contract)
        self.assertNotIn(removed_id, contract)
        stage_report = (ROOT / "STAGING_REPORT.md").read_text(encoding="utf-8")
        for stale in (
            "provisional_pending_ch51_production_acceptance",
            "Chapter 51 dependency is provisional",
            "pending production acceptance",
        ):
            self.assertNotIn(stale, stage_report)
        self.assertIn("20260901T143740Z_9b8ffa07bc57_69cb27d9", stage_report)
        self.assertIn("the host status was accepted", stage_report)
        self.assertIn("the verifier verdict was correct", stage_report)
        runtime_before = SERVICE._runtime_fingerprint()
        _, search_errors = SERVICE._fixed_search_reconstruction(
            {
                "arguments": {
                    "source_id": removed_id,
                    "query": "cor:ch51-choquet",
                    "context_lines": 0,
                    "max_hits": 1,
                },
                "structured_content": {},
            },
            runtime_before,
        )
        _, read_errors = SERVICE._fixed_read_reconstruction(
            {
                "arguments": {
                    "source_id": removed_id,
                    "start_line": 1,
                    "end_line": 1,
                },
                "structured_content": {},
            },
            runtime_before,
        )
        self.assertTrue(any("not allowlisted" in error for error in search_errors))
        self.assertTrue(any("not allowlisted" in error for error in read_errors))

    def test_mcp_reversed_query_is_not_credited_as_complete(self):
        source = (ROOT / "runtime" / "hardened_mcp.py").read_text(encoding="utf-8")
        self.assertIn(
            "if contains is None and not reverse and limit >= len(all_items):",
            source,
        )

    def test_strict_json_loader_rejects_nested_duplicates_and_nonfinite(self):
        with self.assertRaisesRegex(ValueError, "duplicate JSON object key"):
            SERVICE._strict_json_loads('{"outer":{"x":1,"x":2}}')
        for token in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(token=token):
                with self.assertRaisesRegex(ValueError, "non-finite"):
                    SERVICE._strict_json_loads('{"value":' + token + "}")

    def test_contract_excludes_model_supplied_provenance(self):
        contract = (ROOT / "runtime" / "contract.md").read_text(encoding="utf-8")
        self.assertIn("memory_append_reference(run_id, record)", contract)
        self.assertIn("canonical-only fields", contract)
        section_start = contract.index("`record` argument has exactly the simplified shape")
        block_start = contract.index("```json", section_start) + len("```json")
        block_end = contract.index("```", block_start)
        simplified_block = contract[block_start:block_end]
        self.assertNotIn("search_result_sha256", simplified_block)
        self.assertNotIn('"sha256"', simplified_block)


class MemoryRecordSchemaTests(unittest.TestCase):
    def test_valid_statement_record(self):
        record = {
            "record_type": "statement_check",
            "location": "Proof, step 1",
            "status": "verified",
            "critical_errors": [],
            "gaps": [],
            "detail": "The hypotheses and deduction agree.",
        }
        self.assertEqual(
            SERVICE._memory_record_validation_errors("statement_checks", record), []
        )

    def test_verified_record_with_finding_is_rejected(self):
        record = {
            "record_type": "statement_check",
            "location": "Proof, step 1",
            "status": "verified",
            "critical_errors": [{"location": "step 1", "issue": "false"}],
            "gaps": [],
            "detail": "Contradictory status.",
        }
        self.assertTrue(
            SERVICE._memory_record_validation_errors("statement_checks", record)
        )

    def test_malformed_record_is_rejected(self):
        self.assertTrue(
            SERVICE._memory_record_validation_errors("statement_checks", {})
        )

    def test_valid_no_reference_record(self):
        record = {
            "record_type": "reference_check",
            "reference_mode": "no_external_references",
            "location": "Entire proof",
            "status": "verified",
            "search_query": "",
            "search_result_sha256": "",
            "search_result_count": 0,
            "search_status": "not_applicable_no_external_references",
            "search_evidence": [],
            "source_evidence": [],
            "contextual_definition_comparison": "No source-dependent definition occurs.",
            "applicability": "No external result is invoked.",
            "critical_errors": [],
            "gaps": [],
            "detail": "No external reference occurs.",
        }
        self.assertEqual(
            SERVICE._memory_record_validation_errors("reference_checks", record), []
        )

    def test_external_source_evidence_requires_a_positive_search_hit(self):
        record = {
            "record_type": "reference_check",
            "reference_mode": "external",
            "location": "Proof, cited step",
            "status": "verified",
            "search_query": "a theorem query",
            "search_result_sha256": "a" * 64,
            "search_result_count": 1,
            "search_status": "ok",
            "search_evidence": ["The returned theorem was compared."],
            "source_evidence": [
                {
                    "source_id": "cld_1204_6277",
                    "sha256": "b" * 64,
                    "search_query": "local potential",
                    "search_result_sha256": "c" * 64,
                    "search_result_count": 0,
                    "line_ranges": [{"start_line": 10, "end_line": 20}],
                    "comparison": "The hypotheses were compared line by line.",
                }
            ],
            "contextual_definition_comparison": "Definitions agree in this context.",
            "applicability": "All hypotheses are met.",
            "critical_errors": [],
            "gaps": [],
            "detail": "External reference audit.",
        }
        self.assertTrue(
            SERVICE._memory_record_validation_errors("reference_checks", record)
        )


class CanonicalReferenceTests(unittest.TestCase):
    def _simplified(self):
        return {
            "location": "Proof, cited step",
            "status": "verified",
            "search_query": "full theorem statement",
            "search_evidence": ["The theorem statement was compared."],
            "source_evidence": [
                {
                    "source_id": "source",
                    "search_query": "local potential",
                    "line_ranges": [{"start_line": 2, "end_line": 2}],
                    "comparison": "The source hypotheses agree.",
                }
            ],
            "contextual_definition_comparison": "Definitions agree.",
            "applicability": "All assumptions hold.",
            "critical_errors": [],
            "gaps": [],
            "detail": "Complete external-reference audit.",
        }

    def _events(self):
        return [
            {
                "sequence": 1,
                "tool": "search_arxiv_theorems",
                "detail": {
                    "query_sha256": SERVICE._sha256_text("full theorem statement"),
                    "status": "ok",
                    "count": 4,
                    "result_sha256": "a" * 64,
                },
            },
            {
                "sequence": 2,
                "tool": "search_fixed_source",
                "detail": {
                    "source_id": "source",
                    "query_sha256": SERVICE._sha256_text("local potential"),
                    "hits": 1,
                    "result_sha256": "b" * 64,
                },
            },
            {
                "sequence": 3,
                "tool": "read_fixed_source_lines",
                "detail": {
                    "source_id": "source",
                    "start_line": 2,
                    "end_line": 2,
                },
            },
        ]

    def test_canonicalizer_supplies_all_provenance_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.txt"
            source.write_text("first\nlocal potential\n", encoding="utf-8")
            canonical, binding = canonicalize_external_reference_record(
                self._simplified(), self._events(), {"source": source}
            )
        self.assertEqual(canonical["record_type"], "reference_check")
        self.assertEqual(canonical["reference_mode"], "external")
        self.assertEqual(canonical["search_status"], "ok")
        self.assertEqual(canonical["search_result_sha256"], "a" * 64)
        self.assertEqual(canonical["search_result_count"], 4)
        self.assertEqual(
            canonical["source_evidence"][0]["search_result_sha256"], "b" * 64
        )
        self.assertEqual(
            canonical["source_evidence"][0]["search_result_count"], 1
        )
        self.assertEqual(binding["theorem_search_sequence"], 1)
        self.assertEqual(binding["source_bindings"][0]["fixed_search_sequence"], 2)
        self.assertEqual(binding["source_bindings"][0]["read_sequences"], [3])
        self.assertEqual(len(binding["canonical_record_sha256"]), 64)

    def test_fabricated_top_level_digest_is_rejected(self):
        record = self._simplified()
        record["search_result_sha256"] = "f" * 64
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.txt"
            source.write_text("first\nlocal potential\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "keys mismatch"):
                canonicalize_external_reference_record(
                    record, self._events(), {"source": source}
                )

    def test_fabricated_source_digest_is_rejected(self):
        record = self._simplified()
        record["source_evidence"][0]["sha256"] = "f" * 64
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.txt"
            source.write_text("first\nlocal potential\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "keys mismatch"):
                canonicalize_external_reference_record(
                    record, self._events(), {"source": source}
                )

    def test_latest_exact_search_controls_order_and_cannot_be_skipped(self):
        events = self._events()
        events.append(
            {
                "sequence": 4,
                "tool": "search_arxiv_theorems",
                "detail": {
                    "query_sha256": SERVICE._sha256_text("full theorem statement"),
                    "status": "ok",
                    "count": 2,
                    "result_sha256": "c" * 64,
                },
            }
        )
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.txt"
            source.write_text("first\nlocal potential\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "theorem-search < fixed"):
                canonicalize_external_reference_record(
                    self._simplified(), events, {"source": source}
                )

    def test_read_before_latest_fixed_search_is_rejected(self):
        events = self._events()
        events.append(
            {
                "sequence": 4,
                "tool": "search_fixed_source",
                "detail": {
                    "source_id": "source",
                    "query_sha256": SERVICE._sha256_text("local potential"),
                    "hits": 2,
                    "result_sha256": "d" * 64,
                },
            }
        )
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.txt"
            source.write_text("first\nlocal potential\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "fixed-source-search < read"):
                canonicalize_external_reference_record(
                    self._simplified(), events, {"source": source}
                )

    def test_boolean_search_count_is_rejected(self):
        events = self._events()
        events[0]["detail"]["count"] = True
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.txt"
            source.write_text("first\nlocal potential\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "invalid result count"):
                canonicalize_external_reference_record(
                    self._simplified(), events, {"source": source}
                )

    def test_boolean_line_range_is_rejected(self):
        record = self._simplified()
        record["source_evidence"][0]["line_ranges"][0]["start_line"] = True
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.txt"
            source.write_text("first\nlocal potential\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "is invalid"):
                canonicalize_external_reference_record(
                    record, self._events(), {"source": source}
                )

    def test_memory_append_source_forbids_external_records(self):
        source = (ROOT / "runtime" / "hardened_mcp.py").read_text(encoding="utf-8")
        self.assertIn(
            "external reference records must use memory_append_reference", source
        )


class CanonicalHostReplayTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.old_roots = (
            SERVICE.RUNTIME_ROOT,
            SERVICE.MEMORY_ROOT,
            SERVICE.RESULTS_ROOT,
            SERVICE.RECEIPTS_ROOT,
        )
        self.runtime_root = self.root / "runtime"
        self.memory_root = self.root / "memory"
        self.results_root = self.root / "results"
        self.receipts_root = self.root / "receipts"
        self.source_path = self.runtime_root / "sources" / "cld_1204.6277.txt"
        self.source_path.parent.mkdir(parents=True)
        self.source_path.write_text(
            "first\nlocal potential\nlast\n", encoding="utf-8"
        )
        self.source_paths = {
            "bmps_2603_08664": self.runtime_root / "sources" / "bmps_2603.08664.txt",
            "bc_0911_2923v1": self.runtime_root / "sources" / "bc_0911.2923v1.txt",
            "berman_0710_4375v2": self.runtime_root / "sources" / "berman_0710.4375v2.txt",
            "cld_1204_6277": self.source_path,
            "dxz_2302_02541v3": self.runtime_root / "sources" / "dxz_2302.02541v3.txt",
            "ducros_aif_2009": self.runtime_root / "sources" / "AIF_2009__59_4_1443_0.txt",
            "gk_1406_7637": self.runtime_root / "sources" / "gk_1406.7637.txt",
            "gk_1509_09079": self.runtime_root / "sources" / "gk_1509.09079.txt",
            "stacks_01PR": self.runtime_root / "sources" / "stacks_01PR.html",
            "stacks_02O1": self.runtime_root / "sources" / "stacks_02O1.html",
            "stacks_0AY8": self.runtime_root / "sources" / "stacks_0AY8.html",
            "stacks_0BXQ": self.runtime_root / "sources" / "stacks_0BXQ.html",
            "gz_1403_7247": self.runtime_root / "sources" / "gz_1403_7247.txt",
            "boucksom_l2": self.runtime_root / "sources" / "boucksom_l2.txt",
            "begz_0812_3674v2": self.runtime_root / "sources" / "begz_0812_3674v2.txt",
            "bt82_new_capacity": self.runtime_root / "sources" / "bt82_new_capacity.txt",
            "km_1102_5596": self.runtime_root / "sources" / "km_1102_5596.txt",
            "p148_ch51_dependency_v3": self.runtime_root / "sources" / "p148_ch51_dependency_v3.txt",
        }
        source_contents = {
            "bmps_2603_08664": "first\nDefinition 2.31\nlast\n",
            "bc_0911_2923v1": "first\nLemma 1.6.\nlast\n",
            "berman_0710_4375v2": "first\nTheorem 1.4.\nlast\n",
            "dxz_2302_02541v3": "first\nDefinition 4.1.\nlast\n",
            "ducros_aif_2009": "first\nDucros source\nlast\n",
            "gk_1406_7637": "first\n(1.4.3)\nlast\n",
            "gk_1509_09079": "first\nTheorem 8.4\nlast\n",
            "stacks_01PR": "first\nProposition 28.27.13\nlast\n",
            "stacks_02O1": "first\nLemma 30.16.2\nlast\n",
            "stacks_0AY8": "first\nLemma 37.53.6\nlast\n",
            "stacks_0BXQ": "first\nSection 33.27\nlast\n",
            "gz_1403_7247": "first\nTheorem 1.1.\nlast\n",
            "boucksom_l2": "first\nCorollary 10.18.\nlast\n",
            "begz_0812_3674v2": "first\nDefinition 1.1.\nlast\n",
            "bt82_new_capacity": "first\nTHEOREM 6.9.\nlast\n",
            "km_1102_5596": "first\n(3.4)\nlast\n",
            "p148_ch51_dependency_v3": "first\ncor:ch51-choquet\nlast\n",
        }
        for source_id, content in source_contents.items():
            self.source_paths[source_id].write_text(content, encoding="utf-8")
        SERVICE.RUNTIME_ROOT = self.runtime_root
        SERVICE.MEMORY_ROOT = self.memory_root
        SERVICE.RESULTS_ROOT = self.results_root
        SERVICE.RECEIPTS_ROOT = self.receipts_root

    def tearDown(self):
        (
            SERVICE.RUNTIME_ROOT,
            SERVICE.MEMORY_ROOT,
            SERVICE.RESULTS_ROOT,
            SERVICE.RECEIPTS_ROOT,
        ) = (
            self.old_roots
        )
        self.temporary.cleanup()

    @staticmethod
    def _event(sequence, tool, detail=None):
        event = {
            "sequence": sequence,
            "timestamp_utc": f"2026-09-01T00:00:{sequence:02d}+00:00",
            "tool": tool,
        }
        if detail is not None:
            event["detail"] = detail
        return event

    @staticmethod
    def _write_json(path, value):
        path.write_text(
            json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    @staticmethod
    def _write_jsonl(path, values):
        path.write_text(
            "".join(
                json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n"
                for value in values
            ),
            encoding="utf-8",
        )

    @staticmethod
    def _payload():
        return {
            "verification_report": {
                "summary": "All checks passed.",
                "critical_errors": [],
                "gaps": [],
            },
            "verdict": "correct",
            "repair_hints": "",
        }

    @staticmethod
    def _statement_record():
        return {
            "record_type": "statement_check",
            "location": "Proof, step 1",
            "status": "verified",
            "critical_errors": [],
            "gaps": [],
            "detail": "The step is valid.",
        }

    @staticmethod
    def _no_reference_record():
        return {
            "record_type": "reference_check",
            "reference_mode": "no_external_references",
            "location": "Entire proof",
            "status": "verified",
            "search_query": "",
            "search_result_sha256": "",
            "search_result_count": 0,
            "search_status": "not_applicable_no_external_references",
            "search_evidence": [],
            "source_evidence": [],
            "contextual_definition_comparison": "No source-dependent definition occurs.",
            "applicability": "No external result is invoked.",
            "critical_errors": [],
            "gaps": [],
            "detail": "No external reference occurs.",
        }

    @staticmethod
    def _with_digest(value):
        result = dict(value)
        result["result_sha256"] = SERVICE._sha256_bytes(
            SERVICE._canonical_json_bytes(result)
        )
        return result

    def _materialize(
        self,
        events,
        reference_records,
        call_specs,
        runtime_before,
        *,
        payload=None,
        statement_record=None,
    ):
        run_id = self._testMethodName
        run_memory = self.memory_root / run_id
        run_memory.mkdir(parents=True)
        (self.results_root / run_id).mkdir(parents=True)
        payload = self._payload() if payload is None else copy.deepcopy(payload)
        statement_record = (
            self._statement_record()
            if statement_record is None
            else copy.deepcopy(statement_record)
        )
        payload_sha = SERVICE._sha256_bytes(SERVICE._canonical_json_bytes(payload))

        meta_statement = "Host-bound test statement"
        host_statement_sha = SERVICE._sha256_text(meta_statement)
        normalized_statement_sha = SERVICE._sha256_text(meta_statement.rstrip("\n"))
        proof_sha = SERVICE._sha256_text("Host-bound test proof")
        events[0]["detail"] = {
            "meta_statement_sha256": host_statement_sha,
            "meta_statement_normalized_sha256": normalized_statement_sha,
            "host_statement_sha256": host_statement_sha,
        }
        self._write_json(
            run_memory / "meta.json",
            {
                "run_id": run_id,
                "statement": meta_statement,
                "statement_sha256": host_statement_sha,
                "statement_normalized_sha256": normalized_statement_sha,
                "host_statement_sha256": host_statement_sha,
                "host_statement_normalized_sha256": normalized_statement_sha,
                "proof_sha256": proof_sha,
                "created_at_utc": events[0]["timestamp_utc"],
            },
        )
        self._write_jsonl(
            run_memory / "statement_checks.jsonl",
            [
                {
                    "timestamp_utc": events[1]["timestamp_utc"],
                    "channel": "statement_checks",
                    "record": statement_record,
                }
            ],
        )
        reference_append_events = [
            event
            for event in events
            if event["tool"] in {"memory_append", "memory_append_reference"}
            and event.get("detail", {}).get("channel") == "reference_checks"
        ]
        self._write_jsonl(
            run_memory / "reference_checks.jsonl",
            [
                {
                    "timestamp_utc": reference_append_events[index]["timestamp_utc"],
                    "channel": "reference_checks",
                    "record": record,
                }
                for index, record in enumerate(reference_records)
            ],
        )
        self._write_jsonl(
            run_memory / "verification_reports.jsonl",
            [
                {
                    "timestamp_utc": events[-1]["timestamp_utc"],
                    "channel": "verification_reports",
                    "record": {
                        "event_type": "final_report_written",
                        "output_path": str(
                            self.results_root / run_id / "verification.json"
                        ),
                        "verdict": payload["verdict"],
                        "payload_sha256": payload_sha,
                    },
                }
            ],
        )
        self._write_jsonl(run_memory / "failed_checks.jsonl", [])

        counts = {
            "statement_checks": 1,
            "reference_checks": len(reference_records),
            "verification_reports": 1,
            "failed_checks": 0,
            "events": len(events),
        }
        state = {
            "format": "rethlas-hardened-mcp-state-v1",
            "runtime_contract_version": SERVICE.RUNTIME_CONTRACT_VERSION,
            "run_id": run_id,
            "phase": "finalized",
            "statement_sha256": host_statement_sha,
            "proof_sha256": proof_sha,
            "meta_statement_sha256": host_statement_sha,
            "meta_statement_normalized_sha256": normalized_statement_sha,
            "events": events,
            "channel_counts": counts,
            "tool_counts": dict(Counter(event["tool"] for event in events)),
            "queried_channels": ["reference_checks", "statement_checks"],
            "fully_queried_channels": ["reference_checks", "statement_checks"],
            "validated_payload_sha256": payload_sha,
            "mcp_pid": 123,
            "updated_at_utc": events[-1]["timestamp_utc"],
        }
        receipt = {
            "events": events,
            "memory_files_sha256": {},
            "channel_counts": counts,
            "tool_counts": state["tool_counts"],
            "fully_queried_channels": ["reference_checks", "statement_checks"],
            "queried_channels": ["reference_checks", "statement_checks"],
            "statement_sha256": host_statement_sha,
            "proof_sha256": proof_sha,
            "meta_statement_sha256": host_statement_sha,
            "meta_statement_normalized_sha256": normalized_statement_sha,
            "payload_sha256": payload_sha,
            "mcp_pid": 123,
        }
        statement_wrapper = {
            "timestamp_utc": events[1]["timestamp_utc"],
            "channel": "statement_checks",
            "record": statement_record,
        }
        reference_wrappers = [
            {
                "timestamp_utc": reference_append_events[index]["timestamp_utc"],
                "channel": "reference_checks",
                "record": record,
            }
            for index, record in enumerate(reference_records)
        ]
        canonical_call_specs = []
        validated_sha = None
        for tool, arguments, structured in call_specs:
            arguments = copy.deepcopy(arguments)
            structured = copy.deepcopy(structured)
            if tool == "memory_init":
                arguments = {
                    "run_id": run_id,
                    "meta": {
                        "statement": meta_statement,
                    },
                }
                structured = {
                    "status": "ok",
                    "run_id": run_id,
                    "phase": "initialized",
                    "statement_sha256": host_statement_sha,
                    "statement_normalized_sha256": normalized_statement_sha,
                    "host_statement_sha256": host_statement_sha,
                }
            elif tool == "memory_query":
                channel = arguments["channel"]
                items = (
                    [statement_wrapper]
                    if channel == "statement_checks"
                    else reference_wrappers
                )
                structured = {
                    "run_id": run_id,
                    "channel": channel,
                    "count": len(items),
                    "items": copy.deepcopy(items),
                }
            elif tool == "validate_verification_output":
                validation_errors = SERVICE._validate_result_payload(
                    arguments["payload"]
                )
                is_valid = not validation_errors
                if is_valid:
                    validated_sha = SERVICE._sha256_bytes(
                        SERVICE._canonical_json_bytes(arguments["payload"])
                    )
                structured = {"valid": is_valid, "errors": validation_errors}
            elif tool == "write_verification_output":
                structured = {
                    "status": "ok",
                    "run_id": run_id,
                    "output_path": str(self.results_root / run_id / "verification.json"),
                    "receipt_path": str(self.receipts_root / f"{run_id}.json"),
                    "payload_sha256": validated_sha,
                }
            canonical_call_specs.append((tool, arguments, structured))

        fixture = {
            "run_id": run_id,
            "run_memory": run_memory,
            "events": events,
            "statement_records": [statement_record],
            "reference_records": reference_records,
            "payload": payload,
            "state": state,
            "receipt": receipt,
            "runtime_before": runtime_before,
        }
        self._refresh(fixture)

        records = [{"type": "thread.started", "thread_id": "thread"}, {"type": "turn.started"}]
        for index, (tool, arguments, structured) in enumerate(
            canonical_call_specs, start=1
        ):
            records.extend(
                completed_mcp_pair(f"call_{index}", tool, arguments, structured)
            )
        records.append(
            {
                "type": "turn.completed",
                "usage": {
                    "input_tokens": 0,
                    "cached_input_tokens": 0,
                    "cache_write_input_tokens": 0,
                    "output_tokens": 0,
                    "reasoning_output_tokens": 0,
                },
            }
        )
        calls, binding_errors = SERVICE._completed_mcp_calls(records)
        fixture["records"] = records
        fixture["calls"] = calls
        fixture["binding_errors"] = binding_errors
        return fixture

    def _refresh(self, fixture):
        events = fixture["events"]
        run_memory = fixture["run_memory"]
        fixture["state"]["events"] = events
        fixture["state"]["channel_counts"]["events"] = len(events)
        fixture["state"]["tool_counts"] = dict(
            Counter(event["tool"] for event in events)
        )
        fixture["receipt"]["events"] = events
        fixture["receipt"]["channel_counts"] = fixture["state"]["channel_counts"]
        fixture["receipt"]["tool_counts"] = fixture["state"]["tool_counts"]
        statement_append_events = [
            event
            for event in events
            if event["tool"] == "memory_append"
            and event.get("detail", {}).get("channel") == "statement_checks"
        ]
        self._write_jsonl(
            run_memory / "statement_checks.jsonl",
            [
                {
                    "timestamp_utc": statement_append_events[index]["timestamp_utc"],
                    "channel": "statement_checks",
                    "record": record,
                }
                for index, record in enumerate(fixture["statement_records"])
            ],
        )
        self._write_jsonl(
            run_memory / "reference_checks.jsonl",
            [
                {
                    "timestamp_utc": next(
                        event["timestamp_utc"]
                        for event in events
                        if event.get("detail", {}).get("channel")
                        == "reference_checks"
                        and event.get("detail", {}).get("index") == index
                    ),
                    "channel": "reference_checks",
                    "record": record,
                }
                for index, record in enumerate(
                    fixture["reference_records"], start=1
                )
            ],
        )
        self._write_jsonl(
            run_memory / "events.jsonl",
            [
                {"timestamp_utc": event["timestamp_utc"], "record": event}
                for event in events
            ],
        )
        self._write_json(run_memory / "state.json", fixture["state"])
        fixture["receipt"]["memory_files_sha256"] = {
            path.name: SERVICE._sha256_file(path)
            for path in sorted(run_memory.iterdir())
        }

    def _external_fixture(self):
        run_id = self._testMethodName
        theorem_query = "full theorem statement"
        fixed_query = "local potential"
        theorem_result = self._with_digest(
            {
                "status": "ok",
                "query": theorem_query,
                "count": 1,
                "results": [
                    {
                        "title": "A source",
                        "theorem": "A theorem",
                        "arxiv_id": "0000.00000",
                        "theorem_id": "Theorem 1",
                    }
                ],
            }
        )
        source_sha = SERVICE._sha256_file(self.source_path)
        fixed_result = self._with_digest(
            {
                "source_id": "cld_1204_6277",
                "source_sha256": source_sha,
                "query": fixed_query,
                "count": 1,
                "hits": [
                    {
                        "match_line": 2,
                        "start_line": 2,
                        "end_line": 2,
                        "text": "2: local potential",
                    }
                ],
            }
        )
        read_result = {
            "source_id": "cld_1204_6277",
            "source_sha256": source_sha,
            "start_line": 2,
            "end_line": 2,
            "text": "2: local potential",
        }
        events = [
            self._event(1, "memory_init", {"host_statement_sha256": "0" * 64}),
            self._event(2, "memory_append", {"channel": "statement_checks", "index": 1}),
            self._event(
                3,
                "search_arxiv_theorems",
                {
                    "query_sha256": SERVICE._sha256_text(theorem_query),
                    "status": "ok",
                    "count": 1,
                    "result_sha256": theorem_result["result_sha256"],
                },
            ),
            self._event(
                4,
                "search_fixed_source",
                {
                    "source_id": "cld_1204_6277",
                    "query_sha256": SERVICE._sha256_text(fixed_query),
                    "hits": 1,
                    "result_sha256": fixed_result["result_sha256"],
                },
            ),
            self._event(
                5,
                "read_fixed_source_lines",
                {"source_id": "cld_1204_6277", "start_line": 2, "end_line": 2},
            ),
        ]
        simplified = {
            "location": "Proof, cited step",
            "status": "verified",
            "search_query": theorem_query,
            "search_evidence": ["The theorem statement was compared."],
            "source_evidence": [
                {
                    "source_id": "cld_1204_6277",
                    "search_query": fixed_query,
                    "line_ranges": [{"start_line": 2, "end_line": 2}],
                    "comparison": "The source hypotheses agree.",
                }
            ],
            "contextual_definition_comparison": "Definitions agree.",
            "applicability": "All assumptions hold.",
            "critical_errors": [],
            "gaps": [],
            "detail": "Complete external-reference audit.",
        }
        canonical, binding = canonicalize_external_reference_record(
            simplified, events, {"cld_1204_6277": self.source_path}
        )
        payload = self._payload()
        payload_sha = SERVICE._sha256_bytes(SERVICE._canonical_json_bytes(payload))
        events.extend(
            [
                self._event(
                    6,
                    "memory_append_reference",
                    {"channel": "reference_checks", "index": 1, **binding},
                ),
                self._event(7, "memory_query", {"channel": "statement_checks", "returned": 1}),
                self._event(8, "memory_query", {"channel": "reference_checks", "returned": 1}),
                self._event(9, "validate_verification_output", {"valid": True, "payload_sha256": payload_sha}),
                self._event(10, "write_verification_output", {"payload_sha256": payload_sha}),
            ]
        )
        call_specs = [
            ("memory_init", {"run_id": run_id, "meta": {}}, {"status": "ok"}),
            (
                "memory_append",
                {
                    "run_id": run_id,
                    "channel": "statement_checks",
                    "record": self._statement_record(),
                },
                {
                    "status": "ok",
                    "run_id": run_id,
                    "channel": "statement_checks",
                    "index": 1,
                },
            ),
            ("search_arxiv_theorems", {"query": theorem_query, "num_results": 1}, theorem_result),
            ("search_fixed_source", {"source_id": "cld_1204_6277", "query": fixed_query, "context_lines": 0, "max_hits": 1}, fixed_result),
            ("read_fixed_source_lines", {"source_id": "cld_1204_6277", "start_line": 2, "end_line": 2}, read_result),
            (
                "memory_append_reference",
                {"run_id": run_id, "record": simplified},
                {
                    "status": "ok",
                    "run_id": run_id,
                    "channel": "reference_checks",
                    "index": 1,
                    "canonical_record_sha256": binding[
                        "canonical_record_sha256"
                    ],
                },
            ),
            ("memory_query", {"run_id": run_id, "channel": "statement_checks"}, {"status": "ok"}),
            ("memory_query", {"run_id": run_id, "channel": "reference_checks"}, {"status": "ok"}),
            ("validate_verification_output", {"run_id": run_id, "payload": payload}, {"valid": True}),
            ("write_verification_output", {"run_id": run_id, "payload": payload}, {"status": "ok"}),
        ]
        runtime_before = {
            "sources/cld_1204.6277.txt": {"sha256": source_sha}
        }
        return self._materialize(
            events, [canonical], call_specs, runtime_before
        )

    def _three_source_fixture(self):
        run_id = self._testMethodName
        theorem_query = "three fixed sources"
        theorem_result = self._with_digest(
            {
                "status": "ok",
                "query": theorem_query,
                "count": 1,
                "results": [
                    {
                        "title": "Three sources",
                        "theorem": "A theorem using three sources",
                        "arxiv_id": "0000.00000",
                        "theorem_id": "Theorem 1",
                    }
                ],
            }
        )
        source_specs = [
            ("bmps_2603_08664", "Definition 2.31"),
            ("gk_1406_7637", "(1.4.3)"),
            ("gk_1509_09079", "Theorem 8.4"),
        ]
        events = [
            self._event(1, "memory_init", {"host_statement_sha256": "0" * 64}),
            self._event(2, "memory_append", {"channel": "statement_checks", "index": 1}),
            self._event(
                3,
                "search_arxiv_theorems",
                {
                    "query_sha256": SERVICE._sha256_text(theorem_query),
                    "status": "ok",
                    "count": 1,
                    "result_sha256": theorem_result["result_sha256"],
                },
            ),
        ]
        call_specs = [
            ("memory_init", {"run_id": run_id, "meta": {}}, {"status": "ok"}),
            (
                "memory_append",
                {"run_id": run_id, "channel": "statement_checks", "record": self._statement_record()},
                {"status": "ok", "run_id": run_id, "channel": "statement_checks", "index": 1},
            ),
            ("search_arxiv_theorems", {"query": theorem_query, "num_results": 1}, theorem_result),
        ]
        source_evidence = []
        runtime_before = {}
        for source_id, query in source_specs:
            path = self.source_paths[source_id]
            source_sha = SERVICE._sha256_file(path)
            relative = SERVICE.FIXED_SOURCE_RUNTIME_PATHS[source_id]
            runtime_before[relative] = {"sha256": source_sha}
            fixed_result = self._with_digest(
                {
                    "source_id": source_id,
                    "source_sha256": source_sha,
                    "query": query,
                    "count": 1,
                    "hits": [
                        {
                            "match_line": 2,
                            "start_line": 2,
                            "end_line": 2,
                            "text": f"2: {query}",
                        }
                    ],
                }
            )
            read_result = {
                "source_id": source_id,
                "source_sha256": source_sha,
                "start_line": 2,
                "end_line": 2,
                "text": f"2: {query}",
            }
            search_sequence = len(events) + 1
            events.append(
                self._event(
                    search_sequence,
                    "search_fixed_source",
                    {
                        "source_id": source_id,
                        "query_sha256": SERVICE._sha256_text(query),
                        "hits": 1,
                        "result_sha256": fixed_result["result_sha256"],
                    },
                )
            )
            events.append(
                self._event(
                    search_sequence + 1,
                    "read_fixed_source_lines",
                    {"source_id": source_id, "start_line": 2, "end_line": 2},
                )
            )
            call_specs.extend(
                [
                    (
                        "search_fixed_source",
                        {"source_id": source_id, "query": query, "context_lines": 0, "max_hits": 1},
                        fixed_result,
                    ),
                    (
                        "read_fixed_source_lines",
                        {"source_id": source_id, "start_line": 2, "end_line": 2},
                        read_result,
                    ),
                ]
            )
            source_evidence.append(
                {
                    "source_id": source_id,
                    "search_query": query,
                    "line_ranges": [{"start_line": 2, "end_line": 2}],
                    "comparison": f"The {source_id} hypotheses agree.",
                }
            )
        simplified = {
            "location": "Proof, three-source step",
            "status": "verified",
            "search_query": theorem_query,
            "search_evidence": ["The theorem statement was compared."],
            "source_evidence": source_evidence,
            "contextual_definition_comparison": "All three source definitions agree.",
            "applicability": "All source assumptions hold.",
            "critical_errors": [],
            "gaps": [],
            "detail": "Complete three-source external-reference audit.",
        }
        canonical, binding = canonicalize_external_reference_record(
            simplified,
            events,
            {source_id: self.source_paths[source_id] for source_id, _ in source_specs},
        )
        append_sequence = len(events) + 1
        events.append(
            self._event(
                append_sequence,
                "memory_append_reference",
                {"channel": "reference_checks", "index": 1, **binding},
            )
        )
        payload = self._payload()
        payload_sha = SERVICE._sha256_bytes(SERVICE._canonical_json_bytes(payload))
        events.extend(
            [
                self._event(append_sequence + 1, "memory_query", {"channel": "statement_checks", "returned": 1}),
                self._event(append_sequence + 2, "memory_query", {"channel": "reference_checks", "returned": 1}),
                self._event(append_sequence + 3, "validate_verification_output", {"valid": True, "payload_sha256": payload_sha}),
                self._event(append_sequence + 4, "write_verification_output", {"payload_sha256": payload_sha}),
            ]
        )
        call_specs.extend(
            [
                (
                    "memory_append_reference",
                    {"run_id": run_id, "record": simplified},
                    {
                        "status": "ok",
                        "run_id": run_id,
                        "channel": "reference_checks",
                        "index": 1,
                        "canonical_record_sha256": binding["canonical_record_sha256"],
                    },
                ),
                ("memory_query", {"run_id": run_id, "channel": "statement_checks"}, {"status": "ok"}),
                ("memory_query", {"run_id": run_id, "channel": "reference_checks"}, {"status": "ok"}),
                ("validate_verification_output", {"run_id": run_id, "payload": payload}, {"valid": True}),
                ("write_verification_output", {"run_id": run_id, "payload": payload}, {"status": "ok"}),
            ]
        )
        fixture = self._materialize(events, [canonical], call_specs, runtime_before)
        fixture.update(
            {
                "three_source_simplified": simplified,
                "three_source_ids": [source_id for source_id, _ in source_specs],
            }
        )
        return fixture

    def _no_reference_fixture(self):
        run_id = self._testMethodName
        payload = self._payload()
        payload_sha = SERVICE._sha256_bytes(SERVICE._canonical_json_bytes(payload))
        events = [
            self._event(1, "memory_init", {"host_statement_sha256": "0" * 64}),
            self._event(2, "memory_append", {"channel": "statement_checks", "index": 1}),
            self._event(3, "memory_append", {"channel": "reference_checks", "index": 1}),
            self._event(4, "memory_query", {"channel": "statement_checks", "returned": 1}),
            self._event(5, "memory_query", {"channel": "reference_checks", "returned": 1}),
            self._event(6, "validate_verification_output", {"valid": True, "payload_sha256": payload_sha}),
            self._event(7, "write_verification_output", {"payload_sha256": payload_sha}),
        ]
        statement_record = self._statement_record()
        no_reference_record = self._no_reference_record()
        call_specs = [
            ("memory_init", {"run_id": run_id, "meta": {}}, {"status": "ok"}),
            (
                "memory_append",
                {
                    "run_id": run_id,
                    "channel": "statement_checks",
                    "record": statement_record,
                },
                {
                    "status": "ok",
                    "run_id": run_id,
                    "channel": "statement_checks",
                    "index": 1,
                },
            ),
            (
                "memory_append",
                {
                    "run_id": run_id,
                    "channel": "reference_checks",
                    "record": no_reference_record,
                },
                {
                    "status": "ok",
                    "run_id": run_id,
                    "channel": "reference_checks",
                    "index": 1,
                },
            ),
            ("memory_query", {"run_id": run_id, "channel": "statement_checks"}, {"status": "ok"}),
            ("memory_query", {"run_id": run_id, "channel": "reference_checks"}, {"status": "ok"}),
            ("validate_verification_output", {"run_id": run_id, "payload": payload}, {"valid": True}),
            ("write_verification_output", {"run_id": run_id, "payload": payload}, {"status": "ok"}),
        ]
        return self._materialize(
            events, [no_reference_record], call_specs, {}
        )

    def _finding_fixture(self, early_payload=None):
        run_id = self._testMethodName
        finding = {
            "location": "Proof, step 1",
            "issue": "The asserted implication is unsupported.",
            "severity": "critical",
        }
        statement_record = {
            "record_type": "statement_check",
            "location": "Proof, step 1",
            "status": "failed",
            "critical_errors": [copy.deepcopy(finding)],
            "gaps": [],
            "detail": "The step has a critical error.",
        }
        payload = {
            "verification_report": {
                "summary": "One critical error was found.",
                "critical_errors": [copy.deepcopy(finding)],
                "gaps": [],
            },
            "verdict": "wrong",
            "repair_hints": "Repair the unsupported implication.",
        }
        payload_sha = SERVICE._sha256_bytes(SERVICE._canonical_json_bytes(payload))
        events = [
            self._event(1, "memory_init", {"host_statement_sha256": "0" * 64}),
            self._event(2, "memory_append", {"channel": "statement_checks", "index": 1}),
            self._event(3, "memory_append", {"channel": "reference_checks", "index": 1}),
            self._event(4, "memory_query", {"channel": "statement_checks", "returned": 1}),
            self._event(5, "memory_query", {"channel": "reference_checks", "returned": 1}),
        ]
        call_specs = [
            ("memory_init", {"run_id": run_id, "meta": {}}, {"status": "ok"}),
            (
                "memory_append",
                {
                    "run_id": run_id,
                    "channel": "statement_checks",
                    "record": statement_record,
                },
                {
                    "status": "ok",
                    "run_id": run_id,
                    "channel": "statement_checks",
                    "index": 1,
                },
            ),
            (
                "memory_append",
                {
                    "run_id": run_id,
                    "channel": "reference_checks",
                    "record": self._no_reference_record(),
                },
                {
                    "status": "ok",
                    "run_id": run_id,
                    "channel": "reference_checks",
                    "index": 1,
                },
            ),
            ("memory_query", {"run_id": run_id, "channel": "statement_checks"}, {}),
            ("memory_query", {"run_id": run_id, "channel": "reference_checks"}, {}),
        ]
        next_sequence = 6
        if early_payload is not None:
            early_errors = SERVICE._validate_result_payload(early_payload)
            early_valid = not early_errors
            early_sha = (
                SERVICE._sha256_bytes(SERVICE._canonical_json_bytes(early_payload))
                if early_valid
                else None
            )
            events.append(
                self._event(
                    next_sequence,
                    "validate_verification_output",
                    {"valid": early_valid, "payload_sha256": early_sha},
                )
            )
            call_specs.append(
                (
                    "validate_verification_output",
                    {"run_id": run_id, "payload": copy.deepcopy(early_payload)},
                    {},
                )
            )
            next_sequence += 1
        events.extend(
            [
                self._event(
                    next_sequence,
                    "validate_verification_output",
                    {"valid": True, "payload_sha256": payload_sha},
                ),
                self._event(
                    next_sequence + 1,
                    "write_verification_output",
                    {"payload_sha256": payload_sha},
                ),
            ]
        )
        call_specs.extend(
            [
                (
                    "validate_verification_output",
                    {"run_id": run_id, "payload": payload},
                    {},
                ),
                (
                    "write_verification_output",
                    {"run_id": run_id, "payload": payload},
                    {},
                ),
            ]
        )
        return self._materialize(
            events,
            [self._no_reference_record()],
            call_specs,
            {},
            payload=payload,
            statement_record=statement_record,
        )

    def _replay(self, fixture, calls=None):
        return SERVICE._replay_memory(
            fixture["run_id"],
            fixture["payload"],
            fixture["receipt"],
            fixture["runtime_before"],
            fixture["calls"] if calls is None else calls,
        )

    def _complete_receipt(self, fixture):
        output_path = self.results_root / fixture["run_id"] / "verification.json"
        self._write_json(output_path, fixture["payload"])
        runtime_before = {
            "hardened_mcp.py": {"sha256": "1" * 64},
            "canonical_reference.py": {"sha256": "2" * 64},
            "release_pins.py": {
                "sha256": SERVICE.EXPECTED_RELEASE_PINS_FILE_SHA256
            },
            SERVICE.MODEL_CATALOG_RELATIVE_PATH: {
                "sha256": SERVICE.EXPECTED_MODEL_CATALOG_SHA256
            },
            "verification_output.schema.json": {"sha256": "3" * 64},
            "memory_record.schema.json": {"sha256": "4" * 64},
        }
        source_hashes = {}
        for source_id, relative in SERVICE.FIXED_SOURCE_RUNTIME_PATHS.items():
            digest = SERVICE._sha256_file(self.source_paths[source_id])
            runtime_before[relative] = {"sha256": digest}
            source_hashes[source_id] = digest
        fixture["runtime_before"] = runtime_before
        fixture["receipt"].update(
            {
                "format": "rethlas-hardened-completion-receipt-v1",
                "runtime_contract_version": SERVICE.RUNTIME_CONTRACT_VERSION,
                "release_pinset_sha256": SERVICE.EXPECTED_RELEASE_PINSET_SHA256,
                "release_pins_file_sha256": SERVICE.EXPECTED_RELEASE_PINS_FILE_SHA256,
                "model_catalog_runtime_path": SERVICE.MODEL_CATALOG_RELATIVE_PATH,
                "model_catalog_sha256": SERVICE.EXPECTED_MODEL_CATALOG_SHA256,
                "model_catalog_model": SERVICE.MODEL,
                "model_catalog_reasoning_effort": SERVICE.REASONING_EFFORT,
                "run_id": fixture["run_id"],
                "nonce": "6" * 64,
                "output_file_sha256": SERVICE._sha256_file(output_path),
                "output_path": str(output_path),
                "phase": "finalized",
                "mcp_runtime_sha256": "1" * 64,
                "canonical_reference_sha256": "2" * 64,
                "schema_sha256": "3" * 64,
                "memory_record_schema_sha256": "4" * 64,
                "source_sha256": source_hashes,
                "source_bundle_sha256": {
                    relative: str(pin["sha256"])
                    for relative, pin in SERVICE.SOURCE_BUNDLE_PINS.items()
                },
                "completed_at_utc": fixture["events"][-1]["timestamp_utc"],
            }
        )
        return runtime_before

    def _full_gate_errors(self, fixture):
        runtime_before = self._complete_receipt(fixture)
        return SERVICE._verify_receipt(
            fixture["receipt"],
            fixture["payload"],
            fixture["run_id"],
            "6" * 64,
            "Host-bound test statement",
            "Host-bound test proof",
            runtime_before,
            fixture["calls"],
        )

    def test_host_replay_accepts_transcript_bound_external_reference(self):
        fixture = self._external_fixture()
        self.assertEqual(fixture["binding_errors"], [])
        self.assertEqual(SERVICE._tool_evidence(fixture["records"])["structural_errors"], [])
        self.assertEqual(self._replay(fixture), [])

    def test_full_receipt_gate_accepts_external_reference_fixture(self):
        fixture = self._external_fixture()
        self.assertEqual(self._full_gate_errors(fixture), [])

    def test_host_replay_accepts_three_new_source_fixture(self):
        fixture = self._three_source_fixture()
        self.assertEqual(fixture["binding_errors"], [])
        self.assertEqual(SERVICE._tool_evidence(fixture["records"])["structural_errors"], [])
        self.assertEqual(self._replay(fixture), [])

    def test_full_receipt_gate_accepts_three_new_source_fixture(self):
        fixture = self._three_source_fixture()
        self.assertEqual(
            [item["source_id"] for item in fixture["reference_records"][0]["source_evidence"]],
            fixture["three_source_ids"],
        )
        self.assertEqual(self._full_gate_errors(fixture), [])

    def test_new_source_search_and_read_body_tampering_is_rejected(self):
        fixture = self._three_source_fixture()
        for search_index, read_index in ((3, 4), (5, 6), (7, 8)):
            with self.subTest(search_index=search_index):
                calls = copy.deepcopy(fixture["calls"])
                forged = dict(calls[search_index]["structured_content"])
                forged["count"] = 0
                forged["hits"] = []
                digest_body = dict(forged)
                digest_body.pop("result_sha256")
                forged["result_sha256"] = SERVICE._sha256_bytes(
                    SERVICE._canonical_json_bytes(digest_body)
                )
                calls[search_index]["structured_content"] = forged
                errors = self._replay(fixture, calls)
                self.assertTrue(any("source-byte recomputation" in error for error in errors), errors)
            with self.subTest(read_index=read_index):
                calls = copy.deepcopy(fixture["calls"])
                calls[read_index]["structured_content"]["text"] = "2: forged"
                errors = self._replay(fixture, calls)
                self.assertTrue(any("source-byte recomputation" in error for error in errors), errors)

    def test_new_source_boolean_bounds_and_ranges_are_rejected(self):
        fixture = self._three_source_fixture()
        for search_index, read_index in ((3, 4), (5, 6), (7, 8)):
            calls = copy.deepcopy(fixture["calls"])
            calls[search_index]["arguments"]["max_hits"] = True
            errors = self._replay(fixture, calls)
            self.assertTrue(any("strict bounded integer" in error for error in errors), errors)
            calls = copy.deepcopy(fixture["calls"])
            calls[read_index]["arguments"]["start_line"] = True
            errors = self._replay(fixture, calls)
            self.assertTrue(any("strict valid integer range" in error for error in errors), errors)

    def test_new_source_event_record_manifest_tampering_is_rejected(self):
        fixture = self._three_source_fixture()
        pristine_events = copy.deepcopy(fixture["events"])
        pristine_records = copy.deepcopy(fixture["reference_records"])
        for evidence_index, search_event_index in enumerate((3, 5, 7)):
            fixture["events"][:] = copy.deepcopy(pristine_events)
            fixture["reference_records"][:] = copy.deepcopy(pristine_records)
            event = fixture["events"][search_event_index]
            evidence = fixture["reference_records"][0]["source_evidence"][evidence_index]
            event["detail"]["hits"] = 2
            event["detail"]["result_sha256"] = "e" * 64
            evidence["search_result_count"] = 2
            evidence["search_result_sha256"] = "e" * 64
            fixture["events"][9]["detail"]["canonical_record_sha256"] = (
                SERVICE._sha256_bytes(
                    SERVICE._canonical_json_bytes(fixture["reference_records"][0])
                )
            )
            self._refresh(fixture)
            errors = self._replay(fixture)
            self.assertTrue(
                any("fixed_source" in error and "transcript call" in error for error in errors),
                errors,
            )
        fixture["events"][:] = pristine_events
        fixture["reference_records"][:] = pristine_records
        self._refresh(fixture)

    def test_new_source_positive_hit_ordering_and_allowlist_fail_closed(self):
        fixture = self._three_source_fixture()
        source_map = {
            source_id: self.source_paths[source_id]
            for source_id in fixture["three_source_ids"]
        }
        for evidence_index, (search_event_index, read_event_index) in enumerate(((3, 4), (5, 6), (7, 8))):
            no_hit_events = copy.deepcopy(fixture["events"][:9])
            no_hit_events[search_event_index]["detail"]["hits"] = 0
            with self.subTest(kind="zero_hit", evidence_index=evidence_index):
                canonical, _ = canonicalize_external_reference_record(
                    fixture["three_source_simplified"], no_hit_events, source_map
                )
                errors = SERVICE._memory_record_validation_errors(
                    "reference_checks", canonical
                )
                self.assertTrue(errors, canonical)
            wrong_order_events = copy.deepcopy(fixture["events"][:9])
            wrong_order_events[read_event_index]["sequence"] = wrong_order_events[search_event_index]["sequence"]
            with self.subTest(kind="wrong_order", evidence_index=evidence_index):
                with self.assertRaisesRegex(ValueError, "fixed-source-search < read"):
                    canonicalize_external_reference_record(
                        fixture["three_source_simplified"], wrong_order_events, source_map
                    )
        unknown = copy.deepcopy(fixture["three_source_simplified"])
        unknown["source_evidence"][0]["source_id"] = "BMPS_2603_08664"
        with self.assertRaisesRegex(ValueError, "not allowlisted"):
            canonicalize_external_reference_record(unknown, fixture["events"][:9], source_map)

    def test_receipt_exact_source_keyset_and_digest_routing(self):
        fixture = self._three_source_fixture()
        runtime_before = self._complete_receipt(fixture)
        expected_ids = set(SERVICE.FIXED_SOURCE_RUNTIME_PATHS)
        self.assertEqual(set(fixture["receipt"]["source_sha256"]), expected_ids)
        for source_id, relative in SERVICE.FIXED_SOURCE_RUNTIME_PATHS.items():
            with self.subTest(source_id=source_id):
                self.assertEqual(
                    fixture["receipt"]["source_sha256"][source_id],
                    runtime_before[relative]["sha256"],
                )

    def test_receipt_source_keyset_and_digest_mutations_are_rejected(self):
        mutations = []
        fixture = self._three_source_fixture()
        self._complete_receipt(fixture)
        missing = copy.deepcopy(fixture["receipt"])
        missing["source_sha256"].pop("bmps_2603_08664")
        mutations.append(missing)
        extra = copy.deepcopy(fixture["receipt"])
        extra["source_sha256"]["unknown"] = "a" * 64
        mutations.append(extra)
        swapped = copy.deepcopy(fixture["receipt"])
        swapped["source_sha256"]["bmps_2603_08664"], swapped["source_sha256"]["gk_1406_7637"] = (
            swapped["source_sha256"]["gk_1406_7637"],
            swapped["source_sha256"]["bmps_2603_08664"],
        )
        mutations.append(swapped)
        for invalid in ("A" * 64, "a" * 63, True, 1, None):
            receipt = copy.deepcopy(fixture["receipt"])
            receipt["source_sha256"]["gk_1509_09079"] = invalid
            mutations.append(receipt)
        for receipt in mutations:
            with self.subTest(source_sha256=receipt.get("source_sha256")):
                errors = SERVICE._verify_receipt(
                    receipt,
                    fixture["payload"],
                    fixture["run_id"],
                    "6" * 64,
                    "Host-bound test statement",
                    "Host-bound test proof",
                    fixture["runtime_before"],
                    fixture["calls"],
                )
                self.assertTrue(
                    any("source digest" in error or "runtime digest mismatch" in error for error in errors),
                    errors,
                )

    def test_host_replay_accepts_transcript_bound_no_reference_path(self):
        fixture = self._no_reference_fixture()
        self.assertEqual(fixture["binding_errors"], [])
        self.assertEqual(self._replay(fixture), [])

    def test_full_receipt_gate_accepts_no_reference_fixture(self):
        fixture = self._no_reference_fixture()
        self.assertEqual(self._full_gate_errors(fixture), [])

    def test_full_receipt_gate_rejects_symlinked_output(self):
        fixture = self._no_reference_fixture()
        runtime_before = self._complete_receipt(fixture)
        output_path = self.results_root / fixture["run_id"] / "verification.json"
        target = self.root / "forged-output.json"
        target.write_bytes(output_path.read_bytes())
        output_path.unlink()
        output_path.symlink_to(target)
        errors = SERVICE._verify_receipt(
            fixture["receipt"],
            fixture["payload"],
            fixture["run_id"],
            "6" * 64,
            "Host-bound test statement",
            "Host-bound test proof",
            runtime_before,
            fixture["calls"],
        )
        self.assertTrue(any("symlinked" in error for error in errors), errors)

    def test_host_replay_accepts_finding_complete_payload(self):
        fixture = self._finding_fixture()
        self.assertEqual(fixture["binding_errors"], [])
        self.assertEqual(self._replay(fixture), [])

    def test_schema_invalid_validation_then_correct_payload_is_accepted(self):
        fixture = self._finding_fixture(
            early_payload={
                "verification_report": {
                    "summary": "invalid draft",
                    "critical_errors": [],
                    "gaps": [],
                },
                "verdict": "wrong",
                "repair_hints": "",
            }
        )
        self.assertEqual(fixture["binding_errors"], [])
        self.assertEqual(self._replay(fixture), [])

    def test_schema_valid_dropped_finding_then_correct_payload_is_rejected(self):
        dropped = self._payload()
        fixture = self._finding_fixture(early_payload=dropped)
        errors = self._replay(fixture)
        self.assertTrue(
            any("finding multiset differs" in error for error in errors), errors
        )

    def test_memory_init_argument_tamper_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[0]["arguments"]["meta"]["statement"] = "different"
        errors = self._replay(fixture, calls)
        self.assertTrue(any("memory_init" in error for error in errors), errors)

    def test_memory_init_extra_meta_key_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[0]["arguments"]["meta"]["input_shape"] = "proof_markdown_text"
        errors = self._replay(fixture, calls)
        self.assertTrue(any("meta argument keys" in error for error in errors), errors)

    def test_memory_init_response_tamper_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[0]["structured_content"]["statement_sha256"] = "f" * 64
        errors = self._replay(fixture, calls)
        self.assertTrue(any("response differs" in error for error in errors), errors)

    def test_memory_init_event_extra_key_is_rejected(self):
        fixture = self._no_reference_fixture()
        fixture["events"][0]["detail"]["unexpected"] = True
        self._refresh(fixture)
        errors = self._replay(fixture)
        self.assertTrue(any("meta reconstruction" in error for error in errors), errors)

    def test_coordinated_filtered_empty_query_full_claim_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[3]["arguments"].update(
            {"contains": "definitely-no-match", "limit": 1, "reverse": False}
        )
        calls[3]["structured_content"] = {
            "run_id": fixture["run_id"],
            "channel": "statement_checks",
            "count": 0,
            "items": [],
        }
        fixture["events"][3]["detail"]["returned"] = 0
        self._refresh(fixture)
        errors = self._replay(fixture, calls)
        self.assertTrue(
            any("full-query channels differ" in error for error in errors), errors
        )

    def test_memory_query_boolean_limit_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[3]["arguments"]["limit"] = True
        errors = self._replay(fixture, calls)
        self.assertTrue(any("strict bounded integer" in error for error in errors), errors)

    def test_memory_query_nonboolean_reverse_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[3]["arguments"]["reverse"] = 1
        errors = self._replay(fixture, calls)
        self.assertTrue(any("strict boolean" in error for error in errors), errors)

    def test_memory_query_reverse_true_is_not_a_complete_final_query(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[3]["arguments"]["reverse"] = True
        errors = self._replay(fixture, calls)
        self.assertTrue(
            any("full-query channels differ" in error for error in errors), errors
        )

    def test_memory_query_boolean_result_count_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[3]["structured_content"]["count"] = True
        errors = self._replay(fixture, calls)
        self.assertTrue(any("response differs" in error for error in errors), errors)

    def test_memory_query_item_body_tamper_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[3]["structured_content"]["items"][0]["record"]["detail"] = "forged"
        errors = self._replay(fixture, calls)
        self.assertTrue(any("persisted-channel replay" in error for error in errors), errors)

    def test_memory_query_event_return_tamper_is_rejected(self):
        fixture = self._no_reference_fixture()
        fixture["events"][3]["detail"]["returned"] = False
        self._refresh(fixture)
        errors = self._replay(fixture)
        self.assertTrue(any("persisted-channel replay" in error for error in errors), errors)

    def test_late_append_invalidates_prior_full_query(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        second_record = self._statement_record()
        second_record["location"] = "Proof, step 2"
        second_record["detail"] = "The second step is valid."
        late_event = self._event(
            6,
            "memory_append",
            {"channel": "statement_checks", "index": 2},
        )
        fixture["events"].insert(5, late_event)
        for sequence, event in enumerate(fixture["events"], start=1):
            event["sequence"] = sequence
        calls.insert(
            5,
            {
                "call_id": "late_append",
                "server": "verification_agent",
                "tool": "memory_append",
                "arguments": {
                    "run_id": fixture["run_id"],
                    "channel": "statement_checks",
                    "record": second_record,
                },
                "structured_content": {
                    "status": "ok",
                    "run_id": fixture["run_id"],
                    "channel": "statement_checks",
                    "index": 2,
                },
            },
        )
        fixture["statement_records"].append(second_record)
        fixture["state"]["channel_counts"]["statement_checks"] = 2
        self._refresh(fixture)
        errors = self._replay(fixture, calls)
        self.assertTrue(
            any("fresh complete queries" in error for error in errors), errors
        )

    def test_changed_theorem_response_with_event_anchor_unchanged_is_rejected(self):
        fixture = self._external_fixture()
        calls = copy.deepcopy(fixture["calls"])
        changed = copy.deepcopy(calls[2]["structured_content"])
        changed["results"][0]["theorem"] = "rewritten theorem body"
        base = copy.deepcopy(changed)
        base.pop("result_sha256")
        changed["result_sha256"] = SERVICE._sha256_bytes(
            SERVICE._canonical_json_bytes(base)
        )
        calls[2]["structured_content"] = changed
        errors = self._replay(fixture, calls)
        self.assertTrue(
            any("does not match transcript call" in error for error in errors), errors
        )

    def test_validate_payload_tamper_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[5]["arguments"]["payload"]["verification_report"]["summary"] = "different"
        errors = self._replay(fixture, calls)
        self.assertTrue(any("eventual payload" in error for error in errors), errors)

    def test_validate_response_tamper_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[5]["structured_content"] = {"valid": False, "errors": []}
        errors = self._replay(fixture, calls)
        self.assertTrue(any("independent validation" in error for error in errors), errors)

    def test_validate_event_extra_key_is_rejected(self):
        fixture = self._no_reference_fixture()
        fixture["events"][5]["detail"]["unexpected"] = True
        self._refresh(fixture)
        errors = self._replay(fixture)
        self.assertTrue(any("independent validation" in error for error in errors), errors)

    def test_write_payload_tamper_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[6]["arguments"]["payload"]["verification_report"]["summary"] = "different"
        errors = self._replay(fixture, calls)
        self.assertTrue(any("eventual host payload" in error for error in errors), errors)

    def test_write_response_path_tamper_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = copy.deepcopy(fixture["calls"])
        calls[6]["structured_content"]["output_path"] = "/forged/output.json"
        errors = self._replay(fixture, calls)
        self.assertTrue(any("host paths" in error for error in errors), errors)

    def test_write_event_extra_key_is_rejected(self):
        fixture = self._no_reference_fixture()
        fixture["events"][6]["detail"]["unexpected"] = True
        self._refresh(fixture)
        errors = self._replay(fixture)
        self.assertTrue(any("eventual payload" in error for error in errors), errors)

    def test_duplicate_key_in_memory_jsonl_is_rejected(self):
        fixture = self._no_reference_fixture()
        path = fixture["run_memory"] / "failed_checks.jsonl"
        path.write_text('{"x":1,"x":2}\n', encoding="utf-8")
        fixture["receipt"]["memory_files_sha256"][path.name] = SERVICE._sha256_file(path)
        errors = self._replay(fixture)
        self.assertTrue(any("duplicate JSON object key" in error for error in errors), errors)

    def test_invalid_utf8_in_memory_jsonl_is_rejected(self):
        fixture = self._no_reference_fixture()
        path = fixture["run_memory"] / "failed_checks.jsonl"
        path.write_bytes(b'{"x":"\xff"}\n')
        fixture["receipt"]["memory_files_sha256"][path.name] = SERVICE._sha256_file(path)
        errors = self._replay(fixture)
        self.assertTrue(any("invalid UTF-8" in error for error in errors), errors)

    def test_blank_memory_jsonl_line_is_rejected(self):
        fixture = self._no_reference_fixture()
        path = fixture["run_memory"] / "failed_checks.jsonl"
        path.write_bytes(b"\r\n")
        fixture["receipt"]["memory_files_sha256"][path.name] = SERVICE._sha256_file(path)
        errors = self._replay(fixture)
        self.assertTrue(any("blank or whitespace-only" in error for error in errors), errors)

    def test_unterminated_memory_jsonl_line_is_rejected(self):
        fixture = self._no_reference_fixture()
        path = fixture["run_memory"] / "failed_checks.jsonl"
        path.write_bytes(b"{}")
        fixture["receipt"]["memory_files_sha256"][path.name] = SERVICE._sha256_file(path)
        errors = self._replay(fixture)
        self.assertTrue(any("lacks terminal LF" in error for error in errors), errors)

    def test_duplicate_key_in_state_json_is_rejected(self):
        fixture = self._no_reference_fixture()
        path = fixture["run_memory"] / "state.json"
        path.write_text('{"format":"one","format":"two"}\n', encoding="utf-8")
        fixture["receipt"]["memory_files_sha256"][path.name] = SERVICE._sha256_file(path)
        errors = self._replay(fixture)
        self.assertTrue(any("state.json replay failed" in error for error in errors), errors)

    def test_duplicate_key_in_meta_json_is_rejected(self):
        fixture = self._no_reference_fixture()
        path = fixture["run_memory"] / "meta.json"
        path.write_text('{"run_id":"one","run_id":"two"}\n', encoding="utf-8")
        fixture["receipt"]["memory_files_sha256"][path.name] = SERVICE._sha256_file(path)
        errors = self._replay(fixture)
        self.assertTrue(any("meta.json parse failed" in error for error in errors), errors)

    def test_memory_wrapper_extra_key_is_rejected(self):
        fixture = self._no_reference_fixture()
        path = fixture["run_memory"] / "statement_checks.jsonl"
        wrapper = copy.deepcopy(fixture["calls"][3]["structured_content"]["items"][0])
        wrapper["unexpected"] = True
        self._write_jsonl(path, [wrapper])
        fixture["receipt"]["memory_files_sha256"][path.name] = SERVICE._sha256_file(path)
        errors = self._replay(fixture)
        self.assertTrue(any("wrapper keys mismatch" in error for error in errors), errors)

    def test_receipt_schema_confusion_does_not_crash(self):
        fixture = self._no_reference_fixture()
        fixture["receipt"]["events"] = [True]
        errors = self._replay(fixture)
        self.assertTrue(errors)

    def test_receipt_release_pin_and_complete_bundle_mutations_are_rejected(self):
        fixture = self._external_fixture()
        runtime_before = self._complete_receipt(fixture)
        baseline = SERVICE._verify_receipt(
            fixture["receipt"],
            fixture["payload"],
            fixture["run_id"],
            "6" * 64,
            "Host-bound test statement",
            "Host-bound test proof",
            runtime_before,
            fixture["calls"],
        )
        self.assertEqual(baseline, [])

        mutations = []
        changed_pinset = copy.deepcopy(fixture["receipt"])
        changed_pinset["release_pinset_sha256"] = "0" * 64
        mutations.append(changed_pinset)
        changed_file_pin = copy.deepcopy(fixture["receipt"])
        changed_file_pin["release_pins_file_sha256"] = "0" * 64
        mutations.append(changed_file_pin)
        missing = copy.deepcopy(fixture["receipt"])
        missing["source_bundle_sha256"].pop("sources/gk_1509.09079.pdf")
        mutations.append(missing)
        extra = copy.deepcopy(fixture["receipt"])
        extra["source_bundle_sha256"]["sources/extra.txt"] = "a" * 64
        mutations.append(extra)
        swapped = copy.deepcopy(fixture["receipt"])
        first = "sources/gk_1406.7637.txt"
        second = "sources/gk_1509.09079.txt"
        swapped["source_bundle_sha256"][first], swapped["source_bundle_sha256"][second] = (
            swapped["source_bundle_sha256"][second],
            swapped["source_bundle_sha256"][first],
        )
        mutations.append(swapped)

        for receipt in mutations:
            errors = SERVICE._verify_receipt(
                receipt,
                fixture["payload"],
                fixture["run_id"],
                "6" * 64,
                "Host-bound test statement",
                "Host-bound test proof",
                runtime_before,
                fixture["calls"],
            )
            self.assertTrue(errors)

    def test_receipt_static_catalog_binding_mutations_are_rejected(self):
        fixture = self._external_fixture()
        self.assertEqual(self._full_gate_errors(fixture), [])
        runtime_before = fixture["runtime_before"]
        mutations = {
            "model_catalog_runtime_path": "model_catalog.other.json",
            "model_catalog_sha256": "0" * 64,
            "model_catalog_model": "gpt-5.6-terra",
            "model_catalog_reasoning_effort": "high",
        }
        for field, value in mutations.items():
            with self.subTest(field=field):
                receipt = copy.deepcopy(fixture["receipt"])
                receipt[field] = value
                errors = SERVICE._verify_receipt(
                    receipt,
                    fixture["payload"],
                    fixture["run_id"],
                    "6" * 64,
                    "Host-bound test statement",
                    "Host-bound test proof",
                    runtime_before,
                    fixture["calls"],
                )
                self.assertTrue(
                    any(
                        "receipt field" in error or "receipt runtime digest mismatch" in error
                        for error in errors
                    ),
                    errors,
                )

        missing = copy.deepcopy(fixture["receipt"])
        missing.pop("model_catalog_sha256")
        errors = SERVICE._verify_receipt(
            missing,
            fixture["payload"],
            fixture["run_id"],
            "6" * 64,
            "Host-bound test statement",
            "Host-bound test proof",
            runtime_before,
            fixture["calls"],
        )
        self.assertTrue(any("key allowlist" in error for error in errors), errors)

        extra = copy.deepcopy(fixture["receipt"])
        extra["model_catalog_extra"] = True
        errors = SERVICE._verify_receipt(
            extra,
            fixture["payload"],
            fixture["run_id"],
            "6" * 64,
            "Host-bound test statement",
            "Host-bound test proof",
            runtime_before,
            fixture["calls"],
        )
        self.assertTrue(any("key allowlist" in error for error in errors), errors)

    def test_no_reference_memory_append_argument_record_tamper_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = [dict(call) for call in fixture["calls"]]
        calls[2]["arguments"] = dict(calls[2]["arguments"])
        calls[2]["arguments"]["record"] = dict(
            calls[2]["arguments"]["record"]
        )
        calls[2]["arguments"]["record"]["detail"] = "forged"
        errors = self._replay(fixture, calls)
        self.assertTrue(any("argument record" in error for error in errors))

    def test_no_reference_memory_append_response_tamper_is_rejected(self):
        fixture = self._no_reference_fixture()
        calls = [dict(call) for call in fixture["calls"]]
        calls[2]["structured_content"] = dict(calls[2]["structured_content"])
        calls[2]["structured_content"]["index"] = True
        errors = self._replay(fixture, calls)
        self.assertTrue(any("response" in error for error in errors))

    def test_canonical_append_simplified_argument_tamper_is_rejected(self):
        fixture = self._external_fixture()
        calls = [dict(call) for call in fixture["calls"]]
        calls[5]["arguments"] = dict(calls[5]["arguments"])
        calls[5]["arguments"]["record"] = dict(
            calls[5]["arguments"]["record"]
        )
        calls[5]["arguments"]["record"]["detail"] = "forged"
        errors = self._replay(fixture, calls)
        self.assertTrue(any("canonical record" in error for error in errors))

    def test_canonical_append_response_digest_tamper_is_rejected(self):
        fixture = self._external_fixture()
        calls = [dict(call) for call in fixture["calls"]]
        calls[5]["structured_content"] = dict(calls[5]["structured_content"])
        calls[5]["structured_content"]["canonical_record_sha256"] = "f" * 64
        errors = self._replay(fixture, calls)
        self.assertTrue(any("response" in error for error in errors))

    def test_coordinated_theorem_event_record_and_manifest_tamper_is_rejected(self):
        fixture = self._external_fixture()
        event = fixture["events"][2]
        record = fixture["reference_records"][0]
        event["detail"]["count"] = 0
        event["detail"]["result_sha256"] = "f" * 64
        record["search_result_count"] = 0
        record["search_result_sha256"] = "f" * 64
        fixture["events"][5]["detail"]["canonical_record_sha256"] = (
            SERVICE._sha256_bytes(SERVICE._canonical_json_bytes(record))
        )
        self._refresh(fixture)
        errors = self._replay(fixture)
        self.assertTrue(any("theorem" in error and "transcript call" in error for error in errors))

    def test_coordinated_fixed_search_event_record_and_manifest_tamper_is_rejected(self):
        fixture = self._external_fixture()
        event = fixture["events"][3]
        evidence = fixture["reference_records"][0]["source_evidence"][0]
        event["detail"]["hits"] = 2
        event["detail"]["result_sha256"] = "e" * 64
        evidence["search_result_count"] = 2
        evidence["search_result_sha256"] = "e" * 64
        fixture["events"][5]["detail"]["canonical_record_sha256"] = (
            SERVICE._sha256_bytes(
                SERVICE._canonical_json_bytes(fixture["reference_records"][0])
            )
        )
        self._refresh(fixture)
        errors = self._replay(fixture)
        self.assertTrue(any("fixed_source" in error and "transcript call" in error for error in errors))

    def test_coordinated_read_event_record_and_manifest_tamper_is_rejected(self):
        fixture = self._external_fixture()
        fixture["events"][4]["detail"].update({"start_line": 1, "end_line": 1})
        line_range = fixture["reference_records"][0]["source_evidence"][0]["line_ranges"][0]
        line_range.update({"start_line": 1, "end_line": 1})
        fixture["events"][5]["detail"]["canonical_record_sha256"] = (
            SERVICE._sha256_bytes(
                SERVICE._canonical_json_bytes(fixture["reference_records"][0])
            )
        )
        self._refresh(fixture)
        errors = self._replay(fixture)
        self.assertTrue(any("read_fixed_source_lines" in error for error in errors))

    def test_fixed_search_transcript_body_tamper_is_rejected_by_source_recomputation(self):
        fixture = self._external_fixture()
        calls = [dict(call) for call in fixture["calls"]]
        forged = dict(calls[3]["structured_content"])
        forged["count"] = 0
        forged["hits"] = []
        base = dict(forged)
        base.pop("result_sha256")
        forged["result_sha256"] = SERVICE._sha256_bytes(
            SERVICE._canonical_json_bytes(base)
        )
        calls[3]["structured_content"] = forged
        errors = self._replay(fixture, calls)
        self.assertTrue(any("source-byte recomputation" in error for error in errors))

    def test_read_transcript_body_tamper_is_rejected_by_source_recomputation(self):
        fixture = self._external_fixture()
        calls = [dict(call) for call in fixture["calls"]]
        forged = dict(calls[4]["structured_content"])
        forged["text"] = "2: forged"
        calls[4]["structured_content"] = forged
        errors = self._replay(fixture, calls)
        self.assertTrue(any("source-byte recomputation" in error for error in errors))

    def test_theorem_transcript_count_tamper_is_rejected_from_result_body(self):
        fixture = self._external_fixture()
        calls = [dict(call) for call in fixture["calls"]]
        forged = dict(calls[2]["structured_content"])
        forged["count"] = 0
        base = dict(forged)
        base.pop("result_sha256")
        forged["result_sha256"] = SERVICE._sha256_bytes(
            SERVICE._canonical_json_bytes(base)
        )
        calls[2]["structured_content"] = forged
        errors = self._replay(fixture, calls)
        self.assertTrue(any("count differs" in error for error in errors))

    def test_boolean_theorem_result_count_is_rejected(self):
        fixture = self._external_fixture()
        calls = [dict(call) for call in fixture["calls"]]
        forged = dict(calls[2]["structured_content"])
        forged["count"] = True
        base = dict(forged)
        base.pop("result_sha256")
        forged["result_sha256"] = SERVICE._sha256_bytes(
            SERVICE._canonical_json_bytes(base)
        )
        calls[2]["structured_content"] = forged
        errors = self._replay(fixture, calls)
        self.assertTrue(any("strict nonnegative integer" in error for error in errors))

    def test_boolean_transcript_read_range_is_rejected(self):
        fixture = self._external_fixture()
        calls = [dict(call) for call in fixture["calls"]]
        calls[4]["arguments"] = dict(calls[4]["arguments"])
        calls[4]["arguments"]["start_line"] = True
        errors = self._replay(fixture, calls)
        self.assertTrue(any("strict valid integer range" in error for error in errors))

    def test_boolean_fixed_search_bound_is_rejected(self):
        fixture = self._external_fixture()
        calls = [dict(call) for call in fixture["calls"]]
        calls[3]["arguments"] = dict(calls[3]["arguments"])
        calls[3]["arguments"]["context_lines"] = False
        errors = self._replay(fixture, calls)
        self.assertTrue(any("strict bounded integer" in error for error in errors))

    def test_bool_event_sequence_is_rejected(self):
        fixture = self._no_reference_fixture()
        fixture["events"][0]["sequence"] = True
        self._refresh(fixture)
        errors = self._replay(fixture)
        self.assertTrue(any("sequence is not a strict integer" in error for error in errors))

    def test_bool_append_index_is_rejected(self):
        fixture = self._no_reference_fixture()
        fixture["events"][2]["detail"]["index"] = True
        self._refresh(fixture)
        errors = self._replay(fixture)
        self.assertTrue(any("append indices" in error for error in errors))

    def test_bool_record_range_is_rejected(self):
        fixture = self._external_fixture()
        line_range = fixture["reference_records"][0]["source_evidence"][0]["line_ranges"][0]
        line_range["start_line"] = True
        fixture["events"][5]["detail"]["canonical_record_sha256"] = (
            SERVICE._sha256_bytes(
                SERVICE._canonical_json_bytes(fixture["reference_records"][0])
            )
        )
        self._refresh(fixture)
        errors = self._replay(fixture)
        self.assertTrue(any("strict integers" in error for error in errors))


class ImmutableReleasePinTests(unittest.TestCase):
    """Hostile pre-start attacks against the code-level source pins."""

    @staticmethod
    def _mode_snapshot(root):
        result = {}
        paths = [root, *sorted(root.rglob("*"))]
        for path in paths:
            info = path.lstat()
            relative = "." if path == root else path.relative_to(root).as_posix()
            if stat.S_ISDIR(info.st_mode):
                kind = "directory"
            elif stat.S_ISREG(info.st_mode):
                kind = "regular"
            elif stat.S_ISLNK(info.st_mode):
                kind = "symlink"
            else:
                kind = "special"
            result[relative] = (kind, stat.S_IMODE(info.st_mode))
        return result

    @staticmethod
    def _make_throwaway_copy_owner_writable(candidate):
        """Thaw only a disposable copy, without following any symlink."""

        candidate = candidate.resolve(strict=True)
        source = ROOT.resolve(strict=True)
        if candidate == source or source in candidate.parents:
            raise RuntimeError("refusing to thaw the frozen source tree")
        paths = [candidate, *sorted(candidate.rglob("*"))]
        for path in paths:
            info = path.lstat()
            if stat.S_ISDIR(info.st_mode):
                os.chmod(path, 0o755, follow_symlinks=False)
        for path in paths:
            info = path.lstat()
            if stat.S_ISREG(info.st_mode):
                os.chmod(path, 0o644, follow_symlinks=False)

    def _copy_candidate(self, directory):
        source_modes_before = self._mode_snapshot(ROOT)
        candidate = Path(directory) / "candidate"
        shutil.copytree(ROOT, candidate)
        self._make_throwaway_copy_owner_writable(candidate)
        self.assertEqual(self._mode_snapshot(ROOT), source_modes_before)
        return candidate

    def test_frozen_source_tree_has_exact_read_only_modes(self):
        modes = self._mode_snapshot(ROOT)
        self.assertTrue(modes)
        for relative, (kind, mode) in modes.items():
            with self.subTest(relative=relative, kind=kind):
                self.assertNotIn(kind, {"symlink", "special"})
                self.assertEqual(mode, 0o555 if kind == "directory" else 0o444)

    def test_throwaway_copy_is_writable_and_source_is_unchanged(self):
        source_modes_before = self._mode_snapshot(ROOT)
        source_probe = ROOT / "runtime/sources/gk_1406.7637.txt"
        source_bytes_before = source_probe.read_bytes()
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            candidate_modes = self._mode_snapshot(candidate)
            for relative, (kind, mode) in candidate_modes.items():
                with self.subTest(relative=relative, kind=kind):
                    self.assertNotIn(kind, {"symlink", "special"})
                    self.assertEqual(mode, 0o755 if kind == "directory" else 0o644)
            copied_probe = candidate / "runtime/sources/gk_1406.7637.txt"
            copied_probe.write_bytes(b"throwaway mutation\n")
            scratch = candidate / "runtime/sources/throwaway"
            scratch.mkdir()
            artifact = scratch / "artifact.txt"
            artifact.write_text("throwaway\n", encoding="utf-8")
            artifact.rename(scratch / "renamed.txt")
            (scratch / "renamed.txt").unlink()
            scratch.rmdir()
            self.assertEqual(copied_probe.read_bytes(), b"throwaway mutation\n")
        self.assertEqual(source_probe.read_bytes(), source_bytes_before)
        self.assertEqual(self._mode_snapshot(ROOT), source_modes_before)

    def test_throwaway_thaw_does_not_follow_symlinks(self):
        source_modes_before = self._mode_snapshot(ROOT)
        source_probe = ROOT / "runtime/sources/gk_1406.7637.txt"
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            escape = candidate / "runtime/sources/escape-link"
            escape.symlink_to(source_probe)
            self._make_throwaway_copy_owner_writable(candidate)
            self.assertTrue(escape.is_symlink())
            self.assertEqual(stat.S_IMODE(source_probe.lstat().st_mode), 0o444)
        self.assertEqual(self._mode_snapshot(ROOT), source_modes_before)

    def _service_import(self, candidate):
        runtime = candidate / "runtime"
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        environment["PYTHONPATH"] = str(runtime)
        return subprocess.run(
            [sys.executable, "-B", "-c", "import hardened_service"],
            cwd=runtime,
            env=environment,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )

    def _rewrite_manifest_digest(self, candidate, relative, digest):
        manifest = candidate / "SHA256SUMS"
        rows = manifest.read_text(encoding="utf-8").splitlines()
        replacement = f"{digest}  {relative}"
        replaced = False
        for index, row in enumerate(rows):
            if row.endswith("  " + relative):
                rows[index] = replacement
                replaced = True
        if not replaced:
            rows.append(replacement)
        manifest.write_text("\n".join(rows) + "\n", encoding="utf-8")

    @staticmethod
    def _mutate_one_byte(path):
        data = bytearray(path.read_bytes())
        if not data:
            data.extend(b"x")
        else:
            data[0] ^= 1
        path.write_bytes(bytes(data))

    def _coherently_repin_service_catalog(self, candidate, catalog):
        catalog_path = candidate / "runtime/model_catalog.gpt-5.6-sol.json"
        catalog_path.write_text(
            json.dumps(catalog, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )
        service_path = candidate / "runtime/hardened_service.py"
        source = service_path.read_text(encoding="utf-8")
        source = source.replace(
            f"EXPECTED_MODEL_CATALOG_BYTES = {SERVICE.EXPECTED_MODEL_CATALOG_BYTES}",
            f"EXPECTED_MODEL_CATALOG_BYTES = {catalog_path.stat().st_size}",
            1,
        )
        source = source.replace(
            SERVICE.EXPECTED_MODEL_CATALOG_SHA256,
            SERVICE._sha256_file(catalog_path),
            1,
        )
        service_path.write_text(source, encoding="utf-8")

    def test_static_catalog_mutation_and_missing_file_fail_closed_pre_start(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            catalog_path = candidate / "runtime/model_catalog.gpt-5.6-sol.json"
            self._mutate_one_byte(catalog_path)
            result = self._service_import(candidate)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("static model catalog bytes differ", result.stderr)
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            catalog_path = candidate / "runtime/model_catalog.gpt-5.6-sol.json"
            catalog_path.rename(candidate / "held-model-catalog.json")
            result = self._service_import(candidate)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("static model catalog is missing", result.stderr)

    def test_static_catalog_semantic_confusion_fails_closed_even_after_host_repin(self):
        pristine = SERVICE._strict_json_loads(SERVICE.MODEL_CATALOG_PATH.read_text(encoding="utf-8"))
        mutations = []

        extra_top_key = copy.deepcopy(pristine)
        extra_top_key["extra"] = []
        mutations.append(("top-level keyset", extra_top_key))

        extra_model = copy.deepcopy(pristine)
        extra_model["models"].append(copy.deepcopy(extra_model["models"][0]))
        mutations.append(("exactly one model", extra_model))

        wrong_model = copy.deepcopy(pristine)
        wrong_model["models"][0]["slug"] = "gpt-5.6-terra"
        mutations.append(("selected-model mismatch", wrong_model))

        missing_xhigh = copy.deepcopy(pristine)
        missing_xhigh["models"][0]["supported_reasoning_levels"] = [
            level
            for level in missing_xhigh["models"][0]["supported_reasoning_levels"]
            if level.get("effort") != "xhigh"
        ]
        mutations.append(("does not support the selected reasoning effort", missing_xhigh))

        for expected_error, catalog in mutations:
            with self.subTest(expected_error=expected_error), tempfile.TemporaryDirectory() as directory:
                candidate = self._copy_candidate(directory)
                self._coherently_repin_service_catalog(candidate, catalog)
                result = self._service_import(candidate)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(expected_error, result.stderr)

    def test_clean_code_level_source_pin_gate_accepts_exact_bundle(self):
        self.assertEqual(
            SERVICE._assert_release_source_bundle(), SERVICE.SOURCE_BUNDLE_PINS
        )
        self.assertEqual(len(SERVICE.SOURCE_BUNDLE_PINS), 31)

    def test_each_pre_start_source_mutation_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            for relative in SERVICE.SOURCE_BUNDLE_PINS:
                path = candidate / "runtime" / relative
                original = path.read_bytes()
                self._mutate_one_byte(path)
                result = self._service_import(candidate)
                self.assertNotEqual(result.returncode, 0, relative)
                self.assertIn("immutable release pins", result.stderr, relative)
                path.write_bytes(original)

    def test_mutated_source_and_coherently_changed_mutable_manifest_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            relative = "runtime/sources/bmps_2603.08664.txt"
            path = candidate / relative
            self._mutate_one_byte(path)
            self._rewrite_manifest_digest(
                candidate, relative, SERVICE._sha256_file(path)
            )
            result = self._service_import(candidate)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("immutable release pins", result.stderr)

    def test_missing_source_is_rejected_pre_start(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            path = candidate / "runtime/sources/gk_1406.7637.pdf"
            path.rename(candidate / "held-gk17.pdf")
            result = self._service_import(candidate)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("inventory mismatch", result.stderr)

    def test_extra_source_is_rejected_pre_start(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            (candidate / "runtime/sources/extra.txt").write_text(
                "untrusted", encoding="utf-8"
            )
            result = self._service_import(candidate)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("inventory mismatch", result.stderr)

    def test_symlinked_source_is_rejected_pre_start(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            path = candidate / "runtime/sources/gk_1509.09079.txt"
            path.unlink()
            path.symlink_to("gk_1406.7637.txt")
            result = self._service_import(candidate)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("symlink forbidden", result.stderr)

    def test_cross_wired_source_ids_are_rejected_pre_start(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            first = candidate / "runtime/sources/gk_1406.7637.txt"
            second = candidate / "runtime/sources/gk_1509.09079.txt"
            first_bytes = first.read_bytes()
            second_bytes = second.read_bytes()
            first.write_bytes(second_bytes)
            second.write_bytes(first_bytes)
            result = self._service_import(candidate)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("immutable release pins", result.stderr)

    def test_coherent_release_constant_source_and_manifest_tamper_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            relative = "sources/bmps_2603.08664.txt"
            source = candidate / "runtime" / relative
            self._mutate_one_byte(source)
            new_size = source.stat().st_size
            new_source_digest = SERVICE._sha256_file(source)

            pin_payload = {
                "format": "rethlas-fixed-source-release-pins-v1",
                "fixed_source_runtime_paths": dict(
                    SERVICE._release_pins.FIXED_SOURCE_RUNTIME_PATHS
                ),
                "source_bundle_pins": copy.deepcopy(SERVICE.SOURCE_BUNDLE_PINS),
            }
            pin_payload["source_bundle_pins"][relative] = {
                "bytes": new_size,
                "sha256": new_source_digest,
            }
            new_pinset_digest = SERVICE._sha256_bytes(
                SERVICE._canonical_json_bytes(pin_payload)
            )

            pins_path = candidate / "runtime/release_pins.py"
            pins_text = pins_path.read_text(encoding="utf-8")
            old_pin = SERVICE.SOURCE_BUNDLE_PINS[relative]
            pins_text = pins_text.replace(
                str(old_pin["sha256"]), new_source_digest, 1
            )
            pins_text = pins_text.replace(
                f'"bytes": {old_pin["bytes"]}', f'"bytes": {new_size}', 1
            )
            pins_text = pins_text.replace(
                SERVICE.EXPECTED_RELEASE_PINSET_SHA256, new_pinset_digest, 1
            )
            pins_path.write_text(pins_text, encoding="utf-8")
            self._rewrite_manifest_digest(
                candidate,
                "runtime/" + relative,
                new_source_digest,
            )
            self._rewrite_manifest_digest(
                candidate,
                "runtime/release_pins.py",
                SERVICE._sha256_file(pins_path),
            )
            result = self._service_import(candidate)
            self.assertNotEqual(result.returncode, 0)
            self.assertTrue(
                "host's immutable" in result.stderr
                or "release_pins.py differs" in result.stderr,
                result.stderr,
            )

    def test_host_embedded_pin_constant_tamper_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            service_path = candidate / "runtime/hardened_service.py"
            source = service_path.read_text(encoding="utf-8")
            source = source.replace(
                SERVICE.EXPECTED_RELEASE_PINSET_SHA256, "0" * 64, 1
            )
            service_path.write_text(source, encoding="utf-8")
            result = self._service_import(candidate)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("immutable pin", result.stderr)

    def test_mcp_independently_rejects_mutated_source_before_server_start(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            runtime = candidate / "runtime"
            statement = "source-pin test"
            proof = "proof"
            statement_digest = SERVICE._sha256_text(statement)
            proof_digest = SERVICE._sha256_text(proof)
            run_id = "source_pin_test"
            request_dir = candidate / "artifacts/results" / run_id
            request_dir.mkdir(parents=True)
            (request_dir / "request.json").write_text(
                json.dumps(
                    {
                        "statement": statement,
                        "proof": proof,
                        "statement_sha256": statement_digest,
                        "proof_sha256": proof_digest,
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            self._mutate_one_byte(runtime / "sources/gk_1509.09079.pdf")
            environment = dict(os.environ)
            environment["PYTHONDONTWRITEBYTECODE"] = "1"
            environment["PYTHONPATH"] = str(runtime)
            result = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(runtime / "hardened_mcp.py"),
                    "--run-id",
                    run_id,
                    "--statement-sha256",
                    statement_digest,
                    "--proof-sha256",
                    proof_digest,
                    "--nonce",
                    "a" * 64,
                ],
                cwd=runtime,
                env=environment,
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("immutable release pins", result.stderr)

    def test_mcp_independently_rejects_mutated_static_catalog_before_server_start(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = self._copy_candidate(directory)
            runtime = candidate / "runtime"
            statement = "static-catalog-pin test"
            proof = "proof"
            statement_digest = SERVICE._sha256_text(statement)
            proof_digest = SERVICE._sha256_text(proof)
            run_id = "static_catalog_pin_test"
            request_dir = candidate / "artifacts/results" / run_id
            request_dir.mkdir(parents=True)
            (request_dir / "request.json").write_text(
                json.dumps(
                    {
                        "statement": statement,
                        "proof": proof,
                        "statement_sha256": statement_digest,
                        "proof_sha256": proof_digest,
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            self._mutate_one_byte(runtime / "model_catalog.gpt-5.6-sol.json")
            environment = dict(os.environ)
            environment["PYTHONDONTWRITEBYTECODE"] = "1"
            environment["PYTHONPATH"] = str(runtime)
            result = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(runtime / "hardened_mcp.py"),
                    "--run-id",
                    run_id,
                    "--statement-sha256",
                    statement_digest,
                    "--proof-sha256",
                    proof_digest,
                    "--nonce",
                    "a" * 64,
                ],
                cwd=runtime,
                env=environment,
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("static model catalog bytes differ", result.stderr)


if __name__ == "__main__":
    unittest.main()
