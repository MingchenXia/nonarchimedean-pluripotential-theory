#!/usr/bin/env python3
"""Read-only checker for the frozen Chapter 51 packet/stage FAIL audit."""

from __future__ import annotations

import hashlib
import json
import re
import stat
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PACKET = Path("/private/tmp/ch51_npp_ledger_comprehensive_production_packet_v1_20260901")
STAGE = Path(
    "/private/tmp/rethlas_hardened_v3_3_3_r5_ch51_npp_ledger_v2_source_closed_stage_20260901"
)
PYTHON = Path(
    "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/"
    "agents/verification/tmp/verification-venv/bin/python"
)


def require(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def strict_json(path: Path):
    def reject_duplicates(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key in {path}: {key}")
            result[key] = value
        return result

    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicates,
        parse_constant=lambda value: (_ for _ in ()).throw(
            ValueError(f"nonfinite JSON token in {path}: {value}")
        ),
    )


def check_ledger(root: Path, expected_top_hash: str) -> None:
    ledger_path = root / "SHA256SUMS"
    require(sha256(ledger_path) == expected_top_hash, f"top ledger hash: {root}")
    ledger = {}
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, f"malformed ledger row in {root}: {line}")
        digest, relative = match.groups()
        require(relative not in ledger, f"duplicate ledger row in {root}: {relative}")
        ledger[relative] = digest
    actual = {}
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        info = path.lstat()
        require(not stat.S_ISLNK(info.st_mode), f"symlink in {root}: {relative}")
        if stat.S_ISDIR(info.st_mode):
            continue
        require(stat.S_ISREG(info.st_mode), f"special file in {root}: {relative}")
        if relative != "SHA256SUMS":
            actual[relative] = path
    require(set(ledger) == set(actual), f"ledger inventory: {root}")
    for relative, path in actual.items():
        require(ledger[relative] == sha256(path), f"ledger digest: {root}/{relative}")


def check_manifest(root: Path, expected_hash: str, expected_status: str) -> None:
    manifest_path = root / "MANIFEST.json"
    require(sha256(manifest_path) == expected_hash, f"manifest hash: {root}")
    manifest = strict_json(manifest_path)
    require(manifest["status"] == expected_status, f"manifest status: {root}")
    actual = {
        path.relative_to(root).as_posix(): path
        for path in root.rglob("*")
        if path.is_file()
        and path.relative_to(root).as_posix() not in {"MANIFEST.json", "SHA256SUMS"}
    }
    require(set(manifest["files"]) == set(actual), f"manifest inventory: {root}")
    for relative, path in actual.items():
        row = manifest["files"][relative]
        require(row["bytes"] == path.stat().st_size, f"manifest bytes: {root}/{relative}")
        require(row["sha256"] == sha256(path), f"manifest digest: {root}/{relative}")


