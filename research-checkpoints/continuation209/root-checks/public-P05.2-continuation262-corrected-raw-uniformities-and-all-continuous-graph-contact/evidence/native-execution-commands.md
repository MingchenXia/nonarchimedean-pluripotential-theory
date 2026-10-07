# Commands and observed environment

All writes are in the supplied artifact workspace. Existing Python 3.12.14,
pdflatex, pandoc, pdftoppm and pdftotext were used; executable paths are in
`evidence/environment.json`. No installation or resource-heavy computation
was performed. No supervised compute facility or runtime model switch was
exposed, and none is claimed. There were no account, environment, proxy,
certificate, runtime or sandbox changes, external communications, protected
source edits, private-stream reads or other-campaign inspection.

The following are the reproducible main commands, run from this directory:

```
python prepare_inputs.py
python check_certificates.py
python rebuild_paper.py
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
python build_artifacts.py
```

`prepare_inputs.py` verifies byte-for-byte preservation of all 22 supplied
delimited bodies, including all three grant clarification blocks, and hashes
the four read-only original primary files. Its manifest hashes the actual
supplied bodies, not historical hashes embedded within failed records.
An initially omitted extraction of the R230 clarification block was added
during the final binding audit; the original input and other bodies were
unchanged.

`check_certificates.py` reads `certificate-input.json` and writes the exact
finite results in `evidence/certificate-output.json`; actual stdout is in
`evidence/certificate-output.log`. Its enumerations are only the specified
finite lists. They do not certify a continuum proof. A first checker failure
is retained as `evidence/check-failure-1.log`. The wall classifier was corrected
to discard a sampled equality interval when its active gradients do not have
a common tangent slope: intersection at one point with an unrelated wall
does not make the potential equality interval a wall. The instrumented
`evidence/diagnostic-checker.py` is a reconstructed diagnostic version, not a
claim to retain exact historical program bytes.

`rebuild_paper.py` starts with the unchanged supplied whole255 source and
produces a new complete standalone TeX file. It replaces the false completion
guarantee with the full corrected proof and adds the all-continuous graph
sector. The failed source is never edited. Five successful LaTeX passes are
retained as `evidence/latex-pass1.log` through `latex-pass5.log`; the final
pass produced 27 pages and reported no warning or overflowing box. The build
bindings script checks the current PDF, whole converted argument, proof-unit
counts, local support ordering and exact preservation manifests.

Complete pertinent primary units were read directly from the frozen text
files using `sed` and located using `rg`; the exact unit coverage and every
application are recorded in `source-application-ledger.md`. Rendered BMPS
PDF page 15 and BBGS publisher page 1642 (PDF page 12) were inspected using
the existing pdftoppm/view-image tools, and the resulting images are retained
in `evidence/`. They were not republished primary files. No network retrieval
was needed.

Successful execution, compilation, hashes and finite certificate checks are
reproducibility observations, not mathematical correctness or acceptance.
The entire original P05.2 remains open and candidate is false.
