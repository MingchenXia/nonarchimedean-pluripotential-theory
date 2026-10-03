# Reproduce the manuscript build environment

Use an existing checkout of this repository. Cloud tasks already have an
isolated checkout; do not create a Git worktree unless you explicitly need
one.

## Prerequisites

- TeX Live **2025**, including `tlmgr`, `pdflatex`, `latexmk`, `bibtex`,
  `makeindex`, and the standard LaTeX, graphics, and recommended font
  collections. The setup script checks the TeX Live year and installs the
  missing `newtx`, `doublestroke`, `kastrup`, and `tex-gyre` packages from the
  frozen 2025 archive.
- Python 3, `pdfinfo` (Poppler), GnuPG (`gpg`), and `curl`. The script checks
  the pinned fingerprint of TeX Live's official signing key, requires a
  verified archive signature, and retains TeX Live's download checksum checks.
- HTTPS access to `ftp.math.utah.edu` and `www.tug.org`. In Codex cloud
  environment settings, allow both hostnames if outbound access is restricted.
  No secret is needed.

On Debian 13, a suitable base installation is:

```sh
sudo apt-get update
sudo apt-get install -y \
  texlive-base texlive-latex-base texlive-latex-recommended \
  texlive-latex-extra texlive-pictures texlive-fonts-recommended \
  latexmk poppler-utils python3 gnupg curl
```

Other systems can use the official TeX Live 2025 distribution with the same
programs. Run these commands from the repository root, regardless of where
the checkout is located:

```sh
bash scripts/setup-texlive.sh
bash scripts/validate-manuscript.sh
```

## Codex cloud

Select this repository at `main`. The cloud environment's installation script
can be kept short because the actual setup is versioned here:

```sh
cd /workspace/nonarchimedean-pluripotential-theory
bash scripts/setup-texlive.sh
```

Startup instructions need no service command. Use the existing checkout,
source `scripts/tex-env.sh` before manual TeX commands, and run
`bash scripts/validate-manuscript.sh` after manuscript changes. For restricted
outbound access, allow `ftp.math.utah.edu` and `www.tug.org`.

The setup installs user packages under the ignored `.texlive/` directory. It
does not need administrator access or change tracked manuscript sources.
`validate-manuscript.sh` checks the TeX input and reference graph, Chapter 72
problem inventory, reference-checker tests, and then builds the complete book
at `manuscript/book.pdf`. The book build can take a while. The audited PDF in
`output/pdf/` is a release artifact; the scripts do not replace it.

For manual TeX commands in a new shell, first run `source scripts/tex-env.sh`
from the repository root, then work in `manuscript/`. This sets the paths to
the user-installed packages. Running the setup and validation scripts again
is supported.

If a previous build stopped before a missing TeX package was installed and
`latexmk` reports an error from that previous run without compiling again,
clear its generated build state with `(cd manuscript && latexmk -C book.tex)`
and rerun the validation script.
