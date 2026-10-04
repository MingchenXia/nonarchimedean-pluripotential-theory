This directory contains fresh work for P02.2. The full characterization is unresolved; see `status.json` and `P02.2-argument.md` for exact scope.

Rerun, in order, with the existing Python and TeX environment:

```
python collect_sources.py
python finite_diagnostics.py > finite-diagnostics.stdout.txt
python build_documents.py > tex-build.stdout.txt
python verify_artifacts.py > artifact-validation.stdout.txt
```

`build_documents.py` generates standalone `P02.2-paper.tex` embedding the entire Markdown argument and executes pdflatex twice. Individual stdout and log files, as well as structured diagnostics, are retained. No installation or heavy computation is used. Public cache PDFs are read-only. Selected primary pages, cache text, hashes and application checks are in `source-extracts/`. No execution check certifies the mathematics.
