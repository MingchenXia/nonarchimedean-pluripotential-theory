from __future__ import annotations

import copy
from datetime import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
from typing import Any


HERE = Path(__file__).resolve().parent
STAGE = HERE / "release_stage"
PACKET = HERE / "packet"
SNAPSHOTS = HERE / "snapshots"
PREDECESSOR = Path(
    "/private/tmp/p148_repaired_source_release_authored_stage_dossier_v1_20260901"
)
PREDECESSOR_STAGE = PREDECESSOR / "release_stage"
PREDECESSOR_AUDIT = Path(
    "/private/tmp/p148_repaired_source_release_independent_hostile_audit_v1_20260901"
)
FAILED_DOSSIER = Path(
    "/private/tmp/p148_retry1_final_path_smoke_authored_fail_dossier_v1_20260901"
)
V1_AUTHORED = Path(
    "/private/tmp/p148_smoke_infrastructure_repaired_authored_stage_dossier_v1_20260901"
)
V1_STAGE = V1_AUTHORED / "release_stage"
V1_FAIL_AUDIT = Path(
    "/private/tmp/p148_smoke_infrastructure_repaired_independent_hostile_audit_v1_20260901"
)
TEST_PYTHON = Path(
    "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/"
    "agents/verification/tmp/verification-venv/bin/python"
)

PREDECESSOR_TOP_SHA = "a25f1ce2d370feadfc849b2040bed12a0dc3b91f5053921ce8cbf80883909187"
PREDECESSOR_STAGE_SHA = "e06616686dff546abe2e4e5269781273a8d9062f563fad10a618d2061044dea6"
PREDECESSOR_AUDIT_SHA = "d4086f34593cdd1b02436efe9f8865b1f1b6049a87b5e11a9d9f8fc5d84b4fc3"
FAILED_DOSSIER_SHA = "e7b69860f7327da9e6a375720c2f447d81eb8a7880d1bf5c415848bcbbfc708e"
V1_AUTHORED_SHA = "bea75f18d2b5f765d07439c19189fa203b7a7f772a7dff9cd09c1d1d65721a30"
V1_STAGE_SHA = "4c2a6c9d61966aeac3f0c5c27284a0746d1a8bcc4520340016247947f9c9accc"
V1_FAIL_AUDIT_SHA = "d4843c62df5c706b76bf689484b254eb84b955872117c567b2846ac4c1baac77"
STAGE_SHA = "837d5bb55d134bf4040c1083ffb1cf068b6b6c83bbc16bd7e86f2a1d8f247912"
PACKET_SHA = "87ca97e402d845d4628f72d67c28e19b05674a23f3aa478be04221cecd5df0ff"
STATEMENT_SHA = "9cd8fe1533c99d9d2de9e351610da4b7843d156a523d97344032cf75e3953715"
PROOF_SHA = "adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9"

CHANGED = {
    "STAGING_REPORT.md": "6eb900d5ff6612cc255b7204e1f364e19cbe05d44e80ca947aff030572487e29",
    "check_release.py": "2fcacad42bd34caca8763e80d7c326545d189d49cc70e1f4fe0b73a6a41cf356",
    "run_static_model_long_smoke.py": "6898ef6e8789620dafb5ade3b694f82157a3ef11325ae50670c84aaa2ffc8c09",
    "runtime/contract.md": "fd02279e2379d505a033a38500041b1f9541f9a6daa3c55350cc135448e07abf",
    "tests/test_runtime.py": "9a227222fb8528ac5d753b078c0c5f8a19937ba0543de1e48f07576c92844962",
}
V1_TO_V2_CHANGED = {
    "STAGING_REPORT.md": "6eb900d5ff6612cc255b7204e1f364e19cbe05d44e80ca947aff030572487e29",
    "tests/test_runtime.py": "9a227222fb8528ac5d753b078c0c5f8a19937ba0543de1e48f07576c92844962",
}
FAILED_RAW_SHA = "68fad3795e6dba22226123c8c4540970a80d94b65a9f8810ca67f15ba8b7b360"
FAILED_RECEIPT_SHA = "9b54171da78c6ed580b2ba1a1eb1d022f3559c10422685af8d06e8560ae4330c"
FAILED_SAMPLES_SHA = "e3458a20497ff7b8bf6bf72bdb8575a0bf1f56020e86ce9315c9862ce8947a23"


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
    require(raw.endswith(b"\n"), f"manifest lacks LF: {path}")
    rows: dict[str, str] = {}
    ordered: list[str] = []
    for line in raw.decode("utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        require(match is not None, f"malformed manifest row: {path}: {line!r}")
        digest, relative = match.groups()
        require(relative not in rows, f"duplicate manifest path: {relative}")
        require(not relative.startswith(("/", "../")), f"unsafe manifest path: {relative}")
        rows[relative] = digest
        ordered.append(relative)
    require(ordered == sorted(ordered), f"unsorted manifest: {path}")
    return rows


def actual_files(root: Path) -> list[str]:
    result: list[str] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        info = path.lstat()
        require(not stat.S_ISLNK(info.st_mode), f"symlink: {root}: {relative}")
        require("__pycache__" not in path.parts, f"bytecode cache: {root}: {relative}")
        if stat.S_ISDIR(info.st_mode):
            continue
        require(stat.S_ISREG(info.st_mode), f"special file: {root}: {relative}")
        require(path.suffix != ".pyc", f"bytecode: {root}: {relative}")
        if relative != "SHA256SUMS":
            result.append(relative)
    return sorted(result)


def validate_exact_read_only_modes(root: Path) -> None:
    paths = [root, *sorted(root.rglob("*"))]
    for path in paths:
        relative = "." if path == root else path.relative_to(root).as_posix()
        info = path.lstat()
        require(not stat.S_ISLNK(info.st_mode), f"read-only tree symlink: {relative}")
        require(
            stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode),
            f"read-only tree special path: {relative}",
        )
        expected = 0o555 if stat.S_ISDIR(info.st_mode) else 0o444
        require(
            stat.S_IMODE(info.st_mode) == expected,
            f"read-only tree mode: {relative}: "
            f"{stat.S_IMODE(info.st_mode):04o} != {expected:04o}",
        )


