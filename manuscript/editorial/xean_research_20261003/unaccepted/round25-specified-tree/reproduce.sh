#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
mkdir -p evidence sources build
python assemble_evidence.py > evidence/assembly-output.json
rm -f build/P06.2-partial.aux build/P06.2-partial.out
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build P06.2-partial.tex > build/pass1.stdout
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build P06.2-partial.tex > build/pass2.stdout
cp build/P06.2-partial.pdf P06.2-partial.pdf
python validate_artifacts.py
