from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


SOURCE = Path("/private/tmp/p142_hostile_audit_copy.oKqmYk/frozen")
PYTHON = Path(
    "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/"
    "agents/verification/tmp/verification-venv/bin/python"
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def make_parent_writable(path: Path, stop: Path) -> list[tuple[Path, int]]:
    changed: list[tuple[Path, int]] = []
    parent = path.parent
    while parent != stop.parent:
        old = parent.stat().st_mode & 0o777
        if not (old & 0o200):
            os.chmod(parent, old | 0o200)
            changed.append((parent, old))
        if parent == stop:
            break
        parent = parent.parent
    return changed


def restore_modes(changed: list[tuple[Path, int]]) -> None:
    for path, mode in reversed(changed):
        os.chmod(path, mode)


def rewrite_manifest(root: Path) -> None:
    manifest = root / "SHA256SUMS"
    changed = make_parent_writable(manifest, root)
    old_mode = manifest.stat().st_mode & 0o777
    os.chmod(manifest, 0o644)
    rows = []
    for path in root.rglob("*"):
        if path.is_file() and not path.is_symlink() and path != manifest:
            rows.append((path.relative_to(root).as_posix(), digest(path)))
    payload = "".join(f"{sha256}  {relative}\n" for relative, sha256 in sorted(rows))
    manifest.write_text(payload, encoding="utf-8", newline="\n")
    os.chmod(manifest, old_mode)
    restore_modes(changed)


def mutate_bytes(root: Path, relative: str, transform) -> None:
    path = root / relative
    changed = make_parent_writable(path, root)
    old_mode = path.stat().st_mode & 0o777
    os.chmod(path, 0o644)
    path.write_bytes(transform(path.read_bytes()))
    os.chmod(path, old_mode)
    restore_modes(changed)


def run_checker(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(PYTHON), "-B", "check_dossier.py"],
        cwd=root,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        capture_output=True,
        text=True,
        timeout=90,
        check=False,
    )


STATIC_SNIPPET = (
    "import importlib.util; from pathlib import Path; "
    "p=Path('check_release.py'); s=importlib.util.spec_from_file_location('hostile_release',p); "
    "m=importlib.util.module_from_spec(s); s.loader.exec_module(m); "
    "m.check_manifest(); m.check_catalog(); m.check_release_pins(); m.check_code_contract(); "
    "print('UNEXPECTED_PASS')"
)


def run_release_static(stage: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(PYTHON), "-B", "-c", STATIC_SNIPPET],
        cwd=stage,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        capture_output=True,
        text=True,
        timeout=90,
        check=False,
    )


def record(name: str, completed: subprocess.CompletedProcess[str], expected: str) -> dict[str, object]:
    combined = (completed.stdout + "\n" + completed.stderr).strip()
    return {
        "name": name,
        "status": "PASS_REJECTED" if completed.returncode != 0 and expected in combined else "FAIL",
        "return_code": completed.returncode,
        "expected_marker": expected,
        "observed_tail": combined[-900:],
    }


def top_case(name: str, mutation, expected: str) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix=f"p142_{name}_", dir="/private/tmp") as temporary:
        root = Path(temporary) / "dossier"
        shutil.copytree(SOURCE, root, copy_function=shutil.copy2, symlinks=True)
        mutation(root)
        return record(name, run_checker(root), expected)


def stage_case(name: str, mutation, expected: str, *, targeted_test: str | None = None) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix=f"p142_{name}_", dir="/private/tmp") as temporary:
        stage = Path(temporary) / "release_stage"
        shutil.copytree(SOURCE / "release_stage", stage, copy_function=shutil.copy2, symlinks=True)
        mutation(stage)
        if targeted_test is None:
            rewrite_manifest(stage)
            completed = run_release_static(stage)
        else:
            completed = subprocess.run(
                [str(PYTHON), "-B", "-m", "unittest", targeted_test],
                cwd=stage / "tests",
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
                capture_output=True,
                text=True,
                timeout=90,
                check=False,
            )
        return record(name, completed, expected)


