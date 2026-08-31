#!/usr/bin/env python3
"""Read-only exact-current audit of a strict Rethlas v0.2 receipt.

This checks bytes, coverage, and protocol provenance, not mathematical truth.
The source root must be the independently inspected production implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import sys
from pathlib import Path

from submit_rethlas_packet import materialize


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("statement", "proof", "request", "response", "headers"):
        parser.add_argument(name, type=Path)
    parser.add_argument("--verifier-source", type=Path, required=True)
    parser.add_argument("--statement-dependency", action="append", default=[], type=Path)
    parser.add_argument("--proof-dependency", action="append", default=[], type=Path)
    args = parser.parse_args()

    # Read the same bytes that submission materializes; do not silently fix them.
    statement = materialize(args.statement_dependency, args.statement)
    proof = materialize(args.proof_dependency, args.proof)
    for name, value in (("statement", statement), ("proof", proof)):
        require(
            all(ord(c) >= 32 or c in "\n\r\t" for c in value)
            and "\x7f" not in value,
            f"{name} contains a forbidden control character",
        )
    request = json.loads(args.request.read_bytes())
    response = json.loads(args.response.read_bytes())
    headers = json.loads(args.headers.read_bytes())
    require(set(request) == {"statement", "proof", "verification_deadline_utc"},
            "unexpected request fields")
    require(request["statement"] == statement, "current statement differs from request")
    require(request["proof"] == proof, "current proof differs from request")
    require(headers["status_code"] == 200, "verification HTTP status is not 200")

    source = args.verifier_source.resolve(strict=True)
    sys.path.insert(0, str(source))
    contracts = importlib.import_module("api.contracts")
    contexts = importlib.import_module("api.proof_context")
    for module in (contracts, contexts):
        require(Path(module.__file__).resolve().is_relative_to(source),
                "verification module imported from an unexpected source")
    manifest = contexts.parse_blueprint(proof, target_statement=statement)
    core_keys = {
        "output_schema_version", "verification_report", "verification_status",
        "verdict", "repair_hints", "needs_expanded_proofs", "checked_item_ids",
        "proof_digest", "context_digest",
    }
    adaptive_keys = {"adaptive_context_digest", "item_context_attestations"}
    require(set(response) == core_keys | adaptive_keys,
            "response is not the strict v0.2 aggregate schema")
    contracts.validate_verification_output(
        {key: response[key] for key in core_keys},
        expected_checked_item_ids=list(manifest.item_ids),
        expected_proof_digest=manifest.proof_digest,
        expected_context_digest=contexts.aggregate_context_digest(manifest),
    )
    require(response["verification_status"] == "final", "verification is not final")
    require(response["verdict"] == "correct", "verification did not accept the proof")

    attestations = response["item_context_attestations"]
    require(isinstance(attestations, list), "item attestations are not a list")
    require([a.get("item_id") for a in attestations] == list(manifest.item_ids),
            "adaptive item coverage differs from the exact manifest")
    attestation_keys = {
        "item_id", "disposition", "final_round", "expanded_proof_ids", "max_chars",
        "context_digest", "verdict",
    }
    for attestation in attestations:
        require(set(attestation) == attestation_keys, "unexpected attestation fields")
        require(attestation["disposition"] == "verified", "item was not verified")
        require(attestation["verdict"] == "correct", "an item failed verification")
        context = contexts.build_item_context(
            manifest, attestation["item_id"],
            max_chars=attestation["max_chars"],
            expanded_proof_ids=attestation["expanded_proof_ids"],
            round_index=attestation["final_round"],
        )
        require(context["digest"] == attestation["context_digest"],
                "current item context does not match the attested context")
        require(not context.get("omitted") and not context.get("missing"),
                "a verified context omits or lacks required records")
    require(
        contexts.aggregate_adaptive_context_digest(manifest, attestations)
        == response["adaptive_context_digest"],
        "adaptive aggregate digest differs",
    )
    paths = [*args.statement_dependency, args.statement,
             *args.proof_dependency, args.proof, args.request, args.response,
             args.headers]
    source_paths = [source / "api" / name for name in
                    ("server.py", "contracts.py", "proof_context.py")]
    print(json.dumps({
        "audit": "PASS",
        "scope": "exact-current bytes and strict receipt protocol; not a proof of truth",
        "statement_payload_sha256": sha(statement.encode("utf-8")),
        "proof_payload_sha256": sha(proof.encode("utf-8")),
        "source_kind": manifest.source_kind,
        "checked_item_ids": list(manifest.item_ids),
        "context_digest": response["context_digest"],
        "adaptive_context_digest": response["adaptive_context_digest"],
        "files": {str(p): sha(p.read_bytes()) for p in paths},
        "verifier_source_files": {str(p): sha(p.read_bytes()) for p in source_paths},
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
