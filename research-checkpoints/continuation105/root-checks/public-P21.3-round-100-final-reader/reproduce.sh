#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
mkdir -p logs
python3 prepare.py > logs/prepare.log 2>&1
python3 audit.py > logs/audit-before-build.log 2>&1
pandoc P21.3-core.md --standalone --to=latex --output=P21.3-paper.tex > logs/pandoc.log 2>&1
pdflatex -interaction=nonstopmode -halt-on-error P21.3-paper.tex > logs/pdflatex-pass1.log 2>&1
pdflatex -interaction=nonstopmode -halt-on-error P21.3-paper.tex > logs/pdflatex-pass2.log 2>&1
pdfinfo P21.3-paper.pdf > logs/pdfinfo.log 2>&1
pdftotext P21.3-paper.pdf logs/P21.3-paper-extracted.txt
python3 audit.py > logs/audit-final.log 2>&1
python3 - <<'PY' > logs/deliverable-hashes.log
import hashlib
from pathlib import Path
for name in ['P21.3-core.md','P21.3-argument.md','P21.3-paper.tex',
             'P21.3-paper.pdf','premises.json','source-manifest.json',
             'status.json','notes.json']:
    print(hashlib.sha256(Path(name).read_bytes()).hexdigest(), name)
PY
