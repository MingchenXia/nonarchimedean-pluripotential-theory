# Build and reproducibility evidence

Commands from this fresh workspace:

```bash
bash reproduce.sh
```

The script sequentially runs:

```bash
python assemble_evidence.py > evidence/assembly-output.json
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build P06.2-partial.tex > build/pass1.stdout
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build P06.2-partial.tex > build/pass2.stdout
cp build/P06.2-partial.pdf P06.2-partial.pdf
python validate_artifacts.py
```

The two full compile transcripts are retained separately, along with the final
TeX log, auxiliary file, standalone PDF and its artifact hash. The environment
is in evidence/environment.json. The schema/integrity output is in
evidence/validation-output.json and the complete local artifact manifest is in
evidence/artifact-hashes.json. The original input file and the earlier canonical
notes are preserved; immutable-source comparisons are read-only.

These checks verify exact selections, unchanged predecessor inputs, exact
five-key status, note dependencies, candidate false, a complete accessible
new proof body, and two successful PDF passes with resolved references.
They are packaging/build observations. No finite computation, source hash,
compilation, old PASS or self-audit is a mathematical correctness certificate.
No new graph enumeration is presented as an analytic theorem.

The initial validation rule incorrectly rejected expected unresolved citations
in the first TeX pass, even though both passes compiled and the second resolved
them. Its failed assertion is retained in evidence/validation-initial-failure.txt;
the rule was corrected to reject unresolved references on pass two and actual
TeX errors on either pass. The rerun starts with fresh auxiliary files, so this
normal two-pass behavior remains reproducible rather than hidden by old aux files.

All work was small local computation; no supervised compute facility was
supplied and no heavy computation was launched. No independent mathematical
verifier, extra model, subagent, network or installation was used.
