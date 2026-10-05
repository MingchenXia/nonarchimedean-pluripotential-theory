#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
python prepare_artifacts.py > logs/preparation.log
python prepare_notes.py > logs/note-preparation.log
pandoc P21.3-new-proofs.md --standalone --from=markdown+tex_math_dollars --to=latex -o P21.3-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error P21.3-paper.tex > logs/pdflatex-1.log
pdflatex -interaction=nonstopmode -halt-on-error P21.3-paper.tex > logs/pdflatex-2.log
pdftotext P21.3-paper.pdf logs/P21.3-paper-extracted.txt
python verify.py
