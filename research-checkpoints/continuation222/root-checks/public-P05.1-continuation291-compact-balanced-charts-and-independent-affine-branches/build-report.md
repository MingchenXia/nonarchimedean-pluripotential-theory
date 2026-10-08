The local two-pass `pdflatex -no-shell-escape` build and Markdown rendering completed successfully. `evidence/build-report.json` records exact argument arrays, exit codes, logs, visible tool paths and identical source hashes before/after. `P05.1-paper.pdf` is a review artifact, not proof certification.

Initial cross-reference warnings resolved on the second pass. A long filename caused one initial overfull box, corrected in the source before the final build. The disabled-shell-escape epstopdf warning is expected and retained; no shell escape was enabled. The initial report and logs remain separate. See `logs/diagnostics.md` for the exact-arithmetic diagnostic correction.

Rerun from this directory:

```
python code/audit_inputs.py
python code/exact_checks.py > logs/exact-checks.log
python code/build.py
python code/make_notes.py
python code/bind_artifacts.py
```

The input audit checks 37 bound packet/primary identities. Exact arithmetic uses small declared examples only; no resource-heavy service was exposed or needed. The child's visible environment is in `evidence/environment.json`. It does not independently certify the operator's requested Xean/native provider, model, reasoning setting or single-call configuration. No provider/model changes were requested or made, no nested agents/providers were used, and no source/editor state was changed.
