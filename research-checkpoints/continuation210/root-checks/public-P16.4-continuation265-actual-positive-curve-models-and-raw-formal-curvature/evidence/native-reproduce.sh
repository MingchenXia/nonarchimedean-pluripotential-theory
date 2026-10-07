#!/usr/bin/env bash
set -euo pipefail
python3 verify_packet.py > packet-verification.log
python3 finite_checks.py > finite-checks.log
pandoc -f markdown+tex_math_single_backslash P16.4-argument.md --standalone --number-sections -o P16.4-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error P16.4-paper.tex > build-first.log
pdflatex -interaction=nonstopmode -halt-on-error P16.4-paper.tex > build-second.log
python3 write_notes.py > native-notes-build.log
python3 artifact_audit.py > artifact-audit.log
