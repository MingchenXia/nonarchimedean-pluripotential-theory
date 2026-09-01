from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
from typing import Any


HERE = Path(__file__).resolve().parent
CANDIDATE = Path(
    "/private/tmp/"
    "p148_smoke_infrastructure_repaired_readonly_authored_stage_dossier_v2_20260901"
)
STAGE = CANDIDATE / "release_stage"
PACKET = CANDIDATE / "packet"
V1_STAGE = Path(
    "/private/tmp/p148_smoke_infrastructure_repaired_authored_stage_dossier_v1_20260901/"
    "release_stage"
)
PYTHON = Path(
    "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/"
    "agents/verification/tmp/verification-venv/bin/python"
)

CANDIDATE_TOP_SHA = "0645efed9d2ba12a99501fe07a1988e4e7a09a20e496d21c38937774d1d29d46"
STAGE_SHA = "837d5bb55d134bf4040c1083ffb1cf068b6b6c83bbc16bd7e86f2a1d8f247912"
V1_STAGE_SHA = "4c2a6c9d61966aeac3f0c5c27284a0746d1a8bcc4520340016247947f9c9accc"
PACKET_SHA = "87ca97e402d845d4628f72d67c28e19b05674a23f3aa478be04221cecd5df0ff"
STATEMENT_SHA = "9cd8fe1533c99d9d2de9e351610da4b7843d156a523d97344032cf75e3953715"
PROOF_SHA = "adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9"
V1_CHANGED = {"STAGING_REPORT.md", "tests/test_runtime.py"}

