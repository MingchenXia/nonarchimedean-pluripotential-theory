#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p logs
python3 prepare_sources.py > logs/source-preparation.log 2>&1
python3 assemble.py > logs/assembly.log 2>&1
python3 make_notes.py > logs/notes-generation.log 2>&1
pandoc P21.3-core.md --standalone --from=markdown --to=latex --output=P21.3-paper.tex > logs/pandoc.log 2>&1
pdflatex -interaction=nonstopmode -halt-on-error P21.3-paper.tex > logs/pdflatex-pass1.log 2>&1
pdflatex -interaction=nonstopmode -halt-on-error P21.3-paper.tex > logs/pdflatex-pass2.log 2>&1
pdftotext P21.3-paper.pdf logs/P21.3-paper-extracted.txt
python3 verify.py > logs/verification.log 2>&1
