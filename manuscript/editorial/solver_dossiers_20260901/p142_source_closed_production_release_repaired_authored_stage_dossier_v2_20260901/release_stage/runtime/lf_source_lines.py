"""Decode fixed-source line addresses using LF bytes and no other separator.

The release locators are byte-addressed: only byte ``0x0a`` ends a line.
In particular, form-feed (``0x0c``), carriage return, vertical tab, and the
other separators recognized by :meth:`str.splitlines` remain inside their
containing line.  Decoding retains the runtime's historical replacement
semantics for any malformed UTF-8 byte sequence; the immutable source pins
make that fallback deterministic.
"""

from __future__ import annotations

from pathlib import Path


def read_lf_only_source_lines(path: Path) -> list[str]:
    """Return decoded source lines, splitting exclusively at byte ``0x0a``."""

    chunks = path.read_bytes().split(b"\x0a")
    if chunks and chunks[-1] == b"":
        chunks.pop()
    return [chunk.decode("utf-8", errors="replace") for chunk in chunks]
