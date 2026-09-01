#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def files_excluding(*names: str) -> list[Path]:
    excluded = set(names)
    return sorted(
        path for path in ROOT.rglob("*")
        if path.is_file() and path.relative_to(ROOT).as_posix() not in excluded
    )


def main() -> None:
    manifest = {
        "candidate": "ch51_npp_ledger_comprehensive_production_packet_v2_repaired_authored_20260901",
        "date": "2026-09-01",
        "status": "REPAIRED_PACKET_AUTHORED_NOT_INDEPENDENTLY_AUDITED_NOT_SUBMITTED",
        "files": {
            path.relative_to(ROOT).as_posix(): {
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            for path in files_excluding("MANIFEST.json", "SHA256SUMS")
        },
    }
    (ROOT / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    rows = []
    for path in files_excluding("SHA256SUMS"):
        rows.append(f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}\n")
    (ROOT / "SHA256SUMS").write_text("".join(rows), encoding="utf-8")


if __name__ == "__main__":
    main()
