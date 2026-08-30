#!/usr/bin/env python3
"""Prepare, but do not submit, the dependency-closed P07.1 packet.

The materialization rule is byte-for-byte the rule used by
``manuscript/editorial/tools/submit_rethlas_packet.py``: strip only terminal
newline characters from each UTF-8 input, join adjacent inputs by two newline
characters, and append one final newline.  No socket is opened here.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


RUN = Path(__file__).resolve().parent
DOSSIERS = RUN.parent
MODEL = DOSSIERS / "p071_stone_polyhedral_corners_v2_20260830"
MODEL_RUN = DOSSIERS / "p071_stone_polyhedral_corners_v2_production_run_20260830"
PRINCIPAL = DOSSIERS / (
    "p071_unbranched_polyhedral_complex_local_collapse_candidate_20260830"
)
PRINCIPAL_AUDIT = DOSSIERS / (
    "p071_unbranched_polyhedral_complex_final_exact_reaudit_20260830"
)


EXPECTED = {
    MODEL / "statement.tex":
        "b46b8e22fa8b3f8f64dcf8ae24d164b905dbe8d9035e37c3ede23321717cc002",
    MODEL / "proof.tex":
        "37a3b6a12f6ddd2a3038dd926dfe8120d8955756efe64608fbd2a37b33c01efb",
    MODEL / "SOURCE_AND_OBLIGATION_MATRIX.md":
        "9dcb2c8bab8fb47e3cdeebb8821776770fa1929b2712afbc047bddeed94ae1c0",
    MODEL / "INDEPENDENT_EXACT_SOURCE_RECHECK_20260830.md":
        "3ff43da8dd1044a0144d6f1410ad5b66020ff868c934886c87f3bc38b5c0f974",
    MODEL / "PRODUCTION_RECEIPT.md":
        "4d00534170a7d5b15582eb3ab4878bd79912b919ea19d9dc8fe6be5822a40955",
    MODEL_RUN / "request.json":
        "6697bc79ad50c8b7a9cf3c63dc63fd5b08a9930f9369b304595254f635573d11",
    MODEL_RUN / "response.json":
        "c5871408ef86be152ecd6e169eaae05f590feef00e5487d37f185780951d5285",
    MODEL_RUN / "headers.json":
        "5d7e0c5e93c43726ef62b2204ea7fdde2929d76f3715c87874662570657b50c6",
    PRINCIPAL / "statement.tex":
        "2bc8574fecdc46ecafc1e41f24608c6db60cb9e48f696204ef503a83bed0625e",
    PRINCIPAL / "proof.tex":
        "ab3348d8d0dc31c4c661e1358f8b70894eff83890a3c6d6abc412810dea4ca30",
    PRINCIPAL / "SOURCE_AND_OBLIGATION_MATRIX.md":
        "915ec96b4c1bc8f191429f2ba75425a447b223c721121ef2510e8b396be1a619",
    PRINCIPAL / "EDGE_CASES_AND_OBSTRUCTIONS.md":
        "27646456fe2a37d333afdab36e659ad4e06d0749eeedb9949c64737cc52098b3",
    PRINCIPAL / "README.md":
        "fc95b3043d78e9961c275734c565b9d4d5fba67a92808ecdcb6827a780159dce",
    PRINCIPAL / "RELEASE_MANIFEST.md":
        "5851a597f28606c1aea2a6b4469c59641af161c54b66d92443074e0dc7f9aad8",
    PRINCIPAL_AUDIT / "INDEPENDENT_EXACT_BYTE_REAUDIT_20260830.md":
        "1f0abda081c5ddcd0eaf9ac11a895af2e6b1b6eaace2fadebd9cb8281a4fd4e2",
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_exact(path: Path, data: bytes) -> None:
    """Create a deterministic file, refusing a differing overwrite."""
    if path.exists():
        if path.read_bytes() != data:
            raise RuntimeError(f"refusing to overwrite differing bytes: {path}")
        return
    path.write_bytes(data)


def materialize(paths: list[Path]) -> bytes:
    parts = [path.read_text(encoding="utf-8").rstrip("\n") for path in paths]
    return ("\n\n".join(parts) + "\n").encode("utf-8")


def component_record(path: Path, materialized: bytes) -> dict[str, object]:
    data = path.read_bytes()
    count = materialized.count(data)
    start = materialized.find(data)
    if count != 1 or start < 0:
        raise RuntimeError(f"input does not occur exactly once: {path}")
    return {
        "path": str(path),
        "sha256": digest(data),
        "size_bytes": len(data),
        "occurrence_count": count,
        "start_offset_bytes": start,
        "end_offset_exclusive_bytes": start + len(data),
        "slice_sha256": digest(materialized[start:start + len(data)]),
        "slice_equals_source": True,
    }


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


def main() -> None:
    for path, expected in EXPECTED.items():
        actual = digest(path.read_bytes())
        if actual != expected:
            raise RuntimeError(f"input SHA-256 mismatch: {path}: {actual}")

    principal_manifest_count = verify_checksum_manifest(PRINCIPAL)
    model_manifest_count = verify_checksum_manifest(MODEL)

    model_response = json.loads((MODEL_RUN / "response.json").read_text())
    report = model_response.get("verification_report") or {}
    if model_response.get("verdict") != "correct":
        raise RuntimeError("model dependency lacks final correct verdict")
    if report.get("critical_errors") or report.get("gaps"):
        raise RuntimeError("model dependency production response is not 0/0")

    model_receipt = (MODEL / "PRODUCTION_RECEIPT.md").read_text(encoding="utf-8")
    principal_matrix = (
        PRINCIPAL / "SOURCE_AND_OBLIGATION_MATRIX.md"
    ).read_text(encoding="utf-8")
    principal_audit = (
        PRINCIPAL_AUDIT / "INDEPENDENT_EXACT_BYTE_REAUDIT_20260830.md"
    ).read_text(encoding="utf-8")
    required_bindings = [
        EXPECTED[MODEL / "statement.tex"],
        EXPECTED[MODEL / "proof.tex"],
        EXPECTED[MODEL_RUN / "response.json"],
        EXPECTED[PRINCIPAL / "statement.tex"],
        EXPECTED[PRINCIPAL / "proof.tex"],
    ]
    for value in required_bindings[:3]:
        if value not in model_receipt and value not in principal_matrix:
            raise RuntimeError(f"missing model receipt/matrix binding: {value}")
    for value in required_bindings:
        if value not in principal_audit and value not in principal_matrix:
            raise RuntimeError(f"missing principal source/audit binding: {value}")

    statement_inputs = [MODEL / "statement.tex", PRINCIPAL / "statement.tex"]
    proof_inputs = [MODEL / "proof.tex", PRINCIPAL / "proof.tex"]
    statement = materialize(statement_inputs)
    proof = materialize(proof_inputs)

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
    if statement_records[-1]["end_offset_exclusive_bytes"] != len(statement):
        raise RuntimeError("principal statement is not the terminal byte substring")
    if proof_records[-1]["end_offset_exclusive_bytes"] != len(proof):
        raise RuntimeError("principal proof is not the terminal byte substring")

    manifest = {
        "endpoint_invoked": False,
        "materialization_rule": (
            "Identical to submit_rethlas_packet.py: UTF-8 text; rstrip only "
            "terminal newline characters per input; join with two newline "
            "characters; append one final newline."
        ),
        "statement_components_in_order": statement_records,
        "proof_components_in_order": proof_records,
        "statement_materialized": {
            "path": str(statement_path),
            "size_bytes": len(statement),
            "sha256": digest(statement),
        },
        "proof_materialized": {
            "path": str(proof_path),
            "size_bytes": len(proof),
            "sha256": digest(proof),
        },
        "request_prepared": {
            "path": str(RUN / "request.prepared.json"),
            "sha256": digest(request_bytes),
            "statement_field_equals_materialized": True,
            "proof_field_equals_materialized": True,
            "verification_deadline_utc": None,
        },
        "source_and_dependency_audit": {
            "principal_frozen_manifest_entries_checked": principal_manifest_count,
            "model_frozen_manifest_entries_checked": model_manifest_count,
            "all_expected_context_artifacts_rehashed": True,
            "model_production_verdict": "correct",
            "model_production_critical_errors": 0,
            "model_production_gaps": 0,
            "principal_independent_audit": "PASS 0/0/0/0",
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


if __name__ == "__main__":
    main()
