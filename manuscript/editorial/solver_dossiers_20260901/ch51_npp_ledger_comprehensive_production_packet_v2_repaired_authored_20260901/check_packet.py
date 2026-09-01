#!/usr/bin/env python3
"""Read-only, fail-closed check of the repaired exact source-closed packet."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import stat
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent

PINS = {
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
    "audit/CANDIDATE_SHA256SUMS": "ffddd14e1d8b195fe1ec01ce3ee26b4c6ec2947865bc999c15e88da23c1535a2",
    "audit/CANDIDATE_SOURCE_AUDIT.md": "8678e2cc2104863f2297ee2918bbff5a13a66414e20d883bc647cf396db22788",
    "audit/INDEPENDENT_AUDIT.md": "03dcce4596c3ceb3a8ed25a7ad755cde2c7feea1fa38a30f116bacd4447b54ef",
    "audit/INDEPENDENT_AUDIT_RESULT.json": "0e10ec20f585cbcb4158db8415620e75fd8fec0b3d30de1a3cccef67d3be73e6",
    "audit/INDEPENDENT_AUDIT_SHA256SUMS": "41c3f87708b36083dcceeab4a1b0e898fcbaaa1ff072e4ede608edde25a36f52",
    "audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901/SHA256SUMS": "173fc76c8dbe077eaa61fa60d89c1d586d2405bf01bc238bcf92f5415aff0a19",
}

EXPECTED_EXTERNAL_RANGES = {
    "begz_0812_3674v2": [
        (189, 227, "daa8bbf72e713690db64c75a4e21c504a4b6bdcefc8020b7fce305a3aca59c77"),
        (243, 248, "7ff512478821be097726b97b0a3d700a0974bde3fb75008bc3f165285315193c"),
        (250, 303, "d17f5c9e7560eab7968a84ed4b63f72b5c107ef1258476a69b31b2dbae23582e"),
        (305, 323, "bd5e1b2cb18ddb7dac5d4f93d4259c18d3f3c8eb9067ff2f2d156747e7f24839"),
        (326, 352, "c46b1032a8504f95a756c57b68b3385eb39ee25480a1988045acbf6e39da84db"),
        (353, 361, "92dd143279bb5ded0f679de832d922eb39e0e05ca9c51b78e2b9d8b2b91dd09d"),
        (364, 442, "bbb8bd2308ad19b689a759fa106315e54d0b7e223893022d6c89fb3392c17244"),
        (443, 478, "3c4530b49f5a89df6d705f24fc5fd4bf514570cc599bd2d0108c014e5fdcf7f0"),
    ],
    "bt82_new_capacity": [
        (462, 469, "b762e65ee061731f4c9692ebff0e839a4e8eed1813de9270c100bb84ec84d86e"),
        (960, 981, "a4b3f6badc32603515e00029bb58ea07b84d9bcf02ed7665f4f95621f7589211"),
        (1104, 1118, "5acc28dccb5875f26cb311cb6e71192fcd97c9f8611959d533f5e9a05379c0c7"),
    ],
    "ddnl_1705_05796": [
        (62, 65, "31ab3de37448147ca4425ad7a6c1cac669bf45606223742f80a180ccce3739ea"),
        (74, 86, "72779e779493e1058441244eec519ea0da77da66d07d91ff0affc2220d981aac"),
    ],
}

EXPECTED_ANCHORS = [
    {
        "label": "BEGZ Definition 1.1",
        "source_id": "begz_0812_3674v2",
        "lf_line": 211,
        "line_sha256_including_terminal_lf": "99232e2fbff26979af814d36812cc717d3a4984f5044a67a325837cbf3f15954",
        "prefix": "Definition 1.1. If u1 , ..., up are psh functions",
    },
    {
        "label": "Bedford--Taylor Theorem 6.9",
        "source_id": "bt82_new_capacity",
        "lf_line": 1107,
        "line_sha256_including_terminal_lf": "b02be2eafba9f08a86126d222aa9a0dbc6825fdf6675ad327024d40a969258fe",
        "prefix": "    THEOREM 6.9.",
    },
    {
        "label": "DDNL Theorem 1.1",
        "source_id": "ddnl_1705_05796",
        "lf_line": 81,
        "line_sha256_including_terminal_lf": "421eb4e4c12b9d988185039705311bad0bc7132df9c3e22023646492a67d5c66",
        "prefix": "Theorem 1.1. Let θj",
    },
]

EXPECTED_LINE_ADDRESSING = {
    "decoder": "strict UTF-8",
    "form_feed_byte": "0x0c remains content within a line and is never a separator",
    "indexing": "one-based inclusive",
    "separator_byte": "0x0a only",
    "terminal_lf": "the required final 0x0a terminates the last addressed line and does not create an additional line",
}

REPORTED_FILES = {
    "PRODUCTION_REQUEST.json",
    "PROOF.tex",
    "README.md",
    "REPAIR_LEDGER.json",
    "REQUEST_CONTRACT.md",
    "SOURCE_ROUTES.json",
    "STATEMENT.tex",
    "audit/INDEPENDENT_AUDIT.md",
    "audit/INDEPENDENT_AUDIT_RESULT.json",
    "audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901/SHA256SUMS",
    "check_packet.py",
    "source_exact/LEDGER_REPLACEMENT.tex",
    "source_exact/LOCAL_CONSTRUCTION_REPLACEMENT.tex",
    "tests/test_packet.py",
}


def require(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def strict_json(path: Path):
    def reject(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key in {path}: {key}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject)


def lf_only_lines_bytes(path: Path) -> list[bytes]:
    """Address lines using only byte 0x0a; byte 0x0c remains ordinary content."""
    data = path.read_bytes()
    require(data.endswith(b"\x0a"), f"missing terminal LF: {path}")
    require(b"\x0d" not in data, f"CR byte in LF-only source: {path}")
    body = data[:-1]
    result = body.split(b"\x0a")
    for number, raw in enumerate(result, 1):
        try:
            raw.decode("utf-8", errors="strict")
        except UnicodeDecodeError as exc:
            raise RuntimeError(f"invalid UTF-8 at LF line {number}: {path}") from exc
    return result


def lf_only_lines(path: Path) -> list[str]:
    return [raw.decode("utf-8", errors="strict") for raw in lf_only_lines_bytes(path)]


def routed_bytes(rows: list[bytes], start: int, end: int) -> bytes:
    require(1 <= start <= end <= len(rows), f"invalid LF route {start}-{end}")
    return b"\x0a".join(rows[start - 1:end]) + b"\x0a"


def reproduce_layout_derivative(pdf_path: Path) -> bytes:
    executable = shutil.which("pdftotext")
    require(executable is not None, "pdftotext executable is required")
    completed = subprocess.run(
        [executable, "-layout", str(pdf_path), "-"],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=120,
    )
    require(
        completed.returncode == 0,
        f"pdftotext -layout failed for {pdf_path}: {completed.stderr.decode('utf-8', errors='replace')}",
    )
    return completed.stdout


def check_nested_sha_ledger(directory: Path, expected_top_sha256: str) -> None:
    ledger_path = directory / "SHA256SUMS"
    require(sha256(ledger_path) == expected_top_sha256, f"nested top SHA: {directory}")
    ledger = {}
    for raw in lf_only_lines_bytes(ledger_path):
        match = re.fullmatch(rb"([0-9a-f]{64})  (.+)", raw)
        require(match is not None, f"malformed nested SHA row: {raw!r}")
        digest = match.group(1).decode("ascii")
        relative = match.group(2).decode("utf-8", errors="strict")
        require(relative not in ledger, f"duplicate nested SHA row: {relative}")
        ledger[relative] = digest
    actual = {
        path.relative_to(directory).as_posix(): path
        for path in directory.rglob("*")
        if path.is_file() and path.relative_to(directory).as_posix() != "SHA256SUMS"
    }
    require(set(ledger) == set(actual), f"nested SHA inventory: {directory}")
    for relative, path in actual.items():
        require(ledger[relative] == sha256(path), f"nested SHA mismatch: {relative}")


def check_routes() -> None:
    route_path = ROOT / "SOURCE_ROUTES.json"
    routes = strict_json(route_path)
    route_blob_lower = route_path.read_bytes().lower()
    require(b"splitlines" not in route_blob_lower, "form-feed-aware line semantics forbidden")
    require(b"runtime_line" not in route_blob_lower, "runtime/LF line-number split-brain forbidden")
    require(routes["format"] == "ch51-npp-ledger-source-routes-v2", "route format")
    require(routes["target_order"] == ["STATEMENT.tex", "PROOF.tex"], "target order")
    require(routes["line_addressing"] == EXPECTED_LINE_ADDRESSING, "LF-only addressing contract")
    require(
        routes["line_numbering"]
        == "one-based LF-only inclusive ranges; only byte 0x0a separates lines and byte 0x0c remains within a line",
        "single-valued LF line-numbering declaration",
    )

    candidate = routes["candidate_routes"]
    require(len(candidate) == 2, "candidate route count")
    for item in candidate:
        target = ROOT / item["target_path"]
        exact = ROOT / item["packet_path"]
        require(target.read_bytes() == exact.read_bytes(), f"target/exact mismatch: {target}")
        require(sha256(target) == item["sha256"], f"candidate route hash: {target}")

    external = {item["source_id"]: item for item in routes["external_routes"]}
    require(set(external) == set(EXPECTED_EXTERNAL_RANGES), "external route ids")
    source_lines = {}
    for source_id, expected in EXPECTED_EXTERNAL_RANGES.items():
        item = external[source_id]
        require(item["extraction"] == "pdftotext -layout", f"extraction mode: {source_id}")
        require(
            item["normalization"]
            == "append one LF byte after the terminal form-feed; all routed line contents and one-based line numbers are unchanged",
            f"text normalization contract: {source_id}",
        )
        actual = [
            (row["start_line"], row["end_line"], row["route_sha256"])
            for row in item["ranges"]
        ]
        require(actual == expected, f"exact LF line routes: {source_id}")
        for row in item["ranges"]:
            require(
                set(row) == {"start_line", "end_line", "route_sha256"},
                f"unexpected route metadata: {source_id}",
            )

        text_path = ROOT / item["text_path"]
        pdf_path = ROOT / item["pdf_path"]
        require(sha256(text_path) == item["text_sha256"], f"text route hash: {source_id}")
        require(sha256(pdf_path) == item["pdf_sha256"], f"PDF route hash: {source_id}")
        raw = reproduce_layout_derivative(pdf_path)
        require(raw.endswith(b"\x0c"), f"raw derivative terminal form-feed: {source_id}")
        require(not raw.endswith(b"\x0a"), f"unexpected raw terminal LF: {source_id}")
        require(
            sha256_bytes(raw) == item["pre_normalization_text_sha256"],
            f"reproduced raw derivative hash: {source_id}",
        )
        require(text_path.read_bytes() == raw + b"\x0a", f"raw-plus-one-LF normalization: {source_id}")

        rows = lf_only_lines_bytes(text_path)
        source_lines[source_id] = rows
        for start, end, expected_hash in expected:
            exact = routed_bytes(rows, start, end)
            require(sha256_bytes(exact) == expected_hash, f"exact route content: {source_id}:{start}-{end}")

    metadata_anchors = []
    for item in routes["external_anchor_checks"]:
        require(set(item) == {"label", "lf_line", "line_sha256_including_terminal_lf", "source_id"},
                f"anchor metadata fields: {item.get('label')}")
        metadata_anchors.append(item)
    expected_metadata = [{key: value for key, value in item.items() if key != "prefix"}
                         for item in EXPECTED_ANCHORS]
    require(metadata_anchors == expected_metadata, "exact anchor metadata")

    for anchor in EXPECTED_ANCHORS:
        source_id = anchor["source_id"]
        line_number = anchor["lf_line"]
        line = source_lines[source_id][line_number - 1]
        require(
            sha256_bytes(line + b"\x0a") == anchor["line_sha256_including_terminal_lf"],
            f"exact anchor-line bytes: {anchor['label']}",
        )
        require(
            line.decode("utf-8", errors="strict").startswith(anchor["prefix"]),
            f"readable anchor prefix: {anchor['label']}",
        )
        containing = [
            (start, end) for start, end, _ in EXPECTED_EXTERNAL_RANGES[source_id]
            if start <= line_number <= end
        ]
        require(len(containing) == 1, f"anchor in exactly one contracted range: {anchor['label']}")

    partition = routes["claim_partition"]
    imported = partition["imported"]
    require(len(imported) == 1, "imported claim count")
    require(imported[0]["source_id"] == "ddnl_1705_05796", "DDNL import route")
    require(imported[0]["candidate_range"] == {"start_line": 317, "end_line": 327},
            "DDNL candidate range")
    require(imported[0]["source_ranges"] == [{"start_line": 62, "end_line": 65},
                                                {"start_line": 74, "end_line": 86}],
            "DDNL source partition")
    supplied = partition["internally_supplied"]
    require(len(supplied) == 2, "internally supplied partition")


def check_semantics() -> None:
    statement = (ROOT / "STATEMENT.tex").read_text(encoding="utf-8")
    proof = (ROOT / "PROOF.tex").read_text(encoding="utf-8")
    require(len(lf_only_lines(ROOT / "STATEMENT.tex")) == 150, "statement line count")
    require(len(lf_only_lines(ROOT / "PROOF.tex")) == 420, "proof line count")
    require("eq:complex-npp-potential-mass-forward" in statement, "forward mass inequality")
    require("eq:complex-npp-potential-mass-reverse" in statement, "reverse mass inequality")
    require("eq:complex-npp-potential-common-current" in statement, "common exhaustion")
    require("\\begin{theorem}\\label{thm:complex-npp-ledger}" in proof, "theorem target")
    require("\\cite[Theorem~1.1]{DDNL18mono}" in proof, "DDNL citation")
    require("it is exactly" in proof[proof.index("Monotonicity of total masses"):], "DDNL import wording")
    require("item \\cref{itm:ch51-import:monotone}" in proof, "import-ledger routing")
    require("We reproduce the local argument" in proof, "internally supplied closedness")
    require("We first construct the pullback" in proof, "internally supplied pullback")
    require("F:=\\mu^{-1}(Z)" in proof, "exact exceptional pair")
    require("eq:complex-npp-pushforward-zero-trace" in proof, "pushforward trace scope")
    require("eq:complex-npp-modification-local-mass" in proof, "downstairs local mass")

    audit = strict_json(ROOT / "audit/INDEPENDENT_AUDIT_RESULT.json")
    require(audit == {
        "blockers": [],
        "candidate": "ch51_npp_ledger_comprehensive_candidate_v2_20260901",
        "date": "2026-09-01",
        "production_verified": False,
        "verdict": "PASS_READY_FOR_SOURCE_CLOSED_PRODUCTION_PACKET",
    }, "independent mathematical audit binding")
    request = strict_json(ROOT / "PRODUCTION_REQUEST.json")
    require(request["execution_status"] == "PREPARED_NOT_SUBMITTED", "request status")
    require(request["submission_performed"] is False, "submission firewall")
    require(request["statement_sha256"] == PINS["STATEMENT.tex"], "request statement hash")
    require(request["proof_sha256"] == PINS["PROOF.tex"], "request proof hash")
    require(request["release_stage"] is None, "known-failed runtime stage must not be attached")
    require(request["release_stage_status"] == "SEPARATE_REPAIRED_STAGE_REQUIRED_AND_NOT_YET_AUDITED",
            "runtime repair boundary")


def check_repair_ledger() -> None:
    ledger = strict_json(ROOT / "REPAIR_LEDGER.json")
    require(
        ledger["authored_status"]
        == "REPAIRED_PACKET_AUTHORED_NOT_INDEPENDENTLY_AUDITED_NOT_SUBMITTED",
        "repair-ledger authored status",
    )
    require(ledger["artifact_delta_from_frozen_v1"] == {
        "added": [
            "REPAIR_LEDGER.json",
            "audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901/AUDIT.md",
            "audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901/AUDIT_RESULT.json",
            "audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901/EVIDENCE.json",
            "audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901/P148_FAILED_SMOKE_RESULT.json",
            "audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901/SHA256SUMS",
            "audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901/check_audit.py",
            "tests/test_packet.py",
        ],
        "generated_after_authored_changes": ["MANIFEST.json", "SHA256SUMS"],
        "modified": [
            "AUTHOR_REPORT.md",
            "PRODUCTION_REQUEST.json",
            "README.md",
            "REQUEST_CONTRACT.md",
            "SOURCE_ROUTES.json",
            "check_packet.py",
            "make_manifest.py",
        ],
    }, "artifact delta ledger")
    require(ledger["exact_byte_preservation"] == {
        relative: PINS[relative]
        for relative in (
            "PROOF.tex",
            "STATEMENT.tex",
            "source_exact/LEDGER_REPLACEMENT.tex",
            "source_exact/LOCAL_CONSTRUCTION_REPLACEMENT.tex",
            "source_pins/BEGZ10_arXiv0812.3674v2.pdf",
            "source_pins/BEGZ10_arXiv0812.3674v2.txt",
            "source_pins/BT82_A_new_capacity.pdf",
            "source_pins/BT82_A_new_capacity.txt",
            "source_pins/DDNL18mono_arXiv1705.05796.pdf",
            "source_pins/DDNL18mono_arXiv1705.05796.txt",
        )
    }, "exact-byte preservation ledger")
    provenance = ledger["provenance"]
    require(provenance["frozen_v1_packet_sha256sums_sha256"]
            == "145f6305a0ea847c176e1cd55d8da46977d8c2545c873d792a6c1ba5f7a18d71",
            "v1 provenance top hash")
    require(provenance["frozen_failed_audit_sha256sums_sha256"]
            == PINS["audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901/SHA256SUMS"],
            "failed-audit provenance top hash")
    blockers = [item["blocker"] for item in ledger["repairs"]]
    require(blockers == ["SOURCE_EXTRACTION_MODE_MISDECLARED",
                          "LF_ROUTE_AND_RUNTIME_LINE_NUMBERING_DIVERGE"],
            "repair blocker ledger")
    require(ledger["runtime_scope"].startswith("No runtime stage is bundled"), "runtime exclusion")


def check_manifest() -> None:
    manifest = strict_json(ROOT / "MANIFEST.json")
    require(
        manifest["status"] == "REPAIRED_PACKET_AUTHORED_NOT_INDEPENDENTLY_AUDITED_NOT_SUBMITTED",
        "manifest status",
    )
    require(
        manifest["candidate"]
        == "ch51_npp_ledger_comprehensive_production_packet_v2_repaired_authored_20260901",
        "manifest candidate",
    )
    actual = {}
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT).as_posix()
        info = path.lstat()
        require(not stat.S_ISLNK(info.st_mode), f"symlink in packet: {relative}")
        if stat.S_ISDIR(info.st_mode):
            continue
        require(stat.S_ISREG(info.st_mode), f"special file in packet: {relative}")
        if relative not in {"MANIFEST.json", "SHA256SUMS"}:
            actual[relative] = path
    require(set(manifest["files"]) == set(actual), "manifest inventory")
    for relative, path in actual.items():
        row = manifest["files"][relative]
        require(row["bytes"] == path.stat().st_size, f"manifest bytes: {relative}")
        require(row["sha256"] == sha256(path), f"manifest hash: {relative}")

    ledger = {}
    for raw in lf_only_lines_bytes(ROOT / "SHA256SUMS"):
        match = re.fullmatch(rb"([0-9a-f]{64})  (.+)", raw)
        require(match is not None, f"malformed SHA256SUMS row: {raw!r}")
        digest = match.group(1).decode("ascii")
        relative = match.group(2).decode("utf-8", errors="strict")
        require(relative not in ledger, f"duplicate SHA row: {relative}")
        ledger[relative] = digest
    ledger_actual = {
        path.relative_to(ROOT).as_posix(): path
        for path in ROOT.rglob("*")
        if path.is_file() and path.relative_to(ROOT).as_posix() != "SHA256SUMS"
    }
    require(set(ledger) == set(ledger_actual), "SHA ledger inventory")
    for relative, path in ledger_actual.items():
        require(ledger[relative] == sha256(path), f"SHA ledger mismatch: {relative}")


def check_author_report() -> None:
    report = (ROOT / "AUTHOR_REPORT.md").read_text(encoding="utf-8")
    rows = {}
    for relative, digest in re.findall(
        r"^\| `([^`]+)` \| `([0-9a-f]{64})` \|$", report, re.M
    ):
        require(relative not in rows, f"duplicate authored hash row: {relative}")
        rows[relative] = digest
    require(set(rows) == REPORTED_FILES, "author report hash inventory")
    for relative, digest in rows.items():
        require(sha256(ROOT / relative) == digest, f"author report hash: {relative}")
    for boundary in (
        "REPAIRED_PACKET_AUTHORED_NOT_INDEPENDENTLY_AUDITED_NOT_SUBMITTED",
        "No production submission was made",
        "No final-path smoke was run",
        "No runtime stage is bundled",
        "independent hostile audit",
    ):
        require(boundary in report, f"author report boundary: {boundary}")


def main() -> None:
    for relative, expected in PINS.items():
        path = ROOT / relative
        require(path.is_file(), f"missing pinned input: {relative}")
        require(sha256(path) == expected, f"pinned input mismatch: {relative}")
    check_nested_sha_ledger(
        ROOT / "audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901",
        PINS["audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901/SHA256SUMS"],
    )
    check_routes()
    check_semantics()
    check_repair_ledger()
    check_author_report()
    check_manifest()
    print("PASS_REPAIRED_CH51_SOURCE_CLOSED_PACKET_AUTHORED_ONLY")


if __name__ == "__main__":
    main()
