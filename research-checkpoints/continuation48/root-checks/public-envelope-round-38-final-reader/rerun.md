# Rerun commands

Run these commands in the supplied fresh artifact workspace. They write only here and read only this workspace and the five named public source caches. No installation or worker service is needed.

```bash
python3 checks/refresh_sources.py
python3 checks/render_sources.py
python3 checks/finite_graph.py
python3 checks/build.py
python3 checks/package_notes.py
python3 checks/check_artifacts.py
```

The last build script runs the following actual commands sequentially:

```bash
python3 build-paper.py
pdflatex -interaction=nonstopmode -halt-on-error P03.3-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error P03.3-paper.tex
```

Both complete stdout/stderr build logs are retained in checks. The final paper source is standalone and includes every part of the new argument. The optional finite graph program uses standard-library exact fractions and enumerates active constraints in three tiny graphs, without numerical solvers or analytic-space simulation. There is no resource-heavy computation.

input.json is unchanged. input-original.json is an exact byte copy; assignment-original.txt and task-original.json preserve the supplied assignment and task. environment.json records Python, compiler paths and platform. It makes no unverified assertion about runtime model routing.

The note proofs are drafts. Successful programs, PDF rendering, hashes and TeX compilation do not certify their mathematics.
