#!/usr/bin/env python3
"""Generate the book index with consistent spelling and untouched TeX sources."""

from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys


ENTRY = re.compile(r"^\\indexentry\{(?P<key>.*)\}\{(?P<page>[^{}]*)\}\s*$")


def canonical_key(key):
    key = key.replace("Monge--Ampere", "Monge--Amp\\`ere")
    return re.sub(
        r"^Stokes formula(?=[!|]|$)", "Stokes formula@Stokes' formula", key
    )


def main():
    args = sys.argv[1:]
    if "-o" not in args or not args:
        raise SystemExit("Usage: make_book_index.py [makeindex options] -o OUTPUT INPUT.idx")
    output = Path(args[args.index("-o") + 1])
    source = Path(args[-1])
    if source.suffix != ".idx" or not source.is_file():
        raise SystemExit("The final argument must be an existing .idx input file.")

    raw = source.read_bytes()
    lines = raw.decode("utf-8").splitlines(keepends=True)
    result = []
    changes = []
    entries = 0
    for line in lines:
        match = ENTRY.match(line)
        if match is not None:
            entries += 1
            key = match["key"]
            fixed = canonical_key(key)
            if fixed != key:
                changes.append({"original": key, "normalized": fixed, "page": match["page"]})
                line = line[:match.start("key")] + fixed + line[match.end("key"):]
        result.append(line)

    normalized = "".join(result).encode("utf-8")
    normalized_path = source.with_suffix(".normalized.idx")
    normalized_path.write_bytes(normalized)
    record = {
        "input": str(source),
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "normalized_input": str(normalized_path),
        "normalized_sha256": hashlib.sha256(normalized).hexdigest(),
        "entry_count": entries,
        "changed_entry_count": len(changes),
        "changes": changes,
        "source_input_preserved": source.read_bytes() == raw,
        "page_arguments_preserved": True,
    }
    output.with_suffix(".index-normalization.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Book index: normalized {len(changes)} of {entries} entries; page arguments preserved.")

    args[-1] = str(normalized_path)
    if "-t" not in args:
        args[-1:-1] = ["-t", str(output.with_suffix(".ilg"))]
    return subprocess.run(["makeindex", *args], check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
