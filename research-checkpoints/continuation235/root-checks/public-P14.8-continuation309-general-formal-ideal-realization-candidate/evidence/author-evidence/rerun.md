# Rerun the author's bounded work

Run each command independently from this artifact directory. They execute only inspected fresh author programs. Original bound sources are expected at the immutable paths recorded in source-inventory.json. Python 3 and local pdflatex are used; no network or shell escape is needed.

```bash
python archive_and_inventory.py
python verify_examples.py
python build_and_check.py
python bind_artifacts.py
```

For a specific source range, for example the final DPS proof unit:

```bash
python read_bound.py dps 736 775
```

The reader retains literal LF/form-feed records and appends a local extraction log. Large combined outputs should be avoided; the sourcecoverage table gives the already inspected bounded chunks. Long quoted sources remain local.

build_and_check.py inspects the self-contained author TeX, emits a complete source-derived Markdown copy, and runs pdflatex with `-no-shell-escape -interaction=nonstopmode -halt-on-error`. It repeats at most three times to resolve references. The initial build warnings and inventory failure are retained separately; rerunning overwrites current receipts but not those initial diagnostic files. The PDF may acquire new creation metadata on recompilation, so hashes bind the actual delivered bytes rather than promise time-independent binary identity. Exact example-output.json is deterministic for example-input.json.

No continuum proof is delegated to a program. Source application scopes, mathematical imports and limits are in source-application-ledger.md; sourcecoverage.md documents the actual bounded reading. environment.json records the bounded observed tools and Python/platform details without inspecting private configuration. No supervised compute facility is needed for this workload.
