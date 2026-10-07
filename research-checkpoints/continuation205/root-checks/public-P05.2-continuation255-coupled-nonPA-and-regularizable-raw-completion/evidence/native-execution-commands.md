# Reproduction and actual execution record

Run in the supplied artifact directory, using the already installed Python, pdflatex, pandoc and PDF tools:

```sh
python check_certificates.py
python rebuild_paper.py
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
python write_notes.py
python build_artifacts.py
```

The section sources and rebuild script regenerate the current manuscript from the preserved supplied failed TeX plus explicit material replacements and added proof units. They do not edit preserved/whole247.tex. build_artifacts.py converts the full argument using pandoc, verifies all note supports refer to earlier local notes, verifies preserved-body hashes, inspects the actual PDF/log, and generates the artifact manifest. The manifest excludes itself.

Actual execution: Python extracted fourteen exact delimited supplied bodies from input.json, kept their current hashes, and checked the four frozen primary hashes. Source text was read only from the four authorized files. Original PDF pages BMPS 12 and BBGS 11 were rendered locally and viewed; actual images remain in evidence/. The complete primary proof-unit audit and exact applications are in source-application-ledger.md. No historical files named inside the supplied records were read.

The initial LaTeX compilation failed on MA_R because the existing MA macro already contained a subscript. The actual initial log was copied to evidence/latex-initial-failure.log, and the explicit operator expression corrected it. Subsequent two-pass builds succeeded. A shell command ending with rg had exit 1 because there were no warning matches; the preceding compilation itself succeeded. Final build validation records warnings and pages directly from the actual log/PDF.

The first checker failed because an axis list used generator expressions with late-bound loop variables. Immediate tuples corrected the implementation; the failure is recorded in evidence/checker-initial-failure.txt. The second checker exposed redundant central affine forms producing duplicate first walls in the generic pair enumerator; the actual stderr is retained in evidence/checker-second-failure.txt. The zero supports +/-z were removed from max(a_N+/-z, +/-2z), since they are everywhere redundant. This does not change the function or the mathematical mass formulas. The final exact checks pass, and their stdout/stderr and complete rational wall/atom output are retained. All these are reproducibility observations, not mathematical grants.

Environment details are in evidence/environment.json. No installations, account or authentication changes, proxy/CA changes, sandbox modifications, private-stream inspection, other-campaign reads, editor operations, GitHub writes or messages to others occurred. No resource-heavy computation ran, and no supervised compute facility was exposed. The requested model route was not selectable or independently verified. The managed runtime skill was read; its environment_status tool was not exposed. No network action was needed.
