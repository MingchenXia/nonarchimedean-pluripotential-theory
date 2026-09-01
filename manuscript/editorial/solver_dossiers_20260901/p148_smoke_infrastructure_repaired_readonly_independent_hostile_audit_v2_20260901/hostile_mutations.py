from __future__ import annotations

from datetime import timedelta
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
from typing import Any, Callable


CANDIDATE = Path(
    "/private/tmp/"
    "p148_smoke_infrastructure_repaired_readonly_authored_stage_dossier_v2_20260901"
)
STAGE = CANDIDATE / "release_stage"
PYTHON = Path(
    "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/"
    "agents/verification/tmp/verification-venv/bin/python"
)


def require(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fingerprint(root: Path) -> dict[str, tuple[str, int, str | None]]:
    result: dict[str, tuple[str, int, str | None]] = {}
    for path in [root, *sorted(root.rglob("*"))]:
        relative = "." if path == root else path.relative_to(root).as_posix()
        info = path.lstat()
        if stat.S_ISDIR(info.st_mode):
            kind, digest = "directory", None
        elif stat.S_ISREG(info.st_mode):
            kind, digest = "regular", sha(path)
        elif stat.S_ISLNK(info.st_mode):
            kind, digest = "symlink", os.readlink(path)
        else:
            kind, digest = "special", None
        result[relative] = (kind, stat.S_IMODE(info.st_mode), digest)
    return result


def thaw(root: Path) -> None:
    paths = [root, *sorted(root.rglob("*"))]
    for path in paths:
        info = path.lstat()
        if stat.S_ISDIR(info.st_mode):
            os.chmod(path, 0o755, follow_symlinks=False)
    for path in paths:
        info = path.lstat()
        if stat.S_ISREG(info.st_mode):
            os.chmod(path, 0o644, follow_symlinks=False)


def freeze(root: Path) -> None:
    paths = [root, *sorted(root.rglob("*"))]
    for path in paths:
        info = path.lstat()
        if stat.S_ISREG(info.st_mode):
            os.chmod(path, 0o444, follow_symlinks=False)
    for path in reversed(paths):
        info = path.lstat()
        if stat.S_ISDIR(info.st_mode):
            os.chmod(path, 0o555, follow_symlinks=False)


def clean_temp(root: Path) -> None:
    if root.exists():
        thaw(root)
        shutil.rmtree(root)


def fresh_temp(prefix: str) -> Path:
    return Path(tempfile.mkdtemp(prefix=prefix, dir="/private/tmp"))


def expect_runtime_error(function: Callable[[], Any], fragment: str) -> str:
    try:
        function()
    except RuntimeError as error:
        require(fragment in str(error), f"wrong failure: {error!s}")
        return str(error)
    raise RuntimeError(f"hostile mutation accepted; expected {fragment!r}")


def load_module(name: str, path: Path):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def check_mode_drift() -> dict[str, Any]:
    temp = fresh_temp("p148-audit-mode-")
    source_before = fingerprint(CANDIDATE)
    try:
        copied = temp / "candidate"
        shutil.copytree(CANDIDATE, copied)
        os.chmod(copied / "AUTHOR_REPORT.md", 0o644)
        completed = subprocess.run(
            [str(PYTHON), "-B", "check_dossier.py"],
            cwd=copied,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        combined = completed.stdout + completed.stderr
        require(completed.returncode != 0, "mode drift passed the top checker")
        require("read-only tree mode" in combined, f"wrong mode failure: {combined}")
        return {"return_code": completed.returncode, "detected": True}
    finally:
        require(fingerprint(CANDIDATE) == source_before, "mode test mutated source")
        clean_temp(temp)


def check_manifest_mutation() -> dict[str, Any]:
    temp = fresh_temp("p148-audit-manifest-")
    source_before = fingerprint(STAGE)
    try:
        copied = temp / "release_stage"
        shutil.copytree(STAGE, copied)
        thaw(copied)
        target = copied / "runtime/contract.md"
        target.write_bytes(target.read_bytes() + b"\nHOSTILE\n")
        code = (
            "import importlib.util; from pathlib import Path; "
            "p=Path('check_release.py').resolve(); "
            "s=importlib.util.spec_from_file_location('audit_manifest_checker',p); "
            "m=importlib.util.module_from_spec(s); s.loader.exec_module(m); "
            "m.check_manifest()"
        )
        completed = subprocess.run(
            [str(PYTHON), "-B", "-c", code],
            cwd=copied,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        combined = completed.stdout + completed.stderr
        require(completed.returncode != 0, "byte drift passed release manifest")
        require("digest mismatch: runtime/contract.md" in combined, combined)
        return {"return_code": completed.returncode, "detected": True}
    finally:
        require(fingerprint(STAGE) == source_before, "manifest test mutated source")
        clean_temp(temp)


def check_code_contract_mutation(old: str, new: str, expected: str, label: str) -> dict[str, Any]:
    temp = fresh_temp(f"p148-audit-{label}-")
    source_before = fingerprint(STAGE)
    try:
        copied = temp / "release_stage"
        shutil.copytree(STAGE, copied)
        thaw(copied)
        runner = copied / "run_static_model_long_smoke.py"
        text = runner.read_text(encoding="utf-8")
        require(text.count(old) >= 1, f"mutation anchor missing: {label}")
        runner.write_text(text.replace(old, new, 1), encoding="utf-8")
        code = (
            "import importlib.util; from pathlib import Path; "
            "p=Path('check_release.py').resolve(); "
            f"s=importlib.util.spec_from_file_location('audit_{label}_checker',p); "
            "m=importlib.util.module_from_spec(s); s.loader.exec_module(m); "
            "m.check_code_contract()"
        )
        completed = subprocess.run(
            [str(PYTHON), "-B", "-c", code],
            cwd=copied,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        combined = completed.stdout + completed.stderr
        require(completed.returncode != 0, f"{label} mutation passed contract")
        require(expected in combined, f"wrong {label} failure: {combined}")
        return {"return_code": completed.returncode, "detected": True}
    finally:
        require(fingerprint(STAGE) == source_before, f"{label} test mutated source")
        clean_temp(temp)


def check_helper_removal() -> dict[str, Any]:
    temp = fresh_temp("p148-audit-helper-removal-")
    source_before = fingerprint(STAGE)
    try:
        copied = temp / "release_stage"
        shutil.copytree(STAGE, copied)
        thaw(copied)
        test_path = copied / "tests/test_runtime.py"
        text = test_path.read_text(encoding="utf-8")
        anchor = (
            "        shutil.copytree(ROOT, candidate)\n"
            "        self._make_throwaway_copy_owner_writable(candidate)\n"
        )
        replacement = (
            "        shutil.copytree(ROOT, candidate)\n"
            "        # hostile removal of the disposable-copy thaw\n"
        )
        require(text.count(anchor) == 1, "helper-removal anchor is not unique")
        test_path.write_text(text.replace(anchor, replacement, 1), encoding="utf-8")
        freeze(copied)
        completed = subprocess.run(
            [
                str(PYTHON), "-B", "-m", "unittest", "discover", "-s", "tests",
                "-p", "test_runtime.py", "-k", "throwaway_copy_is_writable",
            ],
            cwd=copied,
            capture_output=True,
            text=True,
            timeout=90,
            check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        combined = completed.stdout + completed.stderr
        require(completed.returncode != 0, "removed thaw helper did not fail")
        require(
            any(marker in combined for marker in ("PermissionError", "Errno 13", "Operation not permitted")),
            f"helper-removal failure was not a write barrier: {combined}",
        )
        return {"return_code": completed.returncode, "detected": True}
    finally:
        require(fingerprint(STAGE) == source_before, "helper-removal test mutated source")
        clean_temp(temp)


def check_helper_guard_and_symlink() -> dict[str, Any]:
    temp = fresh_temp("p148-audit-helper-guard-")
    source_before = fingerprint(STAGE)
    imported_runtime: str | None = None
    try:
        source = temp / "source"
        shutil.copytree(STAGE, source)
        imported_runtime = str(source / "runtime")
        module = load_module(
            "p148_audit_helper_test_module",
            source / "tests/test_runtime.py",
        )
        helper = module.ImmutableReleasePinTests._make_throwaway_copy_owner_writable
        frozen_before = fingerprint(source)
        expect_runtime_error(lambda: helper(source), "refusing to thaw")
        expect_runtime_error(lambda: helper(source / "runtime"), "refusing to thaw")
        require(fingerprint(source) == frozen_before, "guard attempt changed source")

        candidate = temp / "throwaway"
        shutil.copytree(source, candidate)
        external = temp / "external-frozen.txt"
        external.write_text("external\n", encoding="utf-8")
        os.chmod(external, 0o444)
        external_sha = sha(external)
        links = candidate / "runtime/sources"
        os.chmod(links, 0o755)
        escape = links / "escape-link"
        escape.symlink_to(external)
        os.chmod(links, 0o555)
        helper(candidate)
        require(escape.is_symlink(), "helper replaced disposable symlink")
        require(sha(external) == external_sha, "helper followed symlink into target bytes")
        require(stat.S_IMODE(external.lstat().st_mode) == 0o444, "helper chmod followed symlink")
        require(fingerprint(source) == frozen_before, "sibling thaw changed source")
        return {
            "source_and_descendant_guarded": True,
            "symlink_target_mode": "0444",
            "symlink_target_unchanged": True,
        }
    finally:
        for name in (
            "release_pins",
            "canonical_reference",
            "p148_smoke_runner",
            "p148_release_checker",
            "p148_audit_helper_test_module",
        ):
            sys.modules.pop(name, None)
        if imported_runtime is not None:
            sys.path[:] = [item for item in sys.path if item != imported_runtime]
        require(fingerprint(STAGE) == source_before, "helper guard test mutated candidate")
        clean_temp(temp)


def check_stream_process_contracts() -> dict[str, Any]:
    module = load_module(
        "p148_audit_runtime_test_module",
        STAGE / "tests/test_runtime.py",
    )
    checker = module.RELEASE_CHECKER
    runner = module.SMOKE_RUNNER

    stdout, receipt = module.strict_smoke_stdout_fixture()
    checker.validate_stdout_smoke(stdout, receipt)
    runner._parse_stdout_records(stdout.encode("utf-8"))
    lines = stdout.splitlines()
    lines.insert(2, module.state_db_warning())
    polluted = "\n".join(lines) + "\n"
    expect_runtime_error(
        lambda: checker.validate_stdout_smoke(polluted, receipt),
        "not strict JSON",
    )
    expect_runtime_error(
        lambda: runner._parse_stdout_records(polluted.encode("utf-8")),
        "not strict JSON",
    )

    valid_stderr = module.state_db_warning() + "\n" + module.shell_snapshot_warning() + "\n"
    checker.validate_stderr_smoke(valid_stderr, module.stderr_receipt(1, 1))
    runner._classify_stderr(valid_stderr.encode("utf-8"))
    expect_runtime_error(
        lambda: checker.validate_stderr_smoke(
            module.state_db_warning() + " suffix\n", module.stderr_receipt(1, 0)
        ),
        "not an allowlisted warning",
    )
    expect_runtime_error(
        lambda: runner._classify_stderr(b"credential unavailable\n"),
        "not an allowlisted warning",
    )

    live = module.FakePolledProcess([None, None])
    state, rows = runner._observe_process(live, lambda pid: [{"pid": pid}])
    require((state, rows) == ("live", [{"pid": 42}]), "pre/post live poll contract")
    zombie_rows = [{"pid": 42, "ppid": 1, "elapsed": "05:30", "command": "(codex)"}]
    raced = module.FakePolledProcess([None, 0])
    state, rows = runner._observe_process(raced, lambda _pid: zombie_rows)
    require((state, rows) == ("exited_during_scan", zombie_rows), "post-poll race contract")
    before = module.FakePolledProcess([0])
    state, rows = runner._observe_process(
        before, lambda _pid: (_ for _ in ()).throw(RuntimeError("scan called"))
    )
    require((state, rows) == ("exited_before_scan", []), "pre-poll exit contract")

    mcp_started = module.SMOKE_BASE + timedelta(seconds=18)
    mcp_completed = module.SMOKE_BASE + timedelta(seconds=328)
    timestamps = [
        module.SMOKE_BASE + timedelta(seconds=316),
        module.SMOKE_BASE + timedelta(seconds=331),
    ]
    checker.validate_cache_horizon_bracketing(
        timestamps,
        [{"codex", "mcp-python", "code-mode-host"}, set()],
        ["live", "exited_during_scan"],
        mcp_started,
        mcp_completed,
    )
    expect_runtime_error(
        lambda: checker.validate_cache_horizon_bracketing(
            [timestamps[0], module.SMOKE_BASE + timedelta(seconds=325)],
            [{"codex", "mcp-python", "code-mode-host"}, set()],
            ["live", "exited_during_scan"],
            mcp_started,
            mcp_completed,
        ),
        "does not follow horizon-crossing",
    )
    process_receipt, samples = module.terminal_race_process_fixture()
    checker.validate_process_samples(samples, process_receipt, mcp_started, mcp_completed)
    samples[-1]["descendants"][0]["pid"] = 99
    expect_runtime_error(
        lambda: checker.validate_process_samples(
            samples, process_receipt, mcp_started, mcp_completed
        ),
        "terminal zombie PID mismatch",
    )
    runner_source = (STAGE / "run_static_model_long_smoke.py").read_text(encoding="utf-8")
    require("os.openpty()" in runner_source, "PTY creation missing")
    require("stdin=stdin_slave_fd" in runner_source, "PTY slave stdin missing")
    require("stdout=stdout_handle" in runner_source, "stdout split missing")
    require("stderr=stderr_handle" in runner_source, "stderr split missing")
    require("stderr=subprocess.STDOUT" not in runner_source, "stderr remains merged")
    return {
        "stdout_contamination_rejected": True,
        "stderr_allowlist_exact": True,
        "pty_contract_present": True,
        "pre_post_poll_races_checked": 3,
        "terminal_zombie_binding_checked": True,
        "horizon_bridge_checked": True,
    }


def main() -> None:
    candidate_before = fingerprint(CANDIDATE)
    results = {
        "mode_drift": check_mode_drift(),
        "manifest_byte_drift": check_manifest_mutation(),
        "stdout_stderr_contract_mutation": check_code_contract_mutation(
            "stderr=stderr_handle,",
            "stderr=subprocess.STDOUT,",
            "stdout/stderr split missing",
            "stream",
        ),
        "pty_contract_mutation": check_code_contract_mutation(
            "os.openpty()",
            "os.pipe()",
            "terminal stdin strategy missing",
            "pty",
        ),
        "helper_removal_temp_mutation_failure": check_helper_removal(),
        "helper_overreach_and_symlink": check_helper_guard_and_symlink(),
        "stdout_stderr_poll_zombie_horizon": check_stream_process_contracts(),
    }
    require(fingerprint(CANDIDATE) == candidate_before, "hostile matrix mutated candidate")
    print(json.dumps({"verdict": "PASS", "checks": results}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
