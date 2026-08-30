#!/usr/bin/env python3
"""Prepare, but never submit, the dependency-closed P06.2 packet.

The mathematical fields use exactly the materialization rule in
``submit_rethlas_packet.py``.  This script performs no network operation.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


RUN = Path(__file__).resolve().parent
DOSSIERS = RUN.parent
PRINCIPAL = DOSSIERS / "p062_nonstrict_boundary_resonance_20260830"
AUDIT = DOSSIERS / "p062_nonstrict_boundary_resonance_independent_audit_20260830"
STRICT = DOSSIERS / "p062_endpoint_polycylinder_rigid_slicing_v4_20260830"
STRICT_RUN = DOSSIERS / "p062_endpoint_polycylinder_rigid_slicing_v4_production_run_20260830"

PRINCIPAL_STATEMENT = PRINCIPAL / "p062_nonstrict_boundary_resonance_statement_20260830.tex"
PRINCIPAL_PROOF = PRINCIPAL / "p062_nonstrict_boundary_resonance_proof_20260830.tex"
PRINCIPAL_AUDIT = AUDIT / "INDEPENDENT_EXACT_BYTE_HOSTILE_REAUDIT_20260830.md"
STRICT_REQUEST = STRICT_RUN / "request.json"
STRICT_RESPONSE = STRICT_RUN / "response.json"
STRICT_RECEIPT = STRICT / "PRODUCTION_RECEIPT.md"
BERKOVICH_EXCERPT = RUN / "dependencies/berkovich_relative_interior_and_open_map_excerpt.txt"
CLD_EXCERPT = RUN / "dependencies/cld_scalar_extension_surjectivity_excerpt.txt"

EXPECTED = {
    PRINCIPAL_STATEMENT:
        "27ff3ad7a6174b8b38d5890d8c891681edf416f02e2538017db22edf372c1ed8",
    PRINCIPAL_PROOF:
        "15ff9b3a28b63c1e3f37c104f27e30e77431f389ec694a1d3f3823232ef1f125",
    PRINCIPAL / "SHA256SUMS":
        "c62908add097974a5f639e13b2709ac4bdeea7ff5b08771ffc28785dca62006b",
    PRINCIPAL / "SOURCE_MATRIX.md":
        "e7c677defca9d16a0c2369958441401eccbaec8bba0db55caa094613fec70cf4",
    PRINCIPAL_AUDIT:
        "3a2023342aefdb7bcefcd5a74c05620334907efe7c5ec4e5f9bd51a68d025aa6",
    STRICT / "SHA256SUMS":
        "45aeebfbd055a79bb5eca5d20d167df1c91caa3453d375d410b222157f3b1f17",
    STRICT / "p062_endpoint_polycylinder_v4_statement_20260830.tex":
        "56ffaad6c42e0a14c56279e263d326120ce03f6ae132d8261deee56ff9ca7663",
    STRICT / "p062_endpoint_polycylinder_v4_proof_20260830.tex":
        "2616ac69cd450010b8f0d108d030bd69d2ff2728cad9641ad7d9d0e1a981a0b7",
    STRICT_RECEIPT:
        "1f0c92b2e9c0f03b9d96bbd1c301ffc5aa48787056fe96cda2499f449047d60e",
    STRICT_REQUEST:
        "7b5bdbb4a15fb8d5202d57ddb4c49f84e1844908863c95580ceec7c1f1324171",
    STRICT_RESPONSE:
        "c0d9aaf5a8ef3400b6b20782a0a8d9073c24c200027c4451a9aec9e5432b446d",
    STRICT_RUN / "headers.json":
        "1013a47eaabe8bdeec363937720e76b988fb76dbd90f2009ca10f6a513d0cb94",
    BERKOVICH_EXCERPT:
        "dd56342be988f2ba1d06646160646ce64eece21388fd55fca5b4058226aefabe",
    CLD_EXCERPT:
        "f03831a7ad52df5a6bda36113c34461b02ead09e14d2cff0c238c914da8a596f",
}

EXPECTED_STRICT_STATEMENT_FIELD = (
    "37d8e0b829a6e0780242985da534e180b6428aa8eb3e0251d92ff1cf83fe97d8"
)
EXPECTED_STRICT_PROOF_FIELD = (
    "f3be33890f0ede20b0feea4533fa30159a451568849a2071ac9de738dc6ce278"
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_exact(path: Path, data: bytes) -> None:
    if path.exists():
        if path.read_bytes() != data:
            raise RuntimeError(f"refusing to overwrite differing bytes: {path}")
        return
    path.write_bytes(data)


def materialize(paths: list[Path]) -> bytes:
    parts = [path.read_text(encoding="utf-8").rstrip("\n") for path in paths]
    return ("\n\n".join(parts) + "\n").encode("utf-8")


def verify_checksum_manifest(directory: Path) -> int:
    count = 0
    for line in (directory / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, name = line.split(maxsplit=1)
        path = directory / name.strip()
        if digest(path.read_bytes()) != expected:
            raise RuntimeError(f"frozen SHA256SUMS mismatch: {path}")
        count += 1
    return count


def component_record(path: Path, materialized: bytes) -> dict[str, object]:
    source = path.read_bytes()
    count = materialized.count(source)
    start = materialized.find(source)
    if count != 1 or start < 0:
        raise RuntimeError(f"input does not occur exactly once: {path}")
    return {
        "path": str(path),
        "sha256": digest(source),
        "size_bytes": len(source),
        "occurrence_count": count,
        "start_offset_bytes": start,
        "end_offset_exclusive_bytes": start + len(source),
        "slice_sha256": digest(materialized[start:start + len(source)]),
        "slice_equals_source": True,
    }


def main() -> None:
    for path, expected in EXPECTED.items():
        actual = digest(path.read_bytes())
        if actual != expected:
            raise RuntimeError(f"input SHA-256 mismatch: {path}: {actual}")

    principal_manifest_count = verify_checksum_manifest(PRINCIPAL)
    strict_manifest_count = verify_checksum_manifest(STRICT)

    strict_request = json.loads(STRICT_REQUEST.read_text(encoding="utf-8"))
    strict_statement = strict_request["statement"].encode("utf-8")
    strict_proof = strict_request["proof"].encode("utf-8")
    if digest(strict_statement) != EXPECTED_STRICT_STATEMENT_FIELD:
        raise RuntimeError("strict-v4 request statement field changed")
    if digest(strict_proof) != EXPECTED_STRICT_PROOF_FIELD:
        raise RuntimeError("strict-v4 request proof field changed")

    strict_principal_statement = (
        STRICT / "p062_endpoint_polycylinder_v4_statement_20260830.tex"
    ).read_bytes()
    strict_principal_proof = (
        STRICT / "p062_endpoint_polycylinder_v4_proof_20260830.tex"
    ).read_bytes()
    if strict_statement.count(strict_principal_statement) != 1:
        raise RuntimeError("strict-v4 principal statement binding failed")
    if strict_proof.count(strict_principal_proof) != 1:
        raise RuntimeError("strict-v4 principal proof binding failed")

    strict_response = json.loads(STRICT_RESPONSE.read_text(encoding="utf-8"))
    strict_report = strict_response.get("verification_report") or {}
    if strict_response.get("verdict") != "correct":
        raise RuntimeError("strict-v4 dependency lacks a correct verdict")
    if strict_report.get("critical_errors") or strict_report.get("gaps"):
        raise RuntimeError("strict-v4 production verification is not 0/0")

    audit_text = PRINCIPAL_AUDIT.read_text(encoding="utf-8")
    for required in (
        EXPECTED[PRINCIPAL_STATEMENT], EXPECTED[PRINCIPAL_PROOF],
        "PASS: zero critical errors and zero proof gaps",
    ):
        if required not in audit_text:
            raise RuntimeError(f"independent audit lacks binding: {required}")

    strict_statement_path = RUN / "dependencies/strict_v4_statement.materialized.tex"
    strict_proof_path = RUN / "dependencies/strict_v4_proof.materialized.tex"
    write_exact(strict_statement_path, strict_statement)
    write_exact(strict_proof_path, strict_proof)

    statement_inputs = [strict_statement_path, PRINCIPAL_STATEMENT]
    proof_inputs = [
        strict_proof_path,
        STRICT_RECEIPT,
        STRICT_RESPONSE,
        BERKOVICH_EXCERPT,
        CLD_EXCERPT,
        PRINCIPAL / "SOURCE_MATRIX.md",
        PRINCIPAL_AUDIT,
        PRINCIPAL_PROOF,
    ]
    statement = materialize(statement_inputs)
    proof = materialize(proof_inputs)
    if not statement.endswith(PRINCIPAL_STATEMENT.read_bytes()):
        raise RuntimeError("principal statement bytes are not the terminal bytes")
    if not proof.endswith(PRINCIPAL_PROOF.read_bytes()):
        raise RuntimeError("principal proof bytes are not the terminal bytes")

    statement_path = RUN / "statement.materialized.tex"
    proof_path = RUN / "proof.materialized.tex"
    write_exact(statement_path, statement)
    write_exact(proof_path, proof)

    request_payload = {
        "statement": statement.decode("utf-8"),
        "proof": proof.decode("utf-8"),
        "verification_deadline_utc": None,
    }
    request_bytes = (
        json.dumps(request_payload, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")
    parsed = json.loads(request_bytes.decode("utf-8"))
    if parsed["statement"].encode("utf-8") != statement:
        raise RuntimeError("prepared request changes statement bytes")
    if parsed["proof"].encode("utf-8") != proof:
        raise RuntimeError("prepared request changes proof bytes")
    write_exact(RUN / "request.prepared.json", request_bytes)

    statement_records = [component_record(path, statement) for path in statement_inputs]
    proof_records = [component_record(path, proof) for path in proof_inputs]
    manifest = {
        "endpoint_invoked": False,
        "principal": {
            "statement_sha256": EXPECTED[PRINCIPAL_STATEMENT],
            "proof_sha256": EXPECTED[PRINCIPAL_PROOF],
            "independent_audit_sha256": EXPECTED[PRINCIPAL_AUDIT],
            "independent_audit_verdict": "PASS 0/0",
        },
        "verified_strict_v4_dependency": {
            "statement_field_sha256": digest(strict_statement),
            "proof_field_sha256": digest(strict_proof),
            "production_response_sha256": EXPECTED[STRICT_RESPONSE],
            "production_verdict": "correct",
            "critical_errors": 0,
            "gaps": 0,
        },
        "frozen_manifests_checked": {
            "principal_entries": principal_manifest_count,
            "strict_v4_entries": strict_manifest_count,
        },
        "materialization_rule": (
            "UTF-8; strip only terminal newline characters from each input; "
            "join adjacent inputs with two newline characters; append one final newline."
        ),
        "statement_components_in_order": statement_records,
        "proof_components_in_order": proof_records,
        "statement_materialized": {
            "path": str(statement_path),
            "size_bytes": len(statement),
            "sha256": digest(statement),
            "principal_is_exact_terminal_bytes": True,
        },
        "proof_materialized": {
            "path": str(proof_path),
            "size_bytes": len(proof),
            "sha256": digest(proof),
            "principal_is_exact_terminal_bytes": True,
        },
        "request_prepared": {
            "path": str(RUN / "request.prepared.json"),
            "sha256": digest(request_bytes),
            "decoded_fields_equal_materialized_files": True,
            "verification_deadline_utc": None,
        },
    }
    manifest_bytes = (
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    write_exact(RUN / "MATERIALIZATION_MANIFEST.json", manifest_bytes)

    input_lines = [
        f"{expected}  {path}\n"
        for path, expected in sorted(EXPECTED.items(), key=lambda item: str(item[0]))
    ]
    write_exact(RUN / "INPUT_SHA256SUMS", "".join(input_lines).encode("utf-8"))

    archive_names = [
        "README.md",
        "assemble_prepared_packet.py",
        "dependencies/berkovich_relative_interior_and_open_map_excerpt.txt",
        "dependencies/cld_scalar_extension_surjectivity_excerpt.txt",
        "dependencies/strict_v4_statement.materialized.tex",
        "dependencies/strict_v4_proof.materialized.tex",
        "statement.materialized.tex",
        "proof.materialized.tex",
        "request.prepared.json",
        "MATERIALIZATION_MANIFEST.json",
        "INPUT_SHA256SUMS",
    ]
    archive_lines = []
    for name in archive_names:
        path = RUN / name
        archive_lines.append(f"{digest(path.read_bytes())}  {name}\n")
    write_exact(RUN / "SHA256SUMS", "".join(archive_lines).encode("utf-8"))

    print(json.dumps({
        "endpoint_invoked": False,
        "statement_sha256": digest(statement),
        "proof_sha256": digest(proof),
        "request_prepared_sha256": digest(request_bytes),
        "principal_statement_sha256": EXPECTED[PRINCIPAL_STATEMENT],
        "principal_proof_sha256": EXPECTED[PRINCIPAL_PROOF],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
