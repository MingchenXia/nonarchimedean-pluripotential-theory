#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 init_workspace.py
python3 provenance.py
python3 build_and_check.py
python3 make_notes.py
pdftotext build/P16.1-paper.pdf build/P16.1-paper.txt
