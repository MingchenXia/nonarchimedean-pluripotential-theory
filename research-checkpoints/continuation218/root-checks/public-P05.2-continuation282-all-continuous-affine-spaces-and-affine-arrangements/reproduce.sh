#!/bin/sh
set -eu
python audit_inputs.py > audit-output.json
python check_continuation282.py > certificate-run.log
pandoc -f latex -t markdown P05.2-paper.tex -o argument.md
python -c "from pathlib import Path; [p.unlink(missing_ok=True) for p in (Path('P05.2-paper.aux'), Path('P05.2-paper.out'))]"
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error P05.2-paper.tex > build-pass1.stdout.log
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error P05.2-paper.tex > build-pass2.stdout.log
python make_notes.py
