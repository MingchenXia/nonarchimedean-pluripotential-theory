# Reproduction and limits

The requested whole audit is incomplete. Read audit-report.md for the separate INCONCLUSIVE verdicts and explicit missing-body list. No original problem is closed. All own findings are saved in native-notes.json with candidate=false and valid earlier local supports.

Read-only input hash audit: `python3 audit_io.py init`.

Own displayed-read coverage: `python3 finalize_coverage.py`. This distinguishes byte hashes, structural parsing, bounded displayed text and whole-body examination. It does not certify historical universal reading.

Own historical comparisons and saved-log diagnostics: `python3 history_check.py`.

The inspected safe checker/input and unchanged TeX were prepared with `python3 reproduce.py --prepare`, inspected, then run with `python3 reproduce.py`. The checker ran exactly once. The driver refuses to repeat or overwrite the saved run. For a fresh rerun, copy OWN reproduce.py and frozen-bindings.json to a new fresh writable directory and invoke those two commands there. Do not execute any supplied emitters/auditors/builders/orchestrators/binders. The only supplied executable allowed by this driver is the previously fully inspected small bounded arithmetic copy. Its input, source and stdout/stderr are in own-scratch.

The driver runs three `pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error P05.1-paper.tex` passes; `pandoc P05.1-paper.tex --from=latex --to=gfm --standalone --output=argument.md`; and `pdfinfo P05.1-paper.pdf`. It uses argument arrays, no shell and no environment changes. All commands, exits, versions and output hashes are in own-build-finite-records.json; all fresh stdout/stderr and pass-specific TeX logs are retained.

Own note regeneration: `python3 write_notes.py`. Own validation and artifact binding: `python3 validate_own.py`. These are fresh own bookkeeping programs, not supplied emitters or automatic acceptance routines.

No primary long passages or pixels are republished in these public artifacts. PDF inputs are hash-verified and text original immediate units are displayed locally. Finite checks and build success do not prove continuum claims. The coordinate checker assigns its coordinate-model word terms rather than implementing an arbitrary saturated-lattice recursion. A historical initial-source reconstruction is not a captured initial hash. No supervised heavy-compute service was provided or used.
