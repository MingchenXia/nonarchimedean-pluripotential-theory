# Packet manifest

Current exact packet: `revised1/statement.tex`, `revised1/proof.tex`, `revised1/sources.bib`.

The initial root-level `statement.tex` and `proof.tex` are preserved as historical frozen bytes. `revised1` changes only typesetting: removes the optional new theorem title, converts 22 bracketed source references to proper citation commands, uses roman differential notation, and adjusts the source-interface comment. The mathematical content is unchanged.

```text
4d997e024fa7ec642299a0d86ae1d9b9d06c6041f7f10b694369d7faa458d28c  revised1/statement.tex
c7a2a08ad4ad82df4470004d01fa131fecdc01ab03f60eefa67bbe7eaa8f0a5a  revised1/proof.tex
e13ee7ebd05a7d11fe483f0906dd7c3119e0b4b97e52e3275fb6e886852f07c3  revised1/sources.bib
d6b9c9cbcd5edacfe33d568d7479e02f9c726f9c505c51b266e05fe2b461642e  AUDIT.md
423a49e9ecd0e5b9ab8997b833d04c4a3dae9faa21d5d6b442d5cee515767020  SOURCE_INTERFACE.md
```

Source evidence and the exact source-interface conflict are in `SOURCE_INTERFACE.md`; the interpretation and scope are in `AUDIT.md`.

Local typesetting check: `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build compile_check.tex`, run from `revised1`, completed successfully. The final TeX and BibTeX logs contain no warnings, undefined citations, undefined references, or overfull/underfull boxes. All four rendered pages were visually inspected. The wrapper and build products are diagnostic artifacts, not a mathematical verifier result.

Theorem/proof bytes were rehashed after the build and retain the listed values. An independent mathematical recheck of the exact `revised1` bytes and a successful strict production verification remain required. This agent did not submit either version. No live manuscript or live bibliography was changed.
