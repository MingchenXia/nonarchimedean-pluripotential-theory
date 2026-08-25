#!/usr/bin/env python3
"""Submit exact frozen statement/proof bytes to a local Rethlas verifier."""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("statement", type=Path)
    parser.add_argument("proof", type=Path)
    parser.add_argument("request_archive", type=Path)
    parser.add_argument("response_archive", type=Path)
    parser.add_argument("headers_archive", type=Path)
    parser.add_argument("--endpoint", default="http://127.0.0.1:8107/verify")
    parser.add_argument("--timeout-seconds", type=int, default=3300)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    statement = args.statement.read_text(encoding="utf-8")
    proof = args.proof.read_text(encoding="utf-8")
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
    response = requests.post(
        args.endpoint,
        data=request_bytes,
        headers=headers,
        timeout=args.timeout_seconds,
    )
    args.response_archive.write_bytes(response.content)
    safe_headers = {
        key: value
        for key, value in response.headers.items()
        if key.lower() in {"content-type", "content-length", "date", "server"}
    }
    args.headers_archive.write_text(
        json.dumps(
            {"status_code": response.status_code, "headers": safe_headers},
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    response.raise_for_status()

    body = response.json()
    summary = {
        "run_id": body.get("run_id"),
        "verification_status": body.get("verification_status"),
        "verdict": body.get("verdict"),
        "checked_items": len(body.get("checked_item_ids", [])),
        "critical_errors": len(body.get("critical_errors", [])),
        "gaps": len(body.get("gaps", [])),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
