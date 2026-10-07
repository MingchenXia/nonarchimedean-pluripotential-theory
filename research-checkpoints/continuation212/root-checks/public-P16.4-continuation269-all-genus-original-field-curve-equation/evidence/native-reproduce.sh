#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python verify_packet.py > packet-check.log
python record_reading.py > reading-check.log
python finite_checks.py > finite-checks.log
pandoc -f markdown+tex_math_single_backslash P16.4-argument.md --standalone --number-sections -o P16.4-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error P16.4-paper.tex > build-first.log
pdflatex -interaction=nonstopmode -halt-on-error P16.4-paper.tex > build-second.log
python audit_artifacts.py > audit.log
