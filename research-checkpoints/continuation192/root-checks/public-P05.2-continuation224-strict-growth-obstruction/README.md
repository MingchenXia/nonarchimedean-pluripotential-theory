# P05.2 research deliverable

The independently proved result is an exact noncontact envelope on the U(3,4) Bergman fan with a strictly convex positive-at-infinity reference. For the integral example Gamma=h and U=2u_epsilon, the genuine PA endpoint has raw masses 4,3,3, degree ten, and contact integral -4 epsilon. The original classification is still open; candidate=false.

- P05.2-paper.tex and P05.2-paper.pdf: standalone manuscript.
- argument.md: full arguments, hypotheses, limitations, failed approaches, and reproduction details.
- source-application-ledger.md: quote-free exact-version applications and retrieval limitations.
- execution-requests.md: actual source queries and local commands, including the failed retrieval and initial compilation.
- structured-notes.json: local registered notes and supportingNoteIds.
- check_obstruction.py and obstruction-input.json: exact finite arithmetic checks.
- evidence/check-output.json and evidence/environment.json: output and environment.
- source_provenance.py and evidence/source-provenance.json: actual retained-file hashes and complete source-unit coverage.
- sources/: actual saved retrieval text responses; no original PDF byte stream was acquired.

Rerun from this directory:

```sh
python check_obstruction.py
python source_provenance.py
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex
```

No installations or resource-heavy computation were used. Execution success does not establish mathematical correctness; these are unverified research drafts. The parent handles external checkpoints and acceptance.
