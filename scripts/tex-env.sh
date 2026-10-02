#!/usr/bin/env bash
# Source this file before running TeX commands outside the repository scripts.

NAPPT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
export NAPPT_ROOT
export TEXMFHOME="${TEXMFHOME:-$NAPPT_ROOT/.texlive}"
export TEXMFCONFIG="${TEXMFCONFIG:-$TEXMFHOME/texmf-config}"
export TEXMFVAR="${TEXMFVAR:-$TEXMFHOME/texmf-var}"
