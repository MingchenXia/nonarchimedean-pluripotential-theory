#!/usr/bin/env python3
"""Materialize and verify the current exact-live P14.3 source audit.

V4 is an historical record whose inherited Chapter 72 and inventory line
numbers no longer locate P14.3.  This successor preserves V4 and resolves the
three live excerpts from explicit content anchors before pinning their bytes.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


AUDIT = Path(__file__).resolve().parent
REPO = AUDIT.parents[4]
V3 = AUDIT.parent
FILES = {
    "chapter71": REPO / "manuscript/parts/part6/ch71_pseudoeffective_mp_dxz.tex",
    "chapter72": REPO / "manuscript/parts/part6/ch72_major_open_problems.tex",
    "inventory": REPO / "manuscript/editorial/open_problem_atomic_inventory_20260824.md",
    "v3_statement": V3 / "STATEMENT_V3.md",
    "v3_proof": V3 / "PROOF_V3.md",
    "v3_receipt": V3 / "VERIFICATION_RUN_V3_20260909/response.json",
}
ANCHORS = {
    "chapter71_finite_energy_and_p143": (
        "chapter71",
        r"\begin{theorem}\label{thm:pseff-kahler-finite-energy-link}",
        r"\begin{corollary}\label{cor:p141-finite-energy-raw-image}",
        False,
    ),
    "chapter72_p143_boundary": (
        "chapter72",
        "The domination-preserving rational-divisorial approximation",
        "alter the P14.3 status.",
        True,
    ),
    "inventory_p143_boundary": (
        "inventory",
        "- **P14.3** `[T4; open; source-bound conditional theorem verified]`",
        "replayable release pin or production verifier receipt.",
        True,
    ),
}
RANGE_TOKENS = {
    "chapter71_finite_energy_and_p143": (
        "thm:p143-dominated-divisorial-density",
        "cor:p143-all-point-kahler-comparison",
        "thm:p142-raw-transform-usc",
        "eq:pseff-finite-energy-divisorial-link",
    ),
    "chapter72_p143_boundary": (
        "thm:p143-dominated-divisorial-density",
        "cor:p143-all-point-kahler-comparison",
        "nor retires P14.3",
    ),
    "inventory_p143_boundary": (
        "**P14.3** `[T4; open; source-bound conditional theorem verified]`",
        "normalization are explicit premises.",
        "remains open.",
        "live-open boundary; it is a local integrity check",
    ),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_range(path: Path, start: int, end: int) -> str:
    rows = path.read_text(encoding="utf-8").splitlines()
    return "\n".join(rows[start - 1 : end]) + "\n"


def locate(
    key: str, path: Path, start_token: str, end_token: str, include_end: bool
) -> tuple[int, int]:
    rows = path.read_text(encoding="utf-8").splitlines()
    start = next((index for index, row in enumerate(rows) if start_token in row), None)
    if start is None:
        raise RuntimeError(f"missing start anchor: {start_token}")
    end = next(
        (index for index, row in enumerate(rows[start:], start) if end_token in row),
        None,
    )
    if end is None:
        raise RuntimeError(f"missing end anchor: {end_token}")
    if not include_end:
        end -= 1
    excerpt = "\n".join(rows[start : end + 1])
    if not all(token in excerpt for token in RANGE_TOKENS[key]):
        raise RuntimeError(f"incomplete anchored excerpt: {start_token}")
    return start + 1, end + 1


def resolved_ranges() -> dict[str, dict[str, int | str]]:
    result: dict[str, dict[str, int | str]] = {}
    for key, (file_key, start_token, end_token, include_end) in ANCHORS.items():
        start, end = locate(key, FILES[file_key], start_token, end_token, include_end)
        result[key] = {"file": file_key, "start": start, "end": end}
    return result


def write(name: str, value: str) -> None:
    (AUDIT / name).write_text(value, encoding="utf-8")


def materialize() -> None:
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    ranges = resolved_ranges()
    pins = {
        "git_head": head,
        "files": {key: {"path": str(value.relative_to(REPO)), "sha256": digest(value)} for key, value in FILES.items()},
        "ranges": ranges,
    }
    write("RELEASE_PINS.json", json.dumps(pins, indent=2, sort_keys=True) + "\n")
    context = "# P14.3 V5 current exact-live source audit\n\n"
    context += "This is a local integrity audit, not a new theorem or a production verifier receipt.\n"
    context += "It binds the accepted conditional V3 packet to the listed current live sources.\n\n"
    for key, item in ranges.items():
        path = FILES[str(item["file"])]
        context += f"## {key} — lines {item['start']}–{item['end']}\n\n```text\n"
        context += source_range(path, int(item["start"]), int(item["end"]))
        context += "```\n\n"
    write("CONTEXT.md", context.rstrip() + "\n")
    names = ["CONTEXT.md", "README.md", "RELEASE_PINS.json", "build_and_check.py"]
    write("SHA256SUMS", "\n".join(f"{digest(AUDIT / name)}  {name}" for name in names) + "\n")


def check() -> None:
    pins = json.loads((AUDIT / "RELEASE_PINS.json").read_text(encoding="utf-8"))
    for key, item in pins["files"].items():
        path = REPO / item["path"]
        if digest(path) != item["sha256"]:
            raise RuntimeError(f"source drift: {key}")
    manifest = dict(row.split("  ", 1) for row in (AUDIT / "SHA256SUMS").read_text().splitlines())
    for expected, name in manifest.items():
        if digest(AUDIT / name) != expected:
            raise RuntimeError(f"packet drift: {name}")
    context = (AUDIT / "CONTEXT.md").read_text(encoding="utf-8")
    for key, item in pins["ranges"].items():
        path = FILES[item["file"]]
        excerpt = source_range(path, int(item["start"]), int(item["end"]))
        if excerpt not in context:
            raise RuntimeError(f"missing exact range: {key}")
        if not all(token in excerpt for token in RANGE_TOKENS[key]):
            raise RuntimeError(f"incomplete pinned range: {key}")
    receipt = json.loads(FILES["v3_receipt"].read_text(encoding="utf-8"))
    if receipt.get("verdict") != "correct" or receipt.get("verification_status") != "final":
        raise RuntimeError("V3 receipt status")
    print("PASS_P143_V5_CURRENT_EXACT_LIVE_AUDIT")


if __name__ == "__main__":
    materialize()
    check()
