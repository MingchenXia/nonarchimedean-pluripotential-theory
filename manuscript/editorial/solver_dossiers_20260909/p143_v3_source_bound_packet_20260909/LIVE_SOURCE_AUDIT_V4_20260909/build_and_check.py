#!/usr/bin/env python3
"""Materialize and verify the local exact-live P14.3 source audit."""
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
RANGES = {
    "chapter71_finite_energy_and_p143": (1044, 1291),
    "chapter72_p143_boundary": (2803, 2824),
    "inventory_p143_boundary": (876, 888),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_range(path: Path, start: int, end: int) -> str:
    rows = path.read_text(encoding="utf-8").splitlines()
    return "\n".join(rows[start - 1 : end]) + "\n"


def write(name: str, value: str) -> None:
    (AUDIT / name).write_text(value, encoding="utf-8")


def materialize() -> None:
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    pins = {
        "git_head": head,
        "files": {key: {"path": str(value.relative_to(REPO)), "sha256": digest(value)} for key, value in FILES.items()},
        "ranges": {key: list(value) for key, value in RANGES.items()},
    }
    write("RELEASE_PINS.json", json.dumps(pins, indent=2, sort_keys=True) + "\n")
    context = "# P14.3 V4 local exact-live source audit\n\n"
    context += "This is a local integrity audit, not a new theorem or a production verifier receipt.\n"
    context += "It binds the accepted conditional V3 packet to the listed current live sources.\n\n"
    for key, (start, end) in RANGES.items():
        path_key = "chapter71" if key.startswith("chapter71") else ("chapter72" if key.startswith("chapter72") else "inventory")
        context += f"## {key} — lines {start}–{end}\n\n```text\n{source_range(FILES[path_key], start, end)}```\n\n"
    write("CONTEXT.md", context.rstrip() + "\n")
    write("README.md", "# P14.3 V4 local exact-live audit\n\nRun `python3 build_and_check.py` from this directory. The audit verifies only exact local source binding and the preserved conditional boundary; it does not retire P14.3.\n")
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
    chapter71 = FILES["chapter71"].read_text(encoding="utf-8")
    chapter72 = FILES["chapter72"].read_text(encoding="utf-8")
    inventory = FILES["inventory"].read_text(encoding="utf-8")
    context = (AUDIT / "CONTEXT.md").read_text(encoding="utf-8")
    for key, (start, end) in RANGES.items():
        path_key = "chapter71" if key.startswith("chapter71") else ("chapter72" if key.startswith("chapter72") else "inventory")
        if source_range(FILES[path_key], start, end) not in context:
            raise RuntimeError(f"missing exact range: {key}")
    required = [
        "thm:p143-dominated-divisorial-density",
        "cor:p143-all-point-kahler-comparison",
        "thm:p142-raw-transform-usc",
        "eq:pseff-finite-energy-divisorial-link",
    ]
    if not all(token in chapter71 for token in required):
        raise RuntimeError("P14.3 live dependency interface")
    if (
        "nor retires P14.3" not in chapter72
        or "**P14.3** `[T4; open; source-bound conditional theorem verified]`" not in inventory
    ):
        raise RuntimeError("P14.3 live-open boundary")
    receipt = json.loads(FILES["v3_receipt"].read_text(encoding="utf-8"))
    if receipt.get("verdict") != "correct" or receipt.get("verification_status") != "final":
        raise RuntimeError("V3 receipt status")
    print("PASS_P143_V4_LOCAL_EXACT_LIVE_AUDIT")


if __name__ == "__main__":
    materialize()
    check()