def validate_manifest(root: Path, expected_sha: str) -> dict[str, str]:
    manifest = root / "SHA256SUMS"
    require(sha(manifest) == expected_sha, f"manifest digest: {root}")
    rows = manifest_rows(manifest)
    require(sorted(rows) == actual_files(root), f"manifest inventory: {root}")
    for relative, digest in rows.items():
        require(sha(root / relative) == digest, f"manifest row: {root}: {relative}")
    return rows


def fingerprint(root: Path) -> dict[str, str]:
    return {relative: sha(root / relative) for relative in actual_files(root)}


def import_module(name: str, path: Path):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def check_snapshots() -> None:
    bindings = {
        "predecessor_authored_SHA256SUMS": (PREDECESSOR / "SHA256SUMS", PREDECESSOR_TOP_SHA),
        "predecessor_release_stage_SHA256SUMS": (
            PREDECESSOR_STAGE / "SHA256SUMS", PREDECESSOR_STAGE_SHA
        ),
        "predecessor_independent_audit_SHA256SUMS": (
            PREDECESSOR_AUDIT / "SHA256SUMS", PREDECESSOR_AUDIT_SHA
        ),
        "failed_final_smoke_dossier_SHA256SUMS": (
            FAILED_DOSSIER / "SHA256SUMS", FAILED_DOSSIER_SHA
        ),
        "repaired_release_stage_SHA256SUMS": (V1_STAGE / "SHA256SUMS", V1_STAGE_SHA),
        "v1_authored_SHA256SUMS": (V1_AUTHORED / "SHA256SUMS", V1_AUTHORED_SHA),
        "v1_release_stage_SHA256SUMS": (V1_STAGE / "SHA256SUMS", V1_STAGE_SHA),
        "v1_independent_fail_audit_SHA256SUMS": (
            V1_FAIL_AUDIT / "SHA256SUMS", V1_FAIL_AUDIT_SHA
        ),
    }
    for snapshot_name, (source, expected) in bindings.items():
        snapshot = SNAPSHOTS / snapshot_name
        require(sha(snapshot) == expected, f"snapshot digest: {snapshot_name}")
        require(snapshot.read_bytes() == source.read_bytes(), f"snapshot drift: {snapshot_name}")
    require(sha(SNAPSHOTS / "failed_merged_codex.log") == FAILED_RAW_SHA, "failed raw snapshot")
    require(sha(SNAPSHOTS / "failed_receipt_v1.json") == FAILED_RECEIPT_SHA,
            "failed receipt snapshot")
    require(sha(SNAPSHOTS / "failed_process_samples_v1.json") == FAILED_SAMPLES_SHA,
            "failed sample snapshot")


