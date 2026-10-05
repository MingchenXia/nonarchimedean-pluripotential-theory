The unchanged original P16.1 is not solved. `canonical-notes.json` registers four unverified native proof notes and sets `candidate=false`. `status.json` records the precise remaining C1 hypothesis. The standalone argument is `P16.1-paper.pdf`, with source `argument.md` and generated `P16.1-paper.tex`.

The draft proves M1–M3, all-point resolved-nef fiber constancy and the original-reference contact application using the actual varying-class definitions. Arbitrary-cardinality envelope descent, normalization/E1/product transport and the actual variational equation are conditional on the explicitly stated countable original-class weak-to-genuine global C1. No independent Runge result is assumed.

Run from this directory:

```
python3 rerun.py
python3 validate.py
```

Reproduction is offline and uses retained primary inputs and installed Pandoc/pdfTeX. `commands.json`, `environment-rerun.json`, `logs/` and `artifact-manifest.json` record exact execution and hashes. Both pdfLaTeX pass logs are retained. The initial failed PDF build is separately preserved under `logs/failed-*`; only an appendix backslash required a typesetting correction.

`input-original.json` is byte-identical to the supplied input. `task-original.json` and `assignment-original.txt` retain the exact task and assignment. `source-files.json` verifies the 23 supplied primary files. `premises.json` has nonnegative external premise indices and complete passage coverage. `source-extracts/source-provenance.json` contains exact versions, hashes, literal units and inclusive one-based LF coordinates computed by UTF8 byte decode and `split('\n')`. Public web snapshot hashes are text hashes, not PDF hashes. All retrieved evidence, including failed or unrelated retrieval diagnostics, remains in `evidence/`.

The 1,339 finite rational cases check only the declared graph/arithmetic grids; they do not verify model hypotheses or mathematical correctness. No resource-heavy computation or other worker/model was used. Compilation, hashes and consistency checks are documentary observations, not mathematical proof certificates.