def main() -> None:
    cases: list[dict[str, object]] = []

    cases.append(top_case(
        "regular_mode_0644",
        lambda root: os.chmod(root / "AUTHOR_REPORT.md", 0o644),
        "regular file is not frozen 0444",
    ))

    def add_symlink(root: Path) -> None:
        changed = make_parent_writable(root / "EVIL_LINK", root)
        (root / "EVIL_LINK").symlink_to("RESULT.json")
        restore_modes(changed)

    cases.append(top_case("top_symlink", add_symlink, "top-level inventory"))

    def add_cache(root: Path) -> None:
        parent = root / "release_stage/runtime"
        changed = make_parent_writable(parent / "__pycache__", root)
        cache = parent / "__pycache__"
        cache.mkdir(mode=0o755)
        payload = cache / "attack.pyc"
        payload.write_bytes(b"hostile")
        os.chmod(payload, 0o444)
        os.chmod(cache, 0o555)
        restore_modes(changed)

    cases.append(top_case("nested_bytecode_cache", add_cache, "cache:"))

    def add_special_fifo(root: Path) -> None:
        parent = root / "release_stage/runtime"
        changed = make_parent_writable(parent / "HOSTILE_FIFO", root)
        os.mkfifo(parent / "HOSTILE_FIFO", mode=0o444)
        restore_modes(changed)

    cases.append(top_case(
        "nested_special_fifo",
        add_special_fifo,
        "non-regular frozen-tree entry",
    ))

    def add_smoke(root: Path) -> None:
        stage = root / "release_stage"
        changed = make_parent_writable(stage / "STATIC_MODEL_LONG_SMOKE", root)
        (stage / "STATIC_MODEL_LONG_SMOKE").mkdir(mode=0o555)
        restore_modes(changed)

    cases.append(top_case("forbidden_smoke_tree", add_smoke, "unexpected smoke"))

    def add_artifacts(root: Path) -> None:
        stage = root / "release_stage"
        changed = make_parent_writable(stage / "artifacts", root)
        (stage / "artifacts").mkdir(mode=0o555)
        restore_modes(changed)

    cases.append(top_case(
        "forbidden_artifacts_tree",
        add_artifacts,
        "unexpected production artifacts",
    ))

    def source_byte(root: Path) -> None:
        mutate_bytes(root, "release_stage/runtime/sources/dxz_2302.02541v3.txt", lambda raw: raw[:-1] + b"X")

    cases.append(top_case("source_byte_tamper", source_byte, "manifest byte mismatch"))

    def coherent_target(root: Path) -> None:
        for relative in ("target/STATEMENT.tex", "release_stage/target/STATEMENT.tex"):
            mutate_bytes(root, relative, lambda raw: raw + b"% hostile\n")
        rewrite_manifest(root / "release_stage")
        rewrite_manifest(root)

    cases.append(top_case("coherent_target_and_manifest_repin", coherent_target, "outer target digest"))

    def duplicate_json(root: Path) -> None:
        mutate_bytes(root, "RESULT.json", lambda raw: raw.replace(b'{\n  "format":', b'{\n  "format": "duplicate",\n  "format":', 1))
        rewrite_manifest(root)

    cases.append(top_case("duplicate_json_key_with_top_repin", duplicate_json, "duplicate JSON key"))

    cases.append(stage_case(
        "lf_helper_splitlines",
        lambda stage: mutate_bytes(
            stage,
            "runtime/lf_source_lines.py",
            lambda raw: raw.replace(b'path.read_bytes().split(b"\\x0a")', b'path.read_text(encoding="utf-8").splitlines()'),
        ),
        "byte-level LF-only source split missing",
    ))

    cases.append(stage_case(
        "merged_stderr",
        lambda stage: mutate_bytes(
            stage,
            "run_static_model_long_smoke.py",
            lambda raw: raw.replace(b"stderr=stderr_handle,", b"stderr=subprocess.STDOUT,", 1),
        ),
        "smoke stdout/stderr split missing",
    ))

    cases.append(stage_case(
        "no_input_pty_removed",
        lambda stage: mutate_bytes(
            stage,
            "run_static_model_long_smoke.py",
            lambda raw: raw.replace(b"os.openpty()", b"os.pipe()", 1),
        ),
        "dedicated terminal stdin strategy missing",
    ))

    cases.append(stage_case(
        "poll_after_scan_removed",
        lambda stage: mutate_bytes(
            stage,
            "run_static_model_long_smoke.py",
            lambda raw: raw.replace(
                b"descendants = scanner(process.pid)\n    if process.poll() is not None:",
                b"descendants = scanner(process.pid)\n    if False:",
                1,
            ),
        ),
        "AssertionError",
        targeted_test="test_runtime.SmokeProcessObservationTests.test_exit_between_poll_and_ps_is_terminal_not_identity_drift",
    ))

    cases.append(stage_case(
        "locator_downgrade",
        lambda stage: mutate_bytes(
            stage,
            "runtime/release_pins.py",
            lambda raw: raw.replace(b"(437, 458,", b"(437, 448,", 1),
        ),
        "release_pins.py digest mismatch",
    ))

    require_all = all(case["status"] == "PASS_REJECTED" for case in cases)
    print(json.dumps({"status": "PASS" if require_all else "FAIL", "case_count": len(cases), "cases": cases}, indent=2, sort_keys=True))
    if not require_all:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
