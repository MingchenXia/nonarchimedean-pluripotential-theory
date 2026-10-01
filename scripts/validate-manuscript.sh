#!/usr/bin/env bash
set -euo pipefail

source "$(dirname -- "${BASH_SOURCE[0]}")/tex-env.sh"
cd "$NAPPT_ROOT/manuscript"

for package_file in newtxtext.sty newtxmath.sty dsfont.sty binhex.tex ts1-qtmb.tfm; do
  kpsewhich "$package_file" >/dev/null || {
    printf 'TeX package file missing: %s; run scripts/setup-texlive.sh first\n' "$package_file" >&2
    exit 1
  }
done

PYTHONDONTWRITEBYTECODE=1 python3 editorial/tools/refcheck.py
PYTHONDONTWRITEBYTECODE=1 python3 editorial/tools/check_open_problem_inventory.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest editorial.tools.test_refcheck -v
latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
test -s book.pdf
pdfinfo book.pdf | grep '^Pages:'
