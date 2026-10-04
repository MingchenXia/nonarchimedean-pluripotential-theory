The deliverable is a partial mathematical result for P16.6. Read [P16.6-argument.md](P16.6-argument.md) or [P16.6-paper.pdf](P16.6-paper.pdf). It gives an arbitrary-support finite-energy theorem in arbitrary dimension separately at the trivial characteristic-zero and discrete residue-characteristic-zero endpoints. The general complete-field residual scope remains unproved; `candidate=false`.

To reproduce using only the ten supplied source caches and existing tools:

```sh
python3 audit_sources.py > source-audit-output.txt 2>&1
python3 build_artifacts.py > build-output.txt 2>&1
python3 verify_artifacts.py > verification-output.txt 2>&1
```

`build_artifacts.py` generates the standalone TeX file from the full Markdown argument, renders four actual source-PDF pages, refreshes source provenance, and executes `pdflatex` twice. The two final actual stdout/stderr streams and TeX logs are in `build/pass1` and `build/pass2`. `build/build-report.json` preserves commands, exit codes, hashes and warnings. Earlier build attempts are archived rather than presented as final checks. The initial failure was an undeclared `mathscr` command; the final preamble uses the already installed `mathrsfs` package.

`source-extracts/source-provenance.json` records exact supplied versions and hashes, literal published proof extracts, application checks, limitations and actual-PDF inspection records. The sign slip in the PDF statement of BFJ v1 Lemma 6.10 is handled by the directly proved integrability bound (7a)--(7b), not silently corrected in a quotation. The synthetic estimate (2.27) has absolute-value bars in the actual PDF.

`input.json` and `input-original.json` are byte-identical. `assignment-original.txt` and `task-original.json` preserve the decoded input. `status.json` has exactly the five requested keys. `notes.json` contains the four canonical notes and the false candidate flag. `environment.json`, `checks.json`, and `artifact-manifest.json` record reproducibility information. No heavy compute service, external model, worker, subagent, network fetch, installation or external message was used.

These checks establish source identity and artifact reproducibility. They are not a proof checker and do not validate the mathematics.
