from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import stat


ROOT = Path(__file__).resolve().parent
BASE_SOURCE = Path(
    "/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory/"
    "manuscript/editorial/solver_dossiers_20260901/"
    "ch51_npp_no_pluripolar_charge_production_packet_v2_20260901/"
    "FROZEN_POSTIMAGE_ch51_complex_prerequisites.tex"
)
ACCEPTED_ARCHIVE = Path(
    "/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory/"
    "manuscript/editorial/solver_dossiers_20260901/"
    "ch51_npp_no_pluripolar_charge_production_archive_v2_20260901"
)

BASE_SHA = "4db4d9028c80b47994143172c356c39419954471af222b8a4f9740b9b5fcf834"
CORRECTED_SHA = "b31c01ebe39eff954e322a5924ef5814b64337d389605ed247ddd38f71279965"
PACKET_SHA = "c2404ea689ed09cf80fb8059145bc74bab123fd39c7e1d3b70f2f37b4c484fce"
STATEMENT_SHA = "9cd8fe1533c99d9d2de9e351610da4b7843d156a523d97344032cf75e3953715"
PROOF_SHA = "adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9"
RUN_ID = "20260901T143740Z_9b8ffa07bc57_69cb27d9"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha(path: Path) -> str:
    return digest(path.read_bytes())


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def reject_duplicates(pairs):
    value = {}
    for key, item in pairs:
        require(key not in value, f"duplicate JSON key: {key}")
        value[key] = item
    return value


def strict_json(path: Path):
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicates,
        parse_constant=lambda item: (_ for _ in ()).throw(
            RuntimeError(f"nonfinite JSON value: {item}")
        ),
    )


def regular_file(path: Path) -> None:
    info = path.lstat()
    require(stat.S_ISREG(info.st_mode), f"non-regular file: {path}")
    require(not stat.S_ISLNK(info.st_mode), f"symlink: {path}")