def check_preservation() -> None:
    old_rows = validate_manifest(PREDECESSOR_STAGE, PREDECESSOR_STAGE_SHA)
    new_rows = validate_manifest(STAGE, STAGE_SHA)
    require(len(old_rows) == len(new_rows) == 44, "release row count")
    require(set(old_rows) == set(new_rows), "release path inventory changed")
    changed = {relative for relative in old_rows if old_rows[relative] != new_rows[relative]}
    require(changed == set(CHANGED), f"unexpected changed-file set: {sorted(changed)}")
    for relative, digest in CHANGED.items():
        require(new_rows[relative] == digest, f"changed digest: {relative}")
    unchanged = set(new_rows) - changed
    require(len(unchanged) == 39, "unchanged release-row count")
    for relative in unchanged:
        require(
            (STAGE / relative).read_bytes() == (PREDECESSOR_STAGE / relative).read_bytes(),
            f"protected byte drift: {relative}",
        )
    sources = [relative for relative in new_rows if relative.startswith("runtime/sources/")]
    require(len(sources) == 31 and all(relative in unchanged for relative in sources),
            "fixed-source preservation")
    for relative in (
        "runtime/hardened_service.py",
        "runtime/hardened_mcp.py",
        "runtime/release_pins.py",
        "runtime/canonical_reference.py",
        "runtime/memory_record.schema.json",
        "runtime/verification_output.schema.json",
        "runtime/model_catalog.gpt-5.6-sol.json",
        "static_model_smoke_mcp.py",
    ):
        require(relative in unchanged, f"protected control byte changed: {relative}")

    v1_rows = validate_manifest(V1_STAGE, V1_STAGE_SHA)
    require(set(v1_rows) == set(new_rows), "v1-to-v2 path inventory changed")
    v1_changed = {
        relative for relative in v1_rows if v1_rows[relative] != new_rows[relative]
    }
    require(v1_changed == set(V1_TO_V2_CHANGED), "v1-to-v2 changed-file set")
    for relative, digest in V1_TO_V2_CHANGED.items():
        require(new_rows[relative] == digest, f"v1-to-v2 digest: {relative}")
    for relative in set(new_rows) - v1_changed:
        require(
            (STAGE / relative).read_bytes() == (V1_STAGE / relative).read_bytes(),
            f"v1 protected byte drift: {relative}",
        )