def run_checker(root: Path, script: str, expected: str) -> None:
    result = subprocess.run(
        [str(PYTHON), "-B", script],
        cwd=root,
        env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin:/usr/sbin:/sbin"},
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    require(result.returncode == 0, f"authored checker failed: {root}: {result.stderr}")
    require(result.stdout.strip() == expected, f"authored checker output: {root}")


def extract(pdf: Path, *, layout: bool) -> bytes:
    command = ["pdftotext"]
    if layout:
        command.append("-layout")
    command.extend([str(pdf), "-"])
    result = subprocess.run(command, capture_output=True, timeout=60, check=False)
    require(result.returncode == 0, f"pdftotext failed for {pdf}: {result.stderr!r}")
    return result.stdout


def check_routes() -> None:
    packet_routes = strict_json(PACKET / "SOURCE_ROUTES.json")
    stage_routes = strict_json(STAGE / "SOURCE_ROUTES.json")
    require(sha256(PACKET / "SOURCE_ROUTES.json") ==
            "1e58e2763abb43d217976f6f2decb239bf47ce44c8546d014fae38b2cd351912",
            "packet route hash")
    require(sha256(STAGE / "SOURCE_ROUTES.json") ==
            "6344bb8decf5f0fb74760c3f35236aa6bcdb3c28a26d49b75b9079fdc93b3447",
            "stage route hash")
    packet_external = {row["source_id"]: row for row in packet_routes["external_routes"]}
    stage_external = {row["source_id"]: row for row in stage_routes["external_routes"]}
    require(set(packet_external) == set(stage_external) == {
        "begz_0812_3674v2", "bt82_new_capacity", "ddnl_1705_05796"
    }, "external route ids")

    expected = {
        "begz_0812_3674v2": {
            "declared": "pdftotext",
            "plain": "51410bdbf39ac3e3c36b5b3f953325a5e81cbdb424c9046d0b1d6414e1eac697",
            "layout": "890173e309165984432e7326d13b7e096662cc805fbc19045a297f12211254c7",
            "bundled": "8bc1801705532fc32a2e8b5d0dcd8d19ec6c3b4efdeab36fc945264e0fad0a91",
        },
        "bt82_new_capacity": {
            "declared": "pdftotext",
            "plain": "b90db94a1d308e526b1b08bf20536e1ff4f79b29a012658c84379f44a591a83a",
            "layout": "716a2e1012a35ab6811873bc9f84d981627b7d6f4d9e6e4c8d48b0b525460d8b",
            "bundled": "247b69c13c392e1b05b3ae964059270b0dae47cecdee889648afd13ed28910d4",
        },
        "ddnl_1705_05796": {
            "declared": "pdftotext -layout",
            "layout": "c46d0c5d9ef56e4788337baef00e53bd099f130cf13913cd94b1ba19e9c5004f",
            "bundled": "cd1cc5bacbfc6b0ec023cceaf751d22a8484cfe38ae8bac531b1f5d99a321df7",
        },
    }
    for source_id, row in stage_external.items():
        pin = expected[source_id]
        require(row["extraction"] == pin["declared"], f"declared extraction: {source_id}")
        pdf = STAGE / row["pdf_path"]
        text = STAGE / row["text_path"]
        layout = extract(pdf, layout=True)
        require(sha256_bytes(layout) == pin["layout"], f"layout extraction: {source_id}")
        require(row["pre_normalization_text_sha256"] == pin["layout"],
                f"pre-normalization route: {source_id}")
        require(text.read_bytes() == layout + b"\n", f"one-LF normalization: {source_id}")
        require(sha256(text) == pin["bundled"], f"bundled text: {source_id}")
        if "plain" in pin:
            plain = extract(pdf, layout=False)
            require(sha256_bytes(plain) == pin["plain"], f"plain extraction: {source_id}")
            require(pin["plain"] != row["pre_normalization_text_sha256"],
                    f"expected declared-command mismatch: {source_id}")
        packet_row = packet_external[source_id]
        for key in (
            "extraction", "normalization", "pdf_sha256", "text_sha256",
            "pre_normalization_text_sha256", "ranges"
        ):
            require(packet_row[key] == row[key], f"packet/stage route parity: {source_id}:{key}")


def check_targets_and_partition() -> None:
    statement_hash = "9ff17ccf6ecafdaedf746e8472671bbd9436cf5661667e27815e1a1d39698575"
    proof_hash = "187ef5530c9baf375cab4d15108a4447f3ddb3cc4c0b2780a7bf8d7cd2f33d70"
    statement_paths = [
        PACKET / "STATEMENT.tex",
        PACKET / "source_exact/LOCAL_CONSTRUCTION_REPLACEMENT.tex",
        STAGE / "target/STATEMENT.tex",
        STAGE / "runtime/sources/ch51_npp_ledger_v2_local.tex",
    ]
    proof_paths = [
        PACKET / "PROOF.tex",
        PACKET / "source_exact/LEDGER_REPLACEMENT.tex",
        STAGE / "target/PROOF.tex",
        STAGE / "runtime/sources/ch51_npp_ledger_v2_ledger.tex",
    ]
    require({sha256(path) for path in statement_paths} == {statement_hash}, "statement preservation")
    require({sha256(path) for path in proof_paths} == {proof_hash}, "proof preservation")
    require(len(statement_paths[0].read_text(encoding="utf-8").splitlines()) == 150,
            "statement line count")
    proof_lines = proof_paths[0].read_text(encoding="utf-8").splitlines()
    require(len(proof_lines) == 420, "proof line count")
    require("Monotonicity of total masses" in proof_lines[316], "import range start")
    require("Theorem~1.1]{DDNL18mono}" in proof_lines[320], "DDNL citation")
    require("Modifications" in proof_lines[327], "internal range restart")

    partition = strict_json(STAGE / "SOURCE_ROUTES.json")["claim_partition"]
    require(partition["imported"] == [{
        "candidate_path": "runtime/sources/ch51_npp_ledger_v2_ledger.tex",
        "candidate_range": {"end_line": 327, "start_line": 317},
        "description": "The unrestricted monotonicity of total mixed nonpluripolar masses is imported from DDNL Theorem 1.1; for p<n the packet adjoins n-p smooth Kahler entries.",
        "source_id": "ddnl_1705_05796",
        "source_ranges": [
            {"end_line": 65, "start_line": 62},
            {"end_line": 86, "start_line": 74},
        ],
    }], "import partition")
    require(partition["internally_supplied"][1]["ranges"] == [
        {"end_line": 316, "start_line": 51},
        {"end_line": 420, "start_line": 328},
    ], "internal proof partition")
    ddnl_text = (STAGE / "runtime/sources/ddnl_1705.05796.txt").read_text(
        encoding="utf-8"
    )
    ddnl_lf = ddnl_text.split("\n")
    ddnl_runtime = ddnl_text.splitlines()
    require("less singular than" in ddnl_lf[61], "DDNL LF orientation route")
    require("less singular than" in ddnl_runtime[62], "DDNL runtime orientation shift")
    require("Theorem 1.1." in ddnl_lf[80], "DDNL LF theorem route")
    require("Theorem 1.1." in ddnl_runtime[81], "DDNL runtime theorem shift")

    begz_text = (STAGE / "runtime/sources/begz_0812_3674v2.txt").read_text(
        encoding="utf-8"
    )
    require("Definition 1.1." in begz_text.split("\n")[210], "BEGZ LF anchor")
    require("Definition 1.1." in begz_text.splitlines()[214], "BEGZ runtime anchor")
    bt_text = (STAGE / "runtime/sources/bt82_new_capacity.txt").read_text(
        encoding="utf-8"
    )
    require("THEOREM 6.9." in bt_text.split("\n")[1106], "BT82 LF anchor")
    require("THEOREM 6.9." in bt_text.splitlines()[1130], "BT82 runtime anchor")
    require(not any("THEOREM 6.9." in line for line in bt_text.splitlines()[1103:1118]),
            "contracted BT82 tool range must miss Theorem 6.9")

    service = (STAGE / "runtime/hardened_service.py").read_text(encoding="utf-8")
    mcp = (STAGE / "runtime/hardened_mcp.py").read_text(encoding="utf-8")
    require('.read_text(encoding="utf-8", errors="replace").splitlines()' in service,
            "host splitlines implementation")
    require('.read_text(encoding="utf-8", errors="replace").splitlines()' in mcp,
            "MCP splitlines implementation")


def check_pinset_and_runner() -> None:
    require(sha256(STAGE / "runtime/release_pins.py") ==
            "639019e6b0a7af1dc0d3b0bb4d78f94936df19a8e2148d985b56f939fbe4ff3d",
            "release pin module")
    command = [
        str(PYTHON), "-B", "-c",
        "import release_pins as p; print(p.canonical_pinset_sha256())",
    ]
    result = subprocess.run(
        command,
        cwd=STAGE / "runtime",
        env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin:/usr/sbin:/sbin"},
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    require(result.returncode == 0, f"pinset recomputation: {result.stderr}")
    require(result.stdout.strip() ==
            "c731c6d278c9fe905d1d4d109b46b9a01181c2bb146f6eef3a010d0b0d3063d0",
            "canonical pinset")

    runner = STAGE / "run_static_model_long_smoke.py"
    require(sha256(runner) ==
            "5a8f25b6851667d284d84bd8874fdfcdeb640f51380727a95a72eb9991b10c78",
            "known failed runner hash")
    source = runner.read_text(encoding="utf-8")
    require("stderr=subprocess.STDOUT" in source, "merged stderr blocker")
    require("while process.poll() is None and time.monotonic() < deadline:" in source,
            "terminal sampling race blocker")
    failed = strict_json(ROOT / "P148_FAILED_SMOKE_RESULT.json")
    require(sha256(ROOT / "P148_FAILED_SMOKE_RESULT.json") ==
            "8ce5e6624854b647f55de53aa8d0257adacf8c98825a9a0c13da2641e6561ec9",
            "copied failed-smoke result")
    require(failed["verdict"] == "FAIL", "prior smoke verdict")
    require({row["id"] for row in failed["blockers"]} == {
        "RAW_LIFECYCLE_NON_JSON_INTERLEAVING",
        "TERMINAL_PROCESS_SAMPLE_EXIT_RACE",
    }, "prior smoke blockers")


def check_no_generated_artifacts() -> None:
    forbidden_parts = {"__pycache__", ".pytest_cache", "artifacts", "STATIC_MODEL_LONG_SMOKE"}
    for root in (PACKET, STAGE):
        for path in root.rglob("*"):
            require(not any(part in forbidden_parts for part in path.relative_to(root).parts),
                    f"generated path in frozen object: {path}")


def check_audit_files() -> None:
    result = strict_json(ROOT / "AUDIT_RESULT.json")
    require(result["verdict"] == "FAIL_REPAIR_REQUIRED", "audit verdict")
    require(result["production_submission_authorized"] is False, "production firewall")
    require(result["ready_for_final_path_smoke"] is False, "smoke firewall")
    require({row["id"] for row in result["blockers"]} == {
        "SOURCE_EXTRACTION_MODE_MISDECLARED",
        "LF_ROUTE_AND_RUNTIME_LINE_NUMBERING_DIVERGE",
        "KNOWN_FAILED_FINAL_PATH_SMOKE_RUNNER_REUSED",
    }, "audit blocker set")
    evidence = strict_json(ROOT / "EVIDENCE.json")
    require(evidence["runtime_static_suite"] == [
        {"elapsed_seconds": 17.138, "errors": 0, "failures": 0, "tests_run": 135},
        {"elapsed_seconds": 16.293, "errors": 0, "failures": 0, "tests_run": 135},
    ], "static suite evidence")
    report = (ROOT / "AUDIT.md").read_text(encoding="utf-8")
    for marker in (
        "FAIL_REPAIR_REQUIRED",
        "SOURCE_EXTRACTION_MODE_MISDECLARED",
        "LF_ROUTE_AND_RUNTIME_LINE_NUMBERING_DIVERGE",
        "KNOWN_FAILED_FINAL_PATH_SMOKE_RUNNER_REUSED",
        "Chapter 51 mathematical target",
        "did not install",
    ):
        require(marker in report, f"audit report marker: {marker}")

    ledger = {}
    for line in (ROOT / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, f"malformed audit SHA row: {line}")
        digest, relative = match.groups()
        require(relative not in ledger, f"duplicate audit SHA row: {relative}")
        ledger[relative] = digest
    actual = {
        path.relative_to(ROOT).as_posix(): path
        for path in ROOT.iterdir()
        if path.is_file() and path.name != "SHA256SUMS"
    }
    require(set(ledger) == set(actual), "audit SHA inventory")
    for relative, path in actual.items():
        require(ledger[relative] == sha256(path), f"audit SHA digest: {relative}")


def main() -> None:
    check_ledger(PACKET, "145f6305a0ea847c176e1cd55d8da46977d8c2545c873d792a6c1ba5f7a18d71")
    check_ledger(STAGE, "9a227d3c7bf256d97dc9a361b63bf06d4633b463916d60b08326a27ba92950b1")
    check_manifest(PACKET, "c04ba66fb1c0b026cb81e75f3ce56479f4ebab949d6fb407ceb93c7684323c76",
                   "AUTHORED_PACKET_NOT_SUBMITTED")
    check_manifest(STAGE, "ba69a35596c369b6e5e751dcf8d6ca9b4d3d1ade2667cbe92cd57a56c261b8f7",
                   "AUTHORED_STATIC_STAGE_NOT_RELEASED")
    run_checker(PACKET, "check_packet.py", "PASS_AUTHORED_SOURCE_CLOSED_PACKET_NOT_SUBMITTED")
    run_checker(STAGE, "check_static_stage.py",
                "PASS_AUTHORED_CH51_SOURCE_CLOSED_STATIC_STAGE_NOT_RELEASED")
    check_routes()
    check_targets_and_partition()
    check_pinset_and_runner()
    check_no_generated_artifacts()
    check_audit_files()
    print("PASS_FROZEN_CH51_PACKET_STAGE_FAIL_AUDIT: 3 blockers")


if __name__ == "__main__":
    main()
