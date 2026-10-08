# Execution record and reproducibility

Only the bound mathematical and original-primary inputs and this author's own fresh artifacts were read. All writes are in this artifact directory. The source directories and binding manifests were unchanged. No supplied executable was run. The own readers, exact checker, build wrapper and audit wrapper are ordinary inspected standard-library programs; they do not invoke a shell for TeX/Pandoc. No network, nested provider, agent, source mutation, heavy computation, auth/runtime/account/HOME/CODEX_HOME/proxy/CA change or protected editor action was used.

## Initial failures and repairs retained

1. The first inline binding selection used indices 28 and 29 for a 26-entry mathematical packet. It exited 1 with `IndexError: list index out of range` (tool chunk 16cf15). Indices 24 and 25 were then used. This was a reader indexing failure, not mathematical evidence.
2. The first aggregate working294 output exceeded its 10,000-token output cap by about 53 tokens. The repair reread character interval [14000,21000). One later aggregated repair output was itself truncated by 1,523 tokens. The interval was then reread alone (chunk b7e75c), with no truncation. Entire successfully displayed intervals plus the standalone repair cover the working document. No supplied body was shortened or changed.
3. For Unicode ledger records at mathematical indices 10 and 11, byte lengths 13,611 and 4,987 were incorrectly used as Python character lengths. Reader assertions failed (chunk 0ed52a). A second attempt incorrectly used 13,557 and 4,975 despite the measured lengths (chunk fb632b). The true character lengths 13,499 and 4,963 were finally used and passed (chunk c569dc). The own reader source was unchanged throughout. All successful coverage entries contain both characters and LF coordinates. These failed attempts did not read unbound files or mutate inputs.
4. First own TeX compilation returned 0 but had undefined-reference/rerun warnings. Second returned 0 with one rerun warning. A third unchanged-source pass returned 0 with no warning, overfull or underfull box report. All three stdout/stderr/engine logs are retained. The TeX source hash stayed `738b023af49002450cac0a3df5aa2a62fc1a3e21ff750b2aa572cfb141647603` across these passes. Build success is not mathematical correctness.

The earlier reader failures were emitted by native tools before this prose record was made; their chunk identifiers and error text are historical observations, not reconstructed raw stderr captures. Successful bounded read intervals are mechanically logged. No unavailable native transcript file is claimed.

## Own exact execution

`python check_exact.py > exact-check.stdout.log 2> exact-check.stderr.log` returned 0. The checker uses only Python Fraction, exact Gaussian elimination, bounded determinant expansion and elementary integer Euclidean operations. Its stdout is the JSON also saved as `exact-output.json`; stderr is empty. It finds the diagnostic's eight dual epigraph vertices from all 35 triples, checks the full trace comparison certificate and all listed rational incidences/lattices, then checks 26,961 rational dependent-model tuples, 33 trace points including both dual boundary endpoints, and 44 ordered products in six fixed matrices. Its exact outputs are separately reported in the notes. There is no numerical tolerance or solver. These finite domains alone are exhaustive.

`python build_paper.py` ran fixed argv arrays for Pandoc and the first two no-shell-escape TeX passes, with captured stdout/stderr; a separate fixed-array subprocess ran the third pass and appended its report. Pandoc returned 0 with no warning. Final TeX output is 18 pages, 343,812 bytes. The source remained unchanged. The invocation used `/usr/bin/pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error P05.1-paper.tex`. No supplied build or emitter was executed. Only own source and tools were used.

The revised own build wrapper was then exercised once. It wrote `build-rerun-1/` plus wrapper stdout/stderr, preserved `initial-build/`, kept the TeX source unchanged and completed Pandoc plus three warning-free passes. This extra build verifies the changed wrapper's log-preservation behavior; it is not additional mathematical evidence.

The observed environment is Python 3.12.14 (Clang 22.1.3), Linux x86_64 with glibc 2.41, pdfTeX 1.40.26 (TeX Live 2025/dev/Debian) and Pandoc 3.1.11.1. Full observed version lines and executable paths are saved in `environment.json`. No OpenAI runtime/model introspection or independent effort attestation was available. The caller requested one native Codex gpt-6.1-sol xhigh author call; this author neither switched models nor claims independent configuration certification.

## Rerun commands

Run from this artifact directory. The own audit verifies original hashes, whole mathematical coverage, complete essential original-unit ranges, exact finite output constraints, source-to-Markdown regeneration and saved note supports. It is not a theorem prover.

```text
python audit_artifacts.py
python check_exact.py
python build_paper.py
python audit_artifacts.py
```

The build wrapper preserves first-run logs in an immutable-by-convention archive and sends any later build logs to numbered rerun directories. It uses three unchanged-source TeX passes on future reruns. Alternatively run Pandoc followed by three explicit no-shell-escape TeX invocations. Those commands are recorded in `commands.json` together with every logged successful bounded read argv. Public artifact bindings contain only filenames, bytes and hashes. Long source extracts remain LOCALONLY.

No resource-heavy computation was needed. No supervised heavy-compute facility was exposed, and none was launched locally. The saved `native-notes.json` is the unverified author draft; native FINAL is issued separately. Semantic disposition is the same but no byte-for-byte native FINAL capture is available or claimed. Exactly six whole grant premises, historical INCONCLUSIVE distinctions, OPEN original classifications and candidate=false remain.
