#!/usr/bin/env python3
"""Materialize exact, item-structured evidence for the P14.2 V6 audit."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CANDIDATE = Path("/private/tmp/p142_hostile_repair_v6_20260909")
OUTPUT = ROOT / "PROOF_CONTEXT.md"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def display_name(path: Path) -> str:
    try:
        return path.relative_to(CANDIDATE).as_posix()
    except ValueError:
        return path.relative_to(ROOT).as_posix()


def append_exhibits(lines: list[str], exhibits: tuple[Path, ...]) -> None:
    for exhibit in exhibits:
        text = exhibit.read_text(encoding="utf-8")
        lines.extend(
            (
                "",
                f"Exact exhibit {display_name(exhibit)}; SHA-256 {digest(exhibit)}.",
                "Every following line is indented evidence, not a proof heading.",
            )
        )
        lines.extend(f"    {line}" if line else "" for line in text.splitlines())


def append_test_range(lines: list[str], start: int, end: int) -> None:
    source = CANDIDATE / "tests/test_runtime.py"
    source_lines = source.read_text(encoding="utf-8").splitlines()
    if not (1 <= start <= end <= len(source_lines)):
        raise ValueError(f"invalid test range {start}-{end}")
    lines.extend(
        (
            "",
            (
                "Exact targeted regression exhibit tests/test_runtime.py:"
                f"{start}-{end}; complete-file SHA-256 {digest(source)}."
            ),
            "Every following line is indented evidence, not a proof heading.",
        )
    )
    lines.extend(
        f"    {line}" if line else "" for line in source_lines[start - 1 : end]
    )


def append_item(
    lines: list[str],
    *,
    title: str,
    statement: str,
    proof: str,
    exhibits: tuple[Path, ...] = (),
    depends_on: str = "",
) -> None:
    lines.extend(
        (
            f"# {title}",
            "",
            f"<!-- rethlas-depends-on: {depends_on} -->",
            "",
            "## statement",
            statement,
            "",
            "## proof",
            proof,
        )
    )
    append_exhibits(lines, exhibits)
    lines.append("")


def main() -> None:
    final_statement = (ROOT / "STATEMENT.tex").read_text(encoding="utf-8").rstrip("\n")
    final_proof = (ROOT / "PROOF.tex").read_text(encoding="utf-8").rstrip("\n")
    lines: list[str] = []
    append_item(
        lines,
        title="lemma thm:p142-v6-manifest-and-checker",
        statement=(
            "The exact frozen V6 tree has a checker that verifies full manifest "
            "inventory and SHA-256 rows and rejects writable release paths before "
            "any limited source-stage integrity pass."
        ),
        proof=(
            "Inspect the exact stage report, manifest, and checker. Verify that "
            "the checker independently enumerates files, rejects symlinks and "
            "nonregular paths, checks every digest, and scans the root plus every "
            "descendant for write bits. Do not infer a smoke result."
        ),
        exhibits=(
            CANDIDATE / "STAGING_REPORT.md",
            CANDIDATE / "SHA256SUMS",
            CANDIDATE / "check_release.py",
            ROOT / "LOCAL_PREFLIGHT.md",
            ROOT / "AUDIT_SCOPE.md",
        ),
    )
    append_item(
        lines,
        title="lemma thm:p142-v6-runner-replay-binding",
        statement=(
            "The runner writes a passed smoke receipt only after the exact frozen "
            "release checker validates parsed stdout, stderr, and process evidence."
        ),
        proof=(
            "Inspect the runner's pending-to-final status transition and the checker "
            "functions it calls. Confirm that any validator failure becomes a failed "
            "receipt and that lifecycle, item shape, decoded diagnostics, type-exact "
            "MCP arguments/results, usage schema, and complete process evidence are "
            "all covered before pass."
        ),
        exhibits=(
            CANDIDATE / "run_static_model_long_smoke.py",
            CANDIDATE / "static_model_smoke_mcp.py",
        ),
    )
    append_item(
        lines,
        title="lemma thm:p142-v6-authenticated-source-tools",
        statement=(
            "The host and decorated MCP authenticate inert pin data before use and "
            "address fixed source lines using only LF bytes; their pre-server request "
            "and digest gates are fail-closed."
        ),
        proof=(
            "Trace the raw pin authentication, source routing, LF-only decoder, "
            "target/request validation, and delayed FastMCP import in the exact host "
            "and MCP sources. The behavioral endpoint regression is supplied below; "
            "do not substitute a source-text count for that behavior."
        ),
        exhibits=(
            CANDIDATE / "runtime/release_pins.json",
            CANDIDATE / "runtime/lf_source_lines.py",
            CANDIDATE / "runtime/hardened_service.py",
            CANDIDATE / "runtime/hardened_mcp.py",
            CANDIDATE / "runtime/contract.md",
        ),
    )
    append_item(
        lines,
        title="lemma thm:p142-v6-adversarial-regressions",
        statement=(
            "The supplied post-freeze 179-test regression run includes targeted "
            "counterexamples for every V5 critical repair and evidence gap."
        ),
        proof=(
            "Inspect the complete-file-digest-bound test ranges. Verify false-zero "
            "decoded diagnostic rejection, strict JSON equality and wrappers, runner "
            "process-gate invocation, LF-control-byte MCP endpoint behavior, manifest "
            "content/inventory/mode mutation rejection, and the recorded-statement "
            "digest FastMCP-sentinel mutation. The preflight records the exact run."
        ),
    )
    append_test_range(lines, 1, 730)
    append_test_range(lines, 1360, 1435)
    append_test_range(lines, 3665, 4225)
    lines.append("")
    append_item(
        lines,
        title="theorem thm:p142-v6-pre-smoke-hostile-audit",
        statement=final_statement,
        proof=final_proof,
        depends_on=(
            "thm:p142-v6-manifest-and-checker, thm:p142-v6-runner-replay-binding, "
            "thm:p142-v6-authenticated-source-tools, thm:p142-v6-adversarial-regressions"
        ),
    )
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUTPUT} ({len(OUTPUT.read_bytes())} bytes)")


if __name__ == "__main__":
    main()
