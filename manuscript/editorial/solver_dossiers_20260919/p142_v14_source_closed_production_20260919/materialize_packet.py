#!/usr/bin/env python3
"""Materialize the exact P14.2 V14 target and its cited source extracts."""

from __future__ import annotations

import hashlib
from pathlib import Path
import shutil


REPO_ROOT = Path(__file__).resolve().parents[4]
DOSSIER = Path(__file__).resolve().parent
V14 = (
    REPO_ROOT
    / "manuscript/editorial/solver_dossiers_20260911"
    / "p142_v14_preproduction_gate_20260911"
)
SOURCES = (
    REPO_ROOT
    / "manuscript/editorial/solver_dossiers_20260901"
    / "p142_source_closed_production_release_repaired_authored_stage_dossier_v2_20260901"
    / "release_stage/runtime/sources"
)

TARGET_HASHES = {
    "STATEMENT.tex": "cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2",
    "PROOF.tex": "7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac",
    "EXAMPLE.tex": "7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f",
}

SOURCE_HASHES = {
    "mp_2409.06221v2.txt": "724926d161cb3744dd5037e259f098a944a072419176bdc3e02538a657e5c59d",
    "dxz_2302.02541v3.txt": "3234b3366d4aa4e235c5d2581cb131c68b95cdb0b386622302b4707930ea57f9",
    "darvas_xia_2003.04818.txt": "794c9e34736334b6ba2ff01a257a916b619e9036cb02e2a2e160c494e6c358ed",
    "demailly_ein_lazarsfeld_math0002035.txt": "0ae95d36227cc357a45b42336fdc1c28588be7163d25e160ba9e5a47bf8e81a3",
    "xia_2312.17150v3.txt": "a39c27332e746fa7f711718542658b1a0cfc526b8922f6f220e159089ac9562d",
}

EXTRACTS = (
    ("MP24 Definition 1.3.1", "mp_2409.06221v2.txt", 413, 423),
    ("DXZ23 relative test curves", "dxz_2302.02541v3.txt", 437, 458),
    ("DXZ23 transition formula and Definition 3.3", "dxz_2302.02541v3.txt", 848, 880),
    ("DXZ23 projective-limit compatibility", "dxz_2302.02541v3.txt", 873, 925),
    ("DX22 I-equivalence and Proposition 2.18", "darvas_xia_2003.04818.txt", 1055, 1185),
    ("DEL00 Theorem 2.6", "demailly_ein_lazarsfeld_math0002035.txt", 596, 613),
    ("Xia23 ideal-valuative formula", "xia_2312.17150v3.txt", 628, 647),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_hash(path: Path, expected: str) -> None:
    actual = digest(path)
    if actual != expected:
        raise SystemExit(f"hash mismatch for {path}: {actual} != {expected}")


def main() -> None:
    for name, expected in TARGET_HASHES.items():
        source = V14 / "target" / name
        require_hash(source, expected)
        shutil.copyfile(source, DOSSIER / name)

    source_lines: dict[str, list[bytes]] = {}
    for name, expected in SOURCE_HASHES.items():
        source = SOURCES / name
        require_hash(source, expected)
        source_lines[name] = source.read_bytes().splitlines(keepends=True)

    output = bytearray()
    output.extend(b"P14.2 V14 SOURCE EXTRACTS\n")
    output.extend(
        b"These are the exact cited physical-line ranges from full source files "
        b"whose SHA-256 values match the V14 release manifest.\n"
    )
    for label, name, first, last in EXTRACTS:
        output.extend(b"\nBEGIN SOURCE EXTRACT\n")
        output.extend(f"label: {label}\n".encode("utf-8"))
        output.extend(f"file: {name}\n".encode("utf-8"))
        output.extend(f"full-source-sha256: {SOURCE_HASHES[name]}\n".encode("ascii"))
        output.extend(f"physical-lines: {first}-{last}\n".encode("ascii"))
        output.extend(b"BEGIN EXACT SOURCE BYTES\n")
        output.extend(b"".join(source_lines[name][first - 1 : last]))
        if output[-1:] != b"\n":
            output.extend(b"\n")
        output.extend(b"END EXACT SOURCE BYTES\n")
        output.extend(b"END SOURCE EXTRACT\n")
    (DOSSIER / "SOURCE_EXTRACTS.txt").write_bytes(output)


if __name__ == "__main__":
    main()
