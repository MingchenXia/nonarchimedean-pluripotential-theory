# Scoped common-H real regularization paper

The own manuscript is [P05.1-paper.pdf](P05.1-paper.pdf) (18 pages), with source [P05.1-paper.tex](P05.1-paper.tex) and generated [argument.md](argument.md). It reconstructs the whole common-H dependent-page theorem, embedded full-affine foundation and exact diagnostic. This is an unverified author draft, not independent acceptance. Candidate=false; original P05.1/P05.2 remain OPEN.

Review [source-application-ledger.md](source-application-ledger.md), [scope-and-gaps.md](scope-and-gaps.md), [proof-source-coverage.md](proof-source-coverage.md), [execution-record.md](execution-record.md), and [native-notes.json](native-notes.json). Bindings and successful interval coverage identify inputs and artifacts; they do not establish mathematical correctness. Long primary extracts remain LOCALONLY.

From this directory rerun:

```text
python audit_artifacts.py
python check_exact.py
python build_paper.py
python audit_artifacts.py
```

Exact checking exhausts only the specified finite lists. Initial failures and first-pass warnings are retained. The build wrapper preserves initial logs and writes later build logs to numbered rerun directories, uses fixed arguments, disables TeX shell escape and verifies unchanged source. No network, supplied executable, nested agent/provider or heavy compute is required.
