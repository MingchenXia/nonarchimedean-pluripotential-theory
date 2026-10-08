# Reproducible unreviewed paper

Read `P05.1-paper.tex` or `P05.1-paper.pdf` for the complete mathematical paper. `argument.md` contains the entire source-derived body and proofs. `source-application-ledger.md` maps every assigned working unit and every original primary unit. `scope-and-gaps.md` states the excluded hypotheses and precise remaining original-classification gap. `native-notes.json` is the saved final draft-note payload, with candidate=false.

All commands run from this directory. Only the fresh programs below are executed. The frozen supplied source programs are never executed.

```bash
python3 audit_inputs.py > source-audit.log 2>&1
python3 exact_checks.py > exact-checks.log 2>&1
python3 make_argument.py
python3 build.py > build-rerun-driver.log 2>&1
python3 bind_artifacts.py
python3 verify_delivery.py
```

Requirements: Python3 standard library and the already-installed pdfLaTeX engine. No package installation, network, service, agents, or heavy computation is required. If TeX is unavailable, the TeX and Markdown proofs remain readable; the build is then reported as unavailable, not as mathematical failure. The current build used pdfTeX 1.40.26, TeX Live 2025/dev/Debian, with shell escape disabled. Python arithmetic checks use `fractions.Fraction` without a floating-point solver.

`build.py` preserves every prior build report and pass log in numbered history directories before a rerun. Initial cross-reference warnings and the nonmutating patch-context failure are recorded in `execution-history.md`. `exact-output.json` contains all finite LP and sharp-family records. The exact run has 1,577 assertions and PCC cost −1/4, exhaustive for the explicitly stated finite lists only. The continuum theorems are proved in the paper, not inferred from checks, metadata, or compilation.

`input-bindings.json` records all 36 task-bound inputs. `snapshot-bindings.json` binds their complete local copies in `LOCALONLY/inputs`; `audit_inputs.py` falls back to those copies if the original packet is unavailable. These input files are never executed. `whole-read-coverage.jsonl` and `primary-read-coverage.jsonl` bind the bounded source reads, including repaired truncation. Literal LF means `text.split('\n')`; formfeeds do not introduce LF positions. `LOCALONLY` holds primary excerpts and input copies; keep these local. No whole-PDF visual reading or historical execution is asserted.

`artifact-bindings.json` hashes the delivered files without recursively hashing itself. Regeneration updates the Markdown source hash, the final PDF copy, and bindings. Repeated build artifacts are evidence of presentation only. New notes and this manuscript have no automatic acceptance. Original P05.1/P05.2 remain OPEN.
