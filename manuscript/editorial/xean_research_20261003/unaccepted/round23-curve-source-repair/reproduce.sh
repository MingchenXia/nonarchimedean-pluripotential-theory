#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
python prepare_evidence.py > evidence/extraction-output.json
python diagnostics/finite_checks.py > diagnostics/output.json
python assemble_and_validate.py > evidence/validation-output.json
