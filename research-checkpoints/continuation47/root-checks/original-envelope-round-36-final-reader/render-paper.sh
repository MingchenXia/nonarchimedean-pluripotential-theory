#!/usr/bin/env bash
set -euo pipefail
pandoc P03.3-argument.md --from markdown+tex_math_dollars --to latex --standalone --top-level-division=section --variable documentclass=article --variable fontsize=11pt --variable geometry:margin=1in --output P03.3-paper.tex
