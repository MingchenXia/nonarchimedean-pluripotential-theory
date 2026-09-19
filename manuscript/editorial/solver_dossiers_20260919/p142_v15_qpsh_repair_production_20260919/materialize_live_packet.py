#!/usr/bin/env python3
"""Extract the exact live P14.2 V15 repair and its internal premise."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
DOSSIER = Path(__file__).resolve().parent
CH71 = REPO_ROOT / "manuscript/parts/part6/ch71_pseudoeffective_mp_dxz.tex"

TARGETS = (
    "lem:p142-monotone-parameter-supremum",
    "thm:p142-raw-transform-usc",
    "cor:p142-pseudoeffective-raw-usc",
)
PREMISES = ("thm:pseff-perturbation-independent-transform",)
STATEMENT_ONLY_PREMISES = ("prop:pseff-one-curve-transform",)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def environment(data: bytes, label: str) -> tuple[bytes, int]:
    marker = f"\\label{{{label}}}".encode()
    label_at = data.index(marker)
    starts = list(re.finditer(rb"\\begin\{([A-Za-z]+)\}(?:\[[^\n]*\])?", data[:label_at]))
    if not starts:
        raise SystemExit(f"no environment before {label}")
    start_match = starts[-1]
    name = start_match.group(1)
    end_marker = b"\\end{" + name + b"}"
    end = data.index(end_marker, label_at) + len(end_marker)
    return data[start_match.start() : end], end


def proof_after(data: bytes, offset: int, label: str) -> bytes:
    named = b"\\begin{proof}[Proof of \\cref{" + label.encode() + b"}]"
    try:
        start = data.index(named, offset)
    except ValueError:
        start = data.index(b"\\begin{proof}", offset)
    end_marker = b"\\end{proof}"
    end = data.index(end_marker, start) + len(end_marker)
    return data[start:end]


def packet(title: str, chunks: list[tuple[str, bytes]]) -> bytes:
    output = bytearray(f"P14.2 V15 EXACT LIVE {title.upper()} PACKET\n".encode())
    for label, chunk in chunks:
        output.extend(b"\nBEGIN EXACT LIVE CHUNK\n")
        output.extend(f"label: {label}\n".encode())
        output.extend(f"chunk-sha256: {sha256(chunk)}\n".encode())
        output.extend(b"BEGIN CHUNK BYTES\n")
        output.extend(chunk)
        if output[-1:] != b"\n":
            output.extend(b"\n")
        output.extend(b"END CHUNK BYTES\nEND EXACT LIVE CHUNK\n")
    return bytes(output)


def main() -> None:
    data = CH71.read_bytes()
    statements: list[tuple[str, bytes]] = []
    proofs: list[tuple[str, bytes]] = []
    premise_statements: list[tuple[str, bytes]] = []
    premise_proofs: list[tuple[str, bytes]] = []
    statement_only_premises: list[tuple[str, bytes]] = []
    ledger = []

    for label in TARGETS:
        statement, end = environment(data, label)
        proof = proof_after(data, end, label)
        statements.append((label, statement))
        proofs.append((label, proof))
        ledger.append((label, sha256(statement), sha256(proof), "target"))

    for label in PREMISES:
        statement, end = environment(data, label)
        proof = proof_after(data, end, label)
        premise_statements.append((label, statement))
        premise_proofs.append((label, proof))
        ledger.append((label, sha256(statement), sha256(proof), "premise"))

    for label in STATEMENT_ONLY_PREMISES:
        statement, _ = environment(data, label)
        statement_only_premises.append((label, statement))
        ledger.append((label, sha256(statement), "-", "declared-premise"))

    statement_packet = packet("statement", statements)
    proof_packet = packet("proof", proofs)
    premise_statement_packet = packet("premise statement", premise_statements)
    premise_proof_packet = packet("premise proof", premise_proofs)
    statement_only_packet = packet(
        "additional declared premise statement", statement_only_premises
    )
    (DOSSIER / "STATEMENT.tex").write_bytes(statement_packet)
    (DOSSIER / "PROOF.tex").write_bytes(proof_packet)
    (DOSSIER / "PREMISE_STATEMENT.tex").write_bytes(premise_statement_packet)
    (DOSSIER / "PREMISE_PROOF.tex").write_bytes(premise_proof_packet)
    (DOSSIER / "ADDITIONAL_PREMISE_STATEMENT.tex").write_bytes(
        statement_only_packet
    )

    lines = [
        "label\tstatement_sha256\tproof_sha256\trole",
        *("\t".join(row) for row in ledger),
        f"STATEMENT.tex\t{sha256(statement_packet)}\t-\tpacket",
        f"PROOF.tex\t-\t{sha256(proof_packet)}\tpacket",
        f"PREMISE_STATEMENT.tex\t{sha256(premise_statement_packet)}\t-\tpacket",
        f"PREMISE_PROOF.tex\t-\t{sha256(premise_proof_packet)}\tpacket",
        f"ADDITIONAL_PREMISE_STATEMENT.tex\t{sha256(statement_only_packet)}\t-\tpacket",
    ]
    (DOSSIER / "LIVE_CHUNK_HASHES.tsv").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
