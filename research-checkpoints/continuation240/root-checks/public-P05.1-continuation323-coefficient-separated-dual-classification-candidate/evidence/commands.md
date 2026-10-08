# Rerun commands and retained execution observations

All commands run in this directory with the existing environment. Only own programs are executed. No network, agent/provider delegation, supplied program, runtime/auth/account/environment modification, or protected editor operation is required.

```bash
python check_exact.py
python build_artifacts.py
pandoc -f latex -t markdown P05.1-paper.tex -o argument.md
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error P05.1-paper.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error P05.1-paper.tex
python record_provenance.py
```

The checker writes check-output.json and exhausts only its check-input.json lists. Original execution occurred once. Metadata generation can rehash inputs without mathematical review. TeX first build failure and later pass logs are retained; epstopdf's shell-escape-disabled warning is expected and no shell escape is enabled. No resource-heavy computation was needed, and no operator supervised compute service was exposed. environment.json records tool versions without credentials/proxy/CA values. Model/effort and universal past operations are not independently certified.

Controller and input byte bindings establish identity only. final-notes.json is the canonical prepared structured content issued in the FINAL response; final-note-bindings.json binds its fields and whole UTF-8 serialization. No unavailable provider-envelope byte capture or later saved-expansion identity is fabricated. Any downstream exact native FINAL byte capture must be bound separately by that downstream reader.
