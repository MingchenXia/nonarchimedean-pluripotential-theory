#!/usr/bin/env python3
"""Read-only integrity and source-boundary checks for the P14.8 V7 packet."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


AUDIT = Path(__file__).resolve().parent
REPO = AUDIT.parents[4]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def range_text(source: bytes, start: int, end: int) -> str:
    rows = source.decode("utf-8").splitlines()
    return "\n".join(rows[start - 1 : end]) + "\n"


def pinned_blob(commit: str, relative: str) -> bytes:
    return subprocess.check_output(
        ["git", "show", f"{commit}:{relative}"], cwd=REPO
    )


def main() -> None:
    pins = json.loads((AUDIT / "RELEASE_PINS.json").read_text(encoding="utf-8"))
    subprocess.run(
        ["git", "rev-parse", "--verify", f"{pins['git_head']}^{{commit}}"],
        cwd=REPO,
        check=True,
        stdout=subprocess.DEVNULL,
    )

    for item in pins["files"].values():
        source = pinned_blob(pins["git_head"], item["path"])
        require(
            hashlib.sha256(source).hexdigest() == item["sha256"],
            f"pinned source digest: {item['path']}",
        )

    require(
        hashlib.sha256(
            pinned_blob(pins["git_head"], pins["files"]["v6_statement"]["path"])
        ).hexdigest()
        == pins["v6_statement_sha256"],
        "V6 statement published identity",
    )

    manifest = {}
    for row in (AUDIT / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        expected, name = row.split("  ", 1)
        manifest[name] = expected
    actual = {path.name for path in AUDIT.iterdir() if path.is_file() and path.name != "SHA256SUMS"}
    require(set(manifest) == actual, "packet manifest inventory")
    for name, expected in manifest.items():
        require(digest(AUDIT / name) == expected, f"packet digest: {name}")

    context = (AUDIT / "AUDIT_PROOF_CONTEXT.md").read_text(encoding="utf-8")
    statement = (AUDIT / "AUDIT_STATEMENT.md").read_text(encoding="utf-8")
    for key, source_name in (
        ("ch51_scope_and_comparisons", "chapter51"),
        ("ch51_strong_openness", "chapter51"),
        ("ch51_i_preorder", "chapter51"),
        ("ch51_i_envelope_and_projection", "chapter51"),
        ("ch51_npp_bidegree_one", "chapter51"),
        ("ch51_npp_ledger", "chapter51"),
        ("ch51_cantor_family", "chapter51"),
        ("ch72_p148_status", "chapter72"),
        ("inventory_p148_status", "inventory"),
    ):
        start, end = pins["ranges"][key]
        source = pinned_blob(pins["git_head"], pins["files"][source_name]["path"])
        require(range_text(source, start, end) in context, f"exact source range: {key}")
    v6_statement = pinned_blob(
        pins["git_head"], pins["files"]["v6_statement"]["path"]
    ).decode("utf-8")
    v6_statement_indented = "\n".join(f"    {row}" for row in v6_statement.splitlines()) + "\n"
    require(v6_statement_indented in context, "complete frozen V6 target statement")
    pins_text = (AUDIT / "RELEASE_PINS.json").read_text(encoding="utf-8")
    require(pins_text in context, "provenance metadata is attached")
    require(context.startswith("# theorem thm:p148-v7-exact-live-integration\n\n## statement\n"), "V7 theorem protocol header")
    require(context.count("\n## statement\n") == 1, "exactly one theorem statement section")
    require(context.count("\n## proof\n") == 1, "exactly one theorem proof section")
    live_statement = context.split("## statement\n\n", 1)[1].split("\n\n## proof", 1)[0]
    require(live_statement.rstrip("\n") == statement.rstrip("\n"), "exact target statement binding")

    for token in (
        "unique normalized \\(\\mathcal I\\)-model representative",
        "without a positive-nonpluripolar-mass hypothesis",
        "nonpluripolar mass \\(1-s\\)",
        "neither a raw representative nor its raw mass descends",
        "P14.8 open; this review does not retire it",
        "an authenticated premise of this model review",
    ):
        require(token in statement, f"audit claim boundary: {token}")
    inventory = pinned_blob(
        pins["git_head"], pins["files"]["inventory"]["path"]
    ).decode("utf-8")
    chapter72 = pinned_blob(
        pins["git_head"], pins["files"]["chapter72"]["path"]
    ).decode("utf-8")
    require("**P14.8** `[T5; open; source-bound exact dichotomy verified]`" in inventory, "inventory live-open status")
    require("P14.8 does not retire or change the" in chapter72, "Chapter 72 live-open status")
    print("PASS_P148_V7_EXACT_LIVE_AUDIT")


if __name__ == "__main__":
    main()
