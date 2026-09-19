#!/usr/bin/env python3
"""Extract the exact live unconditional P14.3 statements and proofs."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
DOSSIER = Path(__file__).resolve().parent
CH60 = REPO_ROOT / "manuscript/parts/part5/ch60_mp_psh.tex"
CH59 = REPO_ROOT / "manuscript/parts/part5/ch59_complex_dual_complexes.tex"
CH53 = REPO_ROOT / "manuscript/parts/part5/ch53_transcendental_metrics.tex"
CH54 = REPO_ROOT / "manuscript/parts/part5/ch54_operations_trace.tex"
CH71 = REPO_ROOT / "manuscript/parts/part6/ch71_pseudoeffective_mp_dxz.tex"

TARGETS = (
    (CH60, "prop:mp-psh-decreasing-stability"),
    (CH71, "thm:p143-mp-section"),
    (CH71, "thm:p143-full-kahler-comparison"),
)

PREMISES = (
    (CH59, "prop:mp-tropical-compactness"),
    (CH60, "prop:mp-model-psh-stability"),
    (CH60, "def:mp-general-psh"),
    (CH60, "thm:mp-psh-divisorial"),
    (CH53, "prop:tna-common-terminal"),
    (CH53, "thm:tna-positive-volume"),
    (CH54, "def:operations-maximum"),
    (CH54, "def:operations-infimum"),
    (CH71, "prop:pseff-one-curve-transform"),
    (CH71, "eq:pseff-constant-transform"),
    (CH71, "thm:pseff-perturbation-independent-transform"),
    (CH71, "thm:pseff-divisorial-inversion"),
    (CH71, "thm:pseff-kahler-finite-energy-link"),
    (CH71, "thm:p143-dominated-divisorial-density"),
    (CH71, "cor:p143-all-point-kahler-comparison"),
    (CH71, "cor:p141-finite-energy-raw-image"),
    (CH71, "prop:pseff-operation-formulas"),
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def extract(path: Path, label: str) -> tuple[bytes, bytes]:
    data = path.read_bytes()
    marker = f"\\label{{{label}}}".encode()
    label_at = data.index(marker)
    starts = list(re.finditer(rb"\\begin\{([A-Za-z]+)\}", data[:label_at]))
    if not starts:
        raise SystemExit(f"no environment before {label} in {path}")
    start_match = starts[-1]
    environment = start_match.group(1)
    end_marker = b"\\end{" + environment + b"}"
    statement_end = data.index(end_marker, label_at) + len(end_marker)
    proof_start = data.index(b"\\begin{proof}", statement_end)
    proof_end_marker = b"\\end{proof}"
    proof_end = data.index(proof_end_marker, proof_start) + len(proof_end_marker)
    return data[start_match.start() : statement_end], data[proof_start:proof_end]


def materialize(kind: str, chunks: list[tuple[Path, str, bytes]]) -> bytes:
    output = bytearray()
    output.extend(f"P14.3 EXACT LIVE {kind.upper()} PACKET\n".encode())
    for path, label, chunk in chunks:
        output.extend(b"\nBEGIN EXACT LIVE CHUNK\n")
        output.extend(f"source: {path.relative_to(REPO_ROOT)}\n".encode())
        output.extend(f"label: {label}\n".encode())
        output.extend(f"chunk-sha256: {sha256(chunk)}\n".encode())
        output.extend(b"BEGIN CHUNK BYTES\n")
        output.extend(chunk)
        if output[-1:] != b"\n":
            output.extend(b"\n")
        output.extend(b"END CHUNK BYTES\n")
        output.extend(b"END EXACT LIVE CHUNK\n")
    return bytes(output)


def main() -> None:
    statements: list[tuple[Path, str, bytes]] = []
    proofs: list[tuple[Path, str, bytes]] = []
    premises: list[tuple[Path, str, bytes]] = []
    ledger = []
    for path, label in TARGETS:
        statement, proof = extract(path, label)
        statements.append((path, label, statement))
        proofs.append((path, label, proof))
        ledger.append(
            (
                str(path.relative_to(REPO_ROOT)),
                label,
                sha256(statement),
                sha256(proof),
                "target",
            )
        )

    for path, label in PREMISES:
        statement, _ = extract(path, label)
        premises.append((path, label, statement))
        ledger.append(
            (
                str(path.relative_to(REPO_ROOT)),
                label,
                sha256(statement),
                "-",
                "declared-premise",
            )
        )

    statement_packet = materialize("statement", statements)
    proof_packet = materialize("proof", proofs)
    premise_packet = materialize("declared premise statement", premises)
    (DOSSIER / "STATEMENT.tex").write_bytes(statement_packet)
    (DOSSIER / "PROOF.tex").write_bytes(proof_packet)
    (DOSSIER / "PREMISE_STATEMENTS.tex").write_bytes(premise_packet)

    lines = [
        "source\tlabel\tstatement_sha256\tproof_sha256\trole",
        *("\t".join(row) for row in ledger),
        f"STATEMENT.tex\tpacket\t{sha256(statement_packet)}\t-\tpacket",
        f"PROOF.tex\tpacket\t-\t{sha256(proof_packet)}\tpacket",
        f"PREMISE_STATEMENTS.tex\tpacket\t{sha256(premise_packet)}\t-\tpacket",
    ]
    (DOSSIER / "LIVE_CHUNK_HASHES.tsv").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