def main() -> None:
    expected_entries = {
        "FROZEN_CORRECTED_CH51_SOURCE.tex",
        "PROOF.tex",
        "PROPOSED_STATEMENT.tex",
        "SHA256SUMS",
        "SOURCE_LEDGER.md",
        "SPAN_MAP.json",
        "check_packet.py",
        "p148_ch51_dependency_v3.txt",
    }
    require({path.name for path in ROOT.iterdir()} == expected_entries, "packet inventory mismatch")
    for path in ROOT.iterdir():
        regular_file(path)
        require("__pycache__" not in path.parts and path.suffix != ".pyc", f"cache byte: {path}")

    base_bytes = BASE_SOURCE.read_bytes()
    corrected_path = ROOT / "FROZEN_CORRECTED_CH51_SOURCE.tex"
    corrected_bytes = corrected_path.read_bytes()
    require(len(base_bytes) == 195756 and digest(base_bytes) == BASE_SHA, "base source binding")
    require(len(corrected_bytes) == 195880 and digest(corrected_bytes) == CORRECTED_SHA, "corrected source binding")
    base_lines = base_bytes.decode("utf-8").splitlines(keepends=True)
    corrected_lines = corrected_bytes.decode("utf-8").splitlines(keepends=True)
    require(len(base_lines) == len(corrected_lines) == 4516, "source line count")
    changed = [
        index + 1
        for index, (old, new) in enumerate(zip(base_lines, corrected_lines))
        if old != new
    ]
    require(changed == [3775, 3776, 3784, 3785, 3786], f"unexpected source delta: {changed}")
    expected_new = {
        3775: r"choice \(\ell_0=1\) and \(\ell_m=\rme^{-4^m}\) for \(m\geq1\)" + "\n",
        3776: r"satisfies both hypotheses, since the summands for \(m\geq1\) equal \(2^m\)." + "\n",
        3784: r"when the displayed series diverges.  With \(\ell_0=1\) and \(\ell_m=\rme^{-4^m}\) for \(m\geq1\)," + "\n",
        3785: r"one has \(\ell_1/\ell_0=\rme^{-4}\leq1/2\); for \(m\geq1\), \(\ell_{m+1}/\ell_m=\rme^{-3\cdot4^m}\leq1/2\) and" + "\n",
        3786: r"\(2^{-m}\log(1/\ell_m)=2^m\), so the series diverges." + "\n",
    }
    for line_number, expected in expected_new.items():
        require(corrected_lines[line_number - 1] == expected, f"corrected line {line_number}")

    accepted_machine = ACCEPTED_ARCHIVE / "independent_audit/MACHINE_SUMMARY.json"
    accepted_report = ACCEPTED_ARCHIVE / "independent_audit/REPORT.md"
    accepted_manifest = ACCEPTED_ARCHIVE / "SHA256SUMS"
    require(sha(accepted_machine) == "9bb022221ae30d321e00a4569bf9e2a0c19ee4252b3e26b2be7ca44c994a2930", "machine receipt hash")
    require(sha(accepted_report) == "e18d900b8361c63e969cf24cc01e5ca9e159fb298fb038af6a5c02bd9ee955a0", "audit report hash")
    require(sha(accepted_manifest) == "1087f356dbdcd04e1cd76943015ddc4ee48a7da3c9023909c949a340d30fa8f7", "archive manifest hash")
    accepted = strict_json(accepted_machine)
    require(accepted["verdict"] == "PASS", "independent Ch51 receipt audit")
    require(accepted["run_id"] == RUN_ID, "accepted run id")
    require(accepted["model"] == "gpt-5.6-sol" and accepted["reasoning_effort"] == "xhigh", "accepted model/effort")
    require(accepted["acceptance_status"] == "accepted" and accepted["acceptance_errors"] == [], "accepted host status")
    require(accepted["verification_verdict"] == "correct", "accepted verifier verdict")
    require(accepted["verification_critical_errors"] == [] and accepted["verification_gaps"] == [], "accepted verifier defects")

    mapping = strict_json(ROOT / "SPAN_MAP.json")
    require(set(mapping) == {
        "format", "status", "target", "chapter51_no_pluripolar_charge_acceptance",
        "chapter51_source", "packet", "spans", "excluded",
    }, "span-map keyset")
    require(mapping["format"] == "p148-ch51-noncircular-dependency-map-v3", "map format")
    require(mapping["status"] == "authored_static_stage_bound_to_accepted_ch51_run", "map status")
    bound = mapping["chapter51_no_pluripolar_charge_acceptance"]
    require(bound["run_id"] == RUN_ID, "map run binding")
    require(bound["acceptance_status"] == "accepted" and bound["verification_verdict"] == "correct", "map acceptance binding")
    require(bound["critical_errors"] == [] and bound["gaps"] == [], "map error/gap binding")
    source_record = mapping["chapter51_source"]
    require(source_record["base_sha256"] == BASE_SHA and source_record["corrected_sha256"] == CORRECTED_SHA, "map source hashes")
    require(source_record["changed_lines_only"] == changed and source_record["line_shift_from_base"] == 0, "map source delta")

    spans = mapping["spans"]
    require(len(spans) == 10, "ten-span count")
    reconstructed = b""
    packet_cursor = 1
    for item in spans:
        start, end = item["source_lines"]
        block = "".join(corrected_lines[start - 1:end]).encode("utf-8")
        require(len(block) == item["bytes"], f"span bytes {start}-{end}")
        require(digest(block) == item["sha256"], f"span digest {start}-{end}")
        require(end - start + 1 == item["lines"], f"span lines {start}-{end}")
        packet_start, packet_end = item["packet_lines"]
        require(packet_start == packet_cursor, "packet span continuity")
        require(packet_end - packet_start + 1 == item["lines"], "packet span length")
        packet_cursor = packet_end + 1
        reconstructed += block

    definition = "".join(corrected_lines[3287:3301]).encode("utf-8")
    require(len(definition) == 420, "definition bytes")
    require(digest(definition) == "6f88ee1baa59594bb4c637cdac959842d97441dd0b303053009fce59714ee2c1", "definition hash")
    require(definition == "".join(base_lines[3287:3301]).encode("utf-8"), "definition changed from accepted postimage")
    require(corrected_lines[3302].startswith(r"\begin{theorem}\label{thm:complex-i-projection}"), "projection boundary")

    packet_path = ROOT / "p148_ch51_dependency_v3.txt"
    packet = packet_path.read_bytes()
    require(packet == reconstructed, "packet reconstruction")
    require(len(packet) == 34444 and packet.count(b"\n") == 784, "packet shape")
    require(digest(packet) == PACKET_SHA, "packet digest")
    text = packet.decode("utf-8")
    require("def:complex-i-envelope" in text and "eq:complex-i-envelope" in text, "I-envelope definition missing")
    require(r"choice \(\ell_0=1\) and \(\ell_m=\rme^{-4^m}\) for \(m\geq1\)" in text, "Cantor index repair missing")
    require(r"choice \(\ell_m=\rme^{-4^m}\) satisfies both hypotheses" not in text, "old false compatibility remains")
    require(r"\ell_1/\ell_0=\rme^{-4}\leq1/2" in text, "first-ratio check missing")
    for forbidden in (
        "thm:complex-i-projection",
        "eq:complex-i-projection",
        r"Zero mass is not an \(\mathcal I\)-condition",
        r"\varphi_s:=sG_\mu",
        "potentials of every mass",
        "P14.8",
    ):
        require(forbidden not in text, f"circular marker: {forbidden}")

    excluded = mapping["excluded"][1]
    excluded_start, excluded_end = excluded["source_lines"]
    excluded_bytes = "".join(corrected_lines[excluded_start - 1:excluded_end]).encode("utf-8")
    require(len(excluded_bytes) == 770 and digest(excluded_bytes) == excluded["sha256"], "excluded conclusion binding")
    require(excluded_bytes not in packet, "excluded all-mass conclusion leaked")

    targets = {
        "PROPOSED_STATEMENT.tex": (2900, STATEMENT_SHA),
        "PROOF.tex": (3884, PROOF_SHA),
    }
    for name, (size, expected) in targets.items():
        data = (ROOT / name).read_bytes()
        require(len(data) == size and digest(data) == expected, f"target binding: {name}")

    manifest_text = (ROOT / "SHA256SUMS").read_text(encoding="utf-8")
    require(manifest_text.endswith("\n"), "manifest terminal LF")
    rows = {}
    order = []
    for row in manifest_text.splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^/\n]+)", row)
        require(match is not None, f"malformed manifest row: {row!r}")
        expected, name = match.groups()
        require(name not in rows and name != "SHA256SUMS", "invalid manifest path")
        rows[name] = expected
        order.append(name)
    require(order == sorted(order), "manifest order")
    require(set(rows) == expected_entries - {"SHA256SUMS"}, "manifest inventory")
    for name, expected in rows.items():
        require(sha(ROOT / name) == expected, f"manifest digest: {name}")

    print("PASS_AUTHORED_NONCIRCULAR_DEPENDENCY_PACKET_V3")


if __name__ == "__main__":
    main()
