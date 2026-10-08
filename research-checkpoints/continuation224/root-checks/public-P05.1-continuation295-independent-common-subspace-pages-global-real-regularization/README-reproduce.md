# Reproduction

Work in this artifact directory. The supplied packets and their enumerated files are inputs only. Never execute any supplied emitter, orchestration, binding, mutation or reproduction program. The following programs are our own small inspected programs. They use Python's standard library, local TeX, and local Pandoc, with fixed subprocess argument arrays and shell escape disabled.

```bash
python3 audit_inputs.py
python3 make_ledger.py
python3 exact_checks.py
python3 build_paper.py
python3 make_native_notes.py
python3 bind_artifacts.py
python3 validate_delivery.py
```

The first command verifies the immutable 25 mathematical entries and four primary byte objects, the whole mathematical read coverage, and records the LF convention and environment. It does not execute source data. The second generates the quote-free source application ledger from metadata and our own analysis. The third enumerates only the finite grids/word lists in exact-check-input.json. The fourth performs three no-shell-escape TeX passes and converts our own TeX to the full argument.md. The fifth writes the authoritative structured notes. The sixth binds the produced artifacts without a circular self-hash. The seventh checks required files, bindings, section conversion coverage and final build diagnostics. Bindings describe the saved run: rebuilt PDFs and logs may have different timestamps; mathematical inputs and deterministic exact-check output remain reproducible.

The saved exact-check-output.txt is the stdout of `python3 exact_checks.py`. The saved build-output.txt is the stdout of `python3 build_paper.py`; every TeX pass has separate stdout, stderr and full log files. audit-inputs-output.txt and source-ledger-output.txt retain their own command output. The initial failing input and failure logs, and the intermediate layout/reference-warning logs, are separately retained. Do not overwrite those historical diagnostic artifacts when reproducing.

To inspect a bound mathematical object in a small chunk, the own reader's syntax is `python3 read_bound.py math INDEX START STOP`. The character interval is half-open, at most 28,000 characters, and each read verifies its hash. Output containing third-party passages must remain LOCALONLY; for new local inspection redirect it into a LOCALONLY directory. Public source metadata and own analysis are in source-application-ledger.md. LF ranges split only at newline; a PDF form-feed is not an extra LF.

The environment recorded Python 3.12.14, pdfTeX 1.40.26 (TeX Live 2025/dev/Debian), and Pandoc 3.1.11.1. No external package install, network access, nested agent/provider, or heavy compute is needed. No supervised heavy-compute facility was exposed. The model label requested by the operator is not independently observable through this audit.

P05.1-paper.tex and its 14-page PDF are the paper; argument.md is the full source-to-Markdown proof. proof-source-coverage.md maps all obligations. scope-and-gaps.md states the exact conditional claim and exclusions. source-application-ledger.md records all six whole grants, their clarifications and the sole four primary bytes/units. native-notes.json is intended to be byte-content-equivalent after JSON parsing to the final structured response. Candidate is false; original P05.1/P05.2 remain OPEN. Checks and compilation are finite execution evidence, not mathematical verification or independent acceptance.