def check_packet() -> None:
    validate_manifest(PACKET, PACKET_SHA)
    require(sha(PACKET / "PROPOSED_STATEMENT.tex") == STATEMENT_SHA, "statement digest")
    require(sha(PACKET / "PROOF.tex") == PROOF_SHA, "proof digest")
    completed = subprocess.run(
        [sys.executable, "-B", "check_packet.py"],
        cwd=PACKET,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    require(completed.returncode == 0, f"packet checker failed:\n{completed.stdout}\n{completed.stderr}")


def check_static_stage() -> tuple[Any, Any]:
    require(not (STAGE / "STATIC_MODEL_LONG_SMOKE").exists(), "stage contains smoke artifacts")
    require(not (STAGE / "artifacts").exists(), "stage contains production artifacts")
    checker = import_module("p148_repaired_release_checker", STAGE / "check_release.py")
    runner = import_module("p148_repaired_smoke_runner", STAGE / "run_static_model_long_smoke.py")
    checker.check_manifest()
    checker.check_catalog()
    checker.check_release_pins()
    checker.check_code_contract()
    source = (STAGE / "run_static_model_long_smoke.py").read_text(encoding="utf-8")
    require("stdout=stdout_handle" in source and "stderr=stderr_handle" in source,
            "split Popen streams")
    require("stderr=subprocess.STDOUT" not in source, "merged stderr remains")
    require("os.openpty()" in source and "stdin=stdin_slave_fd" in source,
            "PTY stdin strategy")
    return checker, runner


def check_failed_evidence_replay(checker: Any, runner: Any) -> None:
    old_receipt = strict_json(SNAPSHOTS / "failed_receipt_v1.json")
    raw_lines = (SNAPSHOTS / "failed_merged_codex.log").read_text(encoding="utf-8").splitlines()
    json_lines: list[str] = []
    stderr_lines: list[str] = []
    banner_count = 0
    for line in raw_lines:
        if line.startswith("{"):
            json_lines.append(line)
        elif checker.STATE_WARNING.fullmatch(line) or checker.SHELL_WARNING.fullmatch(line):
            stderr_lines.append(line)
        elif line == "Reading additional input from stdin...":
            banner_count += 1
        else:
            raise RuntimeError(f"unclassified failed raw line: {line!r}")
    require(len(json_lines) == 7 and len(stderr_lines) == 105 and banner_count == 1,
            "failed raw classification")
    stdout = "\n".join(json_lines) + "\n"
    stderr = "\n".join(stderr_lines) + "\n"

    receipt = copy.deepcopy(old_receipt)
    receipt["stdout_forbidden_diagnostic_count"] = 0
    receipt["stderr_forbidden_diagnostic_count"] = 0
    receipt["stderr_warning_counts"] = {
        "state_db": 104,
        "shell_snapshot_cleanup": 1,
    }
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
    for validator in (
        lambda: checker.validate_stderr_smoke(
            "Reading additional input from stdin...\n",
            {
                **receipt,
                "stderr_warning_counts": {"state_db": 0, "shell_snapshot_cleanup": 0},
            },
        ),
        lambda: runner._classify_stderr(b"Reading additional input from stdin...\n"),
    ):
        try:
            validator()
        except RuntimeError as error:
            require("not an allowlisted warning" in str(error), "stdin banner failure mode")
        else:
            raise RuntimeError("stdin banner unexpectedly accepted")

    samples = strict_json(SNAPSHOTS / "failed_process_samples_v1.json")
    failed_root = (
        "/Users/mingchen/Documents/ChatGPT/Yethlas/runtime/"
        "rethlas_hardened_v3_3_3_r5_p148_retry1_final_20260901"
    )
    stage_root = str(STAGE.resolve())
    for index, sample in enumerate(samples):
        sample["root_observation"] = (
            "live" if index < len(samples) - 1 else "exited_during_scan"
        )
        for row in sample["descendants"]:
            row["command"] = row["command"].replace(failed_root, stage_root)
    checker.validate_process_samples(samples, receipt, mcp_started, mcp_completed)


def run_tests_twice() -> list[float]:
    times: list[float] = []
    for number in range(2):
        completed = subprocess.run(
            [str(TEST_PYTHON), "-B", "-m", "unittest", "discover", "-s", "tests"],
            cwd=STAGE,
            capture_output=True,
            text=True,
            timeout=240,
            check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        output = completed.stdout + "\n" + completed.stderr
        match = re.search(r"Ran 161 tests in ([0-9.]+)s", output)
        require(
            completed.returncode == 0
            and match is not None
            and re.search(r"\nOK\s*$", output) is not None,
            f"161-test pass {number + 1} failed:\n{output}",
        )
        times.append(float(match.group(1)))
    return times


def check_ledgers() -> None:
    baseline = strict_json(HERE / "BASELINE_PRESERVATION.json")
    require(baseline["v2_release_stage_manifest_sha256"] == STAGE_SHA,
            "baseline stage digest")
    require(
        set(baseline["pre_repair_to_v2"]["substantive_changed_files"]) == set(CHANGED),
        "baseline pre-repair changed-file set",
    )
    require(
        set(baseline["v1_to_v2"]["substantive_changed_files"])
        == set(V1_TO_V2_CHANGED),
        "baseline v1-to-v2 changed-file set",
    )
    require(baseline["v1_to_v2"]["byte_identical_manifest_rows"] == 42,
            "baseline v1-to-v2 preservation count")
    result = strict_json(HERE / "RESULT.json")
    require(result["verdict"] == "READY_FOR_INDEPENDENT_STATIC_AUDIT", "result verdict")
    require(result["independently_audited"] is False, "independent audit flag")
    require(result["test_inventory"] == 161 and result["regression_tests_added"] == 26,
            "result test inventory")
    require(result["read_only_boundary"]["directories"] == "0555", "directory mode ledger")
    require(result["read_only_boundary"]["regular_files"] == "0444", "file mode ledger")
    require(result["read_only_boundary"]["source_chmod_calls"] == 0,
            "source chmod ledger")
    require(result["blockers"] == [], "authored blockers")
    require(all(value is False for value in result["prohibited_actions_performed"].values()),
            "prohibited action recorded")
    tests = strict_json(HERE / "TEST_RUNS.json")
    require(tests["final_test_inventory"] == 161, "test-ledger inventory")
    require(tests["regression_tests_added"] == 26, "test-ledger regression count")
    require(tests["read_only_regression_tests_added"] == 3,
            "read-only regression count")
    require(
        tests["authored_prefreeze_qa"]["tests"] == 161
        and tests["authored_prefreeze_qa"]["result"] == "OK",
        "prefreeze QA ledger",
    )
    policy = tests["post_final_metadata_freeze_policy"]
    require(policy["top_checker_invocations"] == 2, "top-checker invocation policy")
    require(policy["full_suites_per_invocation"] == 2, "top-checker suite policy")
    require(policy["source_tree_mutations"] == 0, "post-freeze mutation policy")
    require(tests["smoke_runs"] == tests["production_submissions"] == 0,
            "forbidden execution ledger")


def main() -> None:
    validate_exact_read_only_modes(HERE)
    own_before = fingerprint(HERE)
    stage_before = fingerprint(STAGE)
    validate_manifest(HERE, sha(HERE / "SHA256SUMS"))
    check_snapshots()
    check_preservation()
    check_packet()
    checker, runner = check_static_stage()
    check_failed_evidence_replay(checker, runner)
    times = run_tests_twice()
    check_ledgers()
    require(fingerprint(STAGE) == stage_before, "stage mutated during checking")
    require(fingerprint(HERE) == own_before, "dossier mutated during checking")
    print("PASS_FROZEN_P148_SMOKE_INFRASTRUCTURE_AUTHORED_STAGE")
    print(json.dumps({"tests": 161, "test_seconds": times}, sort_keys=True))


if __name__ == "__main__":
    main()
