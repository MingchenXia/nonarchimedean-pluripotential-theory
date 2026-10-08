# Local deliverable

P12.6-paper.tex is the standalone typeset source, containing all new proofs and literal qualified grant components. Compilation was not run. ROOT/operator handles the compiler.

argument.md and native-notes.json contain the complete expanded new proof chain. The source ledger, exact scope, coverage, original-scope/noncircularity decision and acceptance-decision.json distinguish scoped draft theorems from the unresolved exact original and entire family. Candidate=false.

Run from this directory:

    python audit_inputs.py
    python bounded_checks.py
    python build_delivery.py
    python final_audit.py

These are newly owned standard-library programs. They never execute or import supplied programs. The assembly performs no compilation. Reports retain exact inputs, output, environment, source paths, hashes and rerun commands. All 53 bound files matched; the bounded arithmetic diagnostic has 802 cases and zero failures. Those observations do not establish mathematical correctness.

No external source, source pixels, catalogue or publication was produced. No subagent, extra native job, private ACTIVE252 output or heavy computation was used. No supervised heavy-compute facility was exposed or needed.
