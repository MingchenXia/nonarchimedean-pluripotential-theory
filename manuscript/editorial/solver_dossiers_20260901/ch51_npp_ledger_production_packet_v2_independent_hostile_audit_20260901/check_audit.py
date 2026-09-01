#!/usr/bin/env python3
"""Independent fail-closed audit of the repaired Chapter 51 packet.

This checker deliberately does not import the authored packet checker.  It
reimplements strict JSON parsing, LF-only addressing, PDF derivative
reproduction, route hashing, the claim partition, the immutable envelope,
and hostile-mutation gates.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable


DOSS = Path(__file__).resolve().parent
PACKET = Path(
    "/private/tmp/ch51_npp_ledger_comprehensive_production_packet_v2_repaired_authored_20260901"
)
V1_PACKET = Path(
    "/private/tmp/ch51_npp_ledger_comprehensive_production_packet_v1_20260901"
)

PACKET_TOP_SHA256 = "4b0e713319c99a2a0d2d7d157d089e974b231b4656ed57759f0039c28dfa20a5"
PACKET_MANIFEST_SHA256 = "af8f5d6763bc35ee04afc0b8e430f2d4bdba48551a9c712542058fed26a534f7"
V1_PACKET_TOP_SHA256 = "145f6305a0ea847c176e1cd55d8da46977d8c2545c873d792a6c1ba5f7a18d71"
FAILED_AUDIT_TOP_SHA256 = "173fc76c8dbe077eaa61fa60d89c1d586d2405bf01bc238bcf92f5415aff0a19"

PRESERVED = {
    "STATEMENT.tex": "9ff17ccf6ecafdaedf746e8472671bbd9436cf5661667e27815e1a1d39698575",
    "PROOF.tex": "187ef5530c9baf375cab4d15108a4447f3ddb3cc4c0b2780a7bf8d7cd2f33d70",
    "source_exact/LOCAL_CONSTRUCTION_REPLACEMENT.tex": "9ff17ccf6ecafdaedf746e8472671bbd9436cf5661667e27815e1a1d39698575",
    "source_exact/LEDGER_REPLACEMENT.tex": "187ef5530c9baf375cab4d15108a4447f3ddb3cc4c0b2780a7bf8d7cd2f33d70",
    "source_pins/BEGZ10_arXiv0812.3674v2.pdf": "43097be8459edfd948929fade34367fa7bbd0fe691d9cba1a4f27a11181214cd",
    "source_pins/BEGZ10_arXiv0812.3674v2.txt": "8bc1801705532fc32a2e8b5d0dcd8d19ec6c3b4efdeab36fc945264e0fad0a91",
    "source_pins/BT82_A_new_capacity.pdf": "e75ea91e48c14a9838a800aee25b68ed04169c4372f2ce4b399967b53005b758",
    "source_pins/BT82_A_new_capacity.txt": "247b69c13c392e1b05b3ae964059270b0dae47cecdee889648afd13ed28910d4",
    "source_pins/DDNL18mono_arXiv1705.05796.pdf": "1e614744bc4d769f377827ca81774b5f6c3d345a2619216fb6f4c81682d599cc",
    "source_pins/DDNL18mono_arXiv1705.05796.txt": "cd1cc5bacbfc6b0ec023cceaf751d22a8484cfe38ae8bac531b1f5d99a321df7",
}

SOURCE_SPECS = {
    "begz_0812_3674v2": {
        "pdf": "source_pins/BEGZ10_arXiv0812.3674v2.pdf",
        "text": "source_pins/BEGZ10_arXiv0812.3674v2.txt",
        "pdf_sha256": PRESERVED["source_pins/BEGZ10_arXiv0812.3674v2.pdf"],
        "layout_bytes": 163107,
        "layout_sha256": "890173e309165984432e7326d13b7e096662cc805fbc19045a297f12211254c7",
        "plain_bytes": 123642,
        "plain_sha256": "51410bdbf39ac3e3c36b5b3f953325a5e81cbdb424c9046d0b1d6414e1eac697",
        "text_bytes": 163108,
        "text_sha256": PRESERVED["source_pins/BEGZ10_arXiv0812.3674v2.txt"],
        "lf_lines": 2651,
        "form_feeds": 54,
        "ranges": [
            (189, 227, "daa8bbf72e713690db64c75a4e21c504a4b6bdcefc8020b7fce305a3aca59c77"),
            (243, 248, "7ff512478821be097726b97b0a3d700a0974bde3fb75008bc3f165285315193c"),
            (250, 303, "d17f5c9e7560eab7968a84ed4b63f72b5c107ef1258476a69b31b2dbae23582e"),
            (305, 323, "bd5e1b2cb18ddb7dac5d4f93d4259c18d3f3c8eb9067ff2f2d156747e7f24839"),
            (326, 352, "c46b1032a8504f95a756c57b68b3385eb39ee25480a1988045acbf6e39da84db"),
            (353, 361, "92dd143279bb5ded0f679de832d922eb39e0e05ca9c51b78e2b9d8b2b91dd09d"),
            (364, 442, "bbb8bd2308ad19b689a759fa106315e54d0b7e223893022d6c89fb3392c17244"),
            (443, 478, "3c4530b49f5a89df6d705f24fc5fd4bf514570cc599bd2d0108c014e5fdcf7f0"),
        ],
    },
    "bt82_new_capacity": {
        "pdf": "source_pins/BT82_A_new_capacity.pdf",
        "text": "source_pins/BT82_A_new_capacity.txt",
        "pdf_sha256": PRESERVED["source_pins/BT82_A_new_capacity.pdf"],
        "layout_bytes": 83498,
        "layout_sha256": "716a2e1012a35ab6811873bc9f84d981627b7d6f4d9e6e4c8d48b0b525460d8b",
        "plain_bytes": 67569,
        "plain_sha256": "b90db94a1d308e526b1b08bf20536e1ff4f79b29a012658c84379f44a591a83a",
        "text_bytes": 83499,
        "text_sha256": PRESERVED["source_pins/BT82_A_new_capacity.txt"],
        "lf_lines": 1778,
        "form_feeds": 40,
        "ranges": [
            (462, 469, "b762e65ee061731f4c9692ebff0e839a4e8eed1813de9270c100bb84ec84d86e"),
            (960, 981, "a4b3f6badc32603515e00029bb58ea07b84d9bcf02ed7665f4f95621f7589211"),
            (1104, 1118, "5acc28dccb5875f26cb311cb6e71192fcd97c9f8611959d533f5e9a05379c0c7"),
        ],
    },
    "ddnl_1705_05796": {
        "pdf": "source_pins/DDNL18mono_arXiv1705.05796.pdf",
        "text": "source_pins/DDNL18mono_arXiv1705.05796.txt",
        "pdf_sha256": PRESERVED["source_pins/DDNL18mono_arXiv1705.05796.pdf"],
        "layout_bytes": 140674,
        "layout_sha256": "c46d0c5d9ef56e4788337baef00e53bd099f130cf13913cd94b1ba19e9c5004f",
        "plain_bytes": 102612,
        "plain_sha256": "58e5cd143570f8ec0dba96d40da85a557694287c2cfd3ec877d43146f4c6a0bc",
        "text_bytes": 140675,
        "text_sha256": PRESERVED["source_pins/DDNL18mono_arXiv1705.05796.txt"],
        "lf_lines": 2308,
        "form_feeds": 38,
        "ranges": [
            (62, 65, "31ab3de37448147ca4425ad7a6c1cac669bf45606223742f80a180ccce3739ea"),
            (74, 86, "72779e779493e1058441244eec519ea0da77da66d07d91ff0affc2220d981aac"),
        ],
    },
}

ANCHORS = [
    (
        "BEGZ Definition 1.1",
        "begz_0812_3674v2",
        211,
        "99232e2fbff26979af814d36812cc717d3a4984f5044a67a325837cbf3f15954",
        b"Definition 1.1. If u1 , ..., up are psh functions",
    ),
    (
        "Bedford--Taylor Theorem 6.9",
        "bt82_new_capacity",
        1107,
        "b02be2eafba9f08a86126d222aa9a0dbc6825fdf6675ad327024d40a969258fe",
        b"    THEOREM 6.9.",
    ),
    (
        "DDNL Theorem 1.1",
        "ddnl_1705_05796",
        81,
        "421eb4e4c12b9d988185039705311bad0bc7132df9c3e22023646492a67d5c66",
        b"Theorem 1.1. Let \xce\xb8j",
    ),
]

LINE_ADDRESSING = {
    "decoder": "strict UTF-8",
    "form_feed_byte": "0x0c remains content within a line and is never a separator",
    "indexing": "one-based inclusive",
    "separator_byte": "0x0a only",
    "terminal_lf": "the required final 0x0a terminates the last addressed line and does not create an additional line",
}

EXPECTED_PARTITION = {
    "imported": [
        {
            "candidate_path": "source_exact/LEDGER_REPLACEMENT.tex",
            "candidate_range": {"start_line": 317, "end_line": 327},
            "description": "The unrestricted monotonicity of total mixed nonpluripolar masses is imported from DDNL Theorem 1.1; for p<n the packet adjoins n-p smooth Kahler entries.",
            "source_id": "ddnl_1705_05796",
            "source_ranges": [
                {"start_line": 62, "end_line": 65},
                {"start_line": 74, "end_line": 86},
            ],
        }
    ],
    "internally_supplied": [
        {
            "candidate_path": "source_exact/LOCAL_CONSTRUCTION_REPLACEMENT.tex",
            "ranges": [{"start_line": 1, "end_line": 150}],
            "scope": "local definition, admissible exhaustions, both potential-choice mass inequalities, and the common-exhaustion current",
        },
        {
            "candidate_path": "source_exact/LEDGER_REPLACEMENT.tex",
            "ranges": [
                {"start_line": 51, "end_line": 316},
                {"start_line": 328, "end_line": 420},
            ],
            "scope": "positivity, no pluripolar charge, potential independence, positive-cone multilinearity, compact-Kahler local finiteness, closedness, and the modification formula",
        },
    ],
}

CACHE_NAMES = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".cache",
    ".DS_Store",
}


class AuditError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuditError(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def strict_json(path: Path):
    def reject_duplicates(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key: {path}:{key}")
            result[key] = value
        return result

    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AuditError(f"invalid strict JSON: {path}: {exc}") from exc


def lf_rows(data: bytes, label: str) -> list[bytes]:
    """Split at byte 0x0a only; byte 0x0c is ordinary line content."""
    require(data.endswith(b"\x0a"), f"terminal LF: {label}")
    require(b"\x0d" not in data, f"CR forbidden by LF-only contract: {label}")
    rows = data[:-1].split(b"\x0a")
    require(len(rows) == data.count(b"\x0a"), f"LF row count: {label}")
    for index, row in enumerate(rows, 1):
        try:
            row.decode("utf-8", errors="strict")
        except UnicodeDecodeError as exc:
            raise AuditError(f"strict UTF-8: {label}:LF {index}") from exc
    return rows


def route_bytes(rows: list[bytes], start: int, end: int) -> bytes:
    require(1 <= start <= end <= len(rows), f"route bounds: {start}-{end}")
    return b"\x0a".join(rows[start - 1 : end]) + b"\x0a"


def parse_sha_ledger(path: Path) -> dict[str, str]:
    result = {}
    for row in lf_rows(path.read_bytes(), path.as_posix()):
        match = re.fullmatch(rb"([0-9a-f]{64})  (.+)", row)
        require(match is not None, f"malformed SHA row: {path}:{row!r}")
        relative = match.group(2).decode("utf-8", errors="strict")
        require(relative not in result, f"duplicate SHA row: {path}:{relative}")
        require(not relative.startswith("/"), f"absolute SHA path: {path}:{relative}")
        require(".." not in Path(relative).parts, f"escaping SHA path: {path}:{relative}")
        result[relative] = match.group(1).decode("ascii")
    return result


def verify_sha_directory(root: Path, top_sha256: str, require_read_only: bool = False) -> None:
    require(root.is_dir(), f"missing SHA directory: {root}")
    ledger_path = root / "SHA256SUMS"
    require(sha256(ledger_path) == top_sha256, f"top SHA mismatch: {root}")
    ledger = parse_sha_ledger(ledger_path)
    actual = {}
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        mode = path.lstat().st_mode
        require(not stat.S_ISLNK(mode), f"symlink forbidden: {root}:{relative}")
        if stat.S_ISDIR(mode):
            if require_read_only:
                require(stat.S_IMODE(mode) == 0o555, f"directory mode is not 0555: {root}:{relative}")
            continue
        require(stat.S_ISREG(mode), f"special file forbidden: {root}:{relative}")
        if require_read_only:
            require(stat.S_IMODE(mode) == 0o444, f"file mode is not 0444: {root}:{relative}")
        if relative != "SHA256SUMS":
            actual[relative] = path
    require(set(ledger) == set(actual), f"SHA inventory mismatch: {root}")
    for relative, path in actual.items():
        require(ledger[relative] == sha256(path), f"SHA content mismatch: {root}:{relative}")


def verify_no_cache(root: Path) -> None:
    for path in [root, *root.rglob("*")]:
        name = path.name
        require(name not in CACHE_NAMES, f"cache artifact forbidden: {path}")
        require(not name.endswith((".pyc", ".pyo", ".swp", ".tmp", "~")), f"cache/temp artifact forbidden: {path}")


def verify_packet_envelope(root: Path) -> None:
    verify_no_cache(root)
    verify_sha_directory(root, PACKET_TOP_SHA256, require_read_only=True)
    manifest_path = root / "MANIFEST.json"
    require(sha256(manifest_path) == PACKET_MANIFEST_SHA256, "packet manifest hash")
    manifest = strict_json(manifest_path)
    require(
        manifest.get("candidate")
        == "ch51_npp_ledger_comprehensive_production_packet_v2_repaired_authored_20260901",
        "manifest candidate",
    )
    require(
        manifest.get("status")
        == "REPAIRED_PACKET_AUTHORED_NOT_INDEPENDENTLY_AUDITED_NOT_SUBMITTED",
        "manifest status",
    )
    actual = {
        path.relative_to(root).as_posix(): path
        for path in root.rglob("*")
        if path.is_file() and path.relative_to(root).as_posix() not in {"MANIFEST.json", "SHA256SUMS"}
    }
    require(set(manifest.get("files", {})) == set(actual), "manifest inventory")
    for relative, path in actual.items():
        row = manifest["files"][relative]
        require(set(row) == {"bytes", "sha256"}, f"manifest row schema: {relative}")
        require(row["bytes"] == path.stat().st_size, f"manifest byte count: {relative}")
        require(row["sha256"] == sha256(path), f"manifest content hash: {relative}")


def verify_static_pins(root: Path) -> None:
    for relative, expected in PRESERVED.items():
        path = root / relative
        require(path.is_file(), f"missing preserved byte source: {relative}")
        require(sha256(path) == expected, f"target/source pin: {relative}")
    require(
        (root / "STATEMENT.tex").read_bytes()
        == (root / "source_exact/LOCAL_CONSTRUCTION_REPLACEMENT.tex").read_bytes(),
        "statement/source-exact byte identity",
    )
    require(
        (root / "PROOF.tex").read_bytes()
        == (root / "source_exact/LEDGER_REPLACEMENT.tex").read_bytes(),
        "proof/source-exact byte identity",
    )
    require(len(lf_rows((root / "STATEMENT.tex").read_bytes(), "STATEMENT.tex")) == 150, "statement LF line count")
    require(len(lf_rows((root / "PROOF.tex").read_bytes(), "PROOF.tex")) == 420, "proof LF line count")


def recursively_reject_line_split_metadata(value, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            lowered = key.lower()
            require(not ("runtime" in lowered and "line" in lowered), f"forbidden route metadata key: {path}.{key}")
            require("splitlines" not in lowered, f"forbidden route metadata key: {path}.{key}")
            recursively_reject_line_split_metadata(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            recursively_reject_line_split_metadata(child, f"{path}[{index}]")
    elif isinstance(value, str):
        lowered = value.lower()
        require("splitlines" not in lowered, f"forbidden route metadata value: {path}")
        require("runtime line" not in lowered, f"forbidden route metadata value: {path}")
        require("runtime-line" not in lowered, f"forbidden route metadata value: {path}")


def expected_external_rows(spec: dict) -> list[dict]:
    return [
        {"start_line": start, "end_line": end, "route_sha256": digest}
        for start, end, digest in spec["ranges"]
    ]


def verify_route_contract(root: Path) -> dict:
    routes = strict_json(root / "SOURCE_ROUTES.json")
    recursively_reject_line_split_metadata(routes)
    require(routes.get("format") == "ch51-npp-ledger-source-routes-v2", "route format")
    require(routes.get("target_order") == ["STATEMENT.tex", "PROOF.tex"], "target order")
    require(routes.get("line_addressing") == LINE_ADDRESSING, "line-addressing contract")
    require(
        routes.get("line_numbering")
        == "one-based LF-only inclusive ranges; only byte 0x0a separates lines and byte 0x0c remains within a line",
        "line-numbering contract",
    )
    candidate_expected = [
        {
            "line_ranges": [{"start_line": 1, "end_line": 150}],
            "packet_path": "source_exact/LOCAL_CONSTRUCTION_REPLACEMENT.tex",
            "role": "exact local setup and internally supplied construction",
            "runtime_source_id": "ch51_npp_ledger_v2_local",
            "sha256": PRESERVED["STATEMENT.tex"],
            "target_path": "STATEMENT.tex",
        },
        {
            "line_ranges": [{"start_line": 1, "end_line": 420}],
            "packet_path": "source_exact/LEDGER_REPLACEMENT.tex",
            "role": "exact theorem statement and proof",
            "runtime_source_id": "ch51_npp_ledger_v2_ledger",
            "sha256": PRESERVED["PROOF.tex"],
            "target_path": "PROOF.tex",
        },
    ]
    require(routes.get("candidate_routes") == candidate_expected, "candidate route table")

    external = routes.get("external_routes")
    require(isinstance(external, list) and len(external) == 3, "external route count")
    by_id = {item.get("source_id"): item for item in external}
    require(len(by_id) == 3 and set(by_id) == set(SOURCE_SPECS), "external source ids")
    for source_id, spec in SOURCE_SPECS.items():
        item = by_id[source_id]
        require(item.get("extraction") == "pdftotext -layout", f"extraction mode: {source_id}")
        require(
            item.get("normalization")
            == "append one LF byte after the terminal form-feed; all routed line contents and one-based line numbers are unchanged",
            f"normalization declaration: {source_id}",
        )
        require(item.get("pdf_path") == spec["pdf"], f"PDF path: {source_id}")
        require(item.get("text_path") == spec["text"], f"text path: {source_id}")
        require(item.get("pdf_sha256") == spec["pdf_sha256"], f"PDF metadata hash: {source_id}")
        require(item.get("pre_normalization_text_sha256") == spec["layout_sha256"], f"raw derivative metadata hash: {source_id}")
        require(item.get("text_sha256") == spec["text_sha256"], f"normalized text metadata hash: {source_id}")
        require(item.get("ranges") == expected_external_rows(spec), f"external range table: {source_id}")

    require(routes.get("claim_partition") == EXPECTED_PARTITION, "claim partition")
    imported = set(range(317, 328))
    supplied = set(range(51, 317)) | set(range(328, 421))
    require(not imported & supplied, "claim partition disjointness")
    require(imported | supplied == set(range(51, 421)), "claim partition proof coverage")
    return routes


def run_pdftotext(pdf: Path, layout: bool) -> bytes:
    executable = shutil.which("pdftotext")
    require(executable is not None, "pdftotext executable missing")
    command = [executable]
    if layout:
        command.append("-layout")
    command.extend([str(pdf), "-"])
    completed = subprocess.run(
        command,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=120,
    )
    require(completed.returncode == 0, f"pdftotext failed: {pdf}:layout={layout}")
    return completed.stdout


def verify_anchors_only(root: Path) -> None:
    for label, source_id, line_number, expected_hash, prefix in ANCHORS:
        spec = SOURCE_SPECS[source_id]
        rows = lf_rows((root / spec["text"]).read_bytes(), spec["text"])
        require(line_number <= len(rows), f"anchor bounds: {label}")
        line = rows[line_number - 1]
        require(sha256_bytes(line + b"\x0a") == expected_hash, f"anchor bytes: {label}")
        require(line.startswith(prefix), f"anchor readable content: {label}")


def verify_external_sources(root: Path, routes: dict) -> None:
    route_by_id = {item["source_id"]: item for item in routes["external_routes"]}
    range_count = 0
    source_rows = {}
    for source_id, spec in SOURCE_SPECS.items():
        pdf = root / spec["pdf"]
        text = root / spec["text"]
        require(sha256(pdf) == spec["pdf_sha256"], f"PDF pin: {source_id}")
        require(sha256(text) == spec["text_sha256"], f"normalized text pin: {source_id}")
        require(text.stat().st_size == spec["text_bytes"], f"normalized text bytes: {source_id}")

        layout = run_pdftotext(pdf, layout=True)
        require(len(layout) == spec["layout_bytes"], f"layout derivative bytes: {source_id}")
        require(sha256_bytes(layout) == spec["layout_sha256"], f"layout derivative hash: {source_id}")
        require(layout.endswith(b"\x0c"), f"layout terminal form-feed: {source_id}")
        require(not layout.endswith(b"\x0a"), f"layout unexpectedly has terminal LF: {source_id}")
        require(text.read_bytes() == layout + b"\x0a", f"exact raw-plus-one-LF normalization: {source_id}")
        require(text.read_bytes().endswith(b"\x0c\x0a"), f"normalized form-feed/LF suffix: {source_id}")
        require(not text.read_bytes().endswith(b"\x0c\x0a\x0a"), f"more than one appended LF: {source_id}")

        plain = run_pdftotext(pdf, layout=False)
        require(len(plain) == spec["plain_bytes"], f"plain derivative bytes: {source_id}")
        require(sha256_bytes(plain) == spec["plain_sha256"], f"plain derivative hash: {source_id}")
        require(plain != layout, f"plain/layout extraction unexpectedly identical: {source_id}")

        rows = lf_rows(text.read_bytes(), spec["text"])
        source_rows[source_id] = rows
        require(len(rows) == spec["lf_lines"], f"LF-only line count: {source_id}")
        require(sum(row.count(b"\x0c") for row in rows) == spec["form_feeds"], f"form-feed retention: {source_id}")
        require(rows[-1] == b"\x0c", f"terminal form-feed remains line content: {source_id}")
        for start, end, expected_hash in spec["ranges"]:
            actual = sha256_bytes(route_bytes(rows, start, end))
            require(actual == expected_hash, f"route content hash: {source_id}:{start}-{end}")
            range_count += 1
    require(range_count == 13, "all thirteen routed range hashes")

    metadata = routes["external_anchor_checks"]
    expected_metadata = [
        {
            "label": label,
            "source_id": source_id,
            "lf_line": line_number,
            "line_sha256_including_terminal_lf": expected_hash,
        }
        for label, source_id, line_number, expected_hash, _ in ANCHORS
    ]
    require(metadata == expected_metadata, "anchor metadata table")
    verify_anchors_only(root)
    for label, source_id, line_number, _, _ in ANCHORS:
        containing = [
            (start, end)
            for start, end, _ in SOURCE_SPECS[source_id]["ranges"]
            if start <= line_number <= end
        ]
        require(len(containing) == 1, f"anchor contracted exactly once: {label}")


def verify_ddnl_partition_semantics(root: Path) -> None:
    proof_rows = lf_rows((root / "PROOF.tex").read_bytes(), "PROOF.tex")
    imported = b"\x0a".join(proof_rows[316:327]).decode("utf-8", errors="strict")
    require("it is exactly" in imported, "DDNL import exactness wording")
    require("\\cite[Theorem~1.1]{DDNL18mono}" in imported, "DDNL theorem citation")
    require("less singular" not in imported, "DDNL orientation is routed to source, not silently restated")
    require("When \\(p<n\\)" in imported, "DDNL p<n specialization")
    require("adjoining \\(n-p\\) copies" in imported, "DDNL smooth-entry specialization")
    require("zero potential" in imported, "DDNL smooth-entry singularity orientation")

    ddnl_rows = lf_rows(
        (root / SOURCE_SPECS["ddnl_1705_05796"]["text"]).read_bytes(),
        "DDNL text",
    )
    orientation = route_bytes(ddnl_rows, 62, 65).decode("utf-8", errors="strict")
    theorem = route_bytes(ddnl_rows, 74, 86).decode("utf-8", errors="strict")
    require("u is said to be less singular than v" in orientation, "DDNL less-singular definition")
    require("v \xe2\x89\xa4 u + C" not in orientation, "impossible byte-escaped orientation sentinel")
    require("v \u2264 u + C" in orientation, "DDNL less-singular orientation")
    require("uj is less singular than vj" in theorem, "DDNL theorem hypothesis orientation")
    require("Theorem 1.1." in theorem, "DDNL theorem anchor content")
    require("\u2265" in theorem, "DDNL mass inequality direction")

    statement_rows = lf_rows((root / "STATEMENT.tex").read_bytes(), "STATEMENT.tex")
    require(len(statement_rows) == 150, "internal local block coverage")
    internal_proof = list(range(51, 317)) + list(range(328, 421))
    require(len(internal_proof) == 359, "internal proof range cardinality")
    require(set(internal_proof).isdisjoint(set(range(317, 328))), "internal/imported ranges disjoint")
    require(set(internal_proof) | set(range(317, 328)) == set(range(51, 421)), "proof-body partition complete")
    require("\\begin{theorem}" in b"\x0a".join(proof_rows[:50]).decode("utf-8"), "unpartitioned lines 1--50 are theorem statement")


def verify_failure_provenance(root: Path) -> None:
    nested = root / "audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901"
    verify_sha_directory(nested, FAILED_AUDIT_TOP_SHA256, require_read_only=True)
    result = strict_json(nested / "AUDIT_RESULT.json")
    require(result.get("verdict") == "FAIL_REPAIR_REQUIRED", "prior FAIL verdict")
    require(result.get("mathematical_target_rejected") is False, "prior audit preserved mathematical target")
    require(result.get("production_submission_authorized") is False, "prior audit submission firewall")
    require(result.get("ready_for_final_path_installation") is False, "prior audit installation firewall")
    require(result.get("ready_for_final_path_smoke") is False, "prior audit smoke firewall")
    blocker_ids = [item.get("id") for item in result.get("blockers", [])]
    require(
        blocker_ids
        == [
            "SOURCE_EXTRACTION_MODE_MISDECLARED",
            "LF_ROUTE_AND_RUNTIME_LINE_NUMBERING_DIVERGE",
            "KNOWN_FAILED_FINAL_PATH_SMOKE_RUNNER_REUSED",
        ],
        "prior FAIL blocker ledger",
    )
    evidence = strict_json(nested / "EVIDENCE.json")
    require(
        evidence["fixed_source_routes"]["begz_0812_3674v2"]["layout_raw_sha256"]
        == SOURCE_SPECS["begz_0812_3674v2"]["layout_sha256"],
        "prior BEGZ extraction evidence",
    )
    require(
        evidence["fixed_source_routes"]["bt82_new_capacity"]["plain_raw_sha256"]
        == SOURCE_SPECS["bt82_new_capacity"]["plain_sha256"],
        "prior BT extraction evidence",
    )
    require(evidence["known_failed_runner"]["runner_sha256"] == "5a8f25b6851667d284d84bd8874fdfcdeb640f51380727a95a72eb9991b10c78", "prior failed runner")

    repair = strict_json(root / "REPAIR_LEDGER.json")
    require(repair["provenance"]["frozen_v1_packet_sha256sums_sha256"] == V1_PACKET_TOP_SHA256, "v1 top provenance")
    require(repair["provenance"]["frozen_failed_audit_sha256sums_sha256"] == FAILED_AUDIT_TOP_SHA256, "prior FAIL top provenance")
    require([item["blocker"] for item in repair["repairs"]] == ["SOURCE_EXTRACTION_MODE_MISDECLARED", "LF_ROUTE_AND_RUNTIME_LINE_NUMBERING_DIVERGE"], "packet repair ledger")
    require(repair["runtime_scope"].startswith("No runtime stage is bundled"), "runtime remains separate")

    request = strict_json(root / "PRODUCTION_REQUEST.json")
    require(request["execution_status"] == "PREPARED_NOT_SUBMITTED", "production not submitted")
    require(request["submission_performed"] is False, "submission firewall")
    require(request["release_stage"] is None, "no runtime stage attached")
    require(request["release_stage_status"] == "SEPARATE_REPAIRED_STAGE_REQUIRED_AND_NOT_YET_AUDITED", "separate runtime repair gate")


def verify_v1_preservation_if_available(root: Path) -> None:
    if not V1_PACKET.is_dir():
        return
    require(sha256(V1_PACKET / "SHA256SUMS") == V1_PACKET_TOP_SHA256, "v1 top SHA at audit time")
    for relative, expected in PRESERVED.items():
        v1 = V1_PACKET / relative
        current = root / relative
        require(v1.is_file(), f"v1 preserved file missing: {relative}")
        require(sha256(v1) == expected, f"v1 preserved hash: {relative}")
        require(v1.read_bytes() == current.read_bytes(), f"v1/v2 byte identity: {relative}")


def verify_packet_semantics(root: Path, reproduce_pdfs: bool = True) -> None:
    verify_static_pins(root)
    routes = verify_route_contract(root)
    if reproduce_pdfs:
        verify_external_sources(root, routes)
    else:
        verify_anchors_only(root)
    verify_ddnl_partition_semantics(root)
    verify_failure_provenance(root)


def make_writable(root: Path) -> None:
    for path in sorted(root.rglob("*"), key=lambda item: len(item.parts)):
        if path.is_dir():
            os.chmod(path, 0o755)
        elif path.is_file():
            os.chmod(path, 0o644)
    os.chmod(root, 0o755)


def rewrite_json(path: Path, mutator: Callable[[dict], None]) -> None:
    payload = strict_json(path)
    mutator(payload)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def expected_rejection(action: Callable[[], None], marker: str) -> str:
    try:
        action()
    except AuditError as exc:
        message = str(exc)
        require(marker in message, f"hostile case rejected at wrong gate: expected {marker!r}, got {message!r}")
        return message
    raise AuditError(f"hostile mutation unexpectedly accepted; expected gate {marker}")


def authored_checker_rejects(root: Path) -> bool:
    completed = subprocess.run(
        [sys.executable, "-B", "check_packet.py"],
        cwd=root,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=180,
    )
    return completed.returncode != 0


def run_hostile_suite() -> dict:
    cases = {}

    def run_case(name: str, mutate: Callable[[Path], None], gate: Callable[[Path], None], marker: str) -> None:
        with tempfile.TemporaryDirectory(prefix=f"ch51_v2_hostile_{name}_", dir="/private/tmp") as temporary:
            copy = Path(temporary) / "packet"
            shutil.copytree(PACKET, copy, symlinks=True)
            make_writable(copy)
            mutate(copy)
            message = expected_rejection(lambda: gate(copy), marker)
            require(authored_checker_rejects(copy), f"authored checker accepted hostile case: {name}")
            cases[name] = {
                "authored_checker_rejected": True,
                "independent_gate": marker,
                "independent_rejected": True,
                "observed_failure": message,
            }

    run_case(
        "extraction_mode",
        lambda root: rewrite_json(root / "SOURCE_ROUTES.json", lambda data: data["external_routes"][0].__setitem__("extraction", "pdftotext")),
        lambda root: verify_route_contract(root),
        "extraction mode",
    )
    run_case(
        "line_semantics",
        lambda root: rewrite_json(root / "SOURCE_ROUTES.json", lambda data: data["line_addressing"].__setitem__("separator_byte", "0x0c only")),
        lambda root: verify_route_contract(root),
        "line-addressing contract",
    )
    run_case(
        "forbidden_runtime_number_metadata",
        lambda root: rewrite_json(root / "SOURCE_ROUTES.json", lambda data: data.__setitem__("runtime_line_numbering", "one-based str.splitlines()")),
        lambda root: verify_route_contract(root),
        "forbidden route metadata",
    )
    run_case(
        "range_hash",
        lambda root: rewrite_json(root / "SOURCE_ROUTES.json", lambda data: data["external_routes"][0]["ranges"][0].__setitem__("route_sha256", "0" * 64)),
        lambda root: verify_route_contract(root),
        "external range table",
    )

    def mutate_anchor(root: Path) -> None:
        path = root / SOURCE_SPECS["begz_0812_3674v2"]["text"]
        data = path.read_bytes()
        rows = lf_rows(data, "anchor mutation source")
        require(rows[210].startswith(b"Definition 1.1."), "anchor mutation precondition")
        rows[210] = b"X" + rows[210][1:]
        path.write_bytes(b"\x0a".join(rows) + b"\x0a")

    run_case(
        "anchor_content",
        mutate_anchor,
        lambda root: verify_anchors_only(root),
        "anchor bytes",
    )

    def mutate_target(root: Path) -> None:
        path = root / "STATEMENT.tex"
        data = path.read_bytes()
        require(data, "target mutation precondition")
        path.write_bytes((b"X" if data[:1] != b"X" else b"Y") + data[1:])

    run_case(
        "target_hash",
        mutate_target,
        lambda root: verify_static_pins(root),
        "target/source pin",
    )
    run_case(
        "claim_partition",
        lambda root: rewrite_json(root / "SOURCE_ROUTES.json", lambda data: data["claim_partition"]["imported"][0]["candidate_range"].__setitem__("start_line", 316)),
        lambda root: verify_route_contract(root),
        "claim partition",
    )
    require(set(cases) == {
        "extraction_mode",
        "line_semantics",
        "forbidden_runtime_number_metadata",
        "range_hash",
        "anchor_content",
        "target_hash",
        "claim_partition",
    }, "hostile case inventory")
    return cases


def verify_dossier() -> None:
    verify_no_cache(DOSS)
    ledger_path = DOSS / "SHA256SUMS"
    require(ledger_path.is_file(), "audit SHA256SUMS missing")
    ledger = parse_sha_ledger(ledger_path)
    actual = {
        path.relative_to(DOSS).as_posix(): path
        for path in DOSS.rglob("*")
        if path.is_file() and path.relative_to(DOSS).as_posix() != "SHA256SUMS"
    }
    require(set(ledger) == set(actual), "audit SHA inventory")
    for relative, path in actual.items():
        require(ledger[relative] == sha256(path), f"audit SHA content: {relative}")

    result = strict_json(DOSS / "AUDIT_RESULT.json")
    require(
        result["verdict"]
        == "PASS_PACKET_READY_FOR_ATTACHMENT_TO_SEPARATELY_AUDITED_FINAL_PATH_RELEASE",
        "binary PASS verdict",
    )
    require(result["blockers"] == [], "audit blocker list")
    require(result["production_submission_performed"] is False, "audit submission firewall")
    require(result["runtime_audited"] is False, "audit runtime boundary")
    require(result["packet_sha256sums_sha256"] == PACKET_TOP_SHA256, "audit packet top binding")
    require(result["packet_manifest_sha256"] == PACKET_MANIFEST_SHA256, "audit manifest binding")
    require(result["external_range_hashes_verified"] == 13, "audit range count")
    require(result["hostile_mutations_rejected"] == 7, "audit hostile count")

    evidence = strict_json(DOSS / "EVIDENCE.json")
    require(evidence["packet_envelope"]["sha256sums_sha256"] == PACKET_TOP_SHA256, "evidence top binding")
    require(evidence["packet_envelope"]["manifest_sha256"] == PACKET_MANIFEST_SHA256, "evidence manifest binding")
    require(evidence["v1_preservation"]["v1_sha256sums_sha256"] == V1_PACKET_TOP_SHA256, "evidence v1 binding")
    require(evidence["route_verification"]["range_count"] == 13, "evidence route count")
    require(evidence["route_verification"]["line_splitter"] == "0x0a-only over bytes; terminal LF removed before splitting; 0x0c retained as content", "evidence LF splitter")

    recorded = strict_json(DOSS / "HOSTILE_MUTATION_RESULTS.json")
    fresh = run_hostile_suite()
    require(recorded == fresh, "hostile-mutation rerun result")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--semantic-only", type=Path)
    parser.add_argument("--hostile-json", action="store_true")
    arguments = parser.parse_args()
    if arguments.semantic_only is not None:
        verify_packet_semantics(arguments.semantic_only, reproduce_pdfs=True)
        print("PASS_CH51_PACKET_V2_INDEPENDENT_SEMANTIC_CHECK")
        return
    if arguments.hostile_json:
        print(json.dumps(run_hostile_suite(), indent=2, sort_keys=True))
        return

    verify_packet_envelope(PACKET)
    verify_packet_semantics(PACKET, reproduce_pdfs=True)
    verify_v1_preservation_if_available(PACKET)
    verify_dossier()
    print("PASS_INDEPENDENT_CH51_PACKET_V2_HOSTILE_AUDIT")


if __name__ == "__main__":
    main()
