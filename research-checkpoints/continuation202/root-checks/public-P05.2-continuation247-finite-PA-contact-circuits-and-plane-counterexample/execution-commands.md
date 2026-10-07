# Actual execution and rerun commands

Work was confined to the artifact workspace. The four authorized frozen primary files were read from the exact read-only paths in the task. No installation, network or authentication modification, model switch, protected-file edit, or resource-heavy computation occurred.

Environment and actual four-file hashes: evidence/environment.json and evidence/primary-provenance.json.

Actual implementation runs:

    python prepare_inputs.py > evidence/preparation-output.json
    python check_certificates.py > evidence/certificate-stdout.json
    pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex

The check program was rerun after correcting a metadata bound from floating-point formatting to an exact Fraction and adding two oblique saturated-covolume tests. Every final assertion passed. The final paper was compiled twice after layout fixes; logs are evidence/latex-pass3.txt and evidence/latex-pass4.txt. The last build produced a 10-page PDF, with no reported warnings or overflowing boxes. An initial compile failed on a double-subscript macro, which was corrected to a separate operator macro; subsequent builds succeeded. The complete initial failing log was overwritten, so only this observed diagnostic is preserved, not a purported original full log.

Primary audit commands included rg searches and sed line ranges listed in source-application-ledger.md, plus:

    pdftoppm -f 15 -l 17 -r 85 -png <frozen-prefix>/BMPS.pdf evidence/BMPS
    pdftoppm -f 27 -l 27 -r 90 -png <frozen-prefix>/BMPS.pdf evidence/BMPS
    pdftoppm -f 12 -l 13 -r 100 -png <frozen-prefix>/BBGS.pdf evidence/BBGS
    pdftoppm -f 9 -l 11 -r 90 -png <frozen-prefix>/BBGS.pdf evidence/BBGS

The prefix denotes the literal read-only prefix recorded in the source ledger, not an alternate source. Original rendered pages were viewed through the local image tool.

Rerun from this directory:

    python prepare_inputs.py
    python check_certificates.py
    pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
    python build_artifacts.py

The last script creates the complete Markdown argument, structured notes and artifact manifest. Execution success and compilation establish reproducibility observations, not mathematical correctness.
