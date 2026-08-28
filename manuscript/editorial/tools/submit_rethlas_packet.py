#!/usr/bin/env python3
"""Submit exact frozen statement/proof bytes to a local Rethlas verifier."""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("statement", type=Path)
    parser.add_argument("proof", type=Path)
    parser.add_argument("request_archive", type=Path)
    parser.add_argument("response_archive", type=Path)
    parser.add_argument("headers_archive", type=Path)
    parser.add_argument(
        "--statement-dependency",
        action="append",
        default=[],
        type=Path,
        help=(
            "prepend an exact dependency to the submitted statement; "
            "repeat for more than one dependency"
        ),
    )
    parser.add_argument(
        "--proof-dependency",
        action="append",
        default=[],
        type=Path,
        help=(
            "prepend an exact dependency proof to the submitted proof; "
            "repeat for more than one dependency"
        ),
    )
    parser.add_argument("--endpoint", default="http://127.0.0.1:8107/verify")
    parser.add_argument("--timeout-seconds", type=int, default=3300)
    return parser.parse_args()


def materialize(dependencies: list[Path], principal: Path) -> str:
    """Read exact UTF-8 inputs, separating bundled artifacts visibly."""
    if not dependencies:
        return principal.read_text(encoding="utf-8")
    parts = [
        path.read_text(encoding="utf-8").rstrip("\n")
        for path in (*dependencies, principal)
    ]
    return "\n\n".join(parts) + "\n"


def main() -> None:
    args = parse_args()
    statement = materialize(args.statement_dependency, args.statement)
    proof = materialize(args.proof_dependency, args.proof)
    deadline = datetime.now(timezone.utc) + timedelta(
        seconds=args.timeout_seconds
    )
    payload = {
        "statement": statement,
        "proof": proof,
        "verification_deadline_utc": deadline.isoformat(),
    }
    request_bytes = (
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")

    for path in (
        args.request_archive,
        args.response_archive,
        args.headers_archive,
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
    args.request_archive.write_bytes(request_bytes)

    headers = {"Content-Type": "application/json; charset=utf-8"}
    token = os.environ.get("VERIFY_API_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(
        args.endpoint,
        data=request_bytes,
        headers=headers,
        method="POST",
    )
    try:
        with urlopen(request, timeout=args.timeout_seconds) as response:
            response_bytes = response.read()
            response_status = response.status
            response_headers = dict(response.headers.items())
    except HTTPError as error:
        response_bytes = error.read()
        response_status = error.code
        response_headers = dict(error.headers.items())
    args.response_archive.write_bytes(response_bytes)
    safe_headers = {
        key: value
        for key, value in response_headers.items()
        if key.lower() in {"content-type", "content-length", "date", "server"}
    }
    args.headers_archive.write_text(
        json.dumps(
            {"status_code": response_status, "headers": safe_headers},
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    if response_status >= 400:
        raise RuntimeError(
            f"verification endpoint returned HTTP {response_status}"
        )

    body = json.loads(response_bytes)
    report = body.get("verification_report") or {}
    summary = {
        "run_id": body.get("run_id"),
        "verification_status": body.get("verification_status"),
        "verdict": body.get("verdict"),
        "checked_items": len(body.get("checked_item_ids", [])),
        "critical_errors": len(
            report.get("critical_errors", body.get("critical_errors", []))
        ),
        "gaps": len(report.get("gaps", body.get("gaps", []))),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
