from __future__ import annotations

import time
from datetime import datetime, timezone
from typing import Any, Dict

from fastmcp import FastMCP


APP = FastMCP("rethlas-static-model-ttl-smoke")


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@APP.tool(name="wait_across_catalog_ttl")
def wait_across_catalog_ttl(seconds: int) -> Dict[str, Any]:
    if type(seconds) is not int or seconds != 310:
        raise ValueError("the immutable smoke duration is exactly 310 seconds")
    started_at_utc = _utc_now()
    started = time.monotonic()
    deadline = started + seconds
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break
        time.sleep(min(5.0, remaining))
    elapsed = time.monotonic() - started
    return {
        "status": "ok",
        "requested_seconds": seconds,
        "elapsed_seconds": elapsed,
        "started_at_utc": started_at_utc,
        "completed_at_utc": _utc_now(),
    }


if __name__ == "__main__":
    APP.run()
