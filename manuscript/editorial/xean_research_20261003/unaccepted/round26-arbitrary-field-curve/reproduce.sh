#!/bin/bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
python prepare.py | tee evidence/prepare-output.txt
python build-and-check.py | tee evidence/build-check-output.txt
python finalize-manifest.py
