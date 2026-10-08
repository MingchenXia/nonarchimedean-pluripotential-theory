# Original P12.2 research234 deliverable

Original OPEN. Candidate=false. This is an unverified mathematical draft with new full smooth and continuous conductor results and an explicit non-isolated raw-cone separation example.

Read P12.2-paper.tex or build/P12.2-paper.pdf (the standalone paper), argument.md (complete proofs), native-notes.json (the proof-bearing local support graph), source-application-ledger.md, scope-and-gaps.md, and whole-proof-coverage.md. The source ledger gives exact frozen BFJ identities, immediate units, application hypotheses, and exclusions. No prior proposal or execution result is a correctness grant.

Rerun in this directory, in order:

```
python3 inspect_inputs.py
python3 check_exact.py
python3 make_delivery.py
python3 build_and_report.py
python3 verify_delivery.py
```

The programs use only Python's standard library and installed pdftotext/pdflatex. Compilation has explicit `-no-shell-escape`. No network, supplied scripts, external provider, agents, or heavy computation is used. The exact checker enumerates only the stated small finite diagnostic grid. Immutable source paths remain in reports/input-hashes.json; they must exist to rerun input verification/extraction. Paper generation and compilation need only the fresh local note files and installed programs.

Reports retain environment/version details, source extraction argv, all 24 bound file hash matches, exact finite checks, initial build warnings and subsequent build history, final structural verification, and own artifact hashes. The hash manifest excludes itself. A residual underfull paragraph warning is disclosed in final-verification.json; the final PDF has no overfull text-box warning. No backend model certificate or mathematical acceptance is asserted.
