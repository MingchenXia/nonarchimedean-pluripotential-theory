#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
mkdir -p logs/tex-build
python build_evidence.py > logs/evidence-build.json
python prepare.py > logs/prepare.json
python write_notes.py > logs/notes-build.json
pandoc P21.3-core.md --from=markdown+tex_math_dollars --to=latex --standalone \
  --include-in-header=paper-header.tex \
  --variable=geometry:margin=1in --variable=fontsize:11pt \
  --variable=colorlinks:true --variable=linkcolor:blue --variable=urlcolor:blue \
  --output=P21.3-paper.tex > logs/pandoc.stdout.log 2> logs/pandoc.stderr.log
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory=logs/tex-build P21.3-paper.tex > logs/pdflatex-pass1.log 2>&1
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory=logs/tex-build P21.3-paper.tex > logs/pdflatex-pass2.log 2>&1
cp logs/tex-build/P21.3-paper.pdf P21.3-paper.pdf
pdftotext -layout P21.3-paper.pdf logs/P21.3-paper-extracted.txt
python audit.py > logs/audit.json