PROTECTED_V1_PATHS = {
    "check_release.py",
    "run_static_model_long_smoke.py",
    "runtime/canonical_reference.py",
    "runtime/contract.md",
    "runtime/hardened_mcp.py",
    "runtime/hardened_service.py",
    "runtime/memory_record.schema.json",
    "runtime/model_catalog.gpt-5.6-sol.json",
    "runtime/release_pins.py",
    "runtime/verification_output.schema.json",
    "static_model_smoke_mcp.py",
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
        require("__pycache__" not in path.parts, f"cache path: {root}: {relative}")
        if stat.S_ISDIR(info.st_mode):
            continue
        require(stat.S_ISREG(info.st_mode), f"special path: {root}: {relative}")
        require(path.suffix != ".pyc", f"bytecode: {root}: {relative}")
        if relative != "SHA256SUMS":
            result.append(relative)
    return sorted(result)


def validate_manifest(root: Path, expected_sha: str) -> dict[str, str]:
    manifest = root / "SHA256SUMS"
    require(sha(manifest) == expected_sha, f"manifest digest: {root}")
    rows = manifest_rows(manifest)
    require(sorted(rows) == actual_files(root), f"manifest inventory: {root}")
    for relative, digest in rows.items():
        require(sha(root / relative) == digest, f"manifest row: {root}: {relative}")
    return rows


def validate_own_manifest() -> None:
    manifest = HERE / "SHA256SUMS"
    rows = manifest_rows(manifest)
    require(sorted(rows) == actual_files(HERE), "audit manifest inventory")
    for relative, digest in rows.items():
        require(sha(HERE / relative) == digest, f"audit manifest row: {relative}")


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


def validate_exact_read_only_tree(root: Path) -> tuple[int, int]:
    directories = 0
    files = 0
    for path in [root, *sorted(root.rglob("*"))]:
        relative = "." if path == root else path.relative_to(root).as_posix()
        info = path.lstat()
        require(not stat.S_ISLNK(info.st_mode), f"read-only symlink: {relative}")
        if stat.S_ISDIR(info.st_mode):
            directories += 1
            expected = 0o555
        else:
            require(stat.S_ISREG(info.st_mode), f"read-only special path: {relative}")
            files += 1
            expected = 0o444
        require(
            stat.S_IMODE(info.st_mode) == expected,
            f"read-only mode: {relative}: {stat.S_IMODE(info.st_mode):04o}",
        )
    return directories, files


def check_candidate() -> None:
    top_rows = validate_manifest(CANDIDATE, CANDIDATE_TOP_SHA)
    stage_rows = validate_manifest(STAGE, STAGE_SHA)
    packet_rows = validate_manifest(PACKET, PACKET_SHA)
    require(len(stage_rows) == 44, "release row count")
    require(sha(PACKET / "PROPOSED_STATEMENT.tex") == STATEMENT_SHA, "statement")
    require(sha(PACKET / "PROOF.tex") == PROOF_SHA, "proof")
    require("PROPOSED_STATEMENT.tex" in packet_rows and "PROOF.tex" in packet_rows,
            "packet target inventory")
    directories, files = validate_exact_read_only_tree(CANDIDATE)
    require((directories, files) == (7, 70), "candidate path-kind counts")
    require(not (STAGE / "STATIC_MODEL_LONG_SMOKE").exists(), "live smoke tree")
    require(not (STAGE / "artifacts").exists(), "production artifact tree")
    require(not any("__pycache__" in path.parts for path in CANDIDATE.rglob("*")),
            "candidate bytecode cache")
    require(len(top_rows) == 69, "candidate top row count")

    v1_rows = validate_manifest(V1_STAGE, V1_STAGE_SHA)
    require(set(stage_rows) == set(v1_rows), "v1 path inventory")
    changed = {relative for relative in stage_rows if stage_rows[relative] != v1_rows[relative]}
    require(changed == V1_CHANGED, f"unexpected v1 changes: {sorted(changed)}")
    require(len(stage_rows) - len(changed) == 42, "v1 preserved-row count")
    source_paths = {
        relative for relative in stage_rows if relative.startswith("runtime/sources/")
    }
    require(len(source_paths) == 31, "fixed-source count")
    for relative in source_paths | PROTECTED_V1_PATHS:
        require(
            (STAGE / relative).read_bytes() == (V1_STAGE / relative).read_bytes(),
            f"protected v1 byte drift: {relative}",
        )

    require(
        (HERE / "candidate_top_SHA256SUMS").read_bytes()
        == (CANDIDATE / "SHA256SUMS").read_bytes(),
        "candidate top snapshot",
    )
    require(
        (HERE / "candidate_release_SHA256SUMS").read_bytes()
        == (STAGE / "SHA256SUMS").read_bytes(),
        "candidate release snapshot",
    )
    require(
        (HERE / "candidate_packet_SHA256SUMS").read_bytes()
        == (PACKET / "SHA256SUMS").read_bytes(),
        "candidate packet snapshot",
    )
    require(
        (HERE / "v1_release_SHA256SUMS").read_bytes()
        == (V1_STAGE / "SHA256SUMS").read_bytes(),
        "v1 release snapshot",
    )


def run_candidate_checker() -> None:
    completed = subprocess.run(
        [str(PYTHON), "-B", "check_dossier.py"],
        cwd=CANDIDATE,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    output = completed.stdout + "\n" + completed.stderr
    require(completed.returncode == 0, f"candidate checker failed:\n{output}")
    require(
        "PASS_FROZEN_P148_SMOKE_INFRASTRUCTURE_AUTHORED_STAGE" in output,
        "candidate checker marker",
    )
    require('"tests": 161' in output, "candidate checker test inventory")


def run_hostile_matrix() -> None:
    completed = subprocess.run(
        [str(PYTHON), "-B", "hostile_mutations.py"],
        cwd=HERE,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    require(
        completed.returncode == 0,
        f"hostile matrix failed:\n{completed.stdout}\n{completed.stderr}",
    )
    value = json.loads(completed.stdout, object_pairs_hook=reject_duplicates)
    require(value.get("verdict") == "PASS", "hostile matrix verdict")
    require(len(value.get("checks", {})) == 7, "hostile matrix executable groups")


def check_ledgers() -> None:
    result = strict_json(HERE / "RESULT.json")
    require(result["verdict"] == "PASS_READY_FOR_NEW_FINAL_PATH_SMOKE", "result verdict")
    require(result["candidate_top_manifest_sha256"] == CANDIDATE_TOP_SHA,
            "result top digest")
    require(result["release_stage_manifest_sha256"] == STAGE_SHA,
            "result release digest")
    require(result["fixed_sources"] == 31, "result source count")
    require(result["v1_byte_identical_release_rows"] == 42, "result preservation")
    require(result["exact_suite"]["complete_runs"] == 4, "result suite runs")
    require(result["exact_suite"]["passes"] == 4, "result suite passes")
    require(result["hostile_mutations"] == result["hostile_mutations_passed"] == 12,
            "result hostile count")
    require(result["blockers"] == [], "result blockers")
    require(all(value is False for value in result["prohibited_actions_performed"].values()),
            "prohibited action ledger")
    tests = strict_json(HERE / "TEST_RUNS.json")
    require(tests["complete_suite_runs_total"] == tests["complete_suite_passes_total"] == 4,
            "test-run total")
    require(len(tests["independent_direct_complete_suite_runs"]) == 2,
            "direct independent runs")
    hostile = strict_json(HERE / "HOSTILE_MUTATIONS.json")
    require(hostile["verdict"] == "PASS", "hostile ledger verdict")
    require(hostile["case_count"] == hostile["passed"] == 12 and hostile["failed"] == 0,
            "hostile ledger count")


def main() -> None:
    validate_exact_read_only_tree(HERE)
    validate_own_manifest()
    candidate_before = fingerprint(CANDIDATE)
    audit_before = fingerprint(HERE)
    check_candidate()
    check_ledgers()
    run_candidate_checker()
    run_hostile_matrix()
    require(fingerprint(CANDIDATE) == candidate_before, "candidate changed during audit check")
    require(fingerprint(HERE) == audit_before, "audit dossier changed during check")
    print("PASS_INDEPENDENT_P148_READ_ONLY_SMOKE_INFRASTRUCTURE_AUDIT_V2")
    print(json.dumps({"candidate": CANDIDATE_TOP_SHA, "tests_per_run": 161}, sort_keys=True))


if __name__ == "__main__":
    main()
