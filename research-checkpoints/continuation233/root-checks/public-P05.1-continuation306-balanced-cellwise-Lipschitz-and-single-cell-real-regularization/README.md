# Scoped P05.1 verification artifacts

The substantial paper is `P05.1-paper.tex` and its built PDF is `P05.1-paper.pdf`. The author-maintained mathematical text is `argument.md`. `source-application-ledger.md` records the four original primary identities, exact immediate units and metric/sign/category restrictions, and the six whole qualified grant packets. `scope-and-gaps.md` preserves the full original OPEN objectives and the all-face compatibility gap. `native-notes.json` is the saved expanded draft note set; it is not asserted to be byte-identical to the actual native final response. All notes and the paper keep candidate=false.

Rerun from this directory, without installing dependencies or modifying the supplied sources:

```text
python code/audit_inputs.py
python code/checks.py
python code/build.py
pdftotext -layout P05.1-paper.pdf reports/paper-extracted.txt
python code/make_notes.py
python code/validate.py --skip-binding --save-report
python code/bind_artifacts.py
python code/validate.py
```

The audit reads only the two supplied manifests and their bound files. It verifies all 28 mathematical packet hashes and all four primary hashes, and checks the union of recorded whole-packet read ranges. The four original PDF/text pairs are not copied into this artifact directory. Literal LF, not `splitlines()` formfeed counting, supplies the recorded unit bounds. A source excerpt can be redisplayed in a bounded chunk, for example `python code/read_bound.py primary 3 604 670 --lf`; the output is a local-only source excerpt, not public paper content. `reports/read-command-list.txt` gives the recorded reader commands.

The exact-arithmetic checks use `inputs/check-input.json`. Their detailed output is `reports/exact-checks.json`: 578 two-direction star tests, 121 distance tests, four unbounded-face inset examples, one saturated covolume identity, eleven dyadic inequalities, 67 exact primal-irrational-height comparisons, and seven orthant limiting-inequality illustrations. These are finite checks with explicitly limited domains, not continuum proofs or mathematical acceptance. The primal example uses exact signs in Q(sqrt(2)); the paper separately proves its error bound on the whole real line.

The build uses Pandoc and `pdflatex -no-shell-escape`, through argument-list subprocess calls without a shell. Each new run gets a new `build/run-NNN` directory. The first logs and their warnings remain in `build/`; the initial TeX is `build/initial-paper.tex`. New source snapshots and logs are retained per run. `reports/build-report.json` records hashes before/after unchanged TeX compilation, commands, warning records and result. PDF creation timestamps can change on rerun even when the source is unchanged. `reports/environment.json` records only ordinary tool/platform versions; it does not expose authentication or runtime configuration or certify the underlying model identity.

The input task is preserved unchanged in `inputs/retained-task.json`. `reports/proof-coverage.json` lists all 14 working units and their proof locations. `artifact-bindings.json` hashes all own retained files except itself; no self-hash is claimed. The binding code is our fresh program, not a supplied binder. All program execution is local and bounded. No network, agent, nested provider, heavy compute or supplied runner is used.

The proofs establish the finite balanced cellwise Lipschitz/support assertion, the exact single-cell real majorants, and the sharp unbalanced orthant diagnostic as draft scoped theorems. They do not establish arbitrary all-face compatible global regularization. Original P05.1/P05.2 remain OPEN.
