#!/usr/bin/env python3
"""Check the exact local P14.2 V6 candidate against current Chapter 71."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys


AUDIT = Path(__file__).resolve().parent
REPO = Path(__file__).resolve().parents[5]
CANDIDATE = Path("/private/tmp/p142_hostile_repair_v6_20260909")
SOURCE = REPO / "manuscript/parts/part6/ch71_pseudoeffective_mp_dxz.tex"
PINNED_PYTHON = Path(
    "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/"
    "agents/verification/tmp/verification-venv/bin/python"
)
EXPECTED_CANDIDATE_MANIFEST_SHA256 = (
    "3511b635413d7ace9013edd278216017096d7359ac5dd2b3155cbf179c83e97f"
)
STATEMENT_HEADER = b"% Isolated research candidate. Independent and production gates apply.\n"
TARGET_RANGES = {
    "target/STATEMENT.tex": ((615, 692), (850, 865)),
    "target/PROOF.tex": ((693, 849), (867, 897)),
    "target/EXAMPLE.tex": ((899, 927),),
}
AUDIT_FILES = (
    "CONTEXT.md",
    "LOCAL_REPLAY.md",
    "README.md",
    "RELEASE_PINS.json",
    "check_exact_live_binding.py",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_bytes(ranges: tuple[tuple[int, int], ...]) -> bytes:
    rows = SOURCE.read_bytes().splitlines(keepends=True)
    selected: list[bytes] = []
    for start, end in ranges:
        if not (1 <= start <= end <= len(rows)):
            raise RuntimeError(f"invalid source range {start}-{end}")
        selected.extend(rows[start - 1 : end])
    return b"".join(selected)


def parse_manifest(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for row in path.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^/][^\n]*)", row)
        if match is None:
            raise RuntimeError(f"malformed manifest row: {row!r}")
        expected, name = match.groups()
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts or name in result:
            raise RuntimeError(f"unsafe or duplicate manifest name: {name!r}")
        result[name] = expected
    if not result:
        raise RuntimeError("empty manifest")
    return result


def candidate_paths() -> tuple[set[str], list[Path]]:
    files: set[str] = set()
    directories = [CANDIDATE]
    for path in CANDIDATE.rglob("*"):
        if path.is_symlink():
            raise RuntimeError(f"candidate symlink: {path}")
        if path.is_dir():
            directories.append(path)
        elif path.is_file():
            files.add(path.relative_to(CANDIDATE).as_posix())
        else:
            raise RuntimeError(f"candidate nonregular path: {path}")
    return files, directories


def check_candidate() -> dict[str, str]:
    if not CANDIDATE.is_dir() or CANDIDATE.is_symlink():
        raise RuntimeError("missing or invalid V6 candidate directory")
    manifest_path = CANDIDATE / "SHA256SUMS"
    if digest(manifest_path) != EXPECTED_CANDIDATE_MANIFEST_SHA256:
        raise RuntimeError("candidate manifest fingerprint")
    manifest = parse_manifest(manifest_path)
    actual_files, directories = candidate_paths()
    expected_files = set(manifest)
    if actual_files - {"SHA256SUMS"} != expected_files:
        raise RuntimeError("candidate manifest inventory")
    for directory in directories:
        if directory.stat().st_mode & (stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH):
            raise RuntimeError(f"candidate writable directory: {directory}")
    for name, expected in manifest.items():
        path = CANDIDATE / name
        if path.is_symlink() or not path.is_file():
            raise RuntimeError(f"candidate manifest target: {name}")
        if path.stat().st_mode & (stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH):
            raise RuntimeError(f"candidate writable file: {name}")
        if digest(path) != expected:
            raise RuntimeError(f"candidate content drift: {name}")
    return manifest


def check_live_target_binding(manifest: dict[str, str]) -> None:
    if not SOURCE.is_file():
        raise RuntimeError("missing live Chapter 71 source")
    for target, ranges in TARGET_RANGES.items():
        expected = source_bytes(ranges)
        if target == "target/STATEMENT.tex":
            expected = STATEMENT_HEADER + expected
        actual = (CANDIDATE / target).read_bytes()
        if actual != expected:
            raise RuntimeError(f"live target mismatch: {target}")
        if manifest.get(target) != digest(CANDIDATE / target):
            raise RuntimeError(f"target manifest mismatch: {target}")


def materialize() -> None:
    manifest = check_candidate()
    check_live_target_binding(manifest)
    pins = {
        "candidate_manifest_sha256": EXPECTED_CANDIDATE_MANIFEST_SHA256,
        "candidate_path": str(CANDIDATE),
        "chapter71": {
            "path": str(SOURCE.relative_to(REPO)),
            "sha256": digest(SOURCE),
        },
        "target_ranges": {name: [list(pair) for pair in ranges] for name, ranges in TARGET_RANGES.items()},
        "target_sha256": {name: manifest[name] for name in TARGET_RANGES},
    }
    (AUDIT / "RELEASE_PINS.json").write_text(
        json.dumps(pins, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    context = [
        "# P14.2 V7 exact-live binding context",
        "",
        "This local audit binds the frozen V6 source-stage targets to exact current",
        "Chapter 71 bytes. It is not an independent hostile audit, a final-path smoke",
        "receipt, or a production-verification result.",
        "",
        f"Candidate manifest SHA-256: `{EXPECTED_CANDIDATE_MANIFEST_SHA256}`.",
        f"Current Chapter 71 SHA-256: `{digest(SOURCE)}`.",
        "",
    ]
    for target, ranges in TARGET_RANGES.items():
        rendered = ", ".join(f"{start}-{end}" for start, end in ranges)
        context.extend(
            (
                f"## {target} ← Chapter 71 lines {rendered}",
                "",
                "```tex",
                source_bytes(ranges).decode("utf-8").rstrip("\n"),
                "```",
                "",
            )
        )
    (AUDIT / "CONTEXT.md").write_text("\n".join(context).rstrip() + "\n", encoding="utf-8")
    (AUDIT / "LOCAL_REPLAY.md").write_text(
        "# P14.2 V7 local replay\n\n"
        "The exact V6 candidate passed a fresh local replay: its 57-entry digest "
        "manifest, read-only mode gate, catalog, release-pin, and code-contract "
        "checks passed; its pinned Python then ran 179 regression tests successfully. "
        "The target statement, proof, and example are byte-for-byte bound to the "
        "current Chapter 71 slices in `CONTEXT.md`.\n\n"
        "This replay is local evidence only. It does not replace the required "
        "independent hostile audit, final-path installation, 310-second smoke, or "
        "production verification, and does not retire P14.2.\n",
        encoding="utf-8",
    )
    lines = [f"{digest(AUDIT / name)}  {name}" for name in AUDIT_FILES]
    (AUDIT / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")


def check_audit_manifest() -> None:
    manifest = parse_manifest(AUDIT / "SHA256SUMS")
    if set(manifest) != set(AUDIT_FILES):
        raise RuntimeError("audit manifest inventory")
    for name, expected in manifest.items():
        if digest(AUDIT / name) != expected:
            raise RuntimeError(f"audit content drift: {name}")


def check() -> None:
    check_audit_manifest()
    manifest = check_candidate()
    check_live_target_binding(manifest)
    pins = json.loads((AUDIT / "RELEASE_PINS.json").read_text(encoding="utf-8"))
    if pins.get("candidate_manifest_sha256") != EXPECTED_CANDIDATE_MANIFEST_SHA256:
        raise RuntimeError("audit candidate pin")
    if pins.get("chapter71", {}).get("sha256") != digest(SOURCE):
        raise RuntimeError("audit Chapter 71 pin")
    if "independent hostile audit" not in (AUDIT / "LOCAL_REPLAY.md").read_text(encoding="utf-8"):
        raise RuntimeError("audit scope boundary")
    print("PASS_P142_V7_LOCAL_EXACT_LIVE_BINDING")


def run_tests() -> None:
    if not PINNED_PYTHON.is_file():
        raise RuntimeError("missing pinned verification Python")
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    completed = subprocess.run(
        [str(PINNED_PYTHON), "-B", "-m", "unittest", "discover", "-s", "tests", "-q"],
        cwd=CANDIDATE,
        env=environment,
        check=False,
    )
    if completed.returncode:
        raise RuntimeError(f"V6 regression replay failed: {completed.returncode}")
    print("PASS_P142_V7_LOCAL_REGRESSION_REPLAY")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--materialize", action="store_true")
    parser.add_argument("--run-tests", action="store_true")
    arguments = parser.parse_args()
    if arguments.materialize:
        materialize()
    check()
    if arguments.run_tests:
        run_tests()


if __name__ == "__main__":
    main()
