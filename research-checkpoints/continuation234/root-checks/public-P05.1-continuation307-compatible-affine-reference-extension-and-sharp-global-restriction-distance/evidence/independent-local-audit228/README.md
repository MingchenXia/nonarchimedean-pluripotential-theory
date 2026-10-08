# Reproduce this audit

This directory contains only fresh own audit artifacts. Supplied paper/packet bytes are unchanged. Start with audit-report.md; full proof/source/coverage/evidence reports accompany it. Mathematical DATA and primary snapshots are retained under LOCALONLY; primary text/PDF excerpts must remain local.

The executed finite checker is an inspected exact copy in finite-check/, run once with its original281-byte input. EXECONCE guards prevent accidental reruns. The two-pass unchanged build is in fresh-build/, with full warning logs. No supplied builder/emitter/auditor/binder/ROOT helper was executed.

Commands already used:

```
python audit_io.py bindings
python audit_io.py decode
python audit_io.py read m 4 1 85  # remaining exact ranges in own-read-displays.jsonl
python reproduce.py check       # guarded; already executed exactly once
python reproduce.py build       # guarded; already executed two passes
python reproduce.py presentation
python collect_records.py
python finalize_records.py
```

For a new checker/build reproduction, create a NEW own scratch directory, copy the already inspected finite code/input and unchanged TeX, and run the recorded argv there. Keep previous records and execution guards. Boundaries: nine unreviewed mathematics, own evidence, sole four primaries and original task only; no absent grant bodies or unbound native/private material. No network, agents or heavy compute is needed. No supervised compute facility was provided.

candidate=false; original P05.1/P05.2 OPEN. Finite execution and compilation success are separate from unverified mathematical correctness.
